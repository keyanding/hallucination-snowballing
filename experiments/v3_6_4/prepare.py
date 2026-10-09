"""One-shot pre-inference freeze with a snapshot of the reviewed project ledger."""
import importlib.metadata
import json
import random
from datetime import datetime, timezone
from pathlib import Path
from transformers import AutoTokenizer
from experiments.v3_6_0.prepare import digest, MODEL
from experiments.v3_6_0.design import shuffled
from experiments.v3_6_3.prepare import read
from experiments.v3_6_3_1.prepare import old_ids as prior_ids
from scripts.validated_findings import review_spec, validate_data
from src.calibration_v3_4_1 import REVISION
from .design import make_cases, render, audit_cases, LEVELS, sha

OUT = Path('results/v3_6_4')
SOURCE = Path('experiments/v3_6_4')
CAP = 96


def load(name):
    return read(OUT/name)


def text(name, value):
    (OUT/name).write_text(value, encoding='utf-8', newline='\n')


def write(name, value):
    text(name, json.dumps(value, ensure_ascii=False, indent=2)+'\n')


def old_ids():
    old, sources = prior_ids()
    extra = [f'results/v3_6_3_1/{name}_cases.json' for name in ('calibration', 'main', 'diagnostic')]
    for path in extra:
        for c in read(path):
            old.update(c[k+'_'+role] for k in ('entity', 'state', 'outcome') for role in ('a', 'b'))
    return old, sources+extra


def ledger_review(data, ledger_hash):
    treatments = {
        'F01':('AVOIDED','Whole-output eligibility and independent confirmation; no denominator substitution.'),
        'F02':('AVOIDED','Synthetic explicit records avoid closed-book knowledge and birthplace granularity.'),
        'F05':('AVOIDED','No supporting prose that asserts a competing answer; exactly one gold path.'),
        'F06':('AVOIDED','No UNKNOWN instruction or fallback shell.'),
        'F07':('AVOIDED','No Recorded intermediate result shell or downstream inference.'),
        'F14':('AVOIDED','One frozen cap96; report truncation independently, exclude censored outputs from eligible yield; no sweep.'),
        'F15':('AVOIDED','No answer options or numbered candidate list; records are relational evidence.'),
        'F16':('INTENTIONALLY_RETESTED','Eight seeded selected-level record permutations; non-gating identity diagnostic.'),
        'F17':('AVOIDED','Only unconstrained greedy generation, no likelihood or constrained channel.'),
        'F18':('TARGETED','Qualify natural wrong-state yield on disjoint development and confirmation cases.'),
        'F19':('INTENTIONALLY_RETESTED','Pre-frozen 4/24 development and 3/24 confirmation wrong-yield thresholds.'),
        'F26':('OVERRIDDEN','Keep exact normalization/no repair; separate truncation flag from syntax category as required here.'),
        'F27':('OVERRIDDEN','Keep pinned stateless NF4/BF16 greedy stack; explicitly change cap16 to96.'),
        'C03':('FROZEN_REUSE','Reuse opaque ID family, token-count matching, unique suffixes and fresh historical exclusion.'),
    }
    rows = []
    for item in data['findings']+data['validated_components']:
        rid = item['id']
        treatment, rationale = treatments.get(rid, ('NOT_RELEVANT','No call tests this component or question; prior scope is preserved without claiming new validation.'))
        modified = rid in ('C02', 'C04', 'C05')
        if modified:
            treatment = 'INTENTIONALLY_RETESTED'
            rationale = {
                'C02':'Replace direct A-to-B lookup with entity-to-marker-to-state task; old direct lookup result does not transfer.',
                'C04':'Preserve normalization and no extraction; use four syntax/identity categories with orthogonal truncation.',
                'C05':'Reuse model/revision/quantization/greedy execution; cap96 replaces cap16 to reduce censoring.'}[rid]
        row = dict(id=rid, ledger_status=item['status'], treatment=treatment, rationale=rationale, modified=modified)
        if modified:
            row['modification'] = dict(component=rid, prior_evidence=item['evidence_files'], reason=rationale,
                                       prior_conclusion_no_longer_applies='Old exact-interface compliance does not validate this two-relation cap96 task.',
                                       revalidation_gate='Parser/control-flow unit tests plus frozen valid>=22/24, INVALID<=1/24, TRUNCATED<=1/24 and development/confirmation yield gates.')
        rows.append(row)
    review = dict(ledger_sha256=ledger_hash, latest_completed_version=data['future_spec_protocol']['latest_incorporated_version'], rows=rows)
    table = '| Finding / Component | Ledger status | Treatment in this experiment | Rationale |\n|---|---|---|---|\n'
    table += '\n'.join('| '+' | '.join(r[k] for k in ('id','ledger_status','treatment','rationale'))+' |' for r in rows)+'\n'
    return review, table


