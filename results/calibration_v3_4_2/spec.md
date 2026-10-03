# Experiment v3.4.2 Codex Specification
## Monotonic Composition-Complexity Calibration for Qwen3-4B

## 0. Purpose

v3.4.1 showed that the calibration framework itself works:

- free generation, constrained candidate choice, and candidate-likelihood ranking agreed 96/96;
- output-format failures were eliminated;
- M2 (entity-near interference) and M3 (evidence-order/local salience) did not induce meaningful errors;
- M1 produced only a sparse isolated error;
- M4 (longer composition) was the most promising family, but the observed error pattern was sparse and non-monotonic.

v3.4.2 therefore narrows scope to one question:

> Can we construct a genuinely monotonic reasoning-complexity axis for Qwen3-4B, such that first-hop candidate confidence degrades progressively as valid composition depth and competing partial paths increase?

This is a calibration experiment only.

Do not run downstream propagation.
Do not report NPR.
Do not integrate SHAR/HalluSE.
Do not change model family.

---

# 1. Design intent

The experiment has four goals.

### Goal A — Isolate a cleaner difficulty axis

Difficulty must increase by controlled reasoning-graph complexity, not by changing candidate identity, answer plausibility, wording style, or evidence source quality.

### Goal B — Separate path depth from branch competition

Two factors should be varied explicitly:

1. `depth`: number of composition steps required to resolve the correct candidate;
2. `branching`: number of plausible structurally parallel dead-end paths.

### Goal C — Detect a capability frontier through both behavior and margin

A useful frontier should show not only more wrong candidate selections, but also a systematic decline in the gold-vs-best-wrong likelihood margin.

### Goal D — Produce a frozen construction rule for v3.5

Only if the frontier is confirmed on held-out cases should the selected regime be recommended for later natural-error propagation experiments.

---

# 2. Model and inference

Use the same pinned setup as v3.4.1:

```text
Qwen3-4B-Instruct-2507
4-bit NF4
BF16 compute
same tokenizer
same chat template
same deterministic settings
```

Use the same three elicitation channels:

```text
F = free generation
C = constrained candidate choice
L = candidate likelihood
```

Channel C remains the primary calibration channel.
Channel F and Channel L remain diagnostics.

---

# 3. Candidate universe

Each base case must use exactly four candidate intermediate entities:

```text
{B, B1', B2', B3'}
```

Requirements:

1. exactly one gold candidate `B`;
2. same four candidates reused across all difficulty levels of the same base case;
3. candidate order frozen across levels;
4. all candidates real entities;
5. all candidates have unique frozen downstream targets for future v3.5 use;
6. no candidate additions/replacements after inference;
7. gold candidate position balanced across the full split.

Candidate identity must never be part of the difficulty manipulation.

---

# 4. Synthetic reasoning graph

v3.4.2 should use a deliberately controlled symbolic graph overlay on top of real candidate names.

Reason:

- the candidate identities remain realistic and traceable;
- reasoning depth/branching can be manipulated cleanly;
- factual ambiguity from open-world knowledge is minimized;
- difficulty can be changed without changing who the candidates are.

Each prompt contains:

```text
candidate-name mapping records
graph-link records
one query asking which candidate is reached from the target item
```

Example:

```text
Record R17 names Feng Xiaoning.
Record R23 names Rolf Schübel.
Record R41 names Rodrigo Grande.
Record R58 names Anil Das.

Film A has credited-director link X1.
Record X1 has credited-director link X2.
Record X2 has credited-director link R17.
```

The answer is:

```text
Feng Xiaoning
```

The graph semantics must be explicit and deterministic.

No world knowledge is required to solve the first-hop task.

---

# 5. Factorial difficulty design

Use two controlled factors.

## Factor 1 — Composition depth

Define:

```text
Depth 1
Depth 2
Depth 3
Depth 4
```

Meaning:

```text
Depth 1:
A -> B

Depth 2:
A -> X1 -> B

Depth 3:
A -> X1 -> X2 -> B

Depth 4:
A -> X1 -> X2 -> X3 -> B
```

