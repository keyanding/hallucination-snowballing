"""Natural first-hop checkpoints and matched, isolated downstream branches."""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import time
import traceback

from .common import digest, read_jsonl, write_jsonl
from .experiment_v2 import canonical, matches, validate_load_test
from .experiment_v3 import IndependentHFAdapter, TEMPLATES, fraction, parse_answer, reference_facts, write_json
from .experiment_v3_1 import classify
from .generation.local_hf_adapter import MODEL

OUT = Path('results/smoke_v3_3')
DATA = Path('data/candidates_v3_3.jsonl')
INDEX = Path('data/evidence_index_v3_3.json')
EVIDENCE = ('E0', 'E1', 'E2', 'E3a', 'E3b')
POLICY = dict(min_CLA=0.90, min_valid_cases=8, max_unsupported_invalid=0.10,
              max_bad_first_hop_format=0.25, stop_unsupported_majority=0.50,
              missing_natural_evidence='stop affected natural branch; registered counterfactual fallback',
              seed=42, max_new_tokens=32)
SOURCES = ('experiment_v3_3.py', 'prepare_v3_3.py', 'experiment_v3.py',
           'experiment_v3_1.py', 'experiment_v2.py', 'generation/local_hf_adapter.py')


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def first_prompt(case):
    return (f'Question:\n{case["original_question"]}\n\nFirst solve only the first step:\n'
            f'Who directed "{case["A"]}"?\n\nAnswer with only the person\'s name.')


def state_span(raw):
    parsed = parse_answer(raw)
    if not parsed['parse_valid'] or parsed['rejection']:
        raise ValueError('No reliable first-hop entity span')
    return len(raw) - len(raw.lstrip()), len(raw.rstrip())


def replace_state(raw, state):
    start, end = state_span(raw)
    return raw[:start] + state + raw[end:]


def evidence(case, condition):
    gold = f'"{case["A"]}" was directed by {case["B"]}.'
    wrong = f'"{case["A"]}" was directed by {case["B_prime"]}.'
    return {'E0': '', 'E1': gold, 'E2': wrong,
            'E3a': gold + '\n' + wrong, 'E3b': wrong + '\n' + gold}[condition]


def continuation(case, condition):
    # All branches receive identical downstream facts after the checkpoint.
    extra = evidence(case, condition)
    question = TEMPLATES[case['relation']][1].format(person='that person')
    return (reference_facts(case, case['evidence_order']) + '\n\n'
            + ('Additional evidence:\n' + extra + '\n\n' if extra else '')
            + 'Now continue to the second step.\n\nUsing the first-step result above, answer:\n'
            + question + '\n\nAnswer with only the requested name or location.')


def branch_messages(case, raw, state, condition):
    return [dict(role='user', content=first_prompt(case)),
            dict(role='assistant', content=raw if state is None else replace_state(raw, state)),
            dict(role='user', content=continuation(case, condition))]


def control_prompt(case, state, stripped=False):
    facts = reference_facts(case, case['evidence_order'])
    subject = 'the person in the current Step 1 state' if stripped else state
    question = TEMPLATES[case['relation']][1].format(person=subject)
    return (facts + '\n\n' + ('Current Step 1 state:\n' + state + '\n\n' if stripped else '')
            + 'According to the reference facts, ' + question
            + '\n\nAnswer with only the requested name or location.')


def audit_pair(case, raw):
    start, end = state_span(raw)
    for state in (case['B'], case['B_prime']):
        changed = replace_state(raw, state)
        assert changed[:start] == raw[:start]
        assert changed[start + len(state):] == raw[end:]
    for condition in EVIDENCE:
        left = branch_messages(case, raw, case['B'], condition)
        right = branch_messages(case, raw, case['B_prime'], condition)
        assert left[0] == right[0] and left[2] == right[2]
        base = continuation(case, condition)
        if evidence(case, condition):
            base = base.replace('Additional evidence:\n' + evidence(case, condition) + '\n\n', '', 1)
        assert base == continuation(case, 'E0')
    assert evidence(case, 'E2') == evidence(case, 'E1').replace(
        ' was directed by ' + case['B'] + '.', ' was directed by ' + case['B_prime'] + '.')
    assert evidence(case, 'E3a').splitlines() == list(reversed(evidence(case, 'E3b').splitlines()))
    return True


