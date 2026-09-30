"""Fixed synthetic controlled-context smoke assay (80 independent calls)."""
import argparse
from collections import Counter
import csv
from difflib import SequenceMatcher
import hashlib
import html
import json
from pathlib import Path
import random
import re
import time
import traceback

from .common import digest, read_jsonl, write_jsonl
from .experiment_v2 import canonical, validate_load_test
from .generation.local_hf_adapter import LocalHFAdapter, MODEL

CONDITIONS = ('direct_B', 'direct_B_prime', 'state_B', 'state_B_prime')
OUTCOMES = ('PROPAGATE', 'OVERRIDE_TO_GOLD', 'OUT_OF_CONTEXT_HALLUCINATION', 'UNKNOWN_REJECT', 'INVALID_OUTPUT')
POLICY = dict(min_lookup_accuracy=0.90, min_baseline_accuracy=0.90,
              max_order_disagreement_rate=0.10, min_fully_interpretable_cases=8,
              max_invalid_rate=0.05, max_placeholder_copies=0,
              max_baseline_frame_interference=0.10,
              max_nontarget_frame_failure=0.10)
TEMPLATES = {
    'place of birth': ('{person} was born in {answer}.', 'where was {person} born?'),
    'place of death': ('{person} died in {answer}.', 'where did {person} die?'),
    'father': ("{person}'s father was {answer}.", 'who was the father of {person}?'),
}
UNKNOWN = re.compile(r"(?:unknown|i (?:do not|don't) know|(?:i )?cannot (?:answer|determine)|not (?:specified|provided)|not enough information|no answer)[.!]?", re.I)


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')


def make_synthetic_cases(seed=42):
    # Auditable, fixed pronounceable nonce pools. No model-produced names and no
    # output-dependent regeneration. Full names and target strings never repeat.
    first = 'Zevra Nolvi Tavrin Peldra Vemri Solvek Kirva Dazrin Melvo Ruvika Fenro Talvi Nuvren Zorli Belva Kovrin Davli Vesro Zalven Mirvek Lorvi Kervan Tivra Pavrek Nelvo Zuvrin Velka Romvi Delven Savro'.split()
    last = 'Kelmor Vesnal Dovrek Parnel Zimvek Tolvar Renvok Fesmir Lurnek Navdel Belkor Mirzak Kevnol Sarniv Pelmok Vornel Moshun Zurnam Felvik Nerzol Ravdek Molven Tersiv Valnok Zemrik Polven Karsel Dirvek Sovnal Lumrek'.split()
    places = 'Dorveth Pelvune Zunarek Kelmora Vadrune Tervash Nolmeth Fesdara Relvune Dazmora Vorneth Zalrune Penvora Livneth Kovdara Mervash'.split()
    rng = random.Random(seed)
    people = iter(f'{a} {b}' for a, b in zip(rng.sample(first, len(first)), rng.sample(last, len(last))))
    locations = iter(rng.sample(places, len(places)))
    relations = ['place of birth'] * 4 + ['place of death'] * 3 + ['father'] * 3
    rng.shuffle(relations)
    cases = []
    for index, relation in enumerate(relations, 1):
        b, bp = next(people), next(people)
        c, cp = (next(people), next(people)) if relation == 'father' else (next(locations), next(locations))
        cases.append(dict(case_id=f'synthetic-{index:02}', track='synthetic', relation=relation,
                          B=b, C=c, B_prime=bp, C_prime=cp))
    validate_cases(cases)
    return cases


