# v3.2 diagnosis

All 320 planned independent calls completed. The measurement gate **fails**: C5 gold-state adherence is 4/10, and only 4/10 cases satisfy the predefined cross-C0–C5 interpretability rule (required ≥8/10). The run did not trigger early stopping because only one condition fell below the GSA threshold; the pre-inference rule required two such conditions to stop. No threshold, prompt, case, alias or label was changed after inference.

The user explicitly approved a common H1 backbone for C2–C6, omitting the old H2 sentence. C4 retains the original first-hop evidence but does not reproduce v3.1 H3 verbatim. The frozen plan and all full prompts are in [the audit](context_ablation_audit.md); all actual prompts, answers and per-case changes are in [inspection](inspection.md).

| Context | Direct lookup CLA | Gold-state GSA | Alternative-state PR | Gold override OR |
|---|---:|---:|---:|---:|
| C0 minimal | 20/20 | 10/10 | 10/10 | 0/10 |
| C1 original question | 20/20 | 10/10 | 10/10 | 0/10 |
| C2 neutral length control | 20/20 | 9/10 | 10/10 | 0/10 |
| C3 gold-name cue | 20/20 | 10/10 | 8/10 | 2/10 |
| C4 gold first-hop evidence | 20/20 | 10/10 | 4/10 | 6/10 |
| C5 matched alternative evidence | 20/20 | 4/10 | 10/10 | 0/10 |
| C6a gold then alternative | 20/20 | 10/10 | 10/10 | 0/10 |
| C6b alternative then gold | 20/20 | 10/10 | 10/10 | 0/10 |

All denominators retain the same ten cases. Direct lookup totals 160/160. All 320 answers are short, parseable supplied targets; none are invalid, UNKNOWN, refusals, unsupported answers or unresolved alias mismatches. No semantic relabeling was needed. Conditional SFIR for B is 0%, 0%, 10%, 0%, 0%, 60%, 0%, 0%; for B′ it is 0%, 0%, 0%, 20%, 60%, 0%, 0%, 0% across the displayed conditions. For B′, SFIR includes meaningful evidence-driven override, not a failure to read the reference facts.

## Answers to the seven specified questions

1. **Neutral length:** PR(C2)−PR(C1) = 0 percentage points. There is no observed reduction in alternative-state propagation from this length-matched neutral sentence bank. Nevertheless C2 causes one gold-state error: real-04 returns Rēzekne instead of Rosario. Neutral padding is therefore not behaviorally inert for every branch.

2. **Gold-name mention:** PR(C3)−PR(C2) = −20 points. real-03 and real-05 override to Denver and Yuen Siu-tien, respectively. This is consistent with a gold-name cue changing behavior in some cases without an explicit first-hop assertion. It does not establish a general effect from ten cases or isolate every lexical difference in the filler.

3. **Gold relational evidence:** PR(C4)−PR(C3) = −40 points. C4 overrides in real-01, 02, 03, 04, 08 and 10. Relative to C3, five cases newly override, while real-05 switches back to propagation; real-03 overrides in both. The net effect is therefore not a uniform per-case progression. Explicit evidence produces a larger aggregate shift than the lexical cue here, but C4 also retains original film metadata (year, country, cast where present). This contrast cannot isolate the relation predicate alone. C4 PR is 40%, versus old H3's 20%; the changed backbone/heading means this is not a failed exact replication or an isolated H2 effect.

4. **Matched alternative evidence:** PR(C5)−PR(C4) = +60 points, restoring alternative-state propagation to 10/10. However C5 also causes gold-state failures in real-01, 02, 03, 04, 05 and 10, each returning C′. Thus its context can override either supplied state direction; high PR does not mean robust state following. C4/C5 differ only by substituting B′ for B, with tokenizer length differences of −4 to +4 tokens from the names themselves. C5 is counterfactual task context, not a newly asserted real-world fact.

5. **Conflicting evidence and order:** C6a and C6b both follow the supplied alternative state in 10/10 cases and the supplied gold state in 10/10. There are 0/10 alternative-state order-sensitive pairs; all raw answers also agree across orders for all four probe types. Behavior is consistent with state following when both claims are present, with no observed primacy/recency effect on this set. This does not establish that the model internally detects or resolves a contradiction.

6. **Direct lookup versus state effects:** Every condition has 20/20 exact direct answers, including all cases with state errors or overrides. These observed changes are separable from direct lookup failure in the recorded controls. They remain sensitive to the state-framed question and added task context; flawless lookup does not rescue the failed GSA measurement gate.

7. **Gold-state stability:** It does not remain high across all conditions. C2 reaches the inclusive 90% threshold; C5 reaches only 40%. Only real-06, 07, 08 and 09 remain interpretable across C0–C5 under the frozen rule. No denominator is reduced post hoc, and a four-case subset is not substituted as the primary analysis.

## Scope and endpoint

The pattern is descriptively consistent with explicit first-hop evidence shifting answers more than neutral length or gold-name mention alone. It is **not a fully validated v3.2 assay under the requested gate**, because matched alternative evidence substantially disrupts the gold-state control. The complete failed-gate result is retained for review rather than repaired by rerunning or excluding cases.

These are paired observations of ten fixed cases under one model and decoding setup, not 320 independent research samples. They concern externally supplied states and context-supported answers, not naturally generated hallucinations or inferred internal reasoning. C7 was omitted before inference because a third intermediate lacked a matched downstream fact. No natural-trajectory experiment, model-family expansion, SHARS/HalluSE integration or scale-up was launched.

Validation: 42 unit tests passed before inference; all 95 prior result artifacts retained their hashes. [Verification](verification.json) binds actual prompts, raw responses, frozen source/data/plan, metric recomputation and per-call isolation. The original raw trajectories remain unchanged. Human scientific review is still required before deciding a follow-up design.