class BranchAdapter(IndependentHFAdapter):
    def render(self, messages, generation=True):
        return self.tokenizer.apply_chat_template(messages, tokenize=False,
                                                 add_generation_prompt=generation, enable_thinking=False)

    def generate_messages(self, messages):
        tc = self.torch
        tc.manual_seed(POLICY['seed'])
        formatted = self.render(messages)
        inputs = self.tokenizer(formatted, return_tensors='pt').to(self.model.device)
        kwargs = dict(do_sample=False, temperature=None, top_p=None, top_k=None,
                      max_new_tokens=POLICY['max_new_tokens'], use_cache=False,
                      pad_token_id=self.tokenizer.eos_token_id)
        assert 'past_key_values' not in inputs and 'past_key_values' not in kwargs
        if tc.cuda.is_available():
            tc.cuda.synchronize()
        start = time.perf_counter()
        with tc.inference_mode():
            generated = self.model.generate(**inputs, **kwargs)
        if tc.cuda.is_available():
            tc.cuda.synchronize()
        new = generated[0, inputs.input_ids.shape[1]:]
        raw = self.tokenizer.decode(new, skip_special_tokens=True)
        return dict(raw_generation=raw, raw_sha256=sha(raw), rendered_prompt=formatted,
                    prompt_sha256=sha(formatted), messages=messages,
                    input_tokens=inputs.input_ids.shape[1], output_tokens=new.numel(),
                    latency_seconds=time.perf_counter() - start,
                    truncated=bool(new.numel() >= POLICY['max_new_tokens'] and new[-1].item() != self.tokenizer.eos_token_id),
                    isolation=dict(fresh_tokenization=True, use_cache=False, past_key_values_supplied=False,
                                   cross_branch_history=False, explicit_checkpoint_messages=max(0, len(messages) - 1)))


def frozen_check():
    prep = json.loads((OUT / 'preparation.json').read_text(encoding='utf-8'))
    for path, expected in prep['frozen_files'].items():
        if digest(path) != expected:
            raise ValueError('Frozen file changed: ' + path)
    if prep['policy'] != POLICY:
        raise ValueError('Policy changed')
    return prep


def prepare():
    if OUT.exists():
        raise FileExistsError('Refusing to overwrite v3.3 preparation')
    cases = read_jsonl(DATA)
    if len(cases) != 12:
        raise ValueError('Need twelve fixed cases')
    OUT.mkdir(parents=True)
    lines = ['# v3.3 pre-inference branch audit',
             'The following are frozen branch templates instantiated with the registered entities. Natural raw answers are unknown at this stage; post-Phase-A checkpoints and eligibility will be appended without changing this pre-inference section.',
             'Each branch is a fresh chat serialization of user first-hop prompt, assistant first-hop answer, then a user continuation. Only the assistant answer span is replaced. Downstream facts are added after the checkpoint in every continuation; E0 has no added FIRST-HOP evidence. This is evidence-assisted continuation of a naturally generated first hop, not an uninterrupted closed-book trajectory.']
    for case in cases:
        audit_pair(case, case['B'])
        lines += ['## ' + case['case_id'], '```json\n' + json.dumps(case, ensure_ascii=False, indent=2) + '\n```',
                  '**First-hop prompt**\n```text\n' + first_prompt(case) + '\n```']
        for condition in EVIDENCE:
            lines += ['### ' + condition,
                      '**Gold state template**\n```json\n' + json.dumps(branch_messages(case, case['B'], case['B'], condition), ensure_ascii=False, indent=2) + '\n```',
                      '**Wrong state template**\n```json\n' + json.dumps(branch_messages(case, case['B'], case['B_prime'], condition), ensure_ascii=False, indent=2) + '\n```']
        for state in (case['B'], case['B_prime']):
            lines += ['**Direct lookup**\n```text\n' + control_prompt(case, state) + '\n```']
        lines += ['**S0**\n```text\n' + control_prompt(case, case['B_prime'], True) + '\n```']
    (OUT / 'branch_audit.pre_inference.md').write_text('\n\n'.join(lines), encoding='utf-8')
    (OUT / 'branch_audit.md').write_bytes((OUT / 'branch_audit.pre_inference.md').read_bytes())
    prior = {str(p).replace('\\', '/'): digest(p) for folder in
             ('smoke', 'smoke_v2', 'smoke_v2_1', 'smoke_v3', 'smoke_v3_1', 'smoke_v3_2')
             for p in (Path('results') / folder).rglob('*') if p.is_file() and '__pycache__' not in str(p)}
    write_json(OUT / 'prior_artifact_hashes.json', prior)
    paths = [DATA, INDEX, DATA.with_suffix('.manifest.json'), OUT / 'branch_audit.pre_inference.md']
    paths += [Path('src') / name for name in SOURCES]
    write_json(OUT / 'preparation.json', dict(policy=POLICY,
               frozen_files={str(p).replace('\\', '/'): digest(p) for p in paths}))


