"""Freeze a provenance-backed four-director universe before any v3.4 output."""
from collections import defaultdict
import json
from pathlib import Path
import random
import re

from .common import digest, norm, read_jsonl, write_jsonl
from .prepare import chain
from .experiment_v3 import TEMPLATES, write_json


DATA = Path('data/candidates_v3_4.jsonl')
GOLD_DIRECTORS = ('Gu Changwei', 'Yuen Woo-ping', 'Rahul Rawail', 'Ildikó Enyedi',
                  'James Goldstone', 'León Klimovsky', 'Bhappi Sonie', 'Walter Hugo Khouri')


def prepare():
    if DATA.exists() or DATA.with_suffix('.manifest.json').exists():
        raise FileExistsError('Refusing to overwrite frozen candidate universe')
    source = Path('data/dev.json')
    old_manifest = json.loads(Path('data/candidates_v3_3.manifest.json').read_text(encoding='utf-8'))
    if digest(source) != old_manifest['source_sha256']:
        raise ValueError('Frozen source changed')
    rows = json.loads(source.read_text(encoding='utf-8'))
    people = {}
    for case in read_jsonl('data/candidates_v3_3.jsonl'):
        for prime in (False, True):
            name = case['B_prime' if prime else 'B']
            people[norm(name)] = dict(name=name, target=case['C_prime' if prime else 'C'],
                relation=case['relation'], target_aliases=case['aliases_C_prime' if prime else 'aliases_C'],
                downstream_evidence=case['donor_downstream_evidence' if prime else 'downstream_evidence'],
                downstream_source_id=case['donor_id' if prime else 'source_id'])
    objects = defaultdict(set)
    for row in rows:
        for s, r, o in row.get('evidences', []):
            objects[norm(s), r].add(norm(o))
    films = defaultdict(dict)
    for row in sorted(rows, key=lambda r: r['_id']):
        path = chain(row)
        if not path or path[0][1] != 'director' or norm(path[0][2]) not in people:
            continue
        a, b = path
        person = people[norm(a[2])]
        if b[1] != person['relation'] or norm(b[2]) != norm(person['target']):
            continue
        if len(objects[norm(a[0]), 'director']) != 1:
            continue
        context = dict(row['context'])
        for title, i in row['supporting_facts']:
            if title not in context or not 0 <= i < len(context[title]):
                continue
            text = context[title][i]
            if not re.search(r'directed by\s+' + re.escape(a[2]) + r'(?=[.,;]|$)', text, re.I):
                continue
            years = re.findall(r'\b(?:19|20)\d{2}\b', ' '.join(context[title]))
            year_note = None
            if not years and title == 'Alice: A True Story':
                # Explicitly reviewed film/year statement in the director article.
                year_text = context['Anil Das'][8]
                assert 'Alice - A True Story' in year_text and '(2014)' in year_text
                years = ['2014']
                year_note = dict(title='Anil Das', sentence_id=8, text=year_text)
            if not years:
                continue
            films[norm(a[2])][norm(a[0])] = dict(A=a[0], title=title, source_id=row['_id'],
                year=int(years[0]), year_note=year_note, director=person['name'], original_question=row['question'],
                evidence=dict(title=title, sentence_id=i, text=text))
    pool = [(people[norm(name)], film) for name in GOLD_DIRECTORS
            for film in sorted(films[norm(name)].values(), key=lambda f: f['title'])]
    if len(pool) != 20:
        raise ValueError(f'Expected exactly twenty preselected films; found {len(pool)}')
    rng = random.Random(42)
    rng.shuffle(pool)
    gold_positions = list(range(4)) * 5
    rng.shuffle(gold_positions)
    cases = []
    for i, ((gold, film), position) in enumerate(zip(pool, gold_positions), 1):
        same_director = [f for f in films[norm(gold['name'])].values() if f['A'] != film['A']]
        if not same_director:
            raise ValueError('No distinct source-backed bridge film')
        bridge = rng.choice(sorted(same_director, key=lambda f: f['title']))
        candidates = [dict(gold, bridge_film=bridge)]
        options = []
        for key, person in people.items():
            if person['relation'] != gold['relation'] or person['name'] == gold['name']:
                continue
            available = [f for f in films[key].values() if f['A'] != film['A']]
            if available:
                other = min(available, key=lambda f: (abs(f['year'] - film['year']), f['title']))
                options.append((abs(other['year'] - film['year']), person['name'], person, other))
        for distance, _, person, other in sorted(options):
            if any(norm(person['target']) == norm(c['target']) for c in candidates):
                continue
            if distance > 30:
                continue
            candidates.append(dict(person, bridge_film=other, era_gap_years=distance))
            if len(candidates) == 4:
                break
        if len(candidates) != 4:
            raise ValueError('Cannot obtain three distinct-target, era-near director alternatives: ' + film['title'] + ' / ' + repr([(x[1], x[0]) for x in options]))
        wrong = rng.choice(candidates[1:])['name']
        alternatives = candidates[1:]
        rng.shuffle(alternatives)
        ordered = alternatives[:position] + candidates[:1] + alternatives[position:]
        direct_facts = [f'"{c["bridge_film"]["title"]}" was directed by {c["name"]}.' for c in ordered]
        link = f'The films "{film["title"]}" and "{bridge["title"]}" have the same director.'
        first_facts = [link] + direct_facts
        rng.shuffle(first_facts)
        case = dict(case_id=f'universe-{i:02}', A=film['title'], r1='director', relation=gold['relation'],
                    B=gold['name'], C=gold['target'], original_question=film['original_question'],
                    candidates=ordered, registered_wrong=wrong, first_hop_evidence=first_facts,
                    source_A=film, source_bridge=bridge,
                    construction='Derived shared-director equality from two explicit frozen source claims; four bridge-film/director facts prevent a unique-name shortcut.',
                    plausibility='All are real directors from prior reviewed 2Wiki cases; every alternative has a documented film within 30 years of A; no target collisions.',
                    seed=42)
        assert len({norm(c['target']) for c in ordered}) == 4
        assert all(f'"{film["title"]}" was directed by ' not in text for text in first_facts)
        assert all(c['bridge_film']['title'] != film['title'] for c in ordered)
        cases.append(case)
    write_jsonl(DATA, cases)
    write_json(DATA.with_suffix('.manifest.json'), dict(
        version='3.4', seed=42, cases=20, source_sha256=digest(source), candidates_sha256=digest(DATA),
        source_code_sha256=digest(__file__), source='Frozen 2WikiMultiHopQA dev.json',
        unique_gold_directors=len(set(c['B'] for c in cases)),
        relation_counts={r: sum(c['relation'] == r for c in cases) for r in TEMPLATES},
        selection='Twenty source films of eight preselected directors with multiple supported films; downstream facts reuse reviewed v3.3 candidate/donor pool. Selection and ordering frozen before v3.4 inference.',
        gold_position_counts={str(p + 1): gold_positions.count(p) for p in range(4)},
        no_v34_outputs_used=True, repeated_directors_not_independent=True))


if __name__ == '__main__':
    prepare()
