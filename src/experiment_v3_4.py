"""Traceable natural selections in a frozen four-candidate universe."""
import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import traceback

from .common import digest, read_jsonl
from .experiment_v2 import canonical, matches, validate_load_test
from .experiment_v3 import TEMPLATES, fraction, parse_answer, write_json
from .experiment_v3_3 import BranchAdapter, replace_state, sha
from .generation.local_hf_adapter import MODEL
from .prepare_v3_4 import DATA

OUT = Path('results/smoke_v3_4')
POLICY = dict(cases=20, seed=42, min_CLA=0.95, min_valid_first_hops=15,
              min_traceable_errors=5, max_OSER=0.25, max_invalid_downstream=0.10,
              min_complete_branch_cases=15, max_new_tokens=32)
SOURCES = ('prepare_v3_4.py', 'experiment_v3_4.py', 'experiment_v3_3.py', 'experiment_v3.py',
           'experiment_v2.py', 'generation/local_hf_adapter.py', 'common.py')
VALID_FIRST = ('CORRECT_FIRST_HOP', 'TRACEABLE_WRONG_CANDIDATE')


def first_prompt(case):
    names = '\n'.join(f'{i}. {c["name"]}' for i, c in enumerate(case['candidates'], 1))
    evidence = '\n'.join('- ' + f for f in case['first_hop_evidence'])
    return (f'Question:\n{case["original_question"]}\n\nFirst solve only the first step.\n\n'
            + 'Candidate directors:\n' + names + '\n\nEvidence:\n' + evidence
            + f'\n\nBased on the evidence above, who directed "{case["A"]}"?'
            + '\n\nAnswer with only one candidate name.')


def reference_facts(case):
    template = TEMPLATES[case['relation']][0]
    return 'Reference facts:\n' + '\n'.join(
        '- ' + template.format(person=c['name'], answer=c['target']) for c in case['candidates'])


def continuation(case):
    return (reference_facts(case) + '\n\nNow continue to the second step.\n\n'
            + 'Using the first-step result above, answer:\n'
            + TEMPLATES[case['relation']][1].format(person='that person')
            + '\n\nAnswer with only the requested name or location.')


def branch_messages(case, raw, state=None):
    return [dict(role='user', content=first_prompt(case)),
            dict(role='assistant', content=raw if state is None else replace_state(raw, state)),
            dict(role='user', content=continuation(case))]


def lookup_prompt(case, name, stripped=False):
    subject = 'the person in the current Step 1 state' if stripped else name
    return (reference_facts(case) + '\n\n'
            + ('Current Step 1 state:\n' + name + '\n\n' if stripped else '')
            + 'According to the reference facts, ' + TEMPLATES[case['relation']][1].format(person=subject)
            + '\n\nAnswer with only the requested name or location.')


def audit_case(case):
    people = case['candidates']
    assert len(people) == 4 and len({p['name'] for p in people}) == 4
    assert len({canonical(p['target']) for p in people}) == 4
    alias_sets = [{canonical(v) for v in p['target_aliases']} for p in people]
    assert all(not alias_sets[i] & alias_sets[j] for i in range(4) for j in range(i))
    assert sum(p['name'] == case['B'] for p in people) == 1
    assert case['registered_wrong'] in {p['name'] for p in people} - {case['B']}
    assert case['source_A']['director'] == case['source_bridge']['director'] == case['B']
    assert case['A'] != case['source_bridge']['title']
    expected = [f'The films "{case["A"]}" and "{case["source_bridge"]["title"]}" have the same director.']
    expected += [f'"{p["bridge_film"]["title"]}" was directed by {p["name"]}.' for p in people]
    assert sorted(case['first_hop_evidence']) == sorted(expected)
    for p in people:
        assert p['bridge_film']['director'] == p['name'] and p['bridge_film']['title'] != case['A']
        assert p['relation'] == case['relation']
        assert canonical(p['target']) in canonical(p['downstream_evidence']['text'])
        assert case['first_hop_evidence'].count(f'"{case["A"]}" was directed by {p["name"]}.') == 0
    gold = branch_messages(case, case['B'], case['B'])
    wrong = branch_messages(case, case['B'], case['registered_wrong'])
    assert gold[0] == wrong[0] and gold[2] == wrong[2]
    assert reference_facts(case) in gold[2]['content']
    return dict(four_candidates=True, four_unique_targets=True, disjoint_target_aliases=True,
                source_backed_composition=True, no_direct_A_to_B_statement=True,
                all_names_present_in_bridge_evidence=True, identical_downstream_facts=True,
                answer_span_only_replacement=True)