def classify_first(case, generated, index):
    parsed = parse_answer(generated['raw_generation'], generated.get('truncated', False))
    value = parsed['parsed_answer']
    if not parsed['parse_valid'] or parsed['rejection']:
        label = 'UNKNOWN_OR_INVALID'
    elif matches(value, case['aliases_B']):
        label = 'CORRECT_FIRST_HOP'
    elif matches(value, case['aliases_B_prime']):
        label = 'KNOWN_ALTERNATIVE'
    else:
        label = 'OTHER_WRONG_ENTITY'
    candidates = [item for item in index if item['relation'] == case['relation']
                  and matches(value, item['entity_aliases'])]
    return parsed | dict(classification=label, natural_B_hat=value,
                         entity_identity_verified=label in ('CORRECT_FIRST_HOP', 'KNOWN_ALTERNATIVE') or bool(candidates),
                         evidence_candidates=candidates,
                         eligibility='pending explicit evidence review and direct lookup')


def phase_a(cases, adapter):
    index = json.loads(INDEX.read_text(encoding='utf-8'))
    with (OUT / 'first_hop_generations.jsonl').open('x', encoding='utf-8') as stream:
        for case in cases:
            messages = [dict(role='user', content=first_prompt(case))]
            row = adapter.generate_messages(messages)
            row.update(classify_first(case, row, index))
            checkpoint_messages = messages + [dict(role='assistant', content=row['raw_generation'])]
            checkpoint = adapter.render(checkpoint_messages, generation=False)
            # This verifies the assistant answer is genuinely appended to the
            # exact Phase-A chat prompt, rather than rewriting its earlier text.
            assert checkpoint.startswith(row['rendered_prompt'] + row['raw_generation'])
            row.update(case_id=case['case_id'], prefix_checkpoint=checkpoint,
                       prefix_checkpoint_sha256=sha(checkpoint), checkpoint_messages=checkpoint_messages)
            stream.write(json.dumps(row, ensure_ascii=False) + '\n')
            stream.flush()
            print(json.dumps({k: row[k] for k in ('case_id', 'raw_generation', 'classification')}, ensure_ascii=False), flush=True)


def resolve_pair(case, first, decision):
    pair = dict(case)
    origin = 'registered_counterfactual'
    natural_eligible = False
    if decision['use_natural_wrong']:
        if first['classification'] not in ('KNOWN_ALTERNATIVE', 'OTHER_WRONG_ENTITY'):
            raise ValueError('Not a natural wrong state')
        proof = decision['evidence']
        assert proof['relation'] == case['relation']
        if first['classification'] == 'KNOWN_ALTERNATIVE':
            assert proof['target'] == case['C_prime']
            assert proof['evidence'] == [case['donor_downstream_evidence']]
        elif proof not in first['evidence_candidates']:
            raise ValueError('Unfrozen evidence provenance')
        assert matches(first['natural_B_hat'], proof['entity_aliases'])
        if canonical(proof['target']) == canonical(case['C']):
            raise ValueError('Natural wrong state shares gold target')
        pair.update(B_prime=first['natural_B_hat'], C_prime=proof['target'],
                    aliases_C_prime=proof['target_aliases'], natural_downstream_provenance=proof)
        origin, natural_eligible = 'natural_wrong', True
    return pair, origin, natural_eligible


