# Experiment v3.1 Codex Specification
## Real-Entity Context Ladder for Error-Propagation Robustness

## 0. Purpose

Build directly on the successful v3 Track A synthetic assay.

v3 established that, under a minimal fixed context, Qwen3-4B can:

- retrieve explicitly provided downstream facts;
- use a supplied intermediate state reliably;
- follow either `B -> C` or `B' -> C'`;
- remain stable to evidence-order reversal.

The next experiment should test whether this controlled propagation behavior remains stable when the surrounding context becomes progressively more realistic and informative.

The main research question is:

> When an LLM is placed into an incorrect intermediate state `B'`, how does increasing and changing the surrounding context affect whether the model propagates that state to `C'`, overrides it back toward the gold trajectory `C`, or produces a different unsupported answer?

This experiment uses **real entities** and a **context ladder**.

Do not yet use natural model-generated trajectories.
Do not yet integrate SHAR/HalluSE.
Do not yet compare multiple model families.

---

# 1. Core causal structure

For each case define:

\[
A \xrightarrow{r_1} B \xrightarrow{r_2} C
\]

and a matched alternative state:

\[
B' \xrightarrow{r_2} C'
\]

The propagation contrast is always:

```text
same context H
same downstream relation
same downstream evidence
different supplied state:
B  vs  B'
```

For each context level `H_k`, compare:

\[
P(Y \mid B, H_k)
\]

with:

\[
P(Y \mid B', H_k)
\]

The experiment should measure how the effect of the state intervention changes as context grows.

---

# 2. Main experimental question

The primary quantity of interest is not a single propagation rate.

Instead estimate propagation as a function of context:

\[
PR(H_k) = P(C' \mid state=B', H_k)
\]

and compare:

\[
PR(H_0), PR(H_1), PR(H_2), PR(H_3)
\]

The experiment should also measure whether increasingly informative context causes:

```text
PROPAGATE
OVERRIDE_TO_GOLD
OUT_OF_CONTEXT_HALLUCINATION
UNKNOWN_REJECT
```

to change in frequency.

---

# 3. Case source

Use real cases derived from 2WikiMultiHopQA or the existing v2/v2.1 candidate-generation pipeline.

Do not use synthetic names in this experiment.

However, do not require the model to recall facts from parametric memory.

Every downstream fact needed to answer the state-conditioned question must be explicitly present in the reference context.

Use only cases satisfying all of the following:

1. explicit two-hop compositional structure;
2. single-valued first-hop target `B`;
3. single-valued downstream relation `r2`;
4. explicit evidence for `B -> C`;
5. matched donor/alternative entity `B'`;
6. explicit evidence for `B' -> C'`;
7. `C != C'`;
8. no unresolved aliases or answer-granularity ambiguity;
9. no multi-valued downstream relations;
10. the original first-hop evidence clearly identifies `B`.

Prefer:

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

---

# 4. Sample size

Use a fixed smoke set of:

```text
10 real-entity cases
```

Select them before generation.

Do not replace cases after observing outputs.

Save:

```text
data/candidates_v3_1.jsonl
```

with a manifest and hash.

If fewer than 10 clean cases can be constructed without ambiguity, stop and report the available number rather than weakening the criteria.

---

# 5. Context ladder

For every case construct four context levels.

The ladder should be cumulative where possible.

The same context level must be used for both the `B` and `B'` state branches.

## H0 — Minimal downstream context

Contains only the two downstream facts:

```text
Reference facts:
1. B <r2> C.
2. B' <r2> C'.
```

Example:

```text
Reference facts:
1. Helmut Käutner was born in Düsseldorf.
2. Gustaf Molander was born in Helsinki.
```

No original question.
No film/song title.
No first-hop evidence.
No unrelated evidence.

This is the real-entity analogue of v3 Track A.

---

## H1 — Original task framing added

Add the original multi-hop question or equivalent task framing, but do not include the first-hop answer.

Example:

```text
Original task:
Where was the director of "The Last Bridge" born?

Reference facts:
1. Helmut Käutner was born in Düsseldorf.
2. Gustaf Molander was born in Helsinki.
```

The goal is to test whether merely restoring the original task frame changes state-following.

Do not add evidence establishing who directed the film.

---

## H2 — Neutral accumulated context

Add context from the original example that is relevant to the topic but does not reveal or contradict the first-hop identity.

Examples may include:

- publication/film/song metadata;
- date or genre;
- non-answer-bearing surrounding sentences;
- other neutral supporting context.

Requirements:

- H2 must not explicitly identify `B`;
- H2 must not identify `B'`;
- H2 must not contain the downstream answer except in the controlled downstream facts;
- H2 must be identical across the `B` and `B'` branches.

The purpose is to introduce realistic context accumulation and distraction without direct contradiction.

---

## H3 — Gold first-hop evidence added

Add the original first-hop evidence that explicitly establishes:

\[
A \xrightarrow{r_1} B
\]

Example:

```text
Original task:
Where was the director of "The Last Bridge" born?

Additional evidence:
"The Last Bridge" was directed by Helmut Käutner.

Reference facts:
1. Helmut Käutner was born in Düsseldorf.
2. Gustaf Molander was born in Helsinki.
```

For the `state=B` branch, the context is consistent.

For the `state=B'` branch, the same context conflicts with the supplied state.

This level is intentionally designed to test whether the model:

- follows the externally supplied incorrect state;
- overrides it using conflicting evidence;
- becomes uncertain;
- produces another answer.

Do not label `B'` as false in the prompt.

---

# 6. State-conditioned prompt

For every context level, use the same downstream prompt form.

Example for birthplace:

```text
<context block>

Current Step 1 state:
Gustaf Molander

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the location.
```

Matched gold branch:

```text
<context block>

Current Step 1 state:
Helmut Käutner

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the location.
```

The only difference between paired prompts at the same context level must be the supplied state value.

Do not add:

```text
correct
incorrect
oracle
injected
false
hallucinated
```

to model-facing prompts.

---

# 7. Direct context-lookup controls

For every case and every context level, verify that the model can still retrieve the downstream facts directly.

Run:

```text
Question:
According to the information above, where was B born?
```

expected:

```text
C
```

and:

```text
Question:
According to the information above, where was B' born?
```

expected:

```text
C'
```

Use equivalent natural-language questions for other relation types.

These direct probes are required because a failure under a richer context may be caused by context interference before any state propagation is involved.

---

# 8. Core conditions

For each case and each context level run four independent calls:

```text
direct_B
direct_B_prime
state_B
state_B_prime
```

Each call must start from a fresh single-user prompt.

Do not carry any previous answer or KV cache across calls.

For 10 cases and 4 context levels:

```text
10 × 4 × 4 = 160 model calls
```

Use deterministic greedy decoding.

---

# 9. Output instruction

Keep output requirements minimal.

Use:

```text
Answer with only the requested name or location.
```

Do not use angle-bracket placeholders.

Do not require duplicated fields such as:

```text
Step 2:
Final answer:
```

The parsed response should be a single short entity/value.

---

# 10. Primary behavioral labels

For `state_B_prime`, classify the output as:

## PROPAGATE

Output is exactly `C'`.

Interpretation:

```text
The model follows the supplied alternative state through the downstream relation.
```

## OVERRIDE_TO_GOLD

Output is exactly `C`.

Interpretation:

```text
The model ignores or overrides the supplied B' state and returns the downstream value associated with the gold trajectory.
```

This is especially meaningful at H3.

## OUT_OF_CONTEXT_HALLUCINATION

Output is neither `C` nor `C'` and is unsupported by the provided context.

## UNKNOWN_REJECT

Explicit refusal, uncertainty, or inability to answer.

## INVALID_OUTPUT

Malformed or unparsable response.

For `state_B`, exact `C` is expected.

---

# 11. Metrics

Use the following metrics as the primary mechanism measures.

Do not add unnecessary metrics unless they diagnose a specific confound.

## 11.1 Context Lookup Accuracy — CLA

For each context level:

\[
CLA(H_k)
\]

is the proportion of direct lookup probes that return the explicit reference fact correctly.

Report separately for:

```text
B
B'
```

and combined.

Purpose:

```text
Does the richer context itself disrupt access to explicitly supplied facts?
```

---

## 11.2 Gold-State Adherence — GSA

For each context level:

\[
GSA(H_k) = P(output=C \mid state=B, H_k)
\]

Purpose:

```text
Can the model still correctly follow the gold intermediate state under this amount/type of context?
```

This is a control, not the main propagation result.

---

## 11.3 Propagation Rate — PR

For each context level:

\[
PR(H_k) = P(output=C' \mid state=B', H_k)
\]

This is the primary propagation metric.

Purpose:

```text
How often does the model continue from the supplied alternative/error state?
```

---

## 11.4 Override Rate — OR

For each context level:

\[
OR(H_k) = P(output=C \mid state=B', H_k)
\]

This is especially important at H3.

Purpose:

```text
How often does context cause the model to override B' and return to the gold trajectory?
```

---

## 11.5 State-Frame Interference Rate — SFIR

Count cases where:

```text
direct lookup is correct
but state-conditioned lookup is incorrect
```

for the same entity and context level.

Report separately for `B` and `B'`.

Purpose:

```text
Does the state representation itself interfere with otherwise available context knowledge?
```

---

## 11.6 Context Effect on Propagation — ΔPR

Use H0 as the calibrated reference:

\[
\Delta PR(H_k) = PR(H_k) - PR(H_0)
\]

Report:

```text
ΔPR(H1)
ΔPR(H2)
ΔPR(H3)
```

Purpose:

```text
How much does additional context change propagation relative to the minimal-context assay?
```

Do not reduce the entire result to one aggregate PR.

---

# 12. Secondary outcomes

Also report:

```text
OUT_OF_CONTEXT_HALLUCINATION rate
UNKNOWN_REJECT rate
INVALID_OUTPUT rate
```

per context level.

These are diagnostic outcomes, not primary metrics.

---

# 13. Key paired analyses

For each case, construct a row:

```text
case
H0 state_B'
H1 state_B'
H2 state_B'
H3 state_B'
```

This allows trajectory-style context sensitivity to be inspected within the same case.

Example:

```text
Case 07:
H0 -> PROPAGATE
H1 -> PROPAGATE
H2 -> PROPAGATE
H3 -> OVERRIDE_TO_GOLD
```

This pattern would suggest:

```text
the supplied error state remains effective under neutral context growth,
but explicit contradictory first-hop evidence triggers recovery.
```

Another possible pattern:

```text
H0 -> PROPAGATE
H1 -> OUT_OF_CONTEXT_HALLUCINATION
H2 -> OUT_OF_CONTEXT_HALLUCINATION
H3 -> OVERRIDE_TO_GOLD
```

would indicate stronger context sensitivity and less stable propagation.

---

# 14. Do not interpret H3 override as a failure of the assay

At H3, the context explicitly supports `B` while the supplied current state is `B'`.

Therefore:

```text
OVERRIDE_TO_GOLD
```

is a scientifically meaningful outcome.

It should not fail the experiment.

The experiment fails only if the context is too unstable to tell what happened.

For example:

- direct lookup collapses;
- output becomes mostly unsupported;
- state_B control also fails;
- prompts are malformed.

---

# 15. Smoke gate

The v3.1 smoke is valid if:

1. at H0, combined CLA >= 90%;
2. at H0, GSA >= 90%;
3. at least 8/10 cases are valid and interpretable across H0–H2;
4. direct lookup remains >= 80% at H1 and H2;
5. invalid-output rate <= 5%;
6. no systematic formatting/placeholder issue appears.

Do not require high PR at H3.

Do not require PR to remain constant across context levels.

Variation in PR is the object of study.

---

# 16. Stop conditions

## Stop Condition 1 — H0 regression

If real-entity H0 fails badly despite explicit downstream evidence, stop.

The real-entity assay is not yet calibrated.

## Stop Condition 2 — context lookup collapse

If CLA drops sharply before H3, stop and inspect the added context.

Do not interpret lower PR as a propagation effect if the model can no longer retrieve `C` or `C'` directly.

## Stop Condition 3 — gold-state collapse

If GSA falls substantially under H1/H2, the richer context is disrupting basic task execution.

Do not attribute state_B' failures specifically to error propagation.

## Stop Condition 4 — excessive unsupported answers

If H1/H2 produce many out-of-context values, inspect context construction for ambiguity or unintended cues.

## Stop Condition 5 — no silent case replacement

Do not replace difficult real cases after viewing outputs.

Report them.

---

# 17. Evidence construction audit

Before any inference, generate:

```text
results/smoke_v3_1/context_audit.md
```

For every case show:

```text
A
r1
B
r2
C
B'
C'
H0
H1
H2
H3
```

Human-readable checks must verify:

- H0 contains only the two downstream facts;
- H1 adds task framing only;
- H2 adds no first-hop answer;
- H2 contains no `C`/`C'` leakage outside the controlled facts;
- H3 explicitly establishes `B`;
- all four context blocks are identical between the paired `state_B` and `state_B'` calls.

Do not run the model until this audit file has been generated.

---

# 18. Output artifacts

Create:

```text
results/smoke_v3_1/
```

Required files:

```text
context_audit.md
trajectories.jsonl
inspection.md
diagnosis.md
metrics.json
summary.csv
gate.json
manifest.json
```

Every trajectory record should include:

```json
{
  "case_id": "...",
  "context_level": "H0|H1|H2|H3",
  "condition": "direct_B|direct_B_prime|state_B|state_B_prime",
  "relation": "...",
  "B": "...",
  "C": "...",
  "B_prime": "...",
  "C_prime": "...",
  "prompt": "...",
  "raw_generation": "...",
  "parsed_answer": "...",
  "expected_answer": "...",
  "label": "...",
  "direct_lookup_pass": true,
  "state_adherence_pass": true
}
```

---

# 19. inspection.md

The inspection should make within-case context changes easy to read.

For each case show a compact table:

| Context | CLA B | CLA B' | state B | state B' | injected label |
|---|---|---|---|---|---|
| H0 | ... | ... | ... | ... | ... |
| H1 | ... | ... | ... | ... | ... |
| H2 | ... | ... | ... | ... | ... |
| H3 | ... | ... | ... | ... | ... |

Then include the exact prompts and raw responses below.

Highlight:

```text
PROPAGATE -> OVERRIDE_TO_GOLD
PROPAGATE -> OUT_OF_CONTEXT_HALLUCINATION
direct-correct -> state-wrong
gold-state failure
```

when these transitions occur.

---

# 20. diagnosis.md

Summarize:

1. whether H0 replicates the v3 synthetic calibration on real entities;
2. whether H1 changes propagation merely by restoring the original task frame;
3. whether H2 neutral context accumulation changes PR or GSA;
4. whether H3 contradictory first-hop evidence shifts outcomes from PROPAGATE toward OVERRIDE_TO_GOLD;
5. whether any observed PR change can be separated from simple context lookup failure;
6. whether the state frame itself becomes unstable at richer context levels.

Do not make claims about spontaneous hallucination.

---

# 21. Interpretation scope

If the experiment works, it can support a statement of the form:

> Under explicit downstream evidence, propagation from a supplied alternative intermediate state is stable under some contexts but changes systematically when the surrounding context becomes more informative or contradictory.

It cannot yet establish:

> Naturally generated hallucinations propagate at the same rate.

That requires the next experiment using natural trajectory branching.

---

# 22. Next step after v3.1

Do not automatically proceed.

If v3.1 is interpretable, the next experiment should use:

```text
natural multi-hop generation
-> checkpoint prefix
-> branch from the same prefix
-> correct B versus naturally wrong or injected B'
-> continue generation
```

That experiment should reuse the best-performing context representation identified here.

SHAR/HalluSE should still remain outside the experiment until the propagation measurement is stable under realistic context growth.
