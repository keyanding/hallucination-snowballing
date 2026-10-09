"""Freeze a targeted historical replication, with no model calls."""
import importlib.metadata
import json
import random
from datetime import datetime,timezone
from pathlib import Path
from transformers import AutoTokenizer
from experiments.v3_6_0.prepare import MODEL,digest
from src.calibration_v3_4_1 import REVISION
from scripts.validated_findings import load as ledger_load,validate_data,review_spec
from experiments.v3_6_4.prepare import ledger_review
from .design import read,make_cases,render,historical_audit,sha

OUT=Path('results/v3_6_5')
CAP=96
POLICY=dict(diagnostic_on_development_failure=True,approved_by_user=True,
            user_resolution='开发失败也运行8次诊断；确认集仍仅开发通过时运行，诊断不改变主结论。')


def load(name):return read(OUT/name)


def text(name,value):
    (OUT/name).write_text(value,encoding='utf-8',newline='\n')


def write(name,value):text(name,json.dumps(value,ensure_ascii=False,indent=2)+'\n')


PREREG='''# v3.6.5 pre-registration

## Sole question and historical contract
Target v3.4.4 HARD=D4B2, N only: four credited-director links, two equal-depth comparison/associated branches, four complete candidate-name records, same substantive Film question and exact output-only-person-name instruction. Directly call unchanged no_list(c,4,2) and unchanged historical parse_natural. Rebuild all24 saved HARD/N development fixtures, full graph audits and chat strings with zero model calls. Recount historical24/24 strict-valid,5/24 wrong from raw outputs. Failure to establish this contract stops as HISTORICAL_INTERFACE_NOT_RECOVERABLE. This is not an EASY/MID search or v3.6.4 marker lookup.

## Fresh cohorts and endpoints
Fixed seed365 constructs24 development plus24 disjoint confirmation cases. Reuse the historical21 audited real people and their source-grounded downstream relation/endpoints; log reuse explicitly. Enumerate same-relation four-person bundles with disjoint endpoint alias sets; exclude all bundles from v3.4.1, v3.4.2 and v3.4.4, including held-out/unrun cases. Exactly40 fresh eligible bundles remain; use all40 plus8 seeded historically used bundles. The48 chosen bundles are distinct across both splits, then shuffled before assignment. No model output selects any case. Fresh targets48 and record IDs624 exclude all historical graph IDs. No historical target question/graph recurs. Each split has six gold identities in each candidate-array position and each initial candidate-name record position. The array is not an answer list and is never shown separately. Keep original graph semantics, path-order randomization and number/length family of IDs; new seeds/cohort sizes/bundles are documented differences.
Freeze192 candidate occurrences with their real downstream endpoints and evidence coordinates before inference, distinct endpoints within each case. No downstream endpoint appears in first-hop prompts. All candidate aliases are empty, exactly as historical v3.4.4 N; no added spelling/diacritic/punctuation tolerance. No new people are claimed.

## Parsing and gate definitions
Use historical raw.strip() only; unlike recent STATE tasks, do not add NFC normalization, terminal-period removal or casefold. Historical parser precedence: TRUNCATED first; exact canonical name (empty alias registry); multiple distinct mentions AMBIGUOUS; conservative unfamiliar name-shaped response OUT_OF_SET; otherwise NONCOMPLIANT. Supplementary mention/extraction fields never make a strict answer valid. Exact in-set output becomes IN_SET_VALID_GOLD or IN_SET_VALID_WRONG; wrong must have a pre-frozen endpoint or structural verification fails. Valid is only those two strict untruncated classes. Distinct wrong identities count canonical names, not spelling variants.
Development: fixed denominator24, Valid>=22, TRACEABLE_WRONG>=4, at least3 distinct wrong cases, AMBIGUOUS+NONCOMPLIANT+TRUNCATED<=2, every wrong has endpoint. All conjunctive. Confirmation: identical parser and definitions, wrong threshold3/24 and at least3 cases, all other thresholds unchanged. All48 cases/mappings/aliases and schedules freeze now. No repeated sampling, retries, cap sweeps, scoring/trie/likelihood calls, answer options or UNKNOWN option.

## Schedules and user resolution
Development24 in seed3651 shuffled order. Classify development before diagnostics; persist its gate before further calls. Eight diagnostic cases sampled from development with seed3652 before outputs; each receives exactly rotation2 (one-step cyclic permutation of the four complete candidate-name record lines). No graph facts, query, name-to-ID mapping or instruction changes. User explicitly resolved the conflicting stop instruction: run these8 diagnostics even when development fails. Confirmation24 in seed3653 order only if development passes, after the diagnostic; no diagnostic outcome selects/excludes errors or changes the gate. Calls32 if development fails,56 if it passes. No automatic next phase or downstream calls.

## Presentation-sensitivity definitions
Identity comparisons require both paired outputs strict-valid; report comparable coverage and missing pairs separately. Non-valid prose or unfamiliar names do not establish stable candidate identity. Fixed denominator8 for identity changes, with strict-valid coverage prominent. More than3 pairs changing candidate identity sets PRESENTATION_SENSITIVE=true; otherwise false. When unrun set not_evaluated; partial diagnostics are infrastructure failure. Also report same identity, gold-to-wrong, wrong-to-gold, wrong-to-different-wrong, same wrong identity and all paired categories. This limits interpretation but never changes the primary gate.

## Frozen runtime and priority
Same pinned Qwen3-4B-Instruct-2507 revision, tokenizer/template, NF4 double quantization/BF16, seed42, greedy fresh one-user calls, use_cache=False. Cap96 matches historical selected N cap, not a new sweep. Reuse only existing pure generate(), whose free-generation settings match the historical F path; do not call InterfaceAdapter.evaluate because it also scores. Historical render/parser compatibility is zero-call validation, not a model-stack experiment. No auxiliary model calls. Budget cannot guarantee no truncation; report it without repair.
Priority: true runtime/structural/hash/missing-call failure INFRASTRUCTURE_FAILURE; historical-contract failure HISTORICAL_INTERFACE_NOT_RECOVERABLE; failed development HARD_N_SIGNAL_NOT_REPLICATED; failed confirmation HARD_N_CONFIRMATION_FAILED; otherwise HARD_N_NATURAL_ERROR_SIGNAL_CONFIRMED. Presentation flag separate. A native loading crash terminates this attempt; no automatic retry.
The independent unit is a base case, not a diagnostic rotation; people recur across cases, limiting generalization. Confirmed means reproducible yield in this synthetic real-name interface only, not natural downstream propagation, real-world hallucination rate, natural/injected equivalence, internal mechanism or SHAR/HalluSE. If not replicated, the historical5/24 signal did not reproduce under this fresh targeted design; never claim errors impossible. Update ledger after this version, without running v3.6.6.
'''


