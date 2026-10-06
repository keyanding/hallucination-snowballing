"""Paired pilot estimands and bounded interpretation; no model calls."""
import json
import math
from collections import Counter
from pathlib import Path
from src.experiment_v3 import write_json
from src.common import read_jsonl, digest
from .build_cases import OUT, load, POLICY, BOUNDARY, verify
from .render_prompts import CONDITIONS
from .validate_cases import parse, classify


def fraction(n,d):return dict(count=n,denominator=d,rate=n/d if d else None)


def binomial_interval(k,n):
    def tail(p):return sum(math.comb(n,j)*p**j*(1-p)**(n-j) for j in range(k,n+1))
    def cdf(p):return sum(math.comb(n,j)*p**j*(1-p)**(n-j) for j in range(k+1))
    lo,hi=0.,1.
    for _ in range(80):
        mid=(lo+hi)/2
        if tail(mid)<.025:lo=mid
        else:hi=mid
    lower=0. if k==0 else (lo+hi)/2
    lo,hi=0.,1.
    for _ in range(80):
        mid=(lo+hi)/2
        if cdf(mid)>.025:lo=mid
        else:hi=mid
    return dict(forward=k,discordant=n,exact95=[lower,1. if k==n else (lo+hi)/2],
                two_sided_sign_p=min(1.,2*sum(math.comb(n,j) for j in range(min(k,n-k)+1))/2**n),
                interpretation='Descriptive conditional discordance interval; small sample, reused people, not evidence of an internal mechanism.')


def compute(cases,outputs,capability_pass):
    bycase={c['case_id']:c for c in cases}
    parsed=[]
    for r in outputs:
        p=parse(r['raw_text'],bycase[r['case_id']],r['truncated'])
        parsed.append(r|p|dict(outcome=classify(p,r['wrong_state'])))
    assert len({(r['case_id'],r['condition']) for r in parsed})==len(parsed)
    complete=len(parsed)==72
    categories=['PROPAGATE_WRONG','OVERRIDE_TO_GOLD','GOLD_FOLLOW','INDUCED_WRONG','OTHER_ANSWER','UNKNOWN','INVALID']
    cells={}
    for condition in CONDITIONS:
        subset=[r for r in parsed if r['condition']==condition]
        counts=Counter(r['outcome'] for r in subset)
        valid=[r for r in subset if r['parse_valid']]
        cells[condition]=dict(observed=len(subset),planned=12,counts={k:counts[k] for k in categories},
            all_case_rates={k:fraction(counts[k],12) if len(subset)==12 else dict(count=counts[k],denominator=12,rate=None) for k in categories},
            valid_parse_rates={k:fraction(sum(r['outcome']==k for r in valid),len(valid)) for k in categories},
            valid_parses=len(valid),invalid_subtypes=dict(Counter(r['invalid_subtype'] for r in subset if r['outcome']=='INVALID')))
    table={a:{b:0 for b in ('C','Cp','OTHER')} for a in ('C','Cp','OTHER')}
    pairs=[]
    for c in cases:
        group={r['condition']:r for r in parsed if r['case_id']==c['case_id']}
        if len(group)!=6:continue
        a,b=group['G-BACKGROUND'],group['G-CURRENT']
        x,y=a['identity'] or 'OTHER',b['identity'] or 'OTHER'
        table[x][y]+=1
        pairs.append(dict(case_id=c['case_id'],background=x,current=y,background_category=a['parse_category'],current_category=b['parse_category'],
            delta_OR=int(y=='C')-int(x=='C'),delta_PR=int(y=='Cp')-int(x=='Cp'),both_valid=a['parse_valid'] and b['parse_valid'],
            reverse_correct_to_wrong=group['C0']['identity']=='C' and group['C-WCURRENT']['identity']=='Cp'))
    forward=sum(p['both_valid'] and p['background']!='C' and p['current']=='C' for p in pairs)
    reverse=sum(p['both_valid'] and p['background']=='C' and p['current']!='C' for p in pairs)
    checks=dict(complete=complete,capability=capability_pass,
        C0=cells['C0']['counts']['GOLD_FOLLOW']>=10,S0=cells['S0']['counts']['PROPAGATE_WRONG']>=8,
        framing_format=all(cells[k]['counts']['INVALID']<=2 for k in ('G-CURRENT','G-BACKGROUND')))
    signal=all(checks.values()) and forward>=4 and reverse<=1
    recommendation='STOP_INVALID' if not all(checks.values()) else 'PILOT_SIGNAL_CONFIRM_SEPARATELY' if signal else 'STOP_UNINFORMATIVE'
    n=len(pairs);discordant=table['Cp']['C']+table['C']['Cp']
    primary=dict(delta_OR=fraction(sum(p['delta_OR'] for p in pairs),n),delta_PR=fraction(sum(p['delta_PR'] for p in pairs),n),
        valid_pair_delta_OR=fraction(sum(p['delta_OR'] for p in pairs if p['both_valid']),sum(p['both_valid'] for p in pairs)),
        valid_pair_delta_PR=fraction(sum(p['delta_PR'] for p in pairs if p['both_valid']),sum(p['both_valid'] for p in pairs)),
        transition_2x2={a:{b:table[a][b] for b in ('C','Cp')} for a in ('C','Cp')},transition_with_other=table,
        transitions_involving_other=sum(v for a,row in table.items() for b,v in row.items() if a=='OTHER' or b=='OTHER'),
        gold_aligned_forward=forward,gold_aligned_reverse=reverse,
        discordance_uncertainty=binomial_interval(table['Cp']['C'],discordant) if discordant>=4 else dict(forward=table['Cp']['C'],discordant=discordant,interval=None,reason='Fewer than four strict C/Cp discordances; counts only.'))
    gate=dict(recommendation=recommendation,checks=checks,framing_signal=signal,
        evidence_dominance=complete and all(cells[k]['counts']['OVERRIDE_TO_GOLD']>=8 for k in ('G-CURRENT','G-BACKGROUND')),
        wrong_state_dominance=complete and all(cells[k]['counts']['PROPAGATE_WRONG']>=8 for k in ('G-CURRENT','G-BACKGROUND')),
        manipulation_failed=not(checks['C0'] and checks['S0']),v3_5_2_executed=False,independent_confirmation_executed=False,
        identification_boundary=BOUNDARY)
    secondary=dict(correct_to_wrong_flips=fraction(sum(p['reverse_correct_to_wrong'] for p in pairs),n),
        induced_wrong_rate_difference=fraction(cells['C-WCURRENT']['counts']['INDUCED_WRONG']-cells['C0']['counts']['INDUCED_WRONG'],12) if complete else None)
    return parsed,dict(cells=cells,primary=primary,secondary=secondary,paired_cases=pairs,complete=complete),gate


