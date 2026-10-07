# v3.6.1 — Minimal Propagation Primitive & Failure Diagnosis

## 0. Purpose

v3.6.0 failed assay calibration even though direct mapping lookup was almost perfect.

Observed pattern:

- direct mapping lookup: 39/40
- C0 correct-state adherence: 17/20
- W0 wrong-state adherence: 20/20
- mapping swap: 19/20
- record-order invariance: 15/20
- unmapped → UNKNOWN: 20/20
- entity-label invariance: 17/20
- parse validity: 160/160

The purpose of v3.6.1 is **not** to force the assay to pass.

It is to distinguish three competing explanations:

1. **Model robustness limitation** — Qwen3-4B understands the task nominally but is not robust enough under this symbolic prompt family.
2. **Prompt brittleness / fallback interference** — extra prompt structure, especially entity scaffolding and the global UNKNOWN instruction, creates avoidable execution failures.
3. **Dataset / surface-form artifact** — identifier tokenization, mapping order, or other construction details systematically affect behavior.

This version also attempts to validate a **minimal state-propagation primitive** before rebuilding any A→B→C task.

No SHAR, HalluSE, natural hallucination, or internal-mechanism claim is allowed.

---

## 1. Research questions

### RQ1 — Is the v3.6.0 failure caused by prompt complexity?
Does removing irrelevant entity scaffolding and simplifying the instruction increase mapped-state accuracy?

### RQ2 — Does the global UNKNOWN rule create fallback overuse?
Does removing the UNKNOWN instruction from mapped-state prompts reduce false `UNKNOWN` responses?

### RQ3 — Are failures associated with surface form?
Are v3.6.0 failures associated with identifier token counts, mapping-line position, lexical form, or other frozen construction features?

### RQ4 — Can Qwen3-4B reliably execute a minimal propagation primitive?
Can the model satisfy

\[
B \rightarrow C,\qquad B' \rightarrow C'
\]

with near-perfect reliability when irrelevant structure is removed?

---

## 2. Claim boundary

Even if v3.6.1 passes, it licenses only:

> Qwen3-4B can reliably follow an explicitly supplied symbolic state-to-outcome mapping under a validated minimal prompt.

It does **not** establish natural hallucination propagation, multi-hop snowballing, SHAR behavior, internal mechanisms, robustness to arbitrary context, or real-world factual reasoning.

---

## 3. Stage A — Static audit of v3.6.0

Use existing v3.6.0 artifacts only. No model calls.

Audit all 20 v3.6.0 calibration cases. For every identifier record:

- raw string,
- tokenizer token IDs,
- token count,
- character length,
- state mapping line position,
- outcome mapping line position,
- entity token count,
- whether case failed C0,
- whether case failed REVERSE,
- whether case failed ENTITY_LABEL,
- whether any mapped condition produced UNKNOWN.

Required outputs:

```text
results/v3_6_1/v360_failure_audit.json
results/v3_6_1/v360_failure_audit.md
```

Report descriptive associations only. Do not claim causality from 20 cases.

Specifically check:

1. Are the three C0 failures concentrated in first-line or second-line mappings?
2. Do failed state IDs have systematically different tokenizer lengths?
3. Do failed outcome IDs have systematically different tokenizer lengths?
4. Do failed entity IDs have unusual tokenizer lengths?
5. Do failures share any lexical prefix/suffix pattern?
6. Does REVERSE failure occur mainly when C0 was already wrong?
7. Does ENTITY_LABEL failure occur because ENTITY_LABEL becomes correct while C0 is wrong, or because ENTITY_LABEL itself becomes wrong?

---

## 4. Stage B — Controlled replay on all 20 old calibration cases

Use the same 20 v3.6.0 calibration cases. Do **not** test only the three failed cases.

For each case, render both the original gold state and original wrong state under four prompt families.

Total:

\[
20 \times 2 \times 4 = 160
\]

new model calls.

Use the same pinned Qwen3-4B checkpoint, tokenizer, NF4/BF16 stack, chat template, greedy decoding, and fresh stateless calls as v3.6.0.

