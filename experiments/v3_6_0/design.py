"""Opaque disjoint cases and exact state-only prompt interventions."""
import itertools
import random
import re
import unicodedata
from experiments.v3_5_1.render_prompts import sha

CORE = ('C0', 'W0', 'LOOKUP_GOLD', 'LOOKUP_WRONG', 'SWAP', 'REVERSE', 'UNMAPPED')
PREFIX = 'This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.'
UNKNOWN_RULE = 'If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.'
SEED = 360


def make_cases():
    rng = random.Random(SEED)
    codes = [letter + f'{number:02}' for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for number in range(100)]
    rng.shuffle(codes)
    used = set()

    def take():
        value = codes.pop()
        assert value not in used
        used.add(value)
        return value

    cases = []
    for split, count in [('calibration', 20), ('main', 40)]:
        patterns = list(itertools.product((0, 1), repeat=3)) * (2 if count == 20 else 5)
        if count == 20:
            patterns += [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
        rng.shuffle(patterns)
        for i, (state_bit, outcome_bit, order_bit) in enumerate(patterns, 1):
            entity = 'Entity_' + take()
            alternative = 'Entity_' + take()
            states = sorted(['State_' + take(), 'State_' + take()])
            # Match lengths but exclude same letter or shared numeric suffix digits.
            first = take()
            suitable = next(v for v in reversed(codes) if v[0] != first[0] and not set(v[1:]) & set(first[1:]))
            codes.remove(suitable)
            assert suitable not in used
            used.add(suitable)
            outcomes = sorted(['Outcome_' + first, 'Outcome_' + suitable])
            case = dict(case_id=f'v360-{split}-{i:03}', split=split, entity=entity,
                        alternate_entity=alternative, unmapped_state='State_' + take(),
                        gold_state=states[state_bit], wrong_state=states[1-state_bit],
                        gold_outcome=outcomes[outcome_bit], wrong_outcome=outcomes[1-outcome_bit],
                        record_order=['gold', 'wrong'] if order_bit == 0 else ['wrong', 'gold'],
                        template='gold-record-first' if order_bit == 0 else 'wrong-record-first',
                        gold_state_lexical_rank=state_bit+1, gold_outcome_lexical_rank=outcome_bit+1,
                        seed=SEED)
            cases.append(case)
    validate_cases(cases)
    return cases[:20], cases[20:]


def validate_cases(cases):
    identifiers = []
    pairs = []
    for c in cases:
        keys = ('entity', 'alternate_entity', 'unmapped_state', 'gold_state', 'wrong_state', 'gold_outcome', 'wrong_outcome')
        values = [c[k] for k in keys]
        assert len(set(values)) == 7
        for k, v in zip(keys, values):
            prefix = 'Entity' if 'entity' in k else 'Outcome' if 'outcome' in k else 'State'
            assert re.fullmatch(prefix + r'_[A-Z][0-9]{2}', v)
        a, b = c['gold_outcome'].split('_')[1], c['wrong_outcome'].split('_')[1]
        assert a[0] != b[0] and not set(a[1:]) & set(b[1:])
        identifiers.extend(values)
        pairs += [(c['gold_state'], c['gold_outcome']), (c['wrong_state'], c['wrong_outcome'])]
    assert len(set(identifiers)) == len(identifiers)
    assert len(set(pairs)) == len(pairs)
    for split, n in [('calibration', 20), ('main', 40)]:
        sub = [c for c in cases if c['split'] == split]
        assert len(sub) == n
        for field in ('gold_state_lexical_rank', 'gold_outcome_lexical_rank'):
            assert sum(c[field] == 1 for c in sub) == n//2
        assert sum(c['record_order'][0] == 'gold' for c in sub) == n//2
    return dict(cases=60, unique_identifiers=len(identifiers), unique_state_outcome_pairs=len(pairs),
                disjoint_splits=True, no_shared_outcome_suffix_characters=True, balanced_roles=True)


def render(c, condition, unknown_rule):
    assert condition in CORE + ('ENTITY_LABEL',)
    state = c['wrong_state'] if condition in ('W0', 'LOOKUP_WRONG') else c['unmapped_state'] if condition == 'UNMAPPED' else c['gold_state']
    entity = c['alternate_entity'] if condition == 'ENTITY_LABEL' else c['entity']
    mappings = [(c[role + '_state'], c[('wrong' if role == 'gold' else 'gold') + '_outcome'] if condition == 'SWAP' else c[role + '_outcome']) for role in c['record_order']]
    if condition == 'REVERSE':
        mappings.reverse()
    records = '\n'.join(f'{a} maps to {b}.' for a, b in mappings)
    if condition.startswith('LOOKUP'):
        body = f'Question:\nAccording to the supplied mapping, what does {state} map to?'
    else:
        body = (f'Current entity:\n{entity}\n\nWorking intermediate state:\n{state}\n\n'
                f'Question:\nUsing the working intermediate state and the downstream mappings above, what is the outcome for {entity}?')
    prompt = PREFIX + '\n\nDownstream mappings:\n' + records + '\n\n' + body + '\n\nOutput only the outcome identifier.'
    if unknown_rule:
        prompt += '\n' + UNKNOWN_RULE
    resolved = dict(mappings).get(state, 'UNKNOWN')
    return dict(case_id=c['case_id'], split=c['split'], condition=condition, supplied_state=state, entity=entity,
                expected=resolved, mappings=mappings, record_order_sha256=sha(records),
                prompt=prompt, text_sha256=sha(prompt), auxiliary=False)


def audit(c, unknown_rule):
    rows = {k: render(c, k, unknown_rule) for k in CORE + ('ENTITY_LABEL',)}
    a, b = rows['C0']['prompt'], rows['W0']['prompt']
    span = '\nWorking intermediate state:\n'
    before, tail = a.split(span)
    original, after = tail.split('\n', 1)
    assert original == c['gold_state']
    assert before + span + c['wrong_state'] + '\n' + after == b
    assert a.replace(c['entity'], c['alternate_entity']) == rows['ENTITY_LABEL']['prompt']
    assert rows['REVERSE']['mappings'] == list(reversed(rows['C0']['mappings']))
    for k in CORE + ('ENTITY_LABEL',):
        r = rows[k]
        # Parse actual rendered mapping lines independently of the expected field.
        mappings = re.findall(r'^(State_[A-Z][0-9]{2}) maps to (Outcome_[A-Z][0-9]{2})\.$', r['prompt'], re.M)
        assert len(mappings) == 2 and len(dict(mappings)) == 2
        assert dict(mappings).get(r['supplied_state'], 'UNKNOWN') == r['expected']
        assert not re.search(r'\b(gold|wrong|correct|donor|C0|W0)\b', r['prompt'])
        assert not re.search(r'^\d+[.)] ', r['prompt'], re.M)
    assert rows['SWAP']['expected'] == c['wrong_outcome']
    assert rows['UNMAPPED']['expected'] == 'UNKNOWN'
    assert rows['REVERSE']['expected'] == rows['ENTITY_LABEL']['expected'] == c['gold_outcome']
    return rows


def normalize(raw):
    return unicodedata.normalize('NFC', raw).strip().removesuffix('.')


def parse(raw, c, truncated=False):
    value = normalize(raw)
    if truncated:
        category, subtype = 'INVALID', 'TRUNCATED'
    elif value == c['gold_outcome']:
        category, subtype = 'C', None
    elif value == c['wrong_outcome']:
        category, subtype = 'Cp', None
    elif value == 'UNKNOWN':
        category, subtype = 'UNKNOWN', None
    elif re.fullmatch(r'Outcome_[A-Z][0-9]{2}', value):
        category, subtype = 'OTHER', None
    else:
        category, subtype = 'INVALID', 'NONCOMPLIANT'
    return dict(normalized=value, category=category, invalid_subtype=subtype,
                permitted=category in ('C', 'Cp', 'UNKNOWN'))


def shuffled(rows, seed):
    rng = random.Random(seed)
    for attempt in range(1, 10001):
        rng.shuffle(rows)
        if all(a['case_id'] != b['case_id'] for a, b in zip(rows, rows[1:])):
            return rows, attempt
    raise AssertionError('No nonadjacent schedule')
