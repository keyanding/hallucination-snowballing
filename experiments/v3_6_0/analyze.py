"""Calibration A-H and paired main metrics; all thresholds are fixed."""
import math
from collections import Counter
from .design import parse

CATEGORIES = ('C', 'Cp', 'UNKNOWN', 'OTHER', 'INVALID')


def rate(count, denominator, complete=True):
    return dict(count=count, denominator=denominator, rate=count/denominator if complete and denominator else None)


def wilson(count, denominator):
    if not denominator:
        return None
    z = 1.959963984540054
    p = count/denominator
    d = 1+z*z/denominator
    center = (p+z*z/(2*denominator))/d
    radius = z*math.sqrt(p*(1-p)/denominator+z*z/(4*denominator**2))/d
    return [max(0., center-radius), min(1., center+radius)]


def parsed_rows(cases, rows):
    lookup = {c['case_id']: c for c in cases}
    assert len({(r['case_id'], r['condition']) for r in rows}) == len(rows)
    return [r | parse(r['raw_text'], lookup[r['case_id']], r['truncated']) for r in rows]


def calibration_metrics(cases, rows):
    parsed = parsed_rows(cases, rows)
    lookup = {(r['case_id'], r['condition']): r for r in parsed}
    complete = len(parsed) == 160
    correct = Counter(r['condition'] for r in parsed if r['permitted'] and r['normalized'] == r['expected'])
    def unchanged(condition):
        return sum((c['case_id'], 'C0') in lookup and (c['case_id'], condition) in lookup
                   and lookup[c['case_id'], 'C0']['permitted'] and lookup[c['case_id'], condition]['permitted']
                   and lookup[c['case_id'], 'C0']['normalized'] == lookup[c['case_id'], condition]['normalized'] for c in cases)
    counts = dict(A=correct['LOOKUP_GOLD']+correct['LOOKUP_WRONG'], B=correct['C0'], C=correct['W0'],
                  D=correct['SWAP'], E=unchanged('REVERSE'), F=correct['UNMAPPED'],
                  G=sum(r['permitted'] for r in parsed), H=unchanged('ENTITY_LABEL'))
    denominators = dict(A=40, B=20, C=20, D=20, E=20, F=20, G=160, H=20)
    minima = dict(A=38, B=19, C=19, D=19, E=19, F=18, G=159, H=19)
    gates = {k: dict(**rate(counts[k], denominators[k], complete), minimum=minima[k],
                     passed=complete and counts[k] >= minima[k]) for k in counts}
    return parsed, dict(complete=complete, gates=gates, passed=complete and all(g['passed'] for g in gates.values()),
                        category_counts={k: sum(r['category'] == k for r in parsed) for k in CATEGORIES},
                        correct_by_condition=dict(correct), unchanged_def='Both parsed outputs permitted and normalized-identical to same-case C0; correctness separately reported.')


def main_metrics(cases, rows):
    parsed = parsed_rows(cases, rows)
    by = {(r['case_id'], r['condition']): r for r in parsed}
    complete = len(parsed) == 80
    counts = {k: {c: sum(r['condition'] == k and r['category'] == c for r in parsed) for c in CATEGORIES} for k in ('C0', 'W0')}
    transitions = {a: {b: 0 for b in CATEGORIES} for a in CATEGORIES}
    pairs = []
    for c in cases:
        if (c['case_id'], 'C0') not in by or (c['case_id'], 'W0') not in by:
            continue
        a, b = by[c['case_id'], 'C0'], by[c['case_id'], 'W0']
        transitions[a['category']][b['category']] += 1
        pairs.append(dict(case_id=c['case_id'], C0=a['category'], W0=b['category'],
                          switched=a['category'] == 'C' and b['category'] == 'Cp'))
    switch = sum(p['switched'] for p in pairs)
    metrics = dict(A_C=rate(counts['C0']['C'], 40, complete), A_W=rate(counts['W0']['Cp'], 40, complete),
                   S=rate(switch, 40, complete), Cp_under_C0=rate(counts['C0']['Cp'], 40, complete),
                   delta_state=dict(numerator=counts['W0']['Cp']-counts['C0']['Cp'], denominator=40,
                                    rate=(counts['W0']['Cp']-counts['C0']['Cp'])/40 if complete else None))
    for k in ('A_C', 'A_W', 'S'):
        metrics[k]['wilson_95'] = wilson(metrics[k]['count'], 40) if complete else None
    other_invalid = sum(counts[k][v] for k in counts for v in ('OTHER', 'INVALID'))
    gates = dict(G1=complete and counts['C0']['C'] >= 38, G2=complete and counts['W0']['Cp'] >= 38,
                 G3=complete and switch >= 36, G4=complete and counts['C0']['Cp'] <= 2,
                 G5=complete and other_invalid <= 2)
    return parsed, dict(complete=complete, metrics=metrics, condition_counts=counts,
                        other_plus_invalid=rate(other_invalid, 80, complete), gates=gates,
                        passed=all(gates.values()), paired_transitions=transitions, pairs=pairs,
                        statistical_unit='40 paired base cases; not 80 independent semantic populations.')


def decide(calibration, main):
    if not calibration['passed']:
        return 'STOP_ASSAY_INVALID'
    return 'ASSAY_VALIDATED' if main['passed'] else 'STOP_MAIN_ASSAY_INVALID'
