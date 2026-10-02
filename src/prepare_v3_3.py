"""Freeze twelve cases and a provenance index before natural first-hop inference."""
from collections import defaultdict
import copy
import json
from pathlib import Path

from .common import digest, norm, read_jsonl, write_jsonl
from .prepare_v3_1 import aliases, source_case
from .experiment_v3 import write_json


EXTRA = [
    ('022a3dd40bdd11eba7f7acde48001122', 'ba289b440bdb11eba7f7acde48001122'),
    ('06c74c8c0bde11eba7f7acde48001122', 'b0a2e8ba0bd911eba7f7acde48001122'),
]


def prepare():
    target = Path('data/candidates_v3_3.jsonl')
    registry_path = Path('data/evidence_index_v3_3.json')
    if target.exists() or registry_path.exists():
        raise FileExistsError('Frozen v3.3 data already exists')
    source = Path('data/dev.json')
    rows = json.loads(source.read_text(encoding='utf-8'))
    expected = json.loads(Path('data/candidates_v3_1.manifest.json').read_text(encoding='utf-8'))
    if digest(source) != expected['source_sha256']:
        raise ValueError('Different frozen evidence source')
    by_id = {r['_id']: r for r in rows}
    objects = defaultdict(set)
    for row in rows:
        for s, relation, o in row.get('evidences', []):
            objects[norm(s), relation].add(norm(o))
    cases = copy.deepcopy(read_jsonl('data/candidates_v3_1.jsonl'))
    for source_id, donor_id in EXTRA:
        gold = source_case(by_id[source_id], objects)
        donor = source_case(by_id[donor_id], objects)
        a, b = gold['path']
        da, db = donor['path']
        if b[1] != db[1] or norm(b[2]) == norm(db[2]):
            raise ValueError('Invalid donor')
        cases.append(dict(source_id=source_id, donor_id=donor_id,
                          original_question=by_id[source_id]['question'], A=a[0], r1=a[1],
                          B=a[2], relation=b[1], C=b[2], B_prime=da[2], C_prime=db[2],
                          aliases_C=aliases(b[2]), aliases_C_prime=aliases(db[2]),
                          gold_evidence_chain=gold['path'], donor_evidence_chain=donor['path'],
                          first_hop_evidence=gold['first'], downstream_evidence=gold['second'],
                          donor_first_hop_evidence=donor['first'], donor_downstream_evidence=donor['second']))
    for i, case in enumerate(cases, 1):
        case.update(case_id=f'natural-{i:02}', evidence_order=1 if i % 2 else 2,
                    aliases_B=aliases(case['B']), aliases_B_prime=aliases(case['B_prime']))
    # Candidate evidence, not automatically certified facts. An observed natural
    # alternative requires explicit sentence/identity/granularity review before use.
    index = []
    for row in sorted(rows, key=lambda r: r['_id']):
        context = dict(row['context'])
        for s, relation, o in row.get('evidences', []):
            if relation not in ('father', 'place of birth', 'place of death'):
                continue
            support = [dict(title=t, sentence_id=i, text=context[t][i])
                       for t, i in row['supporting_facts']
                       if t in context and 0 <= i < len(context[t])
                       and norm(t) == norm(s) and norm(o) in norm(context[t][i])]
            if support and len(objects[norm(s), relation]) == 1:
                index.append(dict(entity=s, relation=relation, target=o,
                                  entity_aliases=aliases(s), target_aliases=aliases(o),
                                  source_id=row['_id'], evidence=support))
    write_jsonl(target, cases)
    write_json(registry_path, index)
    write_json(target.with_suffix('.manifest.json'), dict(
        count=12, source_sha256=digest(source), candidates_sha256=digest(target),
        evidence_index_sha256=digest(registry_path), source='2WikiMultiHopQA frozen dev.json',
        selection='Previous ten cases retained regardless of outcomes; two additions reviewed before v3.3 inference. Four cases per relation. Donors for additions reuse previously reviewed donors.',
        previous_results_known=True, v33_inference_used_in_selection=False,
        evidence_index_note='Frozen lookup candidates only; substring presence alone does not certify a relation. Natural alternative entries require review.',
        source_code_sha256=digest(__file__)))


if __name__ == '__main__':
    prepare()
