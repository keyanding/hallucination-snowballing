"""Calibration/main gates, unrepaired pipeline accounting and diagnostics."""
from .design import parse,CONDITIONS,UP_CATS,DOWN_CATS
from experiments.v3_6_0.analyze import wilson


def measure(count,n,complete=True,ci=False):
    r=dict(count=count,denominator=n,rate=count/n if complete and n else None)
    if ci:
        r['wilson_95']=wilson(count,n) if complete and n else None
    return r


def parsed(cases,rows):
    by={c['case_id']:c for c in cases}
    assert len({(r['case_id'],r['condition'],r['reverse']) for r in rows})==len(rows)
    return [r|parse(r['raw_text'],by[r['case_id']],r['condition'].startswith('U-'),r['truncated']) for r in rows]


def component(cases,rows):
    p=parsed(cases,rows)
    by={(r['case_id'],r['condition']):r for r in p}
    complete=len(p)==len(cases)*4 and set(by)=={(c['case_id'],k) for c in cases for k in CONDITIONS}
    expected={'U-GOLD':'B','U-ALT':'Bp','P-GOLD':'C','P-ALT':'Cp'}
    correct={k:sum(r['condition']==k and r['category']==expected[k] for r in p) for k in CONDITIONS}
    tables={prefix:{a:{b:0 for b in cats} for a in cats} for prefix,cats in (('U',UP_CATS),('P',DOWN_CATS))}
    pair_counts={}
    for prefix in ('U','P'):
        pair_counts[prefix]=0
        for c in cases:
            ka,kb=(c['case_id'],prefix+'-GOLD'),(c['case_id'],prefix+'-ALT')
            if ka not in by or kb not in by:
                continue
            a,b=by[ka]['category'],by[kb]['category']
            tables[prefix][a][b]+=1
            pair_counts[prefix]+=a==expected[ka[1]] and b==expected[kb[1]]
    return p,dict(complete=complete,correct=correct,pairs=pair_counts,tables=tables,
                  permitted=sum(r['permitted'] for r in p),off_target=sum(r['category'] in ('OTHER_STATE','OTHER_OUTCOME','INVALID') for r in p),
                  categories={k:{cat:sum(r['condition']==k and r['category']==cat for r in p) for cat in (UP_CATS if k.startswith('U') else DOWN_CATS)} for k in CONDITIONS})


def calibration(cases,rows):
    p,m=component(cases,rows)
    counts=dict(A=m['correct']['U-GOLD'],B=m['correct']['U-ALT'],C=m['correct']['P-GOLD'],D=m['correct']['P-ALT'],E=m['pairs']['U'],F=m['pairs']['P'],G=m['permitted'])
    gates={k:measure(n,80 if k=='G' else 20,m['complete'])|dict(minimum=79 if k=='G' else 19,passed=m['complete'] and n>=(79 if k=='G' else 19)) for k,n in counts.items()}
    return p,m|dict(gates=gates,passed=all(v['passed'] for v in gates.values()))


