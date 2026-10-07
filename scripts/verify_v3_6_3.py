"""Independent exact-output and actual-state-forwarding verification."""
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from transformers import AutoTokenizer

OUT=Path('results/v3_6_3')


def load(name):
    return json.loads((OUT/name).read_text(encoding='utf-8'))


def norm(value):
    return unicodedata.normalize('NFC',value).strip().removesuffix('.')


def main():
    manifest=load('manifest.json')
    for group in ('frozen','prior_artifacts'):
        for path,value in manifest[group].items():
            assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==value,path
    freeze=load('decoding_freeze.json')
    tok=AutoTokenizer.from_pretrained(freeze['model'],revision=freeze['revision'],cache_dir='.cache/huggingface',local_files_only=True)
    audit=load('identifier_tokenization_audit.json')
    for r in audit['candidates']:
        ids=tok.encode(r['raw'],add_special_tokens=False)
        assert ids==r['token_ids'] and len(ids)==r['token_count']
    cal_cases,main_cases=load('calibration_cases.json'),load('main_cases.json')
    cases={c['case_id']:c for c in cal_cases+main_cases}
    allids=[c[role+'_'+field] for c in cases.values() for role in ('gold','alt') for field in ('entity','state','outcome')]
    assert len(allids)==len(set(allids))==360
    plan=load('prompt_plan.json')
    rows={}
    for stage in ('calibration','main_upstream','main_propagation','pipeline_generated','integrated','order_diagnostic'):
        rows[stage]=[json.loads(s) for s in (OUT/(stage+'_outputs.jsonl')).read_text(encoding='utf-8').splitlines()]
        actual=rows[stage]
        assert len({(r['case_id'],r['condition']) for r in actual})==len(actual)
        if stage!='pipeline_generated':
            for expected,r in zip(plan[stage],actual):
                assert all(r[k]==v for k,v in expected.items())
        for r in actual:
            assert tok.decode(r['output_token_ids'],skip_special_tokens=True)==r['raw_text']
            assert len(r['output_token_ids'])==r['output_tokens']<=16
            assert r['truncated']==(r['output_tokens']>=16 and r['output_token_ids'][-1]!=tok.eos_token_id)
            rendered=tok.apply_chat_template([dict(role='user',content=r['prompt'])],tokenize=False,add_generation_prompt=True,enable_thinking=False)
            assert rendered==r['rendered_prompt']
            assert len(tok.encode(rendered,add_special_tokens=False))==r['input_tokens']
            for key,hkey in (('prompt','text_sha256'),('rendered_prompt','rendered_sha256'),('raw_text','raw_sha256')):
                assert hashlib.sha256(r[key].encode()).hexdigest()==r[hkey]
            assert r['seed']==42 and r['new_chat'] and not r['use_cache'] and not r['constrained']
            assert 'UNKNOWN' not in r['prompt'] and not re.search(r'\b(gold|alt|wrong|correct)\b',r['prompt'],re.I)
            c=cases[r['case_id']]
            v=norm(r['raw_text'])
            up=r['condition'].startswith('U-')
            if r['truncated']:
                cat='INVALID'
            elif up:
                cat='B' if v==c['gold_state'] else 'Bp' if v==c['alt_state'] else 'OTHER_STATE' if re.fullmatch(r'STATE_[A-Z][0-9]{2}',v) else 'INVALID'
            else:
                cat='C' if v==c['gold_outcome'] else 'Cp' if v==c['alt_outcome'] else 'UNKNOWN' if v=='UNKNOWN' else 'OTHER_OUTCOME' if re.fullmatch(r'OUTCOME_[A-Z][0-9]{2}',v) else 'INVALID'
            r.update(category=cat,normalized=v,permitted=cat in (('B','Bp') if up else ('C','Cp')))
    cr=rows['calibration']
    assert len(cr)==80
    cb={(r['case_id'],r['condition']):r for r in cr}
    expected={'U-GOLD':'B','U-ALT':'Bp','P-GOLD':'C','P-ALT':'Cp'}
    counts={k:sum(r['condition']==k and r['category']==v for r in cr) for k,v in expected.items()}
    cc=dict(zip('ABCD',(counts[k] for k in expected)))
    cc.update(E=sum(cb[c['case_id'],'U-GOLD']['category']=='B' and cb[c['case_id'],'U-ALT']['category']=='Bp' for c in cal_cases),
              F=sum(cb[c['case_id'],'P-GOLD']['category']=='C' and cb[c['case_id'],'P-ALT']['category']=='Cp' for c in cal_cases),
              G=sum(r['permitted'] for r in cr))
    metrics=load('metrics.json')
    assert cc=={k:v['count'] for k,v in metrics['calibration']['gates'].items()}
    calpass=all(v>=(79 if k=='G' else 19) for k,v in cc.items())
    gate=load('gate.json')
    logs=[json.loads(s) for s in (OUT/'pipeline_log.jsonl').read_text(encoding='utf-8').splitlines()]
    pipeline_verified=0
    if not calpass:
        assert all(not r for k,r in rows.items() if k!='calibration') and not logs
        assert gate['final_decision']=='STOP_TWO_HOP_CALIBRATION_INVALID'
        assert gate['integrated_evaluated'] is False
    else:
        assert [len(rows[k]) for k in ('main_upstream','main_propagation','integrated','order_diagnostic')]==[80,80,40,20]
        static=rows['main_upstream']+rows['main_propagation']
        by={(r['case_id'],r['condition']):r for r in static}
        pb={r['case_id']:r for r in rows['pipeline_generated']}
        lb={r['case_id']:r for r in logs}
        assert list(lb)==plan['pipeline_case_order'] and len(logs)==40
        template={r['case_id']:r for r in plan['pipeline_templates']}
        for c in main_cases:
            cid=c['case_id']
            up=by[cid,'U-GOLD']
            valid=up['category']!='INVALID'
            assert (cid in pb)==valid
            assert lb[cid]['upstream_raw']==up['raw_text'] and lb[cid]['upstream_normalized']==up['normalized']
            assert lb[cid]['upstream_text_sha256']==up['text_sha256']
            if valid:
                r=pb[cid]
                assert r['supplied_state']==up['normalized']
                assert r['prompt']==template[cid]['prompt'].replace('{ACTUAL_NORMALIZED_U_GOLD_STATE}',up['normalized'])
                assert r['upstream_source']==lb[cid]
                assert r['created_utc']>=up['created_utc']
                assert 'Upstream mappings' not in r['prompt'] and 'ENTITY_' not in r['prompt']
                mapped=dict(re.findall(r'^(STATE_[A-Z][0-9]{2}) -> (OUTCOME_[A-Z][0-9]{2})$',r['prompt'],re.M))
                assert mapped.get(up['normalized'])==r['expected']
                pipeline_verified+=1
        mc={k:sum(r['condition']==k and r['category']==v for r in static) for k,v in expected.items()}
        switch=sum(by[c['case_id'],'P-GOLD']['category']=='C' and by[c['case_id'],'P-ALT']['category']=='Cp' for c in main_cases)
        e2e=sum(by[c['case_id'],'U-GOLD']['category']=='B' and c['case_id'] in pb and pb[c['case_id']]['category']=='C' for c in main_cases)
        six=list(mc.values())+[switch,e2e]
        assert six==[v['count'] for v in metrics['main']['metrics'].values()]
        off=sum(r['category'] in ('OTHER_STATE','OTHER_OUTCOME','INVALID') for r in static)
        passes=all(n>=(38 if i==5 else 39) for i,n in enumerate(six)) and off<=2
        assert gate['final_decision']==('TWO_HOP_PROPAGATION_ASSAY_VALIDATED' if passes else 'TWO_HOP_PROPAGATION_ASSAY_INVALID')
        subset=load('subsets.json')['integrated']
        ib={(r['case_id'],r['condition']):r for r in rows['integrated']}
        ig=sum(ib[cid,'I-GOLD']['category']=='C' for cid in subset)
        ia=sum(ib[cid,'I-ALT']['category']=='Cp' for cid in subset)
        ip=sum(ib[cid,'I-GOLD']['category']=='C' and ib[cid,'I-ALT']['category']=='Cp' for cid in subset)
        assert gate['INTEGRATED_TWO_HOP_READY']==(min(ig,ia,ip)>=19)
        order=sum(r['category']==by[r['case_id'],r['condition']]['category']==expected[r['condition']] for r in rows['order_diagnostic'])
        assert order==metrics['order_diagnostic']['unchanged_correct']['count']
    pre=(OUT/'design_audit.pre_inference.md').read_bytes()
    assert (OUT/'design_audit.md').read_bytes().startswith(pre)
    result=dict(all_checks_passed=True,historical_artifacts_unchanged=len(manifest['prior_artifacts']),frozen_files=len(manifest['frozen']),
                candidate_tokenizations=7800,exact_output_token_roundtrips=sum(map(len,rows.values())),unrepaired_pipeline_calls_verified=pipeline_verified,
                independently_counted_calibration=cc,final_decision=gate['final_decision'],INTEGRATED_TWO_HOP_READY=gate['INTEGRATED_TWO_HOP_READY'])
    (OUT/'independent_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
