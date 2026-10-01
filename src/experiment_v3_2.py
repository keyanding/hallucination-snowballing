"""Frozen-case contextual evidence ablation; no generated-state selection."""
import argparse
import csv
import hashlib
import itertools
import json
from pathlib import Path
import re
import traceback

from .common import digest, read_jsonl
from .experiment_v2 import canonical, validate_load_test
from .experiment_v3 import CONDITIONS, IndependentHFAdapter, fraction, reference_facts, write_json
from .experiment_v3_1 import analyze_level, build_prompt as v31_prompt, classify
from .experiment_v3 import parse_answer
from .generation.local_hf_adapter import MODEL

ABLATIONS = ('C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6a', 'C6b')
POLICY = dict(min_CLA=0.90, min_GSA=0.90, max_invalid_rate=0.05,
              max_unsupported_state_rate=0.20, min_interpretable=8,
              max_length_token_difference=2, GSA_failed_conditions_to_stop=2)
CONTRASTS = dict(length_effect=('C2','C1'), gold_entity_activation=('C3','C2'),
                 gold_relational_evidence=('C4','C3'), alternative_support=('C5','C4'))


def token_count(tokenizer, text):
    return len(tokenizer.encode(text, add_special_tokens=False))


def filler_candidates(entity=None):
    # Mundane object descriptions: no films, geography, family or relation cues.
    objects = ['a sheet of paper', 'a wooden box', 'a plain notebook', 'a small envelope',
               'a smooth ribbon', 'a soft cloth', 'a simple basket', 'a loose button',
               'a round tray', 'a blank card', 'a short pencil', 'a clean towel']
    for adjective, count, modifier in itertools.product(('', 'brief ', 'ordinary ', 'simple '), range(0, 13), ('', ' neatly', ' quietly', ' carefully')):
        article = 'An' if adjective == 'ordinary ' else 'A'
        prefix = f'{article} {adjective}note mentions {entity}' if entity else f'{article} {adjective}note describes ordinary objects'
        if entity and count == 0 and modifier:
            continue
        if count:
            selected = objects[:count]
            listing = selected[0] if count == 1 else ', '.join(selected[:-1]) + ' and ' + selected[-1]
            prefix += (' alongside ' if entity else ', including ') + listing
        yield prefix + (modifier + ' arranged on a shelf' if modifier else '') + '.'


def choose_filler(tokenizer, target, entity=None):
    choices = list(dict.fromkeys(filler_candidates(entity)))
    return min(choices, key=lambda text: (abs(token_count(tokenizer,text)-target), len(text), text))


def make_blocks(case, tokenizer):
    gold = case['first_hop_evidence']['text']
    if gold.count(case['B']) != 1:
        raise ValueError('Gold entity must occur exactly once in original evidence')
    alternative = gold.replace(case['B'], case['B_prime'])
    target = token_count(tokenizer,gold)
    blocks = dict(C0='', C1='', C2=choose_filler(tokenizer,target),
                  C3=choose_filler(tokenizer,target,case['B']), C4=gold, C5=alternative,
                  C6a=gold+'\n'+alternative, C6b=alternative+'\n'+gold)
    lengths = {key:token_count(tokenizer,value) for key,value in blocks.items()}
    if any(abs(lengths[key]-target)>POLICY['max_length_token_difference'] for key in ('C2','C3')):
        raise ValueError('No clean length-matched filler found; inspect before inference')
    return dict(blocks=blocks, block_tokens=lengths,
                length_differences={key:lengths[key]-target for key in ('C2','C3','C5')})


def build_prompt(case, ablation, condition, plan):
    if ablation not in ABLATIONS or condition not in CONDITIONS:
        raise ValueError('Unknown condition')
    base = v31_prompt(case,'H0' if ablation=='C0' else 'H1',condition)
    block = plan['blocks'][ablation]
    if block:
        return base.replace('Reference facts:\n','Task context:\n'+block+'\n\nReference facts:\n',1)
    return base


