"""Fixed-cohort estimands, explicit missingness and conservative paired intervals."""
import math
from collections import Counter,defaultdict
from .design import first_parse,route,down_parse

N=120
Z=1.959963984540054


def proportion(k,n,complete=True):
    if n==0 or not complete:return dict(count=k,denominator=n,rate=None,wilson95=None)
    p=k/n;d=1+Z*Z/n;center=(p+Z*Z/(2*n))/d;half=Z*math.sqrt(p*(1-p)/n+Z*Z/(4*n*n))/d
    return dict(count=k,denominator=n,rate=p,wilson95=[max(0.,center-half),min(1.,center+half)])


def cp(k,n,alpha=.025):
    if n==0:return None
    def solve(j,target):
        lo,hi=0.,1.
        for _ in range(80):
            p=(lo+hi)/2
            cdf=sum(math.comb(n,x)*p**x*(1-p)**(n-x) for x in range(j+1))
            if cdf>target:lo=p
            else:hi=p
        return (lo+hi)/2
    return [0. if k==0 else solve(k-1,1-alpha/2),1. if k==n else solve(k,alpha/2)]


def paired(values):
    counts=Counter(f'{a}{g}' for a,g in values);n=len(values)
    table={k:counts[k] for k in ('00','01','10','11')}
    if not n:return dict(n_pairs=0,table=table,RD=None,paired95=None)
    a,b=cp(counts['10'],n),cp(counts['01'],n)
    return dict(n_pairs=n,table=table,RD=(counts['10']-counts['01'])/n,
                paired95=[max(-1,a[0]-b[1]),min(1,a[1]-b[0])],interval='Bonferroni difference of97.5% CP discordant-cell intervals; tails0.0125')


def indexed(rows,field='case_id'):
    result={r[field]:r for r in rows};assert len(result)==len(rows),'Duplicate call'
    return result


def down(row,module):
    if row is None:return dict(category='MISSING',normalized=None,truncated=False)
    return down_parse(row['raw_text'],module['legacy'],False,row['truncated'])|dict(truncated=row['truncated'])


def diagnostic(cases,first,rows,ids):
    by=indexed(rows);pairs=[];transitions=Counter();cby={c['case_id']:c for c in cases}
    assert set(by)<=set(ids)
    for cid in ids:
        a=first_parse(first.get(cid),cby[cid]);b=first_parse(by.get(cid),cby[cid]);both=a['strict_valid'] and b['strict_valid']
        same=both and a['identity']==b['identity'];transitions[a['category']+'->'+b['category']]+=1
        pairs.append(dict(case_id=cid,primary=a,diagnostic=b,comparable=both,same=same,changed=both and not same,
            gold_to_wrong=a['category']=='GOLD' and b['category']=='WRONG',wrong_to_gold=a['category']=='WRONG' and b['category']=='GOLD',
            wrong_to_different_wrong=a['category']=='WRONG' and b['category']=='WRONG' and not same,
            same_wrong_identity=a['category']=='WRONG' and same))
    counts={k:sum(p[k] for p in pairs) for k in ('comparable','same','changed','gold_to_wrong','wrong_to_gold','wrong_to_different_wrong','same_wrong_identity')}
    wrong_n=sum(p['primary']['category']=='WRONG' for p in pairs)
    return dict(calls=len(rows),planned=24,pairs=pairs,counts=counts,transitions=dict(transitions),
        fixed_proportions={k:proportion(v,24,len(rows)==24) for k,v in counts.items()},
        changed_fixed=proportion(counts['changed'],24,len(rows)==24),changed_comparable=proportion(counts['changed'],counts['comparable']),
        comparable_coverage=proportion(counts['comparable'],24),same_wrong_persistence=proportion(counts['same_wrong_identity'],wrong_n),
        no_threshold_or_qualification_flag=True)