def prepare():
    if OUT.exists():
        raise FileExistsError('Refusing to overwrite preparation')
    cases = read_jsonl(DATA)
    assert len(cases) == POLICY['cases']
    lines = ['# v3.4 candidate audit before inference',
             'Design A: compose a derived shared-director link with four source-backed bridge-film/director facts. Every candidate is mentioned once in those four facts, preventing a unique-name shortcut. No direct A→candidate assertion reaches Phase A. Downstream facts are withheld until continuation. No v3.4 outputs used in selection.']
    checks = {}
    for case in cases:
        checks[case['case_id']] = audit_case(case)
        lines += ['## ' + case['case_id'], '```json\n' + json.dumps(case, ensure_ascii=False, indent=2) + '\n```',
                  'Checks: ' + json.dumps(checks[case['case_id']]),
                  '**Exact first-hop prompt**\n```text\n' + first_prompt(case) + '\n```',
                  '**Identical continuation for N0/C0/W0**\n```text\n' + continuation(case) + '\n```',
                  '**Checkpoint template**: first-hop user message, exact model assistant answer, then the continuation user message. C0/W0 replace only that assistant answer span.']
        for p in case['candidates']:
            lines += ['**Direct lookup: ' + p['name'] + '**\n```text\n' + lookup_prompt(case, p['name']) + '\n```']
        lines += ['**S0 template (state will be the exact eligible natural selection)**\n```text\n'
                  + lookup_prompt(case, case['registered_wrong'], True) + '\n```']
    OUT.mkdir(parents=True)
    (OUT / 'candidate_audit.md').write_text('\n\n'.join(lines), encoding='utf-8')
    prior = {str(p).replace('\\', '/'): digest(p) for folder in
             ('smoke', 'smoke_v2', 'smoke_v2_1', 'smoke_v3', 'smoke_v3_1', 'smoke_v3_2', 'smoke_v3_3')
             for p in (Path('results') / folder).rglob('*') if p.is_file() and '__pycache__' not in str(p)}
    write_json(OUT / 'prior_artifact_hashes.json', prior)
    paths = [DATA, DATA.with_suffix('.manifest.json'), OUT / 'candidate_audit.md'] + [Path('src') / p for p in SOURCES]
    write_json(OUT / 'preparation.json', dict(policy=POLICY, checks=checks,
               frozen_files={str(p).replace('\\', '/'): digest(p) for p in paths}))


def frozen_check():
    prep = json.loads((OUT / 'preparation.json').read_text(encoding='utf-8'))
    assert prep['policy'] == POLICY
    for path, value in prep['frozen_files'].items():
        if digest(path) != value:
            raise ValueError('Frozen file changed: ' + path)


def classify_first(case, result):
    parsed = parse_answer(result['raw_generation'], result.get('truncated', False))
    name = result['raw_generation'].strip()
    selected = next((p for p in case['candidates'] if p['name'] == name), None)
    if not parsed['parse_valid'] or parsed['rejection']:
        label = 'INVALID_OUTPUT'
    elif selected is None:
        label = 'OUT_OF_SET_ENTITY'
    else:
        label = 'CORRECT_FIRST_HOP' if name == case['B'] else 'TRACEABLE_WRONG_CANDIDATE'
    return parsed | dict(natural_B_hat=name, first_hop_label=label,
                         selected_target=selected['target'] if selected else None)


def phase_a_stop(first):
    reasons = []
    counts = Counter(r['first_hop_label'] for r in first)
    if counts['TRACEABLE_WRONG_CANDIDATE'] < POLICY['min_traceable_errors']:
        reasons.append('Fewer than five traceable natural errors; stop without candidate redesign or retries')
    if sum(counts[k] for k in VALID_FIRST) < POLICY['min_valid_first_hops']:
        reasons.append('Fewer than fifteen in-set valid first hops')
    if counts['OUT_OF_SET_ENTITY'] / len(first) > POLICY['max_OSER']:
        reasons.append('Out-of-set rate exceeds 25%')
    return reasons