def make_review_draft(cases, first_rows):
    draft = {}
    for case, first in zip(cases, first_rows):
        known = first['classification'] == 'KNOWN_ALTERNATIVE'
        proof = dict(entity=case['B_prime'], relation=case['relation'], target=case['C_prime'],
                     entity_aliases=case['aliases_B_prime'], target_aliases=case['aliases_C_prime'],
                     source_id=case['donor_id'], evidence=[case['donor_downstream_evidence']]) if known else None
        draft[case['case_id']] = dict(use_natural_wrong=known, evidence=proof,
            execute=first['parse_valid'] and not first['rejection'],
            reason='Requires explicit evidence/identity review; absent evidence stops this natural branch only')
    write_json(OUT / 'eligibility_review.draft.json', dict(passed=False,
               first_hop_sha256=digest(OUT / 'first_hop_generations.jsonl'), cases=draft))


def phase_b(cases, adapter, review):
    first_rows = read_jsonl(OUT / 'first_hop_generations.jsonl')
    if not review['passed'] or review['first_hop_sha256'] != digest(OUT / 'first_hop_generations.jsonl'):
        raise ValueError('Hash-bound post-Phase-A review required')
    first_map = {r['case_id']: r for r in first_rows}
    if len(first_rows) != len(cases) or set(first_map) != {c['case_id'] for c in cases}:
        raise ValueError('Incomplete Phase-A case set')
    if sum(not r['parse_valid'] for r in first_rows) / len(first_rows) > POLICY['max_bad_first_hop_format']:
        raise ValueError('Natural prefix parsing unreliable; stop before branches')
    resolved = {}
    for case in cases:
        first, decision = first_map[case['case_id']], review['cases'][case['case_id']]
        if decision['execute']:
            pair, origin, eligible = resolve_pair(case, first, decision)
            audit_pair(pair, first['raw_generation'])
            resolved[case['case_id']] = dict(pair=pair, origin=origin, natural_evidence_eligible=eligible)
    write_json(OUT / 'resolved_cases.json', resolved)
    appendix = ['# Post-Phase-A review (pre-inference section above unchanged)',
                'These decisions use only Phase-A responses and frozen evidence, before downstream generation. Natural eligibility additionally requires both direct lookups to pass.',
                '```json\n' + json.dumps(review, ensure_ascii=False, indent=2) + '\n```']
    for first in first_rows:
        appendix += ['## ' + first['case_id'],
                     '```json\n' + json.dumps({k: first[k] for k in ('natural_B_hat', 'classification', 'entity_identity_verified', 'prefix_checkpoint', 'prefix_checkpoint_sha256')}, ensure_ascii=False, indent=2) + '\n```']
    original = (OUT / 'branch_audit.pre_inference.md').read_bytes()
    (OUT / 'branch_audit.md').write_bytes(original + ('\n\n' + '\n\n'.join(appendix)).encode('utf-8'))
    records, stopped = [], []
    with (OUT / 'branch_trajectories.jsonl').open('x', encoding='utf-8') as stream:
        def call(case, messages, branch, condition, role, logical):
            result = adapter.generate_messages(messages)
            result.update(parse_answer(result['raw_generation'], result.get('truncated', False)))
            classification_row = case | result | dict(condition='state_B_prime' if role == 'wrong' else 'state_B')
            label, pending = classify(classification_row)
            if role.startswith('direct'):
                classification_row['condition'] = 'direct_B_prime' if role == 'direct_wrong' else 'direct_B'
                label, pending = classify(classification_row)
            first = first_map[case['case_id']]
            prefix_ok = True
            checkpoint = None
            if len(messages) == 3:
                checkpoint = adapter.render(messages[:2], generation=False)
                prefix_ok = result['rendered_prompt'].startswith(checkpoint)
                start, end = state_span(first['raw_generation'])
                changed = messages[1]['content']
                original = first['prefix_checkpoint']
                # Replace just the answer within the serialized assistant turn.
                offset = len(first['rendered_prompt'])
                assert original[offset:offset + len(first['raw_generation'])] == first['raw_generation']
                intended = original[:offset + start] + changed[start:len(changed) - len(first['raw_generation'][end:]) if first['raw_generation'][end:] else len(changed)] + original[offset + end:]
                prefix_ok = prefix_ok and checkpoint == intended
            if not prefix_ok:
                raise ValueError('Checkpoint changed outside intended state span')
            result.update(case_id=case['case_id'], branch=branch, evidence_condition=condition,
                          role=role, logical_branches=logical, label=label, review_required=pending,
                          state=messages[1]['content'] if len(messages) == 3 else (case['B_prime'] if role in ('wrong', 'direct_wrong') else case['B']),
                          B=case['B'], C=case['C'], B_prime=case['B_prime'], C_prime=case['C_prime'],
                          origin=resolved[case['case_id']]['origin'], prefix_verified=prefix_ok,
                          branch_checkpoint=checkpoint, natural_checkpoint_sha256=first['prefix_checkpoint_sha256'],
                          evidence_counterfactual=condition in ('E2', 'E3a', 'E3b'))
            records.append(result)
            stream.write(json.dumps(result, ensure_ascii=False) + '\n')
            stream.flush()
            print(json.dumps({k: result[k] for k in ('case_id', 'branch', 'raw_generation', 'label')}, ensure_ascii=False), flush=True)
            return result

        # All independent lookup controls precede interpretation of any branch.
        for case_id, data in resolved.items():
            case = data['pair']
            controls = []
            for role, entity in (('direct_gold', case['B']), ('direct_wrong', case['B_prime'])):
                controls.append(call(case, [dict(role='user', content=control_prompt(case, entity))], role, 'lookup', role, []))
            data['lookup_pass'] = all(r['label'] == 'EXACT_CORRECT' for r in controls)
        direct_correct = sum(r['label'] == 'EXACT_CORRECT' for r in records)
        if not records or direct_correct / len(records) < POLICY['min_CLA']:
            stopped.append('Overall CLA below 90%; no downstream branches executed')
        else:
            for case_id, data in resolved.items():
                if not data['lookup_pass']:
                    continue
                case, first = data['pair'], first_map[case_id]
                raw = first['raw_generation']
                natural_logical_used = False
                for condition in EVIDENCE:
                    for role, state in (('gold', case['B']), ('wrong', case['B_prime'])):
                        logical = [('B1' if role == 'gold' else 'B2') + '/' + condition]
                        messages = branch_messages(case, raw, state, condition)
                        if condition == 'E0' and ((role == 'gold' and first['classification'] == 'CORRECT_FIRST_HOP') or (role == 'wrong' and data['natural_evidence_eligible'])):
                            if messages[1]['content'] == raw:
                                logical.append('B0')
                                natural_logical_used = True
                        call(case, messages, role + '/' + condition, condition, role, logical)
                call(case, [dict(role='user', content=control_prompt(case, case['B_prime'], True))], 'S0', 'S0', 'wrong', ['S0'])
                # Preserve B0 exactly even when an alias/punctuation variant makes
                # it distinct from the canonical gold-state replacement.
                if not natural_logical_used and (first['classification'] == 'CORRECT_FIRST_HOP' or data['natural_evidence_eligible']):
                    role = 'wrong' if data['natural_evidence_eligible'] else 'gold'
                    call(case, branch_messages(case, raw, None, 'E0'), 'B0', 'E0', role, ['B0'])
                state_rows = [r for r in records if not r['role'].startswith('direct')]
                bad = sum(r['label'] in ('OUT_OF_CONTEXT_HALLUCINATION', 'INVALID_OUTPUT') for r in state_rows)
                if bad / len(state_rows) > POLICY['stop_unsupported_majority']:
                    stopped.append('Unsupported/invalid downstream outputs exceed 50%; stopped after case ' + case_id)
                    break
    write_json(OUT / 'resolved_cases.json', resolved)
    export(cases, first_rows, records, resolved, stopped)


