# Experiment v2.1 Codex Specification
## Natural-Language Relation Prompts and Explicit Oracle Semantics

## 0. Purpose

Revise the current `hallucination-snowballing` Experiment v2 smoke test.

The current v2 framework is structurally cleaner than v1, but inspection shows that the prompt design still introduces avoidable confounds:

1. relations are expressed in unnatural operator-style language such as:

```text
Apply relation "place of birth" to "Helmut Käutner".
```

2. Oracle prompts provide the correct intermediate answer, but do not explicitly tell the model that this answer is **known to be correct, fixed, and should be used as the premise for the next step**;

3. location questions have answer-granularity ambiguity, especially city/town versus country;

4. exact-match evaluation currently treats broader-but-factually-compatible answers such as:

```text
Düsseldorf -> Germany
Reykjavík -> Iceland
```

the same as genuinely wrong answers.

Experiment v2.1 should fix these issues without changing the overall scientific design.

Do not integrate SHAR/HalluSE yet.

Do not scale beyond a small smoke test.

---

# 1. Existing repository and artifact preservation

Continue using the existing repository:

```text
hallucination-snowballing
```

Preserve all prior artifacts unchanged:

```text
results/smoke/
results/smoke_v2/
```

Create a new directory:

```text
results/smoke_v2_1/
```

Do not overwrite any existing run.

Continue using:

```text
Qwen/Qwen3-4B-Instruct-2507
```

with the existing local 4-bit NF4 adapter unless a runtime issue requires otherwise.

Do not modify the original SHAR repository.

---

# 2. Scientific objective

The scientific structure remains:

\[
A \xrightarrow{r_1} B \xrightarrow{r_2} C
\]

with an injected intermediate state:

\[
B'
\]

and a known corresponding downstream answer:

\[
B' \xrightarrow{r_2} C'
\]

The goal is still to determine what happens when the model is placed into an incorrect intermediate factual state.

However, v2.1 must remove prompt-language ambiguity before interpreting any model behavior mechanistically.

---

# 3. Replace operator-style prompts with natural-language relation templates

Do not use prompts like:

```text
Apply relation "father" to "Leopoldo Torre Nilsson".
```

or:

```text
Apply relation "place of birth" to "Helmut Käutner".
```

Instead, map each relation to a natural-language question template.

Implement a function conceptually like:

```python
render_relation_question(subject, relation, answer_granularity=None)
```

Use relation-specific templates.

At minimum support the relations currently present in the smoke set.

## composer

```text
Who composed "<entity>"?
```

Example:

```text
Who composed "Edavazhiyile Poocha Minda Poocha"?
```

## director

```text
Who directed "<entity>"?
```

Example:

```text
Who directed "The Last Bridge"?
```

## performer

```text
Who performed the song "<entity>"?
```

or if dataset semantics are closer to "artist":

```text
Who performed or recorded the song "<entity>"?
```

Use the template that best matches the dataset relation semantics.

## place of birth

Use:

```text
In which city or town was <person> born?
```

Do not use the vague phrase:

```text
What is the place of birth of <person>?
```

unless city/town granularity is unavailable.

## place of death

Use:

```text
In which city, town, or specific location did <person> die?
```

If the dataset answer is not a city/town but another specific geographic entity such as an island or region, phrase the question as:

```text
At what specific location did <person> die?
```

The generated prompt should reflect the granularity available in the dataset.

## father

Use:

```text
Who was <person>'s father?
```

Do not use:

```text
Apply relation "father" to <person>.
```

---

# 4. Baseline prompt redesign

The baseline condition should still require two explicit steps, but each step should be expressed as a natural-language question.

Example structure:

```text
Question:
Where was the director of the film "The Last Bridge" born?

Solve this in two steps.

Step 1 question:
Who directed "The Last Bridge"?

Step 2 question:
Using the person you identified in Step 1, in which city or town was that person born?

Answer using exactly this format:

Step 1: <person>
Step 2: <city or town>
Final answer: <same answer as Step 2>
```

For a father relation:

```text
Question:
Who is the father of the director of "La Caída"?

Solve this in two steps.

Step 1 question:
Who directed "La Caída"?

Step 2 question:
Using the person you identified in Step 1, who was that person's father?

Answer using exactly this format:

Step 1: <person>
Step 2: <person>
Final answer: <same answer as Step 2>
```

Important:

The prompt should describe the semantic task naturally.

Do not mention graph relations such as `r1`, `r2`, "apply relation", or knowledge-graph terminology in the model-facing prompt.

These may remain in metadata only.

---

# 5. Oracle prompt redesign

This is a critical change.

The Oracle condition must explicitly state that the supplied Step 1 result is:

- correct;
- already established;
- fixed;
- not to be verified or changed;
- the premise for answering Step 2.

Do not merely write:

```text
Step 1: Helmut Käutner
```

without explanation.

Use the following conceptual structure.

Example:

```text
Question:
Where was the director of the film "The Last Bridge" born?

We already know the correct answer to Step 1.

Confirmed Step 1 result:
The director of "The Last Bridge" is Helmut Käutner.

Treat this intermediate result as correct.
Do not verify it, replace it, or answer Step 1 again.

Now answer only the next question:

In which city or town was Helmut Käutner born?

Answer exactly:

Step 2: <city or town>
Final answer: <same answer as Step 2>
```

For the `father` example:

```text
Question:
Who is the father of the director of "La Caída"?

We already know the correct answer to Step 1.

Confirmed Step 1 result:
The director of "La Caída" is Leopoldo Torre Nilsson.

Treat this intermediate result as correct.
Do not verify it, replace it, or repeat it as the Step 2 answer.

Now answer only the next question:

Who was Leopoldo Torre Nilsson's father?

Answer exactly:

Step 2: <person>
Final answer: <same answer as Step 2>
```

This wording is mandatory.

The goal is to remove ambiguity about what the supplied intermediate state means.

---

# 6. Donor probe prompt redesign

The donor probe should also use natural-language questions.

Examples:

Instead of:

```text
Apply relation "place of birth" to "Gustaf Molander".
```

ask:

```text
In which city or town was Gustaf Molander born?

Answer exactly:

Answer: <city or town>
```

Instead of:

```text
Apply relation "father" to "Armando Robles Godoy".
```

ask:

```text
Who was Armando Robles Godoy's father?

Answer exactly:

Answer: <person>
```

Instead of:

```text
Apply relation "place of death" to "Isaac Schwartz".
```

ask:

```text
At what specific location did Isaac Schwartz die?

Answer exactly:

Answer: <specific location>
```

Do not include the original source sample in the donor probe.

The donor probe must remain an independent single-relation capability check.

---

# 7. Injected-state prompt redesign

The injected condition should mirror the Oracle structure, except that the supplied intermediate state is intentionally not labeled as correct or incorrect.

Do not tell the model that the value is false.

Use:

```text
Question:
Where was the director of the film "The Last Bridge" born?

For this continuation, use the following Step 1 result as the current intermediate state:

Step 1 result:
Gustaf Molander

Use this supplied intermediate result as the input to the next step.
Do not replace it or re-answer Step 1.

Now answer:

In which city or town was Gustaf Molander born?

Answer exactly:

Step 2: <city or town>
Final answer: <same answer as Step 2>
```

The wording should enforce continuation from the supplied state without explicitly claiming that the state is true.

This preserves the intervention logic.

---

# 8. Location granularity handling

The current evaluation incorrectly collapses:

```text
EXACT TARGET
```

and:

```text
BROADER BUT FACTUALLY COMPATIBLE LOCATION
```

into a single FAIL.

Add a location-aware semantic label.

For location relations, classify model output as one of:

```text
EXACT_CORRECT
BROADER_CORRECT
WRONG_LOCATION
UNKNOWN
INVALID_OUTPUT
```

Examples:

Dataset:

```text
Düsseldorf
```

Model:

```text
Düsseldorf
```

=> `EXACT_CORRECT`

Dataset:

```text
Düsseldorf
```

Model:

```text
Germany
```

=> `BROADER_CORRECT`

Dataset:

```text
Reykjavík
```

Model:

```text
Iceland
```

=> `BROADER_CORRECT`

Dataset:

```text
Helsingfors
```

Model:

```text
Stockholm
```

=> `WRONG_LOCATION`

Dataset:

```text
Lakshadweep
```

Model:

```text
Chennai
```

=> `WRONG_LOCATION`

Do not automatically classify a country-level answer as hallucination if it contains the gold city/town.

---

# 9. Eligibility rule versus factuality label

Separate:

```text
factual correctness
```

from:

```text
experimental eligibility
```

A response can be factually acceptable but still unsuitable for propagation measurement.

For example:

```text
gold_C = Düsseldorf
model = Germany
```

may be:

```text
semantic_label = BROADER_CORRECT
```

but:

```text
gate_pass = false
```

because the propagation experiment requires an identifiable specific `C`.

Therefore store both.

Example:

```json
{
  "semantic_label": "BROADER_CORRECT",
  "gate_pass": false
}
```

Do not call such a case a hallucination.

---

# 10. Non-location evaluation

For person/entity relations such as:

```text
director
composer
performer
father
```

continue to require correct entity identity.

Use aliases where available.

Add labels:

```text
EXACT_CORRECT
WRONG_ENTITY
UNKNOWN
COPY_INPUT
INVALID_OUTPUT
```

`COPY_INPUT` should be used when the model simply repeats the supplied intermediate entity instead of applying the requested downstream relation.

Example:

Oracle input:

```text
Leopoldo Torre Nilsson
```

Question:

```text
Who was Leopoldo Torre Nilsson's father?
```

Output:

```text
Leopoldo Torre Nilsson
```

=> `COPY_INPUT`

This should be distinguished from a generic wrong answer.

---

# 11. Prompt-diagnosis logging

For every output, record:

```json
{
  "semantic_label": "...",
  "gate_pass": true,
  "failure_type": "..."
}
```

Possible `failure_type` values:

```text
null
knowledge_error
granularity_mismatch
wrong_entity
copy_input
unknown_answer
format_failure
relation_execution_failure
```

