"""Per-K paired metrics and the user-amended decision hierarchy."""
import itertools
from .design import KS, BANDS, parse
from experiments.v3_6_0.analyze import wilson

CATS = ('C','Cp','UNKNOWN','OTHER','INVALID')


def measure(count, denominator, complete=True):
    return dict(count=count, denominator=denominator, rate=count/denominator if complete else None)


def parsed(cases, rows):
    by = {c['case_id']:c for c in cases}
    keys = [(r['case_id'],r['k'],r['condition'],r['position_band'],r['stage']) for r in rows]
    assert len(keys) == len(set(keys)), 'Duplicate calls'
    return [r | parse(r['raw_text'], by[r['case_id']], r['expected'], r['truncated']) for r in rows]


def matrix():
    return {a:{b:0 for b in CATS} for a in CATS}


def per_level(cases, rows):
    by = {(r['case_id'],r['condition']):r for r in rows}
    complete = len(rows) == 80 and set(by) == {(c['case_id'],k) for c in cases for k in ('C0','W0')}
    counts = {k:{cat:sum(r['condition'] == k and r['category'] == cat for r in rows) for cat in CATS} for k in ('C0','W0')}
    paired, pairs = matrix(), []
    for c in cases:
        if any((c['case_id'],k) not in by for k in ('C0','W0')):
            continue
        a,b = (by[c['case_id'],k] for k in ('C0','W0'))
        paired[a['category']][b['category']] += 1
        pairs.append(dict(case_id=c['case_id'], C0=a['category'], W0=b['category'], both_correct=a['correct'] and b['correct']))
    m = dict(A_C=measure(counts['C0']['C'],40,complete), A_W=measure(counts['W0']['Cp'],40,complete),
             S=measure(sum(p['both_correct'] for p in pairs),40,complete),
             U=measure(sum(r['category'] == 'UNKNOWN' for r in rows),80,complete),
             O=measure(sum(r['category'] in ('OTHER','INVALID') for r in rows),80,complete))
    for k in ('A_C','A_W','S'):
        m[k]['wilson_95'] = wilson(m[k]['count'],40) if complete else None
    return dict(complete=complete, metrics=m, condition_counts=counts, state_pair_transitions=paired, case_pairs=pairs)


def main_metrics(cases, raw):
    rows = parsed(cases,raw)
    levels = {str(k):per_level(cases,[r for r in rows if r['k'] == k]) for k in KS}
    by = {(r['case_id'],r['k'],r['condition']):r for r in rows}
    degradation = {}
    for k in KS[1:]:
        complete = levels['0']['complete'] and levels[str(k)]['complete']
        arms = {}
        for arm in ('C0','W0'):
            pairs, tab = [], matrix()
            for c in cases:
                keys = ((c['case_id'],0,arm),(c['case_id'],k,arm))
                if not all(key in by for key in keys):
                    continue
                a,b = (by[key] for key in keys)
                tab[a['category']][b['category']] += 1
                pairs.append(dict(case_id=c['case_id'], before=a['category'], after=b['category'], before_output=a['normalized'], after_output=b['normalized'], before_correct=a['correct'], after_correct=b['correct']))
            arms[arm] = dict(case_transitions=pairs, category_transitions=tab,
                             correct_to_incorrect=sum(p['before_correct'] and not p['after_correct'] for p in pairs),
                             incorrect_to_correct=sum(not p['before_correct'] and p['after_correct'] for p in pairs),
                             correct_to_wrong_or_unknown=sum(p['before_correct'] and p['after'] in (('Cp','UNKNOWN') if arm == 'C0' else ('C','UNKNOWN')) for p in pairs))
        pairby = {n:{p['case_id']:p['both_correct'] for p in levels[n]['case_pairs']} for n in ('0',str(k))}
        lost = [c['case_id'] for c in cases if pairby['0'].get(c['case_id'],False) and c['case_id'] in pairby[str(k)] and not pairby[str(k)][c['case_id']]]
        gained = [c['case_id'] for c in cases if c['case_id'] in pairby['0'] and not pairby['0'][c['case_id']] and pairby[str(k)].get(c['case_id'],False)]
        deltas = {name:dict(numerator=levels[str(k)]['metrics'][metric]['count']-levels['0']['metrics'][metric]['count'], denominator=40,
                           rate=(levels[str(k)]['metrics'][metric]['count']-levels['0']['metrics'][metric]['count'])/40 if complete else None) for name,metric in (('delta_C','A_C'),('delta_W','A_W'),('delta_S','S'))}
        degradation[str(k)] = dict(complete=complete, arms=arms, paired_lost=lost, paired_gained=gained,
                                    lost_count=len(lost), gained_count=len(gained), deltas=deltas)
    complete = len(rows) == 320 and all(v['complete'] for v in levels.values())
    s = [levels[str(k)]['metrics']['S']['count'] for k in KS]
    collapse = complete and all(a>=b for a,b in zip(s,s[1:])) and sum(a>b for a,b in zip(s,s[1:])) >= 2 and s[0]-s[-1] >= 4
    off_target = {str(k):levels[str(k)]['metrics']['O']['count'] for k in KS}
    return rows, dict(complete=complete, levels=levels, degradation=degradation, monotonic_collapse=collapse,
                     paired_success_counts=s, off_target_by_k=off_target, total_off_target=sum(off_target.values()),
                     statistical_unit='40 paired base cases; report C0/W0 separately; 320 calls are not 320 independent populations.')


