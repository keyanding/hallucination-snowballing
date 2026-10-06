"""Case-level estimands and frozen development-only interface selection."""
from collections import Counter
import random
import statistics
from .prepare_v3_4_4 import POLICY, CONDITIONS


def frac(n, d):
    return dict(count=n, denominator=d, rate=n/d if d else None)


def modal(values):
    counts=Counter(values)
    if not counts:
        return None
    top=counts.most_common()
    return top[0][0] if len(top)==1 or top[0][1]>top[1][1] else None


def gold_margin(row):
    scores={s['candidate']:s['mean_logprob_per_token'] for s in row['S']['scores']}
    return scores[row['gold']]-max(v for n,v in scores.items() if n!=row['gold'])


def position_shift(rows, field):
    shifts=[]
    for name in rows[0]['candidate_order']:
        scores=[next(s['mean_logprob_per_token'] for s in r['S']['scores'] if s['candidate']==name) for r in rows]
        first=next(i for i,r in enumerate(rows) if r[field][0]==name)
        shifts.append(dict(identity=name, first_minus_other_mean=scores[first]-statistics.mean(v for i,v in enumerate(scores) if i!=first)))
    return shifts


def cell_summary(rows):
    listed=sorted([r for r in rows if r['interface']=='L'],key=lambda r:r['rotation'])
    natural=next(r for r in rows if r['interface']=='N')
    rotated=sorted([r for r in rows if r['interface']=='R'],key=lambda r:r['rotation'])
    gold=natural['gold']
    out=dict(case_id=natural['case_id'],difficulty=natural['difficulty'],gold=gold)
    if listed:
        values=[r['C']['selected_candidate'] for r in listed]
        wrong=[v!=gold for v in values]
        classification='ALL_CORRECT' if not any(wrong) else 'ROBUST_SAME_WRONG_4_OF_4' if len(set(values))==1 else 'ORDER_SENSITIVE'
        out['L']=dict(identities=values, modal_identity=modal(values), modal_tie=modal(values) is None,
            classification=classification, all_correct=not any(wrong), robust_wrong=len(set(values))==1 and all(wrong),
            partial_wrong_three_of_four=any(v!=gold and values.count(v)==3 for v in set(values)),
            order_sensitive=len(set(values))>1, any_wrong=any(wrong), wrong_fraction=sum(wrong)/4,
            first_fraction=sum(v==r['candidate_order'][0] for v,r in zip(values,listed))/4,
            gold_margins=[gold_margin(r) for r in listed], first_score_shift=position_shift(listed,'candidate_order'))
    out['N']=dict(identity=natural['F']['identity'],category=natural['F']['category'],valid=natural['F']['strict_valid'],
                  wrong=natural['F']['strict_valid'] and natural['F']['identity']!=gold, gold_margin=gold_margin(natural))
    if rotated:
        assert len(rotated)==4
        valid=[r['F']['strict_valid'] for r in rotated]
        values=[r['F']['identity'] for r in rotated]
        observed=[v for v in values if v is not None]
        allvalid=all(valid)
        majority=modal(observed)
        stable3=allvalid and max(Counter(observed).values())>=3
        stable4=allvalid and len(set(observed))==1
        aggregate=majority if stable3 else None
        out['R']=dict(identities=values,categories=[r['F']['category'] for r in rotated],all_valid=allvalid,
            stable_three_of_four=stable3, stable_four_of_four=stable4,
            observed_order_sensitive=len(set(observed))>1,
            order_sensitive_complete=len(set(observed))>1 if allvalid else None,
            aggregate=aggregate,aggregate_status='RESOLVED' if aggregate else 'UNSTABLE_OR_UNRESOLVED',
            wrong_aggregate=aggregate is not None and aggregate!=gold,
            wrong_label='AGGREGATED_TRACEABLE_WRONG' if aggregate and aggregate!=gold else None,
            first_count=sum(r['F']['strict_valid'] and r['F']['identity']==r['record_order'][0] for r in rotated),
            wrong_count=sum(r['F']['strict_valid'] and r['F']['identity']!=gold for r in rotated),
            valid_count=sum(valid), n_matches_all_four=out['N']['valid'] and stable4 and observed[0]==out['N']['identity'],
            gold_margins=[gold_margin(r) for r in rotated],first_score_shift=position_shift(rotated,'record_order'))
    if listed:
        lm=out['L']['modal_identity']
        out['agreement_eligible']=lm is not None and out['N']['valid']
        out['N_L_agree']=out['agreement_eligible'] and lm==out['N']['identity']
        out['disagreement_direction']=None if not out['agreement_eligible'] or out['N_L_agree'] else (
            'L_GOLD_N_WRONG' if lm==gold else 'L_WRONG_N_GOLD' if out['N']['identity']==gold else 'BOTH_WRONG_DIFFERENT')
    return out


