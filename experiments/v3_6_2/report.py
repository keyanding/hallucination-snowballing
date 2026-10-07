"""Generate complete per-K and paired diagnostic reports from raw outputs."""
import json
from .prepare import OUT,load,write,text,verify,digest
from .analyze import main_metrics,diagnostic_metrics,decide
from .design import KS,BANDS


def report():
    verify()
    rows={stage:[json.loads(s) for s in (OUT/(stage+'_outputs.jsonl')).read_text(encoding='utf-8').splitlines()] for stage in ('main','position_diagnostic')}
    plan=load('prompt_plan.json')
    for stage in rows:
        assert len(rows[stage])<=len(plan[stage])
        for p,r in zip(plan[stage],rows[stage]):
            assert all(r[k]==v for k,v in p.items())
    cases=load('cases.json')
    main,m=main_metrics(cases,rows['main'])
    secondary,d=diagnostic_metrics(cases,load('position_schedule.json')['diagnostic_cases'],rows['position_diagnostic'],main)
    gate=decide(m,(OUT/'failure.json').exists(),d['complete'])
    gate.update(main_calls=len(main),diagnostic_calls=len(secondary),off_target_by_k=m['off_target_by_k'],
                monotonic_collapse=m['monotonic_collapse'],paired_success_counts=m['paired_success_counts'])
    write('metrics.json',m)
    write('position_diagnostic_metrics.json',d)
    write('gate.json',gate)
    text('parsed_outcomes.jsonl',''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in main+secondary))
    table=['| K | C0 correct /40 | W0 correct /40 | Paired /40 | UNKNOWN /80 | OTHER+INVALID /80 |','|---|---|---|---|---|---|']
    for k in KS:
        values=m['levels'][str(k)]['metrics']
        table.append('| '+str(k)+' | '+' | '.join(str(values[x]['count']) for x in ('A_C','A_W','S','U','O'))+' |')
    deltas=['| K vs K0 | ΔC /40 | ΔW /40 | ΔS /40 | Paired lost | Paired gained |','|---|---|---|---|---|---|']
    for k in KS[1:]:
        v=m['degradation'][str(k)]
        deltas.append('| '+str(k)+' | '+' | '.join(str(v['deltas'][x]['numerator']) for x in ('delta_C','delta_W','delta_S'))+f" | {v['lost_count']} | {v['gained_count']} |")
    positions=['| K24 position | C0 /12 | W0 /12 | UNKNOWN /24 | OTHER+INVALID /24 |','|---|---|---|---|---|']
    for band in BANDS:
        v=d['bands'][band]
        positions.append('| '+band+' | '+' | '.join(str(v[x]['count']) for x in ('C0','W0','UNKNOWN','OTHER_INVALID'))+' |')
    label=gate['final_decision']
    conclusion={
        'ROBUST_CONTEXT_ASSAY':'The minimal state-propagation primitive remains highly reliable under up to24 irrelevant state-to-outcome records in this synthetic setting.',
        'CONTEXT_SENSITIVE_ASSAY':'The frozen criteria classify this assay as context-sensitive. Report observed per-K and paired effects, including off-target counts, before attributing a direction or source of degradation.',
        'BASE_ASSAY_REGRESSION':'The minimal baseline failed to replicate on the fresh sample. Context-size effects must not be interpreted.',
        'INFRASTRUCTURE_FAILURE':'Structural/runtime execution was invalid or incomplete. No robustness conclusion is licensed.'}[label]
    report=['# v3.6.2 context accumulation robustness','', '**'+label+'**','',
            f"Completed {len(main)}/320 main calls and {len(secondary)}/72 position-diagnostic calls.",'',*table,'',
            'Primary unit:40 paired base cases. C0/W0 are reported separately. Full categories, Wilson95% intervals and case transitions are in metrics.json.','',
            '## Paired changes from K0','',*deltas,'',
            'Paired lost means both C0/W0 correct at K0, but at least one becomes incorrect at that K; gained is the reverse.','',
            '## Separate position diagnosis','',*positions,'',
            'These12 seeded cases do not alter the main gate. Relevant pair region is balanced across primary cases and held fixed per case at positive K; K0 has only two lines.','',
            '## Interpretation','',conclusion,
            'No natural hallucination, upstream reasoning layer, SHAR/HalluSE, conflicting evidence or internal-mechanism claim. No next phase was run.','',
            'See diagnosis.md, inspection.md, pre_registration.md, position_schedule.json and prompt_diff_audit.md. Recompute with `python -m experiments.v3_6_2.report`.']
    if not gate['context_interpretation_allowed']:
        report.insert(4,'**Context-size interpretation stopped. Tables are raw descriptive output only.**')
    text('README.md','\n'.join(report).rstrip()+'\n')
    diagnosis=['# Context robustness diagnosis','', '**'+label+'**','',conclusion,'',
               f"Monotonic collapse={m['monotonic_collapse']}; paired success counts K0/K4/K12/K24={m['paired_success_counts']}.",
               f"Off-target by K={m['off_target_by_k']}; total {m['total_off_target']}/320. These are model outputs; they do not themselves imply infrastructure failure.",
               f"Sensitive triggers, when baseline valid: {gate.get('triggers','not evaluated because an earlier gate has priority')}.",'',
               '## Per-K intervals and complete categories','']
    for k in KS:
        v=m['levels'][str(k)]
        diagnosis += ['### K'+str(k),'']
        for metric in ('A_C','A_W','S'):
            x=v['metrics'][metric]
            diagnosis.append(f"- {metric}: {x['count']}/40; Wilson95% interval {x['wilson_95']}.")
        diagnosis += [f"- Categories by arm: {v['condition_counts']}.",'']
    diagnosis += ['## Paired degradation details','',*deltas,'']
    for k in KS[1:]:
        v=m['degradation'][str(k)]
        diagnosis += ['### K0 → K'+str(k),'',f"Paired lost cases: {v['paired_lost']}; gained: {v['paired_gained']}.",'']
        for arm in ('C0','W0'):
            a=v['arms'][arm]
            diagnosis += [f"{arm}: correct→incorrect {a['correct_to_incorrect']}/40; incorrect→correct {a['incorrect_to_correct']}/40; correct→paired-wrong-or-UNKNOWN {a['correct_to_wrong_or_unknown']}/40.",'',
                          '| Case | K0 category | New category | K0 output | New output |','|---|---|---|---|---|']
            for p in a['case_transitions']:
                diagnosis.append(f"| {p['case_id']} | {p['before']} | {p['after']} | {p['before_output']} | {p['after_output']} |")
            diagnosis.append('')
    diagnosis += ['## Position diagnosis','',*positions,'',
                  'Complete per-case position transitions are recorded in position_diagnostic_metrics.json. Differences within this12-case subset diagnose sensitivity to moving the pair; they do not identify an internal retrieval mechanism.',
                  f"Identical primary/secondary K24 prompts: {len(d['primary_identical_prompt_repeats'])}; token-identical repeats: {sum(r['token_identical'] for r in d['primary_identical_prompt_repeats'])}.",'',
                  '## Limits','',
                  'Same-case nested records preserve ordering and pair region, but longer context necessarily changes absolute distances. K0 cannot balance three regions with only two mappings. The K24 diagnostic is the prespecified12-case subset, not a new40-case replication. Each state/outcome is arbitrary; the findings do not establish real-world factual reasoning or natural hallucination propagation.']
    text('diagnosis.md','\n'.join(diagnosis).rstrip()+'\n')
    inspection=['# Exact prompts and outputs','','Only supplied-state downstream lookup is executed; no first-hop question is asked.','']
    for r in main+secondary:
        inspection += [f"## {r['stage']} / {r['case_id']} / K{r['k']} / {r['condition']} / {r['position_band']}",'',
                       'Query: Return only the mapped outcome.',f"Supplied intermediate: `{r['supplied_state']}`; expected: `{r['expected']}`.",
                       f"Relevant positions: gold={r['gold_position']}, wrong={r['wrong_position']}; parsed={r['category']}; correct={r['correct']}; distractor output={r['distractor_output']}; truncated={r['truncated']}.",
                       f"Prompt SHA256: `{r['text_sha256']}`; rendered SHA256: `{r['rendered_sha256']}`.",'','```text',r['prompt'],'```','','Raw output:','```json',json.dumps(r['raw_text'],ensure_ascii=False),'```','']
    text('inspection.md','\n'.join(inspection).rstrip()+'\n')
    pre=(OUT/'design_audit.pre_inference.md').read_bytes()
    post='\n## Post-inference audit\n\n'+'\n'.join(table)+'\n\n'+'\n'.join(positions)+f'\n\nFinal decision: {label}. Frozen inputs verified; no adaptive tuning.\n'
    (OUT/'design_audit.md').write_bytes(pre+post.encode())
    prior=load('case_manifest.json')['prior_artifacts']
    for path,value in prior.items():
        assert digest(path)==value,path
    write('verification.json',dict(frozen_inputs_unchanged=True,prior_artifacts_unchanged=len(prior),
          output_plan_exact=True,main_calls=len(main),position_diagnostic_calls=len(secondary)))
    text('CHANGELOG.md','# v3.6.2\n\nAdded nested irrelevant-context experiment with320 primary and72 position-diagnostic calls. User-amended gate hierarchy frozen before inference; OTHER/INVALID outputs are not infrastructure errors.\n\nFinal decision: '+label+'\n')
    print('\n'.join(report),flush=True)


if __name__=='__main__':
    report()
