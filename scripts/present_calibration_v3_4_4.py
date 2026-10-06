"""Supplementary descriptive tables, distinct from frozen primary selection."""
import json
import statistics
import random
import sys
from collections import Counter
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.prepare_v3_4_4 import OUT,load
from src.calibration_v3_4_4 import collect
from src.common import read_jsonl,digest
from src.experiment_v3 import write_json

rows=collect()
m=load('metrics.json')
plans={p['plan_id']:p for p in read_jsonl(OUT/'prompt_plan.jsonl')}
categories=['IN_SET_VALID','OUT_OF_SET','AMBIGUOUS','NONCOMPLIANT','TRUNCATED']
text='# Supplementary diagnostics\n\nThese tables add descriptive detail without altering the frozen policy, parser, hypotheses or confirmation decision. Categories with zero observations remain visible.\n\n## Full output taxonomy\n\n| Cohort | Difficulty | Interface | All | Valid | Out of set | Ambiguous | Noncompliant | Truncated | Wrong / valid | Wrong / all |\n|---|---|---|---|---|---|---|---|---|---|---|\n'
details=[]
for cohort in ('development','old','confirmation'):
    for difficulty in ('EASY','MID','HARD'):
        for interface in ('L','N','R'):
            sub=[r for r in rows if (r['cohort'],r['difficulty'],r['interface'])==(cohort,difficulty,interface)]
            if not sub:
                continue
            counts=Counter(r['F']['category'] for r in sub)
            wrong=sum(r['F']['strict_valid'] and r['F']['identity']!=r['gold'] for r in sub)
            vals=[str(counts[k]) for k in categories]
            text+='| '+' | '.join([cohort,difficulty,interface,str(len(sub)),*vals,f'{wrong}/{counts["IN_SET_VALID"]}',f'{wrong}/{len(sub)}'])+' |\n'
            mean_sum=sum(r['S']['top_candidate_by_mean_logprob']!=max(r['S']['scores'],key=lambda v:v['sum_logprob'])['candidate'] for r in sub)
            valid=[r for r in sub if r['F']['strict_valid']]
            score_free=sum(r['F']['identity']!=r['S']['top_candidate_by_mean_logprob'] for r in valid)
            fc=sum(r['F']['identity']!=r['C']['selected_candidate'] for r in valid) if interface=='L' else None
            cs=sum(r['C']['selected_candidate']!=r['S']['top_candidate_by_mean_logprob'] for r in sub) if interface=='L' else None
            details.append(dict(cohort=cohort,difficulty=difficulty,interface=interface,
                categories={k:counts[k] for k in categories},n=len(sub),F_valid=len(valid),F_S_disagree=score_free,F_C_disagree=fc,C_S_disagree=cs,
                S_sum_mean_disagree=mean_sum,Wait_outputs=sum('wait' in r['F']['raw_text'].lower() for r in sub),
                input_tokens_range=[min(plans[r['plan_id']]['input_tokens'] for r in sub),max(plans[r['plan_id']]['input_tokens'] for r in sub)],
                graph_tokens_range=[min(plans[r['plan_id']]['graph_tokens'] for r in sub),max(plans[r['plan_id']]['graph_tokens'] for r in sub)]))
text+='\nL F above is a shadow channel; primary L error rates use C. N/R are unconstrained. No invalid category is treated as a correct semantic response.\n\n## Channel disagreement and token lengths\n\n| Cohort / difficulty / interface | F valid | F vs S disagreements | F vs C | C vs S | S sum vs mean | Input tokens | Graph tokens |\n|---|---|---|---|---|---|---|---|\n'
for d in details:
    text+='| '+' | '.join([f'{d["cohort"]}/{d["difficulty"]}/{d["interface"]}',str(d['F_valid']),str(d['F_S_disagree']),str(d['F_C_disagree']),str(d['C_S_disagree']),str(d['S_sum_mean_disagree']),str(d['input_tokens_range']),str(d['graph_tokens_range'])])+' |\n'
