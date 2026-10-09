# Prior Findings Review

References: docs/validated_findings.md and docs/validated_findings.json.

| Finding / Component | Ledger status | Treatment in this experiment | Rationale |
|---|---|---|---|
| F01 | ACTIVE_WARNING | AVOIDED | Whole-output eligibility and independent confirmation; no denominator substitution. |
| F02 | ACTIVE_WARNING | AVOIDED | Synthetic explicit records avoid closed-book knowledge and birthplace granularity. |
| F03 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F04 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F05 | ACTIVE_WARNING | AVOIDED | No supporting prose that asserts a competing answer; exactly one gold path. |
| F06 | ACTIVE_WARNING | AVOIDED | No UNKNOWN instruction or fallback shell. |
| F07 | ACTIVE_WARNING | AVOIDED | No Recorded intermediate result shell or downstream inference. |
| F08 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F09 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F10 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F11 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F12 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F13 | INCONCLUSIVE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F14 | ACTIVE_WARNING | AVOIDED | Keep historical N cap96, no sweep; truncated responses cannot be strict-valid. |
| F15 | ACTIVE_WARNING | AVOIDED | No answer options or numbered candidate list; records are relational evidence. |
| F16 | ACTIVE_WARNING | INTENTIONALLY_RETESTED | Eight seeded complete name-record cyclic permutations; non-gating regardless of development pass. |
| F17 | ACTIVE_WARNING | AVOIDED | Only unconstrained greedy generation, no likelihood or constrained channel. |
| F18 | INCONCLUSIVE | TARGETED | Replicate historical HARD/N5/24 on fresh graphs, then independent confirmation if development passes. |
| F19 | ACTIVE_WARNING | INTENTIONALLY_RETESTED | Fixed development4/24 and confirmation3/24 traceable wrong yield; no error-selected cases. |
| F20 | INCONCLUSIVE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F21 | INCONCLUSIVE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F22 | OPEN_QUESTION | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F23 | OPEN_QUESTION | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F24 | INCONCLUSIVE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F25 | INCONCLUSIVE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F26 | FROZEN_REUSE | OVERRIDDEN | Use exact v3.4.4 person-name parser, not later state parser; preserve raw text and no extraction. |
| F27 | FROZEN_REUSE | OVERRIDDEN | Same pinned greedy stack; cap96 matches historical N, explicitly differs from cap16 symbolic components. |
| C01 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| C02 | FROZEN_REUSE | NOT_RELEVANT | Do not run direct A-to-B shell; reuse historical D4B2 catalog graph task. |
| C03 | FROZEN_REUSE | NOT_RELEVANT | No opaque-state ID task; retain historical T/R graph ID family and real-name candidates. |
| C04 | FROZEN_REUSE | OVERRIDDEN | Person-name parser is unchanged v3.4.4 implementation; later STATE normalization does not apply. |
| C05 | FROZEN_REUSE | OVERRIDDEN | Same model stack but cap96; historical HARD/N budget and new fixed validity/yield gates. |
| C06 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| C07 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |

## Validated Inheritance

Canonical historical HARD/N renderer and parser reused directly; component modifications disclosed above.

## New manipulation

Fresh targeted replication and independent yield confirmation, no new difficulty search.

# v3.6.5 pre-registration

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

## Uploaded specification

# v3.6.5 — Targeted Replication of the v3.4.4 HARD/N Natural First-Hop Error Signal

## 0. Purpose

Use `docs/validated_findings.md/json` as mandatory prior knowledge.

Do **not** repeat already validated downstream propagation, `Current state` shell, context robustness, explicit A→B lookup, modular A→B→C forwarding, injected B′ propagation, parser, or model-stack tests.

The only question is:

> Does the historical v3.4.4 HARD/N free-generation natural-error signal reproduce on fresh cases and survive independent confirmation?

Historical anchor:

- v3.4.4 development HARD/N: 24/24 valid, 5/24 wrong.
- That specific HARD/N regime was never independently confirmed because v3.4.4 selected N/EASY for confirmation.
- v3.6.4 tested a different explicit synthetic lookup family and produced 0/24 natural errors at all three levels.

Therefore this is a targeted replication, not another frontier search.

---

## 1. Prior Findings Review

