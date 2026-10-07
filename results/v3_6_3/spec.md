# v3.6.3 — Two-Hop Propagation Assay Validation

## 0. Purpose

v3.6.1 validated the minimal downstream primitive:

\[
B \rightarrow C,\qquad B' \rightarrow C'
\]

v3.6.2 showed that this primitive remains stable under up to 24 irrelevant mappings.

v3.6.3 adds exactly one new structural component:

\[
A \rightarrow B
\]

The goal is to validate a clean two-hop propagation assay:

\[
A \rightarrow B \rightarrow C
\]

and a controlled counterfactual state intervention:

\[
A \rightarrow \boxed{B'} \rightarrow C'
\]

This is still **Phase I: establish the phenomenon and measurement validity**.

This version does **not** test naturally occurring hallucinations, SHAR/HalluSE, conflicting real-world evidence, long-form generation, internal neural mechanisms, or real-world factual knowledge.

---

# 1. Core research questions

## RQ1 — Upstream capability
Can the model reliably infer the intermediate state from a synthetic upstream mapping?

\[
A \rightarrow B
\]

and symmetrically:

\[
A' \rightarrow B'
\]

## RQ2 — Propagation capability
When an intermediate state is recorded as the result of a previous step, does the downstream answer reliably follow that state?

\[
B \rightarrow C,\qquad B' \rightarrow C'
\]

## RQ3 — Counterfactual propagation
Holding the entity and downstream mapping fixed, does replacing only the recorded intermediate state from \(B\) to \(B'\) causally switch the downstream answer from \(C\) to \(C'\)?

## RQ4 — End-to-end two-hop capability
Can the same model solve the integrated chain:

\[
A \rightarrow B \rightarrow C
\]

within one prompt?

This is a secondary diagnostic because a correct final answer alone does not prove that the model internally represented or used \(B\).

---

# 2. Claim boundary

If v3.6.3 passes, the strongest licensed conclusion is:

> In a validated synthetic two-hop task, Qwen3-4B can reliably compute an upstream intermediate state, and externally changing the recorded intermediate state causally changes the downstream output in the predicted direction.

It does **not** establish spontaneous hallucination snowballing, natural first-hop error rates, that internally generated errors behave identically to injected ones, an internal computational mechanism, SHAR failure/success, or generalization to real-world factual reasoning.

---

# 3. Experimental architecture

Use a two-step modular pipeline.

## Step 1 — Upstream inference
Input: \(A\) plus upstream mappings. Output: \(B\).

## Step 2 — Downstream propagation
Represent the Step-1 state as a recorded intermediate result. Input: \(B\) plus downstream mappings. Output: \(C\).

The counterfactual intervention replaces only the recorded state:

\[
do(B:=B')
\]

and tests whether:

\[
C \rightarrow C'
\]

---

# 4. Synthetic case structure

Each case contains:

```json
{
  "case_id": "v363-main-001",
  "gold_entity": "ENTITY_A17",
  "alt_entity": "ENTITY_M42",
  "gold_state": "STATE_K04",
  "alt_state": "STATE_R83",
  "gold_outcome": "OUTCOME_Q22",
  "alt_outcome": "OUTCOME_Z63"
}
```

Logical structure:

\[
A \rightarrow B,\quad A' \rightarrow B',\quad B \rightarrow C,\quad B' \rightarrow C'
\]

The words `gold`, `alt`, `wrong`, or `correct` must never appear in prompts.

---

# 5. Identifier construction

Use opaque synthetic identifiers only.

Requirements:

- no real-world entities,
- no reuse from v3.6.0–v3.6.2,
- all identifiers globally unique unless intentionally reused within the same case relation,
- A and A′ matched in tokenizer token count,
- B and B′ matched in tokenizer token count,
- C and C′ matched in tokenizer token count,
- similar character lengths within each role pair,
- no identifier is a substring of another,
- no lexical suffix deliberately shared across upstream/downstream roles.

Selection may depend only on deterministic lexical/tokenization criteria.

Never select cases based on model accuracy.

Save full tokenizer audit before inference.

---

# 6. Dataset split

Use:

- **20 calibration cases**
- **40 fresh main cases**

Calibration and main sets must be disjoint.

No failed calibration case may be replaced.

No main case may be selected based on calibration behavior.

---

# 7. Prompt families

## 7.1 U-GOLD — upstream target A

```text
Synthetic transition task.

Upstream mappings:
ENTITY_A17 -> STATE_K04
ENTITY_M42 -> STATE_R83

Current entity:
ENTITY_A17

Return only the mapped state.
```

Expected: `STATE_K04`

## 7.2 U-ALT — symmetric upstream control

Same prompt, except:

```text
Current entity:
ENTITY_M42
```

Expected: `STATE_R83`

The U-GOLD / U-ALT literal prompt diff must be only the current entity identifier.

---

## 7.3 P-GOLD — recorded intermediate state B

```text
Synthetic propagation task.

Recorded intermediate result:
STATE_K04

Downstream mappings:
STATE_K04 -> OUTCOME_Q22
STATE_R83 -> OUTCOME_Z63

Return only the outcome implied by the recorded intermediate result.
```

Expected: `OUTCOME_Q22`

## 7.4 P-ALT — counterfactual intermediate state B′

Identical prompt except:

```text
Recorded intermediate result:
STATE_R83
```

Expected: `OUTCOME_Z63`

The P-GOLD / P-ALT literal prompt diff must be only the recorded state identifier.

No upstream mapping appears in P-GOLD/P-ALT. This is intentional: the downstream call must not be able to recompute or override the supplied state from upstream evidence.

---

# 8. Generated pipeline condition

For each case, execute U-GOLD first.

Let the parsed output be:

\[
\hat{B}
\]

Then construct a downstream prompt using the **actual normalized U-GOLD output** as the recorded intermediate result.

Call this condition:

```text
PIPELINE-GENERATED
```

Important:

- do not silently replace an incorrect upstream output with the expected state,
- do not repair unexpected state IDs beyond frozen parser normalization,
- if upstream output is a well-formed but unmapped state, pass it through exactly and record downstream behavior,
- if upstream output is malformed/INVALID, do not fabricate a downstream state; mark the pipeline upstream-invalid and do not issue a repaired call.

This condition measures the actual modular two-hop pipeline.

---

# 9. Counterfactual intervention condition

For the same case, independently run P-ALT using the predefined alternative state \(B'\).

This is the causal intervention:

\[
do(B:=B')
\]

The primary causal contrast is:

\[
P\text{-GOLD} \quad vs. \quad P\text{-ALT}
\]

not PIPELINE-GENERATED vs P-ALT when upstream itself failed.

---

# 10. Integrated two-hop diagnostic

Run on **20 pre-registered main cases**.

## I-GOLD

```text
Synthetic two-hop task.

Upstream mappings:
ENTITY_A17 -> STATE_K04
ENTITY_M42 -> STATE_R83

Downstream mappings:
STATE_K04 -> OUTCOME_Q22
STATE_R83 -> OUTCOME_Z63

Current entity:
ENTITY_A17

Follow the mappings and return only the final outcome.
```

Expected: `OUTCOME_Q22`

## I-ALT

Same prompt except:

```text
Current entity:
ENTITY_M42
```

Expected: `OUTCOME_Z63`

Total integrated diagnostic calls:

\[
20 \times 2 = 40
\]

These results diagnose whether the model can execute a two-hop chain in one prompt. They do not by themselves establish propagation through an explicit intermediate state.

---

# 11. Calibration stage

For each of 20 calibration cases run:

- U-GOLD
- U-ALT
- P-GOLD
- P-ALT

Total:

\[
20 \times 4 = 80
\]

calibration calls.

Do not run PIPELINE-GENERATED during calibration.

---

# 12. Calibration gates

All must pass.

- A — U-GOLD capability: at least 19/20 correct.
- B — U-ALT capability: at least 19/20 correct.
- C — P-GOLD adherence: at least 19/20 correct.
- D — P-ALT adherence: at least 19/20 correct.
- E — paired upstream symmetry: at least 19/20 cases have both U-GOLD and U-ALT correct.
- F — paired downstream state switch: at least 19/20 cases have both P-GOLD=C and P-ALT=C′.
- G — parse validity: at least 79/80 outputs are exact permitted state/outcome identifiers.

No UNKNOWN fallback is offered in mapped prompts.

If any A–G fails:

```text
STOP_TWO_HOP_CALIBRATION_INVALID
```

Do not run the main experiment.

---

# 13. Main experiment

Run only if calibration passes.

For each of 40 main cases run:

1. U-GOLD
2. U-ALT
3. P-GOLD
4. P-ALT
5. PIPELINE-GENERATED, if U-GOLD produced a valid state string

Maximum:

\[
40 \times 5 = 200
\]

main modular calls.

Also run the pre-registered 40 integrated diagnostic calls.

Maximum total including calibration:

\[
80 + 200 + 40 = 320
\]

calls.

---

# 14. Main metrics

## 14.1 Upstream capability

\[
A_U^G=P(B\mid A)
\]

\[
A_U^A=P(B'\mid A')
\]

## 14.2 Downstream propagation adherence

\[
A_P^G=P(C\mid B)
\]

\[
A_P^A=P(C'\mid B')
\]

## 14.3 Paired counterfactual switch

\[
S_P=P(Y_B=C,\;Y_{B'}=C')
\]

This is the primary propagation-assay metric.

## 14.4 Clean modular pipeline success

\[
E2E=P(U\text{-GOLD}=B \land PIPELINE=C)
\]

Report both:

- strict end-to-end success,
- downstream success conditional on correct upstream state.

Do not hide upstream failures inside downstream accuracy.

## 14.5 Integrated two-hop accuracy

For the 20-case diagnostic subset:

\[
I_G=P(C\mid A,\text{both mapping tables})
\]

\[
I_A=P(C'\mid A',\text{both mapping tables})
\]

Report separately.

---

# 15. Failure categories

## Upstream

For U-GOLD:
- `B`
- `Bp`
- `OTHER_STATE`
- `INVALID`

For U-ALT:
- `Bp`
- `B`
- `OTHER_STATE`
- `INVALID`

## Downstream

- `C`
- `Cp`
- `OTHER_OUTCOME`
- `UNKNOWN`
- `INVALID`

UNKNOWN is parsed if spontaneously generated but never instructed in mapped prompts.

---

# 16. Main gates

The two-hop propagation assay is validated only if all are true.

- G1 — upstream gold: at least 39/40.
- G2 — upstream alternate: at least 39/40.
- G3 — downstream gold: at least 39/40.
- G4 — downstream alternate: at least 39/40.
- G5 — paired propagation switch: at least 39/40.
- G6 — strict clean pipeline: at least 38/40.
- G7 — parser/off-target: across U-GOLD/U-ALT/P-GOLD/P-ALT main calls, OTHER+INVALID ≤2/160.

If G1–G7 pass:

```text
TWO_HOP_PROPAGATION_ASSAY_VALIDATED
```

Otherwise:

```text
TWO_HOP_PROPAGATION_ASSAY_INVALID
```

---

# 17. Integrated readiness flag

The integrated diagnostic does not change G1–G7.

Set:

```text
INTEGRATED_TWO_HOP_READY=true
```

only if:

- I-GOLD ≥19/20
- I-ALT ≥19/20
- paired integrated success ≥19/20

Otherwise:

```text
INTEGRATED_TWO_HOP_READY=false
```

Interpretation:

- assay validated + integrated ready → next stage may study naturally generated first-hop state errors,
- assay validated + integrated not ready → modular propagation is valid, but do not use single-prompt two-hop tasks for natural propagation yet,
- assay invalid → stop Phase I progression.

---

# 18. Optional upstream order diagnostic

Use 10 seeded main cases.

Reverse the two upstream mapping lines and run:

- U-GOLD
- U-ALT

Total 20 diagnostic calls.

Desired:

\[
\ge 19/20
\]

outputs unchanged and correct.

This does not rescue or invalidate G1–G7, but any failure must be prominently reported.

---

# 19. Randomization and inference freeze

Before inference freeze:

- calibration cases,
- main cases,
- integrated subset,
- order-diagnostic subset,
- call order,
- model revision,
- tokenizer,
- chat template,
- quantization,
- decoding.

Recommended:

- same pinned Qwen3-4B-Instruct checkpoint,
- greedy decoding,
- temperature = 0,
- fresh stateless calls,
- no constrained decoding,
- short max_new_tokens sufficient for one identifier.

Do not rerun failed calls.

Do not replace cases.

---

# 20. Prompt-diff audit

Before inference verify:

### U-GOLD vs U-ALT
Only `Current entity` differs.

### P-GOLD vs P-ALT
Only `Recorded intermediate result` differs.

### I-GOLD vs I-ALT
Only `Current entity` differs.

Any unexpected prompt diff is an infrastructure/design failure.

---

# 21. Structural validity checks

Before any model call verify:

1. all identifiers satisfy tokenizer constraints,
2. all relations are one-to-one within a case,
3. no duplicated outcome within a case,
4. calibration/main sets are disjoint,
5. no old identifiers reused,
6. no prompt contains gold/wrong/correct labels,
7. no UNKNOWN instruction in mapped conditions,
8. no answer candidate list,
9. exact prompt hashes saved,
10. no case selected using model outputs.

Failure:

```text
INFRASTRUCTURE_FAILURE
```

---

# 22. Decision hierarchy

Priority:

1. `INFRASTRUCTURE_FAILURE`
2. `STOP_TWO_HOP_CALIBRATION_INVALID`
3. `TWO_HOP_PROPAGATION_ASSAY_INVALID`
4. `TWO_HOP_PROPAGATION_ASSAY_VALIDATED`

Integrated readiness is a separate boolean.

---

# 23. Interpretation matrix

## Outcome A

```text
TWO_HOP_PROPAGATION_ASSAY_VALIDATED
INTEGRATED_TWO_HOP_READY=true
```

Interpretation:

> The synthetic two-hop chain is sufficiently reliable to proceed to a next-stage experiment in which the first-hop state is generated naturally and occasional first-hop errors are tracked downstream.

This does not yet prove natural snowballing.

## Outcome B

```text
TWO_HOP_PROPAGATION_ASSAY_VALIDATED
INTEGRATED_TWO_HOP_READY=false
```

Interpretation:

> Modular state propagation is validated, but single-prompt two-hop execution is not sufficiently reliable. Do not use integrated prompts to study natural propagation yet.

## Outcome C

```text
TWO_HOP_PROPAGATION_ASSAY_INVALID
```

Interpretation:

> The added upstream layer introduces too much instability for clean propagation inference.

Diagnose whether failure is upstream, downstream, or state-interface related before continuing.

## Outcome D

```text
STOP_TWO_HOP_CALIBRATION_INVALID
```

Interpretation:

> The basic two-hop components were not valid on the calibration set. No main propagation conclusion is licensed.

---

# 24. Statistical reporting

Primary unit: 40 main base cases.

Report:

- raw counts and exact denominators,
- Wilson 95% intervals for G1–G6 metrics,
- paired U-GOLD/U-ALT success table,
- paired P-GOLD/P-ALT transition table,
- strict pipeline failures by upstream/downstream source,
- integrated diagnostic separately.

Do not pool upstream and downstream calls into one accuracy number.

Do not treat 160 modular calls as 160 independent semantic cases.

---

# 25. Required artifacts

Save under:

```text
results/v3_6_3/
```

Required files:

```text
README.md
spec.md
pre_registration.md
design_audit.pre_inference.md
design_audit.md
calibration_cases.json
main_cases.json
identifier_pool.json
identifier_tokenization_audit.json
prompt_plan.json
prompt_diff_audit.md
decoding_freeze.json
chat_template.txt
calibration_outputs.jsonl
main_upstream_outputs.jsonl
main_propagation_outputs.jsonl
pipeline_generated_outputs.jsonl
integrated_outputs.jsonl
order_diagnostic_outputs.jsonl
parsed_outcomes.jsonl
metrics.json
integrated_metrics.json
gate.json
diagnosis.md
inspection.md
CHANGELOG.md
```

---

# 26. Design audit table

Before inference include:

| Design intention | Feature | Observable check | Failure meaning |
|---|---|---|---|
| Add only upstream layer | same minimal downstream primitive | template diff audit | confounded stage transition |
| Validate A→B capability | symmetric A/A′ mappings | upstream gates | upstream task too unstable |
| Preserve downstream causal contrast | P-GOLD/P-ALT differ only by state | literal diff | propagation contrast contaminated |
| Prevent recomputation in propagation test | no upstream table in P prompts | prompt audit | state intervention not isolated |
| Test actual modular chain | pass real U-GOLD output to pipeline | pipeline log | repaired-state artifact |
| Avoid world knowledge | opaque IDs | manifest/token audit | parametric shortcut |
| Avoid UNKNOWN brittleness | no fallback instruction | prompt audit | prior artifact reintroduced |
| Avoid candidate primacy | no answer list | prompt audit | option artifact |
| Separate integrated capability | secondary one-prompt diagnostic | separate metrics | no mechanism overclaim |
| Avoid adaptive tuning | frozen cases/gates | hashes | post-hoc overfit |
| Preserve claim boundary | Phase I only | diagnosis | no natural snowballing/SHAR claim |

---

# 27. What comes after v3.6.3

If and only if:

```text
TWO_HOP_PROPAGATION_ASSAY_VALIDATED
```

and preferably:

```text
INTEGRATED_TWO_HOP_READY=true
```

the next Phase I experiment may study **naturally generated first-hop errors**.

That next experiment should ask:

> When the model itself outputs \(B'\) instead of \(B\), and that actual generated state is carried forward unchanged, does the downstream model produce \(C'\) at a higher rate?

That is the first stage where the term **natural error propagation** becomes appropriate.

Do not add SHAR until that phenomenon is established.

---

# 28. Core discipline

v3.6.3 is not trying to create hallucinations.

It is validating the causal pipeline needed to interpret hallucinations later.

The key measurement object is:

\[
A \rightarrow \hat{B} \rightarrow Y
\]

with a controlled intervention:

\[
do(\hat{B}=B')
\]

Only after this pipeline is demonstrably reliable should Phase I attempt to observe naturally occurring \(B'\) and test whether those errors propagate.


## Frozen execution details

The optional20-call upstream-order diagnostic is included. Maximum total is340 (80 calibration +200 modular +40 integrated +20 order). Pipeline outputs are generated from actual normalized U-GOLD states; their templates/builders and call order are frozen, actual prompt hashes are recorded at runtime.
