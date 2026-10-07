"""Independent token, prompt, position, nesting and gate audit; no inference."""
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
from transformers import AutoTokenizer

OUT=Path('results/v3_6_2')


def load(name):
    return json.loads((OUT/name).read_text(encoding='utf-8'))


def main():
    manifest=load('case_manifest.json')
    for group in ('frozen','prior_artifacts'):
        for path,expected in manifest[group].items():
            assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==expected,path
    freeze=load('decoding_freeze.json')
    tok=AutoTokenizer.from_pretrained(freeze['model'],revision=freeze['revision'],cache_dir='.cache/huggingface',local_files_only=True)
    audit=load('identifier_tokenization_audit.json')
    for row in audit['candidates']:
        tokens=tok.encode(row['raw'],add_special_tokens=False)
        assert tokens==row['token_ids'] and len(tokens)==row['token_count']
        assert len(row['raw'])==row['character_length']
    cases={c['case_id']:c for c in load('cases.json')}
    plan=load('prompt_plan.json')
    byplan={(r['case_id'],r['k'],r['condition']):r for r in plan['main']}
    selected=[]
    old=set()
    for path in audit['old_identifier_sources']:
        for c in json.loads(Path(path).read_text(encoding='utf-8')):
            old.update(v.upper() for k,v in c.items() if k.endswith('_state') or k.endswith('_outcome') or k in ('entity','alternate_entity'))
    for c in cases.values():
        ids=[c[k] for k in ('gold_state','wrong_state','gold_outcome','wrong_outcome')]
        ids += [v for d in c['distractors'] for v in d.values()]
        assert len(set(ids))==52 and not set(ids)&old
        selected+=ids
        for prefix in ('STATE','OUTCOME'):
            group=[v for v in ids if v.startswith(prefix+'_')]
            assert len({len(v) for v in group})==1
            assert len({len(tok.encode(v,add_special_tokens=False)) for v in group})==1
        previous=[]
        for k in (0,4,12,24):
            a,b=(byplan[c['case_id'],k,arm] for arm in ('C0','W0'))
            current=[tuple(r) for r in a['mappings']]
            assert len(current)==k+2
            assert [r for r in current if r in previous]==previous
            previous=current
            before,tail=a['prompt'].split('\nCurrent state:\n')
            state,after=tail.split('\n',1)
            assert state==c['gold_state']
            assert before+'\nCurrent state:\n'+c['wrong_state']+'\n'+after==b['prompt']
    assert len(selected)==len(set(selected))==2080
    for k in (4,12,24):
        subset=[r for r in plan['main'] if r['k']==k and r['condition']=='C0']
        assert Counter(r['position_band'] for r in subset)==dict(beginning=14,middle=13,end=13)
        for r in subset:
            start={'beginning':1,'middle':k//2+1,'end':k+1}[r['position_band']]
            assert sorted([r['gold_position'],r['wrong_position']])==[start,start+1]
    allrows={}
    for stage,n in (('main',320),('position_diagnostic',72)):
        rows=[json.loads(s) for s in (OUT/(stage+'_outputs.jsonl')).read_text(encoding='utf-8').splitlines()]
        assert len(rows)==n
        for p,r in zip(plan[stage],rows):
            assert all(r[key]==value for key,value in p.items())
            assert 'UNKNOWN' not in r['prompt']
            assert tok.decode(r['output_token_ids'],skip_special_tokens=True)==r['raw_text']
            assert len(r['output_token_ids'])==r['output_tokens']<=16
            assert r['truncated']==(r['output_tokens']>=16 and r['output_token_ids'][-1]!=tok.eos_token_id)
            rendered=tok.apply_chat_template([dict(role='user',content=r['prompt'])],tokenize=False,add_generation_prompt=True,enable_thinking=False)
            assert rendered==r['rendered_prompt']
            assert len(tok.encode(rendered,add_special_tokens=False))==r['input_tokens']
            for key,hashkey in (('prompt','text_sha256'),('rendered_prompt','rendered_sha256'),('raw_text','raw_sha256')):
                assert hashlib.sha256(r[key].encode()).hexdigest()==r[hashkey]
            assert r['seed']==42 and r['new_chat'] and not r['use_cache'] and not r['constrained']
            mappings=dict(re.findall(r'^(STATE_[A-Z][0-9]{2}) -> (OUTCOME_[A-Z][0-9]{2})$',r['prompt'],re.M))
            assert len(mappings)==r['k']+2 and mappings[r['supplied_state']]==r['expected']
            c=cases[r['case_id']]
            value=unicodedata.normalize('NFC',r['raw_text']).strip().removesuffix('.')
            if r['truncated']:
                category='INVALID'
            elif value==c['gold_outcome']:
                category='C'
            elif value==c['wrong_outcome']:
                category='Cp'
            elif value=='UNKNOWN':
                category='UNKNOWN'
            elif re.fullmatch(r'OUTCOME_[A-Z][0-9]{2}',value):
                category='OTHER'
            else:
                category='INVALID'
            r.update(category=category,correct=not r['truncated'] and value==r['expected'])
        allrows[stage]=rows
    metrics=load('metrics.json')
    results={}
    by={(r['case_id'],r['k'],r['condition']):r for r in allrows['main']}
    for k in (0,4,12,24):
        rows=[r for r in allrows['main'] if r['k']==k]
        counts=dict(A_C=sum(r['condition']=='C0' and r['correct'] for r in rows),
                    A_W=sum(r['condition']=='W0' and r['correct'] for r in rows),
                    S=sum(by[cid,k,'C0']['correct'] and by[cid,k,'W0']['correct'] for cid in cases),
                    U=sum(r['category']=='UNKNOWN' for r in rows),
                    O=sum(r['category'] in ('OTHER','INVALID') for r in rows))
        assert counts=={key:v['count'] for key,v in metrics['levels'][str(k)]['metrics'].items()}
        results[k]=counts
        if k:
            lost=sum(by[cid,0,'C0']['correct'] and by[cid,0,'W0']['correct'] and not (by[cid,k,'C0']['correct'] and by[cid,k,'W0']['correct']) for cid in cases)
            gained=sum(not (by[cid,0,'C0']['correct'] and by[cid,0,'W0']['correct']) and by[cid,k,'C0']['correct'] and by[cid,k,'W0']['correct'] for cid in cases)
            assert lost==metrics['degradation'][str(k)]['lost_count'] and gained==metrics['degradation'][str(k)]['gained_count']
    s=[results[k]['S'] for k in (0,4,12,24)]
    collapse=all(a>=b for a,b in zip(s,s[1:])) and sum(a>b for a,b in zip(s,s[1:]))>=2 and s[0]-s[-1]>=4
    assert collapse==metrics['monotonic_collapse']
    base=results[0]
    if any(base[key]<39 for key in ('A_C','A_W','S')):
        decision='BASE_ASSAY_REGRESSION'
    elif results[24]['A_C']<38 or results[24]['A_W']<38 or results[24]['S']<37 or metrics['degradation']['24']['lost_count']>=4 or collapse or sum(r['O'] for r in results.values())>2:
        decision='CONTEXT_SENSITIVE_ASSAY'
    else:
        decision='ROBUST_CONTEXT_ASSAY'
    assert load('gate.json')['final_decision']==decision
    diagnostic=load('position_diagnostic_metrics.json')
    for band in ('beginning','middle','end'):
        rows=[r for r in allrows['position_diagnostic'] if r['position_band']==band]
        assert len(rows)==24
        for arm in ('C0','W0'):
            assert sum(r['condition']==arm and r['correct'] for r in rows)==diagnostic['bands'][band][arm]['count']
    pre=(OUT/'design_audit.pre_inference.md').read_bytes()
    assert (OUT/'design_audit.md').read_bytes().startswith(pre)
    result=dict(all_checks_passed=True,frozen_files=len(manifest['frozen']),historical_artifacts_unchanged=len(manifest['prior_artifacts']),
                candidate_tokenizations=5200,selected_identifiers=2080,token_output_roundtrips=392,
                per_k_counts=results,final_decision=decision)
    (OUT/'independent_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
