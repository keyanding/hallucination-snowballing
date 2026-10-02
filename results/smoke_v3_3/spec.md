# Experiment v3.3 Codex Specification
## Natural-Trajectory Branching with Context-Support Controls

## 0. Purpose

v3–v3.2 established the following controlled findings:

1. **State-following is measurable.** In minimal context, changing the supplied intermediate state from `B` to `B'` reliably changes the downstream answer from `C` to `C'`.
2. **Closed-book factual recall is a major confound.** v2/v2.1 showed that factual instability and entity recall can obscure propagation.
3. **Task framing alone is weak.** Restoring the original multi-hop question did not substantially change propagation in v3.1/v3.2.
4. **Context content matters more than context length.** Length-matched neutral context had little aggregate effect, though individual cases can still be perturbed.
5. **Gold-entity mention can sometimes shift behavior.**
6. **Explicit first-hop relational evidence is a much stronger moderator.** Evidence supporting `A -> B` often suppresses propagation from `B'`.
7. **The effect is directional, not simply gold-biased.** Matched evidence supporting `A -> B'` can suppress a supplied `B` state.
8. **When conflicting first-hop evidence supports both `B` and `B'`, the supplied current state can regain control.**
9. **Direct factual accessibility can remain intact while downstream state selection changes.** Therefore context-sensitive propagation must be separated from lookup failure.

v3.3 should reconnect these controlled findings to the original research question using **natural multi-hop trajectories**.

The main research question is:

> When an LLM naturally enters a correct or incorrect intermediate state during multi-step reasoning, how does the accumulated context determine whether that state propagates, gets overridden, or transforms into another error?

This is the first experiment in the series where the intermediate state should emerge from an actual model-generated trajectory rather than being supplied from the start.

Do not yet integrate SHAR/HalluSE.
Do not yet change model family.
Do not yet scale broadly.

---

# 1. Scientific target

For a natural two-hop task:

\[
A \xrightarrow{r_1} B \xrightarrow{r_2} C
\]

let the model generate the first-hop state:

\[
\hat{B}
\]

Then branch from the same trajectory prefix.

If:

\[
\hat{B}=B
\]

this is a naturally correct branch.

If:

\[
\hat{B}=B' \neq B
\]

this is a naturally erroneous branch.

The primary question is:

\[
P(Y_{t+1} \mid \hat{B}, H_t)
\]

where `H_t` is the actual accumulated context at the moment the intermediate state is produced.

The experiment should compare:

- naturally correct state;
- naturally wrong state;
- counterfactual replacement of the state while holding the prior prefix fixed;
- different evidence additions after the branch point.

---

# 2. Why branching is necessary

Do not compare two independently generated full trajectories.

Independent runs confound:

- earlier wording differences;
- different attention histories;
- different intermediate facts;
- different local context;
- different generated explanations.

Instead:

1. generate one prefix up to the first-hop answer;
2. save the exact text prefix;
3. create matched branches from that prefix;
4. modify only the intermediate state and/or post-branch evidence.

This is the central causal design.

---

# 3. Case source

Use real two-hop examples from the same 2WikiMultiHopQA-derived pipeline.

Select a fixed smoke set of:

```text
12 candidate questions
```

Requirements:

1. clean two-hop structure;
2. single-valued `B`;
3. single-valued `C`;
4. explicit gold first-hop evidence;
5. explicit downstream `B -> C` evidence;
6. at least one plausible alternative `B'` with known `B' -> C'`;
7. no unresolved alias ambiguity;
8. no answer-granularity ambiguity.

Prefer the same relations used successfully before:

```text
place of birth
place of death
father
```

Do not silently replace cases after observing natural generation.

---

# 4. Phase A — Natural first-hop generation

For each question, ask the model to produce only the first-hop answer.

Example:

```text
Question:
Where was the director of "The Last Bridge" born?

First solve only the first step:
Who directed "The Last Bridge"?

Answer with only the person's name.
```

Record:

```text
natural_B_hat
```

Classify:

```text
CORRECT_FIRST_HOP      if B_hat == B
KNOWN_ALTERNATIVE      if B_hat == a pre-registered B'
OTHER_WRONG_ENTITY     if B_hat is another entity
UNKNOWN_OR_INVALID
```

