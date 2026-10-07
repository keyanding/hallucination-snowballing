"""Freeze all inputs before inference; never overwrite an existing experiment."""
import hashlib
import importlib.metadata
import json
from datetime import datetime, timezone
from pathlib import Path
from transformers import AutoTokenizer
from src.calibration_v3_4_1 import REVISION
from .design import make_cases, audit, validate_cases, shuffled, UNKNOWN_RULE

OUT = Path('results/v3_6_0')
MODEL = 'Qwen/Qwen3-4B-Instruct-2507'
CAP = 16
BOUNDARY = 'Under a validated synthetic state-dependent task, externally changing the intermediate state causes a predictable change in the downstream answer.'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(name, value):
    (OUT/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')


def load(name):
    return json.loads((OUT/name).read_text(encoding='utf-8'))


def verify():
    for path, expected in load('case_manifest.json')['frozen'].items():
        assert digest(path) == expected, path


def prepare():
    assert not OUT.exists(), 'Never overwrite a frozen experiment'
    cal, main = make_cases()
    checks = validate_cases(cal+main)
    tokenizer = AutoTokenizer.from_pretrained(MODEL, revision=REVISION, cache_dir='.cache/huggingface', local_files_only=True)
    plans = {}
    diff = ['# Exact prompt audit', '', 'All 60 C0/W0 pairs differ only in the supplied state identifier.',
            'All 20 entity controls replace only the two entity occurrences; reversal only changes mapping order.',
            'The following instruction is identical in all 240 planned calls:', '', UNKNOWN_RULE, '']
    for split, cases in [('calibration', cal), ('main', main)]:
        rows = []
        for c in cases:
            audited = audit(c, True)
            for k, row in audited.items():
                if split == 'main' and k not in ('C0', 'W0'):
                    continue
                rendered = tokenizer.apply_chat_template([dict(role='user', content=row['prompt'])], tokenize=False, add_generation_prompt=True, enable_thinking=False)
                row.update(rendered_prompt=rendered, rendered_sha256=hashlib.sha256(rendered.encode()).hexdigest())
                assert row['prompt'].count(UNKNOWN_RULE) == 1
                rows.append(row)
            diff.append(f"- {c['case_id']}: PASS; C0 {audited['C0']['text_sha256']}; W0 {audited['W0']['text_sha256']}")
        plans[split], attempts = shuffled(rows, 360 if split == 'calibration' else 361)
    assert len(plans['calibration']) == 160 and len(plans['main']) == 80
    lengths = [len(tokenizer.encode(c[k], add_special_tokens=False))+1 for c in cal+main for k in ('gold_outcome', 'wrong_outcome')]
    assert max(lengths) <= CAP
    OUT.mkdir(parents=True)
    original = Path('C:/Users/kding/Downloads/v3_6_0_propagation_assay_validation_spec.md').read_text(encoding='utf-8-sig')
    (OUT/'original_spec.md').write_text(original, encoding='utf-8', newline='\n')
    amended = original.replace('20\\times 7 = 140', '20\\times 8 = 160').replace('If any A–G fails:', 'If any A–H fails:')
    amended = amended.replace('- state-irrelevance control\n', '- state-irrelevance control\n- entity-label control\n')
    amended = amended.replace('If any A–H fails:', 'H. Entity-label robustness: at least **19/20** normalized outputs unchanged after replacing only the entity identifier.\n\nIf any A–H fails:')
    amended = amended.replace('Output only the outcome identifier.', 'Output only the outcome identifier.\n'+UNKNOWN_RULE)
    amended += '\n## User amendments frozen before inference\n\nEntity-label control is formal calibration, not auxiliary: 20 × 8 = 160 calls. A–H are mandatory; G ≥99% means at least 159/160. Main remains 40 × 2 = 80.\n\nThe exact UNKNOWN instruction above is included in every template, including direct lookups. F remains 18/20. No other thresholds or main design changed.\n'
    (OUT/'spec.md').write_text(amended, encoding='utf-8', newline='\n')
    prereg = f'''# v3.6.0 pre-registration

Frozen before any inference. Synthetic opaque cases only; calibration 20, main 40; disjoint identifiers.
Calibration: 160 calls (8 per case), including formal ENTITY_LABEL. Main: 80 calls only after A–H pass. Total maximum 240. No auxiliary model calls.
A ≥38/40 direct lookups; B ≥19/20 C0; C ≥19/20 W0; D ≥19/20 swap; E ≥19/20 reversal invariant; F ≥18/20 UNKNOWN; G ≥159/160 permitted parses; H ≥19/20 entity-label invariant.
E/H require two permitted normalized-identical outputs, compared with same-case C0; correctness is separately reported.
Any A–H failure: STOP_ASSAY_INVALID, zero main calls. Main G1 ≥38/40 C, G2 ≥38/40 Cp, G3 ≥36/40 paired switches, G4 ≤2/40 Cp under C0, G5 ≤2/80 OTHER+INVALID. UNKNOWN reported separately.
Main failure: STOP_MAIN_ASSAY_INVALID; all pass: ASSAY_VALIDATED. No follow-up phases automatically.
Normalization: NFC, outer whitespace, one terminal period; no case folding, no extraction. Truncation INVALID; other well-formed Outcome_[A-Z][0-9]{{2}} is OTHER. Only exact C/Cp/UNKNOWN permitted.
Wilson 95% intervals for A_C, A_W, S; paired 5×5 transition table; unit 40 base cases. Unrun main rates are null.
Case seed 360; call shuffle seeds 360/361; no adjacent same-case calls. Greedy seed 42, cap {CAP}, fresh chat, use_cache=False, no constrained output. No retuning or replacing cases.
Uniform instruction, frozen verbatim in all templates:
{UNKNOWN_RULE}
Model {MODEL}, revision {REVISION}, same NF4 double quantization and BF16 stack as v3.5.1.
Permitted conclusion only: {BOUNDARY}
No claim about natural hallucination, internal mechanisms, SHAR, or arbitrary real tasks.
'''
    (OUT/'pre_registration.md').write_text(prereg, encoding='utf-8', newline='\n')
    audit_text = '''# Pre-inference design audit

| Intention | Feature | Observable check | Failure meaning |
|---|---|---|---|
| Eliminate world knowledge | Opaque, disjoint IDs | 420 unique IDs; no real entities | Shortcut contamination |
| State-dependent answer | Two explicit mappings | C0/W0 gates | No state dependence |
| Isolate intervention | State-only diff | 60 exact pair assertions | Confounded contrast |
| Mapping capability | Direct lookups | A ≥38/40 | Capability failure |
| Prevent option primacy | No answer list | Prompt audit | Option artifact |
| Record order | Reversed mapping lines | E ≥19/20 unchanged | Order artifact |
| Mapping use | Swapped outcomes | D ≥19/20 | Mapping shortcut |
| Absent state | Uniform UNKNOWN rule | F ≥18/20 | Guessing |
| Entity identity | Only replace entity ID | H ≥19/20 unchanged | Entity artifact |
| No post-hoc rescue | Frozen A–H, G1–G5 and hashes | Verify before/after inference | Adaptive overfit |
| Claim boundary | Phase I only | Final diagnosis | Unsupported mechanism claim |

Calibration 160, main 80 conditional, maximum 240. G requires 159/160. No auxiliary calls.
Frozen UNKNOWN instruction: '''+UNKNOWN_RULE+'\n'
    for name in ('design_audit.pre_inference.md', 'design_audit.md'):
        (OUT/name).write_text(audit_text, encoding='utf-8', newline='\n')
    (OUT/'prompt_diff_audit.md').write_text('\n'.join(diff)+'\n', encoding='utf-8', newline='\n')
    (OUT/'chat_template.txt').write_text(tokenizer.chat_template, encoding='utf-8', newline='\n')
    write('calibration_cases.json', cal)
    write('main_cases.json', main)
    write('prompt_plan.json', plans)
    write('decoding_freeze.json', dict(model=MODEL, revision=REVISION, max_new_tokens=CAP, max_identifier_tokens_with_eos=max(lengths), seed=42, do_sample=False, use_cache=False, enable_thinking=False, quantization='NF4 double quantization', compute_dtype='torch.bfloat16', versions={n:importlib.metadata.version(n) for n in ('torch', 'transformers', 'bitsandbytes', 'accelerate', 'numpy')}))
    prior_model = json.loads(Path('results/v3_5_1/model_manifest.json').read_text(encoding='utf-8'))
    for path, expected in prior_model['frozen'].items():
        if Path(path).suffix == '.py':
            assert digest(path) == expected, path
    assert prior_model['runtime']['versions'] == load('decoding_freeze.json')['versions']
    assert prior_model['runtime']['chat_template_sha256'] == digest(OUT/'chat_template.txt')
    sources = list(Path('experiments/v3_6_0').glob('*.py')) + [Path('tests/test_v3_6_0.py'), Path('experiments/v3_5_1/run_pilot.py'), Path('experiments/v3_5_1/render_prompts.py'), Path('src/calibration_choice.py'), Path('src/generation/local_hf_adapter.py')]
    frozen = {str(p).replace('\\', '/'):digest(p) for p in sources+list(OUT.iterdir()) if p.name != 'design_audit.md'}
    prior = {str(p).replace('\\', '/'):digest(p) for p in Path('results').rglob('*') if p.is_file() and OUT not in p.parents}
    write('case_manifest.json', dict(created_utc=datetime.now(timezone.utc).isoformat(), checks=checks, frozen=frozen, prior_artifacts=prior, calibration_calls=160, main_calls=80, unknown_rule=UNKNOWN_RULE))
    verify()
    print('Frozen 60 cases, 160 calibration and 80 conditional main calls.', flush=True)


if __name__ == '__main__':
    prepare()
