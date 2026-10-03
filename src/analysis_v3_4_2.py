"""Preregistered factorial metrics, selection, and case diagnostics."""
from .calibration_v3_4_1 import summarize as channel_summary
from .experiment_v3 import fraction
from .graph_v3_4_2 import GRID, easier, key

POLICY = dict(seed=342, near_boundary=0.75, development_error_band=[0.2, 0.5],
              development_min_boundary_count=3, development_median_margin_band=[-1.0, 1.5],
              heldout_error_band=[0.15, 0.5], heldout_min_boundary_count=4,
              minimum_FCA=0.8, minimum_LCA=0.8, maximum_selected_conditions=2,
              neighboring_easier='Immediate grid neighbor (depth-1, branches) or (depth, branches-1); lower ER OR higher GM, strictly.',
              selection_tie_break='Among all qualifiers, increasing depth+branches, then depth, then branches; keep first two.',
              position_bias='Flag if a position is selected >=50%, at least two of its selections are wrong, and wrong selections are >=40% among cases whose gold is elsewhere. Apply per condition and pooled development; pooled flag blocks all selection.',
              case_monotonic='All 17 neighboring comparisons have non-decreasing binary C error AND non-increasing gold margin. Labels also record any adjacent correct-to-wrong margin sign crossing.',
              case_display_order='Increasing depth, then branch count. First means first in this display order, not an assumed total difficulty order.',
              margin_compression='Any strictly smaller gold margin than an immediately easier neighbor; descriptive only.',
              branch_relation='Each competing path has the same length as gold, using one fixed non-query relation on every edge, as in spec section 9.',
              stop_handling='Structural/channel failure stops immediately; empirical flat/cliff/spike checks occur after the complete preregistered dev grid; no adaptive cases or levels.')


def margin(row):
    scores = {s['candidate']: s['mean_logprob_per_token'] for s in row['L']['scores']}
    return scores[row['gold']] - max(v for k, v in scores.items() if k != row['gold'])


def summarize(rows):
    result = channel_summary(rows)
    result['near_boundary'] = fraction(sum(abs(m) <= .75 for m in result['gold_vs_best_wrong_margins']), len(rows))
    result['ER'] = result.pop('TWER_C')
    result['GM'] = result.pop('median_gold_margin')
    result['NBF'] = result.pop('near_boundary')
    return result


def monotonicity(grid):
    result = {}
    for factor in ('depth', 'branches'):
        comparisons = []
        for d, b in GRID:
            previous = (d-1, b) if factor == 'depth' else (d, b-1)
            if previous not in GRID:
                continue
            low, high = grid[key(*previous)], grid[key(d,b)]
            comparisons.append(dict(easier=key(*previous), harder=key(d,b),
                ER_non_decreasing=high['ER']['rate'] >= low['ER']['rate'],
                GM_non_increasing=high['GM'] <= low['GM'],
                ER_change=high['ER']['rate']-low['ER']['rate'], GM_change=high['GM']-low['GM']))
        result[factor] = dict(ER=fraction(sum(x['ER_non_decreasing'] for x in comparisons), len(comparisons)),
            GM=fraction(sum(x['GM_non_increasing'] for x in comparisons), len(comparisons)),
            strictly_increasing_ER=sum(x['ER_change'] > 0 for x in comparisons),
            strictly_decreasing_GM=sum(x['GM_change'] < 0 for x in comparisons), comparisons=comparisons)
    return result


def select(grid, pooled_position_bias=False):
    details = {}
    for d, b in GRID:
        s = grid[key(d,b)]
        support = [key(*n) for n in easier(d,b)
                   if grid[key(*n)]['ER']['rate'] < s['ER']['rate'] or grid[key(*n)]['GM'] > s['GM']]
        checks = dict(error_band=.2 <= s['ER']['rate'] <= .5,
            boundary=s['NBF']['count'] >= 3, median_margin=-1 <= s['GM'] <= 1.5,
            FCA=s['FCA']['rate'] is not None and s['FCA']['rate'] >= .8,
            LCA=s['LCA']['rate'] is not None and s['LCA']['rate'] >= .8,
            no_position_bias=not (s['POSITION_BIAS'] or pooled_position_bias),
            unique_path=s.get('unique_path_audit', False), C_valid=s['C_valid']['rate']==1,
            local_trend=bool(support))
        details[key(d,b)] = dict(depth=d, branches=b, checks=checks,
            qualifies=all(checks.values()), local_support=support,
            failed_checks=[name for name, passed in checks.items() if not passed])
    qualifiers = sorted([v for v in details.values() if v['qualifies']], key=lambda v:(v['depth']+v['branches'],v['depth'],v['branches']))
    return dict(conditions=details, selected=[key(v['depth'],v['branches']) for v in qualifiers[:2]],
                qualifying_not_selected=[key(v['depth'],v['branches']) for v in qualifiers[2:]])