def analyze(cases, first_rows, records, resolved, stopped):
    keys = [(r['case_id'], r['branch']) for r in records]
    if len(keys) != len(set(keys)):
        raise ValueError('Duplicate branch calls')
    indexed = dict(zip(keys, records))
    complete = [case['case_id'] for case in cases if case['case_id'] in resolved
                and resolved[case['case_id']].get('lookup_pass')
                and all((case['case_id'], role + '/' + e) in indexed for role in ('gold', 'wrong') for e in EVIDENCE)
                and (case['case_id'], 'S0') in indexed]
    clean_records = [r for r in records if r['case_id'] in complete]
    counts = Counter(r['classification'] for r in first_rows)
    # NFER counts any failure to return the gold first hop, with unknown/invalid
    # separately reported so this is not called a verified wrong-entity rate.
    metrics = dict(first_hop_counts=dict(counts),
                   NFER=fraction(sum(r['classification'] != 'CORRECT_FIRST_HOP' for r in first_rows), len(first_rows)),
                   verified_wrong_entity_rate=fraction(sum(r['classification'] in ('KNOWN_ALTERNATIVE', 'OTHER_WRONG_ENTITY') and r['entity_identity_verified'] for r in first_rows), len(first_rows)),
                   UNKNOWN_OR_INVALID=fraction(counts['UNKNOWN_OR_INVALID'], len(first_rows)),
                   completed_case_ids=complete, calls=dict(first_hop=len(first_rows), downstream=len(records)))
    direct = [r for r in records if r['role'].startswith('direct')]
    for name, role in (('CLA_B', 'direct_gold'), ('CLA_B_prime', 'direct_wrong'), ('CLA', None)):
        group = [r for r in direct if role is None or r['role'] == role]
        metrics[name] = fraction(sum(r['label'] == 'EXACT_CORRECT' for r in group), len(group))
    metrics['conditions'] = {}
    for e in EVIDENCE:
        wrong = [indexed[c, 'wrong/' + e] for c in complete]
        gold = [indexed[c, 'gold/' + e] for c in complete]
        pair_assessments = {}
        bad_labels = ('OUT_OF_CONTEXT_HALLUCINATION', 'INVALID_OUTPUT', 'UNKNOWN_REJECT')
        for w, g in zip(wrong, gold):
            bad_w, bad_g = w['label'] in bad_labels, g['label'] in bad_labels
            coherent_shift = (e == 'E1' and w['label'] == 'OVERRIDE_TO_GOLD' and g['label'] == 'EXACT_CORRECT') or (e == 'E2' and w['label'] == 'PROPAGATE' and g['label'] == 'OTHER_CONTEXT_TARGET')
            if bad_w and bad_g:
                assessment = 'GENERAL_INTERFERENCE'
            elif bad_w or bad_g:
                assessment = 'UNRESOLVED_INTERFERENCE'
            elif coherent_shift:
                assessment = 'STATE_SELECTIVE'
            elif w['label'] == 'PROPAGATE' and g['label'] == 'EXACT_CORRECT':
                assessment = 'STABLE_STATE_FOLLOWING'
            else:
                assessment = 'OTHER_SUPPORTED_SELECTION'
            pair_assessments[w['case_id']] = assessment
        metrics['conditions'][e] = dict(CPR=fraction(sum(r['label'] == 'PROPAGATE' for r in wrong), len(wrong)),
            OR=fraction(sum(r['label'] == 'OVERRIDE_TO_GOLD' for r in wrong), len(wrong)),
            GSA=fraction(sum(r['label'] == 'EXACT_CORRECT' for r in gold), len(gold)),
            wrong_support_on_gold=fraction(sum(r['label'] == 'OTHER_CONTEXT_TARGET' for r in gold), len(gold)),
            pair_assessments=pair_assessments, assessment_counts=dict(Counter(pair_assessments.values())),
            wrong_outcomes=dict(Counter(r['label'] for r in wrong)),
            strata={origin: fraction(sum(r['label'] == 'PROPAGATE' for r in wrong if r['origin'] == origin), sum(r['origin'] == origin for r in wrong))
                    for origin in ('natural_wrong', 'registered_counterfactual')})
    natural = [r for r in clean_records if 'B0' in r['logical_branches'] and r['origin'] == 'natural_wrong']
    metrics['NPR'] = fraction(sum(r['label'] == 'PROPAGATE' for r in natural), len(natural))
    metrics['natural_error_eligible_ids'] = [r['case_id'] for r in natural]
    s0 = [indexed[c, 'S0'] for c in complete]
    metrics['S0_PR'] = fraction(sum(r['label'] == 'PROPAGATE' for r in s0), len(s0))
    metrics['delta_PR_prefix'] = (round(metrics['conditions']['E0']['CPR']['rate'] - metrics['S0_PR']['rate'], 10) if complete else None)
    metrics['symmetry'] = dict(gold_support_on_wrong=metrics['conditions']['E1']['OR'],
                               wrong_support_on_gold=metrics['conditions']['E2']['wrong_support_on_gold'])
    metrics['order_sensitive_case_ids'] = [c for c in complete if indexed[c, 'wrong/E3a']['label'] != indexed[c, 'wrong/E3b']['label']]
    states = [r for r in records if not r['role'].startswith('direct')]
    bad = sum(r['label'] in ('OUT_OF_CONTEXT_HALLUCINATION', 'INVALID_OUTPUT') for r in states)
    metrics['unsupported_invalid'] = fraction(bad, len(states))
    valid = [c for c in complete if all(r['prefix_verified'] and r['label'] not in ('OUT_OF_CONTEXT_HALLUCINATION', 'INVALID_OUTPUT') for r in states if r['case_id'] == c)]
    checks = dict(CLA=bool(direct) and metrics['CLA']['rate'] >= POLICY['min_CLA'],
                  valid_cases=len(valid) >= POLICY['min_valid_cases'],
                  unsupported_invalid=bool(states) and bad / len(states) <= POLICY['max_unsupported_invalid'],
                  matched_prefixes=bool(states) and all(r['prefix_verified'] for r in states),
                  isolation=bool(records) and all(not r['isolation']['cross_branch_history'] and not r['isolation']['use_cache'] and not r['isolation']['past_key_values_supplied'] for r in records))
    metrics['denominator_note'] = 'NFER: all 12 including unknown/invalid non-correct answers (reported separately). CPR/OR/GSA/S0: common fully executed, direct-correct cases, split by natural versus registered origin. NPR: eligible natural-error B0 only. No sparse-error requirement.'
    gate = dict(passed=all(checks.values()) and not stopped, checks=checks, valid_case_ids=valid,
                stop_reasons=stopped, policy=POLICY, scale_authorized=False, human_review_required=True,
                semantic_review='pending', first_hop_sha256=digest(OUT / 'first_hop_generations.jsonl'))
    return metrics, gate


