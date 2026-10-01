"""Read-only verification of the frozen run; save a derived verification report."""
import hashlib
import json
from pathlib import Path

from src.common import digest, read_jsonl
from src.experiment_v3_2 import analyze, build_prompt


def main():
    out = Path('results/smoke_v3_2')
    read = lambda name: json.loads((out / name).read_text(encoding='utf-8'))
    manifest = read('manifest.json')
    prep = read('preparation.json')
    plans = read('ablation_plan.json')
    rows = read_jsonl(out / 'trajectories.jsonl')
    cases = read_jsonl('data/candidates_v3_1.jsonl')
    case_map = {case['case_id']: case for case in cases}
    gate = read('gate.json')
    metrics, calculated_gate = analyze(cases, rows, gate['stop_reasons'])
    checks = {
        'frozen_data': digest('data/candidates_v3_1.jsonl') == prep['candidates_sha256'],
        'frozen_plan': digest(out / 'ablation_plan.json') == prep['plan_sha256'],
        'frozen_audit': digest(out / 'context_ablation_audit.md') == prep['audit_sha256'],
        'frozen_sources': all(digest(Path('src') / path) == value for path, value in manifest['source_code_sha256'].items()),
        'prior_artifacts': all(Path(path).is_file() and digest(path) == value for path, value in read('prior_artifact_hashes.json').items()),
        'metrics_recomputed': metrics == read('metrics.json'),
        'gate_recomputed': gate['passed'] == calculated_gate['passed'] and gate['quantitative_checks'] == calculated_gate['quantitative_checks'],
        'raw_hashes': all(hashlib.sha256(row['raw_generation'].encode('utf-8')).hexdigest() == row['raw_sha256'] for row in rows),
        'prompt_hashes': all(hashlib.sha256(row['prompt'].encode('utf-8')).hexdigest() == row['prompt_sha256'] for row in rows),
        'exact_frozen_prompts': all(row['prompt'] == build_prompt(case_map[row['case_id']], row['ablation'], row['condition'], plans[row['case_id']]) for row in rows),
        'isolated_calls': all(row['isolation'] == dict(user_messages=1, previous_messages=0, use_cache=False, past_key_values_supplied=False, fresh_tokenization=True) for row in rows),
        'raw_gate_binding': gate['trajectories_sha256'] == digest(out / 'trajectories.jsonl'),
        'inspection_gate_binding': gate['inspection_sha256'] == digest(out / 'inspection.md'),
    }
    report = dict(passed=all(checks.values()), calls=len(rows), checks=checks,
                  prior_files_checked=len(read('prior_artifact_hashes.json')))
    (out / 'verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
    if not report['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
