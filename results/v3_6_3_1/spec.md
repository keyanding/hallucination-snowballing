# v3.6.3.1 effective specification

## Validated Inheritance

| Prior | Component / result | Classification | Treatment | Validation |
|---|---|---|---|---|
| v3.6.1/v3.6.2 | minimal downstream shell: Minimal mapped-state interface passed | FROZEN_REUSE | Reuse Current state shell exactly | Byte equality to both frozen renderers; calibration C/D/F/G |
| v3.6.1 | mapped-state UNKNOWN policy: Fallback unnecessary for mapped-state assay; tested alternatives brittle | FROZEN_REUSE | No UNKNOWN rule in any prompt | Literal prompt audit |
| v3.6.1/v3.6.3 | identifiers and parser: Opaque matched IDs and exact parsing established | FROZEN_REUSE | Same generator, expanded historical exclusion; exact v3.6.3 parser | 7800-candidate token audit, freshness and parser tests |
| v3.6.2 | context accumulation: No failures up to 24 irrelevant mappings | NOT_RELEVANT | Use two mappings without distractors | Exactly two downstream records |
| v3.6.2 | record position: No position failures observed in tested diagnostic | NOT_RELEVANT | No new main position manipulation; retain balanced order construction | Inherited order construction audit |
| v3.6.3 | upstream shell: Calibration upstream A/B/paired each 20/20 | FROZEN_REUSE | Reuse upstream renderer exactly | Byte equality and calibration A/B/E/G |
| v3.6.3 | recorded shell: Recorded shell calibration had three exact-output failures | INTENTIONALLY_RETESTED | Exact former shell in independent diagnostic only | Paired same-state/mapping shell comparison; non-gating |
| v3.6.1/v3.6.2/v3.6.3 | model and decoding: Pinned NF4/BF16 stateless greedy stack used | FROZEN_REUSE | Same revision/tokenizer/chat template, seed42, cap16 | Versions, template hash, render hash and runtime manifest |
| v3.6.3 | integrated shell: Integrated shell frozen but untested after failed calibration | INTENTIONALLY_RETESTED | Reuse exact integrated renderer on 20 main cases after main passes | Separate readiness thresholds, no main-gate effect |

## New manipulation

Actual U-A output is forwarded unchanged into the validated Current state interface.

## Execution resolutions

# v3.6.3.1 pre-registration

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


---

## Supplied source specification (verbatim text)

# v3.6.3.1 — Two-Hop Pipeline with Frozen Validated Downstream Interface

## 0. Purpose

v3.6.3 failed calibration because the experiment changed more than one design dimension at once.

The upstream component:

\[
A \rightarrow B
\]

was validated in calibration:

- U-GOLD: 20/20
- U-ALT: 20/20
- paired upstream success: 20/20

The downstream component did **not** fail because the mapping relation was demonstrably wrong. It failed because v3.6.3 replaced the previously validated downstream interface:

```text
Current state:
STATE_K04
```

with a new interface:

```text
Recorded intermediate result:
STATE_K04
```

and also changed surrounding wording. Three failures were exact-output compliance failures.

Therefore v3.6.3.1 applies one principle:

> **Reuse previously validated components exactly unless the current experiment explicitly studies that component.**

The purpose of v3.6.3.1 is to validate the two-hop modular pipeline while restoring the downstream prompt shell that already passed v3.6.1 and v3.6.2.

---

# 1. Frozen inheritance from prior validated experiments

The following conclusions are treated as **frozen design constraints**.

They are not re-designed in this version.

## 1.1 From v3.6.1

Validated:

\[
B \rightarrow C,\qquad B' \rightarrow C'
\]

under the minimal prompt:

```text
Synthetic mapping task.

Mappings:
STATE_K4 -> OUTCOME_Q2
STATE_M9 -> OUTCOME_Z6

Current state:
STATE_K4

Return only the mapped outcome.
```

Key validated design choices:

- no entity in downstream prompt,
- no UNKNOWN instruction in mapped-state prompts,
- no candidate list,
- opaque synthetic identifiers,
- matched tokenizer construction,
- exact-output parser,
- stateless greedy Qwen3-4B,
- C0/W0 differ only by supplied state.