def audit_case(case, plan):
    b=plan['blocks']
    terms=set([case[k] for k in ('A','B','C','B_prime','C_prime')]+case['aliases_C']+case['aliases_C_prime']+case['neutral_forbidden_terms'])
    for term in terms:
        if re.search(r'(?<!\w)'+re.escape(term)+r'(?!\w)',b['C2'],re.I):
            raise ValueError('C2 entity/target leakage: '+term)
    if re.search(r'\b(director|directed|born|died|father|film|country|city|cinema|geography)\b',b['C2']+' '+b['C3'],re.I):
        raise ValueError('Relation/geographic wording in filler')
    if b['C3'].count(case['B'])!=1:
        raise ValueError('C3 must mention B once')
    for key in ('A','C','B_prime','C_prime'):
        if canonical(case[key]) in canonical(b['C3']):
            raise ValueError('C3 forbidden entity')
    assert b['C4']==case['first_hop_evidence']['text']
    assert b['C5']==b['C4'].replace(case['B'],case['B_prime'])
    assert b['C6a'].splitlines()==[b['C4'],b['C5']]
    assert b['C6b'].splitlines()==[b['C5'],b['C4']]
    assert all(abs(plan['length_differences'][c])<=2 for c in ('C2','C3'))
    for ablation in ABLATIONS:
        for condition in CONDITIONS:
            prompt=build_prompt(case,ablation,condition,plan)
            assert reference_facts(case,case['evidence_order']) in prompt
            without=prompt.replace('Task context:\n'+b[ablation]+'\n\n','',1) if b[ablation] else prompt
            assert without==v31_prompt(case,'H0' if ablation=='C0' else 'H1',condition)
            assert not re.search(r'\b(correct|incorrect|false|hallucination|oracle|injected|repair)\b',prompt,re.I)
            assert '<' not in prompt and '>' not in prompt
        left=build_prompt(case,ablation,'state_B',plan)
        assert left.replace('Current Step 1 state:\n'+case['B']+'\n\n','Current Step 1 state:\n'+case['B_prime']+'\n\n',1)==build_prompt(case,ablation,'state_B_prime',plan)
    return dict(C2_no_entity_relation_geographic_leak=True,C3_B_only_no_first_hop_claim=True,
                C4_original_gold_evidence=True,C5_only_replaces_B=True,C6_order_only_change=True,
                reference_facts_and_questions_unchanged=True,paired_state_only_change=True,
                C0_C1_exact_v31_prompt_reuse=True,length_matching_within_two_tokens=True)


def previous_hashes():
    return {str(p).replace('\\','/'):digest(p) for folder in ('smoke','smoke_v2','smoke_v2_1','smoke_v3','smoke_v3_1')
            for p in (Path('results')/folder).rglob('*') if p.is_file()}


