"""Deterministic lexical/tokenization-only design; no model-output input."""
import hashlib
import random
import re
import unicodedata
from collections import Counter
from experiments.v3_6_0.design import render as old_render

FAMILIES = ('FULL_UNKNOWN', 'FULL_NO_UNKNOWN', 'MINIMAL_UNKNOWN', 'MINIMAL_NO_UNKNOWN')
RULE = 'If the current state has no mapping, output UNKNOWN.'
SEED = 361


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def normalize(text):
    return unicodedata.normalize('NFC', text).strip().removesuffix('.')


def parse(text, case, truncated=False):
    value = normalize(text)
    if truncated:
        category = 'INVALID'
    elif value == case['gold_outcome']:
        category = 'C'
    elif value == case['wrong_outcome']:
        category = 'Cp'
    elif value == 'UNKNOWN':
        category = 'UNKNOWN'
    elif re.fullmatch(r'(?:Outcome|OUTCOME)_[A-Z][0-9]{2}', value):
        category = 'OTHER'
    else:
        category = 'INVALID'
    return dict(normalized=value, category=category, correct=not truncated and value == case.get('expected', ''))


def mappings(case, reverse=False):
    rows = [(case[r+'_state'], case[r+'_outcome']) for r in case['record_order']]
    return rows[::-1] if reverse else rows


def render(case, condition, family='MINIMAL_NO_UNKNOWN', reverse=False):
    assert family in FAMILIES
    assert condition in ('C0', 'W0', 'UNMAPPED')
    state = case['gold_state'] if condition == 'C0' else case['wrong_state'] if condition == 'W0' else case['unmapped_state']
    records = mappings(case, reverse)
    if family.startswith('FULL'):
        assert not reverse and condition != 'UNMAPPED'
        prompt = old_render(case, condition, False)['prompt']
    else:
        block = '\n'.join(f'{a} -> {b}' for a, b in records)
        prompt = f'Synthetic mapping task.\n\nMappings:\n{block}\n\nCurrent state:\n{state}\n\n'
        prompt += RULE+'\nReturn only the mapped outcome or UNKNOWN.' if condition == 'UNMAPPED' else 'Return only the mapped outcome.'
    if family.endswith('_UNKNOWN') and not family.endswith('_NO_UNKNOWN') and condition != 'UNMAPPED':
        prompt += '\n'+RULE
    expected = dict(records).get(state, 'UNKNOWN')
    return dict(case_id=case['case_id'], condition=condition, family=family, reverse=reverse,
                supplied_state=state, expected=expected, mappings=records, prompt=prompt, text_sha256=sha(prompt))


def audit_pair(case, family='MINIMAL_NO_UNKNOWN', reverse=False):
    a, b = (render(case, condition, family, reverse) for condition in ('C0', 'W0'))
    marker = 'Working intermediate state:\n' if family.startswith('FULL') else 'Current state:\n'
    prefix, tail = a['prompt'].split(marker)
    state, suffix = tail.split('\n', 1)
    assert state == case['gold_state']
    assert prefix+marker+case['wrong_state']+'\n'+suffix == b['prompt']
    assert a['mappings'] == b['mappings']
    if family.endswith('NO_UNKNOWN'):
        assert 'UNKNOWN' not in a['prompt']+b['prompt']
    else:
        assert a['prompt'].count(RULE) == b['prompt'].count(RULE) == 1
    if family.startswith('MINIMAL'):
        assert 'Entity' not in a['prompt'] and 'entity' not in a['prompt']
    return a, b


def token_info(tokenizer, identifier):
    ids = tokenizer.encode(identifier, add_special_tokens=False)
    return dict(raw=identifier, token_ids=ids, token_count=len(ids), character_length=len(identifier))


def build_cases(tokenizer, old_cases):
    # Exclude all old suffixes, including entity and unmapped IDs, as a conservative fresh-ID rule.
    old_ids = {v for c in old_cases for k, v in c.items() if k in ('entity', 'alternate_entity', 'unmapped_state', 'gold_state', 'wrong_state', 'gold_outcome', 'wrong_outcome')}
    old_suffixes = {v.split('_')[-1] for v in old_ids}
    pool = [prefix+'_'+letter+f'{n:02}' for prefix in ('STATE', 'OUTCOME') for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for n in range(100)]
    audit = [token_info(tokenizer, v) | dict(eligible=v.split('_')[-1] not in old_suffixes) for v in pool]
    candidates = {}
    for role in ('STATE', 'OUTCOME'):
        sub = [r for r in audit if r['eligible'] and r['raw'].startswith(role+'_')]
        minimum = min(r['token_count'] for r in sub)
        candidates[role] = [r['raw'] for r in sub if r['token_count'] == minimum]
        assert len(candidates[role]) >= 250
    rng = random.Random(SEED)
    for rows in candidates.values():
        rng.shuffle(rows)
    used_suffixes = set(old_suffixes)

    def take(role, avoid=()):
        for value in candidates[role]:
            suffix = value.split('_')[-1]
            if suffix in used_suffixes:
                continue
            # Stronger than no distinctive shared suffix: no shared suffix characters.
            if any(set(suffix) & set(v.split('_')[-1]) for v in avoid):
                continue
            used_suffixes.add(suffix)
            return value
        raise AssertionError('Insufficient lexical/token-balanced candidates')

    cases, controls = [], []
    for stage, count, target in [('main', 40, cases), ('unmapped', 10, controls)]:
        orders = [['gold', 'wrong']]*(count//2)+[['wrong', 'gold']]*(count//2)
        rng.shuffle(orders)
        for i, order in enumerate(orders, 1):
            a, b = take('STATE'), take('STATE')
            c = take('OUTCOME', (a, b))
            d = take('OUTCOME', (a, b, c))
            row = dict(case_id=f'v361-{stage}-{i:03}', gold_state=a, wrong_state=b,
                       gold_outcome=c, wrong_outcome=d, record_order=order)
            if stage == 'unmapped':
                row['unmapped_state'] = take('STATE')
            target.append(row)
    checks = validate(cases, controls, old_ids, tokenizer)
    selected = {v for c in cases+controls for k, v in c.items() if k.endswith('_state') or k.endswith('_outcome')}
    audit = [r | dict(selected=r['raw'] in selected) for r in audit]
    return cases, controls, pool, audit, checks


def validate(cases, controls, old_ids, tokenizer):
    assert len(cases) == 40 and len(controls) == 10
    identifiers = []
    for c in cases+controls:
        values = [v for k, v in c.items() if k.endswith('_state') or k.endswith('_outcome')]
        identifiers += values
        for a in values:
            assert a not in old_ids
            assert all(a not in b for b in values if a != b)
        for role in ('state', 'outcome'):
            a, b = c['gold_'+role], c['wrong_'+role]
            assert len(a) == len(b)
            assert len(tokenizer.encode(a, add_special_tokens=False)) == len(tokenizer.encode(b, add_special_tokens=False))
        for state in (c['gold_state'], c['wrong_state']):
            for outcome in (c['gold_outcome'], c['wrong_outcome']):
                assert not set(state.split('_')[-1]) & set(outcome.split('_')[-1])
        audit_pair(c)
    assert len(identifiers) == len(set(identifiers)) == 210
    assert sum(c['record_order'][0] == 'gold' for c in cases) == 20
    return dict(unique_new_identifiers=210, candidate_pool=5200, gold_first=20, wrong_first=20,
                token_counts_matched=True, lengths_matched=True, no_substrings=True,
                no_shared_state_outcome_suffix_characters=True, selection_uses_model_outputs=False)
