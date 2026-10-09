"""Read-only independent token/category/graph checks; no model loading."""
import json
from collections import Counter
from pathlib import Path
from transformers import AutoTokenizer
from experiments.v3_6_5.prepare import OUT,load,write,verify,MODEL,REVISION
from src.graph_v3_4_2 import audit_prompt,validate_sources
from src.interface_v3_4_4 import parse_natural


def main():
    verify()
    tok=AutoTokenizer.from_pretrained(MODEL,revision=REVISION,cache_dir='.cache/huggingface',local_files_only=True)
    cases={c['case_id']:c for c in load('development_cases.json')+load('confirmation_cases.json')}
    assert validate_sources(list(cases.values()))==192
    mappings=load('downstream_compatibility.json')
    plan=load('prompt_plan.json');gate=load('gate.json');all_rows={}
    for stage in ('development','presentation_diagnostic','confirmation'):
        rows=[json.loads(s) for s in (OUT/(stage+'_outputs.jsonl')).read_text(encoding='utf-8').splitlines() if s]
        all_rows[stage]=rows
        assert len(rows)==gate['calls'][stage]
        for r in rows:
            c=cases[r['case_id']]
            assert audit_prompt(c,4,2,r['prompt'])['unique_queried_endpoint']==r['gold']
            assert tok.decode(r['output_token_ids'],skip_special_tokens=True)==r['raw_text']
            assert r['truncated']==(len(r['output_token_ids'])>=96 and r['output_token_ids'][-1]!=tok.eos_token_id)
            assert r['input_tokens']==len(tok.encode(r['rendered_prompt'],add_special_tokens=False))
            assert r['downstream_endpoints']=={name:v['endpoint'] for name,v in mappings[r['case_id']].items()}
        if stage!='presentation_diagnostic':
            m=load(stage+'_metrics.json');counts=Counter()
            for r in rows:
                p=parse_natural(r['raw_text'],r['names'],r['truncated'],{})
                category=p['category']
                if p['strict_valid']:category='IN_SET_VALID_GOLD' if p['identity']==r['gold'] else 'IN_SET_VALID_WRONG'
                counts[category]+=1
            assert all(counts[k]==v for k,v in m['counts'].items())
    assert len(all_rows['development'])==24 and len(all_rows['presentation_diagnostic'])==8
    assert len(all_rows['confirmation'])==(24 if gate['development_passed'] else 0)
    prim={r['case_id']:r for r in all_rows['development']}
    changes=0;coverage=0
    for r in all_rows['presentation_diagnostic']:
        a=prim[r['case_id']]
        assert a['prompt'].split('\n\nGraph-link records:\n')[1]==r['prompt'].split('\n\nGraph-link records:\n')[1]
        x,y=(parse_natural(v['raw_text'],v['names'],v['truncated'],{}) for v in (a,r))
        if x['strict_valid'] and y['strict_valid']:
            coverage+=1;changes+=x['identity']!=y['identity']
    diag=load('presentation_diagnostic_metrics.json')
    assert diag['changed_identity']==changes and diag['comparable']==coverage
    assert gate['PRESENTATION_SENSITIVE']==(changes>3)
    assert load('development_classification.before_diagnostic.json')==load('development_metrics.json')
    result=dict(passed=True,model_calls_for_verification=0,raw_output_round_trips=sum(map(len,all_rows.values())),
                downstream_source_mappings_checked=192,diagnostic_identity_changes=changes,diagnostic_comparable_pairs=coverage,
                prior_artifacts_unchanged=len(load('manifest.json')['prior_artifacts']),all_frozen_hashes_unchanged=True,
                final_decision=gate['final_decision'])
    write('independent_verification.json',result)
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
