"""Audited repeated-measures reports for candidate-order intervention."""
import json
import math
from pathlib import Path

from .analysis_v3_4_3 import CASE_IDS, CONDITIONS, analyze
from .analysis_v3_4_2 import margin
from .calibration_choice import free_fields
from .calibration_v3_4_1 import FILES
from .calibration_v3_4_3 import OUT, PRIOR, build_plan, collect, load, split_prompt, verify_frozen
from .common import digest, read_jsonl
from .experiment_v3 import write_json
from .experiment_v3_3 import sha
from .graph_v3_4_2 import validate_sources


def rate(value):
    if value['rate'] is None:
        return 'N/A (no eligible comparisons)'
    return f'{value["count"]}/{value["denominator"]} ({value["rate"]:.1%})'


def cell(value):
    return str(value).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','&#124;').replace('\n','<br>')


def verify(write=True):
    verify_frozen()
    cases,rebuilt=build_plan()
    plans={(p['case_id'],p['difficulty'],p['permutation']):p for p in load('permutation_plan.json')}
    for p in rebuilt:
        frozen=plans[p['case_id'],p['difficulty'],p['permutation']]
        assert all(frozen[k]==v for k,v in p.items())
    rows=collect()
    assert len(rows)==72 and len({(r['case_id'],r['difficulty'],r['permutation']) for r in rows})==72
    eos=load('manifest.json')['C_EOS']
    for r in rows:
        p=plans[r['case_id'],r['difficulty'],r['permutation']]
        names=p['candidate_order']
        assert r['gold']==p['gold'] and r['gold_position']==names.index(r['gold'])+1
        assert r['original_pos1']==p['original_pos1']
        for channel in (r['F'],r['C'],r['L']):
            assert channel['prompt']==p['prompt'] and channel['rendered_prompt']==p['rendered_prompt']
            assert channel['candidate_order']==names and channel['prompt_sha256']==sha(p['rendered_prompt'])
            assert channel['input_tokens']==p['input_tokens']
            assert channel['isolation']==dict(fresh_input=True,cross_call_history=False,use_cache=False)
            assert split_prompt(channel['prompt'])[1]==names
        for channel in (r['F'],r['C']):
            assert channel['raw_sha256']==sha(channel['raw_text'])
            assert channel['output_tokens']==len(channel['output_token_ids'])
        f,c,l=r['F'],r['C'],r['L']
        assert f['output_tokens']<=96
        assert all(f[k]==v for k,v in free_fields(f['raw_text'],names,f['truncated']).items())
        assert c['raw_text']==c['selected_candidate'] in names
        assert c['output_token_ids']==p['candidate_token_ids'][names.index(c['selected_candidate'])]+[eos]
        assert c['candidate_token_ids']==p['candidate_token_ids']
        assert c['exact_allowed_candidate'] and c['all_candidates_reachable']
        assert [s['candidate'] for s in l['scores']]==names
        for i,s in enumerate(l['scores']):
            assert s['identity']==s['candidate']==names[i] and s['absolute_candidate_position']==i+1
            assert s['token_ids']==p['candidate_token_ids'][i]
            assert s['token_count']==len(s['token_ids'])==len(s['token_logprobs'])
            assert math.isclose(s['sum_logprob'],sum(s['token_logprobs']),abs_tol=1e-9)
            assert math.isclose(s['mean_logprob_per_token'],s['sum_logprob']/s['token_count'],abs_tol=1e-9)
        ranked=sorted(l['scores'],key=lambda s:-s['mean_logprob_per_token'])
        assert [s['rank'] for s in ranked]==[1,2,3,4]
        assert l['top_candidate_by_mean_logprob']==ranked[0]['candidate'] and l['runner_up']==ranked[1]['candidate']
        assert math.isclose(l['gold_vs_best_wrong_margin'],margin(r),abs_tol=1e-9)
    metrics=analyze(rows)
    for s in metrics['sets'].values():
        for effects in s['identity_position_effects'].values():
            assert abs(sum(effects['delta_by_position'].values()))<1e-8
    old_channels=[{(r['case_id'],r['depth'],r['branches']):r for r in read_jsonl(PRIOR/f)} for f in FILES]
    replicas=[]
    for r in rows:
        if r['permutation']!=1:
            continue
        key=(r['case_id'],r['depth'],r['branches'])
        old_f,old_c,old_l=[channel[key] for channel in old_channels]
        old_scores={s['candidate']:s['mean_logprob_per_token'] for s in old_l['scores']}
        replicas.append(dict(case_id=r['case_id'],difficulty=r['difficulty'],
            prompt_identical=r['C']['prompt_sha256']==old_c['prompt_sha256'],
            free_raw_identical=r['F']['raw_text']==old_f['raw_text'],
            C_identical=r['C']['selected_candidate']==old_c['selected_candidate'],
            maximum_mean_score_difference=max(abs(s['mean_logprob_per_token']-old_scores[s['candidate']]) for s in r['L']['scores'])))
    assert all(r['prompt_identical'] for r in replicas)
    if (OUT/'metrics.json').exists():
        assert metrics==load('metrics.json')
    result=dict(channel_triplets=72,repeated_sets=18,cases=6,mapping_checks=validate_sources(cases),
        prior_artifact_count=len(load('manifest.json')['prior_artifacts']),prior_artifacts_unchanged=True,frozen_inputs_unchanged=True,
        all_permutations_verified=True,only_candidate_list_changed=True,candidate_name_record_order_fixed=True,
        token_and_likelihood_checks=True,prior_P1_replication=replicas,
        output_hashes={f:digest(OUT/f) for f in FILES})
    assert not any(k in json.dumps(metrics) for k in ('"NPR"','"NRR"'))
    if write:
        write_json(OUT/'verification.json',result)
        print(json.dumps({k:v for k,v in result.items() if k!='prior_P1_replication'},indent=2),flush=True)
    return metrics,result


