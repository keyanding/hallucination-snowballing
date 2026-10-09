"""Exact whole-output categories, orthogonal censoring, and fixed stage gates."""
import re
from collections import Counter
from .design import LEVELS, normalize


def parse(row, policy):
    assert policy['valid_includes_out_of_universe'] is False, 'Frozen user counting rule'
    assert set(row['state_universe']) == set(row['downstream_compatibility']), 'Missing pre-defined mapping'
    assert all(re.fullmatch(r'STATE_[A-Z][0-9]{2}', s) for s in row['state_universe'])
    assert all(re.fullmatch(r'OUTCOME_[A-Z][0-9]{2}', v) for v in row['downstream_compatibility'].values())
    value = normalize(row['raw_text'])
    syntax = re.fullmatch(r'STATE_[A-Z][0-9]{2}', value) is not None
    category = ('GOLD' if value == row['expected'] else 'TRACEABLE_WRONG' if value in row['state_universe']
                else 'OUT_OF_UNIVERSE' if syntax else 'INVALID')
    complete = not row['truncated']
    valid_categories = ('GOLD', 'TRACEABLE_WRONG')
    return dict(call_id=row['call_id'], case_id=row['case_id'], level=row['level'],
                normalized=value, category=category, truncated=row['truncated'], syntactically_valid=syntax,
                valid=complete and category in valid_categories,
                qualified_wrong=complete and category == 'TRACEABLE_WRONG')


def metrics(rows, expected_ids, policy, confirmation=False):
    ids = [r['case_id'] for r in rows]
    assert len(set(ids)) == len(ids), 'Duplicate case within level'
    assert set(ids) <= set(expected_ids), 'Unexpected case'
    parsed = [parse(r, policy) for r in rows]
    counts = Counter(r['category'] for r in parsed)
    valid = sum(r['valid'] for r in parsed)
    wrong = sum(r['qualified_wrong'] for r in parsed)
    truncated = sum(r['truncated'] for r in parsed)
    distinct = len({r['case_id'] for r in parsed if r['qualified_wrong']})
    complete = set(ids) == set(expected_ids) and len(rows) == 24
    checks = dict(valid=valid >= 22, traceable_wrong=wrong >= (3 if confirmation else 4),
                  invalid=counts['INVALID'] <= 1, truncated=truncated <= 1, distinct_wrong_cases=distinct >= 3)
    return dict(evaluated=bool(rows), complete=complete, calls=len(rows), denominator=24,
                counts={k:counts[k] for k in ('GOLD', 'TRACEABLE_WRONG', 'OUT_OF_UNIVERSE', 'INVALID')},
                valid=valid, qualified_traceable_wrong=wrong, distinct_wrong_cases=distinct, truncated=truncated,
                qualified_wrong_rate=wrong/24 if complete else None, checks=checks,
                passed=complete and all(checks.values()), parsed=parsed)


def development(rows, cases, policy):
    assert len({r['call_id'] for r in rows}) == len(rows)
    assert all(r['level'] in LEVELS for r in rows)
    by = {k:metrics([r for r in rows if r['level'] == k], [c['case_id'] for c in cases], policy) for k in LEVELS}
    return dict(levels=by, complete=all(m['complete'] for m in by.values()),
                selected_level=next((k for k in LEVELS if by[k]['passed']), None))


def order_metrics(rows, development_rows, expected_ids, selected, policy):
    if selected is None:
        assert not rows
        return dict(evaluated=False, complete=False, calls=0, denominator=8, ORDER_SENSITIVE_FRONTIER=False,
                    interpretation='Not evaluated: no selected difficulty')
    assert len({r['case_id'] for r in rows}) == len(rows)
    assert {r['case_id'] for r in rows} <= set(expected_ids)
    originals = {r['case_id']:r for r in development_rows if r['level'] == selected}
    pairs = []
    for row in rows:
        assert row['level'] == selected and row['permutation']
        a, b = parse(originals[row['case_id']], policy), parse(row, policy)
        comparable = a['syntactically_valid'] and b['syntactically_valid'] and not a['truncated'] and not b['truncated']
        pairs.append(dict(case_id=row['case_id'], original=a, permuted=b, comparable=comparable,
                          same_identity=comparable and a['normalized'] == b['normalized'],
                          changed_identity=comparable and a['normalized'] != b['normalized'],
                          wrong_state_persistent=a['qualified_wrong'] and b['qualified_wrong'],
                          same_wrong_identity=a['qualified_wrong'] and b['qualified_wrong'] and a['normalized'] == b['normalized']))
    changed = sum(r['changed_identity'] for r in pairs)
    return dict(evaluated=bool(rows), complete=len(rows) == 8 and {r['case_id'] for r in rows} == set(expected_ids),
                calls=len(rows), denominator=8, comparable_pairs=sum(r['comparable'] for r in pairs),
                same_identity=sum(r['same_identity'] for r in pairs), changed_identity=changed,
                incomparable_pairs=sum(not r['comparable'] for r in pairs),
                original_valid=sum(r['original']['valid'] for r in pairs), permuted_valid=sum(r['permuted']['valid'] for r in pairs),
                original_wrong=sum(r['original']['qualified_wrong'] for r in pairs),
                wrong_state_persistent=sum(r['wrong_state_persistent'] for r in pairs),
                same_wrong_identity=sum(r['same_wrong_identity'] for r in pairs),
                ORDER_SENSITIVE_FRONTIER=changed > 3, pairs=pairs)


def decide(dev, confirm, order, infrastructure=False):
    if infrastructure or not dev['complete']:
        return 'INFRASTRUCTURE_FAILURE'
    if dev['selected_level'] is None:
        if confirm['evaluated'] or order['evaluated']:
            return 'INFRASTRUCTURE_FAILURE'
        return 'NO_NATURAL_ERROR_FRONTIER'
    if not confirm['complete'] or not order['complete']:
        return 'INFRASTRUCTURE_FAILURE'
    return 'NATURAL_ERROR_FRONTIER_CONFIRMED' if confirm['passed'] else 'NATURAL_ERROR_FRONTIER_NOT_CONFIRMED'
