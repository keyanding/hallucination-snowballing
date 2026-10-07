"""Nested distractors with fixed relative position bands and lexical-only sampling."""
import random
import re
import unicodedata
from collections import Counter
from experiments.v3_6_1.design import sha, token_info

KS = (0, 4, 12, 24)
BANDS = ('beginning', 'middle', 'end')
SEED = 362


def normalize(raw):
    return unicodedata.normalize('NFC', raw).strip().removesuffix('.')


def parse(raw, case, expected, truncated=False):
    value = normalize(raw)
    if truncated:
        category = 'INVALID'
    elif value == case['gold_outcome']:
        category = 'C'
    elif value == case['wrong_outcome']:
        category = 'Cp'
    elif value == 'UNKNOWN':
        category = 'UNKNOWN'
    elif re.fullmatch(r'OUTCOME_[A-Z][0-9]{2}', value):
        category = 'OTHER'
    else:
        category = 'INVALID'
    return dict(normalized=value, category=category, correct=not truncated and value == expected,
                distractor_output=value in {d['outcome'] for d in case['distractors']})


def block(case, k, diagnostic_band=None):
    assert k in KS
    pair = [(case[r+'_state'], case[r+'_outcome']) for r in case['record_order']]
    band = diagnostic_band or case['position_band']
    all_d = [(d['state'], d['outcome']) for d in case['distractors']]
    # Middle nesting selects symmetric prefixes of two frozen halves.
    if case['position_band'] == 'middle':
        selected = all_d[:k//2]+all_d[12:12+k//2]
    else:
        selected = all_d[:k]
    insertion = 0 if band == 'beginning' else k//2 if band == 'middle' else k
    return selected[:insertion]+pair+selected[insertion:]


def render(case, k, condition, diagnostic_band=None):
    assert condition in ('C0', 'W0')
    state = case['gold_state'] if condition == 'C0' else case['wrong_state']
    rows = block(case, k, diagnostic_band)
    records = '\n'.join(f'{a} -> {b}' for a,b in rows)
    prompt = f'Synthetic mapping task.\n\nMappings:\n{records}\n\nCurrent state:\n{state}\n\nReturn only the mapped outcome.'
    return dict(case_id=case['case_id'], k=k, condition=condition,
                stage='position_diagnostic' if diagnostic_band else 'main', position_band=diagnostic_band or case['position_band'],
                supplied_state=state, expected=dict(rows)[state], mappings=rows,
                gold_position=next(i for i,(a,b) in enumerate(rows, 1) if a == case['gold_state']),
                wrong_position=next(i for i,(a,b) in enumerate(rows, 1) if a == case['wrong_state']),
                prompt=prompt, text_sha256=sha(prompt))


def audit_pair(case, k, diagnostic_band=None):
    a, b = (render(case, k, c, diagnostic_band) for c in ('C0', 'W0'))
    before, tail = a['prompt'].split('\nCurrent state:\n')
    supplied, after = tail.split('\n', 1)
    assert supplied == case['gold_state']
    assert before+'\nCurrent state:\n'+case['wrong_state']+'\n'+after == b['prompt']
    assert a['mappings'] == b['mappings']
    assert 'UNKNOWN' not in a['prompt'] and 'entity' not in a['prompt'].lower()
    assert not re.search(r'^\d+[.)] ', a['prompt'], re.M)
    for row in (a,b):
        parsed = re.findall(r'^(STATE_[A-Z][0-9]{2}) -> (OUTCOME_[A-Z][0-9]{2})$', row['prompt'], re.M)
        assert parsed == row['mappings'] and len(parsed) == k+2
        assert len(dict(parsed)) == len(parsed)
        assert dict(parsed)[row['supplied_state']] == row['expected']
    return a,b


def make_cases(tokenizer, old_identifiers):
    old = {v.upper() for v in old_identifiers}
    pool = [p+'_'+letter+f'{n:02}' for p in ('STATE', 'OUTCOME') for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for n in range(100)]
    audit = [token_info(tokenizer, v) | dict(eligible=v not in old) for v in pool]
    rng = random.Random(SEED)
    eligible = {}
    for role in ('STATE', 'OUTCOME'):
        sub = [r for r in audit if r['eligible'] and r['raw'].startswith(role+'_')]
        minimum = min(r['token_count'] for r in sub)
        eligible[role] = [r['raw'] for r in sub if r['token_count'] == minimum]
        assert len(eligible[role]) >= 1040, 'Insufficient stable-token candidate pool'
        rng.shuffle(eligible[role])
    used = set()
    schedule = [('beginning', order) for order in (0,1) for _ in range(7)]
    schedule += [('middle', 0)]*7+[('middle', 1)]*6
    schedule += [('end', 0)]*6+[('end', 1)]*7
    rng.shuffle(schedule)
    cases = []
    for i, (band, order) in enumerate(schedule, 1):
        suffixes = set()

        def take(role, avoid=()):
            for value in eligible[role]:
                suffix = value.split('_')[-1]
                if value in used or suffix in suffixes:
                    continue
                if any(set(suffix) & set(v.split('_')[-1]) for v in avoid):
                    continue
                used.add(value)
                suffixes.add(suffix)
                return value
            raise AssertionError('No lexical match without changing the frozen rules')

        a, b = take('STATE'), take('STATE')
        c, d = take('OUTCOME', (a,b)), take('OUTCOME', (a,b))
        distractors = []
        for j in range(24):
            state = take('STATE')
            distractors.append(dict(state=state, outcome=take('OUTCOME', (state,))))
        cases.append(dict(case_id=f'v362-{i:03}', gold_state=a, wrong_state=b, gold_outcome=c, wrong_outcome=d,
                          record_order=['gold','wrong'] if order == 0 else ['wrong','gold'], position_band=band, distractors=distractors))
    selected = []
    selector = random.Random(363)
    for band in BANDS:
        for first in ('gold', 'wrong'):
            selected.extend(selector.sample([c['case_id'] for c in cases if c['position_band'] == band and c['record_order'][0] == first], 2))
    checks = validate(cases, old, tokenizer)
    audit = [r | dict(selected=r['raw'] in used) for r in audit]
    return cases, selected, pool, audit, checks


def validate(cases, old, tokenizer):
    assert len(cases) == 40
    values = []
    for c in cases:
        ids = [c[k] for k in ('gold_state','wrong_state','gold_outcome','wrong_outcome')]
        ids += [v for d in c['distractors'] for v in d.values()]
        assert len(ids) == len(set(ids)) == 52
        assert len({v.split('_')[-1] for v in ids}) == 52
        assert not set(ids) & set(old)
        values += ids
        for prefix in ('STATE', 'OUTCOME'):
            group = [v for v in ids if v.startswith(prefix+'_')]
            assert len({len(v) for v in group}) == 1
            assert len({len(tokenizer.encode(v, add_special_tokens=False)) for v in group}) == 1
        for k in KS:
            audit_pair(c, k)
        for lower, higher in zip(KS, KS[1:]):
            low, high = block(c, lower), block(c, higher)
            low_set = set(low)
            assert [r for r in high if r in low_set] == low
        for band in BANDS:
            audit_pair(c, 24, band)
    assert len(set(values)) == len(values) == 2080
    assert Counter(c['position_band'] for c in cases) == dict(beginning=14, middle=13, end=13)
    assert sum(c['record_order'][0] == 'gold' for c in cases) == 20
    return dict(cases=40, selected_identifiers=2080, globally_unique_identifiers=True,
                token_and_length_matched=True, nested_by_deletion_only=True,
                bands=dict(beginning=14, middle=13, end=13), gold_first=20, wrong_first=20,
                K0_band_applicability='Only two records; middle/end bands are not distinguishable. Gold-first20/wrong-first20.',
                no_output_based_selection=True)
