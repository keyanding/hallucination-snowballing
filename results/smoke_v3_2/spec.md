# Experiment v3.2 Codex Specification
## Ablating Gold-Evidence Override in Context-Dependent Error Propagation

## 0. Purpose

v3.1 established three important empirical facts on the fixed real-entity smoke set:

1. Minimal explicit downstream context supports stable state following.
2. Restoring the original multi-hop task framing does not by itself disrupt propagation.
3. Adding explicit gold first-hop evidence sharply shifts many alternative-state trajectories from `PROPAGATE` to `OVERRIDE_TO_GOLD`.

However, v3.1 H3 changed several things at once:

- it introduced the gold entity `B` into a new sentence;
- it added an explicit first-hop relation `A -> B`;
- it increased prompt length;
- it increased lexical and semantic support for the gold trajectory;
- it created a direct inconsistency between the task evidence and the supplied current state `B'`.

v3.2 should isolate which of these ingredients is responsible for the H3 override effect.

The main research question is:

> When an LLM is placed in an alternative intermediate state `B'`, what specific contextual features cause downstream generation to stop following `B' -> C'` and instead return to the gold trajectory `B -> C`?

This experiment remains a controlled state-intervention study.

Do not yet use naturally generated erroneous states.
Do not yet integrate SHAR/HalluSE.
Do not yet add new model families.

---

# 1. Core structure

For each case:

\[
A \xrightarrow{r_1} B \xrightarrow{r_2} C
\]

and:

\[
B' \xrightarrow{r_2} C'
\]

The state intervention is:

```text
Current Step 1 state:
B'
```

The downstream question remains the same across all ablation conditions.

The experiment manipulates only the context surrounding this fixed `B'` state.

---

# 2. Fixed case set

Reuse the exact 10 real-entity cases from v3.1.

Do not resample.
Do not replace.
Do not alter aliases.
Do not alter downstream facts.

Use the existing frozen candidate file and record its hash.

The purpose is a within-case ablation of the v3.1 H3 effect.

---

# 3. Why only state_B_prime is primary here

v3.2 focuses on the mechanism underlying override of an alternative/error state.

Therefore the primary experimental branch is:

```text
state_B_prime
```

However, for every context condition also run:

```text
direct_B
direct_B_prime
state_B
```

as controls.

These controls ensure that an observed reduction in `PR` is not caused by:

- failure to retrieve `C'`;
- general prompt corruption;
- degradation of gold-state execution;
- malformed output.

---

# 4. Context conditions

Construct the following matched conditions for every case.

All conditions must preserve the same original task, same downstream facts, same downstream question, same answer instruction, and same `Current Step 1 state: B'`.

Only the added ablation sentence/block may differ.

## C0 — Baseline minimal real context

Equivalent to v3.1 H0.

```text
Reference facts:
1. B <r2> C.
2. B' <r2> C'.

Current Step 1 state:
B'
```

Purpose:

```text
calibrated propagation baseline
```

## C1 — Original task framing only

Equivalent to v3.1 H1.

Add the original multi-hop task.

Do not add first-hop evidence.

Purpose:

```text
confirm that task framing alone does not explain override
```

## C2 — Length-matched neutral control

Add a sentence of approximately the same token length as the original gold first-hop evidence, but with no entity/relation content relevant to `A`, `B`, `B'`, `C`, or `C'`.

Requirements:

- no mention of `A`, `B`, `B'`, `C`, `C'`;
- no geographic cue linked to either target;
- no relation wording such as "directed by" if `r1=director`;
- approximately length-matched to the gold-evidence sentence.

Purpose:

```text
control for added length and generic contextual load
```

## C3 — Gold-entity lexical cue only

Add a sentence containing `B` but not asserting the first-hop relation.

Example:

```text
Additional context:
Helmut Käutner was an important figure in European cinema.
```

Requirements:

- mention `B`;
- do not mention `A`;
- do not express `A -> B`;
- do not mention `C`;
- do not mention `B'` or `C'`;
- avoid relation words that imply the first-hop fact.

Purpose:

```text
test whether merely activating the gold entity is enough to induce override
```

## C4 — Gold first-hop evidence

Equivalent to v3.1 H3.

Add the explicit original first-hop evidence:

```text
A was directed by B.
```

or the exact relation-appropriate evidence.

Purpose:

```text
replicate the v3.1 override effect
```

## C5 — Alternative-state supportive first-hop evidence

Add a structurally matched statement supporting `B'` as the answer to the first hop.

Example:

```text
For this task, "The Last Bridge" was directed by Gustaf Molander.
```

This statement may be counterfactual relative to the real world.

Important:
- present it strictly as task context;
- keep wording parallel to C4;
- do not label it false or hypothetical in model-facing text.