def report():
    verify()
    cases=load('cases.json');plans=load('prompt_plan.json')
    outputs=read_jsonl(OUT/'outputs.jsonl') if (OUT/'outputs.jsonl').exists() else []
    capability=read_jsonl(OUT/'capability_checks.jsonl') if (OUT/'capability_checks.jsonl').exists() else []
    state=load('run_state.json')
    capability_pass=state.get('capability_pass',False)
    parsed,m,gate=compute(cases,outputs,capability_pass)
    for name in ('outputs.jsonl','capability_checks.jsonl'):
        if not (OUT/name).exists():(OUT/name).write_text('',encoding='utf-8')
    (OUT/'parsed_outcomes.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in parsed),encoding='utf-8',newline='\n')
    write_json(OUT/'metrics.json',m);write_json(OUT/'gate.json',gate)
    summary='| Condition | Cp | C | Other | Unknown | Invalid | Valid parses |\n|---|---|---|---|---|---|---|\n'
    for k,s in m['cells'].items():
        counts=s['counts'];wrong=counts['PROPAGATE_WRONG']+counts['INDUCED_WRONG'];gold=counts['OVERRIDE_TO_GOLD']+counts['GOLD_FOLLOW']
        summary+=f'| {k} | {wrong}/12 | {gold}/12 | {counts["OTHER_ANSWER"]}/12 | {counts["UNKNOWN"]}/12 | {counts["INVALID"]}/12 | {s["valid_parses"]}/12 |\n'
    intro='# v3.5.1 task-role framing pilot\n\n'+BOUNDARY+'\n\nExternally supplied erroneous states only; no spontaneous first-hop hallucination or natural snowballing estimate. Anonymous films prevent retrieval of a real film-director association. Explicit real-person city mappings are supplied. Independent fictional controls test context-use capability, not whether every real-city answer causally relied on context. Seven people recur across twelve distinct pairs.\n\n'
    intro+=f'Main calls: **{len(outputs)}/72**. Auxiliary calls: **{state.get("auxiliary_calls",len(capability))}**. Outcome: **{gate["recommendation"]}**.\n\n'
    intro+=summary+'\nAll primary denominators are12 when complete; rates are undefined for an early halt. Valid-parse secondary denominators are explicit in metrics.json. UNKNOWN and INVALID are never reassigned to propagation or override.\n\n'
    intro+='Primary paired contrast:\n\n```json\n'+json.dumps(m['primary'],indent=2)+'\n```\n'
    intro+='\nThe heading contrast includes possible perceived authority/freshness connotations. A null contrast says nothing general about logical evidence relevance. No automatic follow-up or v3.5.2.\n'
    (OUT/'README.md').write_text(intro,encoding='utf-8',newline='\n')
    inspection='# Case-level injected-state inspection\n\n'+BOUNDARY+'\n\nNo upstream model generated the supplied state. Each r2 question is identical across the six arms within its case.\n'
    for c in cases:
        inspection+=f'\n## {c["case_id"]}: Film {c["A"]}\n\nGold: {c["B"]} → {c["C"]}; donor: {c["Bp"]} → {c["Cp"]}.\n\n'
        inspection+='Question: `'+next(p['question'] for p in plans if p['case_id']==c['case_id'])+'`\n\n'
        inspection+='| Condition | Supplied intermediate | Role | Raw output | Outcome |\n|---|---|---|---|---|\n'
        for k in CONDITIONS:
            r=next((r for r in parsed if r['case_id']==c['case_id'] and r['condition']==k),None)
            if r:inspection+='| '+' | '.join([k,r['injected_state'],r['role'] or 'baseline',json.dumps(r['raw_text'],ensure_ascii=False).replace('|','\\|'),r['outcome']+(('/'+r['invalid_subtype']) if r['invalid_subtype'] else '')])+' |\n'
        pair=next((p for p in m['paired_cases'] if p['case_id']==c['case_id']),None)
        inspection+='\nPaired contrast: '+json.dumps(pair,ensure_ascii=False)+'.\n'
    inspection+='\n## Exact matched sample prompts\n'
    for k in ('G-CURRENT','G-BACKGROUND'):
        p=next(p for p in plans if p['case_id']==cases[0]['case_id'] and p['condition']==k)
        inspection+=f'\n### {k}\n\n```text\n{p["prompt"]}\n```\n'
    (OUT/'inspection.md').write_text(inspection,encoding='utf-8',newline='\n')
    cell=m['cells'];primary=m['primary']
    diagnosis='# Diagnosis\n\n'+BOUNDARY+'\n\n'
    answers=[
        f'State manipulation: S0 propagated {cell["S0"]["counts"]["PROPAGATE_WRONG"]}/12; C0 followed gold {cell["C0"]["counts"]["GOLD_FOLLOW"]}/12. Independent capability checks passed: {capability_pass}. Gates: {gate["checks"]}.',
        f'Identical correct evidence under different headings: paired ΔOR={primary["delta_OR"]}; ΔPR={primary["delta_PR"]}. Framing heuristic met: {gate["framing_signal"]}. Evidence dominance: {gate["evidence_dominance"]}; wrong-state dominance: {gate["wrong_state_dominance"]}.',
        'Literal prompt diffs in prompt_diff_audit.md change only the dossier heading. Fact text, source tag, statement location, blank-line spacing, downstream record order and injected state are held fixed. Heading length and perceived authority/freshness are not separately manipulated or isolated.',
        'Exact Cp→C cases: '+str([p['case_id'] for p in m['paired_cases'] if p['background']=='Cp' and p['current']=='C'])+'; C→Cp cases: '+str([p['case_id'] for p in m['paired_cases'] if p['background']=='C' and p['current']=='Cp'])+'. All transitions, including other outputs, appear in metrics.json.',
        f'Wrong supporting evidence: W-CURRENT PR={cell["W-CURRENT"]["counts"]["PROPAGATE_WRONG"]}/12; S0 PR={cell["S0"]["counts"]["PROPAGATE_WRONG"]}/12; G-CURRENT PR={cell["G-CURRENT"]["counts"]["PROPAGATE_WRONG"]}/12. This content-control contrast is distinct from the heading-only pair.',
        f'Reverse direction: C-WCURRENT induced wrong {cell["C-WCURRENT"]["counts"]["INDUCED_WRONG"]}/12; paired C0 gold→wrong flips {m["secondary"]["correct_to_wrong_flips"]}. Symmetry is not assumed.',
        'Every category and denominator is shown below; valid-parse-only rates are in metrics.json.\n\n'+summary,
        'These responses can establish behavioral sensitivity to supplied state, evidence and these role headings when validity gates pass. They do not identify internal attention, beliefs, or a specific computational mechanism.',
        'The intervention is an externally injected erroneous state with explicit source-backed downstream mappings. PR measures propagation under this prompt intervention; it is not spontaneous hallucination incidence or natural end-to-end snowballing.',
        ('One follow-up hypothesis: the same predeclared heading contrast replicates on an independently frozen case set with adequate state-adherence gates. Confirm separately after external design review; no confirmation is launched.' if gate['recommendation']=='PILOT_SIGNAL_CONFIRM_SEPARATELY' else 'STOP this label pilot. No qualifying task-role signal was obtained. Do not search new labels or orderings inside this experiment; any redesigned intervention needs external design review and a separate preregistration.')]
    diagnosis+='\n\n'.join(f'{i}. {answer}' for i,answer in enumerate(answers,1))
    diagnosis+=f'\n\nFinal recommendation: **{gate["recommendation"]}**. With12 cases, absence of discordance is not proof of equivalence, and the null cannot falsify logical relevance or authority effects generally.\n'
    (OUT/'diagnosis.md').write_text(diagnosis,encoding='utf-8',newline='\n')
    before=(OUT/'design_audit.pre_inference.md').read_text(encoding='utf-8')
    rows=[('Propagation',f'S0 {cell["S0"]["counts"]["PROPAGATE_WRONG"]}/12',gate['checks']['S0']),('Gold path',f'C0 {cell["C0"]["counts"]["GOLD_FOLLOW"]}/12',gate['checks']['C0']),('Heading isolation',f'12 literal-diff pairs; ΔOR {primary["delta_OR"]}',True),('Correctness controls',f'6 arms; {len(outputs)} calls',m['complete']),('Reverse influence',str(m['secondary']),m['complete']),('No answer list','0 enumerated lists or constrained main calls',True),('Fixed record order','12 record-block hashes, one per case',True),('Categories',str({k:s['counts']['INVALID'] for k,s in cell.items()}),True),('No cherry-picking',f'{len(outputs)}/72 fixed outputs; 7 people reused',m['complete']),('Bounded continuation',gate['recommendation'],True)]
    after='\n## Post-run audit\n\n| Intention | Observed evidence | Check achieved? |\n|---|---|---|\n'+'\n'.join('| '+a+' | '+b+' | '+str(c)+' |' for a,b,c in rows)+'\n'
    (OUT/'design_audit.md').write_text(before+after,encoding='utf-8',newline='\n')
    (OUT/'CHANGELOG.md').write_text('# v3.5.1 changes\n\n- New standalone task-role pilot; all earlier experimental files preserved.\n- External state injection replaces natural first-hop error elicitation.\n- Six frozen conditions; primary current/background pair changes only a heading.\n- Explicit city mappings, independent capability/format/replay checks, exact parsing and paired outcomes.\n- No adaptive cases, label variants, order extensions or automatic next experiment.\n- No deviations to frozen definitions or thresholds. Generated post-run audit appends to the separately frozen pre-inference audit.\n',encoding='utf-8',newline='\n')
    verify()
    required=['README.md','pre_registration.md','design_audit.md','cases.json','model_manifest.json','prompt_plan.json','prompt_diff_audit.md','capability_checks.jsonl','outputs.jsonl','parsed_outcomes.jsonl','metrics.json','inspection.md','diagnosis.md','gate.json','CHANGELOG.md']
    assert all((OUT/n).exists() for n in required)
    write_json(OUT/'verification.json',dict(required_files=required,output_hashes={n:digest(OUT/n) for n in required},frozen_inputs_and_prior_artifacts_unchanged=True,prior_artifacts=len(load('model_manifest.json')['prior_artifacts']),main_calls=len(outputs),auxiliary_calls=state.get('auxiliary_calls'),classification_checked=True))
    print(json.dumps(gate,indent=2),flush=True)


if __name__=='__main__':report()
