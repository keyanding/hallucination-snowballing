# Experiment v3.4.4 — Separating Reasoning Errors from Answer-Option Order Effects

**Status:** Codex implementation spec / calibration and measurement-validity study  
**Repository:** `keyanding/hallucination-snowballing`  
**Model:** Keep the exact pinned Qwen3-4B-Instruct-2507 / NF4 / BF16 / tokenizer / chat template used in v3.4.3.  
**Scope:** First-hop state selection only. **No downstream continuation, no NPR, no SHAR/HalluSE, and no automatic v3.5 launch.**

## 0. Decision the experiment must enable

The v3.4.3 result has established a *behavioral answer-option-order effect on the six selected cases*: 37/72 outputs chose position 1, 11/18 case-condition sets changed candidate identity across rotations, and first-position preference increased across EASY/MID/HARD. Neither an internal attentional mechanism nor a population-wide effect follows from this. In particular, the counterbalanced MID condition remained frontier-like by aggregate error and margin but still had 13/24 choices in position 1.

**Primary research question for v3.4.4:**

> Can a model-selected wrong intermediate state be measured without a single arbitrary candidate-list ordering determining its identity? If so, how different is that answer from the candidate selected in a conventional four-option prompt?

**Secondary question:**

> Does the order effect depend on the *presence of an answer-option list*, or does it persist through the graph evidence and candidate-name records themselves?

We seek a **measurement protocol**, not a prescribed error rate. The 20–40% error frontier is a *later, optional task-calibration objective*; do not chase it by altering this experiment after viewing answers.

## 1. Preregistered falsifiable hypotheses

- **H1 (listed-choice order effect replicates):** Explicit answer-option list rotations cause answer changes and improve scores for candidates displayed first.
- **H2 (remove list ≠ remove all order effects):** A no-answer-list query reduces *answer-option* bias but may still show *name-record/evidence* order sensitivity. This is an empirical question, not an assumption.
- **H3 (complexity interaction):** List-position sensitivity is greater in the hard graph than in the easy graph, measured by paired changes within new cases.
- **H4 (state-robustness):** Some wrong intermediate identities persist across equivalent renderings, while others depend on presentation. The experiment must distinguish these rather than pooling all wrong answers.

Reject a hypothesis if its preregistered observable pattern is absent. Avoid claims about model-internal attention or a shared mechanism with v3.3 evidence-order effects.

## 2. Experimental population, separation, and preregistration

### 2.1 Old-case **diagnostic** reproduction (not used for primary inference)

Use v3.4.3 `dev-04`, `dev-07`, `dev-05`, `dev-01`, `dev-06`, `dev-08`. Freeze EASY=`D1B0`, MID=`D3B0`, HARD=`D4B2`. Preserve previous graph strings and all four real candidates/downstream mappings. This six-case cohort is deliberately selected and **must not be treated as new independent evidence**.

Run a small diagnostic subset: the three v3.4.3 conditions × six cases for new *no-list* interface(s). Existing P1–P4 results can be referenced diagnostically, but do not merge different past-run outputs into newly controlled paired comparisons without an exact rerun.

### 2.2 Fresh development set (primary)

Build **24 new base cases** that have not appeared in v3.4.1–v3.4.3 inference (new graph target IDs and preferably new entity bundles). Reusing a person is permitted only if logged; do not reuse an identical target question or graph from earlier experiments. Preregister seed, exact graph generator, candidate universe and ground truth **before any model call**.

Every case has four real candidate names `{B, B'_1, B'_2, B'_3}`, each with distinct, independently frozen `r2` endpoints for future propagation; those `r2` facts must **not** appear in first-hop prompts. Ensure unique graph-resolvable gold via a separate deterministic parser. Balance gold across the four baseline candidate positions, six cases each. Candidate names should be reviewed for extreme token-length/spelling artifacts. Do not change them after observing model performance.

Use the same underlying case at **EASY=D1B0, MID=D3B0, HARD=D4B2**. Difficulty labels are merely construction settings, **not proof of monotonic difficulty**. Preserve relation labels and semantic target; record graph token counts and all changes.

### 2.3 Untouched confirmation set

Freeze **16 additional disjoint cases** before development inference. Do not query them during development, inspect answers, or retune based on their outputs. Run once only after a single primary interface policy is chosen *from development data*. This set validates measurement robustness, not a 20–40% error estimate with high precision.

## 3. Intervention: three first-hop answer interfaces

