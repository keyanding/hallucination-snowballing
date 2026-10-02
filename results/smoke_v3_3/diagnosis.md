# v3.3 diagnosis

The **counterfactual branching measurement gate passes**, with all twelve branch matrices valid, 24/24 direct lookups correct, and 0/132 unsupported or invalid state outputs. All 168 actual model calls completed: 12 first hops, 24 direct lookups and 132 counterfactual state probes. **Natural propagation remains unmeasured: NPR is null, with denominator 0.** No eligible natural B0 continuation was executed.

All twelve naturally generated first-hop names differ from the frozen gold names and registered alternatives. None has an explicit, acceptable downstream mapping in the frozen evidence available for this experiment. Under the user's approved case-level stopping rule, their natural-error branches were stopped and the preregistered alternative used only for counterfactual analysis. No first-hop outputs, cases, aliases or prompts were repaired or rerun.

## Natural first-hop yield and eligibility

| Case | Gold intermediate | Natural raw answer | Downstream evidence decision |
|---|---|---|---|
| 01 | Feng Xiaoning | Wang Xiaoshuai | Shanghai occurs in a film title, not a birthplace statement |
| 02 | Helmut Käutner | Andreas Dresen | Director identity mentioned; no birthplace evidence |
| 03 | Jerome Storm | Samiyeh M. A. Al-Sayed | Entity identity and mapping unverified in frozen source |
| 04 | Rodrigo Grande | John Landis | Filmmaker identity mentioned; no birthplace evidence |
| 05 | Yuen Woo-ping | James Marsh | Director identity mentioned; no father evidence |
| 06 | Ildikó Enyedi | Sofia Coppola | Identity mentioned; no explicit father statement |
| 07 | Tinnu Anand | Amit Sharma | Entity identity and mapping unverified in frozen source |
| 08 | Vojtěch Jasný | Tomasz Kowalczyk | Entity identity and mapping unverified in frozen source |
| 09 | Marcello Fondato | Yves Boisset | Director identity mentioned; no death-place evidence |
| 10 | León Klimovsky | Robert F. McGowan | Biography has dates, but no death place |
| 11 | Jan Svěrák | Peter Weir | Director identity mentioned; no father evidence |
| 12 | Walter Hugo Khouri | Jean Renoir | Identity mentioned; relatives' biographical places are not his death place |

All twelve responses are parseable short names, so UNKNOWN_OR_INVALID = 0/12. NFER is **12/12 = 100% non-gold first-hop answers** on this selected smoke set. Nine returned identities are independently named in the frozen source; three remain unverified there. Do not describe all twelve as verified real entities or infer that unverified names necessarily denote invented people.

The raw automatic `entity_identity_verified` flag, and the derived automatic `verified_wrong_entity_rate` of 1/12, refer narrowly to matching the prebuilt relation index. Manual full-source review confirms nine identities but **zero required downstream relations**. The separate [review record](review.json) reports that distinction without modifying raw Phase-A fields. The film-title false positive for Wang Xiaoshuai is why a triple plus target-string match was insufficient. All evidence hits and source coordinates are saved in [natural evidence search](natural_evidence_search.json), with decisions in [eligibility review](eligibility_review.json).

## Counterfactual branch results

Every number below uses the same twelve complete, direct-correct cases. All active wrong states are **registered counterfactuals**, not the naturally generated names. E0 still includes explicit downstream facts; only added first-hop evidence is absent.

| Evidence condition | CPR: wrong state → C′ | OR: wrong state → C | GSA: gold state → C | Gold state → C′ |
|---|---:|---:|---:|---:|
| E0 no first-hop evidence | 11/12 (91.7%) | 1/12 (8.3%) | 12/12 (100%) | 0/12 |
| E1 gold support | 0/12 (0%) | 12/12 (100%) | 12/12 (100%) | 0/12 |
| E2 wrong support | 12/12 (100%) | 0/12 | 1/12 (8.3%) | 11/12 (91.7%) |
| E3a gold then wrong | 4/12 (33.3%) | 8/12 (66.7%) | 12/12 (100%) | 0/12 |
| E3b wrong then gold | 12/12 (100%) | 0/12 | 7/12 (58.3%) | 5/12 (41.7%) |

S0 propagation is 12/12. ΔPR_prefix = 11/12 − 12/12 = **−8.3 percentage points**. Symmetry diagnostics are OR(E1) = 12/12 and P(C′ | gold state, E2) = 11/12; no single pooled symmetry scalar is used.

## Answers to the nine specified questions

1. **How often is the natural first hop wrong?** All twelve answers fail the frozen gold-name check (NFER 100%). All are syntactically valid; nine have source-backed entity identities and three have unresolved identities. This is a descriptive rate on selected difficult questions, not a population estimate. The prior ten cases were retained from earlier experiments and two additions were reviewed before v3.3 inference; the sample was not chosen from a sweep of v3.3 outputs.