def summarize(cells):
    n=len(cells)
    result=dict(cells=n)
    result['N_coverage']=frac(sum(c['N']['valid'] for c in cells),n)
    result['N_wrong_all']=frac(sum(c['N']['wrong'] for c in cells),n)
    result['N_wrong_given_valid']=frac(sum(c['N']['wrong'] for c in cells),sum(c['N']['valid'] for c in cells))
    result['N_gold_all']=frac(sum(c['N']['valid'] and c['N']['identity']==c['gold'] for c in cells),n)
    result['N_categories']=dict(Counter(c['N']['category'] for c in cells))
    if all('L' in c for c in cells):
        result['L_first']=frac(round(sum(c['L']['first_fraction'] for c in cells)*4),n*4)
        result['L_wrong']=frac(round(sum(c['L']['wrong_fraction'] for c in cells)*4),n*4)
        for k in ('all_correct','robust_wrong','partial_wrong_three_of_four','order_sensitive','any_wrong'):
            result['L_'+k]=frac(sum(c['L'][k] for c in cells),n)
        result['L_identity_first_score_shift']=statistics.mean(s['first_minus_other_mean'] for c in cells for s in c['L']['first_score_shift'])
        result['N_L_agreement']=frac(sum(c['N_L_agree'] for c in cells),sum(c['agreement_eligible'] for c in cells))
        result['L_modal_ties']=sum(c['L']['modal_tie'] for c in cells)
        result['agreement_excluded_invalid_N']=sum(not c['N']['valid'] for c in cells)
        result['disagreement_directions']=dict(Counter(c['disagreement_direction'] for c in cells if c['disagreement_direction']))
    if all('R' in c for c in cells):
        for k in ('stable_three_of_four','stable_four_of_four','all_valid','observed_order_sensitive','n_matches_all_four','wrong_aggregate'):
            result['R_'+k]=frac(sum(c['R'][k] for c in cells),n)
        complete=[c for c in cells if c['R']['all_valid']]
        result['R_order_sensitive_complete']=frac(sum(c['R']['order_sensitive_complete'] for c in complete),len(complete))
        result['R_coverage']=frac(sum(c['R']['valid_count'] for c in cells),n*4)
        result['R_wrong_all']=frac(sum(c['R']['wrong_count'] for c in cells),n*4)
        result['R_wrong_given_valid']=frac(sum(c['R']['wrong_count'] for c in cells),sum(c['R']['valid_count'] for c in cells))
        result['R_aggregate_coverage']=result['R_stable_three_of_four']
        result['R_earliest']=frac(sum(c['R']['first_count'] for c in cells),sum(c['R']['valid_count'] for c in cells))
        result['R_categories']=dict(Counter(v for c in cells for v in c['R']['categories']))
        result['R_coverage_by_rotation']=[frac(sum(c['R']['categories'][i]=='IN_SET_VALID' for c in cells),n) for i in range(4)]
        result['R_identity_first_score_shift']=statistics.mean(s['first_minus_other_mean'] for c in cells for s in c['R']['first_score_shift'])
    return result


def bootstrap(cells):
    rng=random.Random(344)
    keys=[k for k,v in summarize(cells).items() if isinstance(v,dict) and 'rate' in v]
    samples={k:[] for k in keys}
    for _ in range(2000):
        stats=summarize(rng.choices(cells,k=len(cells)))
        for k in keys:
            v=stats[k]['rate']
            if v is not None:
                samples[k].append(v)
    return {k:dict(lower=sorted(v)[int(.025*(len(v)-1))],upper=sorted(v)[int(.975*(len(v)-1))],defined_replicates=len(v)) if v else None for k,v in samples.items()}


def natural_gate(stats, route):
    if 'R_earliest' not in stats:
        return dict(passed=False,reason='Record rotations not available')
    rate=lambda k:stats[k]['rate']
    checks=dict(coverage=rate('N_coverage' if route=='N' else 'R_aggregate_coverage')>=.90,
        record_three_of_four=rate('R_stable_three_of_four')>=.75,
        record_four_of_four=rate('R_stable_four_of_four')>=.50,
        no_earliest_record_flag=rate('R_earliest') is not None and rate('R_earliest')<.40,
        N_L_agreement=rate('N_L_agreement') is not None and rate('N_L_agreement')>=.85)
    return dict(passed=all(checks.values()),checks=checks,
        observed_wrong_yield=stats['N_wrong_all' if route=='N' else 'R_wrong_aggregate']['count'])


