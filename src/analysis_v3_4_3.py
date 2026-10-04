"""Paired candidate-order diagnostics; no population inference or propagation."""
from collections import Counter
from statistics import mean, median

from .experiment_v3 import fraction
from .analysis_v3_4_2 import margin

CASE_IDS = ('dev-04','dev-07','dev-05','dev-01','dev-06','dev-08')
CONDITIONS = dict(EASY=(1,0),MID=(3,0),HARD=(4,2))
POLICY = dict(
    permutations='P1 original, P2 left-rotate one, P3 left-rotate two, P4 left-rotate three',
    repeated_unit='case x difficulty (18 sets), nested within six deliberately selected cases; never 72 independent observations',
    PFR='Spec-literal event over P1->P2, P2->P3, P3->P4 (no wrap): old position-1 identity leaves position 1 and new position-1 identity is selected. Denominator: all 3 adjacent comparisons per set.',
    strict_PFR='Additionally require old position-1 identity was selected before rotation, and selected identity changes. Report per all transitions and conditional on previous position-1 selection.',
    classification='Gold 4/4 > same wrong identity 4/4 > position1 >=3/4 with >=2 identities > mixed when both maximum identity and maximum position counts <=2 > unstable other',
    likelihood_aggregation='Compute Delta for each identity within each set; average four identity Deltas within set, then mean/median those set means. Also report identity-level median diagnostically.',
    near_boundary_nats_per_token=0.75,
    strong_position='Descriptive flag A: PSR1>=0.40, >=3 POSITION_1_LOCKED sets, mean Delta1>0, and >=6 order-sensitive sets.',
    strong_identity='Descriptive flag B: mean ISR>=0.875, >=3 IDENTITY_LOCKED sets, literal PFR<=0.25, and <3 POSITION_1_LOCKED sets.',
    difficulty_interaction='Descriptive flag C: EASY PSR1<=0.35 and MID or HARD PSR1 is >=0.15 higher; OR EASY mean Delta1<=0.10 and MID/HARD mean Delta1 is >=0.15 higher and positive.',
    neither='Descriptive flag D: mean ISR<=0.625, literal PFR<=0.35, all PSR within 0.15 of 0.25. Flags are not significance tests; A and C can coexist.',
    frontier_salvage='Per-case error proportion, median margin, near-boundary fraction across four orders; aggregate six cases equally. Heuristic only: mean error 20-50%, median of case median margins -1..1.5, mean near-boundary fraction>=0.375 (prior dev proportional cutoff). Not a replacement clean split.',
    route1='Diagnostic only: PSR1<=0.35, literal PFR<=0.35, strict conditional PFR<=0.25 (or no opportunities), and some frontier heuristic survives.',
    route2='Diagnostic only: choices change in >=3 sets with positive mean Delta1, all pooled PSR within 0.10 of 0.25, and some frontier heuristic survives. If not met, do not claim counterbalancing removed the effect.',
    next_step='Never automatically authorize v3.5 from these selected six cases. Any supported route still needs a new clean development/confirmation split and balanced order.',
    divergence_stop='After each completed 24-prompt difficulty block, stop if >=12 strict F outputs and FCA<0.80. Structural/channel mismatches stop immediately.',
    order_of_execution='EASY then MID then HARD; six cases in spec order; P1 through P4. All 72 calls are new; prior P1 outputs are comparison only.')


def classify(rows):
    choices=[r['C']['selected_candidate'] for r in rows]
    identities=Counter(choices)
    positions=Counter(r['C']['candidate_order'].index(r['C']['selected_candidate'])+1 for r in rows)
    gold=rows[0]['gold']
    if identities.get(gold)==4:
        return 'GOLD_STABLE'
    if max(identities.values())==4:
        return 'IDENTITY_LOCKED'
    if positions[1]>=3 and len(identities)>=2:
        return 'POSITION_1_LOCKED'
    if max(identities.values())<=2 and max(positions.values())<=2:
        return 'MIXED_POSITION_IDENTITY'
    return 'UNSTABLE_OTHER'


