# Experiment v3.4.3 Codex Specification
## Candidate-Order Counterfactual Control for Primacy vs Identity Effects

## 0. Purpose

v3.4.2 produced a promising capability-frontier signal, but 34/38 wrong selections landed on candidate position 1. Because candidate identity and position were fixed within each case, v3.4.2 cannot distinguish candidate-position primacy from candidate-identity preference or case-specific graph effects.

Primary question:

> When candidate identities are permuted while reasoning graph and semantic content remain fixed, do errors follow candidate position, candidate identity, or neither?

Secondary question:

> Does reasoning difficulty amplify any candidate-position effect?

This is a calibration/control experiment only. Do not run downstream propagation. Do not report NPR. Do not integrate SHAR/HalluSE. Do not change model family.

## 1. Core causal intervention

For each case-condition pair, hold fixed:

- graph
- question
- candidate identities
- candidate-name records
- gold identity
- wrong identities
- relation labels
- graph-node IDs
- chat template
- decoding settings

Manipulate only candidate answer-option order.

Each candidate identity must appear exactly once in positions 1, 2, 3, and 4 across the four counterfactual permutations.

## 2. Model and inference

Use exactly the v3.4.2 setup:

- Qwen3-4B-Instruct-2507
- 4-bit NF4
- BF16 compute
- same tokenizer
- same chat template
- same deterministic settings

Use the same channels:

- F = free generation
- C = constrained candidate choice
- L = candidate likelihood

Channel C remains primary.

## 3. Cases

Use six v3.4.2 development cases:

- dev-04
- dev-07
- dev-05
- dev-01
- dev-06
- dev-08

Rationale:

- dev-04, dev-07: always-wrong cases; major contributors to position-1 errors
- dev-05: clean boundary-crossing case
- dev-01: additional nontrivial case
- dev-06, dev-08: always-easy controls

Do not alter this set after inference begins.

## 4. Difficulty conditions

Use exactly three frozen v3.4.2 graph conditions:

- EASY = D1B0
- MID = D3B0
- HARD = D4B2

D3B0 and D4B2 were frontier-like but blocked by the position-bias gate.

Reuse the original graph rendering byte-for-byte wherever possible. Only candidate answer-option order may change.

## 5. Candidate-order permutations

Let the original candidates be A, B, C, D. Use four fixed cyclic rotations:

- P1: A B C D
- P2: B C D A
- P3: C D A B
- P4: D A B C

This guarantees every identity occurs once at every absolute position.

Do not use adaptive or post-hoc permutations.

## 6. Run size

6 cases × 3 difficulty conditions × 4 permutations = 72 prompts.

Run all 72 through F, C, and L.

Do not treat the 72 prompts as 72 independent cases. The repeated unit is case × difficulty condition.

## 7. Critical prompt-invariance requirement

Within one case-condition set, keep identical:

- system prompt
- user instruction
- question wording
- graph records
- graph-record order
- relation vocabulary
- graph-node IDs
- candidate identities
- gold identity
- output instruction

Only candidate answer-option order changes.

### Candidate-name record control

If candidate-name mapping records occur in the evidence, keep those records in one fixed canonical order independent of candidate answer-option order.

Preferred structure:

```text
Record R17 names Candidate A.
Record R23 names Candidate B.
Record R41 names Candidate C.
Record R58 names Candidate D.

[graph evidence unchanged]

Candidates:
1. ...
2. ...
3. ...
4. ...
```

Permute only the explicit candidate list.

Do NOT reorder evidence/name records together with the candidate list, because that would confound candidate-list position with evidence order.

## 8. Relation to prior primacy observations

v3.3 observed an evidence-order primacy tendency under conflicting evidence.

v3.4.2 observed a candidate-position-1 concentration.

Treat these as separate hypotheses.

v3.4.3 tests only:

> candidate-position primacy: a candidate is more likely to be selected when placed earlier in the answer-option list, holding identity and evidence fixed.

Do not claim the same internal mechanism explains v3.3 and v3.4.2.

## 9. Elicitation channels

### F — Free generation

Same style as v3.4.2:

```text
Answer with only one candidate name.
```

Use greedy decoding and max_new_tokens = 96.

Record raw text, strict exact candidate, extractable candidate, out-of-set, truncated.

### C — Constrained choice

Allow only the four complete candidate strings using the same verified guided-choice implementation.

Require 100% valid output.

### L — Candidate likelihood

Score all four candidate identities under every permutation.

Record:

- sum_logprob
- mean_logprob_per_token
- rank
- absolute candidate position
- identity

Primary score remains mean_logprob_per_token.

## 10. Primary metrics

### Position Selection Rate

For position p:

PSR_p = P(selected candidate occupies position p)

Under no position preference, PSR_p should be approximately 0.25 because identity is counterbalanced.

### Identity Stability Rate

For each case-condition set:

ISR = max_i count(selected identity i across the 4 permutations) / 4

ISR = 1 means the same identity is chosen regardless of where it is placed.

### Strict Position-Following Event

For adjacent/permutation comparisons where the old position-1 identity moves away:

- old position-1 identity moves away, and
- the new position-1 identity becomes selected.

Aggregate as PFR, the position-following rate.

### Gold Position Accuracy

For each gold position p:

GPA_p = P(gold selected | gold is at position p)

A candidate-position primacy effect predicts GPA_1 > GPA_2, GPA_3, GPA_4.

## 11. Likelihood-based position effect

For candidate identity i:

Delta(i,p) = score(i at position p) - mean(score(i at the other 3 positions))

Primary focus is Delta(i,1).

Report mean and median Delta by position across case-condition sets.

A systematic positive Delta(i,1) means the same identity receives a higher candidate likelihood merely by being placed first.

## 12. Within-set classification

Classify every case-condition set over its four permutations:

- GOLD_STABLE: gold chosen in 4/4
- IDENTITY_LOCKED: same non-gold identity chosen in 4/4
- POSITION_1_LOCKED: candidate currently in position 1 chosen in at least 3/4, with at least two different identities selected across permutations
- MIXED_POSITION_IDENTITY: choices change with order, but neither identity nor position dominates
- UNSTABLE_OTHER: none of the above

Priority if labels overlap:

GOLD_STABLE > IDENTITY_LOCKED > POSITION_1_LOCKED > MIXED_POSITION_IDENTITY > UNSTABLE_OTHER

## 13. Difficulty × position interaction

For EASY, MID, HARD separately compute:

- PSR_1
- PFR
- mean Delta(position 1)
- GPA by gold position

A pattern such as:

PSR_1(HARD) > PSR_1(MID) > PSR_1(EASY)

or increasing positive Delta(position 1) with difficulty is consistent with:

> greater reasoning uncertainty increases reliance on answer-option order.

Do not interpret this as an internal cognitive mechanism.

## 14. Case-specific checks

### dev-04 and dev-07

Main question:

> Were their v3.4.2 always-wrong outputs caused by the wrong identity itself or because that identity occupied position 1?

If the same wrong identity remains selected across all positions: identity/case effect.

If selection follows whichever identity moves into position 1: position effect.

### dev-05

Main question:

> Does the v3.4.2 capability-boundary behavior survive candidate-order changes?

If the same EASY→MID→HARD degradation persists after counterbalancing, that strengthens the complexity interpretation.

### dev-06 and dev-08

Main question:

> Do always-easy cases remain robust to candidate-order permutation?

If easy controls become highly order-sensitive, the task has a stronger option-order artifact than expected.

## 15. Primary decision logic

### Outcome A — Strong position effect

Evidence:

- PSR_1 materially above 0.25
- multiple POSITION_1_LOCKED sets
- positive position-1 likelihood shifts
- identities selected change when order changes

Interpretation:

v3.4.2 errors were substantially contaminated by candidate-order primacy.

### Outcome B — Strong identity/case effect

Evidence:

- high ISR
- many IDENTITY_LOCKED sets
- low PFR
- same wrong identity selected across positions

Interpretation:

the pooled position signal mainly reflected fixed identity/case effects.

### Outcome C — Difficulty-dependent position effect

Evidence:

- weak order effect at EASY
- stronger order effect at MID/HARD

Interpretation:

reasoning uncertainty may increase reliance on candidate-order heuristics.

### Outcome D — Neither explains instability

Evidence:

- low ISR
- low PFR
- no stable PSR pattern

Interpretation:

selection instability likely arises from more complex graph/prompt interactions.

## 16. Statistical treatment

Use paired/descriptive repeated-measures analysis.

Do not treat 72 prompts as independent.

Optional: exact randomization/permutation test for excess position-1 selection under equal-position assignment.

Do not make population-level claims from six cases.

## 17. Frontier salvage check

Revisit only D3B0 and D4B2 after order counterbalancing.

For each report:

- counterbalanced error behavior
- counterbalanced median gold margin
- near-boundary fraction
- PSR by position
- identity stability

Do not count the four orderings as four new independent cases.

Preferred per-case summary:

1. summarize choice/margin across the four positions;
2. aggregate across the six cases.

This is diagnostic, not a replacement for a new clean development split.

## 18. Design-intent mapping check

Before inference create this table in design_audit.md:

| Design intention | Experimental feature | Observable check | Failure meaning |
|---|---|---|---|
| Separate position from identity | Every identity rotated through all four positions | PSR, ISR, PFR | Position and identity remain confounded |
| Test candidate-position primacy | Candidate answer-list order is the only intervention | Position-conditioned choice and score shifts | No causal position evidence |
| Keep evidence order fixed | Candidate-name records remain canonical | Prompt diff audit | Candidate order confounded with evidence order |
| Test complexity × primacy | EASY/MID/HARD frozen conditions | PSR1/PFR/Delta by difficulty | Interaction cannot be assessed |
| Preserve prior frontier evidence | Reuse D3B0 and D4B2 graphs | Counterbalanced frontier diagnostics | Frontier disappears under order control |
| Preserve traceability | Same frozen candidate/downstream mappings | Mapping audit | Cannot reconnect to v3.5 |
| Avoid format confounds | Same F/C/L channels | C validity, FCA, LCA | Output interface contaminates result |
| Avoid post-hoc case selection | Six cases frozen before run | Manifest hashes | Cherry-picking risk |
| Keep causal claim narrow | Only candidate-list order manipulated | No evidence-order manipulation | Cannot infer general sequence primacy |
| Keep calibration scope | No downstream continuation | NPR absent | Premature propagation claim |

After inference append whether each intention was achieved.

## 19. Gate for next step

v3.4.3 does not automatically authorize v3.5.

A clean v3.5 recommendation is allowed only under one of two routes.

### Route 1 — Position effect small

- no strong PSR_1 elevation
- low PFR
- frontier-like behavior survives permutation

Then future v3.5 must still counterbalance candidate order.

### Route 2 — Position effect real but controllable

- position effect clearly identified
- counterbalancing removes pooled bias
- frontier behavior remains after counterbalancing

Then v3.5 must include balanced/randomized order by design.

If position dominates so strongly that frontier behavior disappears:

v3.5_authorized = false

## 20. Stop conditions

Stop and inspect if:

- graph content differs across permutations
- candidate-name evidence record order changes
- gold identity changes
- any candidate fails to occupy every position once
- constrained-choice mapping no longer matches rendered candidate list
- F/C divergence becomes unexpectedly large
- L scorer uses a different prompt/order
- original v3.4.2 graph cannot be reproduced

## 21. Required artifacts

Create:

```text
results/calibration_v3_4_3/
```

with:

- design_audit.md
- case_manifest.json
- permutation_plan.json
- prompt_diff_audit.md
- free_generation.jsonl
- constrained_choice.jsonl
- candidate_likelihoods.jsonl
- inspection.md
- diagnosis.md
- metrics.json
- position_effects.json
- frontier_salvage.md
- gate.json
- manifest.json

## 22. inspection.md

For every case × difficulty:

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|

Show classification and concise interpretation.

Give special attention to dev-04, dev-07, dev-05.

## 23. diagnosis.md

Answer explicitly:

1. Does candidate position causally affect selection?
2. Is position 1 privileged?
3. Were v3.4.2 errors mostly position-driven or identity/case-driven?
4. What happens to dev-04 and dev-07 when their original position-1 candidates move?
5. Does dev-05 retain its boundary crossing across permutations?
6. Do always-easy controls remain stable?
7. Does candidate-position sensitivity increase with difficulty?
8. Does the same identity receive higher likelihood at position 1?
9. Do D3B0 and D4B2 remain plausible frontier regimes after counterbalancing?
10. What exact candidate-order policy should v3.5 use?

## 24. Language restrictions

Allowed:

- candidate-position effect
- position-1 preference
- behavioral primacy tendency
- order-sensitive selection
- consistent with primacy

Do not claim:

- the model internally attends more to the first option
- the model has a cognitive primacy mechanism
- the same internal mechanism caused v3.3 evidence-order effects

without separate evidence.

## 25. Final interpretation target

v3.4.3 should distinguish:

error follows position

from:

error follows identity

from:

error emerges only under higher reasoning complexity

The main target is a causal diagnosis of why v3.4.2 produced 34/38 wrong selections at position 1.
