"""Freeze v3.6.2 with explicit user-approved gate definitions."""
import importlib.metadata
import json
from datetime import datetime, timezone
from pathlib import Path
from transformers import AutoTokenizer
from experiments.v3_6_0.prepare import digest, MODEL
from experiments.v3_6_0.design import shuffled
from experiments.v3_6_1.design import render as minimal_render, sha
from src.calibration_v3_4_1 import REVISION
from .design import make_cases, audit_pair, KS, BANDS

OUT=Path('results/v3_6_2')
CAP=16
AMENDMENT='''## User-approved decision amendment, frozen before inference

INFRASTRUCTURE_FAILURE is restricted to real structural/runtime/parser implementation faults: bad prompt/render/hash validation, missing calls, model exceptions or parser malfunction. Model-generated OTHER/INVALID is not by itself infrastructure failure.
Priority: INFRASTRUCTURE_FAILURE → BASE_ASSAY_REGRESSION → CONTEXT_SENSITIVE_ASSAY → ROBUST_CONTEXT_ASSAY.
If K0 C0<39/40, W0<39/40 or paired S<39/40, classify BASE_ASSAY_REGRESSION and stop context-size interpretation.
With valid K0, CONTEXT_SENSITIVE_ASSAY holds if any original sensitive criterion is met, or if monotonic collapse holds, or OTHER+INVALID>2/320 with healthy infrastructure/parser. Report off-target counts separately at each K.
Monotonic collapse means S(K0)≥S(K4)≥S(K12)≥S(K24), at least two strict decreases, and S(K0)−S(K24)≥4/40. Use exact integer paired-success counts.
All remaining structurally valid outcomes are ROBUST_CONTEXT_ASSAY. No post-inference threshold changes.
'''


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def load(name):
    return read(OUT/name)