def downstream_label(case, result, state):
    if not result['parse_valid']:
        return 'INVALID_OUTPUT', None
    if result['rejection']:
        return 'UNKNOWN_REJECT', None
    target = next((p for p in case['candidates'] if matches(result['parsed_answer'], p['target_aliases'])), None)
    if target is None:
        return 'OUT_OF_UNIVERSE', None
    if target['name'] == state:
        return 'STATE_TARGET', target['name']
    if target['name'] == case['B']:
        return 'GOLD_TARGET', target['name']
    return 'OTHER_CANDIDATE_TARGET', target['name']


def run(cases, adapter):
    first, records, logical = [], [], {}
    with (OUT / 'first_hop_generations.jsonl').open('x', encoding='utf-8') as stream:
        for case in cases:
            messages = [dict(role='user', content=first_prompt(case))]
            row = adapter.generate_messages(messages)
            row.update(classify_first(case, row))
            checkpoint = adapter.render(messages + [dict(role='assistant', content=row['raw_generation'])], generation=False)
            if not checkpoint.startswith(row['rendered_prompt'] + row['raw_generation']):
                raise ValueError('Natural checkpoint does not match actual generation prefix')
            row.update(case_id=case['case_id'], prefix_checkpoint=checkpoint, checkpoint_sha256=sha(checkpoint))
            first.append(row)
            stream.write(json.dumps(row, ensure_ascii=False) + '\n')
            stream.flush()
            print(json.dumps({k: row[k] for k in ('case_id', 'raw_generation', 'first_hop_label')}, ensure_ascii=False), flush=True)
    stopped = phase_a_stop(first)
    with (OUT / 'branch_trajectories.jsonl').open('x', encoding='utf-8') as stream:
        if stopped:
            export(cases, first, records, logical, stopped)
            return
        first_map = {r['case_id']: r for r in first}
        controls = {}

        def call(case, messages, state, branch):
            result = adapter.generate_messages(messages)
            result.update(parse_answer(result['raw_generation'], result.get('truncated', False)))
            label, chosen = downstream_label(case, result, state)
            prefix = None
            if len(messages) == 3:
                f = first_map[case['case_id']]
                prefix = adapter.render(messages[:2], generation=False)
                offset = len(f['rendered_prompt'])
                expected = f['prefix_checkpoint'][:offset] + messages[1]['content'] + f['prefix_checkpoint'][offset + len(f['raw_generation']):]
                assert messages[0]['content'] == first_prompt(case)
                assert messages[1]['content'] == f['raw_generation'] or messages[1]['content'] == replace_state(f['raw_generation'], state)
                if prefix != expected or not result['rendered_prompt'].startswith(prefix):
                    raise ValueError('Branch changed outside the intended answer span')
            result.update(case_id=case['case_id'], branch=branch, state=state, label=label,
                          selected_candidate=chosen, prefix_verified=True, branch_checkpoint=prefix,
                          call_id=len(records))
            records.append(result)
            stream.write(json.dumps(result, ensure_ascii=False) + '\n')
            stream.flush()
            print(json.dumps({k: result[k] for k in ('case_id', 'branch', 'raw_generation', 'label')}, ensure_ascii=False), flush=True)
            return result

        for case in cases:
            controls[case['case_id']] = []
            for p in case['candidates']:
                row = call(case, [dict(role='user', content=lookup_prompt(case, p['name']))], p['name'], 'lookup/' + p['name'])
                controls[case['case_id']].append(row['label'] == 'STATE_TARGET')
        if sum(sum(v) for v in controls.values()) / 80 < POLICY['min_CLA']:
            stopped.append('CLA below 95%; stop before trajectory branches')
        else:
            for case in cases:
                f = first_map[case['case_id']]
                if f['first_hop_label'] not in VALID_FIRST or not all(controls[case['case_id']]):
                    continue
                wrong = f['natural_B_hat'] if f['first_hop_label'] == 'TRACEABLE_WRONG_CANDIDATE' else case['registered_wrong']
                states = dict(N0=f['natural_B_hat'], C0=case['B'], W0=wrong)
                seen = {}
                logical[case['case_id']] = {}
                for branch, state in states.items():
                    messages = branch_messages(case, f['raw_generation'], None if branch == 'N0' else state)
                    key = adapter.render(messages)
                    if key not in seen:
                        seen[key] = call(case, messages, state, branch)
                    logical[case['case_id']][branch] = seen[key]['call_id']
                if f['first_hop_label'] == 'TRACEABLE_WRONG_CANDIDATE':
                    row = call(case, [dict(role='user', content=lookup_prompt(case, wrong, True))], wrong, 'S0')
                    logical[case['case_id']]['S0'] = row['call_id']
                state_rows = [r for r in records if not r['branch'].startswith('lookup/')]
                if sum(r['label'] == 'INVALID_OUTPUT' for r in state_rows) / len(state_rows) > POLICY['max_invalid_downstream']:
                    stopped.append('Invalid downstream outputs exceed 10%; stopped after current case')
                    break
    export(cases, first, records, logical, stopped)