def analyze(rows, intervals=True):
    groups={}
    for r in rows:
        groups.setdefault((r['cohort'],r['case_id'],r['difficulty']),[]).append(r)
    cells=[dict(cohort=key[0],**cell_summary(values)) for key,values in groups.items()]
    cohorts={}
    for cohort in sorted({c['cohort'] for c in cells}):
        bydiff={}
        for difficulty in CONDITIONS:
            sub=[c for c in cells if c['cohort']==cohort and c['difficulty']==difficulty]
            if sub:
                stats=summarize(sub)
                if intervals:
                    stats['case_bootstrap_95']=bootstrap(sub)
                bydiff[difficulty]=stats
        cohorts[cohort]=bydiff
    disagreement=[]
    for r in rows:
        f=r['F']; s=r['S']; c=r.get('C')
        mean=s['top_candidate_by_mean_logprob']
        total=max(s['scores'],key=lambda v:v['sum_logprob'])['candidate']
        if (f['strict_valid'] and f['identity']!=mean) or (c and c['selected_candidate']!=mean) or total!=mean or not f['strict_valid']:
            disagreement.append(dict(plan_id=r['plan_id'],F=f['identity'],F_category=f['category'],C=c['selected_candidate'] if c else None,S_mean=mean,S_sum=total,
                raw_f=f['raw_text'],note='Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified.'))
    trajectories=[]
    for cid in sorted({c['case_id'] for c in cells if c['cohort']=='development'}):
        group={c['difficulty']:c for c in cells if c['case_id']==cid and c['cohort']=='development'}
        trajectories.append(dict(case_id=cid,L_sensitivity=[group[d]['L']['order_sensitive'] for d in CONDITIONS],
            L_first=[group[d]['L']['first_fraction'] for d in CONDITIONS],
            N_wrong=[group[d]['N']['wrong'] for d in CONDITIONS],N_valid=[group[d]['N']['valid'] for d in CONDITIONS],
            R_sensitivity=[group[d]['R']['observed_order_sensitive'] for d in CONDITIONS],
            L_median_margin=[statistics.median(group[d]['L']['gold_margins']) for d in CONDITIONS],
            N_margin=[group[d]['N']['gold_margin'] for d in CONDITIONS],R_median_margin=[statistics.median(group[d]['R']['gold_margins']) for d in CONDITIONS]))
    paired={}
    rng=random.Random(344)
    for field in ('L_sensitivity','L_first','N_wrong','R_sensitivity','L_median_margin','N_margin','R_median_margin'):
        diffs=[float(t[field][2])-float(t[field][0]) for t in trajectories]
        if diffs:
            boots=sorted(statistics.mean(rng.choices(diffs,k=len(diffs))) for _ in range(2000))
            paired[field]=dict(HARD_minus_EASY_mean=statistics.mean(diffs),case_bootstrap_95=[boots[49],boots[1949]],positive=sum(v>0 for v in diffs),zero=sum(v==0 for v in diffs),negative=sum(v<0 for v in diffs),denominator=len(diffs))
    return dict(cohorts=cohorts,cells=cells,channel_anomalies=disagreement,paired_trajectories=trajectories,paired_changes=paired)


def select_policy(metrics, rows):
    stats=metrics['cohorts']['development']
    gates={d:{route:natural_gate(s,route) for route in ('N','R')} for d,s in stats.items()}
    for route in ('N','R'):
        for difficulty in CONDITIONS:
            gate=gates[difficulty][route]
            if gate['passed']:
                return dict(route=route,difficulty=difficulty,gates=gates,development_gate=gate,
                    claim='natural single-trajectory first-hop selection' if route=='N' else 'order-aggregated state estimate',
                    confirmation_with_R=True,v3_5_executed=False)
    valid=all(r['C']['exact_allowed_candidate'] for r in rows if r['cohort']=='development' and r['interface']=='L')
    eligible=[d for d in CONDITIONS if valid and 1-stats[d]['L_order_sensitive']['rate']>=.75 and stats[d]['L_first']['rate']<.40]
    return dict(route='L' if eligible else None,difficulty=eligible[0] if eligible else None,gates=gates,
        claim='forced-choice candidate selection only' if eligible else 'No adequate measurement policy',
        confirmation_with_R=False,v3_5_executed=False)