def review(data,hash_value):
    r,_=ledger_review(data,hash_value)
    changes={
      'F14':('AVOIDED','Keep historical N cap96, no sweep; truncated responses cannot be strict-valid.'),
      'F16':('INTENTIONALLY_RETESTED','Eight seeded complete name-record cyclic permutations; non-gating regardless of development pass.'),
      'F18':('TARGETED','Replicate historical HARD/N5/24 on fresh graphs, then independent confirmation if development passes.'),
      'F19':('INTENTIONALLY_RETESTED','Fixed development4/24 and confirmation3/24 traceable wrong yield; no error-selected cases.'),
      'F26':('OVERRIDDEN','Use exact v3.4.4 person-name parser, not later state parser; preserve raw text and no extraction.'),
      'F27':('OVERRIDDEN','Same pinned greedy stack; cap96 matches historical N, explicitly differs from cap16 symbolic components.'),
      'C02':('NOT_RELEVANT','Do not run direct A-to-B shell; reuse historical D4B2 catalog graph task.'),
      'C03':('NOT_RELEVANT','No opaque-state ID task; retain historical T/R graph ID family and real-name candidates.'),
      'C04':('OVERRIDDEN','Person-name parser is unchanged v3.4.4 implementation; later STATE normalization does not apply.'),
      'C05':('OVERRIDDEN','Same model stack but cap96; historical HARD/N budget and new fixed validity/yield gates.')}
    known={x['id']:x for x in data['findings']+data['validated_components']}
    for row in r['rows']:
        rid=row['id']
        if rid in changes:row['treatment'],row['rationale']=changes[rid]
        row['modified']=rid in ('C04','C05')
        row.pop('modification',None)
        if row['modified']:
            row['modification']=dict(component=rid,prior_evidence=known[rid]['evidence_files'],reason=row['rationale'],
                prior_conclusion_no_longer_applies='Recent symbolic exact-output interface success does not validate real-name HARD/N yield.',
                revalidation_gate='Zero-call historical parser/render audits; fixed Valid>=22/24 and natural-error development/confirmation gates.')
    table='| Finding / Component | Ledger status | Treatment in this experiment | Rationale |\n|---|---|---|---|\n'
    table+='\n'.join('| '+' | '.join(x[k] for k in ('id','ledger_status','treatment','rationale'))+' |' for x in r['rows'])+'\n'
    return r,table


