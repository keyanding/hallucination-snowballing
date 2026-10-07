# v3.6.2 — Context Accumulation Robustness

## 0. Purpose

v3.6.1 validated a minimal symbolic state-propagation primitive:

\[
B \rightarrow C,\qquad B' \rightarrow C'
\]

with:

- C0: 40/40 correct,
- W0: 40/40 correct,
- paired switch: 40/40,
- unmapped fallback: 10/10,
- record-order diagnostic: 20/20.

Phase I now adds **one and only one complexity dimension**:

> irrelevant context accumulation.

The goal is to determine whether the validated state→outcome primitive remains reliable as unrelated context grows.

This version does **not** add:

- an A→B upstream reasoning layer,
- natural hallucinations,
- SHAR/HalluSE,
- task-role framing,
- conflicting evidence,
- mechanistic interpretability.

---

# 1. Research question

## Primary question

> Does increasing irrelevant context reduce the reliability of a previously validated state-dependent mapping assay?

Formally:

\[
P(C \mid B, H_k)
\]

and

\[
P(C' \mid B', H_k)
\]

where \(H_k\) contains \(k\) irrelevant state→outcome records.

We are interested in whether adherence degrades as \(k\) increases.

---

# 2. Main hypothesis

Null-style operational expectation:

\[
P(\text{correct} \mid H_0)
\approx
P(\text{correct} \mid H_k)
\]

for moderate irrelevant context.

Potential failure pattern:

\[
P(\text{correct} \mid H_k)
<
P(\text{correct} \mid H_0)
\]

as context length / distractor count grows.

This experiment is descriptive and causal with respect to the controlled addition of irrelevant records, but it does not identify an internal mechanism.

---

# 3. Why this stage matters

Future SHAR / verified-text experiments will operate in a growing context, not an isolated two-record prompt.

Before adding multi-hop reasoning or SHAR, we need to know whether:

\[
B/B' \rightarrow C/C'
\]

remains stable when the model must select one relevant mapping among many irrelevant records.

If the primitive already becomes brittle under context accumulation, later failures cannot cleanly be attributed to hallucination propagation.

---

# 4. Core design

Use fresh synthetic cases only.

Each base case contains:

- one gold state \(B\),
- one wrong state \(B'\),
- one gold outcome \(C\),
- one wrong outcome \(C'\),
- a pool of irrelevant state→outcome mappings.

No entity layer.

No UNKNOWN instruction in mapped-state conditions.

No candidate-answer list.

---

# 5. Experimental conditions

Use 40 fresh base cases.

For every case, test both:

- C0: supplied state = \(B\)
- W0: supplied state = \(B'\)

Across four context sizes:

### K0 — no distractors

Only the two relevant mappings:

```text
STATE_A -> OUTCOME_X
STATE_B -> OUTCOME_Y
```

### K4 — 4 irrelevant mappings

Relevant pair + 4 distractor mappings.

### K12 — 12 irrelevant mappings

Relevant pair + 12 distractor mappings.

### K24 — 24 irrelevant mappings

Relevant pair + 24 distractor mappings.

Thus per case:

\[
2 \times 4 = 8
\]

primary mapped-state calls.

Total:

\[
40 \times 8 = 320
\]

calls.

---

# 6. Prompt template

```text
Synthetic mapping task.

Mappings:
{MAPPING_BLOCK}

Current state:
{SUPPLIED_STATE}

Return only the mapped outcome.
```

No other prose.

No entity.

No UNKNOWN rule.

No answer choices.

---

# 7. Distractor construction

## 7.1 Distractor requirements

Each irrelevant mapping must satisfy:

- unique state identifier,
- unique outcome identifier,
- no state/outcome reused elsewhere in the same case,
- no distractor outcome equals C or C′,
- no distractor state equals B or B′,
- token-count and character-length constraints matched to the relevant identifiers as closely as possible.

## 7.2 Tokenization balancing

Before inference:

- audit all identifiers,
- ensure B and B′ have equal token counts,
- ensure C and C′ have equal token counts,
- ensure distractor identifiers come from the same lexical construction family.

Do not select identifiers based on model outputs.

## 7.3 Context nesting

K4 must be a subset of K12.

K12 must be a subset of K24.

Thus:

\[
H_4 \subset H_{12} \subset H_{24}
\]

This allows paired interpretation of degradation as context accumulates.

---

# 8. Record-position control

Context size and position must not be confounded.

For each base case and each K level:

- assign the two relevant mappings to positions using a frozen balanced schedule,
- ensure across cases that B/B′ appear approximately uniformly near:
  - beginning,
  - middle,
  - end.

Do not always place relevant mappings first.

Do not always place them last.

Save exact mapping positions.

---

# 9. Primary conditions

For each case and each K:

### C0(K)

Supplied state = B.

Expected output = C.

### W0(K)

Supplied state = B′.

Expected output = C′.

Literal C0/W0 prompt diff within the same K must be only the supplied state identifier.

---

# 10. Secondary position diagnostic

To separate context-size degradation from position effects, pre-register 12 seeded cases.

For each of those 12 cases at K24:

- render one version with relevant pair near the beginning,
- one near the middle,
- one near the end.

Run both C0 and W0.

Total secondary calls:

\[
12 \times 3 \times 2 = 72
\]

These are not used to alter the main gate.

They diagnose whether any K24 failure is actually driven by record position.

---

# 11. Parsing

Accepted mapped outputs:

- exact expected outcome,
- exact paired alternative outcome,
- `UNKNOWN`,
- `OTHER`,
- `INVALID`.

Normalization only:

- Unicode NFC,
- strip outer whitespace,
- remove one final period.

No extraction from explanatory text.

---

# 12. Main metrics

For each K separately:

## Gold-state adherence

\[
A_C(K)=P(C\mid B,H_K)
\]

## Wrong-state adherence

\[
A_W(K)=P(C'\mid B',H_K)
\]

## Paired state-following rate

\[
S(K)=P(Y_B=C,\;Y_{B'}=C')
\]

## False UNKNOWN

\[
U(K)=P(UNKNOWN\mid \text{mapped state},H_K)
\]

## Off-target rate

\[
O(K)=P(OTHER\lor INVALID)
\]

---

# 13. Context degradation metrics

Define paired degradation relative to K0.

### Gold degradation

\[
\Delta_C(K)=A_C(K)-A_C(0)
\]

### Wrong-state degradation

\[
\Delta_W(K)=A_W(K)-A_W(0)
\]

### Paired degradation

\[
\Delta_S(K)=S(K)-S(0)
\]

Also report case-level transition counts:

- correct at K0 → wrong/unknown at K4,
- correct at K0 → wrong/unknown at K12,
- correct at K0 → wrong/unknown at K24.

Do not average C0 and W0 together without also reporting them separately.

---

# 14. Pre-inference validity checks

Before model calls:

1. all 40 case definitions frozen,
2. all K0/K4/K12/K24 prompts frozen,
3. nested distractor sets verified,
4. C0/W0 literal diff verified,
5. tokenization audit passed,
6. relevant mapping positions balanced,
7. no answer-list syntax,
8. no UNKNOWN instruction in mapped-state prompts,
9. no identifier overlap across roles within a case,
10. no model-output-based case selection.

If any structural audit fails:

```text
INFRASTRUCTURE_FAILURE
```

Do not run inference.

---

# 15. Stage gate

The goal is not to require perfect performance at every K.

Instead, classify robustness.

## ROBUST_CONTEXT_ASSAY

All of:

- K0: C0 ≥39/40
- K0: W0 ≥39/40
- K24: C0 ≥38/40
- K24: W0 ≥38/40
- K24 paired S ≥37/40
- OTHER+INVALID across all 320 calls ≤2

and no monotonic collapse pattern.

## CONTEXT_SENSITIVE_ASSAY

K0 remains valid, but one or more of:

- K24 C0 <38/40
- K24 W0 <38/40
- K24 S <37/40
- at least 4 paired cases correct at K0 and fail at K24

while parser/infrastructure remains valid.

## BASE_ASSAY_REGRESSION

If K0 itself falls below:

- C0 <39/40
- or W0 <39/40
- or paired S <39/40

This means the supposedly validated primitive did not replicate cleanly on the fresh sample.

Stop interpretation of context accumulation.

---

# 16. Interpretation rules

## If ROBUST_CONTEXT_ASSAY

Licensed conclusion:

> The minimal state-propagation primitive remains highly reliable under up to 24 irrelevant state→outcome records in this synthetic setting.

Next Phase I stage may add an upstream A→B layer.

## If CONTEXT_SENSITIVE_ASSAY

Licensed conclusion:

> Increasing irrelevant context degrades the reliability of the minimal state-propagation primitive under this controlled synthetic setting.

Do not yet call this hallucination snowballing.

Next step should identify whether degradation is caused by:
- position,
- retrieval/selection burden,
- or other context-competition effects.

## If BASE_ASSAY_REGRESSION

Do not interpret context size.

Investigate replication / identifier-family issues first.

---

# 17. Statistical reporting

Primary unit: 40 paired base cases.

For each K report:

- raw counts,
- Wilson 95% intervals for A_C, A_W, S,
- paired transitions,
- exact denominators.

For paired K0 vs K24 degradation:

- report exact discordant case counts,
- optionally McNemar exact test descriptively,
- do not overstate p-values from 40 cases.

The experiment is primarily an engineering robustness validation.

---

# 18. Required artifacts

Save under:

```text
results/v3_6_2/
```

Required files:

```text
README.md
spec.md
pre_registration.md
design_audit.pre_inference.md
design_audit.md
case_manifest.json
identifier_pool.json
identifier_tokenization_audit.json
prompt_plan.json
prompt_diff_audit.md
position_schedule.json
decoding_freeze.json
chat_template.txt
main_outputs.jsonl
parsed_outcomes.jsonl
metrics.json
position_diagnostic_outputs.jsonl
position_diagnostic_metrics.json
gate.json
diagnosis.md
inspection.md
CHANGELOG.md
```

---

# 19. Design audit table

Before inference, include:

| Design intention | Feature | Observable check | Failure meaning |
|---|---|---|---|
| Preserve validated primitive | same minimal template | K0 replication | base assay regression |
| Add only one complexity dimension | distractor count only | K0/K4/K12/K24 diff audit | confounded intervention |
| Avoid world knowledge | opaque synthetic IDs | manifest audit | parametric shortcut |
| Avoid fallback interference | no UNKNOWN rule in mapped prompts | prompt audit | prior brittleness reintroduced |
| Avoid answer-list primacy | free exact output | prompt audit | candidate artifact |
| Separate size from position | balanced positions + K24 diagnostic | position metrics | context-size confound |
| Control tokenization | matched lexical family | tokenizer audit | surface-form asymmetry |
| Preserve paired causality | C0/W0 differ only by state | literal diff hashes | causal contrast contaminated |
| Avoid adaptive tuning | frozen cases/thresholds | hashes | post-hoc overfit |
| Preserve claim boundary | Phase I robustness only | diagnosis | no snowballing/SHAR claim |

---

# 20. Example

## K0

```text
Synthetic mapping task.

Mappings:
STATE_K4 -> OUTCOME_Q2
STATE_M9 -> OUTCOME_Z6

Current state:
STATE_K4

Return only the mapped outcome.
```

Expected:

```text
OUTCOME_Q2
```

## K4

```text
Synthetic mapping task.

Mappings:
STATE_A1 -> OUTCOME_R7
STATE_K4 -> OUTCOME_Q2
STATE_P3 -> OUTCOME_L8
STATE_M9 -> OUTCOME_Z6
STATE_T5 -> OUTCOME_C4
STATE_H2 -> OUTCOME_N1

Current state:
STATE_K4

Return only the mapped outcome.
```

Expected:

```text
OUTCOME_Q2
```

The four distractors must be irrelevant.

---

# 21. What comes after v3.6.2

If:

```text
ROBUST_CONTEXT_ASSAY
```

then v3.6.3 should add the upstream relation:

\[
A \rightarrow B \rightarrow C
\]

while preserving the validated downstream mapping primitive.

If:

```text
CONTEXT_SENSITIVE_ASSAY
```

then do not add the upstream layer yet.

First isolate the failure mode:
- relevant-record position,
- distractor similarity,
- or context selection burden.

If:

```text
BASE_ASSAY_REGRESSION
```

return to the v3.6.1 primitive and replication logic.

---

# 22. Final decision labels

Exactly one:

```text
ROBUST_CONTEXT_ASSAY
CONTEXT_SENSITIVE_ASSAY
BASE_ASSAY_REGRESSION
INFRASTRUCTURE_FAILURE
```

No “mostly passed”.

---

# 23. Core discipline

This stage is successful even if irrelevant context breaks the assay.

The purpose is not to prove robustness.

The purpose is to identify the first point at which a previously validated state-propagation primitive stops being reliable.

That boundary is the foundation needed before studying multi-hop hallucination snowballing or SHAR verified-state contamination.


## User-approved decision amendment, frozen before inference

INFRASTRUCTURE_FAILURE is restricted to real structural/runtime/parser implementation faults: bad prompt/render/hash validation, missing calls, model exceptions or parser malfunction. Model-generated OTHER/INVALID is not by itself infrastructure failure.
Priority: INFRASTRUCTURE_FAILURE → BASE_ASSAY_REGRESSION → CONTEXT_SENSITIVE_ASSAY → ROBUST_CONTEXT_ASSAY.
If K0 C0<39/40, W0<39/40 or paired S<39/40, classify BASE_ASSAY_REGRESSION and stop context-size interpretation.
With valid K0, CONTEXT_SENSITIVE_ASSAY holds if any original sensitive criterion is met, or if monotonic collapse holds, or OTHER+INVALID>2/320 with healthy infrastructure/parser. Report off-target counts separately at each K.
Monotonic collapse means S(K0)≥S(K4)≥S(K12)≥S(K24), at least two strict decreases, and S(K0)−S(K24)≥4/40. Use exact integer paired-success counts.
All remaining structurally valid outcomes are ROBUST_CONTEXT_ASSAY. No post-inference threshold changes.
