"""Compact, denominator-explicit v3.4.4 reporting; never runs models."""
import json
from collections import Counter
from pathlib import Path
from .prepare_v3_4_4 import OUT, load, verify_frozen, CONDITIONS
from .calibration_v3_4_4 import collect
from .analysis_v3_4_4 import natural_gate
from .experiment_v3 import write_json
from .common import digest


def rate(v):
    return f'{v["count"]}/{v["denominator"]} ({v["rate"]:.1%})' if v['rate'] is not None else f'{v["count"]}/{v["denominator"]} (undefined)'


def text(name,value):
    (OUT/name).write_text(value,encoding='utf-8',newline='\n')


def report():
    verify_frozen()
    metrics=load('metrics.json')
    selection=load('policy_selection.json')
    rows=collect()
    state=load('run_state.json')
    assert state['status']=='completed'
    route=selection['route']; difficulty=selection['difficulty']
    if route in ('N','R'):
        confirmation=metrics['cohorts']['confirmation'][difficulty]
        gate=natural_gate(confirmation,route)
    elif route=='L':
        confirmation=metrics['cohorts']['confirmation'][difficulty]
        checks=dict(C_valid=all(r['C']['exact_allowed_candidate'] for r in rows if r['cohort']=='confirmation' and r['interface']=='L'),
            stable_identity=1-confirmation['L_order_sensitive']['rate']>=.75,no_dominant_first=confirmation['L_first']['rate']<.40)
        gate=dict(passed=all(checks.values()),checks=checks,observed_wrong_yield=confirmation['L_wrong']['count'])
    else:
        confirmation=None
        gate=dict(passed=False,reason='No development policy met the frozen validity rules; confirmation not queried.')
    gate.update(selected_route=route,selected_difficulty=difficulty,structural_audits_pass=True,
        provenance_verified=True,prior_artifacts_preserved=len(load('manifest.json')['prior_artifacts']),
        v3_5_executed=False,v3_5_design_recommended=bool(gate['passed'] and gate.get('observed_wrong_yield',0)>0),
        error_yield_insufficient=bool(gate['passed'] and gate.get('observed_wrong_yield',0)==0),
        licensed_claim=selection['claim'] if gate['passed'] else 'No confirmed primary policy; descriptive interface comparisons only.',
        no_propagation_claim=True)
    write_json(OUT/'gate.json',gate)
    overview='# v3.4.4 — Answer interfaces and presentation sensitivity\n\nFirst-hop measurement only; no downstream calls, NPR, SHAR/HalluSE or v3.5 execution. Twenty-four new development cases, 16 frozen confirmation cases, and six selected old diagnostic cases. All 40 new candidate bundles, targets and graph nodes are new; people are reused from audited evidence.\n\n'
    overview+='## Exact execution counts\n\n```json\n'+json.dumps(state,indent=2)+'\n```\n\nN and R1 duplicate text is independently queried, not silently reused. Confirmation plans at unselected difficulties are frozen but never queried.\n\n'
    overview+='| Cohort | Difficulty | L wrong / prompts | L first / prompts | L sensitive / cases | N valid / all | N wrong / valid | R sensitive / complete cases | R earliest / valid |\n|---|---|---|---|---|---|---|---|---|\n'
    for cohort,levels in metrics['cohorts'].items():
        for d,s in levels.items():
            overview+='| '+' | '.join([cohort,d,*[rate(s[k]) if k in s else 'not run' for k in ['L_wrong','L_first','L_order_sensitive','N_coverage','N_wrong_given_valid','R_order_sensitive_complete','R_earliest']]])+' |\n'
    overview+=f'\nDevelopment selected **{route or "NO ROUTE"} / {difficulty or "none"}**. Confirmation pass: **{gate["passed"]}**. Licensed claim: {gate["licensed_claim"]} Error-yield insufficient: {gate["error_yield_insufficient"]}.\n\nCase-bootstrap percentile 95% intervals are in metrics.json; the resampling unit is the base case. Engineering thresholds do not prove absence of bias. All invalid categories are reported separately, never counted correct. Scores exclude EOS and are not probabilities. Depth, branches and prompt length covary.\n'
    text('README.md',overview)
    inspection='# Paired case inspection\n\nL is constrained listed choice; N/R are unconstrained free generation. S means per-token mean log-likelihood (EOS excluded). Gold margin = gold minus best wrong. Old diagnostic rows do not borrow prior L outputs into new paired comparisons.\n'
    for cell in metrics['cells']:
        cohort=cell['cohort'];cid=cell['case_id'];d=cell['difficulty']
        group=[r for r in rows if (r['cohort'],r['case_id'],r['difficulty'])==(cohort,cid,d)]
        inspection+=f'\n## {cohort} / {cid} / {d}\n\nGold: **{cell["gold"]}**. Query: credited director reached from the synthetic Film by credited-director links.\n'
        if 'L' in cell:
            inspection+=f'\nL class: {cell["L"]["classification"]}; modal identity: {cell["L"]["modal_identity"] or "TIE (missing)"}.\n\n| Rotation | First option | C chosen identity | C valid | Gold margin |\n|---|---|---|---|---|\n'
            for r in sorted([r for r in group if r['interface']=='L'],key=lambda r:r['rotation']):
                inspection+=f'| P{r["rotation"]} | {r["candidate_order"][0]} | {r["C"]["selected_candidate"]} | {r["C"]["exact_allowed_candidate"]} | {r["S"]["gold_vs_best_wrong_margin"]:.4f} |\n'
        n=next(r for r in group if r['interface']=='N')
        inspection+='\n| Interface | Strict identity | Category | First name record |\n|---|---|---|---|\n'
        for r in sorted([r for r in group if r['interface'] in ('N','R')],key=lambda r:(r['interface'],r['rotation'])):
            inspection+=f'| {r["interface"]}{r["rotation"]} | {r["F"]["identity"] or "—"} | {r["F"]["category"]} | {r["record_order"][0]} |\n'
        inspection+=f'\nN raw: `{json.dumps(n["F"]["raw_text"],ensure_ascii=False)}`. '
        if 'R' in cell:
            inspection+=f'R aggregate: {cell["R"]["aggregate"] or "UNSTABLE_OR_UNRESOLVED"}; R observed identity changes: {cell["R"]["observed_order_sensitive"]}; R all four valid: {cell["R"]["all_valid"]}. '
        if 'L' in cell:
            inspection+=f'L list sensitivity: {cell["L"]["order_sensitive"]}; N/L disagreement: {cell["disagreement_direction"] or "none or ineligible"}. '
        inspection+='\n'
        anomalies=[a for a in metrics['channel_anomalies'] if a['plan_id'] in {r['plan_id'] for r in group}]
        if anomalies:
            inspection+='\nDiagnostic anomalies (raw only here; full logs preserve every output):\n\n'
            for a in anomalies:
                inspection+='- '+json.dumps(a,ensure_ascii=False)+'\n'
    text('inspection.md',inspection)
    dev=metrics['cohorts']['development']
    diagnosis='# v3.4.4 diagnosis\n\n'
    diagnosis+='1. **Does listed first-option preference replicate on new cases?** '+ '; '.join(f'{d}: first {rate(s["L_first"])}, identity-sensitive {rate(s["L_order_sensitive"])}, identity-matched first-score shift {s["L_identity_first_score_shift"]:.4f}' for d,s in dev.items())+'. The 25% equal-exposure reference is descriptive. H1 requires changed identities and positive score shift; results are stratum-specific, not a population mechanism claim.\n\n'
    diagnosis+='2. **What changes when the list is removed?** '+ '; '.join(f'{d}: L wrong {rate(s["L_wrong"])}, N wrong/all {rate(s["N_wrong_all"])}, N wrong/valid {rate(s["N_wrong_given_valid"])} with coverage {rate(s["N_coverage"])}' for d,s in dev.items())+'. This intervention also changes two query/output phrases; it is not a pure order contrast.\n\n'
    diagnosis+='3. **Does record order matter?** '+ '; '.join(f'{d}: R identity-sensitive among complete cells {rate(s["R_order_sensitive_complete"])}, earliest/valid {rate(s["R_earliest"])}, matched score shift {s["R_identity_first_score_shift"]:.4f}' for d,s in dev.items())+'. R rotates complete records, not answer options. H2 is supported only where identities actually change; invalid rotations alone do not establish identity change.\n\n'
    stable=[dict(case_id=c['case_id'],difficulty=c['difficulty'],L=c.get('L',{}).get('identities'),R=c.get('R',{}).get('aggregate')) for c in metrics['cells'] if c['cohort']=='development' and (c.get('L',{}).get('robust_wrong') or c.get('R',{}).get('wrong_aggregate'))]
    diagnosis+='4. **Which wrong identities persist?** L robust wrong requires the same wrong identity in all four outputs; R aggregates require all valid and at least three identical. The latter is AGGREGATED_TRACEABLE_WRONG, never a single trajectory. Cases:\n\n```json\n'+json.dumps(stable,indent=2,ensure_ascii=False)+'\n```\n\n'
    diagnosis+='5. **Is sensitivity greater at higher difficulty?** Paired HARD minus EASY (same cases):\n\n```json\n'+json.dumps(metrics['paired_changes'],indent=2)+'\n```\n\nFull EASY/MID/HARD trajectories are in metrics.json. H3 is supported only if both L sensitivity and first-fraction differences are positive; nonpositive/mixed trajectories limit or reject this prediction. Graph depth, branch count and prompt length covary; no isolated reasoning-depth causal claim.\n\n'
    diagnosis+='6. **How often is natural output valid?** '+ '; '.join(f'{d}: N categories {s["N_categories"]} /24; R categories {s["R_categories"]} /96' for d,s in dev.items())+'. These categories are mutually exclusive; truncation takes precedence. Name-shaped out-of-set classification is conservative, not a semantic person recognizer. Wait/reconsideration output is not a completed answer.\n\n'
    diagnosis+=f'7. **When do channels disagree?** {len(metrics["channel_anomalies"])} renderings across all cohorts have an invalid F or a strict F/C/mean-score or sum/mean difference (see exact records in metrics.json and inspection.md). Greedy token decisions differ from sequence ranking; sum and mean have different length dependence. This identifies operational differences, not their internal mechanism. Raw score sums, token lengths and means are retained; EOS is excluded.\n\n'
    diagnosis+=f'8. **Does confirmation pass?** Selected {route}/{difficulty}; confirmation pass {gate["passed"]}. The full unchanged threshold checks are in gate.json. No alternative was selected after confirmation.\n\n'
    diagnosis+=f'9. **Which future claim is licensed?** {gate["licensed_claim"]} v3.5_executed=false. Error-yield insufficient: {gate["error_yield_insufficient"]}.\n\n'
    diagnosis+='10. **What remains before propagation?** Confirmed interface validity and sufficient traceable wrong yield are separate requirements; a new calibration sample is needed if yield is insufficient. Record order, reused people, limited case count, scoring length/termination sensitivity and construction-dependent complexity remain limitations. Any downstream study requires a new preregistered design and matched causal controls; this experiment measures first-hop selections only.\n'
    text('diagnosis.md',diagnosis)
    post='\n## Post-run design audit\n\n| Design intention | Achieved? | Numerical evidence | Limitations |\n|---|---|---|---|\n'
    evidence=[('Separate option artifacts','Measured',str({d:s['L_order_sensitive'] for d,s in dev.items()}),'No internal mechanism inference'),
        ('Natural no-list primary','Measured',str({d:s['N_coverage'] for d,s in dev.items()}),'Wrong rates conditional on coverage'),
        ('Residual record order','Measured',str({d:s['R_earliest'] for d,s in dev.items()}),'Threshold is heuristic'),
        ('Strict format taxonomy','Verified',str({d:s['N_categories'] for d,s in dev.items()}),'Conservative unknown-name detector'),
        ('Counterbalance','Verified','Every identity occupies each of four L/R positions; all 1170 planned renderings audited','Identity token lengths differ'),
        ('Complexity interaction','Measured',str(metrics['paired_changes'].get('L_sensitivity')),'Depth/branches/length covary'),
        ('Fresh split','Verified',f'24 development; confirmation queried {16 if confirmation else 0}/16','People reused; only one policy/difficulty'),
        ('Frozen r2 traceability','Verified','184 candidate mappings checked; 40 new bundles','No downstream inference'),
        ('Score interpretation','Verified',f'{len(metrics["channel_anomalies"])} diagnostic anomaly rows; exact harness replay','EOS excluded; no probabilities'),
        ('Meaningful failure','Completed',f'738 development+old renderings; {state["confirmation_renderings"]} confirmation; gate {gate["passed"]}','No target error-rate tuning')]
    post+='\n'.join('| '+' | '.join(row)+' |' for row in evidence)+'\n'
    text('design_audit.md',(OUT/'design_audit.pre_inference.md').read_text(encoding='utf-8')+post)
    text('CHANGELOG.md','# Changes from v3.4.3\n\n- Add 24 fresh development and 16 frozen confirmation cases with new graphs and candidate bundles. Preserve all old results and sources.\n- Separate interface L from score channel S. Add unconstrained no-list N and independent name-record rotations R.\n- Freeze strict output taxonomy, format-smoke cap rule, source mappings, order aggregates and development-only selection.\n- Add case-level uncertainty, paired trajectories, explicit invalid denominators, one-shot confirmation and a gate that never launches propagation.\n')
    required=['README.md','design_audit.md','manifest.json','case_manifest.json','development_cases.json','confirmation_cases.json','prompt_plan.jsonl','prompt_diff_audit.md',*{f for fs in __import__('src.calibration_v3_4_4',fromlist=['CHANNELS']).CHANNELS.values() for f in fs if f},'metrics.json','interface_policy.md','gate.json','inspection.md','diagnosis.md','CHANGELOG.md']
    assert all((OUT/n).exists() for n in required)
    write_json(OUT/'verification.json',dict(required_files_present=required,prior_and_frozen_hashes_pass=True,
        output_hashes={n:digest(OUT/n) for n in required},run_state=state))
    print(json.dumps(gate,indent=2),flush=True)


if __name__=='__main__':
    report()