2. **How often does a natural wrong state propagate?** This cannot be estimated. No natural wrong entity had explicit eligible downstream evidence, so NPR = null (0 eligible cases), not 0%. Natural B0 and natural-origin B2/E0 were not run. Every downstream wrong-state row is tagged `registered_counterfactual`. The absence of an eligible natural branch is the main scientific limitation of this run.

3. **Does the same wrong state propagate differently with the prefix?** For the registered alternatives, E0 is 11/12 versus S0 12/12. In natural-09, the registered James Goldstone state produces San Felice Circeo (the gold Marcello Fondato target) under the replayed task transcript, but Shaftsbury, Vermont under S0. The other eleven remain PROPAGATE. This is consistent with prefix/framing sensitivity in one case. Both the task transcript and chat-role framing differ from S0; the comparison does not isolate one phrase. It says nothing directly about the unmeasured naturally generated Yves Boisset state.

4. **Does gold evidence suppress propagation?** Yes for the counterfactual branches: E1 changes the eleven E0 propagations to gold overrides and retains the existing natural-09 override, producing 12/12 overrides. Gold-state controls remain 12/12 exact. The effect is context-supported selection, not evidence that the model detects an internally generated error or repairs a belief.

5. **Does wrong-state support stabilize propagation?** E2 gives 12/12 propagation, restoring the one E0 override. It also moves 11/12 gold-state controls to C′. Natural-03 is the exception: its gold-state branch still returns Denver despite the alternative-director evidence. The mirror effect shows that context support can shift answers in either direction; high wrong-state propagation here does not establish stable reliance on the supplied state.

6. **Does conflict restore control to the state?** Only partially, and order matters in this run. E3a wrong-state propagation is 4/12; E3b is 12/12. Wrong-state answers change in cases 01, 02, 03, 07, 08, 09, 10 and 11. Gold-state answers change in cases 01, 02, 04, 05 and 12 (12/12 gold under E3a versus 7/12 under E3b). All observed changes favor the target supported by the **first** evidence sentence. This is consistent with a primacy tendency, not a recency effect or a universal rule: several cases keep following the state in both orders. Eight wrong-state pairs and five gold-state pairs are repeated observations of the same twelve cases, not independent samples.

7. **Could lookup failure explain the changes?** The shared downstream facts are independently accessible: CLA_B = 12/12, CLA_B_prime = 12/12. There are no failed lookup cases to exclude. Every state response equals one of its own two supplied targets; no unsupported, invalid, UNKNOWN or refusal outputs occurred downstream. These controls separate the observed target-selection changes from minimal direct-lookup failure, but do not establish reliability for other facts or prompts.

8. **State-selective support or general interference?** E1 has 12/12 coherent support-selective pairs: both states return the gold-supported target. E2 has 11/12 coherent mirror pairs: both states return the alternative-supported target; one pair continues to follow its state. No pair becomes unsupported or invalid in both branches, so there is no observed GENERAL_INTERFERENCE under the preregistered diagnostic. E0 and conflict conditions are reported as stable state following or other supported selection rather than artificially forced into a support-versus-interference binary. E2's low GSA is therefore a scientific symmetry result, not an automatic gate failure.

9. **Do natural errors resemble the controlled errors from v3–v3.2?** The run cannot answer that comparison: no eligible natural wrong-state continuation exists. The new **counterfactual** results retain the directional evidence/mirror pattern, but conflict behavior differs from v3.2's order-insensitive state following. Different chat framing, simpler first-hop evidence wording and the expanded twelve-case set prevent attributing that difference to a single ingredient. The intended bridge to natural downstream hallucination has not yet been established.

## Design limits, checks and endpoint

Phase A is a first-hop-only elicitation, not unrestricted multi-step generation. The natural generated prefix contains one short answer and no explanation. For all executed branches, replacing that answer removes the only model-generated text before continuation; the unchanged earlier text is the original task and first-hop instruction. The experiment therefore validates matched replay/intervention mechanics and measures task-transcript counterfactual behavior, while providing no observed natural-error transition.

The downstream fact block is added after the saved checkpoint in every branch. Even an eligible B0 would measure evidence-assisted continuation rather than an uninterrupted closed-book trajectory. The twelve cases are a small fixed convenience sample; the two added cases reuse earlier donors. No statistical generality or internal reasoning mechanism is inferred.

Forty-six tests passed before inference. Complete prompts, first-hop checkpoints, raw responses, logical branch labels and individual changes are in [inspection](inspection.md). [Verification](verification.json) checks frozen inputs/source hashes, exact intended message construction, serialized checkpoint replay, independent calls, recomputed metrics and all **116 prior artifacts**. The gate passes for the twelve counterfactual branch matrices and explicitly does not require natural-error yield; it is not evidence that the natural-propagation research objective has been demonstrated.

Work stops after this smoke and review. No new model, resampling of candidates, SHARS/HalluSE integration, expanded run or automatic GitHub push was performed.
