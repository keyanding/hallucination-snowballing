"""Pre-inference case/template freeze, including conditional pipeline rules."""
import importlib.metadata
import json
import random
import re
from datetime import datetime,timezone
from pathlib import Path
from transformers import AutoTokenizer
from experiments.v3_6_0.prepare import digest,MODEL
from experiments.v3_6_0.design import shuffled
from src.calibration_v3_4_1 import REVISION
from .design import make_cases,audit_pair,render,sha

OUT=Path('results/v3_6_3')
CAP=16


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def load(name):
    return read(OUT/name)


def write(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')


def text(name,value):
    (OUT/name).write_text(value,encoding='utf-8',newline='\n')


def verify():
    for path,value in load('manifest.json')['frozen'].items():
        assert digest(path)==value,path


def old_ids():
    files=['results/v3_6_0/calibration_cases.json','results/v3_6_0/main_cases.json','results/v3_6_1/stage_c_cases.json','results/v3_6_1/unmapped_cases.json','results/v3_6_2/cases.json']
    values=set()
    def walk(x):
        if isinstance(x,dict):
            for v in x.values():
                walk(v)
        elif isinstance(x,list):
            for v in x:
                walk(v)
        elif isinstance(x,str) and re.fullmatch(r'(ENTITY|STATE|OUTCOME)_[A-Z][0-9]{2}',x.upper()):
            values.add(x.upper())
    for file in files:
        walk(read(file))
    return values,files


def prepare():
    assert not OUT.exists(),'Never overwrite existing experiment'
    prior=read('results/v3_6_2/case_manifest.json')
    for path,value in prior['frozen'].items():
        assert digest(path)==value,path
    tok=AutoTokenizer.from_pretrained(MODEL,revision=REVISION,cache_dir='.cache/huggingface',local_files_only=True)
    old,sources=old_ids()
    cal,main,integrated,order,pool,audit=make_cases(tok,old)
    plans=dict(calibration=[r for c in cal for prefix in ('U','P') for r in audit_pair(c,prefix)],
               main_upstream=[],main_propagation=[r for c in main for r in audit_pair(c,'P')],
               integrated=[r for c in main if c['case_id'] in integrated for r in audit_pair(c,'I')],
               order_diagnostic=[r for c in main if c['case_id'] in order for r in audit_pair(c,'U',True)])
    rng=random.Random(366)
    for condition in ('U-GOLD','U-ALT'):
        subset=list(main)
        rng.shuffle(subset)
        plans['main_upstream'] += [render(c,condition) for c in subset]
    for i,key in enumerate(('calibration','main_propagation','integrated','order_diagnostic')):
        plans[key],_=shuffled(plans[key],363+i)
    for rows in plans.values():
        for r in rows:
            rendered=tok.apply_chat_template([dict(role='user',content=r['prompt'])],tokenize=False,add_generation_prompt=True,enable_thinking=False)
            r.update(rendered_prompt=rendered,rendered_sha256=sha(rendered))
    pipeline_order=[c['case_id'] for c in main]
    random.Random(367).shuffle(pipeline_order)
    plans['pipeline_case_order']=pipeline_order
    plans['pipeline_templates']=[render(c,'PIPELINE-GENERATED',supplied='{ACTUAL_NORMALIZED_U_GOLD_STATE}') for c in main]
    plans['pipeline_rule']='Use actual normalized U-GOLD STATE_[A-Z][0-9]{2}, including OTHER_STATE. INVALID/truncated: log skipped, no call. Never substitute expected state. Dynamic prompt and rendered hashes are logged after the already-persisted upstream response.'
    versions={n:importlib.metadata.version(n) for n in ('torch','transformers','bitsandbytes','accelerate','numpy')}
    assert versions==read('results/v3_6_2/decoding_freeze.json')['versions']
    assert sha(tok.chat_template)==digest('results/v3_6_2/chat_template.txt')
    assert max(r['token_count']+1 for r in audit)<=CAP
    OUT.mkdir(parents=True)
    original=Path('C:/Users/kding/Downloads/v3_6_3_two_hop_propagation_assay_spec.md').read_text(encoding='utf-8-sig')
    text('spec.md',original+'\n\n## Frozen execution details\n\nThe optional20-call upstream-order diagnostic is included. Maximum total is340 (80 calibration +200 modular +40 integrated +20 order). Pipeline outputs are generated from actual normalized U-GOLD states; their templates/builders and call order are frozen, actual prompt hashes are recorded at runtime.\n')
    text('chat_template.txt',tok.chat_template)
    write('calibration_cases.json',cal)
    write('main_cases.json',main)
    write('identifier_pool.json',pool)
    write('identifier_tokenization_audit.json',dict(old_sources=sources,old_ids_excluded=len(old),selected=360,pool_size=7800,candidates=audit))
    write('prompt_plan.json',plans)
    write('subsets.json',dict(integrated=integrated,order_diagnostic=order))
    write('decoding_freeze.json',dict(model=MODEL,revision=REVISION,versions=versions,cap=CAP,seed=42,do_sample=False,
          use_cache=False,enable_thinking=False,compute_dtype='torch.bfloat16',quantization='NF4 double quantization',chat_template_sha256=sha(tok.chat_template)))
    prereg='''# v3.6.3 pre-registration

## Data and call budget
20 calibration cases,40 disjoint fresh main cases.7800 candidate identifiers audited,360 chosen by lexical/tokenization rules only, globally unique, no overlap with v3.6.0–v3.6.2. Equal tokenizer counts and character lengths within role pairs, six distinct suffixes per case, no substring overlap. Upstream/downstream order independently balanced in each split (all four combinations5 calibration or10 main cases). No model-output-based selection.
80 calibration U-GOLD/U-ALT/P-GOLD/P-ALT calls; all A–G must pass before any main/secondary call. A/B/C/D≥19/20; E upstream both correct≥19/20; F propagation both correct≥19/20; G exact pair-member identifiers≥79/80. OTHER_STATE/OTHER_OUTCOME/UNKNOWN do not count as permitted for G. Wrong pair members can be permitted parses but fail correctness.
Main: U-GOLD40 first, U-ALT40 next; P-GOLD/P-ALT80; then up to40 generated pipeline calls; integrated40 and optional order20. Maximum total340, with no extra smoke or repeat calls. Greedy seed42,cap16,NF4/BF16,same pinned model/tokenizer/chat template, fresh stateless calls,use_cache=False,no constrained decoding. No reruns of failed calls.
Main upstream phase first guarantees U-GOLD precedes every pipeline call. Static stages have frozen shuffled schedules; pipeline case order is frozen. Integrated subset seed364 selects5 per upstream/downstream order cell; order subset10 cases seed365. Content and rules freeze before all inference.

## Templates and actual state forwarding
Use the exact U/P/I templates in the spec. U and I differ only in Current entity; P differs only in Recorded intermediate result. P has no entity or upstream evidence. The P shell differs from v3.6.1's Current state shell as explicitly specified; cross-version changes cannot isolate the upstream layer alone. Calibration separately validates the new shell.
Normalization: NFC, strip outer whitespace, remove one terminal period. No casefold or extraction. Upstream exact gold=B, alt=Bp, any other STATE_[A-Z][0-9]{2}=OTHER_STATE; all other text, UNKNOWN or truncation=INVALID. Downstream exact gold=C, alt=Cp, other OUTCOME_[A-Z][0-9]{2}=OTHER_OUTCOME, literal UNKNOWN, otherwise INVALID. A truncation is always INVALID.
Pipeline uses the actual normalized U-GOLD string whenever category B/Bp/OTHER_STATE. For an unmapped OTHER_STATE preserve it exactly, retain expected=null, and report downstream behavior without inventing a correct mapped answer. No UNKNOWN instruction is added. INVALID upstream skips the downstream call and counts as strict pipeline failure. Upstream raw/normalized value, category, source hash and skip/call status are logged. Full actual dynamic prompt/rendered hashes are saved after upstream output is persisted. The pipeline renderer, placeholder templates and schedule are frozen before inference; raw-state-dependent full prompts cannot exist before upstream generation.

## Main gates and reporting
G1 upstream gold≥39/40; G2 upstream alt≥39/40; G3 propagation gold≥39/40; G4 propagation alt≥39/40; G5 paired propagation≥39/40; G6 strict U-GOLD=B AND pipeline=C≥38/40. G7 OTHER_STATE+OTHER_OUTCOME+INVALID≤2/160 across the four static main arms only. Spontaneous downstream UNKNOWN is separately reported, not counted in G7, but can fail adherence gates.
Report Wilson95% for G1–G6, counts/denominators, paired upstream and propagation category tables. Strict E2E denominator40 includes all upstream-invalid skips. Conditional downstream denominator is number of correct U-GOLD outputs; if zero, rate=null. Incorrect upstream does not become successful E2E even if pipeline outputs C by chance. Failures split into invalid upstream, incorrect valid upstream, and downstream failure after correct upstream.
Integrated readiness is separate: I-GOLD≥19/20,I-ALT≥19/20,paired≥19/20. Not-run diagnostics have evaluated=false and ready=false, not evidence of inability. Order diagnostic desired≥19/20 unchanged AND correct compared with corresponding main upstream output; it never changes G1–G7. Prominently report any order errors, even if19/20 still meets the threshold.
Decision priority: real structural/runtime failures or missing required calls → INFRASTRUCTURE_FAILURE; failed calibration → STOP_TWO_HOP_CALIBRATION_INVALID with empty main files; else failed G1–G7 → TWO_HOP_PROPAGATION_ASSAY_INVALID; else TWO_HOP_PROPAGATION_ASSAY_VALIDATED. Pipeline-invalid intentional skips are not infrastructure failures. No case replacement, threshold tuning or automatic next phase.

## Claim boundary
Only synthetic upstream lookup and externally controlled recorded-state propagation are validated. Integrated final-answer success does not show internal intermediate-state use. No spontaneous hallucination rate, natural snowballing, equivalence of injected and natural errors, SHAR/HalluSE, neural mechanism or real-world generalization claim.
'''
    text('pre_registration.md',prereg)
    audit_md='''# Pre-inference design audit

| Intention | Feature | Check | Failure meaning |
|---|---|---|---|
| Add upstream mapping | Explicit A→B and symmetric alternative | New U gates; P shell tested separately | Stage/shell brittleness |
| Upstream capability | Balanced symmetric tables | A/B/E and G1/G2 | Lookup instability |
| Isolate intervention | Only recorded state changes | P literal diffs | Confounded propagation |
| Prevent recomputation | No upstream evidence in P | Prompt audit | Override possible |
| Actual modular chain | Forward actual normalized U-GOLD | Source-linked pipeline log | Repaired-state artifact |
| Avoid world knowledge | Fresh opaque IDs |7800-tokenizer audit;360 fresh IDs|Shortcut|
| No fallback interference | No UNKNOWN instruction |Template checks|Fallback brittleness|
| No candidate options | Mapping tables only |Exact prompt audit|Option artifact|
| Integrated diagnostic separate |20 seeded cases|Readiness outside G1–G7|Internal-use overclaim|
| Order diagnostic separate |10 seeded cases|Unchanged and correct≥19/20|Order limitation|
| No adaptive tuning |Frozen rules,subsets,templates|Hash verification|Post-hoc rescue|
| Phase I boundary |No next phase|Final diagnosis|Natural snowballing/SHAR overclaim|

Maximum340 calls including optional20-call order diagnostic. Dynamic pipeline templates and builder freeze before inference; actual prompts follow actual upstream strings and are hashed when built. Malformed upstream skips are recorded, never repaired.
'''
    text('design_audit.pre_inference.md',audit_md)
    text('design_audit.md',audit_md)
    diff=['# Literal prompt diff audit','','All U/P/I pairs change only their designated entity/state field. No gold/alt/wrong/correct labels, UNKNOWN instructions or numbered answer lists occur in model prompts.','']
    for c in cal+main:
        for prefix in ('U','P','I'):
            a,b=audit_pair(c,prefix)
            diff.append(f"- {c['case_id']}/{prefix}: {a['text_sha256']} → {b['text_sha256']}; PASS")
    text('prompt_diff_audit.md','\n'.join(diff)+'\n')
    code=list(Path('experiments/v3_6_3').glob('*.py'))+[Path('tests/test_v3_6_3.py'),Path('src/calibration_v3_4_1.py')]
    code += [Path(p) for p in prior['frozen'] if Path(p).suffix=='.py']
    frozen={str(p).replace('\\','/'):digest(p) for p in code+list(OUT.iterdir()) if p.name!='design_audit.md'}
    history={str(p).replace('\\','/'):digest(p) for p in Path('results').rglob('*') if p.is_file() and OUT not in p.parents}
    write('manifest.json',dict(created_utc=datetime.now(timezone.utc).isoformat(),frozen=frozen,prior_artifacts=history,maximum_calls=340))
    verify()
    print('Frozen60 cases,300 static calls and up to40 actual-state pipeline calls.',flush=True)


if __name__=='__main__':
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
