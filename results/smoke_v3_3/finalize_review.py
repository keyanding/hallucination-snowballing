"""Publish reviewed annotations without changing any raw generation or frozen code."""
import json

from src.common import digest, read_jsonl
from src.experiment_v3 import fraction, write_json
from src.experiment_v3_3 import OUT


def main():
    read = lambda name: json.loads((OUT / name).read_text(encoding='utf-8'))
    eligibility = read('eligibility_review.json')
    rows = read_jsonl(OUT / 'branch_trajectories.jsonl')
    if any(r['review_required'] for r in rows):
        raise ValueError('Unresolved downstream semantic mismatch; inspect before finalizing')
    text = (OUT / 'inspection.md').read_text(encoding='utf-8')
    text = text.replace('Resolution: ```json\n', '**Resolution**\n\n```json\n')
    marker = '<!-- reviewed-eligibility -->'
    if marker in text:
        raise ValueError('Review annotations already applied')
    for case_id, decision in eligibility['cases'].items():
        group = {r['branch']: r for r in rows if r['case_id'] == case_id}
        note = ('**Natural eligibility / B0:** ' + decision['natural_branch_status']
                + '. ' + decision['reason']
                + ' B0 was not run; downstream rows use the registered counterfactual alternative, not the natural answer.\n\n')
        if all(key in group for key in ('wrong/E0', 'wrong/E1', 'wrong/E2', 'wrong/E3a', 'wrong/E3b', 'S0')):
            labels = ' → '.join(group['wrong/' + e]['label'] for e in ('E0', 'E1', 'E2', 'E3a', 'E3b'))
            note += '**Wrong-branch sequence (E0/E1/E2/E3a/E3b):** ' + labels + '. '
            note += 'S0: ' + group['S0']['label'] + '. '
            if group['wrong/E0']['label'] != group['S0']['label']:
                note += 'Prefix sensitivity observed. '
            for role in ('gold', 'wrong'):
                if group[role + '/E3a']['raw_generation'] != group[role + '/E3b']['raw_generation']:
                    note += role.capitalize() + '-state conflict order changes the answer. '
            note += '\n\n'
        text = text.replace('## ' + case_id + '\n', '## ' + case_id + '\n\n' + note, 1)
    text = marker + '\n\n' + text
    (OUT / 'inspection.md').write_text(text, encoding='utf-8')
    verified = sum(d['reviewed_entity_identity_verified'] for d in eligibility['cases'].values())
    review = dict(reviewer='Codex frozen-source evidence and complete downstream target review',
                  downstream_calls_reviewed=len(rows), no_relabeling_or_alias_changes=True,
                  all_downstream_outputs_supported=all(r['label'] in ('EXACT_CORRECT', 'PROPAGATE', 'OVERRIDE_TO_GOLD', 'OTHER_CONTEXT_TARGET') for r in rows),
                  reviewed_wrong_entity_rate=fraction(verified, len(eligibility['cases'])),
                  identity_note='This source-backed manual review supersedes the narrow automatic indexed-entity flag for identity assessment only; raw Phase-A fields and recomputed metrics remain unchanged. Nine entities are named in frozen source; three identities remain unverified. No explicit required downstream mapping exists for any of the twelve.',
                  natural_error_eligible_count=0, natural_B0_calls=0,
                  first_hop_sha256=digest(OUT / 'first_hop_generations.jsonl'),
                  branch_trajectories_sha256=digest(OUT / 'branch_trajectories.jsonl'),
                  eligibility_sha256=digest(OUT / 'eligibility_review.json'),
                  diagnosis_sha256=digest(OUT / 'diagnosis.md'))
    write_json(OUT / 'review.json', review)
    gate = read('gate.json')
    gate.update(semantic_review='Codex completed; human scientific review pending',
                inspection_sha256=digest(OUT / 'inspection.md'), review_sha256=digest(OUT / 'review.json'),
                scientific_scope='Counterfactual branching only; NPR unavailable because no natural error has eligible downstream evidence')
    write_json(OUT / 'gate.json', gate)


if __name__ == '__main__':
    main()
