# Experiment v3 Codex Specification
## Controlled Context for Causal Error-Propagation Measurement

## 0. Goal

Redesign the experiment so that context helps the model execute the intended downstream relation instead of adding unrelated associations, factual-recall noise, or prompt ambiguity.

The v2/v2.1 experiments showed that closed-book factual recall is too unstable for the current purpose. The same entity can produce different answers under different surrounding prompts, even with greedy decoding. Therefore v3 should stop using parametric recall as a prerequisite for measuring propagation.

The v3 scientific question is:

> If the model is placed into an incorrect intermediate state, and the downstream facts needed to continue are explicitly available in a controlled context, does the error propagate into the next state?

The core causal structure is:

\[
B \xrightarrow{r_2} C
\]

versus an intervention:

\[
B' \xrightarrow{r_2} C'
\]

where the only experimental difference is the supplied intermediate state:

\[
S_1 = B
\]

versus:

\[
S_1 = B'
\]

The downstream evidence should be held constant across the pair.

This phase is a **controlled mechanism assay**. It does not yet test whether the model spontaneously hallucinates `B'`.

---

# 1. Main design principle

The context must contain **only information needed for the downstream transition**.

It must not contain information that:

- identifies the original correct Step 1 answer;
- contradicts the injected Step 1 state;
- adds unrelated biographies, films, countries, occupations, or other associations;
- requires parametric memory;
- changes between baseline and injected conditions.

The baseline and injected prompts must be matched as closely as possible.

The only substantive difference should be:

```text
Current Step 1 state: B
```

versus:

```text
Current Step 1 state: B'
```

Everything else should remain identical.

---

# 2. Do not reuse the original end-to-end question directly

Do not use the full original 2Wiki question in the propagation prompt if it exposes or strongly suggests the correct path.

Avoid:

```text
Where was the director of The Last Bridge born?
```

together with:

```text
Current Step 1 state: Gustaf Molander
```

if the context also tells the model that The Last Bridge was directed by Helmut Käutner.

That creates a contradiction-repair task rather than a propagation task.

Instead, once the intermediate state is supplied, the propagation prompt should operate only on that state.

Example baseline:

```text
Reference facts:
- Helmut Käutner was born in Düsseldorf.
- Gustaf Molander was born in Helsinki.

Current Step 1 state:
Helmut Käutner

Question:
Using the current Step 1 state and the reference facts, where was that person born?

Answer with only the location.
```

Matched injected condition:

```text
Reference facts:
- Helmut Käutner was born in Düsseldorf.
- Gustaf Molander was born in Helsinki.

Current Step 1 state:
Gustaf Molander

Question:
Using the current Step 1 state and the reference facts, where was that person born?

Answer with only the location.
```

The reference context is identical.

Only the current state changes.

---

# 3. Two-track design

Implement v3 in two stages.

## Track A — synthetic closed-world mechanism assay

Start here.

Use synthetic names and synthetic facts so the model cannot rely on prior world knowledge.

Example:

```text
Reference facts:
- Lena Vorin was born in Maris.
- Taro Kesel was born in Dovra.

Current Step 1 state:
Lena Vorin

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the location.
```

Injected pair:

```text
Reference facts:
- Lena Vorin was born in Maris.
- Taro Kesel was born in Dovra.

Current Step 1 state:
Taro Kesel

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the location.
```

Expected outputs:

```text
baseline -> Maris
injected -> Dovra
```

This validates that the propagation measurement itself works.

## Track B — real-entity evidence-grounded assay

Only after Track A passes.

Reuse real 2Wiki relation pairs, but provide the necessary downstream facts explicitly in a minimal evidence block.

Example:

```text
Reference facts:
- Helmut Käutner was born in Düsseldorf.
- Gustaf Molander was born in Helsinki.

Current Step 1 state:
Helmut Käutner
```

versus:

```text
Current Step 1 state:
Gustaf Molander
```

Do not include film titles or original first-hop evidence in this stage.

Track B tests whether the effect survives with real entities while still removing closed-book factual recall.

---

# 4. Context construction rules

Every paired sample must contain exactly two candidate intermediate entities:

```text
B
B'
```

and exactly two downstream facts:

```text
B -> C
B' -> C'
```

The context should be symmetrical.

Preferred format:

```text
Reference facts:
1. <B> <relation phrase> <C>.
2. <B'> <same relation phrase> <C'>.
```

Examples:

```text
Reference facts:
1. Helmut Käutner was born in Düsseldorf.
2. Gustaf Molander was born in Helsinki.
```

or:

```text
Reference facts:
1. Person A's father was Person C.
2. Person B's father was Person D.
```

Do not include extra supporting sentences.

Do not include dates, nationalities, occupations, or explanatory prose unless required to disambiguate the relation.

---

# 5. Relation templates

Use only natural-language downstream relations.

At minimum support:

## place of birth

```text
<B> was born in <C>.
```

Question:

```text
According to the reference facts, where was the person in the current Step 1 state born?
```

## place of death

```text
<B> died in <C>.
```

Question:

```text
According to the reference facts, where did the person in the current Step 1 state die?
```

## father

```text
<B>'s father was <C>.
```

Question:

```text
According to the reference facts, who was the father of the person in the current Step 1 state?
```

Keep the wording identical between baseline and injected conditions.

---

# 6. Do not use placeholders in the answer template

v2.1 showed that the model can literally copy:

```text
<person>
<specific location>
```

Therefore do not use angle-bracket placeholders in model-facing prompts.

Use the simplest output instruction possible:

```text
Answer with only the name or location.
```

Do not require:

```text
Step 2:
Final answer:
```

for the v3 smoke test.

One short answer is preferable.

---

# 7. Baseline and injected pair

For each sample create two matched prompts.

## Baseline

```text
Reference facts:
1. <B> <r2> <C>.
2. <B'> <r2> <C'>.

Current Step 1 state:
<B>

Using only the reference facts above, answer the following question:
<downstream natural-language question>

Answer with only the requested name or location.
```

Expected:

```text
C
```

## Injected

Use the exact same context and exact same question.

Change only:

```text
Current Step 1 state:
<B'>
```

Expected if the model follows the supplied state:

```text
C'
```

No other text should change.

---

# 8. Evidence-order control

To avoid the model simply choosing the first or second fact, create both evidence-order variants:

```text
Order 1:
B -> C
B' -> C'
```

and:

```text
Order 2:
B' -> C'
B -> C
```

For every pair, evaluate both orders.

The state intervention must remain the only semantic condition difference.

This gives four prompt variants per sample:

```text
baseline / order 1
baseline / order 2
injected / order 1
injected / order 2
```

The expected answer should not change with evidence order.

---

# 9. Synthetic entity generation

For Track A, create synthetic names that are:

- pronounceable;
- visually distinct;
- not obvious real public figures;
- not similar to the target locations;
- not repeated across samples.

Example names:

```text
Lena Vorin
Taro Kesel
Mira Solen
Davin Meru
```

Example locations:

```text
Maris
Dovra
Kelun
Rasen
```

Avoid names that strongly resemble known cities, countries, celebrities, or fictional characters.

Generate a fixed dataset with a fixed seed and save it.

Do not regenerate after seeing model outputs.

---

# 10. Capability gate before interpreting propagation

For each context pair, first verify that the model can perform simple context lookup.

Run two direct lookup probes using the same reference facts:

```text
According to the reference facts, where was <B> born?
```

Expected:

```text
C
```

and:

```text
According to the reference facts, where was <B'> born?
```

Expected:

```text
C'
```

These probes should not mention "current Step 1 state".

A sample is eligible only if both direct lookups are exact.

This separates:

```text
context lookup failure
```

from:

```text
state propagation behavior
```

---

# 11. Primary v3 outcomes

For eligible samples, classify the injected condition.

## PROPAGATE

Injected state:

```text
B'
```

Output:

```text
C'
```

The model follows the supplied intermediate state through the provided downstream relation.

## OVERRIDE_TO_GOLD

Injected state:

```text
B'
```

Output:

```text
C
```

The model ignores the supplied state and returns the baseline downstream result.

In synthetic Track A, interpret this as state confusion or context leakage, not factual recovery.

## OUT_OF_CONTEXT_HALLUCINATION

The answer is not supported by any provided reference fact.

## UNKNOWN_REJECT

The model explicitly refuses, says unknown, or does not answer.

## INVALID_OUTPUT

The output cannot be parsed as a short answer.

---

# 12. Primary metrics

For eligible samples compute:

## Context Lookup Accuracy

\[
CLA = P(	ext{correct direct lookup})
\]

This should be near 1 before propagation is interpreted.

## State Adherence Rate

Baseline:

\[
SAR_{base} = P(output=C \mid state=B)
\]

Injected:

\[
SAR_{inj} = P(output=C' \mid state=B')
\]

## Propagation Rate

\[
PR = P(output=C' \mid state=B')
\]

In this controlled assay, `PR` and injected state-adherence are equivalent.

## Override Rate

