# v3.4.2 pre-inference design audit

| Design intention | Experimental feature | Observable check | Failure meaning |
|---|---|---|---|
| Build a monotonic difficulty axis | Depth 1–4 × branch count 0–2; eight paired dev cases | ER and median gold margin on all 12 cells; 9 depth and 8 branch comparisons | Observed difficulty may not be ordered |
| Separate two sources of difficulty | At fixed depth all paths have equal length; branch count adds whole parallel paths | Factor-specific curves and paired neighboring changes | Cannot attribute difficulty source |
| Preserve traceability | Four real directors per case with distinct frozen targets and aliases | 80/80 mapping records checked against source triples and sentences | Future propagation cannot be measured |
| Avoid candidate-identity confounds | Candidate list, order, name records, and targets fixed across all conditions | Candidate hashes and prompt invariant sections; 2/position dev, 3/position held-out | Difficulty mixed with identity replacement |
| Avoid format confounds | Existing exact trie C; F greedy 96 tokens; one identical rendered prompt | C validity 100%; all candidate terminals reachable; FCA | Interface failure |
| Measure capability boundary | Teacher-forced candidate mean log probability; EOS excluded | Gold margin, NBF using fixed absolute threshold 0.75; sum scores also retained | Errors may be isolated case artifacts |
| Avoid isolated-error selection | Immediate easier neighbor must have strictly lower ER or higher GM | Per-condition local-support table; no new conditions after inference | Selected condition is a spike |
| Prevent overfitting | Eight dev symbolic targets and twelve new held-out targets, sampled seed 342 before inference | At most two conditions, each on all twelve held-out once | Frontier does not replicate |
| Preserve unique answer | Credited path plus equal-depth comparison/associated paths with disjoint nodes | Parse all 240 rendered graphs; exactly one queried endpoint, no cycles | Errors may reflect ambiguity |
| Keep calibration scope | Only first-hop F/C/L evaluations | No downstream continuation or propagation metrics | Premature propagation claim |

## Frozen decisions

```json
{
  "seed": 342,
  "near_boundary": 0.75,
  "development_error_band": [
    0.2,
    0.5
  ],
  "development_min_boundary_count": 3,
  "development_median_margin_band": [
    -1.0,
    1.5
  ],
  "heldout_error_band": [
    0.15,
    0.5
  ],
  "heldout_min_boundary_count": 4,
  "minimum_FCA": 0.8,
  "minimum_LCA": 0.8,
  "maximum_selected_conditions": 2,
  "neighboring_easier": "Immediate grid neighbor (depth-1, branches) or (depth, branches-1); lower ER OR higher GM, strictly.",
  "selection_tie_break": "Among all qualifiers, increasing depth+branches, then depth, then branches; keep first two.",
  "position_bias": "Flag if a position is selected >=50%, at least two of its selections are wrong, and wrong selections are >=40% among cases whose gold is elsewhere. Apply per condition and pooled development; pooled flag blocks all selection.",
  "case_monotonic": "All 17 neighboring comparisons have non-decreasing binary C error AND non-increasing gold margin. Labels also record any adjacent correct-to-wrong margin sign crossing.",
  "case_display_order": "Increasing depth, then branch count. First means first in this display order, not an assumed total difficulty order.",
  "margin_compression": "Any strictly smaller gold margin than an immediately easier neighbor; descriptive only.",
  "branch_relation": "Each competing path has the same length as gold, using one fixed non-query relation on every edge, as in spec section 9.",
  "stop_handling": "Structural/channel failure stops immediately; empirical flat/cliff/spike checks occur after the complete preregistered dev grid; no adaptive cases or levels."
}
```

## Interpretation and invariance review

Targets are anonymous synthetic Film identifiers, not claims about real films. Candidate bundles are sampled deterministically from the v3.4.1 pre-inference datasets, without consulting output correctness; only candidate identities and source-backed downstream mappings are reused. Dev/held-out target questions are disjoint, while entities may overlap. Every future v3.5 target must be separate from both splits.

All relation vocabulary appears in the same convention even when a relation has no link records. A competing path uses one non-query relation consistently on all its edges, following the spec section 9 example; it differs from the queried path in relation type, not by exactly one altered edge. Every path has the selected depth and terminates at a distinct registered candidate. Candidate-name records precede graph links in a fixed order. Three possible path blocks have a frozen random order per case; absent branches are omitted. Node IDs are sampled independently of candidate order. Only path length and the number of included path blocks vary. Longer paths also increase token count, an inherent limitation of this depth manipulation.

The verifier parses the actual rendered records and traverses relation-specific links; it does not rely only on the graph generator. All four candidate strings have been tokenized against the exact pinned chat template and every guided terminal is reachable. Programmatic graph validation is not represented as an independent human audit.

## Post-run achievement check

| Design intention | Outcome |
|---|---|
| Monotonic axis | Depth ER/GM 6/9 (66.7%)/7/9 (77.8%); branch ER/GM 7/8 (87.5%)/7/8 (87.5%) |
| Separate factors | All 12 factorial cells evaluated on the same eight cases |
| Traceability | 80 frozen mappings rechecked |
| Identity control | All candidate hashes and name records invariant |
| Format control | C valid 96/96 (100.0%); F compliance 96/96 (100.0%) |
| Boundary measurement | All candidate scores and 0.75-threshold fractions retained |
| Avoid isolated selection | Selected []; all local-support checks reported |
| Held-out protection | 0 held-out prompts; only selected cells |
| Unique answer | 240 rendered graphs independently parsed and resolved |
| Calibration scope | Zero downstream calls; propagation metrics absent |
