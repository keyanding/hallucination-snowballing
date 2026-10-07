"""Independent byte/token/parser/gate check for v3.6.3.1; no model calls."""
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
from transformers import AutoTokenizer

OUT=Path('results/v3_6_3_1')
STAGES=('calibration','main_upstream','main_downstream','pipeline_generated','shell_diagnostic','integrated')
EXPECTED={'U-A':'B','U-B':'Bp','D-A':'C','D-B':'Cp','I-A':'C','I-B':'Cp'}


def load(name):
    return json.loads((OUT/name).read_text(encoding='utf-8'))


def sha(value):
    return hashlib.sha256(value.encode()).hexdigest()


def parse(r,c):
    v=unicodedata.normalize('NFC',r['raw_text']).strip().removesuffix('.')
    up=r['condition'].startswith('U-')
    if r['truncated']:
        cat='INVALID'
    elif up:
        cat='B' if v==c['state_a'] else 'Bp' if v==c['state_b'] else 'OTHER_STATE' if re.fullmatch(r'STATE_[A-Z][0-9]{2}',v) else 'INVALID'
    else:
        cat='C' if v==c['outcome_a'] else 'Cp' if v==c['outcome_b'] else 'UNKNOWN' if v=='UNKNOWN' else 'OTHER_OUTCOME' if re.fullmatch(r'OUTCOME_[A-Z][0-9]{2}',v) else 'INVALID'
    return r|dict(category=cat,normalized=v,permitted=cat in (('B','Bp') if up else ('C','Cp')))


def expected_prompt(c,condition,shell,supplied=None):
    up='\n'.join(c['entity_'+r]+' -> '+c['state_'+r] for r in c['up_order'])
    down='\n'.join(c['state_'+r]+' -> '+c['outcome_'+r] for r in c['down_order'])
    role='b' if condition.endswith('-B') else 'a'
    entity=c['entity_'+role]
    if condition.startswith('U-'):
        return f'Synthetic transition task.\n\nUpstream mappings:\n{up}\n\nCurrent entity:\n{entity}\n\nReturn only the mapped state.'
    if condition.startswith('I-'):
        return f'Synthetic two-hop task.\n\nUpstream mappings:\n{up}\n\nDownstream mappings:\n{down}\n\nCurrent entity:\n{entity}\n\nFollow the mappings and return only the final outcome.'
    state=supplied if condition=='PIPELINE-A' else c['state_'+role]
    if shell=='RECORDED':
        return f'Synthetic propagation task.\n\nRecorded intermediate result:\n{state}\n\nDownstream mappings:\n{down}\n\nReturn only the outcome implied by the recorded intermediate result.'
    assert shell=='VALIDATED'
    return f'Synthetic mapping task.\n\nMappings:\n{down}\n\nCurrent state:\n{state}\n\nReturn only the mapped outcome.'