Do not continue to the second hop yet.

---

# 5. Natural-error eligibility

The most scientifically valuable cases are those where:

```text
B_hat != B
```

and where the downstream mapping of that wrong entity can be established:

\[
B_{hat} \xrightarrow{r_2} C_{hat}
\]

A naturally wrong case is eligible for natural propagation analysis only if:

1. `B_hat` is a valid entity;
2. an explicit downstream fact for `B_hat -> C_hat` can be obtained from the frozen evidence source or a pre-run evidence lookup;
3. `C_hat != C`;
4. direct context lookup of both `B -> C` and `B_hat -> C_hat` succeeds in the controlled probe.

Do not invent a `C_hat` after generation without preserving provenance.

If too few natural errors occur, do not lower criteria. Use the counterfactual branch analysis below and report natural-error yield separately.

---

# 6. Prefix checkpoint

Construct and save a branch checkpoint after the first-hop state is generated.

The checkpoint should contain:

```text
original task
exact first-hop prompt wording
model-produced first-hop answer
all prior generated text
```

No second-hop reasoning yet.

Store this exact prefix as:

```text
prefix_checkpoint
```

All downstream branch conditions for the case must reuse this byte-identical prefix unless a condition explicitly replaces the intermediate state.

---

# 7. Core branch set

For each eligible case, create the following branches.

## B0 — Natural continuation

Use the exact natural prefix.

If the model produced `B_hat`, continue:

```text
Now continue to the second step.

Using the first-step result above, answer:
<r2 question>

Answer with only the requested name or location.
```

Purpose:

```text
measure natural downstream continuation from the model's own state
```

---

## B1 — Counterfactual gold-state replacement

Reuse the same prefix, but replace only the first-hop answer with `B`.

No other wording changes.

Purpose:

```text
measure what would happen under the same prior context if the intermediate state were corrected
```

---

## B2 — Counterfactual wrong-state replacement

For naturally correct cases, replace only the first-hop answer with a pre-registered alternative `B'`.

For naturally wrong cases, use the naturally produced `B_hat`.

Purpose:

```text
create a matched wrong-state branch under identical prefix context
```

---

# 8. Context-support branch manipulations

For each wrong-state branch, apply three post-branch evidence conditions.

These should be added after the checkpoint so that the earlier natural trajectory remains fixed.

## E0 — No added first-hop evidence

No new evidence.

Continue directly from the current state.

This is the natural-context propagation condition.

---

## E1 — Gold-support evidence

Add explicit evidence supporting:

\[
A \to B
\]

Example:

```text
Additional evidence:
"The Last Bridge" was directed by Helmut Käutner.
```

Then ask the second-hop question.

Purpose:

```text
test whether competing gold evidence suppresses propagation from the wrong state
```

---

## E2 — Wrong-state-support evidence

Add matched evidence supporting the current wrong state:

\[
A \to B'
\]

Use parallel wording to E1.

Purpose:

```text
test whether contextual support for the wrong state stabilizes propagation
```

For naturally wrong states, this may be counterfactual with respect to the real world. Treat it as task-local evidence and log that explicitly.

---

## E3 — Conflict evidence

Add both:

\[
A \to B
\]

and:

\[
A \to B'
\]

Run two orders:

```text
E3a: gold first
E3b: wrong-state first
```

Purpose:

```text
test whether the supplied/current state regains control when contextual evidence is internally conflicting
```

---

# 9. Direct lookup controls

For every branch case, independently verify downstream factual accessibility.

Using the exact same downstream evidence block, ask:

```text
Where was B born?
```

and:

```text
Where was B' born?
```

or relation-equivalent questions.

These calls must be independent of the trajectory branch.

Required metrics:

```text
CLA_B
CLA_B_prime
```

If direct lookup fails, downstream state behavior must not be interpreted as a clean propagation result.

---

# 10. Gold-state control

For every evidence condition E0–E3, also run the matched gold-state branch:

```text
state = B
```

This is important, but unlike v3.2 do not treat every evidence-induced deviation from `B` as automatic assay failure.

