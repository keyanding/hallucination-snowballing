# v3.4 diagnosis

The smoke **fails its measurement gate and stops after the twenty first-hop calls**. There are eleven correct candidate-name answers, zero traceable wrong-candidate answers, zero parseable out-of-set names, and nine invalid outputs. All nine invalid outputs are explanations truncated at the fixed 32-token cap. Thus only 11/20 first hops are valid (required ≥15), and traceable error yield is 0/20 (required ≥5).

No direct lookup or downstream branch was run after this stop. **NPR, NRR, CCS, CWP, SCS, S0 and CLA are unmeasured/null, not zero.** The required branch_trajectories.jsonl is intentionally empty and inspection marks all downstream branches NOT RUN. There were no retries, longer generations, extraction of names from explanations, changed candidates, relaxed criteria or replacement cases.

| First-hop measurement | Count | Rate over all 20 |
|---|---:|---:|
| IFHA / CORRECT_FIRST_HOP | 11/20 | 55% |
| TNER / TRACEABLE_WRONG_CANDIDATE | 0/20 | 0% |
| OSER / parseable OUT_OF_SET_ENTITY | 0/20 | 0% |
| INVALID_OUTPUT | 9/20 | 45% |

OSER follows the preregistered mutually exclusive classification: malformed/truncated answers are reported separately from parseable out-of-set entities. OSER = 0% therefore does **not** mean every response selected a candidate. Among the eleven valid selections, all are correct; the primary IFHA denominator remains twenty, not eleven.

## Design and evidence audit

The frozen universe contains twenty unique film questions sharing eight gold directors, with three birth-place, eight father and nine death-place cases. Every case has exactly four real director candidates and four distinct downstream targets with disjoint frozen aliases. Alternatives have documented films within thirty years of the target film. Gold positions are balanced five per slot, and evidence/candidate order and W0 replacements were fixed with seed 42.

The first-hop task combines a same-director link between A and a separate film Y with four bridge-film/director facts. Every candidate appears in one of those four facts, so finding the only person mentioned is insufficient. The direct A→B statement is absent from the prompt. The shared-director link is a transparent derivation from two explicit source claims, with both source sentences preserved. All 200 source references were verified against the frozen dev.json before inference, including the downstream mappings. This addresses the *availability* of mappings for in-set selections, but does not guarantee the model will produce wrong in-set selections.

## Invalid-output review

Invalid cases are universe-03, 05, 08, 13, 15, 16, 17, 19 and 20. Each generated an explanatory chain rather than a single candidate name and reached 32 tokens without normal completion. For example, universe-13 explains the shared-director link and mentions Gu Changwei at the end; it remains invalid under the frozen output contract and truncation rule. It is not silently counted as a correct name-only response. Other cases end midway through a name or sentence. None can be used as an exact selected wrong-candidate checkpoint.

The eleven complete name-only responses all select the gold candidate. This is consistent with the composition task being easy for the model when it follows the output contract, but the 45% format/truncation failure means the run cannot cleanly distinguish task easiness from output-protocol instability across all twenty cases. It would be incorrect to report 100% first-hop accuracy for the full set or claim that nine valid wrong intermediate states occurred.

## Answers to the nine specified questions

1. **Did the candidate universe increase traceable natural-error yield?** No observed increase: v3.4 produced zero traceable wrong selections, while v3.3 had zero eligible natural wrong-state continuations because of missing downstream evidence. The bottleneck is different: mappings are now frozen for every allowed candidate, but this run yields no usable naturally selected wrong candidate. Structural traceability improved; empirical natural-error yield did not.

2. **How often was a wrong registered candidate selected?** 0/20 (TNER 0%). Eleven cases select the correct candidate; nine outputs are invalid. No invalid answer is relabeled as a wrong candidate or coerced into the set.

3. **What is NPR?** Unavailable: numerator and denominator are both zero, and no N0 calls were authorized after the first-hop stop. This does not show absence of natural propagation.

4. **How often did natural errors recover to C?** NRR is unavailable for the same reason. No natural wrong branch reached the continuation phase.

5. **Did counterfactual correction switch the answer to C?** CCS and SCS are unavailable. The implementation and unit tests cover answer-span-only replacement, exact checkpoint replay, duplicate logical branches and causal-switch counting, but mock tests are not empirical model evidence. No C0/W0 calls were run in this smoke.

6. **Did stripped context change propagation?** Unmeasured. S0 is defined only for eligible traceable natural errors, of which there are none. ΔNPR_prefix is null.

7. **Could lookup failure explain the result?** Lookup ability was not measured in this run: CLA is null because the predeclared first-hop gate stopped execution before the eighty control calls. The observed stopping reasons are output-format reliability and zero traceable wrong selections, not an observed lookup failure. Earlier experiments' lookup accuracy must not be substituted for v3.4's missing controls.

8. **Did any case leave the candidate universe?** No parseable out-of-set name was returned (OSER 0/20), but nine responses failed the single-name output contract. This distinction matters: membership is not established for those invalid explanations. The original text and truncation flags are preserved in [inspection](inspection.md) and first_hop_generations.jsonl.

9. **Is the design ready for a larger pilot?** No. Both the minimum valid-first-hop count and the mandatory natural-error yield fail. A later, separately frozen revision should first establish reliable first-hop output formatting on a separate calibration set, then evaluate whether a truth-preserving, inspectable composition task yields enough natural wrong selections. Increasing this sample or selectively rerunning cases would not fix the current failed gate. No revised universe or 50–100-case pilot was launched.

## Verification and scope

Fifty-two unit tests passed before model inference. They cover target collisions, direct-answer leakage, exact candidate matching, low-yield stopping, lookup-collapse stopping, supported-other-target tracing, branch deduplication and causal-switch metrics. [Verification](verification.json) checks frozen data/source/audit hashes, raw first-hop prompts and responses, classification, saved checkpoints, metric/gate recomputation and the absence of calls after the stop. A null downstream replay check correctly indicates no actual downstream experiment occurred.

All **145 prior result artifacts** retain their hashes. The twenty current outputs and failed gate remain unchanged. The repeated gold directors and reused candidate pool limit independence; this is a constrained candidate-universe smoke, not open-ended generation or a population estimate. No new model family, richer context ablation, SHARS/HalluSE integration, expansion or automatic GitHub push was performed.