### 4.1 Factor 1 — full vs minimal prompt

#### FULL
Keep:
- synthetic task introduction,
- downstream mapping block,
- current entity,
- working intermediate state,
- full natural-language question.

#### MINIMAL
Remove:
- current entity,
- entity-specific question,
- all prose not necessary for state→mapping execution.

Use:

```text
Synthetic mapping task.

Mappings:
{STATE_1} -> {OUTCOME_1}
{STATE_2} -> {OUTCOME_2}

Current state:
{SUPPLIED_STATE}

Return only the mapped outcome.
```

### 4.2 Factor 2 — UNKNOWN rule present vs absent

#### +UNKNOWN
Append:

```text
If the current state has no mapping, output UNKNOWN.
```

#### -UNKNOWN
Do not mention UNKNOWN at all.

Mapped-state conditions must never require UNKNOWN. The purpose is to test whether the mere availability of an explicit fallback causes false fallback behavior.

### 4.3 Four replay prompt families

For each case and for both B and B′:

1. `FULL_UNKNOWN`
2. `FULL_NO_UNKNOWN`
3. `MINIMAL_UNKNOWN`
4. `MINIMAL_NO_UNKNOWN`

The mappings themselves remain identical to the old case. The supplied state remains identical.

---

## 5. Stage B metrics

For each prompt family report separately:

### Gold-state adherence
\[
A_C=P(C\mid B)
\]

### Wrong-state adherence
\[
A_W=P(C'\mid B')
\]

