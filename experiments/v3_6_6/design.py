"""Prospective graph cohort, bijective identity encoding and frozen two-row routing."""
import copy
import itertools
import json
import random
from collections import Counter
from pathlib import Path
from src.common import norm
from src.prepare_v3_4_4 import no_list
from src.interface_v3_4_4 import parse_natural
from src.graph_v3_4_2 import audit_prompt,validate_sources
from experiments.v3_6_3_1.design import render as down_render,parse as down_parse,audit_pair
from experiments.v3_6_4.prepare import old_ids as before_v364
from experiments.v3_6_1.design import sha,token_info


def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))


def historical_graphs():
    result={};sources=[]
    def walk(x):
        if isinstance(x,dict):
            if all(k in x for k in ('name_nodes','paths','target','gold','candidates','path_order')):
                result[sha(no_list(x,4,2))]=x
            for v in x.values():walk(v)
        elif isinstance(x,list):
            for v in x:walk(v)
    for p in Path('results').rglob('*case*.json'):
        sources.append(p.as_posix());walk(read(p))
    return list(result.values()),sources


def make_cases():
    old,sources=historical_graphs()
    people={p['name']:p for c in old for p in c['candidates']}
    assert len(people)==21
    for name in people:
        assert len({(p['downstream_source_id'],p['relation'],p['target']) for c in old for p in c['candidates'] if p['name']==name})==1,'Ambiguous canonical person/source identity'
    groups=[]
    for rel in sorted({p['relation'] for p in people.values()}):
        for group in itertools.combinations(sorted(n for n,p in people.items() if p['relation']==rel),4):
            sets=[{norm(people[n]['target']),*(norm(a) for a in people[n]['target_aliases'])} for n in group]
            if all(not a&b for a,b in itertools.combinations(sets,2)):groups.append(group)
    rng=random.Random(366);rng.shuffle(groups)
    chosen=[groups[i%len(groups)] for i in range(120)]
    used_targets={c['target'] for c in old};used_nodes={n for c in old for n in list(c['name_nodes'].values())+[n for p in c['paths'] for n in p['nodes']]}
    targets=rng.sample([f'T{i}' for i in range(10000,99999) if f'T{i}' not in used_targets],120)
    nodes=iter(rng.sample([f'R{i}' for i in range(10000,99999) if f'R{i}' not in used_nodes],1560))
    pos=list(range(4))*30;rp=list(range(4))*30;rng.shuffle(pos);rng.shuffle(rp)
    seen={tuple(sorted(p['name'] for p in c['candidates'])) for c in old};cases=[]
    for i,group in enumerate(chosen):
        names=list(group);rng.shuffle(names);gold=names[pos[i]];others=[n for n in names if n!=gold]
        records=rng.sample(others,3);records.insert(rp[i],gold);ids=[next(nodes) for _ in range(13)]
        endpoints=[gold]+rng.sample(others,2);candidates=[copy.deepcopy(people[n]) for n in names]
        c=dict(case_id=f'v366-main-{i+1:03}',split='main',target=targets[i],gold=gold,gold_position=pos[i]+1,
               candidates=candidates,name_nodes=dict(zip(names,ids[:4])),name_record_order=records,
               paths=[dict(endpoint=n,nodes=ids[4+j*3:7+j*3]) for j,n in enumerate(endpoints)],path_order=rng.sample([0,1,2],3),
               bundle=list(group),bundle_id=sha(json.dumps(group,ensure_ascii=False))[:16],historical_bundle_reused=group in seen)
        c['graph_query_sha256']=sha(no_list(c,4,2));audit_prompt(c,4,2,no_list(c,4,2))
        assert c['graph_query_sha256'] not in {sha(no_list(o,4,2)) for o in old}
        cases.append(c)
    assert len({c['graph_query_sha256'] for c in cases})==120 and validate_sources(cases)==480
    counts=Counter(tuple(c['bundle']) for c in cases)
    assert max(counts.values())-min(counts.values())<=1
    return cases,dict(seed=366,historical_sources=sources,excluded_targets=sorted(used_targets),excluded_nodes=sorted(used_nodes),
        historical_graph_fingerprints=sorted(sha(no_list(c,4,2)) for c in old),people_reused=sorted(people),available_bundles=len(groups),
        bundle_uses=[dict(bundle=list(g),count=counts[g]) for g in groups],gold_array_positions=dict(Counter(c['gold_position'] for c in cases)),
        gold_record_positions=dict(Counter(c['name_record_order'].index(c['gold'])+1 for c in cases)),
        historical_bundle_reused_cases=[c['case_id'] for c in cases if c['historical_bundle_reused']],source_mappings_checked=480)


