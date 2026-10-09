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
| F14 | ACTIVE_WARNING | AVOIDED | One frozen cap96; report truncation independently, exclude censored outputs from eligible yield; no sweep. |
| F15 | ACTIVE_WARNING | AVOIDED | No answer options or numbered candidate list; records are relational evidence. |
| F16 | ACTIVE_WARNING | INTENTIONALLY_RETESTED | Eight seeded selected-level record permutations; non-gating identity diagnostic. |
| F17 | ACTIVE_WARNING | AVOIDED | Only unconstrained greedy generation, no likelihood or constrained channel. |
| F18 | INCONCLUSIVE | TARGETED | Qualify natural wrong-state yield on disjoint development and confirmation cases. |
| F19 | ACTIVE_WARNING | INTENTIONALLY_RETESTED | Pre-frozen 4/24 development and 3/24 confirmation wrong-yield thresholds. |
| F20 | INCONCLUSIVE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F21 | INCONCLUSIVE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F22 | OPEN_QUESTION | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F23 | OPEN_QUESTION | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F24 | INCONCLUSIVE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F25 | INCONCLUSIVE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| F26 | FROZEN_REUSE | OVERRIDDEN | Keep exact normalization/no repair; separate truncation flag from syntax category as required here. |
| F27 | FROZEN_REUSE | OVERRIDDEN | Keep pinned stateless NF4/BF16 greedy stack; explicitly change cap16 to96. |
| C01 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| C02 | FROZEN_REUSE | INTENTIONALLY_RETESTED | Replace direct A-to-B lookup with entity-to-marker-to-state task; old direct lookup result does not transfer. |
| C03 | FROZEN_REUSE | FROZEN_REUSE | Reuse opaque ID family, token-count matching, unique suffixes and fresh historical exclusion. |
| C04 | FROZEN_REUSE | INTENTIONALLY_RETESTED | Preserve normalization and no extraction; use four syntax/identity categories with orthogonal truncation. |
| C05 | FROZEN_REUSE | INTENTIONALLY_RETESTED | Reuse model/revision/quantization/greedy execution; cap96 replaces cap16 to reduce censoring. |
| C06 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |
| C07 | FROZEN_REUSE | NOT_RELEVANT | No call tests this component or question; prior scope is preserved without claiming new validation. |

## Validated Inheritance

The full machine-readable review discloses C02/C04/C05 modifications. No downstream calls.

## New manipulation

Qualify natural first-hop error yield in a two-relation task.

# v3.6.4 pre-registration

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

## User-approved counting resolution

{
  "approved_by_user": true,
  "valid_includes_out_of_universe": false,
  "valid_definition": "Only GOLD or TRACEABLE_WRONG, and only when TRUNCATED=false. OUT_OF_UNIVERSE and INVALID are excluded.",
  "truncation_rule": "Even an exact GOLD or TRACEABLE_WRONG state is excluded from Valid and qualified wrong yield when TRUNCATED=true. Count truncation as an independent measurement failure.",
  "state_universe": {
    "EASY": 3,
    "MID": 5,
    "HARD": 8
  },
  "state_universe_rule": "Exactly the legal states explicitly present in that case/difficulty's pre-inference frozen prompt.",
  "traceable_wrong_rule": "Exact non-gold state identifier inside the frozen case/difficulty state universe, with an existing pre-defined mapping in downstream_compatibility.json.",
  "shared_counting_rule": "Development and confirmation use identical counting rules.",
  "freeze_rule": "Write these definitions into spec.md, pre_registration.md and metrics implementation, and freeze before inference."
}

## Uploaded specification (preserved)

# v3.6.4 — Natural First-Hop Error Frontier Qualification

## 0. Purpose

This experiment targets the unresolved bottleneck in:

- `docs/validated_findings.md`
- `docs/validated_findings.json`

Already validated and **not retested here**:
- F03 minimal B→C propagation
- F04 validated `Current state` shell
- F08 context robustness through 24 irrelevant mappings
- F10 explicit A→B lookup
- F11 actual-state modular A→B→C pipeline
- F12 injected counterfactual propagation
- F26 exact parser discipline
- F27 pinned stateless greedy model stack

The only new question is:

> Can a free-generation upstream task produce a stable, independently confirmed set of valid, traceable natural first-hop errors?

No downstream propagation calls are made in this version.

---

## 1. Prior Findings Review

