"""Reports without pooling upstream and downstream outcomes."""
import json
from .prepare import OUT,load,write,text,verify,digest
from .analyze import calibration,main_metrics,integrated,order_diagnostic,decide
from .run import FILES


def report():
    verify()
    raw={k:[json.loads(s) for s in (OUT/(k+'_outputs.jsonl')).read_text(encoding='utf-8').splitlines()] for k in FILES}
    logs=[json.loads(s) for s in (OUT/'pipeline_log.jsonl').read_text(encoding='utf-8').splitlines()]
    plan=load('prompt_plan.json')
    for key in FILES:
        if key=='pipeline_generated':
            continue
        assert len(raw[key])<=len(plan[key])
        for p,r in zip(plan[key],raw[key]):
            assert all(r[k]==v for k,v in p.items())
    cal_cases,cases=load('calibration_cases.json'),load('main_cases.json')
    cp,cal=calibration(cal_cases,raw['calibration'])
    mp,main=main_metrics(cases,raw['main_upstream'],raw['main_propagation'],raw['pipeline_generated'],logs)
    subs=load('subsets.json')
    ip,im=integrated(cases,subs['integrated'],raw['integrated'])
    op,om=order_diagnostic(cases,subs['order_diagnostic'],raw['order_diagnostic'],raw['main_upstream'])
    final=decide(cal,main,im,om,(OUT/'failure.json').exists())
    if cal['complete'] and not cal['passed']:
        assert all(not raw[k] for k in FILES if k!='calibration') and not logs
    gate=dict(final_decision=final,calibration_pass=cal['passed'],main_evaluated=main['complete'],
              main_pass=main['passed'] if main['complete'] else None,INTEGRATED_TWO_HOP_READY=im['ready'],integrated_evaluated=im['evaluated'],
              order_diagnostic_evaluated=om['complete'],order_diagnostic_pass=om['passed'] if om['complete'] else None,
              counts={k:len(v) for k,v in raw.items()},pipeline_skipped=main['pipeline_skipped'])
    write('metrics.json',dict(calibration=cal,main=main,order_diagnostic=om))
    write('integrated_metrics.json',im)
    write('gate.json',gate)
    text('parsed_outcomes.jsonl',''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in cp+mp+ip+op))
    ctable=['| Calibration gate | Count | Minimum | Pass |','|---|---|---|---|']
    for key,v in cal['gates'].items():
        ctable.append(f"| {key} | {v['count']}/{v['denominator']} | {v['minimum']} | {v['passed']} |")
    mtable=['| Main metric | Count | Wilson 95% | Gate passed |','|---|---|---|---|']
    for i,(key,v) in enumerate(main['metrics'].items(),1):
        ci=v['wilson_95']
        interval=f'[{ci[0]:.1%}, {ci[1]:.1%}]' if ci else 'not evaluated'
        mtable.append(f"| {key} | {v['count']}/{v['denominator']} | {interval} | {main['gates']['G'+str(i)] if main['complete'] else 'not evaluated'} |")
    conclusion={
        'INFRASTRUCTURE_FAILURE':'Execution/structural validity failed; no assay interpretation.',
        'STOP_TWO_HOP_CALIBRATION_INVALID':'Calibration failed; main and all secondary calls were not run. No main propagation conclusion is licensed.',
        'TWO_HOP_PROPAGATION_ASSAY_INVALID':'The modular assay failed its fixed main gates. Diagnose upstream, downstream or interface failures before proceeding.',
        'TWO_HOP_PROPAGATION_ASSAY_VALIDATED':'In this validated synthetic task, the model computes upstream states reliably and externally replacing the recorded intermediate state changes the downstream output in the predicted direction.'}[final]
    summary=['# v3.6.3 two-hop propagation assay','', '**'+final+'**','',
             'Calls: '+', '.join(f'{k}={len(v)}' for k,v in raw.items())+f"; total={sum(map(len,raw.values()))}. Pipeline skips={main['pipeline_skipped']}.",'',*ctable,'']
    if main['complete']:
        cond=main['conditional_downstream']
        summary+=['## Main','',*mtable,'',f"G7 OTHER+INVALID: {main['G7_off_target']['count']}/160; pass={main['gates']['G7']}.",
                  f"Downstream C conditional on correct U-GOLD: {cond['count']}/{cond['denominator']}. Strict E2E includes every base case and any upstream-invalid skips.",'',
                  f"INTEGRATED_TWO_HOP_READY={im['ready']}: I-GOLD {im['I_G']['count']}/20, I-ALT {im['I_A']['count']}/20, paired {im['paired']['count']}/20.",
                  f"Order diagnostic: {om['unchanged_correct']['count']}/20 unchanged and correct; threshold19/20."]
        if om['unchanged_correct']['count']<20:
            summary+=['**Order limitation: at least one output was not both unchanged and correct. This diagnostic does not change the main gates.**']
    else:
        summary+=['Main rates/intervals are null because main was not evaluated. Readiness=false with evaluated=false is not a failed integrated test.']
    summary+=['','## Interpretation','',conclusion,
              'Integrated final-answer success does not establish internal use of an intermediate state. No spontaneous hallucination, natural snowballing, SHAR/HalluSE or real-world generalization claim. No subsequent phase was run.','',
              'See diagnosis.md, inspection.md, pre_registration.md and gate.json. Rebuild reporting with `python -m experiments.v3_6_3.report`.']
    text('README.md','\n'.join(summary).rstrip()+'\n')
    diagnosis=['# Diagnosis','', '**'+final+'**','',conclusion,'','## Calibration','',*ctable,'','## Main','']
    if main['complete']:
        diagnosis += mtable+['',f"Condition categories: {main['categories']}.",f"Pipeline outcome categories: {main['pipeline_category_counts']}.",
                            f"Strict pipeline failures: {main['pipeline_failures']}.",'',
                            '## Paired upstream categories','',json.dumps(main['tables']['U'],indent=2),'',
                            '## Paired propagation categories','',json.dumps(main['tables']['P'],indent=2),'',
                            '## Secondary diagnostics','',json.dumps(im,indent=2),json.dumps(om,indent=2)]
    else:
        diagnosis+=['Not run/evaluated. No failed calibration case was replaced or repaired.']
    diagnosis+=['','## Boundary','',
                'P-GOLD/P-ALT is the primary causal contrast. PIPELINE-GENERATED uses actual normalized U-GOLD, including wrong or well-formed unmapped states; invalid upstream outputs are skipped without replacement. Strict E2E requires both upstream B and downstream C, so downstream chance recovery cannot hide upstream failure.',
                'The new recorded-result prompt shell follows the spec and differs from the previous Current state template. Across-version differences cannot isolate the upstream layer alone; component calibration controls this version.',
                'Integrated readiness is separate and does not prove intermediate representation/use. Optional order results do not rescue or invalidate G1–G7. No next-phase experiment was run.']
    text('diagnosis.md','\n'.join(diagnosis).rstrip()+'\n')
    inspection=['# Exact questions, prompts and outputs','','No hidden first-hop repair: every generated-pipeline entry links to the actual U-GOLD raw/normalized state.','']
    for r in cp+mp+ip+op:
        query=r['prompt'].split('\n\n')[-1]
        inspection += [f"## {r['case_id']} / {r['condition']} / reverse={r['reverse']}",'',
                       f"Question/instruction: {query}",
                       f"Current entity: {r['current_entity']}; supplied intermediate: {r['supplied_state']}; expected: {r['expected']}.",
                       f"Category: {r['category']}; normalized: `{r['normalized']}`; truncated={r['truncated']}.",
                       f"Prompt SHA256: `{r['text_sha256']}`; rendered SHA256: `{r['rendered_sha256']}`."]
        if 'upstream_source' in r:
            inspection += ['Upstream source:','```json',json.dumps(r['upstream_source'],ensure_ascii=False,indent=2),'```']
        inspection += ['','```text',r['prompt'],'```','','Raw output:','```json',json.dumps(r['raw_text'],ensure_ascii=False),'```','']
    for r in logs:
        if r['status']=='UPSTREAM_INVALID_SKIPPED':
            inspection+=['## Skipped pipeline '+r['case_id'],'','```json',json.dumps(r,ensure_ascii=False,indent=2),'```','']
    text('inspection.md','\n'.join(inspection).rstrip()+'\n')
    pre=(OUT/'design_audit.pre_inference.md').read_bytes()
    post='\n## Post-inference audit\n\n'+'\n'.join(ctable)+'\n\n'+('No main calls.' if not main['complete'] else '\n'.join(mtable))+f'\n\nDecision: {final}. Readiness={im["ready"]}; evaluated={im["evaluated"]}. Frozen hashes verified.\n'
    (OUT/'design_audit.md').write_bytes(pre+post.encode())
    prior=load('manifest.json')['prior_artifacts']
    for path,value in prior.items():
        assert digest(path)==value,path
    write('verification.json',dict(frozen_inputs_unchanged=True,historical_artifacts_unchanged=len(prior),total_calls=sum(map(len,raw.values())),actual_state_forwarding_checked=True))
    text('CHANGELOG.md','# v3.6.3\n\nAdded calibrated synthetic upstream and recorded-state propagation components, actual unrepaired modular pipeline, separate integrated and optional order diagnostics. Maximum340 calls; no next phase.\n\nFinal decision: '+final+'\n')
    print('\n'.join(summary),flush=True)


if __name__=='__main__':
    report()