def main_metrics(cases,up,prop,pipes,logs):
    p,m=component(cases,up+prop)
    pipeline=parsed(cases,pipes)
    by={(r['case_id'],r['condition']):r for r in p}
    pb={r['case_id']:r for r in pipeline}
    lb={r['case_id']:r for r in logs}
    assert len(pb)==len(pipes) and len(lb)==len(logs)
    complete=m['complete'] and set(lb)=={c['case_id'] for c in cases}
    strict=conditional=correct_up=0
    failures=[]
    for c in cases:
        cid=c['case_id']
        u=by.get((cid,'U-GOLD'))
        if not u:
            continue
        valid=u['category']!='INVALID'
        complete=complete and ((cid in pb)==valid)
        if cid in lb:
            assert lb[cid]['upstream_normalized']==u['normalized']
            assert lb[cid]['status']==('CALLED_UNREPAIRED' if valid else 'UPSTREAM_INVALID_SKIPPED')
        if cid in pb:
            assert pb[cid]['supplied_state']==u['normalized']
        uc=u['category']=='B'
        dc=cid in pb and pb[cid]['category']=='C'
        correct_up+=uc
        strict+=uc and dc
        conditional+=uc and dc
        if not (uc and dc):
            failures.append(dict(case_id=cid,upstream=u['category'],downstream=pb[cid]['category'] if cid in pb else 'NOT_CALLED',
                                 source='UPSTREAM_INVALID' if not valid else 'UPSTREAM_INCORRECT' if not uc else 'DOWNSTREAM_AFTER_CORRECT_UPSTREAM'))
    counts=[m['correct'][k] for k in CONDITIONS]+[m['pairs']['P'],strict]
    metrics={key:measure(n,40,complete,True) for key,n in zip(('A_U_G','A_U_A','A_P_G','A_P_A','S_P','E2E'),counts)}
    gates={f'G{i+1}':complete and n>=(38 if i==5 else 39) for i,n in enumerate(counts)}
    gates['G7']=complete and m['off_target']<=2
    return p+pipeline,m|dict(complete=complete,metrics=metrics,gates=gates,passed=all(gates.values()),
         conditional_downstream=measure(conditional,correct_up,complete),pipeline_calls=len(pipes),pipeline_skipped=sum(l['status']=='UPSTREAM_INVALID_SKIPPED' for l in logs),
         pipeline_failures=failures,pipeline_category_counts={cat:sum(r['category']==cat for r in pipeline) for cat in DOWN_CATS},
         G7_off_target=measure(m['off_target'],160,complete))


def integrated(cases,selected,rows):
    p=parsed(cases,rows)
    by={(r['case_id'],r['condition']):r for r in p}
    complete=set(by)=={(cid,k) for cid in selected for k in ('I-GOLD','I-ALT')} and len(rows)==40
    gold=sum(r['condition']=='I-GOLD' and r['category']=='C' for r in p)
    alt=sum(r['condition']=='I-ALT' and r['category']=='Cp' for r in p)
    pair=sum(by[cid,'I-GOLD']['category']=='C' and by[cid,'I-ALT']['category']=='Cp' for cid in selected if (cid,'I-GOLD') in by and (cid,'I-ALT') in by)
    return p,dict(evaluated=complete,I_G=measure(gold,20,complete),I_A=measure(alt,20,complete),paired=measure(pair,20,complete),ready=complete and min(gold,alt,pair)>=19)


def order_diagnostic(cases,selected,rows,upstream):
    p=parsed(cases,rows)
    b={(r['case_id'],r['condition']):r for r in parsed(cases,upstream)}
    pairs=[]
    for r in p:
        base=b.get((r['case_id'],r['condition']))
        expected='B' if r['condition']=='U-GOLD' else 'Bp'
        pairs.append(dict(case_id=r['case_id'],condition=r['condition'],before=base['category'] if base else None,after=r['category'],
                          unchanged_and_correct=base is not None and base['category']==r['category']==expected))
    complete=len(p)==20 and {(r['case_id'],r['condition']) for r in p}=={(cid,k) for cid in selected for k in ('U-GOLD','U-ALT')}
    count=sum(r['unchanged_and_correct'] for r in pairs)
    return p,dict(complete=complete,unchanged_correct=measure(count,20,complete),passed=complete and count>=19,pairs=pairs)


def decide(cal,main,integrated_result,order,infrastructure_failed=False):
    if infrastructure_failed or not cal['complete']:
        return 'INFRASTRUCTURE_FAILURE'
    if not cal['passed']:
        return 'STOP_TWO_HOP_CALIBRATION_INVALID'
    if not main['complete'] or not integrated_result['evaluated'] or not order['complete']:
        return 'INFRASTRUCTURE_FAILURE'
    return 'TWO_HOP_PROPAGATION_ASSAY_VALIDATED' if main['passed'] else 'TWO_HOP_PROPAGATION_ASSAY_INVALID'