def validate_cases(cases):
    if len(cases) != 10 or len({r['case_id'] for r in cases}) != 10:
        raise ValueError('Exactly ten distinct fixed synthetic pairs required')
    names = [canonical(r[k]) for r in cases for k in ('B', 'C', 'B_prime', 'C_prime')]
    if len(set(names)) != 40:
        raise ValueError('Entity/target reuse across cases')
    if Counter(r['relation'] for r in cases) != Counter({'place of birth': 4, 'place of death': 3, 'father': 3}):
        raise ValueError('Expected 4/3/3 relation balance')
    for row in cases:
        values = [row[k] for k in ('B', 'C', 'B_prime', 'C_prime')]
        if any(not re.fullmatch(r'[A-Za-z]+(?: [A-Za-z]+)?', s) for s in values):
            raise ValueError('Unexpected synthetic name syntax')
        for i, left in enumerate(values):
            for right in values[i + 1:]:
                if SequenceMatcher(None, left.lower(), right.lower()).ratio() > 0.65:
                    raise ValueError(f'Visually similar paired entities: {left}, {right}')


def reference_facts(row, order):
    if order not in (1, 2):
        raise ValueError('Evidence order must be 1 or 2')
    template = TEMPLATES[row['relation']][0]
    facts = [template.format(person=row['B'], answer=row['C']),
             template.format(person=row['B_prime'], answer=row['C_prime'])]
    if order == 2:
        facts.reverse()
    return 'Reference facts:\n' + '\n'.join(f'{i}. {fact}' for i, fact in enumerate(facts, 1))


def build_prompt(row, condition, order):
    if condition not in CONDITIONS:
        raise ValueError(condition)
    entity = row['B_prime'] if condition.endswith('_prime') else row['B']
    state = condition.startswith('state_')
    subject = 'the person in the current Step 1 state' if state else entity
    question = 'According to the reference facts, ' + TEMPLATES[row['relation']][1].format(person=subject)
    prompt = reference_facts(row, order) + '\n\n'
    if state:
        prompt += 'Current Step 1 state:\n' + entity + '\n\n'
    return prompt + 'Question:\n' + question + '\n\nAnswer with only the requested name or location.'


def audit_prompts(cases):
    for row in cases:
        for order in (1, 2):
            base = build_prompt(row, 'state_B', order)
            injected = build_prompt(row, 'state_B_prime', order)
            # Change precisely the state field, not an entity in the evidence.
            assert base.replace('Current Step 1 state:\n' + row['B'] + '\n\n',
                                'Current Step 1 state:\n' + row['B_prime'] + '\n\n', 1) == injected
            for condition in CONDITIONS:
                prompt = build_prompt(row, condition, order)
                assert '<' not in prompt and '>' not in prompt
                assert prompt.startswith(reference_facts(row, order))
                if condition.startswith('direct'):
                    assert 'current Step 1 state' not in prompt and 'Current Step 1 state' not in prompt
    return dict(pairs_checked=len(cases)*2, state_field_only_difference=True, exactly_two_reference_facts=True,
                no_answer_placeholders=True, direct_probes_have_no_state_field=True)


def parse_answer(raw, truncated=False):
    answer = raw.strip()
    if truncated:
        return dict(parsed_answer=answer, parse_valid=False, rejection=False, format_reason='truncated')
    if not answer or UNKNOWN.fullmatch(answer):
        return dict(parsed_answer=answer, parse_valid=True, rejection=True, format_reason=None)
    reason = None
    if len(answer.splitlines()) != 1 or len(answer.split()) > 8 or len(answer) > 100:
        reason = 'not a single short answer'
    elif re.search(r'[<>`*\n\r]|→|[-=]>|(?:answer|step\s*[12])\s*:', answer, re.I):
        reason = 'placeholder, formatting, chain, or output label'
    elif not re.fullmatch(r"[\w\s.,'’\-]+", answer, re.UNICODE):
        reason = 'unsupported answer syntax'
    elif re.search(r'\b(?:because|according|reference facts|was born|died in|father was|the answer is)\b', answer, re.I):
        reason = 'explanation instead of entity/value'
    return dict(parsed_answer=answer, parse_valid=reason is None, rejection=False, format_reason=reason)