| Finding | Ledger status | Treatment |
|---|---|---|
| F03 minimal symbolic propagation | FROZEN_REUSE | NOT_RELEVANT |
| F04 Current-state shell | FROZEN_REUSE | FROZEN_REUSE for future downstream use |
| F10 explicit A→B lookup | FROZEN_REUSE | NOT_RETESTED |
| F11 modular pipeline | FROZEN_REUSE | NOT_RETESTED |
| F12 injected B′→C′ | FROZEN_REUSE | NOT_RETESTED |
| F13 integrated readiness | INCONCLUSIVE | NOT_RELEVANT |
| F14 truncation / cap artifact | ACTIVE_WARNING | AVOIDED |
| F15 candidate-list bias | ACTIVE_WARNING | AVOIDED |
| F16 complex record-order sensitivity | ACTIVE_WARNING | CONTROLLED |
| F17 free/constrained/scoring mismatch | ACTIVE_WARNING | AVOIDED |
| F18 no stable natural-error frontier | INCONCLUSIVE | TARGETED |
| F19 natural-error yield insufficient | ACTIVE_WARNING | TARGETED |
| F20 natural propagation unknown | INCONCLUSIVE | NOT_YET_TESTED |
| F22/F23 SHAR/HalluSE | OPEN_QUESTION | NOT_RELEVANT |

No prior validated component may be silently modified.

---

## 2. Research question

A **qualified natural wrong first-hop state** must be:

1. freely generated by the model,
2. not forced by a candidate list,
3. syntactically valid,
4. non-gold,
5. inside the pre-defined state universe,
6. already associated with a frozen downstream mapping for later work,
7. reproduced on an independent confirmation set.

This version measures **natural-error yield only**, not propagation.

---

## 3. Task family

Use a synthetic two-relation upstream task:

```text
Synthetic relation task.

Records:
ENTITY_A17 has marker P.
ENTITY_M42 has marker R.
ENTITY_Q31 has marker T.
Marker P maps to STATE_K04.
Marker R maps to STATE_R83.
Marker T maps to STATE_H22.

Question:
What state is associated with ENTITY_A17?

Return only the state identifier.
```

The task requires:

\[
A \rightarrow marker \rightarrow B
\]

This is intentionally harder than the already-validated direct A→B lookup.

No candidate list, no UNKNOWN rule, no answer options, no constrained decoding.

---

## 4. Difficulty levels

Use three pre-registered levels:

### EASY
- 3 entities
- 3 marker→state mappings
- no extra distractors

### MID
- 5 entities
- 5 marker→state mappings
- a small number of irrelevant records

### HARD
- 8 entities
- 8 marker→state mappings
- more irrelevant records

All levels must preserve:
- exactly one gold state,
- no contradictory evidence,
- no duplicate valid state for the queried entity.

The only intended manipulation is upstream selection difficulty.

---

## 5. Output budget

F14 is an ACTIVE_WARNING.

Use a non-censoring budget, recommended:

```text
max_new_tokens = 96
```

Do **not** run a cap sweep.

Truncation is reported as a measurement artifact, not a semantic error type.

---

## 6. Development set

Use 24 fresh base cases × EASY/MID/HARD:

\[
24 \times 3 = 72
\]

calls.

One stateless greedy call per case/level.

No repeated sampling.

---

## 7. Output categories

### GOLD
Exact gold state.

### TRACEABLE_WRONG
Exact non-gold state from the case's frozen state universe.

### OUT_OF_UNIVERSE
Well-formed `STATE_[A-Z][0-9]{2}` not in the case.

### INVALID
Anything else.

Track `TRUNCATED` as an orthogonal flag.

Do not extract state IDs from prose.
Do not repair prefixes.

---

## 8. Development qualification gate

A difficulty qualifies only if all pass:

- Valid outputs ≥ 22/24
- TRACEABLE_WRONG ≥ 4/24
- INVALID ≤ 1/24
- TRUNCATED ≤ 1/24
- at least 3 distinct case IDs produce TRACEABLE_WRONG

If multiple levels qualify, choose the easiest in fixed order:

```text
EASY -> MID -> HARD
```

Do not maximize wrong yield.

If none qualify:

```text
NO_NATURAL_ERROR_FRONTIER
```

Stop.

---

## 9. Confirmation set

If one level qualifies, run 24 **fresh** confirmation cases at that level.

Confirm only if:

- Valid ≥ 22/24
- TRACEABLE_WRONG ≥ 3/24
- at least 3 distinct wrong cases
- INVALID ≤ 1/24
- TRUNCATED ≤ 1/24

Pass:

```text
NATURAL_ERROR_FRONTIER_CONFIRMED
```

Fail:

```text
NATURAL_ERROR_FRONTIER_NOT_CONFIRMED
```

No development case may be reused.

---

## 10. Pre-defined downstream compatibility

Before inference, every state in every case must already have a frozen downstream mapping:

\[
B_i \rightarrow C_i
\]

Save:

```text
downstream_compatibility.json
```

These mappings are **not shown** during v3.6.4.

This prevents post-hoc construction after seeing which wrong states appear.

---

## 11. Order diagnostic

Because F16 is ACTIVE_WARNING, run a small non-gating diagnostic only:

- 8 seeded development cases
- selected difficulty
- one frozen record-block permutation each

Report:
- same output identity
- changed identity
- validity
- wrong-state persistence

If >3/8 change identity, set:

```text
ORDER_SENSITIVE_FRONTIER = true
```

This does not alter the primary frontier gate.

---

## 12. No-list / no-channel-substitution rules

Because F15/F17 are ACTIVE_WARNING:

Do not use:
- numbered candidate lists,
- multiple choice,
- constrained candidate decoding,
- likelihood ranking,
- scoring channels

to increase natural-error yield.

Only free-generation outputs count toward TRACEABLE_WRONG.

---

## 13. Parser

Normalization only:
- Unicode NFC
- strip outer whitespace
- remove one terminal period

Accepted state regex:

```text
STATE_[A-Z][0-9]{2}
```

No case folding.
No prose extraction.
No prefix repair.

Preserve every raw output.

---

## 14. Model / decoding inheritance

FROZEN_REUSE:
- Qwen3-4B-Instruct-2507
- same pinned revision
- same NF4/BF16 setup
- stateless fresh calls
- greedy decoding
- `use_cache=False`
- frozen seed

Only output cap differs from single-ID components, explicitly to avoid F14 censoring.

---

## 15. Structural pre-inference audit

Before inference verify:

1. dev and confirmation cases frozen,
2. downstream mappings frozen,
3. unique state universe per case,
4. exactly one gold state,
5. every alternate state has downstream mapping,
6. no candidate list,
7. no UNKNOWN rule,
8. no contradictory evidence,
9. difficulty transformations deterministic,
10. no output-based case selection,
11. cap frozen,
12. prompt hashes saved.

Failure:

```text
INFRASTRUCTURE_FAILURE
```

---

## 16. Decision hierarchy

1. `INFRASTRUCTURE_FAILURE`
2. `NO_NATURAL_ERROR_FRONTIER`
3. `NATURAL_ERROR_FRONTIER_NOT_CONFIRMED`
4. `NATURAL_ERROR_FRONTIER_CONFIRMED`

Separate flag:

```text
ORDER_SENSITIVE_FRONTIER = true/false
```

---

## 17. Interpretation

If confirmed, licensed conclusion:

> A frozen free-generation synthetic upstream task produces a reproducible non-zero yield of valid, traceable natural first-hop errors under the tested model and interface.

Do **not** infer:
- natural propagation,
- natural/injected equivalence,
- real-world hallucination rate,
- SHAR/HalluSE behavior,
- internal mechanism,
- larger-model behavior.

---

## 18. Required artifacts

Save under:

```text
results/v3_6_4/
```

Required:

```text
README.md
spec.md
pre_registration.md
prior_findings_review.md
design_audit.pre_inference.md
design_audit.md
development_cases.json
confirmation_cases.json
downstream_compatibility.json
identifier_tokenization_audit.json
prompt_plan.json
prompt_diff_audit.md
decoding_freeze.json
model_manifest.json
development_outputs.jsonl
development_metrics.json
confirmation_outputs.jsonl
confirmation_metrics.json
order_diagnostic_outputs.jsonl
order_diagnostic_metrics.json
parsed_outcomes.jsonl
gate.json
diagnosis.md
interpretation.md
inspection.md
CHANGELOG.md
```

---

## 19. Ledger update requirement

Before designing v3.6.5, update:

- `docs/validated_findings.md`
- `docs/validated_findings.json`
- `docs/validated_findings_audit.md`
- `docs/validated_findings_CHANGELOG.md`

The next spec is incomplete until v3.6.4 is incorporated.

---

## 20. Next experiment if confirmed

Only after:

```text
NATURAL_ERROR_FRONTIER_CONFIRMED
```

may the next experiment forward the **actual naturally generated** state:

\[
A \rightarrow \hat B \rightarrow Y
\]

through the already validated downstream `Current state` shell and estimate separately:

\[
P(C\mid \hat B=B)
\]

and

\[
P(C'\mid \hat B=B')
\]

No injected B′ may count toward the natural-error denominator.

That would be the first clean test of **natural error propagation**.

---

## 21. Core discipline

This version does not repeat validated questions.

It targets exactly one unresolved prerequisite:

\[
\boxed{\text{Can we obtain a stable, valid natural first-hop error source?}}
\]

Everything already validated is inherited.
Everything already known to be brittle is avoided or explicitly controlled.
