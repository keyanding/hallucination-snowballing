"""Deterministic reports and independent raw-artifact verification."""
import difflib
import json
import math
from pathlib import Path
from statistics import mean

from .analysis_v3_4_2 import analyze, margin
from .calibration_choice import free_fields
from .calibration_v3_4_1 import FILES
from .calibration_v3_4_2 import collect, verify_frozen
from .common import digest
from .experiment_v3 import write_json
from .experiment_v3_3 import sha
from .graph_v3_4_2 import OUT, GRID, audit_prompt, key, load, render, validate_sources


def rate(value):
    if value['rate'] is None:
        return 'N/A (0 eligible)'
    return f'{value["count"]}/{value["denominator"]} ({value["rate"]:.1%})'


def cell(value):
    return str(value).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','&#124;').replace('\n','<br>')


def verify(write=True):
    verify_frozen()
    rows=collect()
    cases={c['case_id']:c for c in load('dev_cases.json')+load('heldout_cases.json')}
    plans={(p['case_id'],p['depth'],p['branches']):p for p in load('prompt_plan.json')}
    for p in plans.values():
        assert audit_prompt(cases[p['case_id']],p['depth'],p['branches'],p['prompt'])==p['audit']
    assert len({(r['case_id'],r['depth'],r['branches']) for r in rows})==len(rows)
    selection_hash=digest(OUT/'development_selection.json')
    eos=load('manifest.json')['C']['EOS']
    for row in rows:
        c=cases[row['case_id']]
        plan=plans[row['case_id'],row['depth'],row['branches']]
        names=[p['name'] for p in c['candidates']]
        assert row['gold']==c['gold'] and row['gold_position']==c['gold_position']
        f,ch,l=row['F'],row['C'],row['L']
        for channel in (f,ch,l):
            assert channel['prompt']==plan['prompt'] and channel['rendered_prompt']==plan['rendered_prompt']
            assert channel['prompt_sha256']==sha(plan['rendered_prompt'])
            assert channel['candidate_order']==names and channel['input_tokens']==plan['input_tokens']
            assert channel['selection_sha256']==(selection_hash if row['split']=='heldout' else None)
            assert channel['isolation']==dict(fresh_input=True,cross_call_history=False,use_cache=False)
        for channel in (f,ch):
            assert channel['raw_sha256']==sha(channel['raw_text'])
            assert channel['output_tokens']==len(channel['output_token_ids'])
        assert f['output_tokens']<=96
        assert all(f[k]==v for k,v in free_fields(f['raw_text'],names,f['truncated']).items())
        assert f['strict_exact_candidate']==f['exact_candidate_only']
        assert ch['selected_candidate']==ch['raw_text'] in names
        assert ch['output_token_ids']==plan['candidate_token_ids'][names.index(ch['selected_candidate'])]+[eos]
        assert ch['exact_allowed_candidate'] and ch['all_candidates_reachable']
        assert [s['candidate'] for s in l['scores']]==names
        for i,s in enumerate(l['scores']):
            assert s['token_ids']==plan['candidate_token_ids'][i]
            assert s['token_count']==len(s['token_logprobs'])==len(s['token_ids'])
            assert math.isclose(sum(s['token_logprobs']),s['sum_logprob'],abs_tol=1e-9)
            assert math.isclose(s['sum_logprob']/s['token_count'],s['mean_logprob_per_token'],abs_tol=1e-9)
        ranked=sorted(l['scores'],key=lambda s:-s['mean_logprob_per_token'])
        assert [s['rank'] for s in ranked]==[1,2,3,4]
        assert l['top_candidate_by_mean_logprob']==ranked[0]['candidate'] and l['runner_up']==ranked[1]['candidate']
        assert math.isclose(l['gold_vs_best_wrong_margin'],margin(row),abs_tol=1e-9)
        assert math.isclose(l['margin_mean_logprob'],ranked[0]['mean_logprob_per_token']-ranked[1]['mean_logprob_per_token'],abs_tol=1e-9)
    metrics=analyze(rows)
    assert metrics['selection']==load('development_selection.json')
    assert sum(r['split']=='dev' for r in rows)==96
    assert len(rows)==96+12*len(metrics['selection']['selected'])
    for condition in metrics['selection']['selected']:
        assert metrics['heldout'][condition]['count']==12
    if (OUT/'metrics.json').exists():
        assert metrics==load('metrics.json')
    assert not any(name in json.dumps(metrics) for name in ('"NPR"','"NRR"'))
    result=dict(channel_triplets=len(rows),source_mapping_checks=validate_sources(list(cases.values())),
        rendered_graphs_checked=len(plans),prior_artifact_count=len(load('manifest.json')['prior_artifacts']),
        frozen_inputs_unchanged=True,prior_artifacts_unchanged=True,selection_recomputed=True,
        prompt_and_token_boundaries_verified=True,likelihood_arithmetic_verified=True,
        output_hashes={name:digest(OUT/name) for name in FILES},development_selection_sha256=selection_hash)
    if write:
        write_json(OUT/'verification.json',result)
        print(json.dumps(result,indent=2),flush=True)
    return metrics,result


