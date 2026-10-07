"""Inherited gate arithmetic with new names and separate shell diagnostics."""
import re
from experiments.v3_6_3 import analyze as previous
from .design import to_legacy, LEGACY, parse

NAMES = {v:k for k,v in LEGACY.items()}


def old_rows(rows):
    return [r | dict(condition=LEGACY[r['condition']]) for r in rows]


def new_rows(rows):
    return [r | dict(condition=NAMES[r['condition']]) for r in rows]


def names(metrics):
    for key in ('correct', 'categories'):
        if key in metrics:
            metrics[key] = {NAMES[k]:v for k,v in metrics[key].items()}
    for key in ('pairs', 'tables'):
        if key in metrics:
            metrics[key] = {('D' if k == 'P' else k):v for k,v in metrics[key].items()}
    return metrics


def calibration(cases, rows):
    p,m = previous.calibration([to_legacy(c) for c in cases], old_rows(rows))
    return new_rows(p), names(m)


def main_metrics(cases, upstream, downstream, pipelines, logs):
    p,m = previous.main_metrics([to_legacy(c) for c in cases], old_rows(upstream), old_rows(downstream), old_rows(pipelines), logs)
    rename = dict(A_U_G='A_U_A', A_U_A='A_U_B', A_P_G='A_D_A', A_P_A='A_D_B', S_P='S_D', E2E='E2E')
    m['metrics'] = {rename[k]:v for k,v in m['metrics'].items()}
    return new_rows(p), names(m)


def integrated(cases, subset, rows):
    p,m = previous.integrated([to_legacy(c) for c in cases], subset, old_rows(rows))
    m['I_A'], m['I_B'] = m.pop('I_G'), m.pop('I_A')
    return new_rows(p), m


def shell_flags(raw, parsed, case, truncated):
    v = parsed['normalized']
    prefix = parsed['category'] == 'INVALID' and v in {case['outcome_a'].split('_')[-1], case['outcome_b'].split('_')[-1]}
    # Standalone alphabetic words, excluding underscore-joined identifiers, mark prose-like INVALID output.
    explanation = parsed['category'] == 'INVALID' and bool(re.search(r'\b[A-Za-z]{2,}\b', v))
    return dict(prefix_omission=prefix, explanation_format=explanation, truncation=truncated)


def shell_diagnostic(cases, rows):
    lookup = {c['case_id']:c for c in cases}
    assert len({(r['case_id'],r['condition'],r['shell']) for r in rows}) == len(rows)
    parsed = []
    for r in rows:
        p = parse(r['raw_text'], lookup[r['case_id']], False, r['truncated'])
        parsed.append(r | p | shell_flags(r['raw_text'], p, lookup[r['case_id']], r['truncated']))
    expected = {(cid, condition, shell) for cid in lookup for condition in ('D-A','D-B') for shell in ('VALIDATED','RECORDED')}
    complete = len(rows) == 40 and {(r['case_id'],r['condition'],r['shell']) for r in rows} == expected
    metrics = {}
    for shell in ('VALIDATED','RECORDED'):
        sub = [r for r in parsed if r['shell'] == shell]
        correct = sum(r['category'] == ('C' if r['condition'] == 'D-A' else 'Cp') for r in sub)
        metrics[shell] = dict(exact_accuracy=previous.measure(correct,20,complete),
            by_state={condition:previous.measure(sum(r['condition']==condition and r['category']==('C' if condition=='D-A' else 'Cp') for r in sub),10,complete) for condition in ('D-A','D-B')},
            invalid_count=sum(r['category']=='INVALID' for r in sub),
            explanation_format_count=sum(r['explanation_format'] for r in sub),prefix_omission_count=sum(r['prefix_omission'] for r in sub),
            truncation_count=sum(r['truncation'] for r in sub),category_counts={cat:sum(r['category']==cat for r in sub) for cat in previous.DOWN_CATS})
    by = {(r['case_id'],r['condition'],r['shell']):r for r in parsed}
    pairs = []
    for cid in lookup:
        for condition in ('D-A','D-B'):
            if not all((cid,condition,shell) in by for shell in metrics):
                continue
            a,b = (by[cid,condition,shell] for shell in ('VALIDATED','RECORDED'))
            target = 'C' if condition=='D-A' else 'Cp'
            pairs.append(dict(case_id=cid,condition=condition,validated=a['category'],recorded=b['category'],
                              validated_output=a['normalized'],recorded_output=b['normalized'],
                              validated_correct=a['category']==target,recorded_correct=b['category']==target))
    return parsed, dict(evaluated=complete,shells=metrics,paired_transitions=pairs,
                        recorded_only_failures=sum(p['validated_correct'] and not p['recorded_correct'] for p in pairs),
                        validated_only_failures=sum(p['recorded_correct'] and not p['validated_correct'] for p in pairs),
                        non_gating=True,counts_may_overlap=True)


def decide(cal, main, shell, integrated_result, infrastructure_failed=False):
    if infrastructure_failed or not cal['complete']:
        return 'INFRASTRUCTURE_FAILURE'
    if not cal['passed']:
        return 'STOP_V3631_CALIBRATION_INVALID'
    if not main['complete'] or not shell['evaluated']:
        return 'INFRASTRUCTURE_FAILURE'
    if not main['passed']:
        return 'TWO_HOP_PIPELINE_INVALID'
    if not integrated_result['evaluated']:
        return 'INFRASTRUCTURE_FAILURE'
    return 'TWO_HOP_PIPELINE_VALIDATED'