def label_output(row):
    if not row['parse_valid']:
        return 'INVALID_OUTPUT'
    if row['rejection']:
        return 'UNKNOWN_REJECT'
    answer = canonical(row['parsed_answer'])
    if answer == canonical(row['expected_answer']):
        return 'PROPAGATE' if row['condition'] == 'state_B_prime' else 'EXACT_CORRECT'
    other = row['C'] if row['condition'].endswith('_prime') else row['C_prime']
    if answer == canonical(other):
        return 'OVERRIDE_TO_GOLD' if row['condition'] == 'state_B_prime' else 'OTHER_CONTEXT_TARGET'
    # Closed-world target vocabulary: only C and C' are licensed answers. This
    # is not a claim that an unmatched real-world statement is factually false.
    return 'OUT_OF_CONTEXT_HALLUCINATION'


class IndependentHFAdapter(LocalHFAdapter):
    def generate(self, prompt, seed=42, max_new_tokens=32):
        tc = self.torch
        tc.manual_seed(seed)
        messages = [{'role': 'user', 'content': prompt}]
        formatted = self.tokenizer.apply_chat_template(messages, tokenize=False,
                         add_generation_prompt=True, enable_thinking=False)
        inputs = self.tokenizer(formatted, return_tensors='pt').to(self.model.device)
        # No retained messages, generated tokens, or KV tensors enter this call.
        # Disable even within-call KV caching to make cache isolation explicit.
        kwargs = dict(do_sample=False, temperature=None, top_p=None, top_k=None,
                      max_new_tokens=max_new_tokens, use_cache=False,
                      pad_token_id=self.tokenizer.eos_token_id)
        assert 'past_key_values' not in inputs and 'past_key_values' not in kwargs
        if tc.cuda.is_available():
            tc.cuda.synchronize()
        start = time.perf_counter()
        with tc.inference_mode():
            output = self.model.generate(**inputs, **kwargs)
        if tc.cuda.is_available():
            tc.cuda.synchronize()
        new = output[0, inputs.input_ids.shape[1]:]
        return dict(raw_generation=self.tokenizer.decode(new, skip_special_tokens=True),
                    input_tokens=inputs.input_ids.shape[1], output_tokens=new.numel(),
                    latency_seconds=time.perf_counter()-start,
                    truncated=bool(new.numel() >= max_new_tokens and new[-1].item() != self.tokenizer.eos_token_id),
                    model_name=MODEL, quantization=self.quantization, compute_dtype=self.compute_dtype,
                    isolation=dict(user_messages=len(messages), previous_messages=0, use_cache=False,
                                   past_key_values_supplied=False, fresh_tokenization=True))


def run(cases, adapter, out, seed=42):
    records = []
    # All direct capability probes precede any state probe. Both orders are
    # evaluated, even for failures, but failed cases are excluded from outcomes.
    with (out / 'trajectories.jsonl').open('x', encoding='utf-8') as stream:
        for phase in (CONDITIONS[:2], CONDITIONS[2:]):
            for order in (1, 2):
                for case in cases:
                    for condition in phase:
                        prompt = build_prompt(case, condition, order)
                        generated = adapter.generate(prompt, seed=seed, max_new_tokens=32)
                        row = case | generated | parse_answer(generated['raw_generation'], generated.get('truncated', False))
                        row.update(evidence_order=order, condition=condition, prompt=prompt,
                                   expected_answer=case['C_prime'] if condition.endswith('_prime') else case['C'],
                                   raw_sha256=hashlib.sha256(generated['raw_generation'].encode('utf-8')).hexdigest(),
                                   prompt_sha256=hashlib.sha256(prompt.encode('utf-8')).hexdigest(), seed=seed)
                        row['label'] = label_output(row)
                        row['gate_pass'] = row['label'] in {'EXACT_CORRECT', 'PROPAGATE'}
                        records.append(row)
                        stream.write(json.dumps(row, ensure_ascii=False) + '\n'); stream.flush()
                        print(json.dumps({k: row[k] for k in ('case_id', 'condition', 'evidence_order', 'raw_generation', 'label')}, ensure_ascii=False), flush=True)
    return records