All interfaces must use **identical underlying graph facts, graph link order, model configuration, query semantics, and gold** for a matched case/difficulty. Different interface headings/instructions are unavoidable; store exact diffs and describe them as part of the intervention. Never describe a prompt change as 'only order' unless it literally is.

### Interface L — Four-option listed choice (positive-control condition)

Replicate the verified v3.4.3 prompt contract, including a clearly displayed four-name candidate list. For each case × difficulty, generate **four cyclic rotations** from a seeded, preregistered base order: P1–P4. Each identity occurs once in positions 1–4.

Keep candidate **name records and all graph records in a canonical fixed order** across these four rotations. Only the answer-option list is rotated. Channel C (candidate-trie constrained choice) is the primary L measurement; also run Channel F (greedy free output) and diagnostic Channel S (candidate sequence log-likelihood). If an implementation must change the original v3.4.3 parser/prompt, document and audit it before proceeding.

### Interface N — No separate candidate answer-option list

Delete the four-item answer-option list entirely. Keep candidate-name mapping records and all graph facts, and ask the same substantive question, e.g. `Which person is reached by following the credited-director links from Film T... ? Output only the person's name.`

The model is **not told an ordered set of four choices**. Use unconstrained free generation as **the primary observation**, with a frozen exact-name/alias parser for in-universe answers and an explicit `OUT_OF_SET`, `AMBIGUOUS`, `NONCOMPLIANT`, `TRUNCATED` breakdown. Do **not** silently coerce an out-of-set answer back to the four choices.

As a *separate labeled diagnostic*, compute likelihood scores for the four frozen candidates and optionally run trie-constrained choice without displaying options. **Never call this diagnostic 'natural free generation'.**

### Interface R — No-list plus name-record-order rotations

Use the same interface N text, but rotate the **candidate-name mapping record block** through four cyclic permutations; keep the graph fact block and query byte-identical. This isolates whether answer changes are sensitive to a *different* ordering source even after the answer-option list is removed.

The answer is again **unconstrained free generation** with strict in-set/out-of-set parsing. For consistency, use the same four rotations of names over record positions; keep record IDs, names, and graph references paired as identical statements, moving only complete record lines. Audit that the graph's unique gold endpoint remains unchanged.

R is **not** a manipulation of answer-option order, and must be analyzed separately from L.

## 4. Outputs and exact call budget

**Fresh development (24 cases × 3 difficulty levels):**

- L: 4 list rotations × 72 case-level cells = **288 prompts**, each with F, C, and S.
- N: 1 canonical record ordering × 72 = **72 prompts**, F primary, candidate score diagnostic, guided-choice optional.
- R: 4 name-record rotations × 72 = **288 prompts**, F primary, candidate score diagnostic, guided-choice optional.

**Fresh confirmation (16 cases):** Evaluate **one preregistered difficulty** and **one selected primary interface policy**, but include a minimal matched reference:
- chosen difficulty, L with all four list rotations, and N with canonical name-record order: **80 distinct prompts** (16 × (4+1));
- if the selected policy depends on R, run the four R rotations too: **64 more prompts**.

**Old selected-case diagnostics:** Six old cases × three difficulty settings × N canonical + R rotations = **90 prompt renderings** (can skip R if run budget is tight, but mark R-old cohort incomplete before starting). Report separately.

If compute budget is limited, run **development EASY+MID first** as a *pilot only* with fully preregistered subsetting; do not interpret HARD as absent because it was not run. Never selectively stop after favorable outcomes. Require structural audits before inference; empirical failure should still produce complete predeclared data whenever feasible.

## 5. Parsing, decoding, and score definitions

- Pin deterministic settings and record model/revision, quantization, software versions, exact chat-template bytes, max_new_tokens, and random seed.
- L: use existing constrained trie for channel C, **validity 100%**; use F shadow, max_new_tokens=96 or the exact v3.4.3 parameter. Preserve the raw text, do not conflate a partial first line with a compliant final answer.
- N and R: unconstrained greedy generation, with a **documented token cap chosen in a format smoke check independent of experiment items**. Preserve full raw text and stop reason. Strict valid = *only* one candidate name or unambiguous registered alias with no explanation; also separately record an extractable candidate inside noncompliant text; never treat extractable as strict-valid for primary analysis.
- When a noncompliant reply begins with an apparent answer followed by `Wait...`, do not call it a completed natural choice. Report separately.
- Require exact alias normalization frozen before inference; no per-output hand edits. `OUT_OF_SET`, `AMBIGUOUS`, `NONCOMPLIANT`, `TRUNCATED`, and `IN_SET_VALID` are mutually exclusive primary categories; attach supplementary extraction tags without changing the primary label.
- Candidate score S: compute raw summed token log-likelihood **and** per-token mean under the same rendered prompt. Record token counts and candidate-specific scores. Mean-normalized scores are diagnostics, not calibrated probabilities and not automatically equivalent to forced-choice distribution. Include sequence-termination/EOS settings. If available report actual normalized four-choice probabilities computed from complete-sequence scores as a sensitivity analysis, clearly labeling the restriction to the candidate set.
- Margin: `score(gold) - max(score(wrong_i))`. Evaluate the **identity-matched position shift** under L and R separately, not a cross-interface margin difference interpreted as pure position effect.
- For N/R, the denominator for `P(wrong | in-set valid)` must be stated; report coverage jointly to avoid selection bias. Also report a *per-all-prompts* wrong-in-set rate, with other outcome categories displayed (not silently treated as correct).