def diagnostic_metrics(cases, selected, raw, primary):
    rows = parsed(cases,raw)
    expected = {(cid,band,arm) for cid in selected for band in BANDS for arm in ('C0','W0')}
    complete = len(rows) == 72 and {(r['case_id'],r['position_band'],r['condition']) for r in rows} == expected
    by = {(r['case_id'],r['position_band'],r['condition']):r for r in rows}
    bands = {}
    for band in BANDS:
        subset = [r for r in rows if r['position_band'] == band]
        bands[band] = dict(C0=measure(sum(r['condition']=='C0' and r['correct'] for r in subset),12,complete),
                           W0=measure(sum(r['condition']=='W0' and r['correct'] for r in subset),12,complete),
                           UNKNOWN=measure(sum(r['category']=='UNKNOWN' for r in subset),24,complete),
                           OTHER_INVALID=measure(sum(r['category'] in ('OTHER','INVALID') for r in subset),24,complete))
    transitions = {}
    for a,b in itertools.combinations(BANDS,2):
        pairs=[]
        for cid in selected:
            for arm in ('C0','W0'):
                if (cid,a,arm) in by and (cid,b,arm) in by:
                    x,y=by[cid,a,arm],by[cid,b,arm]
                    pairs.append(dict(case_id=cid,condition=arm,before=x['category'],after=y['category'],
                                      before_correct=x['correct'],after_correct=y['correct']))
        transitions[a+' -> '+b] = pairs
    primary_by = {(r['case_id'],r['position_band'],r['condition']):r for r in primary if r['k']==24}
    repeats=[]
    for r in rows:
        key=(r['case_id'],r['position_band'],r['condition'])
        if key in primary_by:
            p=primary_by[key]
            assert p['prompt']==r['prompt']
            repeats.append(dict(case_id=r['case_id'],condition=r['condition'],raw_identical=p['raw_text']==r['raw_text'],token_identical=p['output_token_ids']==r['output_token_ids']))
    return rows,dict(complete=complete,bands=bands,paired_position_transitions=transitions,
                     primary_identical_prompt_repeats=repeats,secondary_only=True)


def decide(metrics, infrastructure_failed=False, diagnostic_complete=True):
    if infrastructure_failed or not metrics['complete'] or not diagnostic_complete:
        return dict(final_decision='INFRASTRUCTURE_FAILURE', context_interpretation_allowed=False)
    base=metrics['levels']['0']['metrics']
    if any(base[k]['count']<39 for k in ('A_C','A_W','S')):
        return dict(final_decision='BASE_ASSAY_REGRESSION',context_interpretation_allowed=False)
    high=metrics['levels']['24']['metrics']
    triggers=dict(K24_gold=high['A_C']['count']<38,K24_wrong=high['A_W']['count']<38,
                  K24_paired=high['S']['count']<37,paired_lost_at_least_four=metrics['degradation']['24']['lost_count']>=4,
                  monotonic_collapse=metrics['monotonic_collapse'],off_target_over_two=metrics['total_off_target']>2)
    return dict(final_decision='CONTEXT_SENSITIVE_ASSAY' if any(triggers.values()) else 'ROBUST_CONTEXT_ASSAY',
                context_interpretation_allowed=True,triggers=triggers)