def set_summary(rows):
    rows=sorted(rows,key=lambda r:r['permutation'])
    assert len(rows)==4 and [r['permutation'] for r in rows]==[1,2,3,4]
    names=rows[0]['C']['candidate_order']
    assert all({r['C']['candidate_order'].index(name)+1 for r in rows}=={1,2,3,4} for name in names)
    choices=[r['C']['selected_candidate'] for r in rows]
    identity_counts=Counter(choices)
    positions=[r['C']['candidate_order'].index(r['C']['selected_candidate'])+1 for r in rows]
    transitions=[]
    for old,new in zip(rows,rows[1:]):
        old_first=old['C']['candidate_order'][0]
        new_first=new['C']['candidate_order'][0]
        moves=old_first!=new_first
        literal=moves and new['C']['selected_candidate']==new_first
        opportunity=moves and old['C']['selected_candidate']==old_first
        strict=opportunity and literal and old['C']['selected_candidate']!=new['C']['selected_candidate']
        transitions.append(dict(old_permutation=old['permutation'],new_permutation=new['permutation'],
            old_pos1=old_first,new_pos1=new_first,old_choice=old['C']['selected_candidate'],new_choice=new['C']['selected_candidate'],
            literal_event=literal,strict_opportunity=opportunity,strict_event=strict))
    effects={}
    for identity in names:
        scores={str(r['C']['candidate_order'].index(identity)+1):next(s['mean_logprob_per_token'] for s in r['L']['scores'] if s['candidate']==identity) for r in rows}
        deltas={p:value-mean(v for q,v in scores.items() if q!=p) for p,value in scores.items()}
        effects[identity]=dict(scores_by_position=scores,delta_by_position=deltas)
    margins=[margin(r) for r in rows]
    return dict(case_id=rows[0]['case_id'],difficulty=rows[0]['difficulty'],gold=rows[0]['gold'],
        classification=classify(rows),selected_identities=choices,selected_positions=positions,
        identity_counts=dict(identity_counts),ISR=max(identity_counts.values())/4,
        order_sensitive=len(identity_counts)>1,error_fraction=sum(c!=rows[0]['gold'] for c in choices)/4,
        gold_margins=margins,median_gold_margin=median(margins),mean_gold_margin=mean(margins),
        near_boundary_fraction=sum(abs(m)<=.75 for m in margins)/4,
        transitions=transitions,PFR=fraction(sum(t['literal_event'] for t in transitions),3),
        strict_PFR=fraction(sum(t['strict_event'] for t in transitions),3),
        strict_conditional_PFR=fraction(sum(t['strict_event'] for t in transitions),sum(t['strict_opportunity'] for t in transitions)),
        identity_position_effects=effects,
        set_mean_delta_by_position={str(p):mean(v['delta_by_position'][str(p)] for v in effects.values()) for p in range(1,5)})


def aggregate(rows,sets):
    n=len(rows)
    psr={str(p):fraction(sum(r['C']['candidate_order'].index(r['C']['selected_candidate'])+1==p for r in rows),n) for p in range(1,5)}
    gpa={}
    for p in range(1,5):
        subset=[r for r in rows if r['gold_position']==p]
        gpa[str(p)]=fraction(sum(r['C']['selected_candidate']==r['gold'] for r in subset),len(subset))
    transitions=[t for s in sets for t in s['transitions']]
    strict=[r for r in rows if r['F']['exact_candidate_only']]
    extract=[r for r in rows if r['F']['contains_exactly_one_candidate']]
    delta={str(p):dict(mean=mean(s['set_mean_delta_by_position'][str(p)] for s in sets),
        median=median(s['set_mean_delta_by_position'][str(p)] for s in sets),
        set_count=len(sets),
        identity_level_median=median(v['delta_by_position'][str(p)] for s in sets for v in s['identity_position_effects'].values())) for p in range(1,5)}
    return dict(prompt_count=n,set_count=len(sets),case_count=len({r['case_id'] for r in rows}),PSR=psr,GPA=gpa,
        PFR=fraction(sum(t['literal_event'] for t in transitions),len(transitions)),
        strict_PFR=fraction(sum(t['strict_event'] for t in transitions),len(transitions)),
        strict_conditional_PFR=fraction(sum(t['strict_event'] for t in transitions),sum(t['strict_opportunity'] for t in transitions)),
        mean_ISR=mean(s['ISR'] for s in sets),median_ISR=median(s['ISR'] for s in sets),
        classifications=dict(Counter(s['classification'] for s in sets)),order_sensitive_sets=sum(s['order_sensitive'] for s in sets),
        delta_by_position=delta,C_valid=fraction(sum(r['C']['exact_allowed_candidate'] for r in rows),n),
        error_rate=fraction(sum(r['C']['selected_candidate']!=r['gold'] for r in rows),n),
        FSC=fraction(len(strict),n),FCA=fraction(sum(r['F']['strict_candidate']==r['C']['selected_candidate'] for r in strict),len(strict)),
        EFCA=fraction(sum(r['F']['extractable_candidate']==r['C']['selected_candidate'] for r in extract),len(extract)),
        LCA=fraction(sum(r['L']['top_candidate_by_mean_logprob']==r['C']['selected_candidate'] for r in rows),n),
        truncated=sum(r['F']['truncated'] for r in rows),out_of_set=sum(bool(r['F']['out_of_set_name']) for r in rows))


