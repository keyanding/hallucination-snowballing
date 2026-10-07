"""Exact inherited interfaces with canonical A/B metadata."""
import random
import re
from experiments.v3_6_3 import design as inherited
from experiments.v3_6_1.design import render as minimal_render, sha, normalize
from experiments.v3_6_2.design import render as context_render

CONDITIONS = ('U-A', 'U-B', 'D-A', 'D-B')
LEGACY = {'U-A': 'U-GOLD', 'U-B': 'U-ALT', 'D-A': 'P-GOLD', 'D-B': 'P-ALT',
          'PIPELINE-A': 'PIPELINE-GENERATED', 'I-A': 'I-GOLD', 'I-B': 'I-ALT'}


def to_legacy(c):
    r = dict(case_id=c['case_id'], split=c['split'],
             up_order=['gold' if x == 'a' else 'alt' for x in c['up_order']],
             down_order=['gold' if x == 'a' else 'alt' for x in c['down_order']])
    for field in ('entity', 'state', 'outcome'):
        r['gold_'+field], r['alt_'+field] = c[field+'_a'], c[field+'_b']
    return r


def from_legacy(c, split, index):
    r = dict(case_id=f'v3631-{split}-{index:03}', split=split,
             up_order=['a' if x == 'gold' else 'b' for x in c['up_order']],
             down_order=['a' if x == 'gold' else 'b' for x in c['down_order']])
    for field in ('entity', 'state', 'outcome'):
        r[field+'_a'], r[field+'_b'] = c['gold_'+field], c['alt_'+field]
    return r


def minimal_case(c):
    return dict(case_id=c['case_id'], gold_state=c['state_a'], wrong_state=c['state_b'],
                gold_outcome=c['outcome_a'], wrong_outcome=c['outcome_b'],
                record_order=['gold' if x == 'a' else 'wrong' for x in c['down_order']])


def parse(raw, c, upstream=False, truncated=False):
    return inherited.parse(raw, to_legacy(c), upstream, truncated)


def render(c, condition, shell='VALIDATED', supplied=None):
    if condition.startswith(('U-', 'I-')):
        r = inherited.render(to_legacy(c), LEGACY[condition])
        return r | dict(condition=condition, shell=None)
    assert condition in ('D-A', 'D-B', 'PIPELINE-A')
    state = supplied if condition == 'PIPELINE-A' else c['state_a' if condition == 'D-A' else 'state_b']
    assert state is not None
    if shell == 'RECORDED':
        assert condition != 'PIPELINE-A'
        r = inherited.render(to_legacy(c), LEGACY[condition])
        return r | dict(condition=condition, shell=shell)
    assert shell == 'VALIDATED'
    base = minimal_render(minimal_case(c), 'C0')['prompt']
    before, tail = base.split('\nCurrent state:\n')
    _, after = tail.split('\n', 1)
    prompt = before+'\nCurrent state:\n'+state+'\n'+after
    mappings = [(c['state_'+x], c['outcome_'+x]) for x in c['down_order']]
    return dict(case_id=c['case_id'], split=c['split'], condition=condition, reverse=False,
                shell=shell, supplied_state=state, current_entity=None, expected=dict(mappings).get(state),
                upstream_mappings=[], downstream_mappings=mappings, prompt=prompt, text_sha256=sha(prompt))


def audit_pair(c, prefix, shell='VALIDATED'):
    a, b = (render(c, prefix+'-'+role, shell) for role in ('A', 'B'))
    marker = 'Current entity:\n' if prefix in ('U', 'I') else 'Current state:\n' if shell == 'VALIDATED' else 'Recorded intermediate result:\n'
    before, tail = a['prompt'].split(marker)
    identifier, after = tail.split('\n', 1)
    field = 'entity' if prefix in ('U', 'I') else 'state'
    assert identifier == c[field+'_a']
    assert before+marker+c[field+'_b']+'\n'+after == b['prompt']
    for r in (a, b):
        assert not re.search(r'\b(gold|wrong|correct|alt|error)\b', r['prompt'], re.I)
        assert 'UNKNOWN' not in r['prompt'] and not re.search(r'^\d+[.)] ', r['prompt'], re.M)
        if prefix == 'D' and shell == 'VALIDATED':
            mc = minimal_case(c)
            old_condition = 'C0' if r['condition'] == 'D-A' else 'W0'
            assert r['prompt'] == minimal_render(mc, old_condition)['prompt']
            assert r['prompt'] == context_render(mc | dict(position_band='beginning', distractors=[]), 0, old_condition)['prompt']
            assert 'Recorded intermediate result' not in r['prompt'] and 'ENTITY_' not in r['prompt']
    return a, b


def pipeline(c, upstream):
    parsed = parse(upstream['raw_text'], c, True, upstream['truncated'])
    log = dict(case_id=c['case_id'], upstream_raw=upstream['raw_text'], upstream_normalized=parsed['normalized'],
               upstream_category=parsed['category'], upstream_text_sha256=upstream['text_sha256'])
    if parsed['category'] == 'INVALID':
        return None, log | dict(status='UPSTREAM_INVALID_SKIPPED')
    return render(c, 'PIPELINE-A', supplied=parsed['normalized']), log | dict(status='CALLED_UNREPAIRED')


def identifiers(cases):
    return {c[f+'_'+r] for c in cases for f in ('entity', 'state', 'outcome') for r in ('a', 'b')}


def make_cases(tokenizer, old_ids):
    # Reuse the frozen generator, seed, tokenizer buckets and order balancing exactly.
    cal0, main0, integrated0, _, pool, tokens = inherited.make_cases(tokenizer, old_ids)
    cal = [from_legacy(c, 'calibration', i) for i, c in enumerate(cal0, 1)]
    main = [from_legacy(c, 'main', i) for i, c in enumerate(main0, 1)]
    selected = [main[i]['case_id'] for i, c in enumerate(main0) if c['case_id'] in integrated0]
    blocked = old_ids | identifiers(cal+main)
    diagnostic_pool, _, _, _, _, _ = inherited.make_cases(tokenizer, blocked)
    chosen = random.Random(3631).sample(diagnostic_pool, 10)
    diagnostic = [from_legacy(c, 'diagnostic', i) for i, c in enumerate(chosen, 1)]
    all_cases = cal+main+diagnostic
    ids = identifiers(all_cases)
    assert len(ids) == 420 and not ids & old_ids
    assert len(identifiers(cal) & identifiers(main)) == len(identifiers(diagnostic) & identifiers(cal+main)) == 0
    for c in all_cases:
        for p in ('U', 'D', 'I'):
            audit_pair(c, p)
        audit_pair(c, 'D', 'RECORDED')
    audit = [r | dict(selected=r['raw'] in ids, selected_split=next((c['split'] for c in all_cases if r['raw'] in identifiers([c])), None)) for r in tokens]
    return cal, main, diagnostic, selected, pool, audit