## 6. Preregistered primary estimands

### 6.1 Listed-choice order sensitivity

For each case/difficulty `u`, collect L's four constrained outputs. Record:

- `L_position1_rate`: fraction choosing currently listed first, with 25% descriptive equal-exposure reference.
- `L_order_robust_correct`: all 4 positions yield gold.
- `L_order_robust_wrong_same_identity`: all 4 positions yield the **same non-gold identity**.
- `L_order_sensitive`: more than one selected identity across four rotations.
- `L_any_wrong` and `L_wrong_fraction` (0/4 to 4/4).

**Do not define 'order-robust wrong' as a wrong majority by itself.** A 3/4 modal wrong identity is *partial robustness* and should be labeled separately.

### 6.2 No-list natural answer measurement

For N, compute:

- `N_strict_valid_coverage` and each invalid/out-of-set category;
- `N_gold_rate_over_all`, `N_wrong_in_set_rate_over_all`;
- `N_wrong_given_valid_in_set` with denominator;
- matched identity agreement of N with L's modal identity, **treat L ties explicitly**;
- `N_vs_L_disagreement` and which direction any shift takes.

The central test is whether N yields **traceable wrong first-hop answers without presenting an arbitrary ordered candidate list**. N itself can still contain record-order effects; it is not assumed order-invariant.

### 6.3 Record-order sensitivity

For each case/difficulty `u`, obtain four unconstrained outputs under R. Record:

- `R_identity_stable_4of4`, `R_order_sensitive`, `R_position1_of_record_rate` (only among strict in-set-valid outputs);
- `R_valid_coverage` per rotation and jointly;
- whether the N canonical answer is stable across R rotations;
- whether errors track the *earliest candidate-name record* rather than a displayed answer option.

R and N are **not exchangeable** with L; diagnose effects of list layout vs evidence record order separately.

### 6.4 Difficulty interaction

Analyze paired EASY, MID, HARD on the same cases. Report per-case trajectories of:

- L order sensitivity / position1 fraction;
- N valid wrong responses;
- R order sensitivity;
- gold margin distribution.

Do not infer monotonicity from the words EASY/MID/HARD alone. Complexity and prompt length covary; report length and graph-depth confounds explicitly.

## 7. Primary interface-policy selection — made only on development

For later first-hop studies, prefer the least restrictive protocol that simultaneously:

1. yields at least **90% strict or unambiguous name-only valid coverage** on the development set, with all invalid/out-of-set rates shown;
2. allows traceable wrong in-set identities without an artificial list (do **not** require a target error rate for v3.4.4);
3. has acceptable stability: for R, ≥75% of case/difficulty cells yield one identical strict in-set identity in at least 3 of 4 orderings (and at least 50% are 4/4 identical); for N alone, require cross-check with R, not just one rendering;
4. does not exhibit a dominant candidate-name-record-first effect (diagnose if ≥40% of strict in-set R responses select the earliest name record; investigate before approval; not an automatic causal test);
5. has ≥85% agreement between strict-valid N outputs and a **predeclared order-aggregate** from L in the relevant evaluation stratum, with ties handled as missing rather than forced votes.

**Important:** These numeric criteria are engineering acceptance heuristics, not evidence that the model has no residual order bias. Confirm on new cases; do not loosen them after observing outputs. Report uncertainty intervals at the **case** level (bootstrap over cases only, if used), not over 4 correlated rotations as if independent.

Possible outcomes:

- **Route N:** Free generation without answer options is sufficiently valid and record-order stable. Recommend as primary natural first-hop elicitation; retain constrained/listed probes as diagnostics only.
- **Route R:** Free generation remains order-sensitive but a *precommitted multi-rendering aggregation* provides a stable measurement. Label the aggregated construct *order-robust state estimate*, **not a single naturally generated state**.
- **Route L:** Neither no-list protocol is reliable, but constrained choice remains valid. Retain L strictly as **forced-choice candidate-selection research**, not spontaneous hallucination research.
- **No route:** Interfaces disagree, invalid rates are high, or selection is driven by ordering. Do not proceed to propagation; report measurement failure and alternatives.

For Route R aggregation, define in advance: choose identity only if ≥3/4 of **strict-valid** rotations name the same candidate **and all four rotations are strict-valid**. Otherwise `UNSTABLE_OR_UNRESOLVED`; do not pick the plurality after reviewing results. If the chosen identity is wrong, tag as `AGGREGATED_TRACEABLE_WRONG`, never `SINGLE_TRAJECTORY_NATURAL_WRONG`.

## 8. Confirmation stage and launch gate

At the end of development, freeze the selected **single** primary policy, frozen generator, and a single selected difficulty. Selection is on measured *interface quality / validity*, not simply the cell with most errors. Then run the 16 untouched confirmation cases once.

A recommendation for a **new v3.5 design** is allowed only if:

- exact run provenance and graph uniqueness audits pass;
- all first-hop candidate→`r2` mappings are frozen and distinct;
- primary policy meets the same development acceptance checks on confirmation where measurable;
- repeated presentation effects are explicitly quantified and not ignored;
- the report distinguishes *natural single-output wrong*, *forced-choice wrong*, and *aggregated wrong*;
- no inference about natural snowballing or propagation is made from first-hop-only results.

Regardless of results, `v3.5_executed=false`. Recommendation does not itself launch v3.5. If confirmation N produces too few traceable wrong cases, say *interface usable but error-yield insufficient* and plan a new difficulty-calibration sample instead of post-hoc retuning confirmation data.

## 9. Design-intent → implementation → observable check (required)

Before inference, Codex must populate `design_audit.md` with **actual prompts / hashes**, not generic intentions:

| Design intention | Implemented intervention | Pre-run validity check | Observable outcome | What would falsify it / limit interpretation |
|---|---|---|---|---|
| Separate option-order artifact from semantic errors | L P1–P4, fixed graph and name records | Diff permits *only answer-option lines* to move | L first-position selection and within-case choice changes | Names/graph changed; no effect on new cases |
| Avoid forced option list in primary natural elicitation | N omits list; unconstrained F | Check no ordered answer-options leaked | N in-set wrong/coverage + agreement | High invalid/out-of-set; no traceable wrong |
| Avoid assuming no-list means no order effect | R rotates name-record block independently | Graph block and candidate-ID pairings unchanged | R order sensitivity and record-first preference | Name-record rotation mutates facts |
| Keep output formatting distinct from semantics | Strict parser + separate invalid taxonomy | Parser unit tests on valid, explanation, truncated, alias and multiple-name cases | Coverage + semantic correctness conditional on validity | Extracted partial answer silently counted valid |
| Isolate identity from absolute position | Four rotations for L/R per cell | Each identity occupies each position exactly once | Identity stability and position-conditioned likelihood shifts | Rotations incomplete |
| Check complexity × order effects | EASY/MID/HARD on matched new cases | Same query/candidates; controlled graph builder | Within-case paired trajectories | Uncontrolled evidence changes or token-length confounds |
| Prevent selected-case overfitting | 24 fresh development + 16 untouched confirmation cases | Verify disjoint targets and frozen seed | One-shot confirmation of chosen policy | Confirmation leaks or iterative retuning |
| Preserve future propagation traceability | 4 real candidate identities, distinct `r2` mappings | Mapping coverage and uniqueness 100% | Wrong in-set identities have frozen downstream target | Missing mappings or misleading aliases |
| Guard against L-score overinterpretation | Record sum/mean/token counts and channel differences | Verify exact same rendered prompt/tokenization | Channel agreement/disagreement and margins | Treat mean logprob as calibrated probability |
| Make outcome interpretable even if gate fails | Full invalid breakdown, per-case audit and predefined no-route outcome | Required file audit before launch | Which interface did/did not work, why | Only one scalar pass/fail reported |

After running, append a second table with `achieved?`, numerical evidence, and limitations for every row. A positive result may not be asserted without a corresponding observation; a negative result must be reported honestly.

## 10. Negative controls and implementation tests