def main():
    manifest=load('manifest.json')
    for group in ('frozen','prior_artifacts'):
        for path,h in manifest[group].items():
            assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==h,path
    pre=(OUT/'design_audit.pre_inference.md').read_bytes()
    assert (OUT/'design_audit.md').read_bytes().startswith(pre)
    freeze=load('decoding_freeze.json')
    tok=AutoTokenizer.from_pretrained(freeze['model'],revision=freeze['revision'],cache_dir='.cache/huggingface',local_files_only=True)
    assert sha(tok.chat_template)==freeze['chat_template_sha256']
    audit=load('identifier_tokenization_audit.json')
    for r in audit['candidates']:
        ids=tok.encode(r['raw'],add_special_tokens=False)
        assert ids==r['token_ids'] and len(ids)==r['token_count'] and len(r['raw'])==r['character_length']
    cal,maincases,diagnostic=(load(k+'_cases.json') for k in ('calibration','main','diagnostic'))
    assert (len(cal),len(maincases),len(diagnostic))==(20,40,10)
    cases={c['case_id']:c for c in cal+maincases+diagnostic}
    allids=[c[f+'_'+r] for c in cases.values() for f in ('entity','state','outcome') for r in ('a','b')]
    assert len(allids)==len(set(allids))==420
    assert {r['raw'] for r in audit['candidates'] if r['selected']}==set(allids)
    old=set()
    for source in audit['old_sources']:
        old.update(x.upper() for x in re.findall(r'(?:ENTITY|STATE|OUTCOME)_[A-Z][0-9]{2}',Path(source).read_text(encoding='utf-8'),re.I))
    assert not old&set(allids)
    for c in cases.values():
        selected=[c[f+'_'+r] for f in ('entity','state','outcome') for r in ('a','b')]
        assert len({v.split('_')[-1] for v in selected})==6
        assert all(a not in b for a in selected for b in selected if a!=b)
        for f in ('entity','state','outcome'):
            a,b=c[f+'_a'],c[f+'_b']
            assert len(a)==len(b) and len(tok.encode(a,add_special_tokens=False))==len(tok.encode(b,add_special_tokens=False))
    for split,percell in ((cal,5),(maincases,10)):
        assert set(Counter((tuple(c['up_order']),tuple(c['down_order'])) for c in split).values())=={percell}
    plan=load('prompt_plan.json')
    for stage in STAGES:
        if stage=='pipeline_generated':
            continue
        for p in plan[stage]:
            assert p['prompt']==expected_prompt(cases[p['case_id']],p['condition'],p['shell'])
            assert sha(p['prompt'])==p['text_sha256']
            rendered=tok.apply_chat_template([dict(role='user',content=p['prompt'])],tokenize=False,add_generation_prompt=True,enable_thinking=False)
            assert rendered==p['rendered_prompt'] and sha(rendered)==p['rendered_sha256']
    for p in plan['pipeline_templates']:
        assert p['prompt']==expected_prompt(cases[p['case_id']],'PIPELINE-A','VALIDATED','{ACTUAL_NORMALIZED_U_A_STATE}')
        assert sha(p['prompt'])==p['text_sha256']
    rows={}
    for stage in STAGES:
        actual=[json.loads(s) for s in (OUT/(stage+'_outputs.jsonl')).read_text(encoding='utf-8').splitlines()]
        assert len({(r['case_id'],r['condition'],r['shell']) for r in actual})==len(actual)
        if stage!='pipeline_generated':
            assert len(actual)<=len(plan[stage])
            for p,r in zip(plan[stage],actual):
                assert all(r[k]==v for k,v in p.items())
        for r in actual:
            assert tok.decode(r['output_token_ids'],skip_special_tokens=True)==r['raw_text']
            assert len(r['output_token_ids'])==r['output_tokens']<=16
            assert r['truncated']==(r['output_tokens']>=16 and r['output_token_ids'][-1]!=tok.eos_token_id)
            assert r['prompt']==expected_prompt(cases[r['case_id']],r['condition'],r['shell'],r['supplied_state'])
            rendered=tok.apply_chat_template([dict(role='user',content=r['prompt'])],tokenize=False,add_generation_prompt=True,enable_thinking=False)
            assert rendered==r['rendered_prompt']
            assert len(tok.encode(rendered,add_special_tokens=False))==r['input_tokens']
            for key,hkey in (('prompt','text_sha256'),('rendered_prompt','rendered_sha256'),('raw_text','raw_sha256')):
                assert sha(r[key])==r[hkey]
            assert r['seed']==42 and r['new_chat'] and not r['use_cache'] and not r['constrained']
            assert 'UNKNOWN' not in r['prompt'] and not re.search(r'\b(gold|alt|wrong|correct|error)\b',r['prompt'],re.I)
        rows[stage]=[parse(r,cases[r['case_id']]) for r in actual]
    cr=rows['calibration']
    assert len(cr)==80
    cb={(r['case_id'],r['condition']):r for r in cr}
    counts={k:sum(r['condition']==k and r['category']==v for r in cr) for k,v in list(EXPECTED.items())[:4]}
    cc=dict(zip('ABCD',counts.values()))
    cc.update(E=sum(cb[c['case_id'],'U-A']['category']=='B' and cb[c['case_id'],'U-B']['category']=='Bp' for c in cal),
              F=sum(cb[c['case_id'],'D-A']['category']=='C' and cb[c['case_id'],'D-B']['category']=='Cp' for c in cal),G=sum(r['permitted'] for r in cr))
    metrics=load('metrics.json')
    assert cc=={k:v['count'] for k,v in metrics['calibration']['gates'].items()}
    calpass=all(n>=(79 if k=='G' else 19) for k,n in cc.items())
    gate=load('gate.json')
    logs=[json.loads(s) for s in (OUT/'pipeline_log.jsonl').read_text(encoding='utf-8').splitlines()]
    pipeline_verified=0
    if not calpass:
        assert all(not r for k,r in rows.items() if k!='calibration') and not logs
        assert gate['final_decision']=='STOP_V3631_CALIBRATION_INVALID'
    else:
        assert [len(rows[k]) for k in ('main_upstream','main_downstream','shell_diagnostic')]==[80,80,40]
        static=rows['main_upstream']+rows['main_downstream']
        by={(r['case_id'],r['condition']):r for r in static}
        pb={r['case_id']:r for r in rows['pipeline_generated']}
        lb={r['case_id']:r for r in logs}
        assert list(lb)==plan['pipeline_case_order'] and len(logs)==40
        strict=correct_up=0
        sources=[]
        for c in maincases:
            cid=c['case_id']
            u=by[cid,'U-A']
            valid=u['category']!='INVALID'
            assert (cid in pb)==valid
            log=lb[cid]
            assert log['upstream_raw']==u['raw_text'] and log['upstream_normalized']==u['normalized']
            assert log['upstream_category']==u['category'] and log['upstream_text_sha256']==u['text_sha256']
            assert log['status']==('CALLED_UNREPAIRED' if valid else 'UPSTREAM_INVALID_SKIPPED')
            if valid:
                r=pb[cid]
                assert r['upstream_source']==log and r['supplied_state']==u['normalized']
                assert r['expected']=={c['state_a']:c['outcome_a'],c['state_b']:c['outcome_b']}.get(u['normalized'])
                pipeline_verified+=1
            uc=u['category']=='B'
            dc=valid and pb[cid]['category']=='C'
            correct_up+=uc
            strict+=uc and dc
            if not (uc and dc):
                sources.append('UPSTREAM_INVALID' if not valid else 'UPSTREAM_INCORRECT' if not uc else 'DOWNSTREAM_AFTER_CORRECT_UPSTREAM')
        numbers=[sum(r['condition']==k and r['category']==EXPECTED[k] for r in static) for k in ('U-A','U-B','D-A','D-B')]
        numbers += [sum(by[c['case_id'],'D-A']['category']=='C' and by[c['case_id'],'D-B']['category']=='Cp' for c in maincases),strict]
        m=metrics['main']
        assert numbers==[v['count'] for v in m['metrics'].values()]
        assert all(v['denominator']==40 for v in m['metrics'].values())
        for n,v in zip(numbers,m['metrics'].values()):
            z=1.959963984540054
            center=(n/40+z*z/80)/(1+z*z/40)
            half=z*((n/40*(1-n/40)/40+z*z/(4*40*40))**.5)/(1+z*z/40)
            assert all(abs(a-b)<1e-6 for a,b in zip(v['wilson_95'],(center-half,center+half)))
        assert m['conditional_downstream']['count']==strict and m['conditional_downstream']['denominator']==correct_up
        assert Counter(sources)==Counter(r['source'] for r in m['pipeline_failures'])
        off=sum(r['category'] in ('OTHER_STATE','OTHER_OUTCOME','INVALID') for r in static)
        assert off==m['G7_off_target']['count']
        mainpass=all(n>=(38 if i==5 else 39) for i,n in enumerate(numbers)) and off<=2
        assert mainpass==m['passed']==gate['main_pass']
        assert gate['final_decision']==('TWO_HOP_PIPELINE_VALIDATED' if mainpass else 'TWO_HOP_PIPELINE_INVALID')
        assert len(rows['integrated'])==(40 if mainpass else 0)
        sm=load('shell_diagnostic_metrics.json')
        assert sm['evaluated']
        for shell in ('VALIDATED','RECORDED'):
            sub=[r for r in rows['shell_diagnostic'] if r['shell']==shell]
            assert len(sub)==20
            actual=sm['shells'][shell]
            assert actual['exact_accuracy']['count']==sum(r['category']==EXPECTED[r['condition']] for r in sub)
            assert actual['invalid_count']==sum(r['category']=='INVALID' for r in sub)
            assert actual['truncation_count']==sum(r['truncated'] for r in sub)
            assert actual['prefix_omission_count']==sum(r['category']=='INVALID' and r['normalized'] in {cases[r['case_id']][f].split('_')[-1] for f in ('outcome_a','outcome_b')} for r in sub)
            assert actual['explanation_format_count']==sum(r['category']=='INVALID' and bool(re.search(r'\b[A-Za-z]{2,}\b',r['normalized'])) for r in sub)
        paired={(r['case_id'],r['condition'],r['shell']):r for r in rows['shell_diagnostic']}
        for pair in sm['paired_transitions']:
            a,b=(paired[pair['case_id'],pair['condition'],s] for s in ('VALIDATED','RECORDED'))
            assert a['supplied_state']==b['supplied_state'] and a['downstream_mappings']==b['downstream_mappings']
            assert (pair['validated'],pair['recorded'])==(a['category'],b['category'])
        im=load('integrated_metrics.json')
        ir=rows['integrated']
        ib={(r['case_id'],r['condition']):r for r in ir}
        subset=load('subsets.json')['integrated']
        ic=[sum(r['condition']==k and r['category']==EXPECTED[k] for r in ir) for k in ('I-A','I-B')]
        ip=sum(ib[cid,'I-A']['category']=='C' and ib[cid,'I-B']['category']=='Cp' for cid in subset) if ir else 0
        assert [im[k]['count'] for k in ('I_A','I_B','paired')]==ic+[ip]
        assert im['ready']==(bool(ir) and min(ic+[ip])>=19)==gate['INTEGRATED_TWO_HOP_READY']
    assert gate['counts']=={k:len(r) for k,r in rows.items()}
    assert sum(map(len,rows.values()))<=360
    parsed=[json.loads(s) for s in (OUT/'parsed_outcomes.jsonl').read_text(encoding='utf-8').splitlines()]
    reported={(r['case_id'],r['condition'],r['shell']):r for r in parsed}
    for group in rows.values():
        for r in group:
            q=reported[r['case_id'],r['condition'],r['shell']]
            assert q['category']==r['category'] and q['normalized']==r['normalized']
    result=dict(passed=True,tokenizer_candidates_verified=len(audit['candidates']),fresh_identifiers=420,static_prompts_verified=320,
                output_roundtrips=sum(map(len,rows.values())),actual_pipeline_states_verified=pipeline_verified,
                historical_artifacts_unchanged=len(manifest['prior_artifacts']),frozen_hashes_unchanged=True,
                independent_gate=gate['final_decision'],calibration_counts=cc)
    (OUT/'independent_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