def analyze(cases, first, records, logical, stopped):
    if len(first) != 20 or len({r['case_id'] for r in first}) != 20:
        raise ValueError('Incomplete first-hop set')
    if len({r['call_id'] for r in records}) != len(records):
        raise ValueError('Duplicate call IDs')
    by_call = {r['call_id']: r for r in records}
    fm = {r['case_id']: r for r in first}
    for cid, mapping in logical.items():
        assert all(by_call[n]['case_id'] == cid for n in mapping.values())
    counts = Counter(r['first_hop_label'] for r in first)
    direct = [r for r in records if r['branch'].startswith('lookup/')]
    state_rows = [r for r in records if not r['branch'].startswith('lookup/')]
    complete = [cid for cid, v in logical.items() if all(k in v for k in ('N0', 'C0', 'W0'))]
    eligible = [cid for cid in complete if fm[cid]['first_hop_label'] == 'TRACEABLE_WRONG_CANDIDATE' and 'S0' in logical[cid]]
    output = lambda cid, branch: by_call[logical[cid][branch]]
    natural = [output(cid, 'N0') for cid in eligible]
    corrected = [output(cid, 'C0') for cid in eligible]
    wrong = [output(cid, 'W0') for cid in complete]
    s0 = [output(cid, 'S0') for cid in eligible]
    metrics = dict(calls=dict(first_hop=len(first), lookup=len(direct), unique_state_calls=len(state_rows)),
        first_hop_counts=dict(counts),
        IFHA=fraction(counts['CORRECT_FIRST_HOP'], 20), TNER=fraction(counts['TRACEABLE_WRONG_CANDIDATE'], 20),
        OSER=fraction(counts['OUT_OF_SET_ENTITY'], 20), first_hop_invalid=fraction(counts['INVALID_OUTPUT'], 20),
        CLA_all=fraction(sum(r['label'] == 'STATE_TARGET' for r in direct), len(direct)),
        NPR=fraction(sum(r['label'] == 'STATE_TARGET' for r in natural), len(natural)),
        NRR=fraction(sum(r['label'] == 'GOLD_TARGET' for r in natural), len(natural)),
        CCS=fraction(sum(r['label'] == 'STATE_TARGET' for r in corrected), len(corrected)),
        CWP=fraction(sum(r['label'] == 'STATE_TARGET' for r in wrong), len(wrong)),
        SCS=fraction(sum(a['label'] == b['label'] == 'STATE_TARGET' for a, b in zip(natural, corrected)), len(natural)),
        S0_NPR=fraction(sum(r['label'] == 'STATE_TARGET' for r in s0), len(s0)),
        invalid_downstream=fraction(sum(r['label'] == 'INVALID_OUTPUT' for r in state_rows), len(state_rows)),
        complete_case_ids=complete, eligible_natural_error_ids=eligible,
        natural_other_candidate=fraction(sum(r['label'] == 'OTHER_CANDIDATE_TARGET' for r in natural), len(natural)),
        natural_out_of_universe=fraction(sum(r['label'] == 'OUT_OF_UNIVERSE' for r in natural), len(natural)))
    metrics['delta_NPR_prefix'] = round(metrics['NPR']['rate'] - metrics['S0_NPR']['rate'], 10) if eligible else None
    metrics['denominators'] = 'IFHA/TNER/OSER/invalid: all 20. OSER counts parseable out-of-set entities separately from invalid. NPR/NRR/CCS/SCS/S0: complete traceable natural errors with all four direct lookups correct. CWP: complete direct-correct valid cases. Missing measurements are null. Logical duplicate branches do not create additional model calls.'
    checks = dict(CLA=metrics['CLA_all']['rate'] >= POLICY['min_CLA'] if direct else None,
                  valid_first_hops=sum(counts[k] for k in VALID_FIRST) >= POLICY['min_valid_first_hops'],
                  traceable_error_yield=counts['TRACEABLE_WRONG_CANDIDATE'] >= POLICY['min_traceable_errors'],
                  OSER=metrics['OSER']['rate'] <= POLICY['max_OSER'],
                  invalid_downstream=metrics['invalid_downstream']['rate'] <= POLICY['max_invalid_downstream'] if state_rows else None,
                  complete_branches=len(complete) >= POLICY['min_complete_branch_cases'] if direct else None,
                  replay=all(r['prefix_verified'] for r in state_rows) if state_rows else None,
                  isolation=all(not r['isolation']['cross_branch_history'] and not r['isolation']['use_cache'] and not r['isolation']['past_key_values_supplied'] for r in first + records),
                  frozen_mapping=True)
    return metrics, dict(passed=all(v is True for v in checks.values()) and not stopped, checks=checks,
                         stop_reasons=stopped, thresholds=POLICY, scale_authorized=False, human_review_required=True)