Do not infer internal mechanism too strongly from one output.

These are behavioral labels.

---

# 12. Gate definitions for v2.1

## Gate A1 — baseline

Require:

```text
Step 1 = correct B
```

and:

```text
Step 2 = exact C
```

for experimental eligibility.

If Step 2 is only `BROADER_CORRECT`, record that but do not pass the gate.

## Gate A2 — oracle

Require the model to return exact `C` after being explicitly told:

```text
B is the correct, fixed intermediate result.
```

If the output is `BROADER_CORRECT`, record it separately but do not pass the propagation gate.

## Gate A3 — donor

Require exact `C'`.

Again, `BROADER_CORRECT` may count as semantically compatible but not experimentally eligible.

---

# 13. New diagnostic comparison

For each candidate, store the previous v2 prompt and the new v2.1 prompt metadata only if useful, but do not rerun the old prompt.

The new inspection should explicitly help answer:

```text
Did natural-language prompting fix operator-execution failures?
```

and:

```text
Did explicit Oracle semantics fix cases where the model misunderstood the supplied Step 1?
```

---

# 14. Smoke sample size

Use the same fixed five candidates from v2.

Do not resample new candidates before testing the prompt redesign.

This is important because otherwise prompt improvements become confounded with easier candidate selection.

Run:

```text
5 baseline
5 oracle
5 donor_probe
```

Only run injected trajectories for candidates that pass all three gates.

---

# 15. New output directory

Write all outputs to:

```text
results/smoke_v2_1/
```

Required files:

```text
inspection.md
trajectories.jsonl
metrics.json
summary.csv
gate.json
manifest.json
memory.json
```

Do not overwrite any v2 file.

---

# 16. Updated inspection.md format

For every candidate show:

```text
Question
A
r1
B
r2
C
B'
C'
```

Then show the exact model prompt.

For each condition report:

```text
Model response:
...

Semantic label:
EXACT_CORRECT / BROADER_CORRECT / WRONG_LOCATION / WRONG_ENTITY / COPY_INPUT / UNKNOWN / INVALID_OUTPUT

Gate:
PASS / FAIL

Failure type:
...
```

For location outputs, explicitly note why a broader geographic answer is factually compatible.

Example:

```text
Model answer: Germany
Gold target: Düsseldorf

Semantic label: BROADER_CORRECT
Reason: Düsseldorf is in Germany.
Gate: FAIL
Reason: exact city-level state is required for propagation identification.
```

---

# 17. Revised STOP CONDITIONS

## Stop Condition 1 — baseline relation execution still fails

If natural-language prompts still cause most baseline Step 1 outputs to return the wrong semantic type or unrelated entities, stop and report a remaining model/task capability issue.

## Stop Condition 2 — Oracle still systematically fails

If explicit Oracle instructions still result in most samples failing to compute the downstream relation, stop.

Do not proceed to propagation interpretation.

## Stop Condition 3 — donor knowledge still systematically fails

If natural-language donor probes still fail to recover exact `C'` for most samples, do not inject those donors.

## Stop Condition 4 — only granularity mismatch remains

If the main remaining issue is:

```text
city -> country
```

do not interpret it as hallucination.

Report it as an evaluation/schema issue and consider changing the task to an answer space with less hierarchical ambiguity.

## Stop Condition 5 — no silent candidate replacement

Do not replace failed samples with easier ones during this smoke test.

The fixed v2 candidates must be retained for this prompt-design comparison.

---

# 18. Interpretation rule

Do not claim any evidence about hallucination propagation unless at least 3 candidates satisfy all of:

```text
baseline exact pass
oracle exact pass
donor exact pass
```

Only those candidates may enter the injected-state experiment.

If fewer than 3 pass, the correct conclusion is:

```text
measurement setup remains insufficiently identified
```

not:

```text
propagation is weak or absent
```

---

# 19. Execution order

1. Preserve all existing v1 and v2 outputs.
2. Create `results/smoke_v2_1/`.
3. Reuse the current Qwen3-4B NF4 setup.
4. Implement natural-language relation templates.
5. Implement explicit Oracle semantics.
6. Implement revised injected-state semantics.
7. Add location granularity labels.
8. Add `COPY_INPUT`.
9. Run the same five baseline examples.
10. Run the same five Oracle examples.
11. Run the same five donor probes.
12. Evaluate with both:
   - semantic correctness label;
   - strict experimental gate.
13. Run injected condition only for samples passing all three strict gates.
14. Generate `inspection.md`.
15. Generate `gate.json`.
16. Stop for human review.
17. Do not scale further.

---

# 20. Success criterion

The immediate goal of v2.1 is not to demonstrate hallucination propagation.

Success means determining whether the v2 failures were mainly caused by:

```text
unnatural operator prompts
```

and/or:

```text
ambiguous Oracle semantics
```

rather than by model knowledge alone.

The most important comparison is:

```text
v2 operator-style prompt
vs
v2.1 natural-language prompt
```

on the same five examples.

Only after the natural-language Oracle and donor probes succeed reliably should the experiment move forward to injected-state propagation analysis.
