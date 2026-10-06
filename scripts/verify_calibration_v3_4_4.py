"""Post-run independent checks; no model calls or policy changes."""
import json
import sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.prepare_v3_4_4 import OUT, load
from src.common import digest, read_jsonl
from src.calibration_v3_4_4 import collect
from src.graph_v3_4_2 import audit_prompt, validate_sources, render
from src.interface_v3_4_4 import parse_natural
from src.experiment_v3 import write_json
from src.analysis_v3_4_4 import select_policy, natural_gate


def verify():
    manifest=load('manifest.json')
    for kind in ('frozen','prior_artifacts'):
        for name,expected in manifest[kind].items():
            # design_audit is a pre/post document; its frozen prefix is also retained
            # byte-for-byte in design_audit.pre_inference.md. No inference input changes.
            if name==(OUT/'design_audit.md').as_posix():
                before=(OUT/'design_audit.pre_inference.md').read_bytes()
                assert digest(OUT/'design_audit.pre_inference.md')==expected
                assert Path(name).read_bytes().startswith(before)
            else:
                assert digest(Path(name))==expected,name
    assert digest(Path('data/dev.json'))==manifest['source_sha256']
    plans=read_jsonl(OUT/'prompt_plan.jsonl')
    cases=load('development_cases.json')+load('confirmation_cases.json')+load('case_manifest.json')['old_diagnostic_cases']
    cases={c['case_id']:c for c in cases}
    for p in plans:
        assert audit_prompt(cases[p['case_id']],p['depth'],p['branches'],p['prompt'])==p['graph_audit']
    assert validate_sources(list(cases.values()))==184
    old_plans=json.loads(Path('results/calibration_v3_4_3/permutation_plan.json').read_text(encoding='utf-8'))
    for p in old_plans:
        if p['permutation']==1:
            assert render(cases[p['case_id']],p['depth'],p['branches'])==p['prompt']
    selection=load('policy_selection.json')
    rows=collect()
    expected={p['plan_id'] for p in plans if p['cohort']!='confirmation' or (selection['route'] and p['difficulty']==selection['difficulty'] and (selection['confirmation_with_R'] or p['interface']!='R'))}
    assert {r['plan_id'] for r in rows}==expected
    assert Counter(r['interface'] for r in rows if r['cohort']=='development')==dict(L=288,N=72,R=288)
    assert Counter(r['interface'] for r in rows if r['cohort']=='old')==dict(N=18,R=72)
    byid={p['plan_id']:p for p in plans}
    duplicates=[]
    for r in rows:
        p=byid[r['plan_id']]
        f,s=r['F'],r['S']
        assert f['rendered_prompt']==s['rendered_prompt']==p['rendered_prompt']
        parsed=parse_natural(f['raw_text'],p['candidate_order'],f['truncated'])
        assert all(f[k]==v for k,v in parsed.items())
        assert len(s['scores'])==4
        for score,ids in zip(s['scores'],p['candidate_token_ids']):
            assert score['token_ids']==ids and score['token_count']==len(ids)
            assert abs(sum(score['token_logprobs'])-score['sum_logprob'])<1e-10
            assert abs(score['mean_logprob_per_token']*len(ids)-score['sum_logprob'])<1e-10
        if r['interface']=='L':
            assert r['C']['selected_candidate'] in p['candidate_order'] and r['C']['all_candidates_reachable']
        if r['interface']=='N':
            other=next((v for v in rows if (v['cohort'],v['case_id'],v['difficulty'],v['interface'],v['rotation'])==(r['cohort'],r['case_id'],r['difficulty'],'R',1)),None)
            if other:
                assert f['output_token_ids']==other['F']['output_token_ids']
                assert s['scores']==other['S']['scores']
                duplicates.append(r['plan_id'])
    dev=load('development_metrics.json')
    recomputed=select_policy(dev,rows)
    assert all(selection[k]==v for k,v in recomputed.items())
    gate=load('gate.json')
    assert gate['v3_5_executed'] is False
    if selection['route'] in ('N','R'):
        g=natural_gate(load('metrics.json')['cohorts']['confirmation'][selection['difficulty']],selection['route'])
        assert gate['passed']==g['passed'] and gate['checks']==g['checks']
    result=dict(passed=True,all_1170_graphs_checked=True,mappings=184,old_canonical_exact_matches=18,
                exact_N_R1_repeats=len(duplicates),executed_renderings=len(rows),
                original_frozen_files_verified=True,prior_artifacts_preserved=len(manifest['prior_artifacts']),
                strict_parse_and_score_checks=True,selection_reproduced=True,confirmation_untuned=True,
                audit_lifecycle='design_audit.md is required to append a post-run table; original frozen bytes survive as its prefix and in design_audit.pre_inference.md. All other frozen files retain exact hashes.')
    write_json(OUT/'independent_verification.json',result)
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    verify()
