"""Recompute gates from exact raw outputs and publish an auditable report."""
import json
from .prepare import OUT, BOUNDARY, load, write, verify, digest
from .analyze import calibration_metrics, main_metrics, decide, CATEGORIES


def read_rows(name):
    return [json.loads(line) for line in (OUT/name).read_text(encoding='utf-8').splitlines() if line.strip()]


def report():
    verify()
    cal = read_rows('calibration_outputs.jsonl')
    main = read_rows('main_outputs.jsonl')
    plan = load('prompt_plan.json')
    for split, rows in [('calibration', cal), ('main', main)]:
        assert len(rows) == (160 if split == 'calibration' else len(rows))
        for expected, actual in zip(plan[split], rows):
            for key, value in expected.items():
                assert actual[key] == value, (split, key)
            import hashlib
            assert hashlib.sha256(actual['raw_text'].encode()).hexdigest() == actual['raw_sha256']
    cp, cm = calibration_metrics(load('calibration_cases.json'), cal)
    mp, mm = main_metrics(load('main_cases.json'), main)
    assert len(main) == (80 if cm['passed'] else 0)
    decision = decide(cm, mm)
    write('metrics.json', dict(calibration=cm, main=mm))
    write('gate.json', dict(decision=decision, calibration_pass=cm['passed'], main_run=bool(main), main_pass=mm['passed'] if main else None, calibration_calls=len(cal), main_calls=len(main)))
    (OUT/'parsed_outcomes.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in cp+mp), encoding='utf-8', newline='\n')
    table = ['| Gate | Count | Required | Pass |', '|---|---|---|---|']
    for k, v in cm['gates'].items():
        table.append(f"| {k} | {v['count']}/{v['denominator']} | ≥{v['minimum']} | {v['passed']} |")
    summary = ['# v3.6.0 propagation assay validation', '', f'**{decision}**', '',
               f'Calibration: {len(cal)}/160 calls. Main: {len(main)}/80 calls. No auxiliary calls.', '', '## Calibration', '', *table, '', '## Main', '']
    if main:
        for k in ('A_C', 'A_W', 'S'):
            v = mm['metrics'][k]
            low, high = v['wilson_95']
            summary.append(f"- {k}: {v['count']}/{v['denominator']} ({v['rate']:.1%}), Wilson 95% CI [{low:.1%}, {high:.1%}].")
        summary += [f"- Δstate: {mm['metrics']['delta_state']['numerator']}/40 = {mm['metrics']['delta_state']['rate']:.3f}.", '',
                    '| C0 → W0 | C | Cp | UNKNOWN | OTHER | INVALID |', '|---|---|---|---|---|---|']
        for a in CATEGORIES:
            summary.append('| '+a+' | '+' | '.join(str(mm['paired_transitions'][a][b]) for b in CATEGORIES)+' |')
        summary += ['', f"Main gates: {mm['gates']}.", '', f"Category counts: {mm['condition_counts']}.", 'Statistical unit: 40 paired base cases; 80 calls are not independent semantic populations.']
    else:
        summary += ['Main was not run because calibration failed. Main rates and intervals are null, not zero performance.']
    summary += ['', '## Interpretation', '', BOUNDARY if decision == 'ASSAY_VALIDATED' else 'The assay failed its frozen validity gate. No propagation conclusion is licensed.',
                'No evidence here establishes natural hallucination incidence, internal mechanisms, SHAR performance, or generalization to real-world tasks. No Phase II was run.', '',
                '## Reproducibility', '', 'Frozen seed 360; main shuffle 361; greedy generation seed 42; max_new_tokens 16; fresh calls; NF4/BF16 pinned Qwen3-4B.',
                'See spec.md, pre_registration.md, prompt_plan.json, prompt_diff_audit.md, decoding_freeze.json, case_manifest.json and inspection.md.']
    (OUT/'README.md').write_text('\n'.join(summary)+'\n', encoding='utf-8', newline='\n')
    inspection = ['# Full prompt and output inspection', '', 'Each entry shows the exact subquestion, supplied state, mappings, full prompt, raw output and strict parse. No first-hop question is run; the intermediate state is externally supplied.', '']
    for r in cp+mp:
        question = r['prompt'].split('Question:\n', 1)[1].split('\n\n', 1)[0]
        inspection += [f"## {r['case_id']} / {r['condition']}", '', f"Subquestion: {question}", f"Supplied intermediate: `{r['supplied_state']}`", f"Expected: `{r['expected']}`; parsed: {r['category']}; normalized: `{r['normalized']}`; truncated: {r['truncated']}",
                       f"Prompt SHA256: `{r['text_sha256']}`; rendered SHA256: `{r['rendered_sha256']}`", '', '```text', r['prompt'], '```', '', 'Raw output (JSON string):', '```json', json.dumps(r['raw_text'], ensure_ascii=False), '```', '']
    if not main:
        inspection += ['## Main', '', 'Not run: calibration validity gate failed.']
    (OUT/'inspection.md').write_text('\n'.join(inspection)+'\n', encoding='utf-8', newline='\n')
    pre = (OUT/'design_audit.pre_inference.md').read_bytes()
    post = '\n## Post-run audit\n\n'+'\n'.join(table)+f'\n\nFinal decision: {decision}. Main calls: {len(main)}. Frozen prompt, source and case hashes verified.\n'
    (OUT/'design_audit.md').write_bytes(pre+post.encode())
    prior = load('case_manifest.json')['prior_artifacts']
    for path, expected in prior.items():
        assert digest(path) == expected, path
    write('verification.json', dict(frozen_inputs_unchanged=True, prior_artifacts_unchanged=len(prior), calibration_calls=len(cal), main_calls=len(main), output_plan_exact=True, raw_hashes_valid=True, pre_audit_prefix_unchanged=(OUT/'design_audit.md').read_bytes().startswith(pre)))
    (OUT/'CHANGELOG.md').write_text('# v3.6.0\n\nNew isolated synthetic propagation assay. Before inference, user amendments added formal entity-label gate H (160 calibration calls) and a uniform explicit UNKNOWN instruction. Main remains 80 calls and original G1–G5.\n\nDecision: '+decision+'\n', encoding='utf-8', newline='\n')
    print('\n'.join(summary), flush=True)


if __name__ == '__main__':
    report()
