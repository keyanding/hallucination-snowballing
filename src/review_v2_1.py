"""Confirm provisional v2.1 mismatch diagnoses against saved evidence.

This review cannot change gates or silently add aliases after a run. Corrections
require a separately documented evaluation revision, not confirmation.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

from .common import digest, read_jsonl, write_jsonl
from .experiment_v2_1 import export_results, write_json


def apply_reviews(records, reviews):
    keys = [(r['id'], r['condition']) for r in reviews]
    if len(keys) != len(set(keys)):
        raise ValueError('Duplicate review')
    available = {(r['id'], r['condition']): r for r in records}
    if not set(keys) <= set(available):
        raise ValueError('Review does not identify a recorded call')
    result = copy.deepcopy(records)
    indexed = {(r['id'], r['condition']): r for r in result}
    for review in reviews:
        row = indexed[(review['id'], review['condition'])]
        raw_hash = hashlib.sha256(row['raw_generation'].encode('utf-8')).hexdigest()
        if review['raw_sha256'] != raw_hash or row['raw_sha256'] != raw_hash:
            raise ValueError('Raw output hash mismatch')
        if not review.get('reviewer'):
            raise ValueError('Reviewer required')
        pending = {key for key in ('step1_diagnosis', 'step2_diagnosis', 'final_diagnosis')
                   if row.get(key) and row[key]['review_required']}
        if set(review['fields']) != pending:
            raise ValueError('Review must cover exactly the pending fields')
        for key, confirmation in review['fields'].items():
            if confirmation['semantic_label'] != row[key]['semantic_label']:
                raise ValueError('Confirmation cannot relabel or change gates')
            if not confirmation.get('rationale') or not confirmation.get('evidence'):
                raise ValueError('Evidence and rationale required for every field')
            row[key].update(review_required=False, reason=confirmation['rationale'],
                            review_evidence=confirmation['evidence'], reviewer=review['reviewer'])
        row['review_required'] = False
        chosen = row['final_diagnosis'] if row['step2_diagnosis']['semantic_label'] == 'EXACT_CORRECT' else row['step2_diagnosis']
        row['reason'] = chosen['reason']
        row['semantic_review'] = dict(reviewer=review['reviewer'], raw_sha256=raw_hash)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--run', default='results/smoke_v2_1')
    parser.add_argument('--reviews', required=True)
    args = parser.parse_args()
    out = Path(args.run)
    target = out / 'reviewed_trajectories.jsonl'
    if target.exists():
        parser.error('Review already recorded; refusing overwrite')
    manifest = json.loads((out / 'manifest.json').read_text(encoding='utf-8'))
    if digest('data/candidates_v2.jsonl') != manifest['candidates_sha256']:
        parser.error('Candidate hash changed')
    raw_hash = digest(out / 'trajectories.jsonl')
    reviewed = apply_reviews(read_jsonl(out / 'trajectories.jsonl'), read_jsonl(args.reviews))
    write_jsonl(target, reviewed)
    export_results(out, read_jsonl('data/candidates_v2.jsonl'), reviewed, manifest,
                   read_jsonl('results/smoke_v2/trajectories.jsonl'))
    gate_path = out / 'gate.json'
    gate = json.loads(gate_path.read_text(encoding='utf-8'))
    gate.update(semantic_review='evidence-based mismatch confirmation completed' if not any(r['review_required'] for r in reviewed) else 'partial',
                reviews_sha256=digest(args.reviews), reviewed_trajectories_sha256=digest(target))
    write_json(gate_path, gate)
    assert digest(out / 'trajectories.jsonl') == raw_hash


if __name__ == '__main__':
    main()
