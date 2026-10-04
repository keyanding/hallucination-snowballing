# v3.4.3 pre-inference design audit

| Design intention | Experimental feature | Observable check | Failure meaning |
|---|---|---|---|
| Separate position from identity | Four fixed cyclic rotations per case-condition | 72 plans; every identity at each position once | Identity and position remain confounded |
| Test candidate-position primacy | Replace only explicit four-line candidate list | PSR, GPA, paired identity Delta, choice changes | No causal candidate-list-order evidence |
| Keep evidence order fixed | Original v3.4.2 name and graph records kept byte-identical | Fixed suffix hashes and all 54 prompt diffs | Evidence order is confounded |
| Test complexity x primacy | EASY D1B0, MID D3B0, HARD D4B2 | PSR1/PFR/Delta separately on six paired cases | Interaction cannot be assessed |
| Preserve prior frontier evidence | Original graphs and exact P1 rendering | All 18 P1 prompts reproduce; compare new P1 calls diagnostically | Original result not reproduced |
| Preserve traceability | Same four candidates and downstream mappings per case | 24/24 mapping records audited | Cannot reconnect to future propagation |
| Avoid format confounds | Unchanged F96/C exact trie/L same-template scoring | C validity, FCA, LCA; all candidate terminals reachable | Interface contamination |
| Avoid post-hoc selection | Six specified cases frozen; 72 new calls | Manifest/code/data hashes; no replacements | Cherry-picking risk |
| Keep causal claim narrow | Only answer-option list changes | No evidence-order change; no internal-mechanism claim | Cannot infer general sequence primacy |
| Keep calibration scope | No downstream continuation | Propagation metrics absent | Premature propagation claim |

## Preregistered definitions

```json
{
  "permutations": "P1 original, P2 left-rotate one, P3 left-rotate two, P4 left-rotate three",
  "repeated_unit": "case x difficulty (18 sets), nested within six deliberately selected cases; never 72 independent observations",
  "PFR": "Spec-literal event over P1->P2, P2->P3, P3->P4 (no wrap): old position-1 identity leaves position 1 and new position-1 identity is selected. Denominator: all 3 adjacent comparisons per set.",
  "strict_PFR": "Additionally require old position-1 identity was selected before rotation, and selected identity changes. Report per all transitions and conditional on previous position-1 selection.",
  "classification": "Gold 4/4 > same wrong identity 4/4 > position1 >=3/4 with >=2 identities > mixed when both maximum identity and maximum position counts <=2 > unstable other",
  "likelihood_aggregation": "Compute Delta for each identity within each set; average four identity Deltas within set, then mean/median those set means. Also report identity-level median diagnostically.",
  "near_boundary_nats_per_token": 0.75,
  "strong_position": "Descriptive flag A: PSR1>=0.40, >=3 POSITION_1_LOCKED sets, mean Delta1>0, and >=6 order-sensitive sets.",
  "strong_identity": "Descriptive flag B: mean ISR>=0.875, >=3 IDENTITY_LOCKED sets, literal PFR<=0.25, and <3 POSITION_1_LOCKED sets.",
  "difficulty_interaction": "Descriptive flag C: EASY PSR1<=0.35 and MID or HARD PSR1 is >=0.15 higher; OR EASY mean Delta1<=0.10 and MID/HARD mean Delta1 is >=0.15 higher and positive.",
  "neither": "Descriptive flag D: mean ISR<=0.625, literal PFR<=0.35, all PSR within 0.15 of 0.25. Flags are not significance tests; A and C can coexist.",
  "frontier_salvage": "Per-case error proportion, median margin, near-boundary fraction across four orders; aggregate six cases equally. Heuristic only: mean error 20-50%, median of case median margins -1..1.5, mean near-boundary fraction>=0.375 (prior dev proportional cutoff). Not a replacement clean split.",
  "route1": "Diagnostic only: PSR1<=0.35, literal PFR<=0.35, strict conditional PFR<=0.25 (or no opportunities), and some frontier heuristic survives.",
  "route2": "Diagnostic only: choices change in >=3 sets with positive mean Delta1, all pooled PSR within 0.10 of 0.25, and some frontier heuristic survives. If not met, do not claim counterbalancing removed the effect.",
  "next_step": "Never automatically authorize v3.5 from these selected six cases. Any supported route still needs a new clean development/confirmation split and balanced order.",
  "divergence_stop": "After each completed 24-prompt difficulty block, stop if >=12 strict F outputs and FCA<0.80. Structural/channel mismatches stop immediately.",
  "order_of_execution": "EASY then MID then HARD; six cases in spec order; P1 through P4. All 72 calls are new; prior P1 outputs are comparison only."
}
```

PFR is reported both literally and with strict previous-selection/change requirements. Identity-locked choices can sometimes select the new first option without following position, so the literal rate alone is not evidence of primacy. All 18 sets and six cases remain visible; no permutation test or independent-prompt p-value is planned. Quantitative descriptive flags operationalize unspecified words such as strong/high; they are not significance thresholds. A causal effect here means an output change under the controlled list intervention, not a claim about internal attention or the v3.3 evidence-order mechanism.

## Post-run achievement table

| Design intention | Observed achievement |
|---|---|
| Separate position/identity | 18 sets; all rotations verified; mean ISR=0.722 |
| Test list-position effect | 11/18 choice-sensitive sets; PSR1=37/72 (51.4%) |
| Fixed evidence order | All fixed prefix/suffix hashes and graph audits passed |
| Complexity interaction | EASY/MID/HARD paired summaries reported; no independent-prompt inference |
| Prior frontier | 18 exact P1 input replications and per-case counterbalanced salvage summaries |
| Traceability | 24 frozen mappings rechecked |
| Format controls | C validity=72/72 (100.0%); FCA=68/68 (100.0%); LCA=72/72 (100.0%) |
| Frozen case selection | All six specified cases completed; no additions or replacements |
| Narrow causal scope | Only candidate-list order changed; no internal-mechanism claim |
| Calibration only | Zero downstream calls; no automatic v3.5 authorization |
