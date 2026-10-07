"""Report all paired contrasts and frozen gates; no post-hoc optimization."""
import json
from .prepare import OUT, load, write, text, verify, digest
from .analyze import stage_b, stage_c, decision
from .run import STAGES


def report():
    verify()
    rows = {k:[json.loads(s) for s in (OUT/(k+'_outputs.jsonl')).read_text(encoding='utf-8').splitlines()] for k in STAGES}
    for k in STAGES:
        plan = load(k+'_prompt_plan.json')
        assert len(rows[k]) <= len(plan)
        for p, r in zip(plan, rows[k]):
            assert all(r[key] == value for key, value in p.items())
    bp, bm = stage_b(load('stage_b_cases.json'), rows['stage_b'])
    cp, cm = stage_c(load('stage_c_cases.json'), load('unmapped_cases.json'), rows['stage_c'], rows['unmapped'], rows['record_order'])
    final = decision(bm, cm, (OUT/'failure.json').exists())
    available = load('stronger_model_availability.json')
    assert not available['compatible_stronger_model_available']
    stronger = dict(status='STRONGER_MODEL_DIAGNOSTIC_NOT_RUN', stage_c_invalid_trigger=final == 'MINIMAL_ASSAY_INVALID',
                    stage_b_P3=bm['P3'], reason=available['reason'],
                    failed_mapped_prompts=[dict(case_id=r['case_id'], condition=r['condition'], text_sha256=r['text_sha256']) for r in cp if r['stage'] == 'stage_c' and not r['correct']])
    write('stronger_model_diagnostic.json', stronger)
    write('stage_b_metrics.json', bm)
    write('stage_c_metrics.json', cm)
    gate = dict(stage_b_completed=bm['complete'], stage_b_best_descriptive_condition=bm['best_descriptive_conditions'],
                stage_c_pass=cm['passed'] if cm['all_primary_complete'] else None,
                record_order_diagnostic_pass=cm['record_order']['passed'] if cm['record_order']['complete'] else None,
                stronger_model_diagnostic_status=stronger['status'], final_decision=final)
    write('gate.json', gate)
    text('parsed_outcomes.jsonl', ''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in bp+cp))
    btable = ['| Family | Gold /20 | Wrong /20 | Paired /20 | False UNKNOWN /40 | OTHER+INVALID /40 |', '|---|---|---|---|---|---|']
    for name, group in bm['families'].items():
        m = group['metrics']
        btable.append('| '+name+' | '+' | '.join(str(m[k]['count']) for k in ('A_C', 'A_W', 'S', 'U', 'OTHER_INVALID'))+' |')
    primary = cm['metrics']
    counts = [primary['A_C']['count'], primary['A_W']['count'], primary['S']['count'], primary['U']['count'], primary['OTHER_INVALID']['count'], cm['fallback']['count']]
    ctable = ['| Gate | Count | Required | Pass |', '|---|---|---|---|']
    for k, count, denom, threshold in zip(cm['gates'], counts, (40,40,40,80,80,10), ('≥39','≥39','≥39','=0','≤1','≥9')):
        ctable.append(f"| {k} | {count}/{denom} | {threshold} | {cm['gates'][k]} |")
    reverse = cm['record_order']
    summary = ['# v3.6.1 minimal propagation diagnosis', '', '**'+final+'**', '',
               'Calls: '+', '.join(f'{k}={len(rows[k])}' for k in STAGES)+'. Total '+str(sum(map(len, rows.values())))+'.',
               '', '## Stage B: all old cases', '', *btable, '',
               'Best descriptive family (all ties): '+', '.join(bm['best_descriptive_conditions'])+'. Stage C was fixed independently.',
               'FULL_UNKNOWN uses the new shorter UNKNOWN rule, so it is not a byte-identical replay of v3.6.0.',
               '', '## Stage C: fresh cases', '', *ctable, '']
    for k in ('A_C', 'A_W', 'S'):
        m = primary[k]
        if m['wilson_95']:
            summary.append(f"- {k}: {m['count']}/40; Wilson 95% CI [{m['wilson_95'][0]:.1%}, {m['wilson_95'][1]:.1%}].")
    summary += ['', f"Record-order diagnosis: {reverse['count']}/20 unchanged mapped identity; requires ≥19/20; pass={reverse['passed']}. This does not alter C1–C6."]
    if reverse['complete'] and not reverse['passed']:
        summary += ['**Limitation: record-order robustness failed. Validation of the primary prompt must not be interpreted as order robustness or readiness for a more complex assay.**']
    summary += ['', stronger['status']+': '+stronger['reason'], '',
                'Validation, if achieved, concerns only explicit symbolic state-to-outcome following under the minimal prompt. No natural hallucination, multi-hop snowballing, SHAR, internal mechanism or real-world generalization claim.',
                '', 'See diagnosis.md, v360_failure_audit.md, inspection.md, pre_registration.md, prompt_diff_audit.md and machine-readable metrics. Rebuild reporting with `python -m experiments.v3_6_1.report`.']
    text('README.md', '\n'.join(summary)+'\n')
    diagnosis = ['# Diagnosis', '', '**'+final+'**', '', '## Static audit', '',
                 'See v360_failure_audit.md for all 20 cases and per-identifier tokens. Associations are descriptive; 20 cases cannot identify lexical causes.',
                 '', '## Paired Stage B factors', '']
    comparisons = [('FULL_UNKNOWN', 'FULL_NO_UNKNOWN', 'UNKNOWN removal, full'), ('MINIMAL_UNKNOWN', 'MINIMAL_NO_UNKNOWN', 'UNKNOWN removal, minimal'),
                   ('FULL_UNKNOWN', 'MINIMAL_UNKNOWN', 'Simplification, UNKNOWN'), ('FULL_NO_UNKNOWN', 'MINIMAL_NO_UNKNOWN', 'Simplification, no UNKNOWN')]
    for a,b,label in comparisons:
        x, y = bm['families'][a]['metrics'], bm['families'][b]['metrics']
        t = bm['paired_transitions'][a+' -> '+b]
        diagnosis.append(f"- {label}: mapped accuracy {x['mapped_correct']['count']}/40 → {y['mapped_correct']['count']}/40; false UNKNOWN {x['U']['count']}/40 → {y['U']['count']}/40; paired corrected {t['corrected']}, broken {t['broken']}.")
    if bm['complete']:
        unknown_effects = [(bm['families'][a]['metrics'], bm['families'][b]['metrics']) for a,b,_ in comparisons[:2]]
        supports = [y['mapped_correct']['count'] > x['mapped_correct']['count'] and y['U']['count'] < x['U']['count'] for x,y in unknown_effects]
        minimal_effects = [(bm['families'][a]['metrics'], bm['families'][b]['metrics']) for a,b,_ in comparisons[2:]]
        complexity = [y['mapped_correct']['count'] > x['mapped_correct']['count'] for x,y in minimal_effects]
        diagnosis += ['', f'Directional support for fallback interference in full/minimal matched contrasts: {supports}. Magnitudes above are descriptive, with no significance or internal-mechanism claim.',
                      f'Directional support for simplification in UNKNOWN/no-UNKNOWN matched contrasts: {complexity}. This bundles syntax, prose and entity removal; it does not isolate entity scaffolding.',
                      f"P3 (MINIMAL_NO_UNKNOWN fails more than1/40): {bm['P3']}. Stage C runs independently; stronger-model execution is governed by Section10."]
    diagnosis += ['', '## Fresh validation', '', *ctable, '',
                  'All cases were selected by frozen lexical/tokenization criteria only. Stage C changes the identifier family as well as using the minimal prompt; it does not by itself separate prompt and dataset causes.',
                  f"Order: {reverse['count']}/20 unchanged; correct reversed outputs {reverse['correct']}/20.", '',
                  stronger['status']+'. No stronger-model result or model-size causal claim is available.',
                  '', '## Complete paired family transitions', '']
    for comparison, data in bm['paired_transitions'].items():
        diagnosis += ['### '+comparison, '', '| Case | State | Before | After | Before correct | After correct |', '|---|---|---|---|---|---|']
        for r in data['cases']:
            diagnosis.append(f"| {r['case_id']} | {r['condition']} | {r['before_output']} | {r['after_output']} | {r['correct_before']} | {r['correct_after']} |")
        diagnosis.append('')
    text('diagnosis.md', '\n'.join(diagnosis)+'\n')
    inspection = ['# Exact questions, prompts and outputs', '', 'Only downstream mapping questions are executed. There is no first-hop model call. Supplied states are externally fixed.', '']
    for r in bp+cp:
        query = r['prompt'].split('Question:\n')[-1].split('\n\n')[0] if 'Question:\n' in r['prompt'] else r['prompt'].split('\n\n')[-1]
        inspection += [f"## {r['stage']} / {r['case_id']} / {r['family']} / {r['condition']}", '', f"Query: {query}",
                       f"Supplied intermediate: `{r['supplied_state']}`; expected `{r['expected']}`; category {r['category']}; correct={r['correct']}; truncated={r['truncated']}.",
                       f"Prompt hash: `{r['text_sha256']}`; rendered hash: `{r['rendered_sha256']}`.", '', '```text', r['prompt'], '```', '', 'Raw output:', '```json', json.dumps(r['raw_text'], ensure_ascii=False), '```', '']
    text('inspection.md', '\n'.join(inspection)+'\n')
    pre = (OUT/'design_audit.pre_inference.md').read_bytes()
    (OUT/'design_audit.md').write_bytes(pre+('\n## Post-inference audit\n\n'+'\n'.join(btable)+'\n\n'+'\n'.join(ctable)+f"\n\nOrder invariant {reverse['count']}/20. Decision {final}. Frozen hashes verified.\n").encode())
    for path, expected in load('manifest.json')['prior_artifacts'].items():
        assert digest(path) == expected, path
    write('verification.json', dict(frozen_inputs_unchanged=True, prior_artifacts_unchanged=len(load('manifest.json')['prior_artifacts']), exact_output_plan_match=True, calls={k:len(v) for k,v in rows.items()}))
    text('CHANGELOG.md', '# v3.6.1\n\nStatic audit of all old calibration cases, 2×2 prompt replay, fresh token-balanced minimal primitive, separate fallback/order controls. All inputs frozen before 270 planned calls. No historical artifact modified.\n\nFinal decision: '+final+'\n')
    print('\n'.join(summary), flush=True)


if __name__ == '__main__':
    report()
