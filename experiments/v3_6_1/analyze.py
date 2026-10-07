"""Fixed gates and paired descriptive contrasts, without significance claims."""
import itertools
from .design import parse, FAMILIES
from experiments.v3_6_0.analyze import wilson

CATEGORIES = ('C', 'Cp', 'UNKNOWN', 'OTHER', 'INVALID')


def parsed(cases, rows):
    by = {c['case_id']: c for c in cases}
    assert len({(r['case_id'], r['family'], r['condition'], r['reverse']) for r in rows}) == len(rows)
    return [r | parse(r['raw_text'], by[r['case_id']] | dict(expected=r['expected']), r['truncated']) for r in rows]


def measure(count, n, complete=True):
    return dict(count=count, denominator=n, rate=count/n if complete else None)


def adherence(cases, rows):
    n = len(cases)
    expected = {(c['case_id'], k) for c in cases for k in ('C0', 'W0')}
    by = {(r['case_id'], r['condition']):r for r in rows}
    complete = set(by) == expected and len(rows) == 2*n
    counts = {k: {v:sum(r['condition'] == k and r['category'] == v for r in rows) for v in CATEGORIES} for k in ('C0', 'W0')}
    switches = sum(by[c['case_id'], 'C0']['category'] == 'C' and by[c['case_id'], 'W0']['category'] == 'Cp' for c in cases if (c['case_id'], 'C0') in by and (c['case_id'], 'W0') in by)
    metrics = dict(A_C=measure(counts['C0']['C'], n, complete), A_W=measure(counts['W0']['Cp'], n, complete),
                   S=measure(switches, n, complete), U=measure(sum(r['category'] == 'UNKNOWN' for r in rows), 2*n, complete),
                   OTHER_INVALID=measure(sum(r['category'] in ('OTHER', 'INVALID') for r in rows), 2*n, complete),
                   mapped_correct=measure(sum(r['correct'] for r in rows), 2*n, complete))
    for k in ('A_C', 'A_W', 'S'):
        metrics[k]['wilson_95'] = wilson(metrics[k]['count'], n) if complete else None
    return dict(complete=complete, metrics=metrics, condition_counts=counts)


def stage_b(cases, rows):
    rows = parsed(cases, rows)
    families = {f: adherence(cases, [r for r in rows if r['family'] == f]) for f in FAMILIES}
    transitions = {}
    by = {(r['case_id'], r['family'], r['condition']):r for r in rows}
    for a, b in itertools.combinations(FAMILIES, 2):
        records = []
        matrix = {k:{x:{y:0 for y in CATEGORIES} for x in CATEGORIES} for k in ('C0', 'W0')}
        for c in cases:
            for k in ('C0', 'W0'):
                if (c['case_id'], a, k) not in by or (c['case_id'], b, k) not in by:
                    continue
                x, y = by[c['case_id'], a, k], by[c['case_id'], b, k]
                matrix[k][x['category']][y['category']] += 1
                records.append(dict(case_id=c['case_id'], condition=k, before=x['category'], after=y['category'], before_output=x['normalized'], after_output=y['normalized'], correct_before=x['correct'], correct_after=y['correct']))
        transitions[a+' -> '+b] = dict(matrix=matrix, cases=records,
                                      corrected=sum(not r['correct_before'] and r['correct_after'] for r in records),
                                      broken=sum(r['correct_before'] and not r['correct_after'] for r in records))
    complete = len(rows) == 160 and all(f['complete'] for f in families.values())
    best = []
    if complete:
        maximum = max(f['metrics']['mapped_correct']['count'] for f in families.values())
        best = [k for k, f in families.items() if f['metrics']['mapped_correct']['count'] == maximum]
    return rows, dict(complete=complete, families=families, paired_transitions=transitions,
                     best_descriptive_conditions=best, tie_rule='All ties by mapped correct /40; no selected family changes Stage C.',
                     P3=complete and families['MINIMAL_NO_UNKNOWN']['metrics']['mapped_correct']['count'] < 39)


def stage_c(cases, controls, rows, unmapped, reversed_rows):
    rows, unmapped, reversed_rows = parsed(cases, rows), parsed(controls, unmapped), parsed(cases, reversed_rows)
    primary = adherence(cases, rows)
    m = primary['metrics']
    complete = primary['complete'] and len(unmapped) == 10 and {r['case_id'] for r in unmapped} == {c['case_id'] for c in controls}
    fallback = sum(r['correct'] for r in unmapped)
    gates = dict(C1=complete and m['A_C']['count'] >= 39, C2=complete and m['A_W']['count'] >= 39,
                 C3=complete and m['S']['count'] >= 39, C4=complete and m['U']['count'] == 0,
                 C5=complete and m['OTHER_INVALID']['count'] <= 1, C6=complete and fallback >= 9)
    by = {(r['case_id'], r['condition']):r for r in rows}
    order_pairs = []
    for r in reversed_rows:
        key = (r['case_id'], r['condition'])
        if key not in by:
            continue
        base = by[key]
        unchanged = base['category'] in ('C', 'Cp') and r['category'] in ('C', 'Cp') and base['normalized'] == r['normalized']
        order_pairs.append(dict(case_id=r['case_id'], condition=r['condition'], before=base['category'], after=r['category'], unchanged_mapped_identity=unchanged, reverse_correct=r['correct']))
    count = sum(p['unchanged_mapped_identity'] for p in order_pairs)
    order = dict(**measure(count, 20, len(order_pairs) == 20), complete=len(order_pairs) == 20,
                 passed=len(order_pairs) == 20 and count >= 19, correct=sum(r['correct'] for r in reversed_rows), pairs=order_pairs)
    return rows+unmapped+reversed_rows, dict(**primary, fallback=measure(fallback, 10, len(unmapped) == 10),
        fallback_category_counts={k:sum(r['category'] == k for r in unmapped) for k in CATEGORIES},
        all_primary_complete=complete, gates=gates, passed=all(gates.values()), record_order=order)


def decision(b, c, infrastructure_failed=False):
    if infrastructure_failed or not b['complete'] or not c['all_primary_complete'] or not c['record_order']['complete']:
        return 'INFRASTRUCTURE_FAILURE'
    return 'MINIMAL_ASSAY_VALIDATED' if c['passed'] else 'MINIMAL_ASSAY_INVALID'
