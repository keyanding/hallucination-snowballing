# v3.6.0 — Propagation Assay Validation

## 0. Purpose

This experiment starts **Phase I: Establish the phenomenon**.

Its sole goal is to validate a clean assay for causal error propagation:

\[
B \rightarrow C
\qquad\text{vs.}\qquad
B' \rightarrow C'
\]

where:
- \(B\) = correct intermediate state,
- \(B'\) = counterfactual wrong intermediate state,
- \(C\) = downstream answer implied by \(B\),
- \(C'\) = downstream answer implied by \(B'\).

This version does **not** test SHAR, HalluSE, task-role framing, natural first-hop hallucinations, or internal mechanisms.

The experiment should stop unless the assay itself is demonstrably valid.

---

## 1. Primary research question

> If the model is given an otherwise identical prompt but the supplied intermediate state is changed from \(B\) to \(B'\), does the downstream output causally change from \(C\) to \(C'\)?

Operationally:

\[
\Delta_{state}=P(C'\mid do(B'))-P(C'\mid do(B))
\]

A valid assay must have:
1. high correctness under \(B\),
2. high downstream following under \(B'\),
3. low ambiguity / invalid output,
4. no world-knowledge shortcut,
5. no candidate-position artifact,
6. no leakage of \(C\) or \(C'\) through labels.

---

## 2. Claim boundary

Even if all gates pass, this experiment does **not** establish:
- spontaneous hallucination incidence,
- natural end-to-end hallucination snowballing,
- an internal computational mechanism,
- SHAR failure or success,
- generalization to arbitrary real-world tasks.

A successful result licenses only:

> Under a validated synthetic state-dependent task, externally changing the intermediate state causes a predictable change in the downstream answer.

---

## 3. Core design principles

### 3.1 Synthetic opaque entities only

Do not use real people, real cities, real films, or facts likely present in pretraining.

Use opaque identifiers such as:
- `Entity_A17`
- `State_K04`
- `State_M91`
- `Outcome_Q22`
- `Outcome_Z63`

### 3.2 Explicit downstream mapping

Each case contains:

```text
State_K04 maps to Outcome_Q22.
State_M91 maps to Outcome_Z63.
```

### 3.3 No answer list

Never enumerate possible answers. Output is free-form but expected to be exactly one opaque outcome identifier.

### 3.4 Stateless calls

Every condition is a fresh independent model call.

---

## 4. Dataset

Use:
- **20 calibration cases**
- **40 frozen main cases**

Calibration and main sets must have disjoint opaque identifiers.

Example case:

```json
{
  "case_id": "v360-main-001",
  "entity": "Entity_A17",
  "gold_state": "State_K04",
  "wrong_state": "State_M91",
  "gold_outcome": "Outcome_Q22",
  "wrong_outcome": "Outcome_Z63"
}
```

Constraints:
- all identifiers unique within a case,
- no obvious lexical overlap between gold/wrong outcome identifiers,
- identifier lengths approximately balanced,
- no reuse of an identical full state→outcome pair,
- gold/wrong designation balanced over templates.

---

## 5. Primary prompt

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_K04 maps to Outcome_Q22.
State_M91 maps to Outcome_Z63.

Current entity:
Entity_A17

Working intermediate state:
{SUPPLIED_STATE}

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A17?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Only `{SUPPLIED_STATE}` changes between primary conditions.

### C0 — correct state

```text
Working intermediate state:
State_K04
```

Expected: `Outcome_Q22`

### W0 — wrong state

```text
Working intermediate state:
State_M91
```

Expected: `Outcome_Z63`

The literal C0/W0 prompt diff must be exactly the supplied state identifier.

---

## 6. Calibration controls

Run these on the 20 calibration cases only.

### 6.1 Mapping-only capability

Directly ask:

```text
According to the supplied mapping, what does State_K04 map to?
```

Also test the wrong state.

Purpose: verify pure lookup capability.

### 6.2 State-irrelevance control

Use an unmapped state:

```text
Working intermediate state:
State_X99
```

Expected: `UNKNOWN`.

Purpose: detect guessing or superficial position-following.

### 6.3 Mapping-swap control

Swap outcomes:

```text
State_K04 maps to Outcome_Z63.
State_M91 maps to Outcome_Q22.
```

With `State_K04` supplied, expected output is `Outcome_Z63`.

Purpose: verify use of mapping content rather than fixed role labels.

### 6.4 Record-order control

Reverse the two mapping lines.

Expected output must remain unchanged.

Purpose: exclude strong first-record artifacts.

### 6.5 Entity-label control

Replace `Entity_A17` with a fresh opaque entity while keeping state and mappings unchanged.

Expected output must remain unchanged.

Purpose: verify the downstream answer is mediated by the supplied state, not entity identity.

---

## 7. Calibration execution

Per calibration case run:
- C0
- W0
- gold mapping lookup
- wrong mapping lookup
- mapping swap
- record-order reversal
- state-irrelevance control
- entity-label control

Total:

\[
20\times 8 = 160
\]

calls.

### Calibration pass criteria

A. Mapping capability: at least **38/40** correct.

B. Correct-state adherence: at least **19/20** C0 outputs \(C\).

C. Wrong-state adherence: at least **19/20** W0 outputs \(C'\).

D. Mapping-swap sensitivity: at least **19/20** follow swapped mapping.

E. Record-order robustness: at least **19/20** unchanged after reversal.

F. Unknown-state behavior: at least **18/20** return exactly `UNKNOWN`.

G. Parse validity: at least **99%** outputs are exactly one permitted identifier or `UNKNOWN`.

H. Entity-label robustness: at least **19/20** normalized outputs unchanged after replacing only the entity identifier.

If any A–H fails:

```text
STOP_ASSAY_INVALID
```

Do not:
- replace failed cases,
- lower thresholds,
- tune wording after seeing failures,
- proceed to main cases,
- interpret propagation.

A redesign requires a new version number.

---

## 8. Main experiment

Run only if calibration passes.

For each of 40 frozen main cases:
- C0
- W0

Total:

\[
40\times 2=80
\]

calls.

Randomization:
- frozen seed,
- globally shuffle calls,
- avoid pairing C0/W0 adjacently when possible,
- independent stateless calls,
- freeze model/tokenizer/chat template/decoding before inference.

Recommended decoding:
- same Qwen3-4B checkpoint and stack as prior experiments,
- temperature = 0,
- greedy decoding,
- enough max tokens for one identifier only.

This phase validates causal state-following, not stochastic uncertainty.

---

## 9. Outcome parser

Allowed outputs:
- `gold_outcome`
- `wrong_outcome`
- `UNKNOWN`

Other categories:
- `OTHER`
- `INVALID`

Normalization only:
- Unicode NFC
- strip outer whitespace
- remove one terminal period

Do not extract an identifier from explanatory text.

---

## 10. Primary metrics

### Correct-state adherence

\[
A_C=P(C\mid do(B))
\]

### Wrong-state adherence

\[
A_W=P(C'\mid do(B'))
\]

### Paired state-switch rate

\[
S=P(Y_B=C,\;Y_{B'}=C')
\]

### Wrong-output contrast

\[
\Delta_{state}=P(C'\mid do(B'))-P(C'\mid do(B))
\]

Report `OTHER`, `UNKNOWN`, and `INVALID` separately.

---

## 11. Main interpretation gate

The assay is validated only if all are true:

### G1
\[
A_C\ge0.95
\]
At least 38/40.

### G2
\[
A_W\ge0.95
\]
At least 38/40.

### G3
\[
S\ge0.90
\]
At least 36/40.

### G4
\[
P(C'\mid do(B))\le0.05
\]
At most 2/40.

### G5
`OTHER + INVALID <= 2/80`.

If any gate fails:

```text
STOP_MAIN_ASSAY_INVALID
```

Do not proceed to Phase II or SHAR testing.

If all pass:

```text
ASSAY_VALIDATED
```

---

## 12. Statistical reporting

Report:
- raw counts,
- exact denominators,
- exact binomial or Wilson 95% intervals for \(A_C\), \(A_W\), and \(S\),
- paired C0→W0 transition table,
- exact prompt hashes.

The statistical unit is the **40 paired base cases**, not 80 independent semantic populations.

---

## 13. Required artifacts

Save under:

```text
results/v3_6_0/
```

Required files:

```text
README.md
spec.md
pre_registration.md
design_audit.pre_inference.md
design_audit.md
case_manifest.json
calibration_cases.json
main_cases.json
prompt_plan.json
prompt_diff_audit.md
decoding_freeze.json
chat_template.txt
calibration_outputs.jsonl
main_outputs.jsonl
parsed_outcomes.jsonl
metrics.json
gate.json
inspection.md
CHANGELOG.md
```

---

## 14. Design audit

Before inference create:

| Design intention | Feature | Observable check | Failure meaning |
|---|---|---|---|
| Eliminate parametric knowledge | opaque synthetic identifiers | no real-world entities | world-knowledge shortcut remains |
| Make answer state-dependent | explicit B→C and B′→C′ mappings | C0/W0 pair | assay does not depend on state |
| Isolate state intervention | one-identifier prompt diff | exact diff audit | causal attribution contaminated |
| Verify mapping capability | direct mapping lookups | >=95% | task too hard / parser broken |
| Prevent option primacy | no candidate list | prompt audit | prior artifact reintroduced |
| Prevent record-order artifact | mapping reversal | >=95% invariant | presentation confound |
| Verify mapping use | mapping swap | >=95% follows swap | shortcut / role memorization |
| Detect absent state | unmapped-state test | >=90% UNKNOWN | guessing / forced completion |
| Avoid post-hoc rescue | frozen thresholds | machine-readable gate | adaptive overfitting |
| Preserve inference boundary | Phase I only | final diagnosis | no mechanism / SHAR claim |

Append a post-run table to `design_audit.md` without modifying the frozen pre-inference section.

---

## 15. Example

### C0

```text
This is a synthetic state-transition task. All identifiers are arbitrary and only the supplied context is valid.

Downstream mappings:
State_K04 maps to Outcome_Q22.
State_M91 maps to Outcome_Z63.

Current entity:
Entity_A17

Working intermediate state:
State_K04

Question:
Using the working intermediate state and the downstream mappings above, what is the outcome for Entity_A17?

Output only the outcome identifier.
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
```

Expected:

```text
Outcome_Q22
```

### W0

Same prompt except:

```text
Working intermediate state:
State_M91
```

Expected:

```text
Outcome_Z63
```

### Mapping swap

```text
Downstream mappings:
State_K04 maps to Outcome_Z63.
State_M91 maps to Outcome_Q22.

Working intermediate state:
State_K04
```

Expected:

```text
Outcome_Z63
```

### Unmapped state

```text
Working intermediate state:
State_X99
```

Expected:

```text
UNKNOWN
```

---

## 16. After PASS

If v3.6.0 passes, freeze it as the validated propagation assay.

Only then should later preregistered experiments add one variable at a time, for example:

1. natural \(B'\) vs injected \(B'\),
2. verified-state contamination,
3. SHAR/HalluSE acceptance of downstream \(C'\),
4. later, internal mechanism work.

Do not modify v3.6.0 to include these.

---

## 17. Final decision labels

Exactly one final recommendation:

```text
STOP_ASSAY_INVALID
STOP_MAIN_ASSAY_INVALID
ASSAY_VALIDATED
```

No softer substitute such as “mostly passed”.

---

## 18. Core discipline

The success criterion for v3.6.0 is **not an interesting effect**.

The success criterion is a trustworthy measurement instrument.

A result such as:

```text
C0: 40/40 -> C
W0: 40/40 -> C'
```

is a successful outcome because it establishes a clean causal assay.

Only after that should later experiments ask why errors propagate or whether SHAR prevents propagation.

## User amendments frozen before inference

Entity-label control is formal calibration, not auxiliary: 20 × 8 = 160 calls. A–H are mandatory; G ≥99% means at least 159/160. Main remains 40 × 2 = 80.

The exact UNKNOWN instruction above is included in every template, including direct lookups. F remains 18/20. No other thresholds or main design changed.