Purpose:

```text
test whether first-hop relational evidence in general strengthens whichever state it supports
```

Expected if relational support drives state control:

```text
PR(C5) > PR(C4)
```

## C6 — Explicit conflict: gold and alternative first-hop evidence

Provide both:

```text
A -> B
A -> B'
```

in balanced wording and balanced order.

Run both:

```text
C6a: gold first
C6b: alternative first
```

Purpose:

```text
test how the model behaves when contextual evidence itself is inconsistent
```

Measure whether output follows:

- the supplied state;
- the gold fact;
- the most recent evidence;
- another rule.

---

# 5. Optional C7 — Gold relation without gold entity

Only include if construction is clean.

Add a sentence preserving first-hop relational structure but replacing `B` with an unrelated synthetic proper name.

Purpose:

```text
test whether relation/task structure alone, without activating B, causes override
```

If this condition risks introducing new ambiguity, omit it and document the omission.

---

# 6. Prompt matching

For each case, all state-conditioned prompts should share:

```text
Original task
Reference facts
Current Step 1 state
Downstream question
Answer instruction
```

The only intended change is the ablation context block.

Use:

```text
Answer with only the requested name or location.
```

Do not use placeholders.

Do not use words such as:

```text
correct
incorrect
false
hallucination
oracle
injected
repair
```

in model-facing prompts.

---

# 7. Primary outcomes

For `state_B_prime`, classify:

## PROPAGATE

Output = `C'`

## OVERRIDE_TO_GOLD

Output = `C`

## OUT_OF_CONTEXT_HALLUCINATION

Output is neither `C` nor `C'` and unsupported by context.

## UNKNOWN_REJECT

Explicit uncertainty/refusal/non-answer.

## INVALID_OUTPUT

Malformed or unparsable.

For `state_B`, exact `C` is expected.

---

# 8. Primary metrics

Use a small set of mechanism-relevant metrics.

## 8.1 Context Lookup Accuracy — CLA

Verify direct access to `C` and `C'` remains intact.

## 8.2 Gold-State Adherence — GSA

\[
GSA = P(C \mid state=B)
\]

## 8.3 Propagation Rate — PR

\[
PR = P(C' \mid state=B')
\]

Primary outcome.

## 8.4 Override Rate — OR

