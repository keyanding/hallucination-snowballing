"""Freeze all Stage A/B/C inputs before any model call."""
import importlib.metadata
import json
import random
from datetime import datetime, timezone
from pathlib import Path
from transformers import AutoTokenizer
from .design import build_cases, audit_pair, render, sha, FAMILIES, RULE
from .audit import static_audit
from experiments.v3_6_0.design import shuffled
from experiments.v3_6_0.prepare import digest, MODEL
from src.calibration_v3_4_1 import REVISION

OUT = Path('results/v3_6_1')
OLD = Path('results/v3_6_0')
CAP = 16


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def load(name):
    return read(OUT/name)


def write(name, value):
    (OUT/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')


def text(name, value):
    (OUT/name).write_text(value, encoding='utf-8', newline='\n')


def verify():
    for path, expected in load('manifest.json')['frozen'].items():
        assert digest(path) == expected, path


def availability():
    paths = [Path('.cache/huggingface'), Path.home()/'.cache/huggingface/hub']
    import os
    for variable in ('HF_HOME', 'HF_HUB_CACHE', 'TRANSFORMERS_CACHE'):
        value = os.environ.get(variable)
        if value:
            paths.append(Path(value))
    inventory = {str(p):sorted(x.name for x in p.glob('models--*')) for p in paths}
    return dict(checked_local_model_caches=inventory, compatible_stronger_model_available=False,
                reason='Only the existing Qwen3-4B checkpoint is available in configured/default caches; no stronger-model endpoint is configured in the existing inference adapter. No download or ad hoc infrastructure.',
                conditional_status='STRONGER_MODEL_DIAGNOSTIC_NOT_RUN', selection_seed=1361,
                selection_rule='If Stage C fails and a compatible stronger model is available: all incorrect Stage C mapped calls plus equal-size seeded sample of correct mapped calls. No replacement, no new prompts. If fewer correct calls than failures, report design infeasible instead of silently reducing or duplicating controls.')


def prepare():
    assert not OUT.exists(), 'Never overwrite a frozen experiment'
    oldmanifest = read(OLD/'case_manifest.json')
    for path, expected in oldmanifest['frozen'].items():
        assert digest(path) == expected, path
    tok = AutoTokenizer.from_pretrained(MODEL, revision=REVISION, cache_dir='.cache/huggingface', local_files_only=True)
    oldcal, oldmain = read(OLD/'calibration_cases.json'), read(OLD/'main_cases.json')
    oldoutputs = [json.loads(x) for x in (OLD/'calibration_outputs.jsonl').read_text(encoding='utf-8').splitlines()]
    static, static_md = static_audit(oldcal, oldoutputs, tok)
    cases, controls, pool, tokens, checks = build_cases(tok, oldcal+oldmain)
    selected = random.Random(362).sample(cases, 10)
    b = [r for c in oldcal for f in FAMILIES for r in audit_pair(c, f)]
    primary = [r for c in cases for r in audit_pair(c)]
    unmapped = [render(c, 'UNMAPPED') for c in controls]
    reversed_rows = [r for c in selected for r in audit_pair(c, reverse=True)]
    # Exact controlled factor checks, independently of generation outputs.
    for c in oldcal:
        for k in ('C0', 'W0'):
            for shape in ('FULL', 'MINIMAL'):
                assert render(c, k, shape+'_NO_UNKNOWN')['prompt']+'\n'+RULE == render(c, k, shape+'_UNKNOWN')['prompt']
    plans = dict(stage_b=b, stage_c=primary, unmapped=unmapped, record_order=reversed_rows)
    for i, (key, rows) in enumerate(plans.items()):
        for row in rows:
            rendered = tok.apply_chat_template([dict(role='user', content=row['prompt'])], tokenize=False, add_generation_prompt=True, enable_thinking=False)
            row.update(rendered_prompt=rendered, rendered_sha256=sha(rendered), stage=key)
        plans[key], _ = shuffled(rows, 361+i)
    assert [len(r) for r in plans.values()] == [160, 80, 10, 20]
    max_tokens = max(len(tok.encode(r['expected'], add_special_tokens=False))+1 for rows in plans.values() for r in rows)
    assert max_tokens <= CAP
    versions = {n:importlib.metadata.version(n) for n in ('torch', 'transformers', 'bitsandbytes', 'accelerate', 'numpy')}
    assert versions == read(OLD/'decoding_freeze.json')['versions']
    assert sha(tok.chat_template) == digest(OLD/'chat_template.txt')
    available = availability()
    assert all(names in ([], ['models--Qwen--Qwen3-4B-Instruct-2507']) for names in available['checked_local_model_caches'].values()), 'Inspect discovered stronger model before freezing'
    OUT.mkdir(parents=True)
    text('spec.md', Path('C:/Users/kding/Downloads/v3_6_1_minimal_propagation_diagnosis_spec.md').read_text(encoding='utf-8-sig'))
    text('chat_template.txt', tok.chat_template)
    write('v360_failure_audit.json', static)
    text('v360_failure_audit.md', static_md)
    write('identifier_pool.json', pool)
    write('identifier_tokenization_audit.json', dict(selection_seed=361, checks=checks, candidates=tokens))
    write('stage_b_cases.json', oldcal)
    write('stage_c_cases.json', cases)
    write('unmapped_cases.json', controls)
    write('record_order_cases.json', [c['case_id'] for c in selected])
    for key, rows in plans.items():
        write(key+'_prompt_plan.json', rows)
    write('stronger_model_availability.json', available)
    write('decoding_freeze.json', dict(model=MODEL, revision=REVISION, versions=versions, cap=CAP,
          max_expected_tokens_with_eos=max_tokens, seed=42, do_sample=False, use_cache=False, enable_thinking=False,
          quantization='4bit-nf4 double quantization', compute_dtype='torch.bfloat16', chat_template_sha256=sha(tok.chat_template)))
    prereg = '''# v3.6.1 pre-registration

## Fixed execution
Stage A: all 20 old calibration cases, static only. Stage B: 20 × 2 × 4 = 160 calls. Stage C: 40 × 2 = 80 mapped calls, 10 separate unmapped controls, 20 separate record-order calls. Total 270 new 4B calls. Stage C runs regardless of Stage B results, unless infrastructure fails.
All cases and renderings are frozen before inference; greedy cap16, seed42, fresh chat, no cache or constrained output; same pinned Qwen3/NF4/BF16 stack as v3.6.0. Cases seed361, reverse sample362; call shuffle seeds361/362/363/364. No cap increases or automatic reruns.

## Controlled Stage B factors
All 20 original calibration cases and both states; original mapping associations/order preserved. FULL uses the v3.6.0 prompt minus its UNKNOWN line. The exact new UNKNOWN sentence is appended to FULL/MINIMAL +UNKNOWN variants. Therefore FULL_UNKNOWN is not a byte-identical v3.6.0 replay; comparisons with v3.6.0 also change UNKNOWN wording. Within v3.6.1 matched +/-UNKNOWN pairs differ only by that one line. FULL vs MINIMAL is the specified bundled surface-form manipulation (entity, prose, mapping syntax); it cannot attribute an effect to entity alone.
A_C and A_W denominators20; S20; false-UNKNOWN40. Report all six paired family comparisons, each by C0/W0, exact categories and case outputs. Best descriptive family means maximum total mapped correct/40, all ties retained. No significance tests or post-hoc family choice for Stage C.
P1: report exact accuracy and UNKNOWN deltas for both matched comparisons, with corrected/broken counts. No invented cutoff for 'material'. P2: report matched full/minimal contrasts. P3: MINIMAL_NO_UNKNOWN <39/40 is a diagnostic signal; Section10 governs execution of stronger-model checks (Stage C invalid AND available compatible model).

## Fresh cases
5200 candidates are tokenized before selection. Exclude every suffix from all 60 v3.6.0 cases. For each role select the smallest observed token-count bucket, deterministic shuffle, then lexical constraints only. Equal token counts and character lengths within each state/outcome pair; globally unique IDs, no substrings, no suffix characters shared between any case state and outcome. Gold mapping first20/40, second20/40. Ten controls use fresh disjoint IDs. No entity in Stage C. No outcome-based selection.

## Parser and gates
NFC, outer strip, remove one terminal period only. No case folding or extraction. Exact gold=C, alternative=Cp, exact UNKNOWN; single well-formed Outcome/OUTCOME_[A-Z][0-9]{2} outside case=OTHER; all other outputs or truncations=INVALID. Expected correctness separately recorded. Main denominator40 paired cases, not80 independent units. Wilson95% intervals for A_C/A_W/S.
C1: gold ≥39/40; C2: wrong ≥39/40; C3: paired ≥39/40; C4: mapped UNKNOWN=0/80; C5: OTHER+INVALID≤1/80; C6: unmapped UNKNOWN≥9/10. All six required. Reverse diagnosis: ≥19/20 identical normalized mapped outcomes vs matched primary (both must be C/Cp); correctness separately reported. This is a limitation check, not an additional C gate.
Final decision exactly MINIMAL_ASSAY_VALIDATED, MINIMAL_ASSAY_INVALID or INFRASTRUCTURE_FAILURE. Missing required calls due to infrastructure means INFRASTRUCTURE_FAILURE; no silent retries or partial-rate decisions.

## Stronger-model availability and claim boundary
Local configured/default caches contain only the 4B checkpoint. No compatible stronger model is already available; no new download or ad hoc service. Record STRONGER_MODEL_DIAGNOSTIC_NOT_RUN with reason, and preserve any trigger. If Stage C fails only fallback or there are no mapped failures, the specified matched stronger-model sample is empty and cannot diagnose fallback. No task alteration.
Even validation licenses only reliable explicit symbolic state-to-outcome following under this minimal prompt. It establishes no natural hallucination, multi-hop snowballing, internal mechanism, SHAR behavior, arbitrary-context robustness or real-world reasoning. No next phase automatically.
'''
    text('pre_registration.md', prereg)
    audit_md = '''# Pre-inference design audit

| Intention | Feature | Observable check | Failure meaning |
|---|---|---|---|
| Diagnose all old cases | 20 × four families × two states |160 frozen calls|No cherry-picking|
| UNKNOWN interference | One-line matched factor |Exact prompt assertions|Contaminated factor|
| Prompt complexity | Specified full/minimal templates |Preserved mappings/states|Bundled surface contrast only|
| Remove entity | No entity in C |Template assertions|Entity confound|
| Tokenization balance |5200 audited candidates|Equal within-pair tokens and lengths|Construction asymmetry|
| Causal contrast |Supplied state only|40 literal pair diffs|Intervention confound|
| Fallback separate |10 disjoint controls|≥9/10 UNKNOWN|Fallback unreliable|
| Avoid answer options |Only mapping evidence|No candidate list|Option artifact|
| Order diagnosis |10 seeded cases × two states|≥19/20 unchanged mapped identity|Order limitation, not gate rescue|
| Model-size diagnosis |Only conditional and available|Availability frozen; same prompts|No inference about size without data|
| Prevent optimization |Frozen hashes and C1–C6|Pre/post verification|Adaptive optimization|
| Claim boundary |Minimal primitive only|Final diagnosis|No SHAR/mechanism claim|

Stage C never depends on Stage B pass/fail. Total 270 calls. Static audit is descriptive, not causal.
FULL_UNKNOWN uses the spec's new UNKNOWN wording; it is not a byte-identical v3.6.0 replay.
'''
    text('design_audit.pre_inference.md', audit_md)
    text('design_audit.md', audit_md)
    diff = ['# Prompt diff audit', '', 'All pairwise C0/W0 literal diffs consist solely of the supplied state ID.', 'The +/-UNKNOWN factor is exactly one appended line. Mappings retain original association and order.', '']
    for key in ('stage_b', 'stage_c', 'record_order'):
        rows = plans[key]
        by = {(r['case_id'], r['family'], r['condition']):r for r in rows}
        for r in rows:
            if r['condition'] == 'C0':
                other = by[r['case_id'], r['family'], 'W0']
                diff.append(f"- {key}/{r['case_id']}/{r['family']}: PASS; C0 {r['text_sha256']}; W0 {other['text_sha256']}")
    text('prompt_diff_audit.md', '\n'.join(diff)+'\n')
    sources = list(Path('experiments/v3_6_1').glob('*.py'))+[Path('tests/test_v3_6_1.py')]
    sources += [Path(p) for p in oldmanifest['frozen'] if Path(p).suffix == '.py']
    frozen = {str(p).replace('\\', '/'):digest(p) for p in sources+list(OUT.iterdir()) if p.name != 'design_audit.md'}
    prior = {str(p).replace('\\', '/'):digest(p) for p in Path('results').rglob('*') if p.is_file() and OUT not in p.parents}
    write('manifest.json', dict(created_utc=datetime.now(timezone.utc).isoformat(), frozen=frozen, prior_artifacts=prior, planned_calls=270))
    verify()
    print('Frozen Stage A audit, 5200-tokenizer candidate audit and all 270 prompts.', flush=True)


if __name__ == '__main__':
    prepare()
