"""Real-entity context ladder, fixed 10 x 4 x 4 smoke matrix."""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import re
import traceback

from .common import digest, read_jsonl
from .experiment_v2 import matches, validate_load_test
from .experiment_v3 import (CONDITIONS, OUTCOMES, IndependentHFAdapter, TEMPLATES,
                            fraction, parse_answer, reference_facts, write_json)
from .generation.local_hf_adapter import MODEL

LEVELS = ('H0', 'H1', 'H2', 'H3')
POLICY = dict(H0_min_CLA=0.90, H0_min_GSA=0.90, H1_H2_min_CLA=0.80,
              H1_H2_min_GSA=0.80, min_interpretable_cases=8,
              max_invalid_rate=0.05, max_placeholder_copies=0,
              max_unsupported_state_rate=0.20, H3_min_CLA=0.80, H3_min_GSA=0.80)


def context_block(case, level):
    if level not in LEVELS:
        raise ValueError(level)
    blocks = []
    if level != 'H0':
        blocks.append('Original task:\n' + case['original_question'])
    if level in ('H2', 'H3'):
        blocks.append('Additional context:\n' + case['neutral_evidence']['text'])
    if level == 'H3':
        blocks.append('Additional evidence:\n' + case['first_hop_evidence']['text'])
    blocks.append(reference_facts(case, case['evidence_order']))
    return '\n\n'.join(blocks)


def build_prompt(case, level, condition):
    if condition not in CONDITIONS:
        raise ValueError(condition)
    state = condition.startswith('state')
    subject = case['B_prime'] if condition.endswith('_prime') else case['B']
    prefix = context_block(case, level) + '\n\n'
    if state:
        prefix += 'Current Step 1 state:\n' + subject + '\n\n'
        question = 'Using the current Step 1 state and the information above, ' + TEMPLATES[case['relation']][1].format(person='that person')
    else:
        question = 'According to the information above, ' + TEMPLATES[case['relation']][1].format(person=subject)
    return prefix + 'Question:\n' + question + '\n\nAnswer with only the requested name or location.'


def audit_case(case):
    h = {level: context_block(case, level) for level in LEVELS}
    neutral = case['neutral_evidence']['text']
    if case['neutral_evidence']['title'] != case['first_hop_evidence']['title']:
        raise ValueError('Neutral sentence from a different article/remake')
    if any(re.search(r'(?<!\w)' + re.escape(term) + r'(?!\w)', neutral, re.I) for term in case['neutral_forbidden_terms']):
        raise ValueError('Neutral context leaks entity or answer')
    if any(name.lower() in case['original_question'].lower() for name in (case['B'], case['B_prime'], case['C'], case['C_prime'])):
        raise ValueError('Original framing exposes a supplied entity or answer')
    assert h['H0'] == reference_facts(case, case['evidence_order'])
    assert h['H1'] == 'Original task:\n' + case['original_question'] + '\n\n' + h['H0']
    assert h['H2'].replace('Additional context:\n' + neutral + '\n\n', '', 1) == h['H1']
    assert h['H3'].replace('Additional evidence:\n' + case['first_hop_evidence']['text'] + '\n\n', '', 1) == h['H2']
    assert case['B'] in case['first_hop_evidence']['text']
    for level in LEVELS:
        base, injected = (build_prompt(case, level, condition) for condition in ('state_B', 'state_B_prime'))
        assert base.replace('Current Step 1 state:\n' + case['B'] + '\n\n',
                            'Current Step 1 state:\n' + case['B_prime'] + '\n\n', 1) == injected
        for condition in CONDITIONS:
            prompt = build_prompt(case, level, condition)
            assert not re.search(r'\b(correct|incorrect|oracle|injected|false|hallucinated)\b', prompt, re.I)
            assert '<' not in prompt and '>' not in prompt
    return dict(H0_two_downstream_facts_only=True, H1_task_frame_only=True,
                H2_added_text_no_entity_or_target_leak=True, H2_article_identity_matches=True,
                H3_explicit_first_hop=True, cumulative_context=True, paired_context_and_question_identical=True)


def classify(row):
    if not row['parse_valid']:
        return 'INVALID_OUTPUT', False
    if row['rejection']:
        return 'UNKNOWN_REJECT', False
    prime = row['condition'].endswith('_prime')
    expected = row['aliases_C_prime'] if prime else row['aliases_C']
    other = row['aliases_C'] if prime else row['aliases_C_prime']
    if matches(row['parsed_answer'], expected):
        return ('PROPAGATE' if row['condition'] == 'state_B_prime' else 'EXACT_CORRECT'), False
    if matches(row['parsed_answer'], other):
        return ('OVERRIDE_TO_GOLD' if row['condition'] == 'state_B_prime' else 'OTHER_CONTEXT_TARGET'), False
    # This is a provisional unsupported-answer diagnosis. Review real-entity
    # mismatches against context before making a factuality claim or interpreting.
    return 'OUT_OF_CONTEXT_HALLUCINATION', True