### False-UNKNOWN rate among mapped states
\[
U=P(UNKNOWN\mid B\text{ or }B')
\]

### Paired correct-following rate
\[
S=P(Y_B=C,\;Y_{B'}=C')
\]

Also report exact paired transitions across prompt families.

---

## 6. Stage B interpretation logic

The purpose is diagnosis, not significance testing.

### Pattern P1 — UNKNOWN-rule interference
If no-UNKNOWN variants outperform matched UNKNOWN variants and false-UNKNOWN outputs materially decrease, this supports prompt/fallback interference.

Do not call it an internal mechanism.

### Pattern P2 — prompt-complexity brittleness
If MINIMAL variants outperform FULL variants while mappings are unchanged, this supports surface-form/prompt-complexity brittleness.

### Pattern P3 — persistent 4B limitation
If `MINIMAL_NO_UNKNOWN` still fails more than 1/40 mapped calls, the 4B model is not sufficiently reliable for the minimal assay under the current identifier family.

This triggers the conditional stronger-model diagnostic in Section 10.

---

## 7. Stage C — Fresh minimal propagation primitive

Run this stage regardless of which Stage B factor appears responsible, unless execution infrastructure itself failed.

Use **40 fresh cases** with no overlap with v3.6.0 identifiers.

There is no entity. There is no UNKNOWN instruction in mapped-state prompts.

Each case contains only:

\[
B \rightarrow C
\]
\[
B' \rightarrow C'
\]

### 7.1 Identifier construction

Before inference, generate a large candidate pool of synthetic state/outcome identifiers.

Tokenizer-audit every candidate.

Construct cases so that, within each case:

- B and B′ have equal tokenizer token counts,
- C and C′ have equal tokenizer token counts,
- identifier character lengths are closely matched,
- no identifier is a substring of another,
- no outcome shares a distinctive suffix with its paired state,
- mapping-line position of B vs B′ is balanced 20/20 across cases.

Prefer identifiers that tokenize into a small, stable number of tokens.

Do not search identifier combinations using model accuracy. Identifier selection may depend only on deterministic lexical/tokenization criteria frozen before inference.

Save:

```text
identifier_pool.json
identifier_tokenization_audit.json
```

### 7.2 Minimal prompt

Example:

```text
Synthetic mapping task.

Mappings:
STATE_K4 -> OUTCOME_Q2
STATE_M9 -> OUTCOME_Z6

Current state:
STATE_K4

Return only the mapped outcome.
```

C0 expected: `OUTCOME_Q2`

W0 is identical except `Current state: STATE_M9`, expected `OUTCOME_Z6`.

Literal C0/W0 diff must be the supplied state identifier only.

No `UNKNOWN` instruction is present.

---

## 8. Separate unmapped control

UNKNOWN behavior is no longer mixed into normal mapped-state prompts.

Use **10 additional fresh control cases**.

Prompt:

```text
Synthetic mapping task.

Mappings:
STATE_K4 -> OUTCOME_Q2
STATE_M9 -> OUTCOME_Z6

Current state:
STATE_X7

If the current state has no mapping, output UNKNOWN.
Return only the mapped outcome or UNKNOWN.
```

Expected: `UNKNOWN`.

These calls test fallback behavior only. They are not included in C0/W0 propagation metrics.

---

## 9. Stage C gates

Mapped-state main calls:

\[
40 \times 2 = 80
\]

Unmapped controls: 10.

Total Stage C = 90 model calls.

The minimal propagation primitive is validated only if all hold:

### C1 — Gold-state adherence
\[
A_C \ge 39/40
\]

### C2 — Wrong-state adherence
\[
A_W \ge 39/40
\]

### C3 — Paired state-following
\[
S \ge 39/40
\]

### C4 — False UNKNOWN in mapped prompts
Because UNKNOWN is not offered as an instruction in mapped prompts:

\[
\text{mapped UNKNOWN}=0/80
\]

### C5 — Other/invalid
\[
OTHER + INVALID \le 1/80
\]

### C6 — Unmapped fallback
At least 9/10 unmapped controls output `UNKNOWN`.

If C1–C6 pass:

```text
MINIMAL_ASSAY_VALIDATED
```

Otherwise:

```text
MINIMAL_ASSAY_INVALID
```

No threshold may be changed after inference.

---

## 10. Conditional stronger-model diagnostic

This is diagnostic only and never rescues the 4B assay.

Run only if `MINIMAL_ASSAY_INVALID` and a stronger compatible model is already available without changing the task or requiring ad hoc infrastructure.

Preferred hierarchy:

1. stronger Qwen3-family instruct model with the closest possible chat/inference setup,
2. otherwise another clearly stronger instruct model.

Use exactly:

- all failed Stage C mapped prompts,
- plus an equal-size seeded sample of passed Stage C mapped prompts.

Do not regenerate cases or change prompts.

Report side-by-side:

```text
4B result
stronger-model result
```

Interpretation:

- failures disappear on stronger model → supports model-capability/robustness limitation;
- same prompts fail on both → supports assay/surface-form artifact;
- mixed → unresolved.

If no stronger compatible model is available, record:

```text
STRONGER_MODEL_DIAGNOSTIC_NOT_RUN
```

Do not substitute a different prompt.

---

## 11. Record-order diagnostic in Stage C

For 10 seeded Stage C cases, after primary cases are frozen, pre-register a reversed-mapping rendering.

Run 20 calls total:
- 10 C0 reverse,
- 10 W0 reverse.

Desired:

\[
\ge 19/20
\]

unchanged mapped identity.

Failure does not retroactively change C1–C6, but must be prominently reported as a limitation before proceeding to more complex assays.

---

## 12. Parsing

For mapped conditions accepted categories are:
- exact expected outcome,
- paired alternative outcome,
- `UNKNOWN`,
- `OTHER`,
- `INVALID`.

Normalization only:
- Unicode NFC,
- strip outer whitespace,
- remove one terminal period.

No extraction from explanatory text.

For unmapped controls, exact `UNKNOWN` is correct; everything else is incorrect and categorized.

---

## 13. Required pre-inference audit

Before any new Stage B/C model call:

1. Freeze all prompt templates.
2. Freeze all 20 Stage B case renderings.
3. Freeze all 40 Stage C case definitions.
4. Freeze the 10 unmapped controls.
5. Freeze the 10 record-order diagnostic cases.
6. Freeze decoding parameters.
7. Write prompt hashes.
8. Verify Stage C C0/W0 pairwise literal diffs.
9. Verify tokenizer-balance constraints.
10. Verify no model-output-based identifier selection occurred.

---

## 14. Required artifacts

Save under:

```text
results/v3_6_1/
```

Required:

```text
README.md
spec.md
pre_registration.md
design_audit.pre_inference.md
design_audit.md
v360_failure_audit.json
v360_failure_audit.md
identifier_pool.json
identifier_tokenization_audit.json
stage_b_prompt_plan.json
stage_b_outputs.jsonl
stage_b_metrics.json
stage_c_cases.json
stage_c_prompt_plan.json
stage_c_outputs.jsonl
stage_c_metrics.json
unmapped_outputs.jsonl
record_order_outputs.jsonl
prompt_diff_audit.md
decoding_freeze.json
chat_template.txt
gate.json
diagnosis.md
inspection.md
CHANGELOG.md
```

If stronger-model diagnostic runs:

```text
stronger_model_manifest.json
stronger_model_outputs.jsonl
stronger_model_diagnosis.md
```

---

## 15. Design audit

| Design intention | Feature | Observable check | Failure meaning |
|---|---|---|---|
| Diagnose v3.6.0 rather than tune failures | all 20 old cases replayed | no failure-only selection | avoids cherry-picking |
| Test UNKNOWN interference | mapped prompts with/without fallback rule | false-UNKNOWN contrast | fallback may induce brittleness |
| Test prompt complexity | FULL vs MINIMAL | adherence contrast | irrelevant structure affects execution |
| Remove entity confound | no entity in minimal primitive | exact template audit | entity artifact eliminated |
| Reduce tokenization confound | matched token counts | tokenizer audit | identifier construction still asymmetric |
| Preserve causal contrast | C0/W0 differ only in state | literal diff hashes | contaminated intervention |
| Separate fallback behavior | dedicated unmapped controls | >=9/10 UNKNOWN | fallback task invalid |
| Avoid option primacy | no answer list | prompt audit | prior artifact reintroduced |
| Diagnose model size only if needed | conditional stronger model | same frozen prompts | no rescue-by-retuning |
| Prevent adaptive optimization | frozen cases/thresholds | hashes + gate | post-hoc overfit |
| Preserve claim boundary | minimal primitive only | diagnosis | no snowballing/SHAR claim |

---

## 16. Decision logic

Final `gate.json` must contain:

```text
stage_b_completed
stage_b_best_descriptive_condition
stage_c_pass
record_order_diagnostic_pass
stronger_model_diagnostic_status
final_decision
```

Allowed final decisions:

```text
MINIMAL_ASSAY_VALIDATED
MINIMAL_ASSAY_INVALID
INFRASTRUCTURE_FAILURE
```

Do not use “mostly passed”.

---

## 17. How to interpret likely outcomes

### Outcome A
`MINIMAL_NO_UNKNOWN` is near-perfect and Stage C passes.

Interpretation:

> Qwen3-4B has sufficient nominal capability for the primitive. v3.6.0 failure was primarily assay/prompt brittleness, not inability to perform state→outcome propagation.

### Outcome B
Removing UNKNOWN helps, but minimal primitive still fails.

Interpretation:

> fallback interference was real but insufficient to explain instability.

Use stronger-model diagnostic if available.

### Outcome C
Stage C fails on 4B but the same prompts pass on a stronger model.

Interpretation:

> model robustness/capability is a major limiting factor for this assay family.

### Outcome D
Stage C fails similarly on both 4B and stronger model.

Interpretation:

> likely surface-form/task-construction issue rather than merely model size.

---

## 18. What happens after validation

If and only if:

```text
MINIMAL_ASSAY_VALIDATED
```

the next experiment may add **one** complexity dimension at a time:

1. irrelevant context,
2. an entity layer A,
3. full A→B→C multi-hop dependence,
4. only then verified-state contamination / SHAR.

Do not jump directly from v3.6.1 to a SHAR claim.

The purpose of v3.6.1 is to establish the smallest trustworthy state-propagation primitive and to explain why v3.6.0 failed.
