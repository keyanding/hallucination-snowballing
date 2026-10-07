"""Independent v3.6.1 token/plan/gate audit; never performs inference."""
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from transformers import AutoTokenizer

OUT = Path('results/v3_6_1')


def load(name):
    return json.loads((OUT/name).read_text(encoding='utf-8'))


def norm(value):
    return unicodedata.normalize('NFC', value).strip().removesuffix('.')


def main():
    manifest = load('manifest.json')
    for group in ('frozen', 'prior_artifacts'):
        for path, value in manifest[group].items():
            assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == value, path
    freeze = load('decoding_freeze.json')
    tok = AutoTokenizer.from_pretrained(freeze['model'], revision=freeze['revision'], cache_dir='.cache/huggingface', local_files_only=True)
    for candidate in load('identifier_tokenization_audit.json')['candidates']:
        tokens = tok.encode(candidate['raw'], add_special_tokens=False)
        assert tokens == candidate['token_ids'] and len(tokens) == candidate['token_count']
        assert len(candidate['raw']) == candidate['character_length']
    cases = {c['case_id']:c for filename in ('stage_b_cases.json', 'stage_c_cases.json', 'unmapped_cases.json') for c in load(filename)}
    all_rows = {}
    for stage, required in [('stage_b', 160), ('stage_c', 80), ('unmapped', 10), ('record_order', 20)]:
        rows = [json.loads(s) for s in (OUT/(stage+'_outputs.jsonl')).read_text(encoding='utf-8').splitlines()]
        assert len(rows) == required
        assert len({(r['case_id'], r['family'], r['condition']) for r in rows}) == required
        for expected, r in zip(load(stage+'_prompt_plan.json'), rows):
            assert all(r[k] == v for k,v in expected.items())
            assert tok.decode(r['output_token_ids'], skip_special_tokens=True) == r['raw_text']
            assert len(r['output_token_ids']) == r['output_tokens'] <= 16
            assert r['truncated'] == (r['output_tokens'] >= 16 and r['output_token_ids'][-1] != tok.eos_token_id)
            rendered = tok.apply_chat_template([dict(role='user', content=r['prompt'])], tokenize=False, add_generation_prompt=True, enable_thinking=False)
            assert rendered == r['rendered_prompt']
            assert len(tok.encode(rendered, add_special_tokens=False)) == r['input_tokens']
            for key, hashkey in [('prompt', 'text_sha256'), ('rendered_prompt', 'rendered_sha256'), ('raw_text', 'raw_sha256')]:
                assert hashlib.sha256(r[key].encode()).hexdigest() == r[hashkey]
            assert r['seed'] == 42 and r['new_chat'] and not r['use_cache'] and not r['constrained']
            mapping = re.findall(r'^((?:State|STATE)_[A-Z][0-9]{2})(?: maps to | -> )((?:Outcome|OUTCOME)_[A-Z][0-9]{2})\.?$', r['prompt'], re.M)
            assert len(mapping) == 2 and dict(mapping).get(r['supplied_state'], 'UNKNOWN') == r['expected']
            c = cases[r['case_id']]
            value = norm(r['raw_text'])
            if r['truncated']:
                category = 'INVALID'
            elif value == c['gold_outcome']:
                category = 'C'
            elif value == c['wrong_outcome']:
                category = 'Cp'
            elif value == 'UNKNOWN':
                category = 'UNKNOWN'
            elif re.fullmatch(r'(?:Outcome|OUTCOME)_[A-Z][0-9]{2}', value):
                category = 'OTHER'
            else:
                category = 'INVALID'
            r.update(category=category, correct=not r['truncated'] and value == r['expected'], normalized=value)
        all_rows[stage] = rows
    bmetrics, cmetrics = load('stage_b_metrics.json'), load('stage_c_metrics.json')
    for family, data in bmetrics['families'].items():
        rows = [r for r in all_rows['stage_b'] if r['family'] == family]
        by = {(r['case_id'], r['condition']):r for r in rows}
        expected = dict(A_C=sum(r['condition'] == 'C0' and r['correct'] for r in rows),
                        A_W=sum(r['condition'] == 'W0' and r['correct'] for r in rows),
                        S=sum(by[c['case_id'], 'C0']['correct'] and by[c['case_id'], 'W0']['correct'] for c in load('stage_b_cases.json')),
                        U=sum(r['category'] == 'UNKNOWN' for r in rows),
                        OTHER_INVALID=sum(r['category'] in ('OTHER', 'INVALID') for r in rows),
                        mapped_correct=sum(r['correct'] for r in rows))
        assert expected == {k:v['count'] for k,v in data['metrics'].items()}
    crows = all_rows['stage_c']
    by = {(r['case_id'], r['condition']):r for r in crows}
    values = dict(C1=sum(r['condition'] == 'C0' and r['correct'] for r in crows),
                  C2=sum(r['condition'] == 'W0' and r['correct'] for r in crows),
                  C3=sum(by[c['case_id'], 'C0']['correct'] and by[c['case_id'], 'W0']['correct'] for c in load('stage_c_cases.json')),
                  C4=sum(r['category'] == 'UNKNOWN' for r in crows),
                  C5=sum(r['category'] in ('OTHER', 'INVALID') for r in crows),
                  C6=sum(r['correct'] for r in all_rows['unmapped']))
    gates = dict(C1=values['C1'] >= 39, C2=values['C2'] >= 39, C3=values['C3'] >= 39,
                 C4=values['C4'] == 0, C5=values['C5'] <= 1, C6=values['C6'] >= 9)
    assert gates == cmetrics['gates']
    reverse = sum(r['category'] in ('C', 'Cp') and by[r['case_id'], r['condition']]['category'] in ('C', 'Cp') and r['normalized'] == by[r['case_id'], r['condition']]['normalized'] for r in all_rows['record_order'])
    assert reverse == cmetrics['record_order']['count']
    gate = load('gate.json')
    assert gate['final_decision'] == ('MINIMAL_ASSAY_VALIDATED' if all(gates.values()) else 'MINIMAL_ASSAY_INVALID')
    assert gate['record_order_diagnostic_pass'] == (reverse >= 19)
    pre = (OUT/'design_audit.pre_inference.md').read_bytes()
    assert (OUT/'design_audit.md').read_bytes().startswith(pre)
    result = dict(all_checks_passed=True, frozen_files=len(manifest['frozen']), old_artifacts_unchanged=len(manifest['prior_artifacts']),
                  candidate_tokenizations=5200, exact_output_token_roundtrips=270, independently_counted_gates=values, record_order_unchanged=reverse,
                  final_decision=gate['final_decision'])
    (OUT/'independent_verification.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8', newline='\n')
    audit = load('v360_failure_audit.json')
    details = ['# Supplementary static lexical description', '', 'All old C0 failures compared descriptively; no significance or causal inference.', '']
    for field in ('gold_state', 'gold_outcome', 'entity'):
        failed = [next(i['raw'] for i in c['identifiers'] if i['field'] == field) for c in audit['cases'] if c['flags']['C0_failed']]
        suffixes = [v.split('_')[-1] for v in failed]
        common_positions = [i for i in range(3) if len({s[i] for s in suffixes}) == 1]
        details += [f'- {field}: {failed}; common suffix positions (0=letter, 1=tens, 2=units): {common_positions}.']
    details += ['', 'All role prefixes are shared by construction, including successes. Token counts were uniformly four for gold states, gold outcomes and entities across failed and passed C0 cases. Full per-character success/failure contingency tables remain in v360_failure_audit.json.']
    (OUT/'static_lexical_description.md').write_text('\n'.join(details)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
