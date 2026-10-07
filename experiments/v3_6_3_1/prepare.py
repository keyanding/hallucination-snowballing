"""Freeze exact inherited interfaces, all cases, conditional schedules and gates."""
import importlib.metadata
import random
from datetime import datetime, timezone
from pathlib import Path
from transformers import AutoTokenizer
from experiments.v3_6_0.prepare import digest, MODEL
from experiments.v3_6_0.design import shuffled
from experiments.v3_6_3.prepare import read, old_ids as previous_ids
from experiments.inheritance import validate
from src.calibration_v3_4_1 import REVISION
from .design import make_cases, audit_pair, render, sha, identifiers

OUT = Path('results/v3_6_3_1')
CAP = 16


def load(name):
    return read(OUT/name)


def write(name, value):
    text(name, __import__('json').dumps(value, ensure_ascii=False, indent=2)+'\n')


def text(name, value):
    (OUT/name).write_text(value, encoding='utf-8', newline='\n')


def verify():
    for path, value in load('manifest.json')['frozen'].items():
        assert digest(path) == value, path
    validate((OUT/'spec.md').read_text(encoding='utf-8'), load('validated_inheritance.json'))


def old_ids():
    old, sources = previous_ids()
    extra = ['results/v3_6_3/calibration_cases.json', 'results/v3_6_3/main_cases.json']
    for file in extra:
        for c in read(file):
            old.update(c[r+'_'+f] for r in ('gold','alt') for f in ('entity','state','outcome'))
    return old, sources+extra


def inheritance():
    entries = [
        ('minimal downstream shell', 'v3.6.1/v3.6.2', 'Minimal mapped-state interface passed', 'FROZEN_REUSE', 'Reuse Current state shell exactly', 'Byte equality to both frozen renderers; calibration C/D/F/G'),
        ('mapped-state UNKNOWN policy', 'v3.6.1', 'Fallback unnecessary for mapped-state assay; tested alternatives brittle', 'FROZEN_REUSE', 'No UNKNOWN rule in any prompt', 'Literal prompt audit'),
        ('identifiers and parser', 'v3.6.1/v3.6.3', 'Opaque matched IDs and exact parsing established', 'FROZEN_REUSE', 'Same generator, expanded historical exclusion; exact v3.6.3 parser', '7800-candidate token audit, freshness and parser tests'),
        ('context accumulation', 'v3.6.2', 'No failures up to 24 irrelevant mappings', 'NOT_RELEVANT', 'Use two mappings without distractors', 'Exactly two downstream records'),
        ('record position', 'v3.6.2', 'No position failures observed in tested diagnostic', 'NOT_RELEVANT', 'No new main position manipulation; retain balanced order construction', 'Inherited order construction audit'),
        ('upstream shell', 'v3.6.3', 'Calibration upstream A/B/paired each 20/20', 'FROZEN_REUSE', 'Reuse upstream renderer exactly', 'Byte equality and calibration A/B/E/G'),
        ('recorded shell', 'v3.6.3', 'Recorded shell calibration had three exact-output failures', 'INTENTIONALLY_RETESTED', 'Exact former shell in independent diagnostic only', 'Paired same-state/mapping shell comparison; non-gating'),
        ('model and decoding', 'v3.6.1/v3.6.2/v3.6.3', 'Pinned NF4/BF16 stateless greedy stack used', 'FROZEN_REUSE', 'Same revision/tokenizer/chat template, seed42, cap16', 'Versions, template hash, render hash and runtime manifest'),
        ('integrated shell', 'v3.6.3', 'Integrated shell frozen but untested after failed calibration', 'INTENTIONALLY_RETESTED', 'Reuse exact integrated renderer on 20 main cases after main passes', 'Separate readiness thresholds, no main-gate effect'),
    ]
    return [dict(component=c, prior_version=v, prior_result=p, classification=k, treatment=t, validation=a, modified=False) for c,v,p,k,t,a in entries]