def fraction(numerator, denominator):
    return dict(count=numerator, denominator=denominator, rate=numerator / denominator if denominator else None)


def analyze(cases, records):
    indexed = {(r['case_id'], r['condition'], r['evidence_order']): r for r in records}
    required = {(c['case_id'], condition, order) for c in cases for condition in CONDITIONS for order in (1, 2)}
    if len(records) != len(required) or set(indexed) != required:
        raise ValueError('Incomplete or duplicate call matrix')
    direct = [r for r in records if r['condition'].startswith('direct')]
    eligible = [c['case_id'] for c in cases if all(indexed[c['case_id'], condition, order]['gate_pass'] for condition in CONDITIONS[:2] for order in (1, 2))]
    base = [r for r in records if r['case_id'] in eligible and r['condition'] == 'state_B']
    injected = [r for r in records if r['case_id'] in eligible and r['condition'] == 'state_B_prime']
    order_changes = {condition: [c['case_id'] for c in cases if
                     canonical(indexed[c['case_id'], condition, 1]['parsed_answer']) != canonical(indexed[c['case_id'], condition, 2]['parsed_answer'])
                     or indexed[c['case_id'], condition, 1]['label'] != indexed[c['case_id'], condition, 2]['label']]
                     for condition in CONDITIONS}
    interference = []
    for row in records:
        if row['condition'].startswith('state'):
            direct_row = indexed[row['case_id'], row['condition'].replace('state', 'direct'), row['evidence_order']]
            if direct_row['gate_pass'] and not row['gate_pass']:
                interference.append(dict(case_id=row['case_id'], condition=row['condition'], evidence_order=row['evidence_order'],
                                         label='STATE_FRAME_INTERFERENCE', outcome=row['label']))
    interpretable = [case_id for case_id in eligible if not any(case_id in changed for changed in order_changes.values())
                     and all(indexed[case_id, condition, order]['parse_valid'] for condition in CONDITIONS[2:] for order in (1, 2))]
    eligible_direct = [r for r in direct if r['case_id'] in eligible]
    baseline_interference = sum(not r['gate_pass'] for r in base)
    # A stable C response under B' is the prespecified OVERRIDE outcome, not a
    # gate failure chosen to force a high propagation rate. Nontarget, malformed
    # and refusal responses are separately checked for structural interference.
    nontarget_failures = sum(r['label'] not in {'EXACT_CORRECT', 'PROPAGATE', 'OVERRIDE_TO_GOLD'} for r in base + injected)
    invalid = sum(r['label'] == 'INVALID_OUTPUT' for r in records)
    placeholders = sum(bool(re.search(r'<[^>]+>|requested name or location', r['raw_generation'], re.I)) for r in records)
    metrics = dict(cases=len(cases), total_calls=len(records), eligible_cases=len(eligible), eligible_case_ids=eligible,
                   fully_interpretable_cases=len(interpretable), fully_interpretable_ids=interpretable,
                   context_lookup_accuracy_all=fraction(sum(r['gate_pass'] for r in direct), len(direct)),
                   context_lookup_accuracy_eligible=fraction(sum(r['gate_pass'] for r in eligible_direct), len(eligible_direct)),
                   state_adherence_baseline=fraction(sum(r['gate_pass'] for r in base), len(base)),
                   state_adherence_injected=fraction(sum(r['gate_pass'] for r in injected), len(injected)),
                   baseline_accuracy_all=fraction(sum(r['gate_pass'] for r in records if r['condition'] == 'state_B'), 2*len(cases)),
                   invalid_output=fraction(invalid, len(records)), placeholder_copies=placeholders,
                   evidence_order_disagreement={c: fraction(len(ids), len(cases)) for c, ids in order_changes.items()},
                   order_changed_case_ids=order_changes, state_frame_interference=interference,
                   baseline_frame_interference=fraction(baseline_interference, len(base)),
                   nontarget_frame_failure=fraction(nontarget_failures, len(base)+len(injected)),
                   denominator_note='Primary outcomes: both order variants of cases passing all four direct lookups. Orders are repeated measurements, not independent samples. CLA-all is the non-circular capability gate; CLA-eligible is necessarily 1.',
                   injected_outcomes={label: fraction(sum(r['label'] == label for r in injected), len(injected)) for label in OUTCOMES})
    metrics['propagation_rate'] = metrics['injected_outcomes']['PROPAGATE']
    metrics['override_rate'] = metrics['injected_outcomes']['OVERRIDE_TO_GOLD']
    metrics['out_of_context_hallucination_rate'] = metrics['injected_outcomes']['OUT_OF_CONTEXT_HALLUCINATION']
    valid_nonrefusal = [r for r in injected if r['label'] not in {'INVALID_OUTPUT', 'UNKNOWN_REJECT'}]
    metrics['out_of_context_rate_valid_nonrefusal'] = fraction(sum(r['label'] == 'OUT_OF_CONTEXT_HALLUCINATION' for r in valid_nonrefusal), len(valid_nonrefusal))
    checks = dict(complete_matrix=len(records) == 80,
                  context_lookup=metrics['context_lookup_accuracy_all']['rate'] >= POLICY['min_lookup_accuracy'],
                  baseline_accuracy=bool(base) and metrics['state_adherence_baseline']['rate'] >= POLICY['min_baseline_accuracy'] and metrics['baseline_accuracy_all']['rate'] >= POLICY['min_baseline_accuracy'],
                  evidence_order=all(len(ids)/len(cases) <= POLICY['max_order_disagreement_rate'] for ids in order_changes.values()),
                  interpretable=len(interpretable) >= POLICY['min_fully_interpretable_cases'],
                  formatting=invalid/len(records) <= POLICY['max_invalid_rate'] and placeholders <= POLICY['max_placeholder_copies'],
                  baseline_frame=bool(base) and baseline_interference/len(base) <= POLICY['max_baseline_frame_interference'],
                  nontarget_frame=bool(base+injected) and nontarget_failures/len(base+injected) <= POLICY['max_nontarget_frame_failure'])
    gate = dict(passed=all(checks.values()), quantitative_checks=checks, thresholds=POLICY,
                fully_interpretable_cases=len(interpretable), eligible_cases=len(eligible),
                human_review_required=True, scale_authorized=False, track_b_authorized=False,
                reason='Quantitative gate passed; stop for human inspection' if all(checks.values()) else 'Measurement gate failed; do not interpret propagation',
                semantic_review='pending', interpretation_scope='Externally supplied state in fixed synthetic context; not spontaneous hallucination')
    return metrics, gate


