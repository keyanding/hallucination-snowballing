"""Independent artifact and token audit; no inference or prompt modifications."""
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
from transformers import AutoTokenizer

OUT = Path('results/v3_6_0')


def load(name):
    return json.loads((OUT/name).read_text(encoding='utf-8'))


def main():
    manifest = load('case_manifest.json')
    for group in ('frozen', 'prior_artifacts'):
        for path, expected in manifest[group].items():
            assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected, path
    freeze = load('decoding_freeze.json')
    tok = AutoTokenizer.from_pretrained(freeze['model'], revision=freeze['revision'], cache_dir='.cache/huggingface', local_files_only=True)
    plan = load('prompt_plan.json')
    cases = {c['case_id']:c for split in ('calibration', 'main') for c in load(split+'_cases.json')}
    rows = {}
    counts = {}
    failures = []
    for split in ('calibration', 'main'):
        rows[split] = [json.loads(x) for x in (OUT/(split+'_outputs.jsonl')).read_text(encoding='utf-8').splitlines()]
        assert len(rows[split]) in ((160,) if split == 'calibration' else (0, 80))
        assert len({(r['case_id'], r['condition']) for r in rows[split]}) == len(rows[split])
        counts[split] = Counter()
        for expected, r in zip(plan[split], rows[split]):
            assert all(r[k] == v for k, v in expected.items())
            assert tok.decode(r['output_token_ids'], skip_special_tokens=True) == r['raw_text']
            assert len(r['output_token_ids']) == r['output_tokens'] <= 16
            assert r['truncated'] == (len(r['output_token_ids']) >= 16 and r['output_token_ids'][-1] != tok.eos_token_id)
            rendered = tok.apply_chat_template([dict(role='user', content=r['prompt'])], tokenize=False, add_generation_prompt=True, enable_thinking=False)
            assert rendered == r['rendered_prompt']
            assert len(tok.encode(rendered, add_special_tokens=False)) == r['input_tokens']
            for text_key, hash_key in [('prompt', 'text_sha256'), ('rendered_prompt', 'rendered_sha256'), ('raw_text', 'raw_sha256')]:
                assert hashlib.sha256(r[text_key].encode()).hexdigest() == r[hash_key]
            assert r['seed'] == 42 and r['new_chat'] and not r['use_cache'] and not r['constrained']
            mappings = dict(re.findall(r'^(State_[A-Z][0-9]{2}) maps to (Outcome_[A-Z][0-9]{2})\.$', r['prompt'], re.M))
            assert mappings.get(r['supplied_state'], 'UNKNOWN') == r['expected']
            value = unicodedata.normalize('NFC', r['raw_text']).strip().removesuffix('.')
            c = cases[r['case_id']]
            permitted = not r['truncated'] and value in (c['gold_outcome'], c['wrong_outcome'], 'UNKNOWN')
            correct = permitted and value == r['expected']
            counts[split][r['condition']] += correct
            if not correct:
                failures.append((r['case_id'], r['condition'], r['supplied_state'], r['expected'], value))
    by = {(r['case_id'], r['condition']):r for r in rows['calibration']}
    def norm(r):
        return unicodedata.normalize('NFC', r['raw_text']).strip().removesuffix('.')
    invariance = {}
    for condition in ('REVERSE', 'ENTITY_LABEL'):
        invariance[condition] = 0
        for c in load('calibration_cases.json'):
            a, b = by[c['case_id'], 'C0'], by[c['case_id'], condition]
            permitted = (c['gold_outcome'], c['wrong_outcome'], 'UNKNOWN')
            invariance[condition] += not a['truncated'] and not b['truncated'] and norm(a) in permitted and norm(a) == norm(b)
    cc = counts['calibration']
    gate_counts = dict(A=cc['LOOKUP_GOLD']+cc['LOOKUP_WRONG'], B=cc['C0'], C=cc['W0'], D=cc['SWAP'], E=invariance['REVERSE'], F=cc['UNMAPPED'], G=sum(not r['truncated'] and norm(r) in (cases[r['case_id']]['gold_outcome'], cases[r['case_id']]['wrong_outcome'], 'UNKNOWN') for r in rows['calibration']), H=invariance['ENTITY_LABEL'])
    metrics = load('metrics.json')
    assert gate_counts == {k:v['count'] for k,v in metrics['calibration']['gates'].items()}
    failed = [k for k,v in metrics['calibration']['gates'].items() if not v['passed']]
    gate = load('gate.json')
    if failed:
        assert gate['decision'] == 'STOP_ASSAY_INVALID' and not rows['main']
    pre = (OUT/'design_audit.pre_inference.md').read_bytes()
    assert (OUT/'design_audit.md').read_bytes().startswith(pre)
    result = dict(frozen_files=len(manifest['frozen']), prior_artifacts=len(manifest['prior_artifacts']), raw_token_roundtrips=sum(map(len, rows.values())), independent_calibration_counts=gate_counts, failed_calibration_gates=failed, main_calls=len(rows['main']), tests=90, all_checks_passed=True)
    (OUT/'independent_verification.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8', newline='\n')
    diagnosis = ['# Diagnosis', '', '**'+gate['decision']+'**', '', 'Failed calibration gates: '+(', '.join(failed) or 'none')+'.', '',
                 '## All calibration outputs differing from mapping-implied expected output', '', '| Case | Condition | Supplied state | Expected | Observed |', '|---|---|---|---|---|']
    diagnosis += ['| '+' | '.join(row)+' |' for row in failures]
    diagnosis += ['', '## Invariance interpretation', '',
                  'E and H compare the control output with the same-case C0 output. A control can answer correctly yet fail invariance if C0 was incorrect. Correct-by-condition counts are reported separately in metrics.json.',
                  'UNKNOWN is a permitted parse but is incorrect when the supplied state has a mapping. It therefore need not fail G while it can fail B or other correctness gates.', '',
                  'No failed cases were replaced, no prompt or threshold was tuned, and no further model calls were made beyond the gated run. These observations do not identify an internal cause.']
    (OUT/'diagnosis.md').write_text('\n'.join(diagnosis)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