These are frozen.

## 1.2 From v3.6.2

Validated:

- the same minimal downstream primitive remains reliable with up to 24 irrelevant mappings,
- record position did not create observed failures in the tested diagnostic.

Therefore:

- context accumulation is not required in v3.6.3.1,
- the minimal downstream shell remains the reference interface,
- no new downstream wording should be introduced.

## 1.3 From v3.6.3

Validated:

\[
A \rightarrow B,\qquad A' \rightarrow B'
\]

in the upstream synthetic lookup shell:

- U-GOLD: 20/20
- U-ALT: 20/20
- paired upstream success: 20/20

Therefore the upstream design is frozen and reused.

The only failed component was the new downstream shell.

---

# 2. What is allowed to change in v3.6.3.1

Only one structural addition is allowed:

> **Forward the actual output of the validated upstream step into the validated downstream `Current state` field.**

No other conceptual dimension should change.

Specifically, this version does **not** change:

- model,
- decoding,
- tokenizer,
- identifier family,
- parser rules,
- upstream prompt shell,
- downstream minimal prompt shell,
- no-UNKNOWN policy,
- no-candidate-list policy,
- case-selection logic.

---

# 3. Research questions

## RQ1 — Modular two-hop pipeline validity

Can the model execute:

\[
A \rightarrow B
\]

and then, with the actual generated \(B\) inserted into the previously validated downstream shell:

\[
B \rightarrow C
\]

to produce a correct end-to-end result?

## RQ2 — Counterfactual propagation

If the downstream `Current state` is changed from \(B\) to \(B'\), does the outcome switch from \(C\) to \(C'\)?