PREREG = '''# v3.6.3.1 pre-registration

## Validated Inheritance
The machine-readable validated_inheritance.json and table in spec.md are formal pre-inference inputs. Downstream prompts must equal v3.6.1 MINIMAL_NO_UNKNOWN and v3.6.2 K0 byte for byte after identifier substitution; U/I use the unchanged v3.6.3 renderer; exact parsing calls the unchanged v3.6.3 parser. The recorded shell is diagnostic only. No model, tokenizer, ID family, normalization, decoding, mapped-state UNKNOWN policy or candidate-list change.

## New manipulation
Forward actual normalized U-A output into the frozen Current state field. No repair, extraction, oracle replacement, relabeling or new wording. This is the only new pipeline operation.

## Data, sampling and schedules
20 calibration, 40 main and 10 additional shell-diagnostic cases are disjoint, with 420 globally unique fresh IDs. Integrated uses an intentional 20-case main subset: the spec's disjoint-diagnostic rule applies to the independent shell set, not this explicitly required subset. Exclude all v3.6.0–v3.6.3 case IDs, including unrun cases and distractors. Audit all 7800 ENTITY/STATE/OUTCOME_[A-Z][0-9]{2} candidates. Pair tokenizer counts and character lengths match; six suffixes differ within each case; no substring overlap.
The unchanged v3.6.3 lexical/tokenization generator (seed363, same minimum-token buckets and balanced order cells) constructs 20+40 fresh cases. Integrated subset retains its seed364 five-per-order-cell selection. For shell cases, call that same generator with all selected main/calibration IDs additionally excluded, then sample 10 of its 20 provisional calibration construction cases using seed3631. Discarded construction cases are never inferred; no selection uses model behavior. Diagnostic order-cell balance is not a gate.
Frozen scheduling: main U-A40 followed by U-B40 (case shuffles seed366); downstream80; pipeline in seed367 order. Calibration, downstream, shell and integrated lists are shuffled with seeds3631–3634 to avoid adjacent same-case calls. Their schedules are frozen, as are pipeline placeholders/builders.

## Conditional calls and exact gates
Calibration 80 (U-A/U-B/D-A/D-B). A/B/C/D correct≥19/20; E both upstream correct≥19/20; F both downstream correct≥19/20; G permitted exact paired identifiers≥79/80. OTHER_STATE/OTHER_OUTCOME/UNKNOWN are not permitted for G. Pair-member wrong answers can be permitted parses but fail accuracy. Any A–G failure stops all main/pipeline/diagnostics: STOP_V3631_CALIBRATION_INVALID.
Only after calibration passes: main static160 plus up to40 actual pipeline calls. Main G1–G4 adherence each≥39/40, G5 paired D switch≥39/40, G6 strict E2E≥38/40, G7 OTHER_STATE+OTHER_OUTCOME+INVALID≤2/160 static main calls only. Literal UNKNOWN is reported separately and not included in G7 (it still fails adherence). Strict E2E requires U-A=B AND pipeline=C, denominator40 including skips. Conditional P(pipeline=C | U-A=B) has denominator number of correct U-A and null rate if zero. Downstream chance recovery cannot rescue an upstream mistake. Report Wilson95% for G1–G6, paired U/D tables, and upstream-invalid/upstream-incorrect/downstream-after-correct-upstream failures.
After main completion, run shell diagnostic40 (10 cases ×2 states ×2 shells), whether or not main gates pass. The two shells have identical case mappings/order/supplied state. Diagnostic accuracy is non-gating. Only if all main G1–G7 pass, run integrated40 on the frozen 20-case main subset. I-A, I-B and paired each≥19/20 define separate INTEGRATED_TWO_HOP_READY. Unrun means evaluated=false/ready=false, not observed failure. Maximum360 calls =80+200+40+40. No order diagnostic, smoke calls, retry, replacement, cap increase, or next phase.
Priority: genuine runtime/structural error or missing required calls → INFRASTRUCTURE_FAILURE; failed cal → STOP_V3631_CALIBRATION_INVALID; failed main → TWO_HOP_PIPELINE_INVALID; otherwise TWO_HOP_PIPELINE_VALIDATED. A main failure intentionally omits integrated; it still requires shell calls. Shell accuracy/readiness never rescue or invalidate main gates.

## Normalization and pipeline
NFC, outer strip, one final period removed only. No casefold or extraction. Truncation always INVALID. Upstream: B/Bp/OTHER_STATE/INVALID. Downstream: C/Cp/OTHER_OUTCOME/UNKNOWN/INVALID. Pass valid states including OTHER_STATE through unchanged. For unmapped actual state, expected=null and downstream behavior is descriptive; no UNKNOWN instruction. INVALID upstream logs UPSTREAM_INVALID_SKIPPED, no downstream call, strict failure. Persist raw upstream output first, then log source raw/normalized/category/prompt hash and call/skip status before any pipeline call. Freeze dynamic builder, placeholder prompts and case order now; full actual prompt/rendered hashes become available only after actual upstream generation and are saved per call.

## Shell diagnostic reporting definitions
Per shell report exact accuracy/20, per-state accuracy/10, INVALID, explanation-format, prefix-omission and truncation counts plus same-case/state paired transitions. Prefix omission means INVALID normalized output exactly equals one of the two outcome suffixes. Explanation-format means INVALID with a standalone alphabetic word of length≥2 (regex word boundaries; underscore-joined IDs do not qualify). These are descriptive text flags, not semantic proof of explanation, and never repair an answer. Truncation uses the frozen generation stop rule. Flags may overlap. Compare both directions of discordant pairs without changing gates.

## Stack and boundary
Pinned Qwen/Qwen3-4B-Instruct-2507, inherited revision/chat template/versions, NF4 double quantization/BF16, no offload, greedy seed42, cap16, use_cache=False, fresh one-user chat, no constrained decoding. Greedy implements deterministic temperature-zero intent; sampling controls remain disabled exactly as in inherited generate(). No explanatory-output cap increase.
The study licenses synthetic modular lookup and externally supplied state propagation only. Prior shell compliance failures motivate the diagnostic; they do not prove a unique historical cause. The shell comparison changes the whole shell, not just its heading. Integrated accuracy does not establish internal intermediate use. No natural hallucination/snowballing, injected-natural equivalence, neural mechanism, SHAR/HalluSE or real-world claim; no next phase is run.
'''