def export(cases, first_rows, records, resolved, stopped):
    metrics, gate = analyze(cases, first_rows, records, resolved, stopped)
    write_json(OUT / 'metrics.json', metrics)
    with (OUT / 'summary.csv').open('w', encoding='utf-8', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['condition', 'metric', 'count', 'denominator', 'rate'])
        for key in ('NFER', 'NPR', 'CLA_B', 'CLA_B_prime', 'CLA', 'S0_PR', 'unsupported_invalid'):
            v = metrics[key]
            writer.writerow(['overall', key, v['count'], v['denominator'], v['rate']])
        for e, group in metrics['conditions'].items():
            for key in ('CPR', 'OR', 'GSA', 'wrong_support_on_gold'):
                v = group[key]
                writer.writerow([e, key, v['count'], v['denominator'], v['rate']])
    lines = ['# v3.3 natural-trajectory inspection',
             'All downstream calls use explicit reference facts after the saved first-hop checkpoint. B0 is evidence-assisted natural-state continuation. See [diagnosis](diagnosis.md) and [pre-inference audit](branch_audit.pre_inference.md).']
    first_map = {r['case_id']: r for r in first_rows}
    for case in cases:
        first = first_map[case['case_id']]
        data = resolved.get(case['case_id'], {})
        lines += ['## ' + case['case_id'],
                  f"Gold B: {case['B']}; natural B_hat: {first['natural_B_hat']}; registered B′: {case['B_prime']}; classification: {first['classification']}.",
                  'Resolution: ```json\n' + json.dumps(data, ensure_ascii=False, indent=2) + '\n```',
                  '**Exact Phase-A prompt**\n```text\n' + first['rendered_prompt'] + '\n```',
                  '**Exact first-hop response**\n```text\n' + first['raw_generation'] + '\n```',
                  '**Natural checkpoint**\n```text\n' + first['prefix_checkpoint'] + '\n```',
                  '| Branch / logical branches | Evidence | State | Output | Label |\n|---|---|---|---|---|']
        group = [r for r in records if r['case_id'] == case['case_id']]
        for r in group:
            cells = [r['branch'] + ' / ' + ', '.join(r['logical_branches']), r['evidence_condition'], r['state'], r['raw_generation'], r['label']]
            lines[-1] += '\n| ' + ' | '.join(s.replace('|', '\\|').replace('\n', ' / ') for s in cells) + ' |'
        highlights = []
        for r in group:
            if 'B0' in r['logical_branches'] and r['origin'] == 'natural_wrong':
                highlights.append('Natural error → ' + r['label'])
            if r['role'] == 'wrong' and r['label'] == 'OVERRIDE_TO_GOLD':
                highlights.append(r['branch'] + ': override to gold')
            if r['role'] == 'gold' and r['label'] == 'OTHER_CONTEXT_TARGET':
                highlights.append(r['branch'] + ': mirror override to wrong target')
        lookup = {r['branch']: r for r in group}
        if 'S0' in lookup and 'wrong/E0' in lookup and lookup['S0']['label'] != lookup['wrong/E0']['label']:
            highlights.append('Prefix changes outcome relative to S0')
        lines.append('**Highlights:** ' + ('; '.join(highlights) or 'No override or prefix-outcome change.'))
        for r in group:
            lines += ['### ' + r['branch'], '**Complete rendered prompt**\n```text\n' + r['rendered_prompt'] + '\n```',
                      '**Raw response**\n```text\n' + r['raw_generation'] + '\n```']
    (OUT / 'inspection.md').write_text('\n\n'.join(lines), encoding='utf-8')
    gate.update(trajectories_sha256=digest(OUT / 'branch_trajectories.jsonl'), inspection_sha256=digest(OUT / 'inspection.md'))
    write_json(OUT / 'gate.json', gate)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=('prepare', 'phase-a', 'phase-b'))
    args = parser.parse_args()
    if args.action == 'prepare':
        prepare()
        return
    frozen_check()
    cases = read_jsonl(DATA)
    artifact = OUT / ('first_hop_generations.jsonl' if args.action == 'phase-a' else 'branch_trajectories.jsonl')
    if artifact.exists():
        raise FileExistsError('Refusing to rerun/overwrite ' + str(artifact))
    audit = json.loads((OUT / 'audit_review.json').read_text(encoding='utf-8'))
    assert audit['passed'] and audit['pre_inference_audit_sha256'] == digest(OUT / 'branch_audit.pre_inference.md')
    load = json.loads(Path('results/smoke_v2/load_nf4.json').read_text(encoding='utf-8'))
    validate_load_test(load)
    manifest_path = OUT / 'manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else dict(
        version='3.3', model=MODEL, revision=load['revision'], policy=POLICY,
        data_sha256=digest(DATA), index_sha256=digest(INDEX),
        source_hashes={name: digest(Path('src') / name) for name in SOURCES},
        decoding=dict(do_sample=False, temperature_argument=None, use_cache=False, enable_thinking=False, max_new_tokens=32),
        endpoint='smoke only; no SHARS/HalluSE; no automatic scale-up',
        design='Natural closed-book first-hop answer; explicit text checkpoint replay in isolated fresh calls; downstream facts added after checkpoint; B0 aliases identical E0 calls where possible')
    write_json(manifest_path, manifest)
    adapter = None
    try:
        adapter = BranchAdapter('4bit-nf4', '.cache/huggingface', load['revision'])
        manifest.update(quantization=adapter.quantization, compute_dtype=adapter.compute_dtype,
                        device_map=adapter.device_map, cpu_offload=adapter.offload)
        write_json(manifest_path, manifest)
        if args.action == 'phase-a':
            phase_a(cases, adapter)
            make_review_draft(cases, read_jsonl(OUT / 'first_hop_generations.jsonl'))
        else:
            review = json.loads((OUT / 'eligibility_review.json').read_text(encoding='utf-8'))
            phase_b(cases, adapter, review)
    except Exception:
        write_json(OUT / (args.action + '.failure.json'), dict(error=traceback.format_exc()))
        raise
    finally:
        if adapter:
            write_json(OUT / (args.action + '.memory.json'), adapter.memory())
        prior = json.loads((OUT / 'prior_artifact_hashes.json').read_text(encoding='utf-8'))
        changed = [p for p, value in prior.items() if not Path(p).exists() or digest(p) != value]
        write_json(OUT / 'preservation_check.json', dict(passed=not changed, files_checked=len(prior), changed=changed))
        if changed:
            raise RuntimeError('Prior artifacts changed')


if __name__ == '__main__':
    main()
