"""Recompute measurements and check the frozen provenance without model calls."""
import json
from pathlib import Path

from src.common import digest, read_jsonl
from src import experiment_v3_3 as exp


def main():
    out = exp.OUT
    read = lambda name: json.loads((out / name).read_text(encoding='utf-8'))
    exp.frozen_check()
    first = read_jsonl(out / 'first_hop_generations.jsonl')
    rows = read_jsonl(out / 'branch_trajectories.jsonl')
    cases = read_jsonl(exp.DATA)
    resolved, gate = read('resolved_cases.json'), read('gate.json')
    computed, computed_gate = exp.analyze(cases, first, rows, resolved, gate['stop_reasons'])
    first_map = {r['case_id']: r for r in first}
    review = read('eligibility_review.json')
    resolved_matches_review = True
    for case in cases:
        decision = review['cases'][case['case_id']]
        if decision['execute']:
            pair, origin, eligible = exp.resolve_pair(case, first_map[case['case_id']], decision)
            actual = resolved[case['case_id']]
            resolved_matches_review &= actual['pair'] == pair and actual['origin'] == origin and actual['natural_evidence_eligible'] == eligible
    exact_messages = True
    for r in rows:
        case = resolved[r['case_id']]['pair']
        if r['role'].startswith('direct'):
            state = case['B'] if r['role'] == 'direct_gold' else case['B_prime']
            expected = [dict(role='user', content=exp.control_prompt(case, state))]
        elif r['branch'] == 'S0':
            expected = [dict(role='user', content=exp.control_prompt(case, case['B_prime'], True))]
        else:
            state = None if r['branch'] == 'B0' else case['B'] if r['role'] == 'gold' else case['B_prime']
            expected = exp.branch_messages(case, first_map[r['case_id']]['raw_generation'], state, r['evidence_condition'])
        exact_messages &= r['messages'] == expected
    prior = read('prior_artifact_hashes.json')
    checks = dict(
        frozen_inputs_and_sources=True,
        metrics_recomputed=computed == read('metrics.json'),
        gate_recomputed=computed_gate['passed'] == gate['passed'] and computed_gate['checks'] == gate['checks'],
        exactly_twelve_first_hops=len(first) == 12 and len(first_map) == 12,
        raw_hashes=all(exp.sha(r['raw_generation']) == r['raw_sha256'] for r in first + rows),
        prompt_hashes=all(exp.sha(r['rendered_prompt']) == r['prompt_sha256'] for r in first + rows),
        checkpoint_hashes=all(exp.sha(r['prefix_checkpoint']) == r['prefix_checkpoint_sha256'] for r in first),
        first_hop_prefixes=all(r['prefix_checkpoint'].startswith(r['rendered_prompt'] + r['raw_generation']) for r in first),
        exact_preregistered_messages=exact_messages,
        exact_reviewed_case_resolution=resolved_matches_review,
        actual_checkpoint_replay=all(r['rendered_prompt'].startswith(r['branch_checkpoint']) for r in rows if r['branch_checkpoint'] is not None),
        per_call_isolation=all(not r['isolation']['use_cache'] and not r['isolation']['past_key_values_supplied'] and not r['isolation']['cross_branch_history'] for r in first + rows),
        pre_inference_audit_preserved=(out / 'branch_audit.md').read_bytes().startswith((out / 'branch_audit.pre_inference.md').read_bytes()),
        first_hop_review_binding=read('eligibility_review.json')['first_hop_sha256'] == digest(out / 'first_hop_generations.jsonl'),
        raw_gate_binding=gate['trajectories_sha256'] == digest(out / 'branch_trajectories.jsonl'),
        inspection_gate_binding=gate['inspection_sha256'] == digest(out / 'inspection.md'),
        prior_artifacts=all(Path(p).exists() and digest(p) == value for p, value in prior.items()),
    )
    report = dict(passed=all(checks.values()), checks=checks, prior_files_checked=len(prior),
                  model_calls=len(first) + len(rows), logical_B0_calls=sum('B0' in r['logical_branches'] for r in rows))
    exp.write_json(out / 'verification.json', report)
    print(json.dumps(report, indent=2))
    if not report['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