All links on the gold path must use the same queried relation label.

Do not change candidate names, wording, or output format with depth.

## Factor 2 — Competing branch count

Define:

```text
Branch 0
Branch 1
Branch 2
```

### Branch 0
Only the gold path exists.

### Branch 1
Add one structurally parallel dead-end path.

### Branch 2
Add two structurally parallel dead-end paths.

Requirements:

- wrong branches should be structurally similar to the gold path;
- they must not make the task ambiguous;
- all branches must terminate at registered candidates;
- wrong branches must differ from the gold path by one decisive relation label or graph-role marker before the candidate endpoint.

---

# 6. Difficulty grid

The full development grid is:

```text
Depth 1 × Branch 0
Depth 1 × Branch 1
Depth 1 × Branch 2
Depth 2 × Branch 0
Depth 2 × Branch 1
Depth 2 × Branch 2
Depth 3 × Branch 0
Depth 3 × Branch 1
Depth 3 × Branch 2
Depth 4 × Branch 0
Depth 4 × Branch 1
Depth 4 × Branch 2
```

Total:

```text
12 conditions per base case
```

This is preferred over a single D0–D4 ladder because it separates:

```text
more reasoning depth
```

from:

```text
more competing paths
```

---

# 7. Base-case splits

Construct and freeze:

## Development split

```text
8 base cases
```

Each case runs all 12 depth × branch conditions.

Total Channel-C decisions:

```text
8 × 12 = 96
```

The same 96 prompts are evaluated through F and L.

## Held-out split

```text
12 new base cases
```

Do not run the full grid on held-out.

After development analysis, select at most:

```text
2 candidate frontier conditions
```

Then run each selected condition across all 12 held-out cases.

Held-out target questions must be disjoint from development target questions.

---

# 8. Prompt invariance rules

Within a base case, these must stay fixed across all 12 conditions:

```text
question wording
candidate list
candidate order
candidate-name records
relation vocabulary
chat template
instruction wording
output contract
```

Only these may change:

```text
number of gold-path intermediate graph nodes
number of competing branch paths
```

---

# 9. Gold-path construction

Every condition must preserve one unique deterministic gold path.

Example:

### Depth 1 / Branch 0

```text
Film A has credited-director link R17.
Record R17 names Feng Xiaoning.
```

### Depth 3 / Branch 0

```text
Film A has credited-director link X1.
Record X1 has credited-director link X2.
Record X2 has credited-director link R17.
Record R17 names Feng Xiaoning.
```

### Depth 3 / Branch 1

```text
Film A has credited-director link X1.
Record X1 has credited-director link X2.
Record X2 has credited-director link R17.

Film A has comparison-director link Y1.
Record Y1 has comparison-director link Y2.
Record Y2 has comparison-director link R23.
```

The wrong branch is locally parallel but invalid for the queried relation.

---

# 10. Relation-label control

Use a small fixed relation vocabulary.

Example:

```text
credited-director
comparison-director
associated-director
archival-director
```

The query explicitly asks for:

```text
credited-director
```

Rules:

1. gold path always uses the queried relation;
2. wrong branches use non-query relation labels;
3. relation labels should be structurally parallel and equally explicit;
4. avoid natural-language ambiguity;
5. never use “correct”, “wrong”, “gold”, “distractor” in prompts.

The aim is graph competition, not semantic vagueness.

---

# 11. Elicitation channels

## Channel F — Free generation

Prompt ends with:

```text
Which candidate is the credited director of Film A?

Answer with only one candidate name.
```

Settings:

```text
greedy
max_new_tokens = 96
```

Record:

```text
strict_exact_candidate
extractable_candidate
out_of_set
truncated
raw_text
```

## Channel C — Constrained choice

Allow only one of the four complete candidate strings.

Use the same guided-choice implementation verified in v3.4.1.

Requirements:

```text
100% valid candidate output
all four candidates reachable
same order as F
no post-hoc extraction
```

Primary behavioral metric is based on Channel C.