def analyze_level(records):
    groups = {condition: [r for r in records if r['condition'] == condition] for condition in CONDITIONS}
    indexed = {(r['case_id'], r['condition']): r for r in records}
    direct = groups['direct_B'] + groups['direct_B_prime']
    exact = lambda r: r['label'] in {'EXACT_CORRECT', 'PROPAGATE'}
    m = dict(CLA_B=fraction(sum(exact(r) for r in groups['direct_B']), len(groups['direct_B'])),
             CLA_B_prime=fraction(sum(exact(r) for r in groups['direct_B_prime']), len(groups['direct_B_prime'])),
             CLA=fraction(sum(exact(r) for r in direct), len(direct)),
             GSA=fraction(sum(exact(r) for r in groups['state_B']), len(groups['state_B'])),
             PR=fraction(sum(r['label']=='PROPAGATE' for r in groups['state_B_prime']), len(groups['state_B_prime'])),
             OR=fraction(sum(r['label']=='OVERRIDE_TO_GOLD' for r in groups['state_B_prime']), len(groups['state_B_prime'])),
             pending_review_n=sum(r['review_required'] for r in records),
             invalid_output=fraction(sum(r['label']=='INVALID_OUTPUT' for r in records), len(records)))
    for condition, key in (('state_B','SFIR_B'), ('state_B_prime','SFIR_B_prime')):
        controls = [r for r in groups[condition] if exact(indexed[r['case_id'], condition.replace('state','direct')])]
        m[key] = fraction(sum(not exact(r) for r in controls), len(controls))
    m['secondary_outcomes'] = {label: fraction(sum(r['label']==label for r in groups['state_B_prime']), len(groups['state_B_prime']))
                               for label in OUTCOMES[2:]}
    state = groups['state_B'] + groups['state_B_prime']
    m['unsupported_state_rate'] = fraction(sum(r['label']=='OUT_OF_CONTEXT_HALLUCINATION' for r in state), len(state))
    return m


def stop_reasons(level, metrics):
    if level == 'H3':
        return []
    reasons = []
    minimum_cla = POLICY['H0_min_CLA'] if level == 'H0' else POLICY['H1_H2_min_CLA']
    minimum_gsa = POLICY['H0_min_GSA'] if level == 'H0' else POLICY['H1_H2_min_GSA']
    if metrics['CLA']['rate'] < minimum_cla:
        reasons.append(level + ' context lookup below preregistered floor')
    if metrics['GSA']['rate'] < minimum_gsa:
        reasons.append(level + ' gold-state accuracy below preregistered floor')
    if level in ('H1','H2') and metrics['unsupported_state_rate']['rate'] > POLICY['max_unsupported_state_rate']:
        reasons.append(level + ' excessive unsupported state outputs; inspect before continuation')
    return reasons


def run(cases, adapter, out, seed=42):
    records, stopped = [], []
    with (out / 'trajectories.jsonl').open('x', encoding='utf-8') as stream:
        for level in LEVELS:
            controls = {}
            for condition in CONDITIONS:
                for case in cases:
                    prompt = build_prompt(case, level, condition)
                    result = adapter.generate(prompt, seed=seed, max_new_tokens=32)
                    row = case | result | parse_answer(result['raw_generation'], result.get('truncated',False))
                    row.update(context_level=level, condition=condition, prompt=prompt,
                               expected_answer=case['C_prime'] if condition.endswith('_prime') else case['C'],
                               seed=seed, prompt_sha256=hashlib.sha256(prompt.encode('utf-8')).hexdigest(),
                               raw_sha256=hashlib.sha256(result['raw_generation'].encode('utf-8')).hexdigest())
                    row['label'], row['review_required'] = classify(row)
                    exact = row['label'] in {'EXACT_CORRECT','PROPAGATE'}
                    if condition.startswith('direct'):
                        controls[case['case_id'],condition] = exact
                    row['direct_lookup_pass'] = exact if condition.startswith('direct') else controls[case['case_id'],condition.replace('state','direct')]
                    row['state_adherence_pass'] = exact if condition.startswith('state') else None
                    row['state_frame_interference'] = condition.startswith('state') and row['direct_lookup_pass'] and not exact
                    records.append(row)
                    stream.write(json.dumps(row,ensure_ascii=False)+'\n'); stream.flush()
                    print(json.dumps({k:row[k] for k in ('case_id','context_level','condition','raw_generation','label')},ensure_ascii=False),flush=True)
            stopped = stop_reasons(level,analyze_level([r for r in records if r['context_level']==level]))
            if stopped:
                break
    return records, stopped


