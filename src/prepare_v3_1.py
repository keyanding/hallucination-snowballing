"""Evidence-reviewed fixed real cases; no model-based candidate selection."""
from collections import defaultdict
import json
from pathlib import Path
import re
import unicodedata

from .common import digest, norm, write_jsonl
from .prepare import chain

# Gold source, donor source, neutral sentence from the gold FIRST-HOP article.
# Chosen after source inspection, before any v3.1 generation. No fallback pool.
SELECTION = [
    ('df66ea220bdc11eba7f7acde48001122', '78249bea0bda11eba7f7acde48001122', 1),
    ('97d5e6f00bdb11eba7f7acde48001122', '35aaea880bdc11eba7f7acde48001122', 3),
    ('c22a48e40bd911eba7f7acde48001122', '0bd60cfa0bdd11eba7f7acde48001122', 1),
    ('c40d35580bda11eba7f7acde48001122', '751ba0980bd911eba7f7acde48001122', 1),
    ('4772896e0bdd11eba7f7acde48001122', 'ba289b440bdb11eba7f7acde48001122', 2),
    ('52376a780bdc11eba7f7acde48001122', 'b26e04e80bdb11eba7f7acde48001122', 1),
    ('f0faeb9a0bdb11eba7f7acde48001122', '5b1e1f240bdc11eba7f7acde48001122', 1),
    ('73def83e0bdd11eba7f7acde48001122', '8dfa2e9e0bda11eba7f7acde48001122', 1),
    ('e043b86e0bda11eba7f7acde48001122', 'e1cfab340bda11eba7f7acde48001122', 1),
    ('c5e7570c0bdd11eba7f7acde48001122', 'b0a2e8ba0bd911eba7f7acde48001122', 1),
]


def aliases(name):
    unaccented = ''.join(c for c in unicodedata.normalize('NFKD', name) if not unicodedata.combining(c))
    values = {name, unaccented}
    # Qualification variants reviewed against the saved source sentences. No
    # country-only answers are treated as aliases of a city.
    qualifications = {
        "Xi'an": ["Xi'an, Shaanxi", "Xi'an, China"],
        'Stuttgart': ['Stuttgart, Germany'], 'Düsseldorf': ['Düsseldorf, Germany', 'Dusseldorf, Germany'],
        'Denver': ['Denver, Colorado'], 'Rosario': ['Rosario, Santa Fe', 'Rosario, Santa Fe Province'],
        'Porterville': ['Porterville, California'], 'Shaftsbury, Vermont': ['Shaftsbury'],
        'H. S. Rawail': ['H.S. Rawail', 'H S Rawail'],
    }
    values.update(qualifications.get(name, []))
    return sorted(values)


def source_case(row, objects):
    path = chain(row)
    if row.get('type') != 'compositional' or not path:
        raise ValueError('Not an explicit compositional chain')
    a, b = path
    if a[1] != 'director' or b[1] not in {'father', 'place of birth', 'place of death'}:
        raise ValueError('Unreviewed relation')
    if any(len(objects[norm(s), r]) != 1 for s, r, _ in path):
        raise ValueError('Multiple annotated objects')
    context = dict(row['context'])
    support = [dict(title=t, sentence_id=i, text=context[t][i]) for t, i in row['supporting_facts']]
    first = [s for s in support if re.search(r'directed by\s+' + re.escape(a[2]) + r'(?=[.,;]|$)', s['text'], re.I)]
    second = [s for s in support if norm(s['title']) == norm(b[0]) and norm(b[2]) in norm(s['text'])]
    if not first or not second:
        raise ValueError('Missing unambiguous first/downstream evidence')
    return dict(path=path, first=first[0], second=second[0], context=context)


def prepare(source='data/dev.json', output='data/candidates_v3_1.jsonl'):
    target = Path(output)
    if target.exists() or target.with_suffix('.manifest.json').exists():
        raise FileExistsError('Refusing to overwrite fixed candidates')
    rows = json.loads(Path(source).read_text(encoding='utf-8'))
    by_id = {r['_id']: r for r in rows}
    objects = defaultdict(set)
    for row in rows:
        for s, r, o in row.get('evidences', []):
            objects[norm(s), r].add(norm(o))
    selected = []
    for index, (source_id, donor_id, sentence_id) in enumerate(SELECTION, 1):
        gold, donor = source_case(by_id[source_id], objects), source_case(by_id[donor_id], objects)
        a, b = gold['path']; da, db = donor['path']
        if a[1] != da[1] or b[1] != db[1] or norm(b[2]) == norm(db[2]) or norm(a[2]) == norm(da[2]):
            raise ValueError('Invalid matched donor')
        title = gold['first']['title']
        neutral = dict(title=title, sentence_id=sentence_id, text=gold['context'][title][sentence_id])
        row = dict(case_id=f'real-{index:02}', source_id=source_id, donor_id=donor_id, track='real',
                   original_question=by_id[source_id]['question'], A=a[0], r1=a[1], B=a[2], relation=b[1], C=b[2],
                   B_prime=da[2], C_prime=db[2], aliases_C=aliases(b[2]), aliases_C_prime=aliases(db[2]),
                   gold_evidence_chain=gold['path'], donor_evidence_chain=donor['path'],
                   first_hop_evidence=gold['first'], downstream_evidence=gold['second'],
                   donor_first_hop_evidence=donor['first'], donor_downstream_evidence=donor['second'],
                   neutral_evidence=neutral, evidence_order=1 if index % 2 else 2,
                   validation=dict(single_annotated_r1=True, single_annotated_r2=True,
                     first_hop_single_director_explicit=True, downstream_facts_reviewed=True,
                     granularity='named person' if b[1]=='father' else 'explicit named city/town; no country-only aliases',
                     neutral_article_matches_first_hop_article=True))
        # Inspect surname/first-name mentions as well as full names. A full-name
        # substring check alone missed director leaks in discovery candidates.
        forbidden = set(row['aliases_C'] + row['aliases_C_prime'] + [row['B'], row['B_prime']])
        for key in ('B', 'B_prime') + (('C', 'C_prime') if b[1] == 'father' else ()):
            forbidden.update(part for part in re.split(r'[\s-]+', row[key]) if len(part) >= 3)
        if any(re.search(r'(?<!\w)' + re.escape(term) + r'(?!\w)', neutral['text'], re.I) for term in forbidden):
            raise ValueError(f'H2 entity/answer leak: {row["case_id"]}')
        if re.search(r'\b(director|directed|father|born|died)\b', neutral['text'], re.I):
            raise ValueError('Neutral sentence carries relation evidence')
        row['neutral_forbidden_terms'] = sorted(forbidden)
        selected.append(row)
    if len(selected) != 10 or len({r[k] for r in selected for k in ('B','B_prime')}) != 20:
        raise ValueError('Need ten clean cases with twenty distinct intermediate identities')
    write_jsonl(target, selected)
    manifest = dict(version='3.1', count=10, candidates_sha256=digest(target), source_sha256=digest(source),
                    source='2WikiMultiHopQA dev.json, April 2021 release',
                    selection='Pre-inference manual evidence review after structural scan; four birth, three death, three father. All first hops are single-director films. Twenty distinct intermediate people. Not a representative sample.',
                    evidence_order='fixed alternating 1/2 across cases, held constant across H0-H3; no extra order variants',
                    aliases='predeclared spelling/diacritic/qualification variants; never learned from model outputs',
                    source_code_sha256=digest(__file__), inference_used_in_selection=False)
    target.with_suffix('.manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(json.dumps(manifest, indent=2))


if __name__ == '__main__':
    prepare()