def make_mappings(cases,tok):
    old,sources=before_v364()
    for split in ('development','confirmation'):
        p=f'results/v3_6_4/{split}_cases.json';sources.append(p)
        old.update(m[k] for c in read(p) for m in c['members'] for k in ('entity','state','outcome'))
    pool=[f'{role}_{letter}{n:02}' for role in ('STATE','OUTCOME') for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for n in range(100)]
    audit=[token_info(tok,x)|dict(eligible=x not in old) for x in pool]
    rng=random.Random(3665);candidates={}
    for role in ('STATE','OUTCOME'):
        sub=[a for a in audit if a['eligible'] and a['raw'].startswith(role+'_')];minimum=min(a['token_count'] for a in sub)
        candidates[role]=[a['raw'] for a in sub if a['token_count']==minimum];rng.shuffle(candidates[role])
        assert len(candidates[role])>=480,'Insufficient inherited ID inventory'
    orders=[['a','b']]*60+[['b','a']]*60;rng.shuffle(orders);alt_rng=random.Random(3666)
    used=set();identity={};modules={}
    for i,c in enumerate(cases):
        suffixes=set();table={}
        def take(role):
            v=next(v for v in candidates[role] if v not in used and v.split('_')[-1] not in suffixes)
            used.add(v);suffixes.add(v.split('_')[-1]);return v
        for person in c['candidates']:
            name=person['name'];pid='person-'+sha(name+'|'+person['downstream_source_id'])[:16]
            table[name]=dict(person_id=pid,canonical_name=name,state=take('STATE'),outcome=take('OUTCOME'),source=person)
        assert len({x['person_id'] for x in table.values()})==4 and len(suffixes)==8
        non_gold=[n for n in table if n!=c['gold']];default=alt_rng.choice(non_gold)
        identity[c['case_id']]=dict(by_name=table,by_state={v['state']:n for n,v in table.items()},by_outcome={v['outcome']:n for n,v in table.items()},default_alternate=default)
        for name in non_gold:
            a,b=table[c['gold']],table[name];mid=c['case_id']+'/'+b['person_id']
            legacy=dict(case_id=c['case_id'],split='main',entity_a=a['person_id'],entity_b=b['person_id'],
                state_a=a['state'],state_b=b['state'],outcome_a=a['outcome'],outcome_b=b['outcome'],up_order=['a','b'],down_order=orders[i])
            pair=audit_pair(legacy,'D')
            assert all(len(p['downstream_mappings'])==2 and not any(n in p['prompt'] for n in table) for p in pair)
            module=dict(module_id=mid,case_id=c['case_id'],alternate=name,gold=c['gold'],legacy=legacy)
            module['mapping_hash']=sha(json.dumps(legacy,sort_keys=True,ensure_ascii=False));modules[mid]=module
    assert len(used)==960 and not used&old
    return identity,modules,dict(old_sources=sources,old_excluded=len(old),selected=960,candidates=[a|dict(selected=a['raw'] in used) for a in audit])


def first_prompt(c,diagnostic=False):
    prompt=no_list(c,4,2,2 if diagnostic else 1)
    assert all(p['target'] not in prompt and all(a not in prompt for a in p['target_aliases']) for p in c['candidates'])
    return dict(case_id=c['case_id'],call_id=c['case_id']+('/DIAGNOSTIC' if diagnostic else '/FIRST'),prompt=prompt,text_sha256=sha(prompt),cap=96)


def first_parse(row,c):
    if row is None:return dict(category='MISSING',identity=None,strict_valid=False)
    p=parse_natural(row['raw_text'],[x['name'] for x in c['candidates']],row['truncated'],{})
    if p['strict_valid']:p['category']='GOLD' if p['identity']==c['gold'] else 'WRONG'
    return p


def down_prompt(module,arm):
    assert arm in ('G','A')
    m=module['legacy'];state=m['state_a' if arm=='G' else 'state_b']
    r=down_render(m,'PIPELINE-A',shell='VALIDATED',supplied=state)
    return dict(case_id=module['case_id'],module_id=module['module_id'],arm=arm,supplied_state=state,expected=r['expected'],
                prompt=r['prompt'],text_sha256=r['text_sha256'],mapping_hash=module['mapping_hash'],cap=16)


def route(c,row,identity,modules):
    parsed=first_parse(row,c);mapping=identity[c['case_id']]
    alt=parsed['identity'] if parsed['category']=='WRONG' else mapping['default_alternate']
    mid=c['case_id']+'/'+mapping['by_name'][alt]['person_id'];module=modules[mid]
    assert module['alternate']==alt
    arm='A' if parsed['category']=='WRONG' else 'G'
    p=down_prompt(module,arm) if parsed['strict_valid'] else None
    state=mapping['by_name'][parsed['identity']]['state'] if parsed['strict_valid'] else None
    assert p is None or p['supplied_state']==state
    log=dict(case_id=c['case_id'],raw_hash=row['raw_sha256'] if row else None,parsed_identity=parsed['identity'],first_category=parsed['category'],
             mapping_hash=module['mapping_hash'],module_id=mid,alternate=alt,supplied_state=state,
             actual_prompt_hash=p['text_sha256'] if p else None,natural_status='CALL_REQUIRED' if p else 'SKIPPED_'+parsed['category'])
    return module,p,log