def analyze(cases, records, stopped=()):
    idx = {(r['case_id'],r['context_level'],r['condition']):r for r in records}
    if len(idx)!=len(records):
        raise ValueError('Duplicate calls')
    completed = [level for level in LEVELS if any(r['context_level']==level for r in records)]
    for level in completed:
        if any((case['case_id'],level,c) not in idx for case in cases for c in CONDITIONS):
            raise ValueError('Incomplete context level')
    by_level = {level: analyze_level([r for r in records if r['context_level']==level]) for level in completed}
    for level, m in by_level.items():
        m['delta_PR_from_H0'] = m['PR']['rate'] - by_level['H0']['PR']['rate']
    interpretable = []
    if all(level in by_level for level in LEVELS[:3]):
        for case in cases:
            good = True
            for level in LEVELS[:3]:
                group = [idx[case['case_id'],level,c] for c in CONDITIONS]
                good &= all(r['label']=='EXACT_CORRECT' for r in group[:3]) and group[3]['parse_valid'] and not any(r['review_required'] for r in group)
            if good:
                interpretable.append(case['case_id'])
    invalid = sum(r['label']=='INVALID_OUTPUT' for r in records)
    placeholders = sum(bool(re.search(r'<[^>]+>|requested name or location',r['raw_generation'],re.I)) for r in records)
    checks = dict(complete_160_call_matrix=len(records)==160,
                  H0_CLA='H0' in by_level and by_level['H0']['CLA']['rate']>=POLICY['H0_min_CLA'],
                  H0_GSA='H0' in by_level and by_level['H0']['GSA']['rate']>=POLICY['H0_min_GSA'],
                  H0_H2_interpretable=len(interpretable)>=POLICY['min_interpretable_cases'],
                  H1_H2_CLA=all(h in by_level and by_level[h]['CLA']['rate']>=POLICY['H1_H2_min_CLA'] for h in ('H1','H2')),
                  H1_H2_GSA=all(h in by_level and by_level[h]['GSA']['rate']>=POLICY['H1_H2_min_GSA'] for h in ('H1','H2')),
                  invalid_rate=bool(records) and invalid/len(records)<=POLICY['max_invalid_rate'],
                  no_placeholder_contamination=placeholders==0,
                  no_unreviewed_mismatches=not any(r['review_required'] for r in records),
                  H3_controls='H3' in by_level and by_level['H3']['CLA']['rate']>=POLICY['H3_min_CLA'] and by_level['H3']['GSA']['rate']>=POLICY['H3_min_GSA'],
                  no_unsupported_collapse=all(by_level[h]['unsupported_state_rate']['rate']<=POLICY['max_unsupported_state_rate'] for h in completed))
    metrics = dict(cases=len(cases),calls=len(records),context_levels=by_level,interpretable_case_ids=interpretable,
                   invalid_output=fraction(invalid,len(records)),placeholder_copies=placeholders,
                   denominator_note='CLA-all uses 20 direct probes/level; GSA/PR/OR use the same ten cases at each completed level. No level-dependent filtering. SFIR conditions on a correct direct lookup for that entity. Context levels are repeated measurements.',
                   paired_outcomes=[dict(case_id=case['case_id'],**{h: idx[case['case_id'],h,'state_B_prime']['label'] if h in completed else None for h in LEVELS}) for case in cases])
    gate = dict(passed=all(checks.values()) and not stopped,quantitative_checks=checks,thresholds=POLICY,
                interpretable_cases=len(interpretable),stop_reasons=list(stopped),human_review_required=True,
                next_experiment_authorized=False,scale_authorized=False,semantic_review='pending',
                interpretation='Externally supplied alternative real-entity state under controlled context; not spontaneous hallucination')
    return metrics, gate