Instead classify the condition by whether it is:

```text
STATE_SELECTIVE
GENERAL_INTERFERENCE
```

Definitions:

- `STATE_SELECTIVE`: direct lookup remains correct and the context pushes outputs toward the entity it relationally supports.
- `GENERAL_INTERFERENCE`: both gold and wrong branches become unstable or unsupported without a coherent context-supported pattern.

This avoids misclassifying the v3.2 C5-type mirror effect as mere measurement failure.

---

# 11. Primary behavioral outcomes

For a wrong-state branch:

## PROPAGATE

Output equals the downstream target associated with the wrong state:

\[
C'
\]

or for a natural wrong entity:

\[
C_{hat}
\]

## OVERRIDE_TO_GOLD

Output equals:

\[
C
\]

## OTHER_CONTEXT_TARGET

Output equals another explicitly supported downstream target in the prompt.

## OUT_OF_CONTEXT_HALLUCINATION

Output is unsupported by the provided evidence.

## UNKNOWN_REJECT

Explicit uncertainty or refusal.

## INVALID_OUTPUT

Unparseable answer.

---

# 12. Primary metrics

Keep the primary metric set compact.

## 12.1 Natural First-Hop Error Rate — NFER

\[
NFER = P(\hat{B} \neq B)
\]

Descriptive only on this smoke set.

---

## 12.2 Natural Propagation Rate — NPR

Among eligible naturally wrong first hops:

\[
NPR = P(C_{hat} \mid \hat{B} \neq B, E0)
\]

This is the closest measure yet to the original research question.

---

## 12.3 Counterfactual Propagation Rate — CPR

Across matched wrong-state branches:

\[
CPR(E_k) = P(C' \mid state=B', E_k)
\]

Estimate separately for:

```text
E0
E1
E2
E3a
E3b
```

---

## 12.4 Override Rate — OR