PREREG = '''# v3.6.4 pre-registration

## Data and manipulation
24 development and24 independent confirmation base cases; each has8 unique entity/marker/state paths and8 pre-frozen state-to-outcome mappings. Query is the first generated member; no gold label is shown. Seed3640 constructs all cases before inference. All1152 ENTITY/STATE/OUTCOME identifiers are globally unique and excluded from v3.6.0–v3.6.3.1 used or prepared cases. Every case has24 distinct suffixes. Token count is matched within each identifier family using the smallest eligible tokenizer bucket. Audit all7800 candidate identifiers; no model outputs select cases.
EASY/MID/HARD take the first3/5/8 paths of the same base case, retaining the same query/gold and the relative order of shared records. Entity records precede marker mappings. Two independently shuffled full8-member index orders (seed3640) are filtered for each level. Positions are random, not forced or claimed balanced. MID adds2 and HARD6 marker texture statements (smooth, rough, striped, dotted, plain, ridged); EASY has none. These add no entity-to-marker/state relation. Shared texture records remain identical. This compound selection-load manipulation adds relations and irrelevant attributes; it does not isolate their individual causal effects.
The frozen state universe for each rendered case is its visible3/5/8 states. The full8-state compatibility dictionary for every base case is prepared before outputs, never shown. Confirmation queries/entities/states/outcomes are disjoint from development. Markers/texture vocabulary intentionally recur; independence refers to fresh base cases and IDs, not an unobserved task distribution.

## Parsing and gate policy
Use the separately frozen user_resolution.json as the authoritative Valid-counting policy. Normalize NFC, outer strip and remove exactly one terminal period; no extraction, casefold or prefix repair. GOLD/TRACEABLE_WRONG/OUT_OF_UNIVERSE/INVALID depend on normalized whole text, regardless of truncation. TRUNCATED is orthogonal; censored responses never count as eligible Valid or qualified wrong. Always report raw categories and eligible counts separately. All denominators remain24, never filtered by validity. A completed wrong state qualifies only within the displayed case-level universe and its pre-frozen mapping. Confirmation tests independent yield, not recurrence of the same lexical state ID on disjoint cases.
Development qualifies with Valid>=22/24, eligible TRACEABLE_WRONG>=4/24, INVALID<=1/24, TRUNCATED<=1/24, and>=3 distinct wrong case IDs. Select easiest qualifying EASY, then MID, then HARD; no yield maximization. Confirmation same gates except wrong>=3/24. All criteria conjunctive. No threshold, case, budget, parser or prompt changes after inference.

## Schedules and conditional calls
72 development calls (seed3641 shuffled schedule with no adjacent same-case calls). All72 possible confirmation prompts and24 possible diagnostic prompts are frozen as contingencies, not all executed. Confirmation schedule shuffles24 cases per level using seeds3642/3643/3644. Eight development IDs sampled with seed3645, independent of model outputs. Each selected-level diagnostic uses one deterministic full record-block shuffle seeded by 'v364-order-'+case_id+'-'+level, leaving instructions/question unchanged. Maximum104 calls=72+24+8. No extra smoke, calibration, cap sweep, replay, scoring, constrained decoding or downstream calls.
If no development level qualifies, stop at72; confirmation/order files remain empty and evaluated=false. If a level qualifies, run24 confirmation then8 order calls regardless of confirmation success. No next experiment or automatic natural-state propagation. A genuine run/structure/hash/parser failure stops execution without retries or replacement.

## Non-gating order diagnostic
Compare paired normalized state identities only when both outputs are syntactically well-formed and untruncated (including OUT_OF_UNIVERSE); record incomparable pairs separately, never call unchanged prose a stable state. Report comparable coverage, same identity, changed identity, original/permuted Valid, both TRACEABLE_WRONG, same wrong identity, and all paired categories. More than3 of the fixed8 pairs changing identity sets ORDER_SENSITIVE_FRONTIER=true; otherwise false. Unrun means evaluated=false and flag=false, not observed stability. Invalid/incomparable pairs remain prominent even if flag=false. This diagnostic cannot alter the primary frontier gate.

## Inheritance and decision
Use the unchanged v3.5.1 generate() only (not its runner), same pinned Qwen3-4B-Instruct-2507 revision, tokenizer/chat template, NF4 double quantization/BF16, no offload, seed42, greedy, fresh one-user chats, use_cache=False; sole decoding change cap96. Token cap is a preventive choice, not a guarantee of no censoring. Snapshot prior ledger and verify all inherited source/result hashes before/after. C02 task, C04 category/truncation interface and C05 cap modifications are explicitly reviewed, not silently inherited validation.
Decision priority: real infrastructure failure/missing required calls -> INFRASTRUCTURE_FAILURE; no qualifying level -> NO_NATURAL_ERROR_FRONTIER; confirmation fail -> NATURAL_ERROR_FRONTIER_NOT_CONFIRMED; else NATURAL_ERROR_FRONTIER_CONFIRMED. Order flag separate.
Confirmed licenses reproducible nonzero natural first-hop wrong yield on this tested synthetic interface only. No natural downstream propagation, natural/injected equivalence, real-world hallucination rate, SHAR/HalluSE, internal mechanism or larger-model claim. Failure of this frozen design does not prove natural errors impossible. Incorporate result in project ledger; do not design/run v3.6.5 here.
'''