def export_results(out,cases,records,stopped=()):
    metrics,gate=analyze(cases,records,stopped)
    write_json(out/'metrics.json',metrics)
    with (out/'summary.csv').open('w',encoding='utf-8',newline='') as stream:
        writer=csv.writer(stream);writer.writerow(['context_level','metric','count','denominator','rate_or_delta'])
        for level,m in metrics['context_levels'].items():
            for key in ('CLA_B','CLA_B_prime','CLA','GSA','PR','OR','SFIR_B','SFIR_B_prime'):
                v=m[key];writer.writerow([level,key,v['count'],v['denominator'],v['rate']])
            writer.writerow([level,'delta_PR_from_H0','','',m['delta_PR_from_H0']])
            for key,v in m['secondary_outcomes'].items():
                writer.writerow([level,key,v['count'],v['denominator'],v['rate']])
    lines=['# v3.1 real-entity context ladder inspection',f"Smoke gate: {'PASS' if gate['passed'] else 'FAIL'}; calls: {len(records)}/160; stop for review.",
           '[Context construction audit](context_audit.md) was saved before inference. [Diagnosis](diagnosis.md) describes the interpretation.',
           'Labels on unrecognized values are provisional until evidence review. SFIR on B′ includes scientifically meaningful OVERRIDE_TO_GOLD; it is not an automatic gate failure. No particular H3 propagation rate is required.']
    idx={(r['case_id'],r['context_level'],r['condition']):r for r in records}
    for case in cases:
        lines+=['## '+case['case_id'],'```json\n'+json.dumps({k:case[k] for k in ('A','r1','B','relation','C','B_prime','C_prime')},ensure_ascii=False,indent=2)+'\n```',
                '| Context | CLA B | CLA B′ | state B | state B′ | Injected label |\n|---|---|---|---|---|---|']
        previous=None
        highlights=[]
        for h in LEVELS:
            if h not in metrics['context_levels']:
                lines[-1]+=f'\n| {h} | NOT RUN | NOT RUN | NOT RUN | NOT RUN | STOP |';continue
            rows=[idx[case['case_id'],h,c] for c in CONDITIONS]
            rendered=[r['raw_generation'].replace('\n',' / ').replace('|','\\|') for r in rows]
            lines[-1]+='\n| '+h+' | '+' | '.join(rendered)+' | '+rows[3]['label']+' |'
            if previous=='PROPAGATE' and rows[3]['label'] in {'OVERRIDE_TO_GOLD','OUT_OF_CONTEXT_HALLUCINATION'}:
                highlights.append(f"{h}: PROPAGATE → {rows[3]['label']}")
            for r in rows[2:]:
                if r['state_frame_interference']:
                    highlights.append(f"{h} {r['condition']}: direct-correct → state-wrong ({r['label']})")
            if not rows[2]['state_adherence_pass']:
                highlights.append(h+': gold-state failure')
            previous=rows[3]['label']
        lines.append('**Highlights:** '+('; '.join(highlights) if highlights else 'No outcome transitions, framing failures or gold-state failures.'))
        for h in LEVELS:
            if h not in metrics['context_levels']:continue
            for condition in CONDITIONS:
                r=idx[case['case_id'],h,condition]
                lines += [f'### {h} / {condition}', '**Exact prompt**\n\n```text\n'+r['prompt']+'\n```',
                          '**Raw response**\n\n```text\n'+r['raw_generation']+'\n```',
                          f"Label: {r['label']}; direct lookup pass: {r['direct_lookup_pass']}; state adherence pass: {r['state_adherence_pass']}; pending evidence review: {r['review_required']}."]
    (out/'inspection.md').write_text('\n\n'.join(lines),encoding='utf-8')
    gate.update(trajectories_sha256=digest(out/'trajectories.jsonl'),inspection_sha256=digest(out/'inspection.md'))
    write_json(out/'gate.json',gate)


def previous_hashes():
    return {str(p).replace('\\','/'):digest(p) for folder in ('smoke','smoke_v2','smoke_v2_1','smoke_v3')
            for p in (Path('results')/folder).rglob('*') if p.is_file()}