\[
do(B:=B') \Rightarrow C'
\]

## RQ3 — Interface compatibility diagnostic

Does the previously validated `Current state` shell outperform the failed v3.6.3 `Recorded intermediate result` shell on the same mappings?

This is a small diagnostic only.

It does not alter the main gate.

---

# 4. Claim boundary

If v3.6.3.1 passes, the strongest licensed conclusion is:

> In a validated synthetic modular two-hop task, the model can infer an upstream state and, when that actual state is forwarded into the previously validated downstream interface, produce the corresponding downstream outcome. Replacing the state with a counterfactual alternative predictably changes the downstream outcome.

This still does **not** establish:

- natural hallucination propagation,
- spontaneous first-hop error rates,
- equivalence between injected and naturally generated errors,
- internal neural mechanism,
- SHAR/HalluSE performance,
- real-world factual reasoning.

---

# 5. Synthetic case structure

Each case contains:

```json
{
  "case_id": "v3631-main-001",
  "entity_a": "ENTITY_A17",
  "entity_b": "ENTITY_M42",
  "state_a": "STATE_K04",
  "state_b": "STATE_R83",
  "outcome_a": "OUTCOME_Q22",
  "outcome_b": "OUTCOME_Z63"
}
```

Logical structure:

\[
A \rightarrow B
\]

\[
A' \rightarrow B'
\]

\[
B \rightarrow C
\]

\[
B' \rightarrow C'
\]

Prompt text must never include the words:

- gold,
- wrong,
- correct,
- alt,
- error.

Those labels may exist only in internal metadata.

---

# 6. Dataset

Use:

- 20 calibration cases,
- 40 fresh main cases.

Calibration/main sets are disjoint.

No failed case may be replaced.

No case may be selected based on model behavior.

Prefer reuse of v3.6.3 identifier-generation logic, but generate a fresh case set for this version to avoid hidden dependence on previous outputs.

---

# 7. Identifier construction

Use the same construction principles validated previously:

- opaque synthetic identifiers only,
- no real-world semantics,
- matched tokenizer counts within role pairs,
- similar character lengths,
- globally unique identifiers unless intentionally reused within one case relation,
- no substring relation,
- no model-output-based selection.

Freeze and save tokenizer audit before inference.

---

# 8. Frozen upstream prompt

Reuse the v3.6.3 upstream shell.

## U-A

```text
Synthetic transition task.

Upstream mappings:
ENTITY_A17 -> STATE_K04
ENTITY_M42 -> STATE_R83

Current entity:
ENTITY_A17

Return only the mapped state.
```

Expected:

```text
STATE_K04
```

## U-B

Same prompt, except:

```text
Current entity:
ENTITY_M42
```

Expected:

```text
STATE_R83
```

Literal diff must be only the current entity identifier.

---

# 9. Frozen downstream prompt

Reuse the validated v3.6.1/v3.6.2 shell exactly.

## D-A

```text
Synthetic mapping task.

Mappings:
STATE_K04 -> OUTCOME_Q22
STATE_R83 -> OUTCOME_Z63

Current state:
STATE_K04

Return only the mapped outcome.
```

Expected:

```text
OUTCOME_Q22
```

## D-B

Identical except:

```text
Current state:
STATE_R83
```

Expected:

```text
OUTCOME_Z63
```

The D-A / D-B literal diff must be only the current state identifier.

No new state heading or propagation-specific prose is allowed in the main assay.

---

# 10. Generated pipeline

For each case:

1. Run U-A.
2. Parse the actual normalized upstream output.
3. If it is a valid state identifier, place it unchanged into the frozen downstream shell under:

```text
Current state:
{ACTUAL_UPSTREAM_OUTPUT}
```

4. Run the downstream call.

Call this:

```text
PIPELINE-A
```

Important:

- no correction to expected state,
- no prefix repair,
- no extraction from prose,
- no replacement with oracle state,
- no state relabeling.

If the upstream output is malformed/INVALID:

- do not issue a repaired downstream call,
- record a pipeline skip,
- count strict end-to-end failure.

If the upstream output is a well-formed but unmapped `STATE_*`:

- pass it through unchanged,
- do not add UNKNOWN instructions,
- record downstream output descriptively.

---

# 11. Counterfactual intervention

Independently run D-B.

This implements:

\[
do(B:=B')
\]

The main propagation contrast is:

\[
D\text{-A} \quad vs. \quad D\text{-B}
\]

because these differ only in `Current state`.

---

# 12. Calibration stage

For each of 20 calibration cases run:

- U-A
- U-B
- D-A
- D-B

Total:

\[
20 \times 4 = 80
\]

calls.

Do not run generated pipeline or diagnostics until calibration passes.

---

# 13. Calibration gates

All must pass.

## A — upstream A

At least:

\[
19/20
\]

## B — upstream B

At least:

\[
19/20
\]

## C — downstream A

At least:

\[
19/20
\]

## D — downstream B

At least:

\[
19/20
\]

## E — paired upstream

At least:

\[
19/20
\]

cases have both U-A and U-B correct.

## F — paired downstream switch

At least:

\[
19/20
\]

cases have both D-A and D-B correct.

## G — exact parse compliance

At least:

\[
79/80
\]

outputs are exact permitted identifiers.

If any fail:

```text
STOP_V3631_CALIBRATION_INVALID
```

No main calls.

---

# 14. Main experiment

Run only if calibration passes.

For each of 40 main cases:

1. U-A
2. U-B
3. D-A
4. D-B
5. PIPELINE-A if U-A produced a valid state identifier

Maximum main modular calls:

\[
40 \times 5 = 200
\]

---

# 15. Primary metrics

## Upstream A adherence

\[
A_U^A=P(B\mid A)
\]

## Upstream B adherence

\[
A_U^B=P(B'\mid A')
\]

## Downstream A adherence

\[
A_D^A=P(C\mid B)
\]

## Downstream B adherence

\[
A_D^B=P(C'\mid B')
\]

## Paired counterfactual switch

\[
S_D=P(Y_B=C,\;Y_{B'}=C')
\]

## Strict modular end-to-end

\[
E2E=P(U\text{-A}=B \land PIPELINE\text{-A}=C)
\]

Also report:

\[
P(PIPELINE=C\mid U\text{-A}=B)
\]

separately.

---

# 16. Main gates

All must pass.

## G1

\[
A_U^A \ge 39/40
\]

## G2

\[
A_U^B \ge 39/40
\]

## G3

\[
A_D^A \ge 39/40
\]

## G4

\[
A_D^B \ge 39/40
\]

## G5

\[
S_D \ge 39/40
\]

## G6

\[
E2E \ge 38/40
\]

## G7

Across U-A/U-B/D-A/D-B main calls:

\[
OTHER + INVALID \le 2/160
\]

If all pass:

```text
TWO_HOP_PIPELINE_VALIDATED
```

Else:

```text
TWO_HOP_PIPELINE_INVALID
```

---

# 17. Shell compatibility diagnostic

This diagnostic explicitly tests the failure observed in v3.6.3.

Use **10 seeded calibration-independent cases** after main completion.

For each case, use the same state and mapping in two prompt shells.

## VALIDATED shell

```text
Synthetic mapping task.

Mappings:
STATE_K04 -> OUTCOME_Q22
STATE_R83 -> OUTCOME_Z63

Current state:
STATE_K04

Return only the mapped outcome.
```

## RECORDED shell

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_K04

Downstream mappings:
STATE_K04 -> OUTCOME_Q22
STATE_R83 -> OUTCOME_Z63

Return only the outcome implied by the recorded intermediate result.
```

Run both states in both shells.

Total:

\[
10 \times 2 \times 2 = 40
\]

diagnostic calls.

Report:

- exact-output accuracy,
- INVALID count,
- explanation-format count,
- prefix-omission count,
- truncation count.

This diagnostic is **non-gating**.

It is included only to test whether the v3.6.3 shell itself caused compliance brittleness.

No inference about internal mechanism is allowed.

---

# 18. Integrated two-hop diagnostic

Only run if main assay passes.

Use 20 seeded main cases.

Reuse the v3.6.3 integrated prompt unchanged.

Report separately:

- I-A accuracy,
- I-B accuracy,
- paired integrated accuracy.

Define:

```text
INTEGRATED_TWO_HOP_READY=true
```

only if each required metric is at least 19/20.

This is not part of G1–G7.

---

# 19. Parser

Freeze the same exact parser discipline.

## Upstream

Valid exact outputs:

- expected state,
- paired state.

Any other well-formed `STATE_[A-Z][0-9]{2}`:

```text
OTHER_STATE
```

Anything else:

```text
INVALID
```

## Downstream

Valid exact outputs:

- expected outcome,
- paired outcome.

Other well-formed `OUTCOME_[A-Z][0-9]{2}`:

```text
OTHER_OUTCOME
```

Literal `UNKNOWN`:

```text
UNKNOWN
```

Anything else:

```text
INVALID
```

Normalization only:

- Unicode NFC,
- strip outer whitespace,
- remove one final period.

No extraction.

No prefix repair.

No prose parsing.

---

# 20. Inference freeze

Use the same validated stack:

- pinned Qwen3-4B-Instruct checkpoint,
- same model revision,
- same tokenizer,
- same chat template,
- same NF4/BF16 setup,
- greedy decoding,
- temperature 0,
- fresh stateless calls,
- no constrained decoding,
- same or sufficiently short frozen output cap for one identifier.

Important:

Do **not** increase max_new_tokens merely to accommodate explanatory output.

The target interface is exact identifier emission.

---

# 21. Structural audit before inference

Verify:

1. U-A/U-B differ only in entity identifier.
2. D-A/D-B differ only in current state identifier.
3. downstream shell is byte-identical to the validated v3.6.1/v3.6.2 template apart from identifiers.
4. no UNKNOWN instruction appears in mapped prompts.
5. no candidate list appears.
6. no `Recorded intermediate result` wording appears in main downstream prompts.
7. all identifiers satisfy tokenizer constraints.
8. calibration/main/diagnostic sets are disjoint.
9. all prompt hashes are frozen.
10. no model-output-based case selection occurred.

Any failure:

```text
INFRASTRUCTURE_FAILURE
```

---

# 22. Decision hierarchy

Priority:

1. `INFRASTRUCTURE_FAILURE`
2. `STOP_V3631_CALIBRATION_INVALID`
3. `TWO_HOP_PIPELINE_INVALID`
4. `TWO_HOP_PIPELINE_VALIDATED`

Integrated readiness and shell-diagnostic results are separate fields.

---

# 23. Interpretation matrix

## Case A

```text
TWO_HOP_PIPELINE_VALIDATED
INTEGRATED_TWO_HOP_READY=true
```

Interpretation:

> The modular two-hop pipeline is validated, and the model is also capable of integrated two-hop execution. The next Phase I stage may begin studying naturally generated first-hop errors.

## Case B

```text
TWO_HOP_PIPELINE_VALIDATED
INTEGRATED_TWO_HOP_READY=false
```

Interpretation:

> The modular pipeline is valid, but integrated single-prompt execution is not yet reliable enough for natural-error propagation experiments.

## Case C

```text
TWO_HOP_PIPELINE_INVALID
```

Interpretation:

> Even after restoring the validated downstream interface, the combined upstream→forwarding→downstream pipeline is not sufficiently reliable.

Diagnose the interface boundary or actual state-forwarding behavior.

## Case D

```text
STOP_V3631_CALIBRATION_INVALID
```

Interpretation:

> A previously validated component failed to reproduce on fresh cases. Stop and investigate replication before proceeding.

---

# 24. Required artifacts

Save under:

```text
results/v3_6_3_1/
```

Required:

```text
README.md
spec.md
pre_registration.md
design_audit.pre_inference.md
design_audit.md
calibration_cases.json
main_cases.json
diagnostic_cases.json
identifier_pool.json
identifier_tokenization_audit.json
prompt_plan.json
prompt_diff_audit.md
decoding_freeze.json
chat_template.txt
calibration_outputs.jsonl
main_upstream_outputs.jsonl
main_downstream_outputs.jsonl
pipeline_generated_outputs.jsonl
pipeline_log.jsonl
shell_diagnostic_outputs.jsonl
shell_diagnostic_metrics.json
integrated_outputs.jsonl
integrated_metrics.json
parsed_outcomes.jsonl
metrics.json
gate.json
diagnosis.md
interpretation.md
inspection.md
CHANGELOG.md
```

---

# 25. Design inheritance audit

Before inference create an explicit inheritance table:

| Prior version | Validated conclusion | v3.6.3.1 treatment |
|---|---|---|
| v3.6.1 | minimal B→C shell valid | reuse exactly |
| v3.6.1 | UNKNOWN rule unnecessary and potentially brittle | omit from mapped prompts |
| v3.6.1 | opaque IDs + exact parser valid | reuse |
| v3.6.2 | up to 24 irrelevant mappings not needed for basic validity | do not add distractors here |
| v3.6.2 | position not observed to matter in tested range | no new position manipulation in main |
| v3.6.3 | A→B upstream shell valid | reuse exactly |
| v3.6.3 | new Recorded intermediate result shell failed calibration | remove from main; diagnostic only |

This table must be frozen before inference.

---

# 26. Rule for all future versions

From v3.6.3.1 onward:

> **Every new spec must contain a `Validated Inheritance` section before introducing any new manipulation.**

For each previously established result, explicitly classify it as:

- `FROZEN_REUSE`
- `INTENTIONALLY_RETESTED`
- `NOT_RELEVANT`

No previously validated component may be silently modified.

If a component is modified, the spec must state:

1. why it is modified,
2. which prior conclusion no longer applies,
3. what new validation is required.

This rule is part of the experimental workflow, not just documentation style.

---

# 27. What comes next

If:

```text
TWO_HOP_PIPELINE_VALIDATED
```

and preferably:

```text
INTEGRATED_TWO_HOP_READY=true
```

then the next Phase I stage may study **natural first-hop error propagation**:

\[
A \rightarrow \hat{B}
\]

where \(\hat{B}\) is the model's own generated first-hop state.

Then compare:

\[
P(C' \mid \hat{B}=B')
\]

against:

\[
P(C' \mid \hat{B}=B)
\]

while forwarding the actual state unchanged.

That is the first experiment in which naturally occurring state errors become the object of study.

SHAR/HalluSE should still remain outside the experiment until natural propagation itself is established.

---

# 28. Core discipline

v3.6.3.1 is a repair-by-inheritance experiment.

Its purpose is not to invent a better prompt.

Its purpose is to test the two-hop pipeline while preserving every component that has already been shown to work.

The key principle is:

\[
\boxed{\text{one new variable per stage}}
\]

and:

\[
\boxed{\text{validated components remain frozen unless explicitly retested}}
\]