def analyze(rows):
    assert len(rows)==72
    sets={f'{cid}/{difficulty}':set_summary([r for r in rows if r['case_id']==cid and r['difficulty']==difficulty]) for cid in CASE_IDS for difficulty in CONDITIONS}
    overall=aggregate(rows,list(sets.values()))
    by_difficulty={difficulty:aggregate([r for r in rows if r['difficulty']==difficulty],[s for s in sets.values() if s['difficulty']==difficulty]) for difficulty in CONDITIONS}
    salvage={}
    for difficulty in ('MID','HARD'):
        summaries=[sets[f'{cid}/{difficulty}'] for cid in CASE_IDS]
        er=mean(s['error_fraction'] for s in summaries)
        gm=median(s['median_gold_margin'] for s in summaries)
        nbf=mean(s['near_boundary_fraction'] for s in summaries)
        salvage[difficulty]=dict(condition='D3B0' if difficulty=='MID' else 'D4B2',case_count=6,
            per_case=[{k:s[k] for k in ('case_id','error_fraction','median_gold_margin','mean_gold_margin','near_boundary_fraction','ISR','classification')} for s in summaries],
            equal_case_mean_error=er,median_of_case_median_margins=gm,equal_case_mean_near_boundary=nbf,
            PSR=by_difficulty[difficulty]['PSR'],mean_ISR=by_difficulty[difficulty]['mean_ISR'],
            heuristic_frontier_like=.2<=er<=.5 and -1<=gm<=1.5 and nbf>=.375,
            status='Diagnostic on selected cases, not a clean development/held-out confirmation')
    counts=overall['classifications']
    pfr=overall['PFR']['rate']
    flags=dict(A_strong_position=overall['PSR']['1']['rate']>=.4 and counts.get('POSITION_1_LOCKED',0)>=3 and overall['delta_by_position']['1']['mean']>0 and overall['order_sensitive_sets']>=6,
        B_strong_identity=overall['mean_ISR']>=.875 and counts.get('IDENTITY_LOCKED',0)>=3 and pfr<=.25 and counts.get('POSITION_1_LOCKED',0)<3,
        C_difficulty_dependent_position=any((by_difficulty['EASY']['PSR']['1']['rate']<=.35 and by_difficulty[d]['PSR']['1']['rate']>=by_difficulty['EASY']['PSR']['1']['rate']+.15)
            or (by_difficulty['EASY']['delta_by_position']['1']['mean']<=.10 and by_difficulty[d]['delta_by_position']['1']['mean']>=by_difficulty['EASY']['delta_by_position']['1']['mean']+.15 and by_difficulty[d]['delta_by_position']['1']['mean']>0) for d in ('MID','HARD')),
        D_neither=overall['mean_ISR']<=.625 and pfr<=.35 and all(abs(v['rate']-.25)<=.15 for v in overall['PSR'].values()))
    survives=any(s['heuristic_frontier_like'] for s in salvage.values())
    conditional=overall['strict_conditional_PFR']['rate']
    routes=dict(route1=overall['PSR']['1']['rate']<=.35 and pfr<=.35 and (conditional is None or conditional<=.25) and survives,
        route2=overall['order_sensitive_sets']>=3 and overall['delta_by_position']['1']['mean']>0 and all(abs(v['rate']-.25)<=.1 for v in overall['PSR'].values()) and survives)
    return dict(overall=overall,by_difficulty=by_difficulty,sets=sets,frontier_salvage=salvage,
                descriptive_outcome_flags=flags,diagnostic_routes=routes)