def case_diagnostics(rows):
    grid = {(r['depth'],r['branches']):r for r in rows}
    assert len(grid)==12
    comparisons = []
    for d,b in GRID:
        high = grid[d,b]
        for prev in easier(d,b):
            low = grid[prev]
            low_error = low['C']['selected_candidate'] != low['gold']
            high_error = high['C']['selected_candidate'] != high['gold']
            gm_low, gm_high = margin(low), margin(high)
            comparisons.append(dict(easier=key(*prev), harder=key(d,b), factor='depth' if prev[0]!=d else 'branches',
                error_non_decreasing=high_error>=low_error, margin_non_increasing=gm_high<=gm_low,
                margin_compression=gm_high<gm_low, choice_flip=low['C']['selected_candidate']!=high['C']['selected_candidate'],
                correct_to_wrong=not low_error and high_error,
                boundary_crossing=not low_error and high_error and gm_low>0 and gm_high<0,
                recovery=low_error and not high_error, margin_reversal=gm_high>gm_low))
    errors = sum(r['C']['selected_candidate']!=r['gold'] for r in rows)
    monotonic = all(x['error_non_decreasing'] and x['margin_non_increasing'] for x in comparisons)
    primary = ('CASE_ALWAYS_EASY' if errors==0 else 'CASE_ALWAYS_WRONG' if errors==12 else
               'CASE_MONOTONIC' if monotonic else 'CASE_NON_MONOTONIC')
    crossing = any(x['boundary_crossing'] for x in comparisons)
    labels = [primary] + (['CASE_BOUNDARY_CROSSING'] if crossing else [])
    return dict(labels=labels, wrong_count=errors, all_neighbor_comparisons_monotonic=monotonic,
                first_near_boundary=next((key(d,b) for d,b in GRID if abs(margin(grid[d,b]))<=.75), None),
                first_margin_compression=next((x for x in comparisons if x['margin_compression']), None),
                first_choice_flip=next((x for x in comparisons if x['choice_flip']), None),
                comparisons=comparisons)


def analyze(rows):
    dev = [r for r in rows if r['split']=='dev']
    grid = {}
    for d,b in GRID:
        subset = [r for r in dev if r['depth']==d and r['branches']==b]
        assert len(subset)==8
        grid[key(d,b)] = summarize(subset) | dict(depth=d, branches=b, unique_path_audit=True)
    selection = select(grid, summarize(dev)['POSITION_BIAS'])
    held = {}
    for condition in selection['selected']:
        subset = [r for r in rows if r['split']=='heldout' and key(r['depth'],r['branches'])==condition]
        s = summarize(subset)
        s['confirmation_checks'] = dict(count=s['count']==12,
            error_band=s['ER']['rate'] is not None and .15<=s['ER']['rate']<=.5,
            boundary=s['NBF']['count']>=4, FCA=s['FCA']['rate'] is not None and s['FCA']['rate']>=.8,
            LCA=s['LCA']['rate'] is not None and s['LCA']['rate']>=.8,
            no_position_bias=not s['POSITION_BIAS'], unique_path=True, C_valid=s['C_valid']['rate']==1)
        s['confirmed'] = all(s['confirmation_checks'].values())
        held[condition] = s
    return dict(development=grid, selection=selection, heldout=held, monotonicity=monotonicity(grid),
                case_consistency={cid:case_diagnostics([r for r in dev if r['case_id']==cid]) for cid in sorted({r['case_id'] for r in dev})},
                development_overall=summarize(dev), overall=summarize(rows))