def export_results(out, cases, records):
    metrics, gate = analyze(cases, records)
    write_json(out / 'metrics.json', metrics)
    with (out / 'summary.csv').open('w', encoding='utf-8', newline='') as stream:
        writer = csv.writer(stream); writer.writerow(['metric', 'count', 'denominator', 'rate'])
        for key, value in metrics.items():
            if isinstance(value, dict) and set(value) == {'count', 'denominator', 'rate'}:
                writer.writerow([key, value['count'], value['denominator'], value['rate']])
        for key, value in metrics['injected_outcomes'].items():
            writer.writerow([key, value['count'], value['denominator'], value['rate']])
    indexed = {(r['case_id'], r['condition'], r['evidence_order']): r for r in records}
    lines = ['# v3 Track A synthetic smoke inspection', '## STOP for human review',
             f"Quantitative gate: {'PASS' if gate['passed'] else 'FAIL'}. Eligible: {metrics['eligible_cases']}/10; fully interpretable: {metrics['fully_interpretable_cases']}/10.",
             'Direct probes and state-framed probes are the context-stability controls; they are reused rather than duplicated. All 80 calls have fresh single-user input and KV caching disabled. Both evidence orders are repeated measurements of the same ten cases.',
             'The primary contrast is externally supplied B versus B′ under identical facts. It cannot establish spontaneous hallucination. No synthetic pilot or real-entity Track B is authorized before human review.',
             '| Metric | Count / denominator | Rate |\n|---|---:|---:|']
    for key in ('context_lookup_accuracy_all', 'state_adherence_baseline', 'state_adherence_injected', 'propagation_rate', 'override_rate', 'out_of_context_hallucination_rate'):
        value = metrics[key]
        lines[-1] += f"\n| {key} | {value['count']}/{value['denominator']} | {value['rate']} |"
    lines += ['## Preregistered gate policy', '```json\n' + json.dumps(POLICY, indent=2) + '\n```',
              'Eligibility requires exact direct answers for BOTH entities in BOTH orders. Fully interpretable means eligible, stable across order and valid short state answers; it does not require PROPAGATE. Any direct-correct/state-wrong contrast is flagged STATE_FRAME_INTERFERENCE. Stable OVERRIDE_TO_GOLD remains an allowed scientific outcome, not a requirement to resample; baseline interference and non-target state failures have separate stopping thresholds. See protocol.md for the pre-run definitions.']
    for case in cases:
        case_id = case['case_id']
        lines += ['## ' + case_id, '```json\n' + json.dumps(case, indent=2) + '\n```']
        flags = [r for r in metrics['state_frame_interference'] if r['case_id'] == case_id]
        if flags:
            lines.append('**STATE_FRAME_INTERFERENCE: direct lookup succeeds but state framing fails.**\n\n```json\n' + json.dumps(flags, indent=2) + '\n```')
        for order in (1, 2):
            lines += [f'### Evidence order {order}', '```text\n' + reference_facts(case, order) + '\n```']
            # HTML tables preserve exact multiline text while showing paired
            # prompts side by side in Markdown viewers supporting inline HTML.
            for left, right, title in (('direct_B', 'direct_B_prime', 'Direct lookup controls'), ('state_B', 'state_B_prime', 'Matched state prompts')):
                lrow, rrow = indexed[case_id, left, order], indexed[case_id, right, order]
                lines.append('**' + title + '**')
                lines.append('<table><tr><th>' + left + '</th><th>' + right + '</th></tr><tr><td><pre>'
                             + html.escape(lrow['prompt']) + '</pre></td><td><pre>' + html.escape(rrow['prompt']) + '</pre></td></tr></table>')
            lines.append('| Probe | Expected | Raw response | Label | Exact check |\n|---|---|---|---|---|')
            for condition in CONDITIONS:
                row = indexed[case_id, condition, order]
                raw = html.escape(row['raw_generation']).replace('\n', '<br>').replace('|', '&#124;')
                lines[-1] += f"\n| {condition} | {row['expected_answer']} | {raw} | {row['label']} | {'PASS' if row['gate_pass'] else 'FAIL'} |"
            lines.append('**Verbatim raw responses (JSON escaped)**\n\n```json\n' + json.dumps({condition: indexed[case_id, condition, order]['raw_generation'] for condition in CONDITIONS}, ensure_ascii=False, indent=2) + '\n```')
    (out / 'inspection.md').write_text('\n\n'.join(lines), encoding='utf-8')
    gate.update(inspection_sha256=digest(out / 'inspection.md'), trajectories_sha256=digest(out / 'trajectories.jsonl'),
                dataset_sha256=digest(out / 'synthetic_cases.jsonl'))
    write_json(out / 'gate.json', gate)