Before model calls, run and log:

1. **Graph resolver:** All planned graphs have exactly one valid queried endpoint and no cycles; include original and permuted prompts.
2. **Prompt diff:** L rotations affect only explicit candidate-list ordering; R rotations affect only complete name-record line ordering; all graph links and semantic candidate-name pairs preserved. N differs from L only through intentional removal of list / necessary instructions (document exact diff).
3. **Counterbalance:** Each candidate identity occupies positions 1–4 exactly once within each L/R cell. Check equality with hashes/IDs, not only visual inspection.
4. **Alias parser tests:** Full name, approved alias, out-of-set person, explanation followed by a name, multiple names, incomplete token truncation, `Wait...` after a name. Include an explicit noncompliant class.
5. **Constrained trie sanity:** Every registered candidate is reachable; no other terminal; EOS behavior tested; repeated v3.4.3 prompt reproduces outputs on a small frozen harness test (not counted toward confirmation).
6. **Candidate scoring check:** Verify candidate-token alignment, name-length variation, EOS inclusion/exclusion; raw-score vs length-normalized ranking recorded and differences highlighted.
7. **No leakage:** Downstream `r2` destinations never appear in first-hop prompts; no solution labels or 'gold/wrong' text appears.
8. **Source provenance:** All real person→`r2` mappings audited; graph targets explicitly labeled **synthetic**, never falsely described as factual film credits.

If any structural condition fails, **STOP BEFORE INFERENCE**, fix, regenerate hashes, and document change. Do not patch predeclared examples after seeing outcomes.

## 11. Reporting and required files

Write results under `results/calibration_v3_4_4/`:

- `README.md` — intent, data split, exact call counts, scope, key findings
- `design_audit.md` — pre/post design-intent mapping and checks
- `manifest.json` — git commit, seed, model, pinned environment, prompt/code/data hashes, timestamp
- `case_manifest.json`, `development_cases.json`, `confirmation_cases.json`
- `prompt_plan.jsonl`, `prompt_diff_audit.md`
- `listed_choice_F.jsonl`, `listed_choice_C.jsonl`, `listed_choice_scores.jsonl`
- `no_list_free.jsonl`, `no_list_scores.jsonl`
- `record_rotation_free.jsonl`, `record_rotation_scores.jsonl`
- `metrics.json`, `interface_policy.md`, `gate.json`
- `inspection.md` — compact paired tables for every case/difficulty; include raw outputs only for diagnostic anomalies; avoid hundreds of verbose duplicated rows
- `diagnosis.md` — numbered answers to the questions below
- `CHANGELOG.md` — what changed from v3.4.3 and why

In `inspection.md`, use two compact views:

**Within-case L rotations:** candidate at position 1, chosen identity, valid status, margin, order-robust identity classification.

**Matched N/R comparison:** N raw/parsed identity + validity; R four parsed identities + validity; L modal identity (ties explicit); diagnosis of list-vs-record sensitivity.

`diagnosis.md` must answer:

1. Does the v3.4.3 first-option preference replicate on *new* cases?
2. What happens to the wrong-first-hop rate when the explicit option list is removed?
3. Does name-record order create its own selection bias?
4. Which wrong identities are stable across presentation changes, versus order-induced?
5. Is difficulty associated with larger interface sensitivity? Is this consistent across cases?
6. What proportion of natural outputs are valid, out-of-set, ambiguous, explanatory, or truncated?
7. When do free, constrained, and likelihood channels disagree, and why?
8. Does any policy pass the preregistered engineering gate on untouched confirmation cases?
9. Which, if any, future claim is licensed: forced-choice selection, order-aggregated state, or natural single-trajectory first-hop error?
10. What precisely remains unresolved before studying downstream propagation?

## 12. Stop conditions and interpretation restrictions

**Stop immediately** if graph uniqueness, counterbalancing, mapping, prompt-diff, parser, or constrained-output structural checks fail. **Finish the frozen dataset** for empirical disappointments unless compute limitation was declared in advance. Do not tune on confirmation set or relabel invalid outputs after inspection.

Avoid: “the model internally attends to position 1,” “same mechanism as v3.3 primacy,” “natural hallucination rate of 30%,” or “error propagation was demonstrated.”

Use: “behavioral answer-option-order effect,” “name-record-order effect,” “in-universe candidate selection error,” “natural free-generation error, conditional on parseability,” and “order-aggregated state estimate.”

**Success is a defensible measurement choice, including an evidence-based decision that no current interface is adequate.**
