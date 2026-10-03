"""Verify completed or early-stopped v3.4 without another model call."""
import json
from pathlib import Path

from src.common import digest, read_jsonl
from src import experiment_v3_4 as exp


def main():
    out = exp.OUT
    read = lambda name: json.loads((out / name).read_text(encoding='utf-8'))
    exp.frozen_check()
    cases = read_jsonl(exp.DATA)
    cm = {c['case_id']: c for c in cases}
    first = read_jsonl(out / 'first_hop_generations.jsonl')
    fm = {r['case_id']: r for r in first}
    records = read_jsonl(out / 'branch_trajectories.jsonl')
    logical, gate = read('logical_branches.json'), read('gate.json')
    metrics, computed_gate = exp.analyze(cases, first, records, logical, gate['stop_reasons'])
    expected_messages = True
    labels = True
    for row in records:
        case = cm[row['case_id']]
        if row['branch'].startswith('lookup/') or row['branch'] == 'S0':
            expected = [dict(role='user', content=exp.lookup_prompt(case, row['state'], row['branch'] == 'S0'))]
        else:
            expected = exp.branch_messages(case, fm[row['case_id']]['raw_generation'], None if row['branch'] == 'N0' else row['state'])
        expected_messages &= row['messages'] == expected
        parsed = exp.parse_answer(row['raw_generation'], row.get('truncated', False))
        label, selected = exp.downstream_label(case, parsed, row['state'])
        labels &= label == row['label'] and selected == row['selected_candidate']
    prior = read('prior_artifact_hashes.json')
    checks = dict(
        frozen_inputs_and_sources=True,
        candidate_audits=all(all(exp.audit_case(c).values()) for c in cases),
        metrics_recomputed=metrics == read('metrics.json'),
        gate_recomputed=gate['passed'] == computed_gate['passed'] and gate['checks'] == computed_gate['checks'],
        raw_hashes=all(exp.sha(r['raw_generation']) == r['raw_sha256'] for r in first + records),
        prompt_hashes=all(exp.sha(r['rendered_prompt']) == r['prompt_sha256'] for r in first + records),
        first_prompt_exact=all(r['messages'] == [dict(role='user', content=exp.first_prompt(cm[r['case_id']]))] for r in first),
        first_classification=all(exp.classify_first(cm[r['case_id']], r)['first_hop_label'] == r['first_hop_label'] for r in first),
        natural_checkpoints=all(exp.sha(r['prefix_checkpoint']) == r['checkpoint_sha256'] and r['prefix_checkpoint'].startswith(r['rendered_prompt'] + r['raw_generation']) for r in first),
        downstream_messages=expected_messages, downstream_labels=labels,
        branch_replay=all(r['rendered_prompt'].startswith(r['branch_checkpoint']) for r in records if r['branch_checkpoint'] is not None) if records else None,
        isolation=all(not r['isolation']['cross_branch_history'] and not r['isolation']['use_cache'] and not r['isolation']['past_key_values_supplied'] for r in first + records),
        early_stop_respected=not records if exp.phase_a_stop(first) else True,
        first_gate_binding=gate['first_hop_sha256'] == digest(out / 'first_hop_generations.jsonl'),
        raw_gate_binding=gate['trajectories_sha256'] == digest(out / 'branch_trajectories.jsonl'),
        inspection_gate_binding=gate['inspection_sha256'] == digest(out / 'inspection.md'),
        prior_artifacts=all(Path(p).is_file() and digest(p) == h for p, h in prior.items()))
    report = dict(passed=all(v is not False for v in checks.values()), checks=checks,
                  actual_model_calls=len(first) + len(records), prior_files_checked=len(prior),
                  note='Null branch_replay means no downstream calls were permitted by the stop rule; it is not a passed empirical branch check.')
    exp.write_json(out / 'verification.json', report)
    print(json.dumps(report, indent=2))
    if not report['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
