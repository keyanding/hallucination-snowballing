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