def report():
    m,verification=verify(write=False)
    write_json(OUT/'metrics.json',m)
    effects=dict(overall=m['overall']['delta_by_position'],by_difficulty={d:s['delta_by_position'] for d,s in m['by_difficulty'].items()},
        by_set={name:dict(set_mean_delta_by_position=s['set_mean_delta_by_position'],identities=s['identity_position_effects']) for name,s in m['sets'].items()})
    write_json(OUT/'position_effects.json',effects)
    routes=m['diagnostic_routes']
    gate=dict(measurement_valid=m['overall']['C_valid']['rate']==1,
        diagnostic_routes=routes,descriptive_outcome_flags=m['descriptive_outcome_flags'],
        downstream_calls=0,requires_new_clean_development_split=True,
        recommendation=('A diagnostic route is supported; future design must counterbalance candidate order and confirm on a new clean split.' if any(routes.values()) else
                        'No clean route is supported. Resolve answer-option order sensitivity before any propagation study.'),
        reason='Selected six-case control is diagnostic, not a new independent frontier confirmation.')
    gate['v3.5_authorized']=False
    write_json(OUT/'gate.json',gate)
    interpretations=dict(GOLD_STABLE='Gold identity survives all four list positions.',
        IDENTITY_LOCKED='The same non-gold identity survives all four list positions; identity/case effect within this set.',
        POSITION_1_LOCKED='Selection tracks position 1 in at least three orders while switching identities.',
        MIXED_POSITION_IDENTITY='Order changes choices, with no identity or absolute position selected more than twice.',
        UNSTABLE_OTHER='Not captured by the stable-identity/position-1/mixed rules; inspect the four responses.')
    rows=collect()
    inspection='# Candidate-order counterfactual inspection\n\nEach table is one repeated-measures set, not four independent cases. Only the numbered candidate list changes; name records, graph and question are fixed. Full F raw text and all candidate scores remain in the channel JSONL files. Margin is gold minus best wrong mean log probability, in nats/token.\n'
    for cid in CASE_IDS:
        for difficulty in CONDITIONS:
            s=m['sets'][f'{cid}/{difficulty}']
            subset=sorted([r for r in rows if r['case_id']==cid and r['difficulty']==difficulty],key=lambda r:r['permutation'])
            inspection+=f'\n## {cid} / {difficulty}\n\nGold: {s["gold"]}. **{s["classification"]}** — {interpretations[s["classification"]]}\n\n'
            inspection+='| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |\n|---|---|---|---|---|---:|---|---|---:|\n'
            for r in subset:
                inspection+='| '+' | '.join(map(cell,[f'P{r["permutation"]}']+r['C']['candidate_order']+[r['gold_position'],r['C']['selected_candidate'],r['L']['top_candidate_by_mean_logprob'],f'{margin(r):.4f}']))+' |\n'
            inspection+=f'\nISR={s["ISR"]:.2f}; literal PFR={rate(s["PFR"])}; strict PFR={rate(s["strict_PFR"])}; strict conditional PFR={rate(s["strict_conditional_PFR"])}.\n\n'
            for r in subset:
                flags=[]
                if not r['F']['exact_candidate_only']: flags.append('free format failure')
                if r['F']['extractable_candidate'] and r['F']['extractable_candidate']!=r['C']['selected_candidate']: flags.append('free/constrained disagreement')
                if r['L']['top_candidate_by_mean_logprob']!=r['C']['selected_candidate']: flags.append('likelihood/constrained disagreement')
                if flags:
                    inspection+=f'- P{r["permutation"]}: '+', '.join(flags)+'; raw F: '+cell(r['F']['raw_text'])+'\n'
            inspection+='\nAdjacent changes:\n\n'
            for t in s['transitions']:
                inspection+=f'- P{t["old_permutation"]}→P{t["new_permutation"]}: {t["old_choice"]} → {t["new_choice"]}; new first={t["new_pos1"]}; literal={t["literal_event"]}; strict={t["strict_event"]}.\n'
    (OUT/'inspection.md').write_text(inspection,encoding='utf-8',newline='\n')
    salvage='# Counterbalanced frontier diagnostics\n\nThese are the six deliberately selected cases, not a replacement clean development split. First summarize four orders per case, then aggregate six cases equally. The four rotations are not four new independent cases.\n'
    for difficulty,s in m['frontier_salvage'].items():
        salvage+=f'\n## {difficulty}: {s["condition"]}\n\n| Case | Error fraction across orders | Median gold margin | Near-boundary fraction | ISR | Classification |\n|---|---:|---:|---:|---:|---|\n'
        for c in s['per_case']:
            salvage+=f'| {c["case_id"]} | {c["error_fraction"]:.2f} | {c["median_gold_margin"]:.4f} | {c["near_boundary_fraction"]:.2f} | {c["ISR"]:.2f} | {c["classification"]} |\n'
        salvage+=f'\nEqual-case mean error={s["equal_case_mean_error"]:.1%}; median of six case median margins={s["median_of_case_median_margins"]:.4f}; equal-case mean NBF={s["equal_case_mean_near_boundary"]:.1%}; mean ISR={s["mean_ISR"]:.3f}. Heuristic frontier-like={s["heuristic_frontier_like"]}.\n\n'
        salvage+='PSR: '+ '; '.join(f'position {p}: {rate(value)}' for p,value in s['PSR'].items())+'.\n'
    salvage+='\n'+gate['recommendation']+' No automatic v3.5 authorization.\n'
    (OUT/'frontier_salvage.md').write_text(salvage,encoding='utf-8',newline='\n')
    o=m['overall']
    causal=o['order_sensitive_sets']>0
    flags=[name for name,value in m['descriptive_outcome_flags'].items() if value]
    special='; '.join(cid+': '+', '.join(d+'='+m['sets'][f'{cid}/{d}']['classification'] for d in CONDITIONS) for cid in ('dev-04','dev-07'))
    control='; '.join(cid+': '+', '.join(d+'='+m['sets'][f'{cid}/{d}']['classification'] for d in CONDITIONS) for cid in ('dev-06','dev-08'))
    boundary='; '.join(d+f': error fraction {m["sets"]["dev-05/"+d]["error_fraction"]:.2f}, median margin {m["sets"]["dev-05/"+d]["median_gold_margin"]:.4f}, '+m['sets']['dev-05/'+d]['classification'] for d in CONDITIONS)
    trajectories=[]
    for p in range(1,5):
        chosen=[next(r for r in rows if r['case_id']=='dev-05' and r['difficulty']==d and r['permutation']==p) for d in CONDITIONS]
        trajectories.append(dict(permutation=p,errors=[r['C']['selected_candidate']!=r['gold'] for r in chosen],margins=[margin(r) for r in chosen]))
    comparable=sum((not t['errors'][0] and t['errors'][1] and t['errors'][2] and t['margins'][0]>t['margins'][1]>=t['margins'][2]) for t in trajectories)
    write_json(OUT/'dev05_trajectories.json',trajectories)
    diagnosis='# v3.4.3 diagnosis\n\nCompleted 72 new prompts through F/C/L: 18 paired case-condition sets nested in six selected cases. Candidate-list order alone was manipulated; evidence order and graph content were unchanged. No independent-prompt significance test or population inference is made.\n\n'
    diagnosis+='Descriptive outcome flags: '+(', '.join(flags) or 'No single preregistered A/B/C/D pattern captures the full result')+'.\n\n'
    answers=[
        ('Does candidate position causally affect selection?',f'{o["order_sensitive_sets"]}/18 sets change selected identity across the four rotations. '+('With verified prompt invariance, this is a behavioral causal effect of the candidate-list-order intervention on these inputs.' if causal else 'No choice change was observed across the tested rotations; score effects may still occur.')),
        ('Is position 1 privileged?',f'PSR1={rate(o["PSR"]["1"])} versus the counterbalanced reference 0.25; position-1 locked sets={o["classifications"].get("POSITION_1_LOCKED",0)}/18. Mean position-1 Delta={o["delta_by_position"]["1"]["mean"]:.4f} nats/token; median of set means={o["delta_by_position"]["1"]["median"]:.4f}.'),
        ('Were prior errors position-driven or identity/case-driven?',f'Classification counts: {o["classifications"]}; mean ISR={o["mean_ISR"]:.3f}. Descriptive flags: {flags}. The selected control cases address major contributors but do not estimate a population fraction or assign a cause to every one of the prior 38 errors.'),
        ('What happens to dev-04 and dev-07?',special+'. Their old position-1 identity appears at positions 1,4,3,2 across P1–P4; inspect the identity and position traces rather than counting first-slot errors alone.'),
        ('Does dev-05 retain boundary crossing?',boundary+f'. A strict correct EASY / wrong MID and HARD pattern with decreasing margins survives in {comparable}/4 fixed-permutation trajectories. Full trajectories are in dev05_trajectories.json.'),
        ('Do always-easy controls remain stable?',control+'. GOLD_STABLE is required to call a case-condition robust across all four orders.'),
        ('Does position sensitivity increase with difficulty?','; '.join(f'{d}: PSR1={s["PSR"]["1"]["rate"]:.3f}, literal PFR={s["PFR"]["rate"]:.3f}, mean Delta1={s["delta_by_position"]["1"]["mean"]:.4f}' for d,s in m['by_difficulty'].items())+f'. Descriptive interaction flag C={m["descriptive_outcome_flags"]["C_difficulty_dependent_position"]}; this is not an internal cognitive-mechanism claim.'),
        ('Does the same identity receive higher likelihood in position 1?',f'Identity-matched Delta1 mean={o["delta_by_position"]["1"]["mean"]:.4f}; median of set means={o["delta_by_position"]["1"]["median"]:.4f}; identity-level median={o["delta_by_position"]["1"]["identity_level_median"]:.4f}. Each contrast holds identity, graph and question fixed; position_effects.json retains all contrasts.'),
        ('Do MID/HARD remain plausible frontier regimes?', '; '.join(d+f': equal-case error={s["equal_case_mean_error"]:.1%}, median-of-case-margins={s["median_of_case_median_margins"]:.4f}, NBF={s["equal_case_mean_near_boundary"]:.1%}, heuristic={s["heuristic_frontier_like"]}' for d,s in m['frontier_salvage'].items())+'. These summaries do not replace a new clean development/confirmation split.'),
        ('What exact order policy should future v3.5 use?',gate['recommendation']+' If future validation supports a propagation study, use the same four fixed cyclic rotations per case-condition so each identity occupies every slot once, keep evidence/name records canonical, preregister any randomized base order with a seed, and aggregate per case. This run does not authorize or launch v3.5.')]
    for i,(question,answer) in enumerate(answers,1):
        diagnosis+=f'{i}. **{question}** {answer}\n\n'
    diagnosis+='## Position-conditioned results\n\n| Position | PSR | Gold-position accuracy | Mean Delta | Median set-mean Delta |\n|---|---|---|---:|---:|\n'
    for p in map(str,range(1,5)):
        diagnosis+=f'| {p} | {rate(o["PSR"][p])} | {rate(o["GPA"][p])} | {o["delta_by_position"][p]["mean"]:.4f} | {o["delta_by_position"][p]["median"]:.4f} |\n'
    diagnosis+=f'\nLiteral PFR={rate(o["PFR"])}; strict PFR over all transitions={rate(o["strict_PFR"])}; conditional strict PFR={rate(o["strict_conditional_PFR"])}. Literal PFR does not require the previous first option to have been selected; it can include stable-identity transitions and must not be read alone.\n\n'
    diagnosis+=f'C validity={rate(o["C_valid"])}, F strict compliance={rate(o["FSC"])}, FCA={rate(o["FCA"])}, LCA={rate(o["LCA"])}. Free truncations={o["truncated"]}; short out-of-set-name flags={o["out_of_set"]}.\n\n'
    replicas=verification['prior_P1_replication']
    diagnosis+=f'All 18 P1 inputs match v3.4.2 byte-for-byte. New P1 C choices reproduce {sum(r["C_identical"] for r in replicas)}/18; free raw outputs reproduce {sum(r["free_raw_identical"] for r in replicas)}/18. Maximum mean-score difference={max(r["maximum_mean_score_difference"] for r in replicas):.8f}. All calls are newly run, not reused prior outputs.\n\n'
    diagnosis+='This tests candidate answer-list order, separately from v3.3 evidence order. Cyclic rotations balance absolute positions but do not exhaust all 24 orderings or isolate every relative-neighbor effect. A sequence that changes choices need not be purely position-1 driven; classifications and paired scores distinguish these patterns. No claim about internal attention or a shared internal primacy mechanism is supported.\n'
    (OUT/'diagnosis.md').write_text(diagnosis,encoding='utf-8',newline='\n')
    audit=(OUT/'design_audit.pre_inference.md').read_text(encoding='utf-8')
    audit+='\n## Post-run achievement table\n\n| Design intention | Observed achievement |\n|---|---|\n'
    outcomes=[('Separate position/identity',f'18 sets; all rotations verified; mean ISR={o["mean_ISR"]:.3f}'),
        ('Test list-position effect',f'{o["order_sensitive_sets"]}/18 choice-sensitive sets; PSR1={rate(o["PSR"]["1"])}'),
        ('Fixed evidence order','All fixed prefix/suffix hashes and graph audits passed'),('Complexity interaction','EASY/MID/HARD paired summaries reported; no independent-prompt inference'),
        ('Prior frontier','18 exact P1 input replications and per-case counterbalanced salvage summaries'),('Traceability','24 frozen mappings rechecked'),
        ('Format controls',f'C validity={rate(o["C_valid"])}; FCA={rate(o["FCA"])}; LCA={rate(o["LCA"])}'),
        ('Frozen case selection','All six specified cases completed; no additions or replacements'),('Narrow causal scope','Only candidate-list order changed; no internal-mechanism claim'),
        ('Calibration only','Zero downstream calls; no automatic v3.5 authorization')]
    audit+='\n'.join('| '+a+' | '+b+' |' for a,b in outcomes)+'\n'
    (OUT/'design_audit.md').write_text(audit,encoding='utf-8',newline='\n')
    write_json(OUT/'verification.json',verification)
    print(json.dumps(gate),flush=True)