def prepare(out,data):
    if out.exists():raise FileExistsError('Refusing to overwrite v3.1 output directory')
    cases=read_jsonl(data)
    if len(cases)!=10 or len({c['case_id'] for c in cases})!=10:raise ValueError('Ten clean cases required')
    audits={c['case_id']:audit_case(c) for c in cases}
    out.mkdir(parents=True)
    lines=['# v3.1 pre-inference context construction audit',
           'Ten evidence-reviewed real cases; no model output used in selection. H2 checks apply to its added neutral sentence; controlled facts necessarily contain the two entities and targets. H3 alone adds the first-hop identity evidence. Every added sentence retains its exact source article and sentence index.',
           'Reference order is counterbalanced five/five across cases and fixed across levels. One neutral sentence per case. H3 cumulatively retains H2. No additional order variants are run (160-call design).']
    for c in cases:
        lines+=['## '+c['case_id'],'```json\n'+json.dumps({k:c[k] for k in ('A','r1','B','relation','C','B_prime','C_prime')},ensure_ascii=False,indent=2)+'\n```',
                'Checks: '+json.dumps(audits[c['case_id']]),
                '### Source evidence and alias decisions','```json\n'+json.dumps({k:c[k] for k in ('source_id','donor_id','first_hop_evidence','downstream_evidence','donor_first_hop_evidence','donor_downstream_evidence','neutral_evidence','aliases_C','aliases_C_prime')},ensure_ascii=False,indent=2)+'\n```']
        for h in LEVELS:lines += ['### '+h,'```text\n'+context_block(c,h)+'\n```']
    (out/'context_audit.md').write_text('\n\n'.join(lines),encoding='utf-8')
    write_json(out/'prior_artifact_hashes.json',previous_hashes())
    write_json(out/'preparation.json',dict(candidates_sha256=digest(data),context_audit_sha256=digest(out/'context_audit.md'),
               source_sha256=digest(__file__),policy=POLICY,audits=audits,inference_started=False))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['prepare','run'])
    parser.add_argument('--data',default='data/candidates_v3_1.jsonl')
    parser.add_argument('--output',default='results/smoke_v3_1')
    parser.add_argument('--cache-dir',default='.cache/huggingface')
    args=parser.parse_args();out=Path(args.output)
    if args.action=='prepare':prepare(out,args.data);return
    if (out/'manifest.json').exists() or (out/'trajectories.jsonl').exists():parser.error('Refusing existing run overwrite/resume')
    prep=json.loads((out/'preparation.json').read_text(encoding='utf-8'))
    review=json.loads((out/'audit_review.json').read_text(encoding='utf-8'))
    if prep['candidates_sha256']!=digest(args.data) or prep['source_sha256']!=digest(__file__) or prep['policy']!=POLICY:parser.error('Prepared inputs/code/policy changed')
    if not review.get('passed') or review['context_audit_sha256']!=digest(out/'context_audit.md') or prep['context_audit_sha256']!=review['context_audit_sha256']:parser.error('Pre-inference audit not reviewed')
    cases=read_jsonl(args.data)
    for c in cases:audit_case(c)
    load_path=Path('results/smoke_v2/load_nf4.json');load=json.loads(load_path.read_text(encoding='utf-8'));validate_load_test(load)
    manifest=dict(version='3.1',seed=42,model_name=MODEL,model_revision=load['revision'],candidates_sha256=digest(args.data),
                  context_audit_sha256=digest(out/'context_audit.md'),load_test_sha256=digest(load_path),policy=POLICY,
                  generation_config=dict(do_sample=False,temperature=0,temperature_argument=None,max_new_tokens=32,use_cache=False,enable_thinking=False),
                  decoding_note='HF temperature sampling disabled (None) under deterministic greedy decoding.',
                  source_code_sha256={name:digest(Path(__file__).parent/name) for name in ('experiment_v3_1.py','prepare_v3_1.py','experiment_v3.py','experiment_v2.py','common.py','generation/local_hf_adapter.py')},
                  call_order='H0 to H3; all direct B, then direct B prime, then state B, then state B prime at each level',
                  no_cross_call_history=True,no_cross_call_kv_cache=True)
    write_json(out/'manifest.json',manifest);adapter=None
    try:
        adapter=IndependentHFAdapter('4bit-nf4',args.cache_dir,load['revision'])
        manifest.update(quantization=adapter.quantization,compute_dtype=adapter.compute_dtype,cpu_offload=adapter.offload,device_map=adapter.device_map)
        write_json(out/'manifest.json',manifest)
        records,stopped=run(cases,adapter,out)
        export_results(out,cases,records,stopped)
    except Exception:
        write_json(out/'failure.json',dict(error=traceback.format_exc()))
        write_json(out/'gate.json',dict(passed=False,scale_authorized=False,reason='Runtime failure'))
        raise
    finally:
        if adapter:write_json(out/'memory.json',adapter.memory())
        prior=json.loads((out/'prior_artifact_hashes.json').read_text(encoding='utf-8'))
        changed=[p for p,s in prior.items() if not Path(p).exists() or digest(p)!=s]
        write_json(out/'preservation_check.json',dict(passed=not changed,files_checked=len(prior),changed=changed))
        if changed:raise RuntimeError('Historical artifacts changed')


if __name__=='__main__':main()
