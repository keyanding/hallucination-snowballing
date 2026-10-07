"""Report main gates separately from shell compatibility and integrated readiness."""
import json
from .prepare import OUT, load, write, text, verify, digest
from .analyze import calibration, main_metrics, integrated, shell_diagnostic, decide
from .run import FILES
from .design import pipeline


def report():
    verify()
    raw = {k:[json.loads(s) for s in (OUT/(k+'_outputs.jsonl')).read_text(encoding='utf-8').splitlines()] for k in FILES}
    logs = [json.loads(s) for s in (OUT/'pipeline_log.jsonl').read_text(encoding='utf-8').splitlines()]
    plan = load('prompt_plan.json')
    for key in FILES:
        if key=='pipeline_generated':
            continue
        assert len(raw[key])<=len(plan[key])
        for p,r in zip(plan[key],raw[key]):
            assert all(r[k]==v for k,v in p.items())
    cal_cases,cases,diagnostic = (load(k+'_cases.json') for k in ('calibration','main','diagnostic'))
    cp,cal = calibration(cal_cases,raw['calibration'])
    mp,main = main_metrics(cases,raw['main_upstream'],raw['main_downstream'],raw['pipeline_generated'],logs)
    ip,im = integrated(cases,load('subsets.json')['integrated'],raw['integrated'])
    sp,sm = shell_diagnostic(diagnostic,raw['shell_diagnostic'])
    final = decide(cal,main,sm,im,(OUT/'failure.json').exists())
    if cal['complete'] and not cal['passed']:
        assert all(not raw[k] for k in FILES if k!='calibration') and not logs
    if main['complete'] and not main['passed']:
        assert not raw['integrated']
    up = {r['case_id']:r for r in raw['main_upstream'] if r['condition']=='U-A'}
    case_by = {c['case_id']:c for c in cases}
    log_by = {r['case_id']:r for r in logs}
    for r in raw['pipeline_generated']:
        p,metadata = pipeline(case_by[r['case_id']],up[r['case_id']])
        assert metadata==r['upstream_source']==log_by[r['case_id']]
        assert all(json.dumps(r[k])==json.dumps(v) for k,v in p.items())
    gate = dict(final_decision=final,calibration_pass=cal['passed'],main_evaluated=main['complete'],
                main_pass=main['passed'] if main['complete'] else None,INTEGRATED_TWO_HOP_READY=im['ready'],
                integrated_evaluated=im['evaluated'],shell_diagnostic_evaluated=sm['evaluated'],
                counts={k:len(v) for k,v in raw.items()},pipeline_skipped=main['pipeline_skipped'])
    write('metrics.json',dict(calibration=cal,main=main))
    write('shell_diagnostic_metrics.json',sm)
    write('integrated_metrics.json',im)
    write('gate.json',gate)
    text('parsed_outcomes.jsonl',''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in cp+mp+sp+ip))
    ctable = ['| Calibration gate | Count | Minimum | Pass |','|---|---|---|---|']
    for key,v in cal['gates'].items():
        ctable.append(f"| {key} | {v['count']}/{v['denominator']} | {v['minimum']} | {v['passed']} |")
    mtable = ['| Main metric | Count | Wilson 95% | Gate passed |','|---|---|---|---|']
    for i,(key,v) in enumerate(main['metrics'].items(),1):
        ci = v['wilson_95']
        interval = f'[{ci[0]:.1%}, {ci[1]:.1%}]' if ci else 'not evaluated'
        mtable.append(f"| {key} | {v['count']}/{v['denominator']} | {interval} | {main['gates']['G'+str(i)] if main['complete'] else 'not evaluated'} |")
    conclusion = {
        'INFRASTRUCTURE_FAILURE':'Execution/structural validity failed; no assay interpretation.',
        'STOP_V3631_CALIBRATION_INVALID':'A previously validated component failed to reproduce on fresh cases. Main and all diagnostics were not run; investigate replication before proceeding.',
        'TWO_HOP_PIPELINE_INVALID':'After restoring the validated downstream shell, the modular pipeline still failed at least one fixed main gate. Integrated was intentionally not run.',
        'TWO_HOP_PIPELINE_VALIDATED':'The synthetic modular two-hop pipeline passed: actual inferred states forwarded into the validated Current state interface produced the corresponding outcomes, and counterfactual supplied states predictably switched downstream outcomes.'}[final]
    boundary = 'This does not establish natural hallucination propagation, spontaneous error rates, injected/natural-error equivalence, internal neural mechanism, SHAR/HalluSE performance or real-world reasoning. Integrated final-answer accuracy does not prove internal intermediate use. No next phase was run.'
    summary = ['# v3.6.3.1 frozen-interface two-hop pipeline','', '**'+final+'**','',
               'Calls: '+', '.join(f'{k}={len(v)}' for k,v in raw.items())+f"; total={sum(map(len,raw.values()))}. Pipeline skips={main['pipeline_skipped']}.",'',*ctable,'']
    if main['complete']:
        cond = main['conditional_downstream']
        summary += ['## Main','',*mtable,'',f"G7 OTHER+INVALID={main['G7_off_target']['count']}/160; pass={main['gates']['G7']}.",
                    f"Downstream C conditional on correct U-A: {cond['count']}/{cond['denominator']}. Strict E2E denominator40 includes all skips.",'']
    else:
        summary += ['Main was not evaluated; main rates/intervals are null.','']
    if sm['evaluated']:
        summary += ['## Shell compatibility diagnostic (non-gating)','',
                    '| Shell | Exact accuracy | INVALID | Explanation-format | Prefix omission | Truncated |',
                    '|---|---|---|---|---|---|']
        for name,m in sm['shells'].items():
            summary.append(f"| {name} | {m['exact_accuracy']['count']}/20 | {m['invalid_count']} | {m['explanation_format_count']} | {m['prefix_omission_count']} | {m['truncation_count']} |")
        summary += ['',f"Paired discordances: RECORDED-only failures={sm['recorded_only_failures']}; VALIDATED-only failures={sm['validated_only_failures']}. Flags may overlap and are descriptive, not alternate parsing.",'']
    else:
        summary += ['Shell diagnostic not evaluated.','']
    summary += [f"INTEGRATED_TWO_HOP_READY={im['ready']}; evaluated={im['evaluated']}."]
    if im['evaluated']:
        summary += [f"I-A={im['I_A']['count']}/20; I-B={im['I_B']['count']}/20; paired={im['paired']['count']}/20."]
    else:
        summary += ['Readiness=false with evaluated=false is an unrun diagnostic, not observed inability.']
    summary += ['','## Interpretation','',conclusion,boundary,'','See diagnosis.md, interpretation.md, inspection.md and the frozen pre_registration.md.']
    text('README.md','\n'.join(summary).rstrip()+'\n')
    diagnostic_text = 'The shell diagnostic was not run.'
    if sm['evaluated']:
        v = sm['shells']['VALIDATED']['exact_accuracy']['count']
        r = sm['shells']['RECORDED']['exact_accuracy']['count']
        diagnostic_text = f'The matched shell diagnostic yielded VALIDATED {v}/20 and RECORDED {r}/20. '
        diagnostic_text += ('The validated interface had higher observed exact-output accuracy on these cases. ' if v>r else 'It did not show higher exact-output accuracy for the validated shell on these cases. ')
        diagnostic_text += 'This compares complete prompt shells, not the heading alone, on ten fresh cases; it does not establish a unique cause of historical v3.6.3 failures or an internal mechanism.'
    readiness = ('Integrated two-hop execution met the separate readiness threshold; a later Phase I natural-error study may be designed, but has not been run.' if im['ready'] else
                 'Integrated execution did not meet the separate readiness threshold.' if im['evaluated'] else 'Integrated readiness was not evaluated under the conditional schedule.')
    interpretation = ['# Interpretation','',conclusion,'',readiness,'',diagnostic_text,'',boundary,'']
    text('interpretation.md','\n'.join(interpretation))
    diagnosis = ['# Diagnosis','', '**'+final+'**','',conclusion,'','## Calibration','',*ctable,'','## Main','']
    if main['complete']:
        diagnosis += mtable+['',f"Condition categories: {main['categories']}.",f"Pipeline outcome categories: {main['pipeline_category_counts']}.",
                            f"Strict pipeline failure sources: {main['pipeline_failures']}.",'','## Paired upstream categories','','```json',json.dumps(main['tables']['U'],indent=2),'```','',
                            '## Paired downstream categories','','```json',json.dumps(main['tables']['D'],indent=2),'```']
    else:
        diagnosis += ['Not evaluated; no calibration case was replaced or repaired.']
    diagnosis += ['','## Separate diagnostics','',diagnostic_text,readiness,'','```json',json.dumps(sm,indent=2),'```','',
                  '## Boundary','', 'D-A/D-B differ only by Current state. PIPELINE-A forwards actual normalized U-A, including wrong/unmapped well-formed states; INVALID upstream skips without replacement. Strict E2E requires both U-A=B and pipeline=C.',boundary,'']
    text('diagnosis.md','\n'.join(diagnosis))
    inspection = ['# Exact subquestions, prompts and outputs','','Each pipeline entry links the actual upstream raw/normalized state. Expected answers are report metadata, never added to prompts.','']
    for r in cp+mp+sp+ip:
        question = r['prompt'].split('\n\n')[-1]
        inspection += [f"## {r['case_id']} / {r['condition']} / {r.get('shell')}",'',f"Question/instruction: {question}",
                       f"Current entity: {r['current_entity']}; supplied intermediate: {r['supplied_state']}; expected: {r['expected']}.",
                       f"Category: {r['category']}; normalized (JSON): {json.dumps(r['normalized'],ensure_ascii=False)}; truncated={r['truncated']}.",
                       f"Prompt SHA256: `{r['text_sha256']}`; rendered SHA256: `{r['rendered_sha256']}`."]
        if 'upstream_source' in r:
            inspection += ['','Upstream source:','```json',json.dumps(r['upstream_source'],ensure_ascii=False,indent=2),'```']
        inspection += ['','```text',r['prompt'],'```','','Raw output:','```json',json.dumps(r['raw_text'],ensure_ascii=False),'```','']
    for r in logs:
        if r['status']=='UPSTREAM_INVALID_SKIPPED':
            inspection += ['## Skipped pipeline '+r['case_id'],'','```json',json.dumps(r,ensure_ascii=False,indent=2),'```','']
    text('inspection.md','\n'.join(inspection).rstrip()+'\n')
    pre = (OUT/'design_audit.pre_inference.md').read_bytes()
    post = '\n## Post-inference audit\n\n'+'\n'.join(ctable)+'\n\n'+('\n'.join(mtable) if main['complete'] else 'No main calls.')+f'\n\nDecision: {final}. Readiness={im["ready"]}; evaluated={im["evaluated"]}. Frozen hashes and actual state forwarding verified.\n'
    (OUT/'design_audit.md').write_bytes(pre+post.encode())
    prior = load('manifest.json')['prior_artifacts']
    for path,value in prior.items():
        assert digest(path)==value,path
    write('verification.json',dict(frozen_inputs_unchanged=True,historical_artifacts_unchanged=len(prior),total_calls=sum(map(len,raw.values())),actual_state_forwarding_checked=True))
    text('CHANGELOG.md','# v3.6.3.1\n\nRestored exact validated downstream shell; reused upstream, parser and decoding; forwarded actual states without repair. Added independent paired shell diagnostic, conditional integrated readiness and enforced inheritance workflow. Maximum360 calls; no next phase.\n\nFinal decision: '+final+'\n')
    print('\n'.join(summary),flush=True)


if __name__=='__main__':
    report()