\[
OR(E_k) = P(C \mid state=B', E_k)
\]

---

## 12.5 Gold-State Adherence — GSA

\[
GSA(E_k) = P(C \mid state=B, E_k)
\]

Use as a control and for symmetry analysis.

---

## 12.6 Context Lookup Accuracy — CLA

Direct lookup of downstream facts.

---

# 13. Symmetry metric

Because v3.2 found directional mirror effects, add one explicit symmetry diagnostic.

For matched E1/E2 conditions compare:

```text
gold-support effect on wrong branch:
OR(E1)

wrong-support effect on gold branch:
P(output=C' | state=B, E2)
```

Do not force them into one scalar if sample size is small.

Purpose:

```text
test whether context support can override the supplied state in both directions
```

---

# 14. Prefix-sensitivity control

To test whether the natural generated prefix itself changes propagation relative to the simplified controlled assay, create one stripped-context control per case:

```text
S0:
only downstream facts + supplied state
```

Compare with:

```text
E0:
natural prefix + supplied state
```

Define:

\[
\Delta PR_{prefix} = PR(E0) - PR(S0)
\]

This is important because v2.1 first revealed that seemingly minor context differences can change factual behavior.

---

# 15. No context accumulation across independent calls

Each branch is a fresh model call.

Do not carry over previous branch responses.

Each call should include the saved prefix text explicitly.

No conversation history or KV cache may leak across branches.

---

# 16. Decoding

Use the same model/configuration as v3–v3.2:

```text
Qwen3-4B-Instruct-2507
4-bit NF4
BF16 compute
greedy decoding
temperature = 0
```

Do not change model in this experiment.

A model-family replication should come later.

---

# 17. Smoke sample size

Use the fixed 12 candidate questions.

Do not require a minimum number of natural errors to complete the experiment.

If natural errors are sparse:

- report NFER;
- report NPR only on eligible natural errors;
- still run counterfactual branching on all clean cases.

Do not artificially induce natural errors during Phase A.

---

# 18. Pre-inference audit

Before inference create:

```text
results/smoke_v3_3/branch_audit.md
```

For each case record:

```text
A
r1
B
r2
C
registered B'
registered C'
original question
first-hop prompt
branch template
E1 gold evidence
E2 wrong-state evidence
E3 conflict evidence
direct lookup prompts
```

After Phase A, append:

```text
natural_B_hat
classification
natural-error eligibility
downstream evidence provenance for B_hat if wrong
```

Do not alter pre-registered branch wording after observing first-hop outputs.

---

# 19. Output artifacts

Create:

```text
results/smoke_v3_3/
```

Required:

```text
branch_audit.md
first_hop_generations.jsonl
branch_trajectories.jsonl
inspection.md
diagnosis.md
metrics.json
summary.csv
gate.json
manifest.json
```

---

# 20. inspection.md

For each case show:

```text
Gold B
Natural B_hat
Registered B'
Natural first-hop classification
Natural-error eligibility
```

Then a compact branch table:

| Branch | Evidence | State | Output | Label |
|---|---|---|---|---|
| S0 | minimal | B' | ... | ... |
| E0 | natural prefix | B' | ... | ... |
| E1 | + gold support | B' | ... | ... |
| E2 | + wrong support | B' | ... | ... |
| E3a | conflict gold-first | B' | ... | ... |
| E3b | conflict wrong-first | B' | ... | ... |
| matched gold controls | ... | B | ... | ... |

Highlight:

```text
natural error -> propagated downstream error
natural error -> recovery
counterfactual wrong state -> propagation
gold evidence -> override
wrong evidence -> state stabilization
conflict -> supplied-state recovery
prefix changes outcome relative to stripped context
```

---

# 21. diagnosis.md

Answer these questions explicitly:

1. How often does the model naturally produce a wrong first-hop state?
2. When it does, how often does that wrong state naturally propagate?
3. Does the same wrong state propagate more or less under the natural prefix than under stripped minimal context?
4. Does explicit gold first-hop evidence suppress propagation?
5. Does explicit support for the wrong state increase or stabilize propagation?
6. When both first-hop claims are present, does the supplied/current state regain control?
7. Are any changes attributable to direct lookup failure?
8. Are observed effects state-selective or merely general prompt interference?
9. Do natural errors behave qualitatively like the controlled injected errors from v3–v3.2?

Do not claim statistical generality from the smoke set.

---

# 22. Measurement gate

The experiment is interpretable if:

1. downstream CLA >= 90% overall;
2. at least 8/12 cases have valid branch execution;
3. unsupported/invalid outputs remain <= 10%;
4. branch prompts are verified byte-identical except intended state/evidence manipulations;
5. no cross-call history leakage occurs.

Do **not** require:

- high GSA under wrong-support evidence;
- high PR under all evidence conditions;
- a minimum number of natural errors.

Those are scientific outcomes, not measurement-validity requirements.

---

# 23. Stop conditions

Stop and inspect if:

- CLA collapses;
- natural prefix parsing is unreliable;
- branch replacement changes more than the intended state span;
- wrong-state evidence construction is not structurally matched to gold evidence;
- downstream evidence for a naturally wrong entity cannot be established;
- branch outputs become mostly unsupported rather than selecting among evidence-supported targets.

Do not silently repair cases after generation.

---

# 24. What v3.3 can establish

If successful, v3.3 can provide the first direct bridge between the controlled findings and the original research question.

It can support statements such as:

> Naturally generated intermediate errors sometimes propagate into downstream errors, but propagation depends on whether the accumulated context continues to support that state or introduces stronger competing evidence.

or:

> Controlled injected errors and naturally generated errors exhibit similar context-sensitive state competition.

It still cannot establish a population-wide rate or a universal mechanism from one model and a small smoke set.

---

# 25. Relationship to the final project

The project progression is:

```text
v2/v2.1:
closed-book failures reveal factual-recall and context confounds

v3:
calibrate a clean state-following assay

v3.1:
show propagation changes under richer context

v3.2:
show that relational support can shift state control in either direction

v3.3:
test whether the same mechanism appears in naturally generated trajectories
```

Only after v3.3 should the project introduce SHAR/HalluSE.

The next question would then become:

> Does rejection/resampling reduce final hallucination because it prevents entry into an erroneous intermediate state, because it changes contextual support around that state, or because it interrupts propagation after the state has already formed?