def export(cases, first, records, logical, stopped):
    metrics, gate = analyze(cases, first, records, logical, stopped)
    write_json(OUT / 'logical_branches.json', logical)
    write_json(OUT / 'metrics.json', metrics)
    with (OUT / 'summary.csv').open('w', encoding='utf-8', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['metric', 'count', 'denominator', 'rate'])
        for key, v in metrics.items():
            if isinstance(v, dict) and 'denominator' in v:
                writer.writerow([key, v['count'], v['denominator'], v['rate']])
        writer.writerow(['delta_NPR_prefix', '', '', metrics['delta_NPR_prefix']])
    fm, calls = {r['case_id']: r for r in first}, {r['call_id']: r for r in records}
    lines = ['# v3.4 inspection', 'Gate: ' + ('PASS' if gate['passed'] else 'FAIL'),
             'Stop reasons: ' + ('; '.join(stopped) or 'None'),
             'NPR = null means unmeasured, not zero. See [diagnosis](diagnosis.md) and [candidate audit](candidate_audit.md).']
    for case in cases:
        cid, f = case['case_id'], fm[case['case_id']]
        lines += ['## ' + cid, f"A: {case['A']}; gold B: {case['B']}; gold C: {case['C']}.",
                  'Candidates: ' + '; '.join(p['name'] + ' → ' + p['target'] for p in case['candidates']),
                  f"Natural B_hat: {f['natural_B_hat']}; label: {f['first_hop_label']}; selected target: {f['selected_target']}.",
                  '| Branch | State | Output | Label | Actual call |\n|---|---|---|---|---|']
        mapping = logical.get(cid, {})
        for b in ('N0', 'C0', 'W0', 'S0'):
            if b not in mapping:
                lines[-1] += f'\n| {b} | — | NOT RUN | STOPPED / INELIGIBLE | — |'
                continue
            r = calls[mapping[b]]
            label = r['label']
            if b == 'N0' and f['first_hop_label'] == 'TRACEABLE_WRONG_CANDIDATE':
                label = {'STATE_TARGET': 'NATURAL_PROPAGATE', 'GOLD_TARGET': 'NATURAL_RECOVER_TO_GOLD',
                         'OTHER_CANDIDATE_TARGET': 'NATURAL_OTHER_CANDIDATE_TARGET', 'OUT_OF_UNIVERSE': 'NATURAL_OUT_OF_UNIVERSE'}.get(label, label)
            cells = [b, r['state'], r['raw_generation'], label, str(r['call_id'])]
            lines[-1] += '\n| ' + ' | '.join(s.replace('|', '\\|').replace('\n', ' / ') for s in cells) + ' |'
        if cid in metrics['eligible_natural_error_ids']:
            n, c = calls[mapping['N0']], calls[mapping['C0']]
            if n['label'] == c['label'] == 'STATE_TARGET':
                lines += ['**STATE_CAUSAL_SWITCH:** natural state → its target; corrected state → gold target.']
            if n['label'] != calls[mapping['S0']]['label']:
                lines += ['**Prefix-sensitive difference:** N0 differs from S0.']
        lines += ['**Exact first-hop prompt**\n```text\n' + f['rendered_prompt'] + '\n```',
                  '**Raw first-hop answer**\n```text\n' + f['raw_generation'] + '\n```',
                  '**Exact checkpoint**\n```text\n' + f['prefix_checkpoint'] + '\n```']
        for r in records:
            if r['case_id'] == cid:
                lines += ['### Actual call ' + str(r['call_id']) + ': ' + r['branch'],
                          '```text\n' + r['rendered_prompt'] + '\n```', '**Raw answer**\n```text\n' + r['raw_generation'] + '\n```']
    (OUT / 'inspection.md').write_text('\n\n'.join(lines), encoding='utf-8')
    gate.update(first_hop_sha256=digest(OUT / 'first_hop_generations.jsonl'),
                trajectories_sha256=digest(OUT / 'branch_trajectories.jsonl'),
                inspection_sha256=digest(OUT / 'inspection.md'))
    write_json(OUT / 'gate.json', gate)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=('prepare', 'run'))
    args = parser.parse_args()
    if args.action == 'prepare':
        prepare()
        return
    frozen_check()
    if (OUT / 'first_hop_generations.jsonl').exists() or (OUT / 'manifest.json').exists():
        raise FileExistsError('Refusing rerun or overwrite')
    review = json.loads((OUT / 'audit_review.json').read_text(encoding='utf-8'))
    assert review['passed'] and review['audit_sha256'] == digest(OUT / 'candidate_audit.md')
    cases = read_jsonl(DATA)
    for case in cases:
        audit_case(case)
    load = json.loads(Path('results/smoke_v2/load_nf4.json').read_text(encoding='utf-8'))
    validate_load_test(load)
    manifest = dict(version='3.4', model=MODEL, revision=load['revision'], policy=POLICY,
        dataset_sha256=digest(DATA), audit_sha256=digest(OUT / 'candidate_audit.md'),
        source_hashes={p: digest(Path('src') / p) for p in SOURCES},
        decoding=dict(do_sample=False, temperature_argument=None, use_cache=False, enable_thinking=False, max_new_tokens=32),
        design='Closed candidate-set first-hop composition; checkpoint replay with post-checkpoint downstream facts; no context-support ablations')
    write_json(OUT / 'manifest.json', manifest)
    adapter = None
    try:
        adapter = BranchAdapter('4bit-nf4', '.cache/huggingface', load['revision'])
        manifest.update(quantization=adapter.quantization, compute_dtype=adapter.compute_dtype,
                        device_map=adapter.device_map, cpu_offload=adapter.offload)
        write_json(OUT / 'manifest.json', manifest)
        run(cases, adapter)
    except Exception:
        write_json(OUT / 'failure.json', dict(error=traceback.format_exc()))
        raise
    finally:
        if adapter:
            write_json(OUT / 'memory.json', adapter.memory())
        prior = json.loads((OUT / 'prior_artifact_hashes.json').read_text(encoding='utf-8'))
        changed = [p for p, h in prior.items() if not Path(p).exists() or digest(p) != h]
        write_json(OUT / 'preservation_check.json', dict(passed=not changed, files_checked=len(prior), changed=changed))
        if changed:
            raise RuntimeError('Prior artifacts changed')


if __name__ == '__main__':
    main()
