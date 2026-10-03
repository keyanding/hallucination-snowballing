"""Controlled symbolic graphs with real, frozen candidate identities."""
from collections import Counter, defaultdict
import copy
import json
from pathlib import Path
import random
import re

from .common import digest, norm
from .experiment_v3 import write_json
from .experiment_v3_3 import sha

OUT = Path('results/calibration_v3_4_2')
GRID = [(d, b) for d in range(1, 5) for b in range(3)]
RELATIONS = ('credited-director', 'comparison-director', 'associated-director')
CONVENTION = (
    'This is a synthetic catalog task. Film identifiers and graph links are constructed for this task; '
    'the candidate names refer to real people. Use only the records below. '
    'The relation vocabulary is credited-director, comparison-director, associated-director. '
    'Starting at the named Film, follow only credited-director links until reaching a record that names a candidate. '
    'Comparison-director and associated-director links describe separate catalog relations. '
    'The credited director means the candidate reached by that traversal.'
)


def load(name):
    return json.loads((OUT / name).read_text(encoding='utf-8'))


def key(depth, branches):
    return f'D{depth}B{branches}'


def easier(depth, branches):
    return ([(depth - 1, branches)] if depth > 1 else []) + ([(depth, branches - 1)] if branches else [])


def edges(case, depth, branches):
    result = []
    for path_index in case['path_order']:
        if path_index > branches:
            continue
        path = case['paths'][path_index]
        nodes = [f'Film {case["target"]}'] + ['Record ' + n for n in path['nodes'][:depth - 1]]
        nodes += ['Record ' + case['name_nodes'][path['endpoint']]]
        result.extend((a, RELATIONS[path_index], z) for a, z in zip(nodes, nodes[1:]))
    return result


def name_records(case):
    return [f'Record {case["name_nodes"][name]} names {name}.' for name in case['name_record_order']]


def graph_records(case, depth, branches):
    return [f'{a} has {relation} link {z.removeprefix("Record ")}.' for a, relation, z in edges(case, depth, branches)]


def render(case, depth, branches):
    candidates = '\n'.join(f'{i}. {p["name"]}' for i, p in enumerate(case['candidates'], 1))
    return (CONVENTION + '\n\nCandidate names:\n' + candidates + '\n\nCandidate-name records:\n'
            + '\n'.join(name_records(case)) + '\n\nGraph-link records:\n'
            + '\n'.join(graph_records(case, depth, branches))
            + f'\n\nWhich candidate is the credited director of Film {case["target"]}?'
            + '\n\nAnswer with only one candidate name.')


def audit_prompt(case, depth, branches, text=None):
    """Parse the actual prompt, independently traverse every relation path."""
    text = render(case, depth, branches) if text is None else text
    mappings = {}
    links = defaultdict(list)
    for line in text.splitlines():
        match = re.fullmatch(r'Record (\w+) names (.+)\.', line)
        if match:
            assert match[1] not in mappings
            mappings[match[1]] = match[2]
        match = re.fullmatch(r'(Film \w+|Record \w+) has ([a-z-]+) link (\w+)\.', line)
        if match:
            assert match[2] in RELATIONS
            links[match[1], match[2]].append(match[3])
    names = [p['name'] for p in case['candidates']]
    assert set(mappings.values()) == set(names) and len(mappings) == 4
    endpoints = []
    for index, relation in enumerate(RELATIONS[:branches + 1]):
        node, visited, count = f'Film {case["target"]}', set(), 0
        while (node, relation) in links:
            assert node not in visited, 'Cycle'
            visited.add(node)
            choices = links[node, relation]
            assert len(choices) == 1, 'Multiple queried-relation paths'
            node = 'Record ' + choices[0]
            count += 1
        endpoint = mappings.get(node.removeprefix('Record '))
        assert endpoint == case['paths'][index]['endpoint'], 'Unexpected endpoint'
        assert count == depth, 'Unequal branch depth'
        endpoints.append(endpoint)
    assert len(links) == depth * (branches + 1), 'Unexpected link records'
    assert endpoints[0] == case['gold'] and len(set(endpoints)) == branches + 1
    assert not re.search(r'\b(correct|wrong|gold|distractor)\b', text, re.I)
    return dict(unique_queried_endpoint=endpoints[0], path_depth=depth,
                branch_endpoints=endpoints, link_count=len(links), mapping_count=len(mappings))


def make_cases():
    previous = Path('results/calibration_v3_4_1')
    pool = json.loads((previous / 'dev_cases.json').read_text(encoding='utf-8'))
    pool += json.loads((previous / 'heldout_cases.json').read_text(encoding='utf-8'))
    rng = random.Random(342)
    chosen = rng.sample(sorted(pool, key=lambda c: c['case_id']), 20)
    targets = rng.sample(range(10000, 99999), 20)
    all_cases = []
    for split, subset, offset in [('dev', chosen[:8], 0), ('heldout', chosen[8:], 8)]:
        positions = list(range(4)) * (len(subset) // 4)
        rng.shuffle(positions)
        for i, (old, position) in enumerate(zip(subset, positions)):
            others = [copy.deepcopy(p) for p in old['candidates'] if p['name'] != old['B']]
            rng.shuffle(others)
            gold = copy.deepcopy(next(p for p in old['candidates'] if p['name'] == old['B']))
            candidates = others[:position] + [gold] + others[position:]
            names = [p['name'] for p in candidates]
            ids = ['R' + str(n) for n in rng.sample(range(10000, 99999), 13)]
            record_order = rng.sample(names, 4)
            path_order = rng.sample([0, 1, 2], 3)
            endpoints = [gold['name']] + rng.sample([p['name'] for p in others], 2)
            case = dict(case_id=f'{split}-{i+1:02}', split=split, target='T' + str(targets[offset+i]),
                        gold=gold['name'], gold_position=position+1, candidates=candidates,
                        name_nodes=dict(zip(names, ids[:4])), name_record_order=record_order,
                        paths=[dict(endpoint=name, nodes=ids[4+j*3:7+j*3]) for j, name in enumerate(endpoints)],
                        path_order=path_order, candidate_source_case=old['case_id'],
                        candidate_list_sha256=sha(json.dumps(candidates, sort_keys=True, ensure_ascii=False)))
            all_cases.append(case)
    return all_cases[:8], all_cases[8:]


def validate_sources(cases):
    source_path = Path('data/dev.json')
    source_manifest = json.loads(Path('results/calibration_v3_4_1/dataset_manifest.json').read_text(encoding='utf-8'))
    assert digest(source_path) == source_manifest['source_sha256']
    source = {r['_id']: r for r in json.loads(source_path.read_text(encoding='utf-8'))}
    count = 0
    for c in cases:
        assert len(c['candidates']) == 4
        assert len({norm(p['name']) for p in c['candidates']}) == 4
        alias_sets = [{norm(p['target']), *(norm(a) for a in p['target_aliases'])} for p in c['candidates']]
        for i, aliases in enumerate(alias_sets):
            assert all(not aliases.intersection(other) for other in alias_sets[i+1:])
        assert c['candidates'][c['gold_position']-1]['name'] == c['gold']
        for p in c['candidates']:
            row = source[p['downstream_source_id']]
            ev = p['downstream_evidence']
            assert dict(row['context'])[ev['title']][ev['sentence_id']] == ev['text']
            assert [p['name'], p['relation'], p['target']] in row['evidences']
            count += 1
    return count