## Channel L — Candidate likelihood

For each prompt score all four candidate names.

Record:

```text
sum_logprob
mean_logprob_per_token
rank
gold_vs_best_wrong_margin
```

Primary margin:

\[
M = score(B)-\max_{i \neq B} score(B_i')
\]

Use mean logprob/token for preregistered frontier analysis.

---

# 12. Primary metrics

## 12.1 Error rate

\[
ER(d,b)=P(\hat B \neq B)
\]

using Channel C.

## 12.2 Gold margin

\[
GM(d,b)=\mathrm{median}(M)
\]

## 12.3 Near-boundary fraction

Freeze threshold before inference:

```text
|M| <= 0.75 nats/token
```

Then:

\[
NBF(d,b)=P(|M|\le 0.75)
\]

Use 0.75 because v3.4.1 genuine flips clustered near approximately -0.5 while most easy cases remained much farther away.

## 12.4 Free-vs-Constrained Agreement

\[
FCA=P(F=C)
\]

among strict-valid free outputs.

## 12.5 Likelihood-vs-Constrained Agreement

\[
LCA=P(\arg\max L=C)
\]

---

# 13. Monotonicity diagnostics

For each branch count `b`, inspect:

```text
ER(1,b), ER(2,b), ER(3,b), ER(4,b)
```

Useful pattern:

```text
non-decreasing ER
```

For each depth `d`, inspect:

```text
ER(d,0), ER(d,1), ER(d,2)
```

Useful pattern:

```text
non-decreasing ER
```

Likewise, gold margins should tend to decrease with difficulty:

```text
GM harder < GM easier
```

Perfect case-by-case monotonicity is not required.

---

# 14. Aggregate monotonicity score

For development, compute descriptive monotonicity scores.

## Depth monotonicity

Across branch settings, count adjacent comparisons satisfying:

```text
ER(d+1,b) >= ER(d,b)
```

and separately:

```text
GM(d+1,b) <= GM(d,b)
```

## Branch monotonicity

Across depths, count adjacent comparisons satisfying:

```text
ER(d,b+1) >= ER(d,b)
```

and:

```text
GM(d,b+1) <= GM(d,b)
```

Report proportions only; do not treat as inferential statistics.

---

# 15. Frontier-selection rule

A development condition `(d,b)` is a provisional frontier candidate only if all are true:

1. Channel-C error rate is between:

```text
20% and 50%
```

2. near-boundary fraction is at least:

```text
3/8 cases
```

3. median gold margin is between:

```text
-1.0 and +1.5 nats/token
```

4. FCA >= 80%;
5. LCA >= 80%;
6. no candidate-position bias;
7. unique-answer audit passes;
8. condition lies on a broadly monotonic local path.

“Broadly monotonic local path” means at least one neighboring easier condition has lower ER or higher GM.

Do not select an isolated spike with no local trend.

Select at most two provisional frontier conditions.

---

# 16. Held-out confirmation

For each selected `(depth, branch)` pair, run all 12 held-out cases through F/C/L.

A condition is confirmed if:

1. Channel-C error rate is between:

```text
15% and 50%
```

2. at least 4/12 cases have:

```text
|margin| <= 0.75
```

3. FCA >= 80%;
4. LCA >= 80%;
5. no serious position bias;
6. unique gold path audit passes.

Do not retune after held-out results.

---

# 17. Candidate-position control

Development:

```text
2 cases per gold position
```

Held-out:

```text
3 cases per gold position
```

Candidate order remains fixed across all conditions of a base case.

Report wrong-selection frequency by candidate position.

---

# 18. Base-case consistency check

For every base case produce:

| Depth | Branches | Gold | C choice | L top-1 | Margin |
|---|---:|---|---|---|---:|

Classify the base case:

```text
CASE_MONOTONIC
CASE_NON_MONOTONIC
CASE_ALWAYS_EASY
CASE_ALWAYS_WRONG
CASE_BOUNDARY_CROSSING
```

The target pattern is:

```text
correct at easier levels
margin progressively shrinks
eventually flips at harder level
```

---

# 19. Design-intent mapping check

Before inference create this table in `design_audit.md`:

| Design intention | Experimental feature | Observable check | Failure meaning |
|---|---|---|---|
| Build a monotonic difficulty axis | Factorial depth × branch design | ER and GM trends | Difficulty manipulation is not ordered |
| Separate two sources of difficulty | Depth and branch count manipulated independently | Factor-specific curves | Cannot attribute difficulty source |
| Preserve traceability | Fixed four-candidate universe with frozen downstream mappings | 100% mapping audit | Future propagation cannot be measured |
| Avoid candidate-identity confounds | Same candidates within case across all levels | Hash equality of candidate lists | Difficulty mixed with candidate replacement |
| Avoid format confounds | Channel C primary; F shadow | C validity 100%; FCA | Interface failure |
| Measure capability boundary | Channel L margins | GM/NBF curves | Errors are isolated case artifacts |
| Avoid isolated-error selection | Frontier requires local monotonic support | Neighboring easier-condition check | Selected condition is a spike |
| Prevent overfitting | Dev/held-out split | One-shot held-out confirmation | Frontier does not replicate |
| Preserve unique answer | Deterministic graph + relation audit | One valid queried endpoint | Errors may reflect ambiguity |
| Keep calibration scope | No downstream continuation | NPR absent | Premature propagation claim |

Codex must verify this table against actual rendered prompts before inference.

After inference add a post-run achievement table.

---

# 20. Measurement gate

v3.4.2 passes only if at least one held-out condition is confirmed.

Development alone cannot authorize v3.5.

Additionally require:

```text
Channel-C validity = 100%
FCA >= 80%
LCA >= 80%
no serious position bias
all candidate mappings frozen
zero ambiguous graph renderings
```

If no condition is confirmed:

```text
v3.5_authorized = false
```

---

# 21. Stop conditions

Stop and inspect if:

- guided choice fails;
- likelihood scoring differs from the actual chat rendering;
- any graph contains two valid queried-relation paths;
- candidate identities change across difficulty;
- relation wording changes unintentionally;
- most errors are explained by candidate position;
- error rates remain ~0 across the whole grid;
- the grid jumps directly from near-0 to near-random with no boundary regime;
- observed errors are isolated spikes without margin support.

---

# 22. Required artifacts

Create:

```text
results/calibration_v3_4_2/
```

Required:

```text
design_audit.md
dev_cases.json
heldout_cases.json
prompt_plan.json
free_generation.jsonl
constrained_choice.jsonl
candidate_likelihoods.jsonl
inspection.md
diagnosis.md
metrics.json
frontier_selection.md
gate.json
manifest.json
```

---

# 23. inspection.md

For every base case, show all 12 development conditions.

Highlight:

```text
first margin compression
first near-boundary condition
first choice flip
recovery after flip
non-monotonic reversal
branch-induced flip
depth-induced flip
```

For frontier candidates, show exact prompt differences between neighboring conditions.

---

# 24. diagnosis.md

Answer explicitly:

1. Does increasing depth reduce gold margin?
2. Does increasing branch count reduce gold margin?
3. Which factor matters more for Qwen3-4B?
4. Are behavioral errors broadly monotonic?
5. Are likelihood margins more monotonic than 0/1 error rates?
6. Which cases show genuine boundary crossing?
7. Are any errors isolated spikes?
8. Which development conditions qualify as provisional frontiers?
9. Do held-out cases confirm them?
10. Is there a frozen construction rule suitable for v3.5?

---

# 25. Authorization for v3.5

If and only if the gate passes, recommend one frozen frontier regime:

```text
depth = ...
branch_count = ...
relation vocabulary = ...
candidate construction rule = ...
primary elicitation channel = constrained choice
expected traceable first-hop error range = ...
known limitations = ...
```

Do not automatically launch v3.5.

The future v3.5 should then reintroduce downstream continuation and measure propagation from model-selected wrong intermediate states.