def report():
    metrics,verification=verify(write=False)
    write_json(OUT/'metrics.json',metrics)
    overall=metrics['overall']
    confirmed=[name for name,s in metrics['heldout'].items() if s['confirmed']]
    passed=bool(confirmed and overall['C_valid']['rate']==1 and overall['FCA']['rate'] is not None
                and overall['FCA']['rate']>=.8 and overall['LCA']['rate']>=.8)
    gate=dict(passed=passed,confirmed_conditions=confirmed,
              reason='Held-out frontier confirmed' if passed else 'No held-out condition satisfies the full gate',
              downstream_calls=0,all_candidate_mappings_frozen=True,ambiguous_renderings=0)
    gate['v3.5_authorized']=passed
    write_json(OUT/'gate.json',gate)
    frontier='# Development frontier selection\n\nAll cutoffs, the immediate-neighbor rule and the complexity tie-break were frozen before inference. At most two qualifiers are retained. No post-held-out retuning.\n\n'
    frontier+='| Condition | C error | Gold median margin | Near boundary | FCA | LCA | Easier local support | Failed criteria | Selected |\n|---|---|---|---|---|---|---|---|---|\n'
    for d,b in GRID:
        name=key(d,b)
        s=metrics['development'][name]
        decision=metrics['selection']['conditions'][name]
        frontier+='| '+' | '.join(map(cell,[name,rate(s['ER']),f'{s["GM"]:.4f}',rate(s['NBF']),rate(s['FCA']),rate(s['LCA']),', '.join(decision['local_support']) or 'none',', '.join(decision['failed_checks']) or 'none',name in metrics['selection']['selected']]))+' |\n'
    frontier+='\nHeld-out results:\n\n'
    if not confirmed and not metrics['heldout']:
        frontier+='Not run: no development condition qualified. Twelve frozen held-out cases remain unqueried.\n'
    for name,s in metrics['heldout'].items():
        frontier+=f'- {name}: ER {rate(s["ER"])}, NBF {rate(s["NBF"])}, FCA {rate(s["FCA"])}, LCA {rate(s["LCA"])}; confirmed={s["confirmed"]}.\n'
    (OUT/'frontier_selection.md').write_text(frontier,encoding='utf-8',newline='\n')
    rows=collect()
    cases=load('dev_cases.json')+load('heldout_cases.json')
    inspection='# Factorial calibration inspection\n\nDepth and branch count form a partial order. First events below refer to the frozen depth-major display order, not a single difficulty ladder. Margin is gold minus best wrong candidate mean log probability (nats/token). Raw F outputs are verbatim except HTML escaping; all exact prompts are in prompt_plan.json and channel logs.\n'
    for c in cases:
        subset=[r for r in rows if r['case_id']==c['case_id']]
        inspection+=f'\n## {c["case_id"]}: Film {c["target"]}\n\nWhich candidate is the credited director of Film {c["target"]}?\n\n'
        inspection+='Candidates and frozen downstream mappings (targets are not supplied in prompts):\n\n'
        inspection+='\n'.join(f'- {p["name"]} → {p["relation"]} → {p["target"]}' for p in c['candidates'])+'\n\n'
        if not subset:
            inspection+='Not evaluated: no development frontier qualified. No twelve-condition held-out grid was run.\n'
            continue
        inspection+='| Depth | Branches | Gold | C choice | L top-1 | Margin | Free raw output |\n|---|---:|---|---|---|---:|---|\n'
        for row in subset:
            inspection+='| '+' | '.join(map(cell,[row['depth'],row['branches'],row['gold'],row['C']['selected_candidate'],row['L']['top_candidate_by_mean_logprob'],f'{margin(row):.4f}',row['F']['raw_text']]))+' |\n'
        if c['split']=='dev':
            diag=metrics['case_consistency'][c['case_id']]
            inspection+='\nClassification: '+', '.join(diag['labels'])+'.\n\n'
            for label,field in [('First margin compression','first_margin_compression'),('First near-boundary condition','first_near_boundary'),('First choice flip','first_choice_flip')]:
                value=diag[field]
                if isinstance(value,dict):
                    value=value['easier']+' → '+value['harder']
                inspection+=f'- {label}: {value or "none"}.\n'
            for comp in diag['comparisons']:
                flags=[]
                if comp['recovery']: flags.append('recovery after flip')
                if comp['margin_reversal']: flags.append('non-monotonic margin reversal')
                if comp['correct_to_wrong']: flags.append(comp['factor']+'-induced correct-to-wrong flip')
                if comp['boundary_crossing']: flags.append('margin sign boundary crossing')
                if flags:
                    inspection+=f'- {comp["easier"]} → {comp["harder"]}: '+ '; '.join(flags)+'.\n'
    for name in metrics['selection']['selected']:
        decision=metrics['selection']['conditions'][name]
        candidates=[r for r in rows if r['split']=='dev' and key(r['depth'],r['branches'])==name and r['C']['selected_candidate']!=r['gold']]
        c=next(c for c in cases if c['case_id']==candidates[0]['case_id'])
        inspection+=f'\n## Frontier prompt differences: {name}, {c["case_id"]}\n'
        for neighbor in decision['local_support']:
            nd=metrics['selection']['conditions'][neighbor]
            diff=difflib.unified_diff(render(c,nd['depth'],nd['branches']).splitlines(),render(c,decision['depth'],decision['branches']).splitlines(),fromfile=neighbor,tofile=name,lineterm='')
            inspection+='\n```diff\n'+'\n'.join(diff)+'\n```\n'
    (OUT/'inspection.md').write_text(inspection,encoding='utf-8',newline='\n')
    mono=metrics['monotonicity']
    crossing=[cid for cid,s in metrics['case_consistency'].items() if 'CASE_BOUNDARY_CROSSING' in s['labels']]
    isolated=[name for name,s in metrics['development'].items() if s['ER']['count'] and (not metrics['selection']['conditions'][name]['local_support'] or s['NBF']['count']<3)]
    changes={factor:mean(x['GM_change'] for x in mono[factor]['comparisons']) for factor in ('depth','branches')}
    selected=metrics['selection']['selected']
    diagnosis='# v3.4.2 diagnosis\n\nThis is descriptive calibration of one pinned Qwen3-4B NF4/BF16 setup on synthetic relation graphs with real candidate names. It is not a propagation experiment or a population-level capability estimate.\n\n'
    answers=[
        ('Does increasing depth reduce gold margin?',f'Adjacent median margin is non-increasing in {rate(mono["depth"]["GM"])} comparisons; {mono["depth"]["strictly_decreasing_GM"]} of 9 strictly decrease. Mean adjacent change is {changes["depth"]:.4f} nats/token.'),
        ('Does increasing branching reduce gold margin?',f'Adjacent median margin is non-increasing in {rate(mono["branches"]["GM"])} comparisons; {mono["branches"]["strictly_decreasing_GM"]} of 8 strictly decrease. Mean adjacent change is {changes["branches"]:.4f} nats/token.'),
        ('Which factor matters more?',f'The more negative average adjacent GM change is for {min(changes,key=changes.get)} on this grid. This compares one extra edge with one extra path, different interventions; it is not a general causal ranking. Full paired case tables expose variation hidden by medians.'),
        ('Are behavioral errors broadly monotonic?',f'Depth ER monotonicity: {rate(mono["depth"]["ER"])}; branch ER monotonicity: {rate(mono["branches"]["ER"])}. Strict increases: {mono["depth"]["strictly_increasing_ER"]}/9 and {mono["branches"]["strictly_increasing_ER"]}/8. Flat zero-error comparisons count as monotonic but do not establish increasing difficulty.'),
        ('Are margins more monotonic than errors?',f'Depth GM/ER proportions: {mono["depth"]["GM"]["rate"]:.3f}/{mono["depth"]["ER"]["rate"]:.3f}; branch GM/ER: {mono["branches"]["GM"]["rate"]:.3f}/{mono["branches"]["ER"]["rate"]:.3f}. These descriptive proportions include ties and are not significance tests.'),
        ('Which cases show boundary crossing?',', '.join(crossing) or 'None has an adjacent correct-to-wrong choice with a positive-to-negative gold margin crossing.'),
        ('Are errors isolated spikes?',('Error cells without local trend or the required near-boundary coverage: '+', '.join(isolated)) if isolated else 'No observed error cell lacks both the reported local-trend/boundary checks; inspect selection criteria separately.'),
        ('Which development conditions qualify?',', '.join(selected) if selected else 'None meets all preregistered criteria. See frontier_selection.md for every failed criterion.'),
        ('Does held-out confirm?',', '.join(confirmed) if confirmed else ('No selected held-out condition passes.' if selected else 'Not evaluated because no development condition qualified; all twelve held-out targets remain unqueried.')),
        ('Frozen rule for v3.5?', 'One confirmed construction is described below; do not automatically launch v3.5.' if passed else 'None. The measurement gate fails; v3.5_authorized=false. No difficulty, threshold, candidate or prompt was changed after observing outputs.')]
    for i,(question,answer) in enumerate(answers,1):
        diagnosis+=f'{i}. **{question}** {answer}\n\n'
    diagnosis+=f'Channel checks: C validity {rate(overall["C_valid"])}, free strict compliance {rate(overall["FSC"])}, FCA {rate(overall["FCA"])}, LCA {rate(overall["LCA"])}. Free truncations: {overall["free_truncated"]}; possible short out-of-set answers: {rate(overall["free_outset"])}. Formatting failures never count as C errors.\n\n'
    diagnosis+='## Development grid\n\n| Depth | Branches | ER | Median gold margin | Near-boundary fraction |\n|---|---|---|---|---|\n'
    for d,b in GRID:
        s=metrics['development'][key(d,b)]
        diagnosis+=f'| {d} | {b} | {rate(s["ER"])} | {s["GM"]:.4f} | {rate(s["NBF"])} |\n'
    if passed:
        chosen=metrics['selection']['conditions'][confirmed[0]]
        diagnosis+='\n## Confirmed construction recommendation\n\n'
        diagnosis+=f'Depth={chosen["depth"]}; branch_count={chosen["branches"]}. Use the exact template in prompt_plan.json and the fixed credited-director/comparison-director/associated-director vocabulary. Sample four real candidates with pairwise-distinct audited downstream targets and balanced frozen positions; use anonymous new target identifiers and independently sampled record IDs. Primary state selection uses exact constrained choice. Confirmation error rate: {rate(metrics["heldout"][confirmed[0]]["ER"])}; design target range 15–50%, not a forecast or confidence interval. Future v3.5 must use separate target questions and revalidate external validity.\n'
    diagnosis+='\n## Limits and stop decision\n\nDepth and branch count both increase token count. Candidate identities can recur across splits; questions are disjoint synthetic targets, not unseen-person tests. Path block order is frozen per case, not separately ablated. The synthetic graph links are not evidence about real films. No independent human audit or causal position-sensitivity claim is made; graph uniqueness is checked by parsing every rendering and position bias uses a frozen descriptive rule. Case labels may include both non-monotonicity and boundary crossing. No extra difficulty levels were tried.\n'
    diagnosis+=('No development frontier: stop after the frozen grid and inspect these artifacts. Do not expand or tune on held-out.\n' if not selected else 'Held-out results are final for these selected conditions; do not retune.\n')
    (OUT/'diagnosis.md').write_text(diagnosis,encoding='utf-8',newline='\n')
    audit=(OUT/'design_audit.pre_inference.md').read_text(encoding='utf-8')
    audit+='\n## Post-run achievement check\n\n| Design intention | Outcome |\n|---|---|\n'
    outcomes=[('Monotonic axis',f'Depth ER/GM {rate(mono["depth"]["ER"])}/{rate(mono["depth"]["GM"])}; branch ER/GM {rate(mono["branches"]["ER"])}/{rate(mono["branches"]["GM"])}'),
        ('Separate factors','All 12 factorial cells evaluated on the same eight cases'),('Traceability','80 frozen mappings rechecked'),('Identity control','All candidate hashes and name records invariant'),
        ('Format control',f'C valid {rate(overall["C_valid"])}; F compliance {rate(overall["FSC"])}'),('Boundary measurement','All candidate scores and 0.75-threshold fractions retained'),
        ('Avoid isolated selection',f'Selected {selected}; all local-support checks reported'),('Held-out protection',f'{len(rows)-96} held-out prompts; only selected cells'),
        ('Unique answer','240 rendered graphs independently parsed and resolved'),('Calibration scope','Zero downstream calls; propagation metrics absent')]
    audit+='\n'.join('| '+a+' | '+b+' |' for a,b in outcomes)+'\n'
    (OUT/'design_audit.md').write_text(audit,encoding='utf-8',newline='\n')
    write_json(OUT/'verification.json',verification)
    print(json.dumps(gate),flush=True)
