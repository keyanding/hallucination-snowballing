"""Source-backed real candidates and explicitly task-local catalog manipulations."""
from collections import defaultdict
import json
from pathlib import Path
import random
import re

from .common import digest, norm, read_jsonl
from .prepare import chain
from .experiment_v3 import write_json

OUT = Path('results/calibration_v3_4_1')
MECHANISMS = ('M1', 'M2', 'M3', 'M4')
LEVELS = ('D0', 'D1', 'D2', 'D3')
EXCLUDED = {'Fragment of an Empire', 'The House in the Snow-Drifts', 'The Great Citizen',
            'The Parisian Cobbler', 'Arabian Love', 'Große Freiheit Nr. 7', 'The Last Bridge',
            'The Original Sin (film)', 'El Protegido', 'La caída'}
CONVENTION = ('The following catalog is a task-local index of sourced film credits. '
              'Follow credited-director links until a record names a person. '
              'Comparison-title, comparison-director and reference-director links are catalog cross-references, not directing credits.')


def evidence(case, mechanism, level):
    nodes = case['nodes']
    gold_node = nodes[case['B']]
    wrong_node = nodes[case['near_wrong']]
    link = f'Film "{case["A"]}" has credited-director link {gold_node}.'
    leaves = [f'Record {nodes[name]} names {name}.' for name in case['leaf_order']]
    gold_leaf = f'Record {gold_node} names {case["B"]}.'
    wrong_leaf = f'Record {wrong_node} names {case["near_wrong"]}.'
    other_leaves = [x for x in leaves if x not in (gold_leaf, wrong_leaf)]
    neutral = ['Catalog entries are written as separate statements.', 'The index groups records into sections.']
    near = f'Film "{case["A"]}" has reference-director link {wrong_node}.'
    if mechanism == 'M1':
        if level == 'D0':
            return leaves + [link]
        if level == 'D1':
            movie = case['near_wrong_film']['title']
            return leaves + [link, f'Film "{case["A"]}" has comparison-title link "{movie}".',
                             f'Film "{movie}" has credited-director link {wrong_node}.']
        if level == 'D2':
            return leaves + [near, link]
        return [link, gold_leaf] + other_leaves + [near, wrong_leaf]
    if mechanism == 'M2':
        profile = case['shared_attributes']
        if profile is None:
            raise ValueError('No audited shared attributes for M2')
        b, w = case['B'], case['near_wrong']
        era, genre = profile['era'], profile['genre']
        base = leaves + [link]
        if level == 'D0':
            return base
        one = f'{b} and {w} each has a documented film-directing credit dated within {era}.'
        if level == 'D1':
            return base + [one]
        two = f'{b} and {w} each has a documented {genre}-film directing credit within {era}.'
        if level == 'D2':
            return base + [one, two]
        return base + [one, two, f'{w} has {genre}-film directing experience.',
                       f'The profile for {w} includes directing work within {era}.',
                       f'The comparison profile names {w}.']
    if mechanism == 'M3':
        if level == 'D0':
            return [x for x in leaves if x != gold_leaf] + [link, gold_leaf]
        if level == 'D1':
            return [link, gold_leaf] + [x for x in leaves if x != gold_leaf] + neutral
        if level == 'D2':
            return [link, gold_leaf] + [x for x in leaves if x != gold_leaf] + neutral + [near]
        return [link, gold_leaf] + other_leaves + neutral + [near, wrong_leaf]
    if mechanism == 'M4':
        x, y = case['intermediate_nodes']
        if level == 'D0':
            return leaves + [link]
        if level == 'D1':
            return leaves + [f'Film "{case["A"]}" has credited-director link {x}.',
                             f'Record {x} has credited-director link {gold_node}.']
        path = [f'Film "{case["A"]}" has credited-director link {x}.',
                f'Record {x} has credited-director link {y}.',
                f'Record {y} has credited-director link {gold_node}.']
        if level == 'D3':
            path += [f'Record {x} has comparison-director link {wrong_node}.']
        return leaves + path
    raise ValueError(mechanism)


def prompt(case, mechanism, level):
    names = '\n'.join(f'{i}. {p["name"]}' for i, p in enumerate(case['candidates'], 1))
    return (f'Question:\nWho directed "{case["A"]}"?\n\nCandidate directors:\n' + names
            + '\n\nCatalog convention:\n' + CONVENTION + '\n\nEvidence:\n'
            + '\n'.join('- ' + line for line in evidence(case, mechanism, level))
            + f'\n\nBased on the evidence above, who directed "{case["A"]}"?'
            + '\n\nAnswer with only one candidate name.')