text+='\nF comparisons exclude invalid outputs; C/S and sum/mean denominators are all renderings in the corresponding stratum. S excludes EOS. N/R candidate scores are diagnostic and impose no choice restriction on F. Mean normalization changes length weighting; no score is reported as calibrated probability. Case-bootstrap intervals describe this small case sample and do not model dependence from reused people. Zero-event bootstrap intervals can collapse to zero; they do not establish a zero population event rate.\n'
text+='\n## Gold-margin distributions and matched position shifts\n\nS remains available when F is invalid; these are unconditional score diagnostics. Quartiles describe all renderings, while shift intervals resample whole cases.\n\n| Cohort / difficulty / interface | Gold margin min / Q1 / median / Q3 / max | First-position shift mean [case-bootstrap 95%] |\n|---|---|---|\n'
margin_details=[]
for cohort,levels in m['cohorts'].items():
    for difficulty in levels:
        cells=[c for c in m['cells'] if c['cohort']==cohort and c['difficulty']==difficulty]
        for interface in ('L','N','R'):
            if interface not in cells[0]:
                continue
            values=[c['N']['gold_margin'] for c in cells] if interface=='N' else [v for c in cells for v in c[interface]['gold_margins']]
            qs=statistics.quantiles(values,n=4,method='inclusive')
            five=[min(values),qs[0],statistics.median(values),qs[2],max(values)]
            shift=None
            if interface!='N':
                per_case=[statistics.mean(v['first_minus_other_mean'] for v in c[interface]['first_score_shift']) for c in cells]
                rng=random.Random(344)
                samples=sorted(statistics.mean(rng.choices(per_case,k=len(per_case))) for _ in range(2000))
                shift=dict(mean=statistics.mean(per_case),lower=samples[49],upper=samples[1949])
            margin_details.append(dict(cohort=cohort,difficulty=difficulty,interface=interface,gold_margin_five_number=five,first_position_shift=shift))
            shift_text=f'{shift["mean"]:.4f} [{shift["lower"]:.4f}, {shift["upper"]:.4f}]' if shift else 'not manipulated'
            text+='| '+f'{cohort}/{difficulty}/{interface}'+' | '+' / '.join(f'{v:.4f}' for v in five)+' | '+shift_text+' |\n'
dev=m['cohorts']['development']
hypotheses=dict(
 H1=dict(supported=any(s['L_order_sensitive']['count']>0 for s in dev.values()) and statistics.mean(s['L_identity_first_score_shift'] for s in dev.values())>0,
    criterion='Identity changes on new L rotations plus positive aggregate identity-matched first-position score shift.'),
 H2=dict(supported=any(s['R_observed_order_sensitive']['count']>0 for s in dev.values()),criterion='At least two strict identities across equivalent R presentations, separately from invalid outputs.'),
 H3=dict(supported=all(m['paired_changes'][k]['HARD_minus_EASY_mean']>0 for k in ('L_sensitivity','L_first')),criterion='Paired HARD minus EASY positive for both L sensitivity and L first fraction; intervals and mixed cases reported, not a significance claim.'),
 H4=dict(supported=any(c['L']['robust_wrong'] or (c['R']['stable_four_of_four'] and c['R']['wrong_aggregate']) for c in m['cells'] if c['cohort']=='development') and any(c['L']['order_sensitive'] or c['R']['observed_order_sensitive'] for c in m['cells'] if c['cohort']=='development'),criterion='Requires both 4/4 same-wrong sets and identity-changing sets within L or R, analyzed separately. A 3/4 wrong aggregate is not 4/4 robustness.'))
text+='\n## Hypothesis decisions\n\nAbsent registered patterns are labeled unsupported, not rescued by a different metric.\n\n'
for k,v in hypotheses.items():
    text+=f'- {k}: **{"supported descriptively" if v["supported"] else "unsupported / registered pattern absent"}**. {v["criterion"]}\n'
# Explicitly exploratory all-interface diagnostic; not part of policy selection.
persistent=[]
for c in m['cells']:
    if c['cohort']!='development':
        continue
    if c['L']['robust_wrong'] and c['R']['stable_four_of_four'] and c['N']['valid']:
        identity=c['L']['identities'][0]
        if c['N']['identity']==identity and c['R']['identities'][0]==identity:
            persistent.append(dict(case_id=c['case_id'],difficulty=c['difficulty'],identity=identity))