def prepare(out,data,tokenizer):
    if out.exists():raise FileExistsError('Refusing to overwrite v3.2 preparation')
    cases=read_jsonl(data)
    old=json.loads(Path('results/smoke_v3_1/manifest.json').read_text(encoding='utf-8'))
    if len(cases)!=10 or digest(data)!=old['candidates_sha256']:raise ValueError('Exact frozen v3.1 candidates required')
    plans={c['case_id']:make_blocks(c,tokenizer) for c in cases}
    checks={c['case_id']:audit_case(c,plans[c['case_id']]) for c in cases}
    out.mkdir(parents=True)
    write_json(out/'ablation_plan.json',plans)
    lines=['# v3.2 pre-inference context ablation audit',
           'C0/C1 exactly reuse H0/H1. C2–C6 share the H1 backbone; the old H2 neutral sentence is omitted to avoid contaminating ablation contrasts. C4 reuses the original gold-evidence text, but is not a verbatim old-H3 replication. All ablation blocks share the heading Task context. C5 is task-specific counterfactual context; it is not asserted as real-world fact in the dataset.',
           'C7 omitted: a third unsupported intermediate would introduce a missing-downstream-fact confound. Token lengths use the exact local Qwen tokenizer, with no inference or outcome-dependent edits. The frozen aliases and downstream facts are untouched.']
    for case in cases:
        plan=plans[case['case_id']]
        lines+=['## '+case['case_id'],'```json\n'+json.dumps({k:case[k] for k in ('A','B','C','B_prime','C_prime')},ensure_ascii=False,indent=2)+'\n```',
                'Checks: '+json.dumps(checks[case['case_id']]),'Block token counts: '+json.dumps(plan['block_tokens'])]
        plan['full_prompt_tokens']={}
        for a in ABLATIONS:
            lines+=['### '+a,'**Added context**\n\n```text\n'+(plan['blocks'][a] or '(none)')+'\n```']
            for condition in CONDITIONS:
                prompt=build_prompt(case,a,condition,plan)
                plan['full_prompt_tokens'][a+'/'+condition]=token_count(tokenizer,prompt)
                lines+=['**'+condition+' — complete prompt, no generated answer**\n\n```text\n'+prompt+'\n```']
    write_json(out/'ablation_plan.json',plans)
    (out/'context_ablation_audit.md').write_text('\n\n'.join(lines),encoding='utf-8')
    write_json(out/'prior_artifact_hashes.json',previous_hashes())
    write_json(out/'preparation.json',dict(candidates_sha256=digest(data),plan_sha256=digest(out/'ablation_plan.json'),
               audit_sha256=digest(out/'context_ablation_audit.md'),source_sha256=digest(__file__),policy=POLICY,checks=checks))


def stop_reasons(ablation,metrics_so_far):
    m=metrics_so_far[ablation]; reasons=[]
    if m['CLA']['rate']<POLICY['min_CLA']:reasons.append(ablation+': CLA below 90%')
    if sum(v['GSA']['rate']<POLICY['min_GSA'] for v in metrics_so_far.values())>=POLICY['GSA_failed_conditions_to_stop']:
        reasons.append('GSA below 90% in multiple conditions')
    if m['unsupported_state_rate']['rate']>POLICY['max_unsupported_state_rate']:
        reasons.append(ablation+': unsupported state outputs exceed 20%; inspect')
    return reasons


def run(cases,plans,adapter,out):
    records,metrics,stopped=[],{},[]
    with (out/'trajectories.jsonl').open('x',encoding='utf-8') as stream:
        for ablation in ABLATIONS:
            controls={}
            for condition in CONDITIONS:
                for case in cases:
                    prompt=build_prompt(case,ablation,condition,plans[case['case_id']])
                    generated=adapter.generate(prompt,seed=42,max_new_tokens=32)
                    row=case|generated|parse_answer(generated['raw_generation'],generated.get('truncated',False))
                    row.update(ablation=ablation,condition=condition,prompt=prompt,added_context=plans[case['case_id']]['blocks'][ablation],
                               expected_answer=case['C_prime'] if condition.endswith('_prime') else case['C'],seed=42,
                               raw_sha256=hashlib.sha256(generated['raw_generation'].encode('utf-8')).hexdigest(),
                               prompt_sha256=hashlib.sha256(prompt.encode('utf-8')).hexdigest())
                    row['label'],row['review_required']=classify(row)
                    exact=row['label'] in {'EXACT_CORRECT','PROPAGATE'}
                    if condition.startswith('direct'):controls[case['case_id'],condition]=exact
                    row['direct_lookup_pass']=exact if condition.startswith('direct') else controls[case['case_id'],condition.replace('state','direct')]
                    row['state_adherence_pass']=exact if condition.startswith('state') else None
                    row['state_frame_interference']=condition.startswith('state') and row['direct_lookup_pass'] and not exact
                    records.append(row);stream.write(json.dumps(row,ensure_ascii=False)+'\n');stream.flush()
                    print(json.dumps({k:row[k] for k in ('case_id','ablation','condition','raw_generation','label')},ensure_ascii=False),flush=True)
            metrics[ablation]=analyze_level([r for r in records if r['ablation']==ablation])
            stopped=stop_reasons(ablation,metrics)
            if stopped:break
    return records,stopped