def resolve_rendered(case, mechanism, level):
    lines = evidence(case, mechanism, level)
    paths, names = {}, {}
    for line in lines:
        m = re.fullmatch(r'(Film "[^"]+"|Record \w+) has credited-director link (\w+)\.', line)
        if m:
            if m[1] in paths:
                raise ValueError('Multiple credited paths')
            paths[m[1]] = 'Record ' + m[2]
        m = re.fullmatch(r'Record (\w+) names (.+)\.', line)
        if m:
            names['Record ' + m[1]] = m[2]
    node, visited = f'Film "{case["A"]}"', set()
    while node in paths:
        if node in visited:
            raise ValueError('Credit path cycle')
        visited.add(node)
        node = paths[node]
    if names.get(node) != case['B']:
        raise ValueError('Rendered evidence does not uniquely resolve to gold')
    return names[node], len(visited)


def build():
    if OUT.exists():
        raise FileExistsError('Refusing to overwrite calibration preparation')
    source = Path('data/dev.json')
    expected = json.loads(Path('data/candidates_v3_3.manifest.json').read_text(encoding='utf-8'))
    assert digest(source) == expected['source_sha256']
    rows = json.loads(source.read_text(encoding='utf-8'))
    people = {}
    for c in read_jsonl('data/candidates_v3_3.jsonl'):
        for prime in (False, True):
            name = c['B_prime' if prime else 'B']
            people[norm(name)] = dict(name=name, relation=c['relation'], target=c['C_prime' if prime else 'C'],
                target_aliases=c['aliases_C_prime' if prime else 'aliases_C'],
                downstream_evidence=c['donor_downstream_evidence' if prime else 'downstream_evidence'],
                downstream_source_id=c['donor_id' if prime else 'source_id'])
    objects = defaultdict(set)
    for r in rows:
        for s, relation, o in r.get('evidences', []):
            objects[norm(s), relation].add(norm(o))
    films = defaultdict(dict)
    for row in sorted(rows, key=lambda r: r['_id']):
        path = chain(row)
        if not path or path[0][1] != 'director' or norm(path[0][2]) not in people:
            continue
        a = path[0]
        if len(objects[norm(a[0]), 'director']) != 1:
            continue
        context = dict(row['context'])
        for title, i in row['supporting_facts']:
            if title not in context or not 0 <= i < len(context[title]):
                continue
            text = context[title][i]
            if not re.search(r'directed by\s+' + re.escape(a[2]) + r'(?=[.,;]|$)', text, re.I):
                continue
            years = re.findall(r'\b(?:19|20)\d{2}\b', ' '.join(context[title][:3]))
            if not years and title == 'Alice: A True Story':
                assert '(2014)' in context['Anil Das'][8]
                years = ['2014']
            if not years:
                continue
            attributes = []
            for j, sentence in enumerate(context[title][:3]):
                for genre in re.findall(r'\b(drama|comedy|action|thriller|mystery|war|crime|silent|psychological|musical)\b(?=[^.!?]{0,45}\bfilm\b)', sentence, re.I):
                    attributes.append(dict(genre=genre.lower(), source_id=row['_id'], title=title, sentence_id=j, text=sentence))
            films[norm(a[2])][norm(a[0])] = dict(title=title, source_id=row['_id'], director=people[norm(a[2])]['name'],
                year=int(years[0]), evidence=dict(title=title, sentence_id=i, text=text), genre_evidence=attributes)
    def shared(gold):
        options = []
        for key, person in people.items():
            if person['name'] == gold['name'] or person['relation'] != gold['relation'] or norm(person['target']) == norm(gold['target']):
                continue
            for g in films[norm(gold['name'])].values():
                for w in films[key].values():
                    if g['year'] // 50 != w['year'] // 50:
                        continue
                    for ga in g['genre_evidence']:
                        for wa in w['genre_evidence']:
                            if ga['genre'] == wa['genre']:
                                options.append((abs(g['year'] - w['year']), person['name'], g['title'], w['title'], ga['genre'], g, w, ga, wa))
        if not options:
            return None
        best = min(options, key=lambda x: x[:5])
        gap, name, _, _, genre, g, w, ga, wa = best
        start = g['year'] // 50 * 50
        return dict(wrong=name, genre=genre, era=f'{start}–{start + 49}', year_gap=gap,
                    gold_film=g, wrong_film=w, gold_genre_evidence=ga, wrong_genre_evidence=wa)
    feature_map = {key: shared(person) for key, person in people.items()}
    pool = [(people[key], f) for key in sorted(films) for f in films[key].values() if f['title'] not in EXCLUDED]
    if len(pool) != 36:
        raise ValueError(f'Expected 36 distinct source films, got {len(pool)}')
    rng = random.Random(42)
    eligible = [x for x in pool if feature_map[norm(x[0]['name'])] is not None]
    if len(eligible) < 18:
        raise ValueError('Not enough source-backed shared-attribute cases')
    held = rng.sample(eligible, 12)
    held_titles = {f['title'] for _, f in held}
    remaining = [x for x in pool if x[1]['title'] not in held_titles]
    m2 = rng.sample([x for x in remaining if feature_map[norm(x[0]['name'])] is not None], 6)
    m2_titles = {f['title'] for _, f in m2}
    rest = [x for x in remaining if x[1]['title'] not in m2_titles]
    rng.shuffle(rest)
    groups = dict(M1=rest[:6], M2=m2, M3=rest[6:12], M4=rest[12:18])
    def construct(items, split, mechanism=None):
        positions = ([0, 1, 2, 3, 0, 1] if len(items) == 6 else list(range(4)) * 3)
        rng.shuffle(positions)
        result = []
        for index, ((gold, film), position) in enumerate(zip(items, positions), 1):
            attr = feature_map[norm(gold['name'])]
            near = people[norm(attr['wrong'])] if attr else None
            chosen = [gold] + ([near] if near else [])
            options = []
            for key, person in people.items():
                if person['relation'] != gold['relation'] or not films[key]:
                    continue
                distance = min(abs(f['year'] - film['year']) for f in films[key].values())
                options.append((distance, person['name'], person))
            for _, _, person in sorted(options):
                if any(norm(person['target']) == norm(p['target']) for p in chosen):
                    continue
                chosen.append(person)
                if len(chosen) == 4:
                    break
            assert len(chosen) == 4
            near = near or chosen[1]
            others = chosen[1:]
            rng.shuffle(others)
            candidates = others[:position] + [gold] + others[position:]
            names = [p['name'] for p in candidates]
            ids = rng.sample(range(100, 999), 6)
            leaf_order = names[:]
            rng.shuffle(leaf_order)
            wrong_films = [f for f in films[norm(near['name'])].values() if f['title'] != film['title']]
            near_film = min(wrong_films, key=lambda f: (abs(f['year'] - film['year']), f['title']))
            result.append(dict(case_id=f'{split}-{mechanism or "shared"}-{index:02}', split=split,
                mechanism=mechanism, A=film['title'], B=gold['name'], relation=gold['relation'],
                candidates=candidates, gold_position=position + 1, source_A=film,
                near_wrong=near['name'], near_wrong_film=near_film, shared_attributes=attr,
                nodes=dict(zip(names, ['R' + str(x) for x in ids[:4]])),
                intermediate_nodes=['Q' + str(x) for x in ids[4:]], leaf_order=leaf_order))
        return result
    dev = [case for mech in MECHANISMS for case in construct(groups[mech], 'dev', mech)]
    heldout = construct(held, 'heldout')
    assert len({c['A'] for c in dev + heldout}) == 36
    OUT.mkdir(parents=True)
    write_json(OUT / 'dev_cases.json', dev)
    write_json(OUT / 'heldout_cases.json', heldout)
    write_json(OUT / 'dataset_manifest.json', dict(seed=42, source_sha256=digest(source),
        dev_cases=24, heldout_cases=12, disjoint_target_films=True, entity_overlap_allowed=True,
        heldout_selection='Twelve shared confirmation cases sampled before inference; each selected mechanism uses all twelve at its selected difficulty once.',
        source_selection='Known reviewed downstream candidates; 36 distinct film questions after explicit exclusions; M2-capable heldout and six development cases require supported era+genre pair.',
        exclusions=sorted(EXCLUDED), catalog_status='Researcher-constructed index and comparison links, not historical film claims; credited endpoints and attributes are source-backed.',
        M2_resolution='User-approved fixed candidate set; manipulate salience of shared era and genre with one designated nearby alternative; not a candidate-replacement study.',
        feature_limit='Era is a fixed 50-year band; genre and era proximity are imperfect biographical similarity controls. Other two candidates remain domain-plausible, not necessarily matched on both attributes.',
        future_v35_must_exclude_all_36_base_films=True))


if __name__ == '__main__':
    build()