def write(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')


def text(name,value):
    (OUT/name).write_text(value,encoding='utf-8',newline='\n')


def verify():
    for path,value in load('case_manifest.json')['frozen'].items():
        assert digest(path)==value,path


def old_identifiers():
    sources=['results/v3_6_0/calibration_cases.json','results/v3_6_0/main_cases.json',
             'results/v3_6_1/stage_c_cases.json','results/v3_6_1/unmapped_cases.json']
    values=set()
    for path in sources:
        for c in read(path):
            for key,value in c.items():
                if key.endswith('_state') or key.endswith('_outcome') or key in ('entity','alternate_entity'):
                    values.add(value.upper())
    return values,sources


def prepare():
    assert not OUT.exists(),'Never overwrite a frozen experiment'
    assert read('results/v3_6_1/gate.json')['final_decision']=='MINIMAL_ASSAY_VALIDATED'
    previous=read('results/v3_6_1/manifest.json')
    for path,value in previous['frozen'].items():
        assert digest(path)==value,path
    tok=AutoTokenizer.from_pretrained(MODEL,revision=REVISION,cache_dir='.cache/huggingface',local_files_only=True)
    old,sources=old_identifiers()
    cases,selected,pool,tokens,checks=make_cases(tok,old)
    main=[r for c in cases for k in KS for r in audit_pair(c,k)]
    diagnostic=[r for c in cases if c['case_id'] in selected for band in BANDS for r in audit_pair(c,24,band)]
    for c in cases:
        for r in audit_pair(c,0):
            assert r['prompt']==minimal_render(c,r['condition'])['prompt'],'K0 differs from validated minimal template'
    for rows in (main,diagnostic):
        for r in rows:
            rendered=tok.apply_chat_template([dict(role='user',content=r['prompt'])],tokenize=False,add_generation_prompt=True,enable_thinking=False)
            r.update(rendered_prompt=rendered,rendered_sha256=sha(rendered),input_tokens=len(tok.encode(rendered,add_special_tokens=False)))
    main,_=shuffled(main,362)
    diagnostic,_=shuffled(diagnostic,364)
    assert len(main)==320 and len(diagnostic)==72
    versions={n:importlib.metadata.version(n) for n in ('torch','transformers','bitsandbytes','accelerate','numpy')}
    assert versions==read('results/v3_6_1/decoding_freeze.json')['versions']
    assert sha(tok.chat_template)==digest('results/v3_6_1/chat_template.txt')
    max_output=max(len(tok.encode(r['expected'],add_special_tokens=False))+1 for r in main)
    assert max_output<=CAP
    max_input=max(r['input_tokens'] for r in main+diagnostic)
    assert max_input+CAP<tok.model_max_length
    OUT.mkdir(parents=True)
    original=Path('C:/Users/kding/Downloads/v3_6_2_context_accumulation_robustness_spec.md').read_text(encoding='utf-8-sig')
    text('original_spec.md',original)
    text('spec.md',original+'\n\n'+AMENDMENT)
    text('chat_template.txt',tok.chat_template)
    write('cases.json',cases)
    write('identifier_pool.json',pool)
    write('identifier_tokenization_audit.json',dict(checks=checks,old_identifier_sources=sources,candidates=tokens))
    write('prompt_plan.json',dict(main=main,position_diagnostic=diagnostic))
    positions=[{k:r[k] for k in ('case_id','k','condition','stage','position_band','gold_position','wrong_position','text_sha256','input_tokens')} for r in main+diagnostic]
    write('position_schedule.json',dict(seed=362,diagnostic_selection_seed=363,diagnostic_cases=selected,
          main_bands=checks['bands'],K0_note=checks['K0_band_applicability'],rows=positions,
          schedule_rule='Same case keeps beginning/middle/end band at positive K. Pair is adjacent. Gold-first20/wrong-first20. Within bands gold-first counts7/7/6 and wrong-first7/6/7. Middle selects prefixes of two fixed halves; removing new distractors recovers the exact lower-K mapping sequence.',
          diagnostic_rule='Seed363: two gold-first and two wrong-first cases per main band; all12 run at all3 bands, C0/W0. Distractor order fixed. One position per case duplicates primary K24 prompt but is executed as a fresh diagnostic call.'))
    write('decoding_freeze.json',dict(model=MODEL,revision=REVISION,versions=versions,cap=CAP,seed=42,
          do_sample=False,use_cache=False,enable_thinking=False,compute_dtype='torch.bfloat16',quantization='NF4 double quantization',
          chat_template_sha256=sha(tok.chat_template),max_expected_tokens_with_eos=max_output,max_input_tokens=max_input,tokenizer_model_max_length=tok.model_max_length))
    prereg='''# v3.6.2 pre-registration

40 fresh base cases × four K levels × C0/W0 =320 main calls. Twelve seeded cases × three K24 positions × C0/W0 =72 secondary calls. Total392. All main and diagnostic renderings frozen before any inference. No extra capability/smoke calls. Main calls shuffle seed362; diagnostics seed364; generation seed42; greedy cap16; fresh chat, use_cache=False, no constrained decoding. Same pinned Qwen3/NF4/BF16 stack and exact minimal K0 template as v3.6.1.

## Cases, nesting and position
Candidates: STATE/OUTCOME_[A-Z][0-9]{2},5200 IDs. Exclude old IDs case-insensitively across all v3.6.0 and v3.6.1 cases. Choose each role's smallest available tokenizer-length bucket, deterministic seed362, no model-output input. All2080 selected IDs are globally unique; each case has52 unique suffixes, equal character/token counts within state and outcome roles. Relevant state/outcome suffix characters do not overlap; each distractor state/outcome pair also has disjoint suffix characters.
Each case has24 distractors. All smaller blocks are exact order-preserving subsets of larger blocks, differing only by inserted irrelevant lines. Relevant pair adjacency/order remains fixed. Positive-K bands are beginning14, middle13, end13 across cases, same band across K per case. K0 only has two positions, so three-band placement is inapplicable there; gold-first20/wrong-first20. Beginning positions1/2; middle K/2+1,K/2+2; end K+1,K+2. This balances relative region, not absolute distance; added text also changes distance to the query, so no internal mechanism is isolated.
Secondary selection seed363: sample2 per gold-first/wrong-first cell in each main band (12 total). At K24 place the same pair at beginning/middle/end, holding all distractor content and relative order fixed. All72 calls execute even where24 prompts duplicate primary K24; report exact-repeat consistency, do not reuse outputs. No diagnostic result changes the main gate.

## Parser and statistics
Normalization only NFC, strip outer whitespace, remove one final period. No case folding/extraction. Exact gold=C, paired alternative=Cp, UNKNOWN literal, one other well-formed OUTCOME_[A-Z][0-9]{2}=OTHER; any explanation/multiple output or truncation=INVALID. OTHER may be a distractor outcome: record it separately, but count in off-target O. Model-generated invalid output does not mean parser implementation failed.
For each K: A_C/40,A_W/40,S/40,U/80,O/80, separate categories by C0/W0. Wilson95% intervals for A_C,A_W,S. Unit40 paired cases. Delta_C/Delta_W/Delta_S are integer count differences /40 vs K0. Report exact per-arm5×5 transitions, correct→incorrect and incorrect→correct, paired both-correct→not-both-correct and reverse, including all case IDs. No significance testing required. No pooling hides C0/W0.
On baseline regression collect the prespecified outputs but stop context-size interpretation. Missing required calls or structural/runtime/parser-code faults yield infrastructure failure. Secondary accuracy failures do not change the main gate. No reruns, case replacements, caps or thresholds adapted after inference.

'''+AMENDMENT+'''
## Claim boundary
Robustness licenses only reliable symbolic mapping under up to24 irrelevant records in this setting. Sensitivity is an observed controlled context effect, not hallucination snowballing or an internal explanation. Diagnose position with the secondary subset; do not generalize it to all40 cases. No upstream A→B layer, entities, conflicting evidence, natural hallucinations, SHAR/HalluSE or automatic next phase.
'''
    text('pre_registration.md',prereg)
    audit='''# Pre-inference design audit

| Intention | Feature | Observable check | Failure meaning |
|---|---|---|---|
| Preserve primitive | Exact v3.6.1 minimal template | K0 literal template check and replication | Base regression |
| Add only context | Nested irrelevant mappings | Lower K obtained by deletion only | Confounded intervention |
| Avoid world knowledge | Fresh opaque IDs |2080 unique IDs, no old overlap|Shortcut contamination|
| Avoid fallback interference | No UNKNOWN instruction |All392 prompts checked|Prior brittleness|
| Avoid answer list | Mapping block only |Exact template and regex audit|Candidate artifact|
| Separate region from size | Fixed band, balanced schedule,72 diagnostic calls |14/13/13 positive-K bands; K0 pair order20/20|Position limitation|
| Token balance | Same lexical family |All5200 tokenized, selected tokens/lengths matched|Surface asymmetry|
| Preserve state intervention | Only supplied state changes |196 literal C0/W0 pair checks|Contamination|
| Avoid adaptive optimization | Frozen inputs and user-amended gates |Hash checks|Post-hoc tuning|
| Preserve claim boundary | Context robustness only |Final diagnosis|Unsupported snowballing/SHAR claim|

392 planned calls. UNKNOWN is parsed if generated but never mentioned in a prompt. OTHER/INVALID counts are model outcomes, not infrastructure failure by themselves.
'''
    text('design_audit.pre_inference.md',audit)
    text('design_audit.md',audit)
    diff=['# Exact prompt differences','','196 C0/W0 pairs pass state-only literal comparison. All40 cases pass ordered nesting K0⊂K4⊂K12⊂K24; only distractor mapping lines are inserted. No prompt has UNKNOWN or an entity.','']
    by={(r['case_id'],r['k'],r['stage'],r['position_band'],r['condition']):r for r in main+diagnostic}
    for r in main+diagnostic:
        if r['condition']=='C0':
            b=by[r['case_id'],r['k'],r['stage'],r['position_band'],'W0']
            diff.append(f"- {r['stage']}/{r['case_id']}/K{r['k']}/{r['position_band']}: C0 {r['text_sha256']}; W0 {b['text_sha256']}; PASS")
    text('prompt_diff_audit.md','\n'.join(diff)+'\n')
    code=list(Path('experiments/v3_6_2').glob('*.py'))+[Path('tests/test_v3_6_2.py')]
    code += [Path(p) for p in previous['frozen'] if Path(p).suffix=='.py']
    frozen={str(p).replace('\\','/'):digest(p) for p in code+list(OUT.iterdir()) if p.name!='design_audit.md'}
    prior={str(p).replace('\\','/'):digest(p) for p in Path('results').rglob('*') if p.is_file() and OUT not in p.parents}
    write('case_manifest.json',dict(created_utc=datetime.now(timezone.utc).isoformat(),cases=cases,checks=checks,
          frozen=frozen,prior_artifacts=prior,main_calls=320,secondary_calls=72,gate_amendment=AMENDMENT))
    verify()
    print('Frozen40 cases,320 main calls,72 position diagnostics and user-approved gates.',flush=True)


if __name__=='__main__':
    try:
        prepare()
    except Exception:
        import traceback
        OUT.mkdir(parents=True,exist_ok=True)
        write('preparation_failure.json',dict(error=traceback.format_exc()))
        write('gate.json',dict(final_decision='INFRASTRUCTURE_FAILURE',context_interpretation_allowed=False))
        raise