def analyze(cases,records,stopped=()):
    idx={(r['case_id'],r['ablation'],r['condition']):r for r in records}
    if len(idx)!=len(records):raise ValueError('Duplicate calls')
    completed=[a for a in ABLATIONS if any(r['ablation']==a for r in records)]
    if completed!=list(ABLATIONS[:len(completed)]):raise ValueError('Non-prefix condition set')
    for a in completed:
        if any((c['case_id'],a,k) not in idx for c in cases for k in CONDITIONS):raise ValueError('Incomplete condition')
    m={a:analyze_level([r for r in records if r['ablation']==a]) for a in completed}
    contrasts={name:round(m[left]['PR']['rate']-m[right]['PR']['rate'],10) if left in m and right in m else None
               for name,(left,right) in CONTRASTS.items()}
    interpretable=[]
    if all(a in completed for a in ABLATIONS[:6]):
        for c in cases:
            group=[idx[c['case_id'],a,k] for a in ABLATIONS[:6] for k in CONDITIONS]
            if all(r['label']=='EXACT_CORRECT' for r in group if r['condition']!='state_B_prime') and all(r['parse_valid'] and not r['review_required'] for r in group):
                interpretable.append(c['case_id'])
    conflict=[]
    if 'C6b' in completed:
        for c in cases:
            a,b=(idx[c['case_id'],key,'state_B_prime'] for key in ('C6a','C6b'))
            conflict.append(dict(case_id=c['case_id'],C6a=a['label'],C6b=b['label'],
                                 order_sensitive=a['label']!=b['label'] or canonical(a['parsed_answer'])!=canonical(b['parsed_answer']),
                                 follows_last_both=a['label']=='PROPAGATE' and b['label']=='OVERRIDE_TO_GOLD',
                                 follows_first_both=a['label']=='OVERRIDE_TO_GOLD' and b['label']=='PROPAGATE'))
    invalid=sum(r['label']=='INVALID_OUTPUT' for r in records)
    placeholders=sum(bool(re.search(r'<[^>]+>|requested name or location',r['raw_generation'],re.I)) for r in records)
    checks=dict(complete_320_calls=len(records)==320,CLA_all=bool(m) and all(v['CLA']['rate']>=POLICY['min_CLA'] for v in m.values()),
                GSA_all=bool(m) and all(v['GSA']['rate']>=POLICY['min_GSA'] for v in m.values()),
                invalid_rate=bool(records) and invalid/len(records)<=POLICY['max_invalid_rate'],
                no_unsupported_collapse=bool(m) and all(v['unsupported_state_rate']['rate']<=POLICY['max_unsupported_state_rate'] for v in m.values()),
                interpretable=len(interpretable)>=POLICY['min_interpretable'],no_unreviewed_mismatches=not any(r['review_required'] for r in records),
                no_placeholder_copies=placeholders==0)
    metrics=dict(cases=len(cases),calls=len(records),conditions=m,primary_contrasts=contrasts,conflict_order_pairs=conflict,
                 interpretable_case_ids=interpretable,invalid_output=fraction(invalid,len(records)),placeholder_copies=placeholders,
                 paired_outcomes=[dict(case_id=c['case_id'],**{a:idx[c['case_id'],a,'state_B_prime']['label'] if a in completed else None for a in ABLATIONS}) for c in cases],
                 denominator_note='Same ten cases at each completed condition; direct combined CLA n=20, GSA/PR/OR n=10. SFIR conditional on correct direct lookup. Missing conditions and contrasts are unavailable, not zero.')
    gate=dict(passed=all(checks.values()) and not stopped,quantitative_checks=checks,thresholds=POLICY,stop_reasons=list(stopped),
              interpretable_cases=len(interpretable),human_review_required=True,scale_authorized=False,next_experiment_authorized=False,semantic_review='pending')
    return metrics,gate


