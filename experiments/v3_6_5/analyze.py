"""Historical exact-name parsing and pre-registered yield gates."""
from collections import Counter
from .design import parse_natural

CATEGORIES=('IN_SET_VALID_GOLD','IN_SET_VALID_WRONG','OUT_OF_SET','AMBIGUOUS','NONCOMPLIANT','TRUNCATED')


def parse(row,aliases):
    assert set(row['names'])==set(row['downstream_endpoints'])
    result=parse_natural(row['raw_text'],row['names'],row['truncated'],aliases)
    category=result['category']
    if result['strict_valid']:
        category='IN_SET_VALID_GOLD' if result['identity']==row['gold'] else 'IN_SET_VALID_WRONG'
    return result|dict(category=category,case_id=row['case_id'],call_id=row['call_id'],traceable_wrong=category=='IN_SET_VALID_WRONG')


def metrics(rows,ids,aliases,confirmation=False):
    assert len({r['case_id'] for r in rows})==len(rows)
    assert {r['case_id'] for r in rows}<=set(ids)
    parsed=[parse(r,aliases) for r in rows]
    counts=Counter(r['category'] for r in parsed)
    wrong=[r for r in parsed if r['traceable_wrong']]
    valid=sum(r['strict_valid'] for r in parsed)
    complete=len(rows)==24 and {r['case_id'] for r in rows}==set(ids)
    checks=dict(valid=valid>=22,traceable_wrong=len(wrong)>=(3 if confirmation else 4),
                distinct_wrong_cases=len({r['case_id'] for r in wrong})>=3,
                format_failures=sum(counts[k] for k in ('AMBIGUOUS','NONCOMPLIANT','TRUNCATED'))<=2,
                all_wrong_traceable=all(r['identity'] for r in wrong))
    return dict(evaluated=bool(rows),complete=complete,calls=len(rows),denominator=24,valid=valid,
                counts={k:counts[k] for k in CATEGORIES},traceable_wrong=len(wrong),
                distinct_wrong_cases=len({r['case_id'] for r in wrong}),distinct_wrong_identities=len({r['identity'] for r in wrong}),
                wrong_case_ids=[r['case_id'] for r in wrong],wrong_identities=sorted({r['identity'] for r in wrong}),
                wrong_rate=len(wrong)/24 if complete else None,checks=checks,passed=complete and all(checks.values()),parsed=parsed)


def diagnostic(rows,primary,ids,aliases):
    assert len({r['case_id'] for r in rows})==len(rows)
    assert {r['case_id'] for r in rows}<=set(ids)
    original={r['case_id']:r for r in primary}
    pairs=[]
    for r in rows:
        a,b=parse(original[r['case_id']],aliases),parse(r,aliases)
        both=a['strict_valid'] and b['strict_valid']
        same=both and a['identity']==b['identity']
        pairs.append(dict(case_id=r['case_id'],original=a,permuted=b,comparable=both,same_identity=same,
                          changed_identity=both and not same,gold_to_wrong=a['category']=='IN_SET_VALID_GOLD' and b['traceable_wrong'],
                          wrong_to_gold=a['traceable_wrong'] and b['category']=='IN_SET_VALID_GOLD',
                          wrong_to_different_wrong=a['traceable_wrong'] and b['traceable_wrong'] and not same,
                          same_wrong_identity=a['traceable_wrong'] and same))
    result=dict(evaluated=bool(rows),complete=len(rows)==8,calls=len(rows),denominator=8,pairs=pairs,
                primary_strict_valid=sum(p['original']['strict_valid'] for p in pairs),diagnostic_strict_valid=sum(p['permuted']['strict_valid'] for p in pairs))
    for k in ('comparable','same_identity','changed_identity','gold_to_wrong','wrong_to_gold','wrong_to_different_wrong','same_wrong_identity'):
        result[k]=sum(p[k] for p in pairs)
    result['PRESENTATION_SENSITIVE']=result['changed_identity']>3 if rows else 'not_evaluated'
    return result


def decide(dev,confirm,diag,policy,infrastructure=False):
    if infrastructure or not dev['complete']:
        return 'INFRASTRUCTURE_FAILURE'
    required=dev['passed'] or policy['diagnostic_on_development_failure']
    if required and not diag['complete'] or not required and diag['evaluated']:
        return 'INFRASTRUCTURE_FAILURE'
    if not dev['passed']:
        return 'INFRASTRUCTURE_FAILURE' if confirm['evaluated'] else 'HARD_N_SIGNAL_NOT_REPLICATED'
    if not confirm['complete']:
        return 'INFRASTRUCTURE_FAILURE'
    return 'HARD_N_NATURAL_ERROR_SIGNAL_CONFIRMED' if confirm['passed'] else 'HARD_N_CONFIRMATION_FAILED'