def prepare():
    assert not OUT.exists(), 'Never overwrite existing experiment'
    prior = read('results/v3_6_3/manifest.json')
    for path, value in prior['frozen'].items():
        assert digest(path) == value, path
    tok = AutoTokenizer.from_pretrained(MODEL, revision=REVISION, cache_dir='.cache/huggingface', local_files_only=True)
    old, sources = old_ids()
    cal, main, diagnostic, integrated, pool, audit = make_cases(tok, old)
    plans = dict(calibration=[r for c in cal for p in ('U','D') for r in audit_pair(c,p)],
                 main_upstream=[], main_downstream=[r for c in main for r in audit_pair(c,'D')],
                 shell_diagnostic=[r for c in diagnostic for shell in ('VALIDATED','RECORDED') for r in audit_pair(c,'D',shell)],
                 integrated=[r for c in main if c['case_id'] in integrated for r in audit_pair(c,'I')])
    rng = random.Random(366)
    for condition in ('U-A','U-B'):
        subset = list(main)
        rng.shuffle(subset)
        plans['main_upstream'] += [render(c,condition) for c in subset]
    for i,key in enumerate(('calibration','main_downstream','shell_diagnostic','integrated')):
        plans[key], _ = shuffled(plans[key],3631+i)
    for rows in plans.values():
        for r in rows:
            rendered = tok.apply_chat_template([dict(role='user',content=r['prompt'])],tokenize=False,add_generation_prompt=True,enable_thinking=False)
            r.update(rendered_prompt=rendered,rendered_sha256=sha(rendered))
    order = [c['case_id'] for c in main]
    random.Random(367).shuffle(order)
    plans['pipeline_case_order'] = order
    plans['pipeline_templates'] = [render(c,'PIPELINE-A',supplied='{ACTUAL_NORMALIZED_U_A_STATE}') for c in main]
    plans['pipeline_rule'] = 'Forward actual normalized U-A B/Bp/OTHER_STATE unchanged; INVALID/truncated skips. Runtime full hashes; frozen builder and placeholders. No UNKNOWN instruction.'
    plans['stage_rules'] = dict(calibration=80,main_static=160,pipeline_max=40,shell_diagnostic=40,integrated=40,maximum=360,
                               shell_requires='calibration pass and main completion',integrated_requires='main G1-G7 pass')
    versions = {n:importlib.metadata.version(n) for n in ('torch','transformers','bitsandbytes','accelerate','numpy')}
    assert versions == read('results/v3_6_3/decoding_freeze.json')['versions']
    assert sha(tok.chat_template) == digest('results/v3_6_3/chat_template.txt')
    assert max(r['token_count']+1 for r in audit) <= CAP
    table = inheritance()
    table_md = '| Prior | Component / result | Classification | Treatment | Validation |\n|---|---|---|---|---|\n'+'\n'.join(f"| {r['prior_version']} | {r['component']}: {r['prior_result']} | {r['classification']} | {r['treatment']} | {r['validation']} |" for r in table)+'\n'
    original = Path('C:/Users/kding/Downloads/v3_6_3_1_two_hop_pipeline_frozen_interface_spec.md').read_text(encoding='utf-8-sig')
    spec = '# v3.6.3.1 effective specification\n\n## Validated Inheritance\n\n'+table_md+'\n## New manipulation\n\nActual U-A output is forwarded unchanged into the validated Current state interface.\n\n## Execution resolutions\n\n'+PREREG+'\n\n---\n\n## Supplied source specification (verbatim text)\n\n'+original
    validate(spec,table)
    OUT.mkdir(parents=True)
    text('spec.md',spec)
    text('pre_registration.md',PREREG)
    text('chat_template.txt',tok.chat_template)
    write('validated_inheritance.json',table)
    for name,rows in (('calibration',cal),('main',main),('diagnostic',diagnostic)):
        write(name+'_cases.json',rows)
    write('identifier_pool.json',pool)
    write('identifier_tokenization_audit.json',dict(old_sources=sources,old_ids_excluded=len(old),selected=420,pool_size=7800,candidates=audit))
    write('prompt_plan.json',plans)
    write('subsets.json',dict(integrated=integrated))
    write('decoding_freeze.json',dict(model=MODEL,revision=REVISION,versions=versions,cap=CAP,seed=42,do_sample=False,use_cache=False,
          enable_thinking=False,compute_dtype='torch.bfloat16',quantization='NF4 double quantization',chat_template_sha256=sha(tok.chat_template)))
    pre = '# Pre-inference design audit\n\n'+table_md+'\n'+'''All 70 cases passed literal U/D/I A/B diffs; every validated downstream pair equals both v3.6.1 and v3.6.2 renderers byte for byte. Upstream/integrated/recorded diagnostic reuse v3.6.3 source directly. Main has no recorded heading, entities in downstream, UNKNOWN instructions or answer lists. 420 fresh unique IDs from 7800 tokenized candidates; matched role-pair token and character counts. Calibration/main/shell sets disjoint; integrated intentionally a main subset. No model outputs used for selection.

Maximum360 calls. Calibration gates precede any main/diagnostic call; main gates precede integrated only; independent shell diagnostic follows completed main regardless of main accuracy. Actual pipeline state is never repaired. Templates/builders and parser/gates are frozen; dynamic full hashes are saved at execution. No cap increase or next phase. Shell flags are frozen descriptive heuristics; no mechanism inference. Workflow validator and source comparison checks passed.
'''
    text('design_audit.pre_inference.md',pre)
    text('design_audit.md',pre)
    diff = ['# Literal prompt and inheritance audit','','For each case: U/I differ only by entity; D by state. Validated D equals v3.6.1 minimal and v3.6.2 K0 bytes; RECORDED appears only in the shell diagnostic. Pipeline placeholders use the identical validated D shell.','']
    for c in cal+main+diagnostic:
        for prefix,shell in (('U','VALIDATED'),('D','VALIDATED'),('I','VALIDATED'),('D','RECORDED')):
            a,b = audit_pair(c,prefix,shell)
            diff.append(f"- {c['case_id']}/{prefix}/{shell}: {a['text_sha256']} → {b['text_sha256']}; PASS")
    text('prompt_diff_audit.md','\n'.join(diff)+'\n')
    code = list(Path('experiments/v3_6_3_1').glob('*.py'))+[Path('experiments/inheritance.py'),Path('EXPERIMENT_WORKFLOW.md'),Path('tests/test_v3_6_3_1.py')]
    code += [Path(p) for p in prior['frozen'] if Path(p).suffix=='.py']
    frozen = {str(p).replace('\\','/'):digest(p) for p in code+list(OUT.iterdir()) if p.name!='design_audit.md'}
    history = {str(p).replace('\\','/'):digest(p) for p in Path('results').rglob('*') if p.is_file() and OUT not in p.parents}
    write('manifest.json',dict(created_utc=datetime.now(timezone.utc).isoformat(),frozen=frozen,prior_artifacts=history,maximum_calls=360))
    verify()
    print('Frozen70 cases,320 static calls and up to40 actual-state pipeline calls.',flush=True)


if __name__ == '__main__':
    if OUT.exists():
        raise SystemExit('Existing experiment: preparation refused without modifying any file')
    try:
        prepare()
    except Exception:
        import traceback
        OUT.mkdir(parents=True,exist_ok=True)
        write('preparation_failure.json',dict(error=traceback.format_exc()))
        write('gate.json',dict(final_decision='INFRASTRUCTURE_FAILURE',INTEGRATED_TWO_HOP_READY=False))
        raise