text+='\n## Exploratory persistence across all nine matched observations\n\nThe same wrong identity across L1–L4 C, N F and R1–R4 F (all natural outputs strict-valid). This stronger post-run descriptive check was not used for selection:\n\n```json\n'+json.dumps(persistent,ensure_ascii=False,indent=2)+'\n```\n'
text+='\n## Artifact lifecycle\n\nThe original manifest freezes both design_audit.md and its identical pre-inference copy. The specification also requires appending a post-run table to design_audit.md. Its pre-inference prefix remains byte-identical and verifiable through design_audit.pre_inference.md; the independent verifier explicitly checks that prefix instead of falsely requiring the completed report to have the old whole-file hash. No prompt, parser, policy, generator, model parameter or source hash changed. Use scripts/verify_calibration_v3_4_4.py for post-report verification.\n'
(OUT/'supplementary_diagnostics.md').write_text(text,encoding='utf-8',newline='\n')
write_json(OUT/'supplementary_metrics.json',dict(descriptive_only=True,strata=details,margin_distributions=margin_details,hypotheses=hypotheses,exploratory_all_interface_wrong_persistence=persistent))
inspection_path=OUT/'inspection.md'
inspection=inspection_path.read_text(encoding='utf-8')
for cell in m['cells']:
    group=[r for r in rows if (r['cohort'],r['case_id'],r['difficulty'])==(cell['cohort'],cell['case_id'],cell['difficulty'])]
    n=next(r for r in group if r['interface']=='N')
    question=n['F']['prompt'].rsplit('\n\n',2)[-2]
    heading=f'## {cell["cohort"]} / {cell["case_id"]} / {cell["difficulty"]}\n\nGold: **{cell["gold"]}**. '
    original=heading+'Query: credited director reached from the synthetic Film by credited-director links.'
    replacement=heading+f'First-hop subquestion (N/R): `{question}`.'
    listed=next((r for r in group if r['interface']=='L'),None)
    if listed:
        replacement+=' Listed wording: `'+listed['F']['prompt'].rsplit('\n\n',2)[-2]+'`.'
        replacement+=f' Partial robustness (same wrong identity 3/4): {cell["L"]["partial_wrong_three_of_four"]}.'
    if 'R' in cell and cell['R']['wrong_label']:
        replacement+=' R wrong-state label: '+cell['R']['wrong_label']+'.'
    assert original in inspection
    inspection=inspection.replace(original,replacement,1)
inspection_path.write_text('\n'.join(line.rstrip() for line in inspection.splitlines())+'\n',encoding='utf-8',newline='\n')
for file in ('README.md','diagnosis.md'):
    p=OUT/file
    s=p.read_text(encoding='utf-8')
    s=s.replace('first-hop selection Error-yield', 'first-hop selection. Error-yield')
    dev_cells=[c for c in m['cells'] if c['cohort']=='development']
    stable_l=sum(c['L']['robust_wrong'] for c in dev_cells)
    stable_r=sum(c['R']['stable_four_of_four'] and c['R']['wrong_aggregate'] for c in dev_cells)
    wrong_aggregates=sum(c['R']['wrong_aggregate'] for c in dev_cells)
    resolved_aggregates=sum(c['R']['aggregate'] is not None for c in dev_cells)
    s+=f'\nWrong-state persistence on new development data: L same-wrong 4/4 = **{stable_l}/72 cells**; R same-wrong 4/4 = **{stable_r}/72 cells**; wrong R aggregates = **{wrong_aggregates}/{resolved_aggregates} resolved cells**. These 72 repeated cells belong to 24 base cases. A wrong canonical N answer alone does not establish an order-stable wrong state.\n'
    s+='\nSee [supplementary diagnostics](supplementary_diagnostics.md) for zero-inclusive category counts, explicit channel-disagreement denominators, token-length ranges and hypothesis decisions.\n'
    if file=='README.md':
        s+='\n![Development interface comparison](interface_comparison.png)\n'
    p.write_text(s,encoding='utf-8',newline='\n')
v=load('verification.json')
v['output_hashes']={n:digest(OUT/n) for n in v['required_files_present']}
write_json(OUT/'verification.json',v)
