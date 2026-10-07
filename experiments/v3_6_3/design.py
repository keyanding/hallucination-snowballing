"""Frozen two-hop templates, lexical cases and strict state forwarding."""
import random
import re
from experiments.v3_6_1.design import sha,token_info,normalize

CONDITIONS=('U-GOLD','U-ALT','P-GOLD','P-ALT')
UP_CATS=('B','Bp','OTHER_STATE','INVALID')
DOWN_CATS=('C','Cp','OTHER_OUTCOME','UNKNOWN','INVALID')


def parse(raw,c,upstream=False,truncated=False):
    v=normalize(raw)
    if truncated:
        cat='INVALID'
    elif upstream:
        cat='B' if v==c['gold_state'] else 'Bp' if v==c['alt_state'] else 'OTHER_STATE' if re.fullmatch(r'STATE_[A-Z][0-9]{2}',v) else 'INVALID'
    else:
        cat='C' if v==c['gold_outcome'] else 'Cp' if v==c['alt_outcome'] else 'UNKNOWN' if v=='UNKNOWN' else 'OTHER_OUTCOME' if re.fullmatch(r'OUTCOME_[A-Z][0-9]{2}',v) else 'INVALID'
    return dict(normalized=v,category=cat,permitted=cat in ('B','Bp') if upstream else cat in ('C','Cp'))


def render(c,condition,reverse=False,supplied=None):
    up=[(c[r+'_entity'],c[r+'_state']) for r in c['up_order']]
    down=[(c[r+'_state'],c[r+'_outcome']) for r in c['down_order']]
    if reverse:
        assert condition.startswith('U-')
        up.reverse()
    ub='\n'.join(a+' -> '+b for a,b in up)
    db='\n'.join(a+' -> '+b for a,b in down)
    role='alt' if condition.endswith('-ALT') else 'gold'
    entity=c[role+'_entity']
    if condition.startswith('U-'):
        prompt=f'Synthetic transition task.\n\nUpstream mappings:\n{ub}\n\nCurrent entity:\n{entity}\n\nReturn only the mapped state.'
        state=None
        expected=c[role+'_state']
    elif condition.startswith('I-'):
        prompt=f'Synthetic two-hop task.\n\nUpstream mappings:\n{ub}\n\nDownstream mappings:\n{db}\n\nCurrent entity:\n{entity}\n\nFollow the mappings and return only the final outcome.'
        state=None
        expected=c[role+'_outcome']
    else:
        assert condition in ('P-GOLD','P-ALT','PIPELINE-GENERATED')
        state=supplied if condition=='PIPELINE-GENERATED' else c[role+'_state']
        assert state is not None
        prompt=f'Synthetic propagation task.\n\nRecorded intermediate result:\n{state}\n\nDownstream mappings:\n{db}\n\nReturn only the outcome implied by the recorded intermediate result.'
        expected=dict(down).get(state)
        entity=None
    return dict(case_id=c['case_id'],split=c['split'],condition=condition,reverse=reverse,
                supplied_state=state,current_entity=entity,expected=expected,upstream_mappings=up if condition.startswith(('U-','I-')) else [],
                downstream_mappings=down if not condition.startswith('U-') else [],prompt=prompt,text_sha256=sha(prompt))


def audit_pair(c,prefix,reverse=False):
    a,b=(render(c,prefix+'-'+r,reverse) for r in ('GOLD','ALT'))
    marker='Recorded intermediate result:\n' if prefix=='P' else 'Current entity:\n'
    before,tail=a['prompt'].split(marker)
    value,after=tail.split('\n',1)
    key='state' if prefix=='P' else 'entity'
    assert value==c['gold_'+key]
    assert before+marker+c['alt_'+key]+'\n'+after==b['prompt']
    for r in (a,b):
        assert not re.search(r'\b(gold|alt|wrong|correct)\b',r['prompt'],re.I)
        assert 'UNKNOWN' not in r['prompt']
        assert not re.search(r'^\d+[.)] ',r['prompt'],re.M)
        if prefix=='P':
            assert 'ENTITY_' not in r['prompt'] and 'Upstream' not in r['prompt']
    return a,b


def pipeline(c,upstream_row):
    p=parse(upstream_row['raw_text'],c,True,upstream_row['truncated'])
    metadata=dict(case_id=c['case_id'],upstream_raw=upstream_row['raw_text'],upstream_normalized=p['normalized'],
                  upstream_category=p['category'],upstream_text_sha256=upstream_row['text_sha256'])
    if p['category']=='INVALID':
        return None,metadata|dict(status='UPSTREAM_INVALID_SKIPPED')
    assert re.fullmatch(r'STATE_[A-Z][0-9]{2}',p['normalized'])
    return render(c,'PIPELINE-GENERATED',supplied=p['normalized']),metadata|dict(status='CALLED_UNREPAIRED')


def make_cases(tok,old):
    pool=[role+'_'+letter+f'{n:02}' for role in ('ENTITY','STATE','OUTCOME') for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for n in range(100)]
    audit=[token_info(tok,v)|dict(eligible=v not in old) for v in pool]
    rng=random.Random(363)
    candidates={}
    for role in ('ENTITY','STATE','OUTCOME'):
        sub=[r for r in audit if r['eligible'] and r['raw'].startswith(role+'_')]
        minimum=min(r['token_count'] for r in sub)
        candidates[role]=[r['raw'] for r in sub if r['token_count']==minimum]
        rng.shuffle(candidates[role])
    used=set()
    cases=[]
    for split,n in (('calibration',20),('main',40)):
        patterns=[(a,b) for a in (0,1) for b in (0,1)]*(n//4)
        rng.shuffle(patterns)
        for i,(up,down) in enumerate(patterns,1):
            suffixes=set()
            def take(role):
                value=next(v for v in candidates[role] if v not in used and v.split('_')[-1] not in suffixes)
                used.add(value)
                suffixes.add(value.split('_')[-1])
                return value
            c=dict(case_id=f'v363-{split}-{i:03}',split=split,
                   up_order=['gold','alt'] if up==0 else ['alt','gold'],down_order=['gold','alt'] if down==0 else ['alt','gold'])
            for role in ('entity','state','outcome'):
                c['gold_'+role]=take(role.upper())
                c['alt_'+role]=take(role.upper())
            cases.append(c)
    for c in cases:
        ids=[c[r+'_'+role] for role in ('entity','state','outcome') for r in ('gold','alt')]
        assert len(set(ids))==len({v.split('_')[-1] for v in ids})==6
        assert not set(ids)&old
        for role in ('entity','state','outcome'):
            a,b=c['gold_'+role],c['alt_'+role]
            assert len(a)==len(b) and len(tok.encode(a,add_special_tokens=False))==len(tok.encode(b,add_special_tokens=False))
        assert all(a not in b for a in ids for b in ids if a!=b)
        for prefix in ('U','P','I'):
            audit_pair(c,prefix)
    assert len(used)==360
    main=cases[20:]
    selector=random.Random(364)
    integrated=[]
    for up in ('gold','alt'):
        for down in ('gold','alt'):
            integrated+=selector.sample([c['case_id'] for c in main if c['up_order'][0]==up and c['down_order'][0]==down],5)
    order=random.Random(365).sample([c['case_id'] for c in main],10)
    return cases[:20],main,integrated,order,pool,[r|dict(selected=r['raw'] in used) for r in audit]