def analyze(cases,identity,modules,raw,schedule,technical='NONE',attempted=None):
    assert len(cases)==N
    first=indexed(raw['first_hop']);natural=indexed(raw['natural_downstream']);controlled=indexed(raw['controlled'],'call_id')
    allowed={c['case_id'] for c in cases};assert set(first)<=allowed and set(natural)<=allowed
    outcomes=[];fc=Counter();nw=Counter();ng=Counter();allpairs=[];wrongpairs=[];control_counts={'G':Counter(),'A':Counter()}
    correct_pairs=0;nat_control=[];bundles=defaultdict(lambda:Counter());identities=Counter();gold_ids=set();effective=[];route_orders=defaultdict(Counter);control_truncated=Counter()
    for c in cases:
        cid=c['case_id'];f=first_parse(first.get(cid),c);fc[f['category']]+=1
        module,_,log=route(c,first.get(cid),identity,modules);d=down(natural.get(cid),module)
        assert cid not in natural or f['strict_valid'],'Invalid first hop cannot enter natural denominator'
        cs={arm:down(controlled.get(cid+'/CONTROL_'+arm),module) for arm in ('G','A')}
        for arm in cs:
            control_counts[arm][cs[arm]['category']]+=1
            control_truncated[arm]+=cs[arm]['truncated']
        complete_pair=all(cs[a]['category']!='MISSING' for a in cs)
        if complete_pair:
            value=(int(cs['A']['category']=='Cp'),int(cs['G']['category']=='Cp'));allpairs.append(value)
            correct_pairs+=cs['G']['category']=='C' and cs['A']['category']=='Cp'
            if f['category']=='WRONG':wrongpairs.append(value)
        other_detail='TRUNCATED' if d['truncated'] else d['category']
        result='SKIPPED_'+f['category']
        if f['category']=='WRONG':
            result={'Cp':'PROPAGATION','C':'OVERRIDE','MISSING':'MISSING'}.get(d['category'],'OTHER');nw[result]+=1
            identities[f['identity']]+=1
            if result=='OTHER':nw['OTHER_'+other_detail]+=1
            if complete_pair and d['category']!='MISSING':effective.append((f['identity'],c['bundle_id']))
            if d['category']!='MISSING' and cs['A']['category']!='MISSING':
                nat_control.append(dict(case_id=cid,natural_propagation=result=='PROPAGATION',controlled_alternate=cs['A']['category']=='Cp',
                    same_normalized=d['normalized']==cs['A']['normalized'],same_raw_hash=natural[cid]['raw_sha256']==controlled[cid+'/CONTROL_A']['raw_sha256']))
        elif f['category']=='GOLD':
            gold_ids.add(f['identity']);result={'C':'GOLD_RETAINED','Cp':'ALTERNATE_OUTCOME','MISSING':'MISSING'}.get(d['category'],'OTHER');ng[result]+=1
            if result=='OTHER':ng['OTHER_'+other_detail]+=1
        route_orders[f['category']]['gold_first' if module['legacy']['down_order'][0]=='a' else 'gold_second']+=1
        bundle=bundles[c['bundle_id']];bundle['cases']+=1;bundle['wrong']+=f['category']=='WRONG';bundle['propagation']+=result=='PROPAGATION'
        outcomes.append(dict(case_id=cid,bundle_id=c['bundle_id'],first_status=f['category'],actual_identity=f['identity'],gold=c['gold'],
            state=log['supplied_state'],module_id=module['module_id'],alternate=module['alternate'],natural_outcome=result,natural_parser=d['category'],
            natural_other_detail=other_detail if result=='OTHER' else None,control_G=cs['G']['category'],control_A=cs['A']['category'],
            diagnostic_selected=cid in schedule['diagnostic_ids'],first_missing=cid not in first,natural_missing=f['strict_valid'] and cid not in natural,
            controlled_pair_missing=not complete_pair))
    V=fc['GOLD']+fc['WRONG'];W=fc['WRONG'];G=fc['GOLD'];P=nw['PROPAGATION'];u=fc['MISSING']+nw['MISSING']
    expected=len(first)==120 and len(natural)==V and len(controlled)==240 and len(raw['order_diagnostic'])==24
    complete=expected and technical=='NONE'
    if not expected and technical=='NONE':technical='INFRASTRUCTURE_FAILURE'
    n_eff_nat=W-nw['MISSING'];n_eff_pair=len(wrongpairs)
    diversity=dict(all_wrong_identities=len(identities),all_wrong_bundles=len({o['bundle_id'] for o in outcomes if o['first_status']=='WRONG'}),
        jointly_complete_wrong_identities=len({x[0] for x in effective}),jointly_complete_wrong_bundles=len({x[1] for x in effective}))
    info=('NO_ESTIMABLE_CONDITIONAL_TRAJECTORY' if min(n_eff_nat,n_eff_pair)==0 else 'LOW_INFORMATION_CONDITIONAL_ESTIMATE' if min(n_eff_nat,n_eff_pair)<20 else
          'MINIMUM_DESCRIPTIVE_INFORMATION_MET' if diversity['jointly_complete_wrong_identities']>=5 and diversity['jointly_complete_wrong_bundles']>=10 else 'CONCENTRATED_ERROR_SAMPLE')
    capability_checks=dict(C1=control_counts['G']['C']>=114,C2=control_counts['A']['Cp']>=114,C3=correct_pairs>=114,
        C4_G=control_counts['G']['C']+control_counts['G']['Cp']>=118,C4_A=control_counts['A']['C']+control_counts['A']['Cp']>=118)
    capability='NOT_FULLY_EVALUATED' if len(allpairs)!=120 else 'CURRENT_COHORT_CAPABILITY_SUPPORTED' if all(capability_checks.values()) else 'CURRENT_COHORT_CAPABILITY_LIMITED'
    proportions=dict(natural_wrong_yield=proportion(W,120,len(first)==120),wrong_given_valid=proportion(W,V,len(first)==120),valid_coverage=proportion(V,120,len(first)==120),
        conditional_propagation=proportion(P,W,nw['MISSING']==0),conditional_override=proportion(nw['OVERRIDE'],W,nw['MISSING']==0),
        conditional_other=proportion(nw['OTHER'],W,nw['MISSING']==0),UCR=proportion(P,120,complete),strict_end_to_end_success=proportion(ng['GOLD_RETAINED'],120,complete),
        final_gold_rate=proportion(ng['GOLD_RETAINED']+nw['OVERRIDE'],120,complete),gold_to_alternate=proportion(ng['ALTERNATE_OUTCOME'],G,ng['MISSING']==0),
        legal_forwarding_rate=proportion(len(natural),V),complete_trajectory_coverage=proportion(sum(not o['first_missing'] and not o['natural_missing'] for o in outcomes),120),
        completed_wrong_propagation=proportion(P,n_eff_nat))
    first_metrics={k:proportion(fc[k],120,len(first)==120) for k in ('GOLD','WRONG','TRUNCATED','AMBIGUOUS','OUT_OF_SET','NONCOMPLIANT','MISSING')}
    natural_wrong_metrics={k:proportion(nw[k],W,nw['MISSING']==0) for k in ('PROPAGATION','OVERRIDE','OTHER','MISSING')}
    natural_gold_metrics={k:proportion(ng[k],G,ng['MISSING']==0) for k in ('GOLD_RETAINED','ALTERNATE_OUTCOME','OTHER','MISSING')}
    for k in ('OTHER_OUTCOME','UNKNOWN','INVALID','TRUNCATED'):
        natural_wrong_metrics[k]=proportion(nw['OTHER_'+k],W,nw['MISSING']==0)
        natural_gold_metrics[k]=proportion(ng['OTHER_'+k],G,ng['MISSING']==0)
    pairs=dict(all_controlled=paired(allpairs),natural_wrong_subset=paired(wrongpairs),natural_wrong_total=W,
        missing_all=120-len(allpairs),missing_wrong=W-len(wrongpairs),natural_vs_controlled=nat_control,
        natural_vs_controlled_table=dict(Counter(f"{int(x['natural_propagation'])}{int(x['controlled_alternate'])}" for x in nat_control)))
    return dict(technical_status=technical,collection_status='PROSPECTIVE_COLLECTION_COMPLETE' if complete else 'INCOMPLETE',
        N_planned=120,N_attempted=len(first) if attempted is None else attempted,N_observed=len(first),V=V,G=G,W=W,stage_counts={s:len(r) for s,r in raw.items()},
        first_hop=first_metrics,natural_wrong_counts=dict(nw),natural_gold_counts=dict(ng),natural_wrong_rates=natural_wrong_metrics,natural_gold_rates=natural_gold_metrics,
        proportions=proportions,cascade_missing_bounds=dict(observed_P=P,uncertain_cases=u,denominator=120,lower=P/120,upper=(P+u)/120,final=complete),
        capability=dict(status=capability,checks=capability_checks,counts={a:dict(c) for a,c in control_counts.items()},truncation_rates={a:proportion(control_truncated[a],120,control_counts[a]['MISSING']==0) for a in ('G','A')},category_rates={a:{k:proportion(c[k],120,c['MISSING']==0) for k in ('C','Cp','OTHER_OUTCOME','UNKNOWN','INVALID','MISSING')} for a,c in control_counts.items()},paired_both_correct=proportion(correct_pairs,120,len(allpairs)==120),
            G_adherence=proportion(control_counts['G']['C'],120,control_counts['G']['MISSING']==0),A_adherence=proportion(control_counts['A']['Cp'],120,control_counts['A']['MISSING']==0),
            G_permitted=proportion(control_counts['G']['C']+control_counts['G']['Cp'],120,control_counts['G']['MISSING']==0),A_permitted=proportion(control_counts['A']['C']+control_counts['A']['Cp'],120,control_counts['A']['MISSING']==0)),
        information=dict(status=info,n_eff_natural=n_eff_nat,n_eff_paired_wrong=n_eff_pair,W=W,**diversity),
        concentration=dict(distinct_gold_identities=len(gold_ids),wrong_identity_counts=dict(identities),maximum_wrong_identity_share=proportion(max(identities.values(),default=0),W),
            bundles={k:dict(v) for k,v in bundles.items()}),routed_order_counts={k:dict(v) for k,v in route_orders.items()},
        diagnostic=diagnostic(cases,first,raw['order_diagnostic'],schedule['diagnostic_ids']),paired=pairs,case_outcomes=outcomes)