\[
OR = P(C \mid state=B')
\]

Primary complement to PR.

## 8.5 State-Frame Interference Rate — SFIR

Direct lookup correct but state-conditioned output incorrect.

Report separately for `B` and `B'`.

---

# 9. Primary contrasts

## Length effect

\[
PR(C2) - PR(C1)
\]

Question:

```text
Does merely adding comparable context length reduce propagation?
```

## Gold-entity activation effect

\[
PR(C3) - PR(C2)
\]

Question:

```text
Does mentioning B without first-hop evidence shift the model toward C?
```

## Gold relational-evidence effect

\[
PR(C4) - PR(C3)
\]

Question:

```text
Does explicitly asserting A -> B add override beyond merely mentioning B?
```

## Alternative supportive-evidence effect

\[
PR(C5) - PR(C4)
\]

Question:

```text
Does first-hop relational evidence strengthen the state that it supports?
```

## Conflict effect

Compare:

```text
C4
C5
C6a
C6b
```

Question:

```text
When the prompt contains inconsistent first-hop evidence, what controls downstream state selection?
```

---

# 10. Interpretation patterns

## Pattern A

```text
C2: PROPAGATE
C3: PROPAGATE
C4: OVERRIDE_TO_GOLD
```

Interpretation:

```text
override depends more on explicit first-hop relational evidence than on length or gold-entity activation alone
```

## Pattern B

```text
C2: PROPAGATE
C3: OVERRIDE_TO_GOLD
C4: OVERRIDE_TO_GOLD
```

Interpretation:

```text
lexical/semantic activation of B may already be sufficient to destabilize B'
```

## Pattern C

```text
C4: OVERRIDE_TO_GOLD
C5: PROPAGATE
```

Interpretation:

```text
the model tends to follow contextual first-hop evidence rather than privileging the real-world gold trajectory specifically
```

## Pattern D

```text
C6a != C6b
```

Interpretation:

```text
evidence ordering/recency may control conflict resolution
```

---

# 11. Sample size and call count

Use the same 10 cases.

Minimum required conditions:

```text
C0
C1
C2
C3
C4
C5
C6a
C6b
```

For each condition run:

```text
direct_B
direct_B_prime
state_B
state_B_prime
```

Total:

```text
10 × 8 × 4 = 320 calls
```

Do not scale beyond the fixed ten cases before review.

---

# 12. Decoding

Use the same model and adapter as v3/v3.1:

```text
Qwen3-4B-Instruct-2507
4-bit NF4
BF16 compute
```

Use:

```text
do_sample = false
temperature = 0
```

Preserve independent fresh calls with no cross-call conversation history and no KV-cache reuse.

---

# 13. Pre-inference audit

Before model execution create:

```text
results/smoke_v3_2/context_ablation_audit.md
```

For every case and condition show:

```text
A
B
C
B'
C'
condition
added_context
full_prompt_without_answer
```

Human-readable checks must verify:

- C2 contains no relevant entity/relation leakage;
- C3 mentions B but does not establish `A -> B`;
- C4 exactly establishes `A -> B`;
- C5 supports `A -> B'` in matched wording;
- C6 contains both claims;
- all downstream facts remain unchanged.

Do not run inference if the audit detects contamination.

---

# 14. Output artifacts

Create:

```text
results/smoke_v3_2/
```

Required:

```text
context_ablation_audit.md
trajectories.jsonl
inspection.md
diagnosis.md
metrics.json
summary.csv
gate.json
manifest.json
```

---

# 15. inspection.md

For each case provide one compact table:

| Condition | CLA B | CLA B' | state B | state B' | label |
|---|---|---|---|---|---|
| C0 | ... | ... | ... | ... | ... |
| C1 | ... | ... | ... | ... | ... |
| C2 | ... | ... | ... | ... | ... |
| C3 | ... | ... | ... | ... | ... |
| C4 | ... | ... | ... | ... | ... |
| C5 | ... | ... | ... | ... | ... |
| C6a | ... | ... | ... | ... | ... |
| C6b | ... | ... | ... | ... | ... |

Then include exact prompts and raw responses.

Highlight:

```text
PROPAGATE -> OVERRIDE_TO_GOLD
OVERRIDE_TO_GOLD -> PROPAGATE
order-sensitive conflict resolution
direct-correct -> state-wrong
```

---

# 16. diagnosis.md

Answer explicitly:

1. Does length-matched neutral context reduce PR?
2. Does mentioning B without relation evidence reduce PR?
3. Does explicit `A -> B` evidence reduce PR beyond lexical activation?
4. Does matched `A -> B'` evidence restore/increase PR?
5. Under direct evidence conflict, is behavior state-following, gold-following, order-sensitive, or unstable?
6. Are changes separable from direct lookup failure?
7. Does gold-state adherence remain high across all conditions?

Do not infer internal reasoning processes beyond observed behavior.

Use language such as:

```text
consistent with
suggests
behaviorally prioritizes
```

rather than:

```text
the model realizes
the model knows it is wrong
the model repairs its belief
```

---

# 17. Gate

The measurement remains valid if:

1. combined CLA >= 90% in every condition;
2. GSA >= 90% in every condition;
3. invalid-output rate <= 5%;
4. no systematic out-of-context collapse occurs;
5. at least 8/10 cases remain interpretable across C0–C5.

Do not require a particular PR or OR.

Variation in PR/OR is the scientific result.

C6 may legitimately be unstable because it is intentionally contradictory.

---

# 18. Stop conditions

Stop and inspect if:

- CLA falls below threshold;
- GSA collapses in multiple conditions;
- C2 unexpectedly contains target-relevant semantic cues;
- C3 accidentally asserts the first-hop relation;
- C5 wording is not structurally matched to C4;
- C6 order effects cannot be disentangled from formatting differences;
- outputs become dominated by unsupported answers.

Do not silently edit prompts after viewing results.

---

# 19. What v3.2 can establish

If successful, v3.2 can identify which contextual ingredients most strongly alter downstream propagation from a supplied alternative state.

It may support conclusions such as:

> Explicit first-hop relational evidence, rather than added context length or mere mention of the gold entity, is what most strongly shifts the model from propagation toward override.

or:

> Gold-entity activation alone is sufficient to destabilize alternative-state propagation.

or:

> The model follows whichever first-hop relation receives stronger or more recent contextual support.

These are controlled behavioral findings.

v3.2 still cannot establish natural hallucination propagation.

---

# 20. How this connects to the final research question

The overall research question is:

> When an LLM enters an incorrect intermediate state during multi-step generation, under what conditions does that error propagate, get corrected, or transform into a different error?

v3 established that the downstream state transition can be measured cleanly.

v3.1 established that propagation is context-dependent.

v3.2 isolates which contextual features cause that dependence.

Only after this ablation is understood should the project move to natural trajectory branching:

```text
natural multi-hop generation
-> capture a real prefix
-> identify correct or incorrect intermediate state
-> fork from the same prefix
-> manipulate only the intermediate state or evidence
-> compare downstream trajectories
```

That next stage reconnects the controlled mechanism to naturally occurring hallucinations.

SHAR/HalluSE should be introduced only after the natural propagation mechanism is measurable.