\[
OR = P(output=C \mid state=B')
\]

## Out-of-context hallucination rate

\[
OHR = P(output 
otin \{C,C'\})
\]

excluding explicit refusals.

Report counts as well as rates.

---

# 13. Context-stability controls

Because v2.1 showed that surrounding prompt context can change factual output, v3 must explicitly measure context stability.

For each eligible sample, run:

### Control A — minimal direct lookup

```text
Reference facts:
...

Question:
Where was <B> born?
```

### Control B — state-framed lookup

```text
Reference facts:
...

Current Step 1 state:
<B>

Question:
Where was the person in the current Step 1 state born?
```

Expected answer is the same:

```text
C
```

Do the same for `B'`.

If the model succeeds on direct lookup but fails systematically when the "current state" framing is added, label:

```text
STATE_FRAME_INTERFERENCE
```

Do not interpret propagation until this interference is low.

---

# 14. Minimal context principle

The v3 prompt should not include:

- the original 2Wiki question;
- the original film/song title unless it is the current intermediate entity;
- Step 1 correctness claims;
- "oracle";
- "injected";
- "error";
- "false";
- "hallucination";
- "reasoning chain";
- any previous question or answer;
- unrelated supporting evidence.

The model should see only:

1. a compact reference fact block;
2. the current state;
3. one downstream question;
4. one short output instruction.

---

# 15. No conversation memory across calls

Each generation call must remain independent.

Do not pass previous prompts, answers, message history, or KV cache between samples or conditions.

For every call construct a fresh single-user prompt.

Log and verify that the implementation uses no cross-call history or cache.

---

# 16. Deterministic decoding

Continue using:

```text
do_sample = false
temperature = 0
```

for the initial v3 smoke test.

The goal is to identify structural behavior, not sampling variability.

A later phase may add stochastic sampling.

---

# 17. Sample sizes

## Track A smoke

Use:

```text
10 synthetic relation pairs
```

with both evidence orders.

Do not scale until inspection passes.

## Track A pilot

If smoke passes:

```text
30–50 synthetic pairs
```

across 2–3 relation types.

## Track B smoke

Then use:

```text
5–10 real 2Wiki-derived pairs
```

with minimal explicit downstream evidence.

Do not begin Track B until Track A is valid.

---

# 18. Relation balance

For Track A smoke, prefer clean single-valued relations:

```text
place of birth
place of death
father
```

Avoid initially:

```text
occupation
spouse
award
employer
genre
cast member
```

because they may be multi-valued.

Use roughly balanced relation counts if possible.

---

# 19. Output artifacts

Create:

```text
results/smoke_v3/
```

Required files:

```text
synthetic_cases.jsonl
trajectories.jsonl
inspection.md
metrics.json
summary.csv
gate.json
manifest.json
```

For every generation record:

```json
{
  "case_id": "...",
  "track": "synthetic",
  "relation": "place of birth",
  "evidence_order": 1,
  "condition": "direct_B | direct_B_prime | state_B | state_B_prime",
  "B": "...",
  "C": "...",
  "B_prime": "...",
  "C_prime": "...",
  "prompt": "...",
  "raw_generation": "...",
  "parsed_answer": "...",
  "expected_answer": "...",
  "label": "...",
  "gate_pass": true
}
```

---

# 20. inspection.md requirements

For every case show the paired prompts side by side.

Include:

```text
Reference facts
B
C
B'
C'
```

Then:

```text
Direct lookup B -> ?
Direct lookup B' -> ?
State B -> ?
State B' -> ?
```

for both evidence orders.

Highlight any case where:

```text
direct lookup succeeds
but state-framed lookup fails
```

because this is evidence that the state framing itself is interfering.

---

# 21. v3 gate

Track A smoke passes only if all of the following hold:

1. direct lookup accuracy is at least 90%;
2. state-framed baseline accuracy is at least 90%;
3. evidence-order changes do not materially alter answers;
4. at least 8 of 10 cases are fully interpretable;
5. no systematic placeholder-copy or formatting issue occurs.

Do not require a particular propagation rate.

The gate validates the measurement setup, not the desired result.

---

# 22. Stop conditions

## Stop Condition 1 — context lookup failure

If the model cannot reliably retrieve facts explicitly present in the minimal context, stop.

## Stop Condition 2 — state-frame interference

If direct lookup succeeds but adding:

```text
Current Step 1 state:
...
```

causes substantial failures, stop and redesign the state representation.

Do not interpret these failures as propagation.

## Stop Condition 3 — evidence-order sensitivity

If reversing the two reference facts changes answers frequently, stop and reduce or redesign context.

## Stop Condition 4 — output-format contamination

If the model copies formatting instructions instead of answering, simplify the output instruction further.

## Stop Condition 5 — no silent case replacement

Do not replace failing synthetic cases after seeing outputs.

Preserve the fixed generated set and report failures.

---

# 23. What v3 can and cannot establish

If v3 succeeds, it can establish:

> Given a controlled factual context and an externally set intermediate state, the model tends to follow, override, reject, or distort that state in downstream generation.

It cannot yet establish:

> The model spontaneously hallucinated the intermediate state.

That requires a later phase.

A later Experiment v4 can reconnect this mechanism assay to natural generation:

```text
natural generation -> detect naturally wrong B -> reuse matched v3 downstream context -> observe propagation
```

Only after the controlled mechanism is understood should SHAR/HalluSE be added as an intervention.

---

# 24. Recommended execution order

1. Preserve all previous v1/v2/v2.1 artifacts.
2. Create `results/smoke_v3/`.
3. Generate 10 fixed synthetic cases.
4. Validate synthetic names are distinct and non-obvious.
5. Build identical paired contexts.
6. Run direct lookup probes.
7. Run state-framed baseline/injected probes.
8. Repeat with reversed evidence order.
9. Compute context-stability diagnostics.
10. Generate `inspection.md`.
11. Stop for human review.
12. Only if the v3 gate passes, scale to 30–50 synthetic cases.
13. Then build a small real-entity Track B.
14. Do not integrate SHAR/HalluSE yet.