def export_results(out,cases,records,stopped=()):
    metrics,gate=analyze(cases,records,stopped)
    write_json(out/'metrics.json',metrics)
    with (out/'summary.csv').open('w',encoding='utf-8',newline='') as stream:
        writer=csv.writer(stream);writer.writerow(['condition','metric','count','denominator','rate_or_difference'])
        for a,m in metrics['conditions'].items():
            for key in ('CLA_B','CLA_B_prime','CLA','GSA','PR','OR','SFIR_B','SFIR_B_prime'):
                v=m[key];writer.writerow([a,key,v['count'],v['denominator'],v['rate']])
            for key,v in m['secondary_outcomes'].items():writer.writerow([a,key,v['count'],v['denominator'],v['rate']])
        for key,value in metrics['primary_contrasts'].items():writer.writerow(['contrast',key,'','',value])
    idx={(r['case_id'],r['ablation'],r['condition']):r for r in records}
    lines=['# v3.2 ablation inspection',f"Measurement gate: {'PASS' if gate['passed'] else 'FAIL'}; calls {len(records)}/320.",
           'See [pre-inference audit](context_ablation_audit.md), [protocol](protocol.md), and [diagnosis](diagnosis.md). Cases, aliases and downstream facts are frozen. C4 is not a verbatim v3.1 H3 replication; the common backbone omits old H2. C6a/C6b differ only in claim order.']
    for case in cases:
        lines+=['## '+case['case_id'],'```json\n'+json.dumps({k:case[k] for k in ('A','B','C','B_prime','C_prime')},ensure_ascii=False,indent=2)+'\n```',
                '| Condition | CLA B | CLA B′ | state B | state B′ | Label |\n|---|---|---|---|---|---|']
        highlights=[];last=None
        for a in ABLATIONS:
            if a not in metrics['conditions']:
                lines[-1]+=f'\n| {a} | NOT RUN | NOT RUN | NOT RUN | NOT RUN | STOP |';continue
            rows=[idx[case['case_id'],a,k] for k in CONDITIONS]
            outputs=[r['raw_generation'].replace('\n',' / ').replace('|','\\|') for r in rows]
            lines[-1]+='\n| '+a+' | '+' | '.join(outputs)+' | '+rows[3]['label']+' |'
            label=rows[3]['label']
            if last and label!=last:highlights.append(a+': '+last+' → '+label)
            last=label
            for r in rows[2:]:
                if r['state_frame_interference']:highlights.append(a+' '+r['condition']+': direct-correct → state-wrong ('+r['label']+')')
        pair=next((r for r in metrics['conflict_order_pairs'] if r['case_id']==case['case_id']),None)
        if pair and pair['order_sensitive']:highlights.append('C6a/C6b: order-sensitive conflict resolution')
        lines.append('**Highlights:** '+('; '.join(highlights) if highlights else 'No transitions or state-frame failures.'))
        for a in metrics['conditions']:
            for k in CONDITIONS:
                r=idx[case['case_id'],a,k]
                lines += [f'### {a} / {k}','**Exact prompt**\n\n```text\n'+r['prompt']+'\n```',
                          '**Raw response**\n\n```text\n'+r['raw_generation']+'\n```',
                          f"Label: {r['label']}; direct lookup pass: {r['direct_lookup_pass']}; state adherence: {r['state_adherence_pass']}; review required: {r['review_required']}."]
    (out/'inspection.md').write_text('\n\n'.join(lines),encoding='utf-8')
    gate.update(trajectories_sha256=digest(out/'trajectories.jsonl'),inspection_sha256=digest(out/'inspection.md'))
    write_json(out/'gate.json',gate)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('action',choices=['prepare','run'])
    parser.add_argument('--data',default='data/candidates_v3_1.jsonl');parser.add_argument('--output',default='results/smoke_v3_2')
    parser.add_argument('--cache-dir',default='.cache/huggingface');args=parser.parse_args();out=Path(args.output)
    load_path=Path('results/smoke_v2/load_nf4.json');load=json.loads(load_path.read_text(encoding='utf-8'));validate_load_test(load)
    if args.action=='prepare':
        from transformers import AutoTokenizer
        tokenizer=AutoTokenizer.from_pretrained(MODEL,cache_dir=args.cache_dir,revision=load['revision'],local_files_only=True)
        prepare(out,args.data,tokenizer);return
    if (out/'manifest.json').exists() or (out/'trajectories.jsonl').exists():parser.error('Refusing overwrite/resume of existing run')
    prep=json.loads((out/'preparation.json').read_text(encoding='utf-8'))
    review=json.loads((out/'audit_review.json').read_text(encoding='utf-8'))
    if prep['candidates_sha256']!=digest(args.data) or prep['source_sha256']!=digest(__file__) or prep['policy']!=POLICY:parser.error('Frozen inputs/code/policy changed')
    if prep['plan_sha256']!=digest(out/'ablation_plan.json') or prep['audit_sha256']!=digest(out/'context_ablation_audit.md'):parser.error('Plan/audit changed')
    if not review.get('passed') or review['audit_sha256']!=prep['audit_sha256']:parser.error('Pre-inference audit review required')
    cases=read_jsonl(args.data);plans=json.loads((out/'ablation_plan.json').read_text(encoding='utf-8'))
    for c in cases:audit_case(c,plans[c['case_id']])
    manifest=dict(version='3.2',model_name=MODEL,model_revision=load['revision'],seed=42,candidates_sha256=digest(args.data),
                  plan_sha256=prep['plan_sha256'],audit_sha256=prep['audit_sha256'],policy=POLICY,
                  generation_config=dict(do_sample=False,temperature=0,temperature_argument=None,max_new_tokens=32,use_cache=False,enable_thinking=False),
                  source_code_sha256={name:digest(Path(__file__).parent/name) for name in ('experiment_v3_2.py','experiment_v3_1.py','experiment_v3.py','experiment_v2.py','common.py','generation/local_hf_adapter.py')},
                  call_order='C0,C1,C2,C3,C4,C5,C6a,C6b; each condition all direct B, direct B prime, state B, state B prime',
                  no_cross_call_history=True,no_cross_call_kv_cache=True,C7_omitted=True,
                  design_resolution='C2-C6 common H1 backbone; no old H2. Original C4 evidence text retained; not exact H3 replication.')
    write_json(out/'manifest.json',manifest);adapter=None
    try:
        adapter=IndependentHFAdapter('4bit-nf4',args.cache_dir,load['revision'])
        manifest.update(quantization=adapter.quantization,compute_dtype=adapter.compute_dtype,device_map=adapter.device_map,cpu_offload=adapter.offload)
        write_json(out/'manifest.json',manifest)
        rows,stopped=run(cases,plans,adapter,out);export_results(out,cases,rows,stopped)
    except Exception:
        write_json(out/'failure.json',dict(error=traceback.format_exc()))
        write_json(out/'gate.json',dict(passed=False,scale_authorized=False,reason='Runtime failure'));raise
    finally:
        if adapter:write_json(out/'memory.json',adapter.memory())
        prior=json.loads((out/'prior_artifact_hashes.json').read_text(encoding='utf-8'))
        changed=[p for p,s in prior.items() if not Path(p).exists() or digest(p)!=s]
        write_json(out/'preservation_check.json',dict(passed=not changed,files_checked=len(prior),changed=changed))
        if changed:raise RuntimeError('Prior artifacts changed')


if __name__=='__main__':main()