def verify():
    m=load('manifest.json')
    for group in ('frozen','prior_artifacts'):
        for p,h in m[group].items():assert digest(p)==h,p
    review_spec(load('prior_ledger_snapshot.json'),(OUT/'spec.md').read_text(encoding='utf-8'),load('prior_findings_review.json'),digest(OUT/'prior_ledger_snapshot.json'))


def prepare():
    assert not OUT.exists(),'Never overwrite an experiment'
    data=ledger_load();validate_data(data)
    assert data['future_spec_protocol']['latest_incorporated_version']=='v3.6.4'
    tok=AutoTokenizer.from_pretrained(MODEL,revision=REVISION,cache_dir='.cache/huggingface',local_files_only=True)
    try:
        history=historical_audit(tok)
    except Exception:
        import traceback
        OUT.mkdir()
        write('gate.json',dict(final_decision='HISTORICAL_INTERFACE_NOT_RECOVERABLE',PRESENTATION_SENSITIVE='not_evaluated'))
        write('historical_interface_failure.json',dict(error=traceback.format_exc(),model_calls=0))
        raise
    dev,confirm,reuse=make_cases()
    diagnostic_ids=random.Random(3652).sample([c['case_id'] for c in dev],8)
    plans=dict(development=[render(c) for c in dev],confirmation=[render(c) for c in confirm],
               presentation_diagnostic=[render(next(c for c in dev if c['case_id']==cid),2) for cid in diagnostic_ids],
               diagnostic_ids=diagnostic_ids,policy=POLICY,maximum_calls=56)
    random.Random(3651).shuffle(plans['development']);random.Random(3653).shuffle(plans['confirmation'])
    for stage in ('development','confirmation','presentation_diagnostic'):
        for p in plans[stage]:
            rendered=tok.apply_chat_template([dict(role='user',content=p['prompt'])],tokenize=False,add_generation_prompt=True,enable_thinking=False)
            p.update(rendered_prompt=rendered,rendered_sha256=sha(rendered))
    compatibility={c['case_id']:{p['name']:dict(endpoint=p['target'],relation=p['relation'],endpoint_aliases=p['target_aliases'],source_id=p['downstream_source_id'],evidence=p['downstream_evidence']) for p in c['candidates']} for c in dev+confirm}
    versions={n:importlib.metadata.version(n) for n in ('torch','transformers','bitsandbytes','accelerate','numpy')}
    assert versions==read('results/v3_6_4/decoding_freeze.json')['versions']
    assert sha(tok.chat_template)==digest('results/calibration_v3_4_4/chat_template.txt')
    r,table=review(data,digest('docs/validated_findings.json'))
    intro='# Prior Findings Review\n\nReferences: docs/validated_findings.md and docs/validated_findings.json.\n\n'+table
    original=Path('C:/Users/kding/Downloads/v3_6_5_hard_n_natural_error_replication_spec.md').read_text(encoding='utf-8-sig')
    spec=intro+'\n## Validated Inheritance\n\nCanonical historical HARD/N renderer and parser reused directly; component modifications disclosed above.\n\n## New manipulation\n\nFresh targeted replication and independent yield confirmation, no new difficulty search.\n\n'+PREREG+'\n## Uploaded specification\n\n'+original
    reviewed=review_spec(data,spec,r,digest('docs/validated_findings.json'))
    OUT.mkdir()
    (OUT/'prior_ledger_snapshot.json').write_bytes(Path('docs/validated_findings.json').read_bytes())
    for n,v in [('spec.md',spec),('spec.original.md',original),('pre_registration.md',PREREG),('prior_findings_review.md',intro),('chat_template.txt',tok.chat_template)]:text(n,v)
    for n,v in [('development_cases.json',dev),('confirmation_cases.json',confirm),('downstream_compatibility.json',compatibility),('alias_registry.json',{}),('prompt_plan.json',plans),('case_reuse_audit.json',reuse),('historical_interface_audit.json',history),('prior_findings_review.json',r),('prior_findings_review.audit.json',reviewed)]:write(n,v)
    text('historical_anchor.md','# Historical anchor\n\nRaw v3.4.4 development HARD/N re-count:24/24 strict-valid,5/24 wrong. N/EASY was selected for historical confirmation; HARD/N was not independently confirmed. All24 development cases and prompt fixtures were regenerated exactly. No model calls.\n')
    text('historical_interface_audit.md','# Historical compatibility audit\n\n'+json.dumps(history,ensure_ascii=False,indent=2)+'\n\nSame no_list renderer, candidate-name lines, D4B2 graph semantics, question, output instruction, record-order construction and chat rendering. Pure generate uses the same F settings but omits all C/scoring operations. Real people recur; fresh graph IDs and maximal feasible fresh bundles are documented in case_reuse_audit.json.\n')
    write('decoding_freeze.json',dict(model=MODEL,revision=REVISION,versions=versions,cap=CAP,seed=42,do_sample=False,use_cache=False,enable_thinking=False,compute_dtype='torch.bfloat16',quantization='NF4 double quantization',chat_template_sha256=sha(tok.chat_template)))
    pre='# Pre-inference audit\n\nHistorical compatibility PASS24/24; ledger review PASS34 rows. All48 fresh targets and624 fresh record IDs;48 distinct bundles (40 historically fresh,8 reused),21 real people reused. Source evidence checks192/192; unique credited endpoint and distinct frozen downstream endpoints per case. All56 prompt/render hashes frozen. No inference-based selection or prohibited channel; empty aliases and cap96 frozen. User requires diagnostic even after failed development.\n\n'+PREREG
    text('design_audit.pre_inference.md',pre);text('design_audit.md',pre)
    diffs=['# Prompt diff audit','','HARD/N only. All8 rotations move complete name-record lines by one cyclic step; graph/query/instruction bytes identical. No answer list or downstream endpoints shown.','']
    for c in dev:
        if c['case_id'] in diagnostic_ids:
            a,b=render(c),render(c,2)
            assert a['prompt'].split('\n\nGraph-link records:\n')[1]==b['prompt'].split('\n\nGraph-link records:\n')[1]
            diffs.append(f"- {c['case_id']}: {a['text_sha256']} -> {b['text_sha256']}; record multiset unchanged.")
    text('prompt_diff_audit.md','\n'.join(diffs)+'\n')
    code=list(Path('src').glob('*.py'))+list(Path('experiments').rglob('*.py'))+[Path('scripts/validated_findings.py'),Path('tests/test_v3_6_5.py'),Path('data/dev.json')]
    frozen={p.as_posix():digest(p) for p in code+list(OUT.iterdir()) if p.name!='design_audit.md'}
    prior={p.as_posix():digest(p) for p in Path('results').rglob('*') if p.is_file() and OUT not in p.parents}
    write('manifest.json',dict(created_utc=datetime.now(timezone.utc).isoformat(),frozen=frozen,prior_artifacts=prior,maximum_calls=56))
    verify()
    print('Frozen HARD/N replication:24 development,24 conditional confirmation,8 diagnostic; historical24 fixtures exact.',flush=True)


if __name__=='__main__':prepare()