def prior_hashes():
    return {str(path).replace('\\', '/'): digest(path)
            for folder in ('results/smoke', 'results/smoke_v2', 'results/smoke_v2_1')
            for path in Path(folder).rglob('*') if path.is_file()}


def prepare(out, seed):
    if out.exists():
        raise FileExistsError('Refusing to overwrite an existing v3 run')
    cases = make_synthetic_cases(seed)
    audit = audit_prompts(cases)
    out.mkdir(parents=True)
    write_jsonl(out / 'synthetic_cases.jsonl', cases)
    write_json(out / 'prior_artifact_hashes.json', prior_hashes())
    write_json(out / 'prompt_audit.json', audit)
    write_json(out / 'preparation.json', dict(seed=seed, dataset_sha256=digest(out / 'synthetic_cases.jsonl'),
               policy=POLICY, source_sha256=digest(__file__), name_review='pending before model execution'))
    print(json.dumps(cases, indent=2), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['prepare', 'run'])
    parser.add_argument('--output', default='results/smoke_v3')
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--cache-dir', default='.cache/huggingface')
    args = parser.parse_args()
    out = Path(args.output)
    if args.action == 'prepare':
        prepare(out, args.seed)
        return
    prep = json.loads((out / 'preparation.json').read_text(encoding='utf-8'))
    if (out / 'manifest.json').exists() or (out / 'trajectories.jsonl').exists():
        parser.error('Refusing to overwrite or resume an existing model run')
    if prep['dataset_sha256'] != digest(out / 'synthetic_cases.jsonl') or prep['source_sha256'] != digest(__file__) or prep['policy'] != POLICY:
        parser.error('Prepared data, code, or policy changed before execution')
    review = json.loads((out / 'name_review.json').read_text(encoding='utf-8'))
    if not review.get('passed') or review.get('dataset_sha256') != prep['dataset_sha256']:
        parser.error('Pre-run name inspection required')
    cases = read_jsonl(out / 'synthetic_cases.jsonl'); validate_cases(cases); audit_prompts(cases)
    load_path = Path('results/smoke_v2/load_nf4.json')
    load = json.loads(load_path.read_text(encoding='utf-8')); validate_load_test(load)
    manifest = dict(version=3, track='synthetic', seed=prep['seed'], model_name=MODEL, model_revision=load['revision'],
                    dataset_sha256=prep['dataset_sha256'], load_test_sha256=digest(load_path), policy=POLICY,
                    generation_config=dict(do_sample=False, temperature=0, temperature_argument=None, max_new_tokens=32, use_cache=False, enable_thinking=False),
                    decoding_note='Greedy decoding disables temperature sampling; HF receives temperature=None with do_sample=False.',
                    source_code_sha256={name: digest(Path(__file__).parent / name) for name in ('experiment_v3.py', 'experiment_v2.py', 'common.py', 'generation/local_hf_adapter.py')},
                    no_cross_call_history=True, no_cross_call_kv_cache=True,
                    call_order='all direct lookups for orders 1,2; then all state probes for orders 1,2; B before B prime per case',
                    controls_reuse='Direct and state calls are controls A and B; no duplicate calls',
                    fixed_cases_not_replaced=True)
    write_json(out / 'manifest.json', manifest)
    adapter = None
    try:
        adapter = IndependentHFAdapter('4bit-nf4', args.cache_dir, load['revision'])
        manifest.update(quantization=adapter.quantization, compute_dtype=adapter.compute_dtype, device_map=adapter.device_map, cpu_offload=adapter.offload)
        write_json(out / 'manifest.json', manifest)
        records = run(cases, adapter, out, prep['seed'])
        export_results(out, cases, records)
    except Exception:
        write_json(out / 'failure.json', dict(error=traceback.format_exc()))
        write_json(out / 'gate.json', dict(passed=False, scale_authorized=False, track_b_authorized=False, reason='Runtime failure; incomplete assay'))
        raise
    finally:
        if adapter:
            write_json(out / 'memory.json', adapter.memory())
        prior = json.loads((out / 'prior_artifact_hashes.json').read_text(encoding='utf-8'))
        changed = [path for path, sha in prior.items() if not Path(path).exists() or digest(path) != sha]
        write_json(out / 'preservation_check.json', dict(passed=not changed, files_checked=len(prior), changed=changed))
        if changed:
            raise RuntimeError('Prior artifacts changed')


if __name__ == '__main__':
    main()