| Finding | Status | Treatment |
|---|---|---|
| F03 minimal B→C propagation | FROZEN_REUSE | NOT_RETESTED |
| F04 `Current state` shell | FROZEN_REUSE | NOT_RETESTED |
| F08 context≤24 robustness | FROZEN_REUSE | NOT_RETESTED |
| F10 explicit A→B lookup | FROZEN_REUSE | NOT_RETESTED |
| F11 modular pipeline | FROZEN_REUSE | NOT_RETESTED |
| F12 injected B′→C′ | FROZEN_REUSE | NOT_RETESTED |
| F14 truncation artifact | ACTIVE_WARNING | AVOIDED |
| F15 list-position bias | ACTIVE_WARNING | AVOIDED |
| F16 complex record-order sensitivity | ACTIVE_WARNING | MEASURED, NON-GATING |
| F17 free/constrained/scoring mismatch | ACTIVE_WARNING | AVOIDED |
| F18 no stable frontier | INCONCLUSIVE | TARGETED |
| F19 natural-error yield insufficient | ACTIVE_WARNING | TARGETED |
| F20 natural propagation unknown | INCONCLUSIVE | NOT_YET_TESTED |
| F26 exact parser/raw preservation | FROZEN_REUSE | FROZEN_REUSE |
| F27 stateless greedy stack | FROZEN_REUSE | FROZEN_REUSE |
| F22/F23 SHAR/HalluSE | OPEN_QUESTION | NOT_RELEVANT |

No silent modification of frozen components.

---

## 2. Canonical task reuse

Reuse the **v3.4.4 HARD=D4B2, Interface N** task family and free-generation prompt contract.

Required properties:

- same graph semantics and relation structure,
- same no-answer-list interface,
- same candidate-name mapping records,
- four-candidate universe per case,
- unconstrained free generation,
- same substantive question,
- output only the person's name.

Do **not** substitute the v3.6.4 entity→marker→state family.

Before inference, perform a zero-model-call historical compatibility audit:

1. locate the historical v3.4.4 renderer/generator;
2. regenerate at least 6 saved HARD/N fixtures if possible;
3. compare graph facts, candidate-name records, query wording, output instruction, record-order policy, and chat rendering;
4. document every unavoidable difference.

If historical compatibility cannot be established:

`HISTORICAL_INTERFACE_NOT_RECOVERABLE`

and stop.

---

## 3. Cohorts

Freeze before inference:

- 24 fresh development cases;
- 24 disjoint fresh confirmation cases.

Requirements:

- no repeated historical target question/graph;
- fresh graph IDs;
- candidate bundles fresh where feasible;
- reused real people logged explicitly;
- no case selected by model output.

---

## 4. Downstream traceability

Each case has four candidate identities:

\[
\{B,B'_1,B'_2,B'_3\}
\]

Before inference, freeze a distinct downstream endpoint for every candidate.

Save:

`downstream_compatibility.json`

Do not show these endpoints in first-hop prompts.

A wrong answer counts as `TRACEABLE_WRONG` only if it is a non-gold candidate in the frozen four-person universe and has a pre-frozen downstream endpoint.

---

## 5. Primary interface

Use HARD/N only.

No:

- answer-option list,
- numbered choices,
- trie-constrained choice,
- score-based answer,
- likelihood ranking,
- UNKNOWN option.

The model generates the person name freely.

---

## 6. Decoding

Reuse the pinned Qwen3-4B stack:

- same revision,
- tokenizer/chat template,
- NF4/BF16,
- greedy,
- fresh stateless calls,
- use_cache=False,
- frozen seed.

Use a non-censoring output cap:

`max_new_tokens = 96`

or the exact historical v3.4.4 N cap if repository evidence shows a different non-censoring value.

No cap sweep.

---

## 7. Parser

Match v3.4.4 N semantics.

Primary mutually exclusive categories:

- `IN_SET_VALID_GOLD`
- `IN_SET_VALID_WRONG`
- `OUT_OF_SET`
- `AMBIGUOUS`
- `NONCOMPLIANT`
- `TRUNCATED`

Rules:

- preserve raw text;
- aliases frozen before inference;
- no hand edits;
- no extracting a candidate from explanatory prose for primary scoring;
- supplementary extraction tags allowed but never promoted to strict-valid;
- no post-hoc prefix repair.

Primary:

\[
Valid = GOLD \lor TRACEABLE\_WRONG
\]

---

## 8. Development stage

Run exactly 24 fresh HARD/N free-generation calls.

No repeated sampling.
No order rotations before primary classification.
No scoring channel.

Report:

- valid /24
- gold /24
- traceable wrong /24
- out-of-set /24
- ambiguous /24
- noncompliant /24
- truncated /24
- distinct wrong case IDs
- distinct wrong candidate identities

Development passes only if all hold:

- Valid ≥ 22/24
- TRACEABLE_WRONG ≥ 4/24
- at least 3 distinct wrong cases
- AMBIGUOUS + NONCOMPLIANT + TRUNCATED ≤ 2/24
- every wrong has a pre-frozen downstream endpoint

If not:

`HARD_N_SIGNAL_NOT_REPLICATED`

Stop. Do not add EASY/MID or change prompts.

---

## 9. Confirmation stage

Only if development passes.

Run exactly 24 fresh confirmation HARD/N calls with identical interface/model/parser/cap.

Confirmation passes only if all hold:

- Valid ≥ 22/24
- TRACEABLE_WRONG ≥ 3/24
- at least 3 distinct wrong cases
- AMBIGUOUS + NONCOMPLIANT + TRUNCATED ≤ 2/24
- every wrong is traceable

If all pass:

`HARD_N_NATURAL_ERROR_SIGNAL_CONFIRMED`

Else:

`HARD_N_CONFIRMATION_FAILED`

No tuning between stages.

---

## 10. Presentation-sensitivity diagnostic

F16 is a known warning, so measure it separately.

Freeze an 8-case diagnostic subset before inference.

After primary development classification, for each selected case:

- keep graph facts/query unchanged;
- apply one frozen cyclic permutation to the complete candidate-name record block;
- run one extra N free-generation call.

Report:

- same identity / changed identity,
- gold→wrong,
- wrong→gold,
- wrong→different wrong,
- strict-valid coverage,
- wrong identity persistence.

Do **not** use this diagnostic to select/exclude primary wrong cases.

If >3/8 identities change, set:

`PRESENTATION_SENSITIVE = true`

Else false.

This flag limits interpretation but does not alter the main gate.

---

## 11. Explicitly prohibited repetition

Do not retest as primary questions:

- EASY/MID frontier search,
- v3.6.4 explicit lookup difficulty,
- list-position bias,
- constrained candidate choice,
- likelihood/scoring channels,
- B→C propagation,
- `Current state` shell validity,
- injected B′ propagation,
- integrated two-hop readiness,
- SHAR/HalluSE.

---

## 12. Pre-inference audit

Verify:

1. ledger includes v3.6.4;
2. v3.4.4 HARD/N anchor located;
3. historical interface audit complete;
4. 24+24 fresh cases frozen;
5. downstream mappings frozen for all candidates;
6. no output-based case selection;
7. no answer list;
8. no constrained decoding;
9. alias registry frozen;
10. non-censoring cap frozen;
11. prompt/render hashes saved;
12. diagnostic subset frozen;
13. schedules frozen;
14. historical results unchanged.

Structural failure:

`INFRASTRUCTURE_FAILURE`

---

## 13. Decision hierarchy

Exactly one:

- `INFRASTRUCTURE_FAILURE`
- `HISTORICAL_INTERFACE_NOT_RECOVERABLE`
- `HARD_N_SIGNAL_NOT_REPLICATED`
- `HARD_N_CONFIRMATION_FAILED`
- `HARD_N_NATURAL_ERROR_SIGNAL_CONFIRMED`

Separate field:

`PRESENTATION_SENSITIVE = true/false/not_evaluated`

---

## 14. Interpretation

If signal not replicated:

> The historical v3.4.4 HARD/N 5/24 development signal did not reproduce on the fresh targeted replication.

Do not start another difficulty search in the same run.

If confirmation fails:

> A development signal appeared but did not survive fresh confirmation.

Do not cherry-pick development errors for propagation.

If confirmed:

> The frozen v3.4.4-style HARD/N free-generation interface produces a reproducible non-zero yield of valid, traceable first-hop errors on fresh cases under the tested Qwen3-4B setup.

Still do not infer:

- natural downstream propagation,
- real-world hallucination rate,
- injected/natural equivalence,
- internal mechanism,
- SHAR/HalluSE performance.

---

## 15. Required artifacts

Save under:

`results/v3_6_5/`

Required:

- README.md
- spec.md
- pre_registration.md
- prior_findings_review.md
- historical_anchor.md
- historical_interface_audit.md
- design_audit.pre_inference.md
- design_audit.md
- development_cases.json
- confirmation_cases.json
- downstream_compatibility.json
- alias_registry.json
- prompt_plan.json
- prompt_diff_audit.md
- decoding_freeze.json
- model_manifest.json
- development_outputs.jsonl
- development_metrics.json
- confirmation_outputs.jsonl
- confirmation_metrics.json
- presentation_diagnostic_outputs.jsonl
- presentation_diagnostic_metrics.json
- parsed_outcomes.jsonl
- gate.json
- diagnosis.md
- interpretation.md
- inspection.md
- CHANGELOG.md

---

## 16. Ledger update requirement

Before v3.6.6:

- update `docs/validated_findings.md`
- update `docs/validated_findings.json`
- update `docs/validated_findings_audit.md`
- append `docs/validated_findings_CHANGELOG.md`

No next spec until the ledger includes v3.6.5.

---

## 17. Next experiment if confirmed

Only after:

`HARD_N_NATURAL_ERROR_SIGNAL_CONFIRMED`

may the project test natural propagation.

For each fresh first-hop call:

\[
A \rightarrow \hat B
\]

forward the actual strict-valid generated identity unchanged into a prevalidated downstream interface.

Estimate separately:

\[
P(C\mid \hat B=B)
\]

and

\[
P(C'\mid \hat B=B')
\]

No injected B′ may enter the natural-error denominator.

---

## 18. Core discipline

The project already has one historically promising natural-error regime.

Do not invent another before confirming or falsifying it.

The sole new question is:

\[
oxed{\text{Does the v3.4.4 HARD/N signal replicate and confirm on fresh cases?}}
\]