def verify():
    manifest = load('manifest.json')
    for group in ('frozen', 'prior_artifacts'):
        for path, value in manifest[group].items():
            assert digest(path) == value, path
    data = load('prior_ledger_snapshot.json')
    review_spec(data, (OUT/'spec.md').read_text(encoding='utf-8'), load('prior_findings_review.json'), digest(OUT/'prior_ledger_snapshot.json'))
    audit_cases(load('development_cases.json'), load('confirmation_cases.json'), load('downstream_compatibility.json'))


def prepare():
    assert not OUT.exists(), 'Never overwrite an existing experiment'
    policy = read(SOURCE/'user_resolution.json')
    assert policy['approved_by_user'] and isinstance(policy['valid_includes_out_of_universe'], bool)
    ledger = read('docs/validated_findings.json')
    validate_data(ledger)
    prior = read('results/v3_6_3_1/manifest.json')
    for p, value in prior['frozen'].items():
        assert digest(p) == value, p
    tok = AutoTokenizer.from_pretrained(MODEL, revision=REVISION, cache_dir='.cache/huggingface', local_files_only=True)
    old, sources = old_ids()
    dev, confirm, tokens = make_cases(tok, old)
    compatibility = {c['case_id']:{m['state']:m['outcome'] for m in c['members']} for c in dev+confirm}
    audit = audit_cases(dev, confirm, compatibility)
    diagnostic = random.Random(3645).sample([c['case_id'] for c in dev], 8)
    plans = dict(development=shuffled([render(c,k) for c in dev for k in LEVELS],3641)[0], confirmation={}, order_diagnostic={},
                 order_case_ids=diagnostic, maximum_calls=104, policy=policy)
    for i,k in enumerate(LEVELS):
        plans['confirmation'][k] = shuffled([render(c,k) for c in confirm],3642+i)[0]
        plans['order_diagnostic'][k] = [render(next(c for c in dev if c['case_id']==cid),k,True) for cid in diagnostic]
    allplans = plans['development']+[r for k in LEVELS for r in plans['confirmation'][k]+plans['order_diagnostic'][k]]
    for r in allplans:
        rendered = tok.apply_chat_template([dict(role='user',content=r['prompt'])], tokenize=False, add_generation_prompt=True, enable_thinking=False)
        r.update(rendered_prompt=rendered, rendered_sha256=sha(rendered))
    versions = {n:importlib.metadata.version(n) for n in ('torch','transformers','bitsandbytes','accelerate','numpy')}
    assert versions == read('results/v3_6_3_1/decoding_freeze.json')['versions']
    assert sha(tok.chat_template) == digest('results/v3_6_3_1/chat_template.txt')
    original = Path('C:/Users/kding/Downloads/v3_6_4_natural_first_hop_error_frontier_spec.md').read_text(encoding='utf-8-sig')
    # Copy exact ledger bytes: review hash must equal the snapshot hash after freeze.
    ledger_bytes = Path('docs/validated_findings.json').read_bytes()
    review, table = ledger_review(ledger, digest('docs/validated_findings.json'))
    introduction = '# Prior Findings Review\n\nReferences: docs/validated_findings.md and docs/validated_findings.json.\n\n'+table
    spec = introduction+'\n## Validated Inheritance\n\nThe full machine-readable review discloses C02/C04/C05 modifications. No downstream calls.\n\n## New manipulation\n\nQualify natural first-hop error yield in a two-relation task.\n\n'+PREREG+'\n## User-approved counting resolution\n\n'+json.dumps(policy,ensure_ascii=False,indent=2)+'\n\n## Uploaded specification (preserved)\n\n'+original
    review_result = review_spec(ledger,spec,review,digest('docs/validated_findings.json'))
    OUT.mkdir(parents=True)
    (OUT/'prior_ledger_snapshot.json').write_bytes(ledger_bytes)
    for name,value in [('spec.md',spec),('spec.original.md',original),('pre_registration.md',PREREG+'\n'+json.dumps(policy,ensure_ascii=False,indent=2)+'\n'),('prior_findings_review.md',introduction),('chat_template.txt',tok.chat_template)]:
        text(name,value)
    for name,value in [('development_cases.json',dev),('confirmation_cases.json',confirm),('downstream_compatibility.json',compatibility),('prompt_plan.json',plans),('prior_findings_review.json',review),('prior_findings_review.audit.json',review_result),('user_resolution.json',policy)]:
        write(name,value)
    write('identifier_tokenization_audit.json',dict(old_sources=sources,old_ids_excluded=len(old),selected=1152,pool_size=7800,candidates=tokens))
    write('decoding_freeze.json',dict(model=MODEL,revision=REVISION,versions=versions,cap=CAP,seed=42,do_sample=False,use_cache=False,enable_thinking=False,compute_dtype='torch.bfloat16',quantization='NF4 double quantization',chat_template_sha256=sha(tok.chat_template)))
    pre = '# Pre-inference design audit\n\n'+json.dumps(audit|review_result,indent=2)+'\n\nAll48 cases,168 potential prompts (at most104 executed), compatibility mappings, parser/gates, and user resolution are frozen. Three difficulty levels have nested shared records, one unique gold path, no candidate lists/UNKNOWN/downstream outputs. No selection used model outputs. Original and effective specs retained.\n\n'+PREREG
    text('design_audit.pre_inference.md',pre)
    text('design_audit.md',pre)
    text('prompt_diff_audit.md','# Prompt diff audit\n\nAll48 cases: same query/gold across levels; shared records preserved in relative order;3/5/8 entity and mapping records,0/2/6 irrelevant properties. Order variants have identical record multisets and instructions. No UNKNOWN rule, candidate list or outcome IDs.\n\n'+'\n'.join(f"- {r['call_id']}: text {r['text_sha256']}; rendered {r['rendered_sha256']}" for r in allplans)+'\n')
    code = list(SOURCE.glob('*.py'))+[SOURCE/'user_resolution.json',Path('tests/test_v3_6_4.py'),Path('scripts/validated_findings.py')]
    code += [Path(p) for p in prior['frozen'] if Path(p).suffix=='.py']
    frozen = {p.as_posix():digest(p) for p in code+list(OUT.iterdir()) if p.name!='design_audit.md'}
    history = {p.as_posix():digest(p) for p in Path('results').rglob('*') if p.is_file() and OUT not in p.parents}
    write('manifest.json',dict(created_utc=datetime.now(timezone.utc).isoformat(),frozen=frozen,prior_artifacts=history,maximum_calls=104))
    verify()
    print('Frozen48 cases and168 potential prompts;72 required, maximum104 calls.',flush=True)


if __name__ == '__main__':
    if OUT.exists():
        raise SystemExit('Existing experiment: preparation refused without modifying files')
    prepare()
