# v3.4.4 diagnosis

1. **Does listed first-option preference replicate on new cases?** EASY: first 25/96 (26.0%), identity-sensitive 2/24 (8.3%), identity-matched first-score shift 1.3865; MID: first 45/96 (46.9%), identity-sensitive 14/24 (58.3%), identity-matched first-score shift 2.0034; HARD: first 67/96 (69.8%), identity-sensitive 20/24 (83.3%), identity-matched first-score shift 2.7470. The 25% equal-exposure reference is descriptive. H1 requires changed identities and positive score shift; results are stratum-specific, not a population mechanism claim.

2. **What changes when the list is removed?** EASY: L wrong 3/96 (3.1%), N wrong/all 0/24 (0.0%), N wrong/valid 0/24 (0.0%) with coverage 24/24 (100.0%); MID: L wrong 25/96 (26.0%), N wrong/all 1/24 (4.2%), N wrong/valid 1/24 (4.2%) with coverage 24/24 (100.0%); HARD: L wrong 52/96 (54.2%), N wrong/all 5/24 (20.8%), N wrong/valid 5/24 (20.8%) with coverage 24/24 (100.0%). This intervention also changes two query/output phrases; it is not a pure order contrast.

3. **Does record order matter?** EASY: R identity-sensitive among complete cells 0/24 (0.0%), earliest/valid 24/96 (25.0%), matched score shift 0.7438; MID: R identity-sensitive among complete cells 4/24 (16.7%), earliest/valid 28/96 (29.2%), matched score shift 0.8557; HARD: R identity-sensitive among complete cells 14/23 (60.9%), earliest/valid 41/95 (43.2%), matched score shift 1.6647. R rotates complete records, not answer options. H2 is supported only where identities actually change; invalid rotations alone do not establish identity change.

4. **Which wrong identities persist?** L robust wrong requires the same wrong identity in all four outputs; R aggregates require all valid and at least three identical. The latter is AGGREGATED_TRACEABLE_WRONG, never a single trajectory. Cases:

```json
[]
```

5. **Is sensitivity greater at higher difficulty?** Paired HARD minus EASY (same cases):

```json
{
  "L_sensitivity": {
    "HARD_minus_EASY_mean": 0.75,
    "case_bootstrap_95": [
      0.5416666666666666,
      0.9166666666666666
    ],
    "positive": 18,
    "zero": 6,
    "negative": 0,
    "denominator": 24
  },
  "L_first": {
    "HARD_minus_EASY_mean": 0.4375,
    "case_bootstrap_95": [
      0.3229166666666667,
      0.5520833333333334
    ],
    "positive": 19,
    "zero": 5,
    "negative": 0,
    "denominator": 24
  },
  "N_wrong": {
    "HARD_minus_EASY_mean": 0.20833333333333334,
    "case_bootstrap_95": [
      0.041666666666666664,
      0.375
    ],
    "positive": 5,
    "zero": 19,
    "negative": 0,
    "denominator": 24
  },
  "R_sensitivity": {
    "HARD_minus_EASY_mean": 0.625,
    "case_bootstrap_95": [
      0.4166666666666667,
      0.7916666666666666
    ],
    "positive": 15,
    "zero": 9,
    "negative": 0,
    "denominator": 24
  },
  "L_median_margin": {
    "HARD_minus_EASY_mean": -3.5533703649649055,
    "case_bootstrap_95": [
      -4.261406100673015,
      -2.8234523098654236
    ],
    "positive": 0,
    "zero": 0,
    "negative": 24,
    "denominator": 24
  },
  "N_margin": {
    "HARD_minus_EASY_mean": -1.7902791755485916,
    "case_bootstrap_95": [
      -2.6176782456656094,
      -0.9960198120792584
    ],
    "positive": 1,
    "zero": 0,
    "negative": 23,
    "denominator": 24
  },
  "R_median_margin": {
    "HARD_minus_EASY_mean": -1.4440538669871876,
    "case_bootstrap_95": [
      -1.87734644378941,
      -1.0205583251727663
    ],
    "positive": 1,
    "zero": 0,
    "negative": 23,
    "denominator": 24
  }
}
```

Full EASY/MID/HARD trajectories are in metrics.json. H3 is supported only if both L sensitivity and first-fraction differences are positive; nonpositive/mixed trajectories limit or reject this prediction. Graph depth, branch count and prompt length covary; no isolated reasoning-depth causal claim.

6. **How often is natural output valid?** EASY: N categories {'IN_SET_VALID': 24} /24; R categories {'IN_SET_VALID': 96} /96; MID: N categories {'IN_SET_VALID': 24} /24; R categories {'IN_SET_VALID': 96} /96; HARD: N categories {'IN_SET_VALID': 24} /24; R categories {'IN_SET_VALID': 95, 'TRUNCATED': 1} /96. These categories are mutually exclusive; truncation takes precedence. Name-shaped out-of-set classification is conservative, not a semantic person recognizer. Wait/reconsideration output is not a completed answer.

7. **When do channels disagree?** 14 renderings across all cohorts have an invalid F or a strict F/C/mean-score or sum/mean difference (see exact records in metrics.json and inspection.md). Greedy token decisions differ from sequence ranking; sum and mean have different length dependence. This identifies operational differences, not their internal mechanism. Raw score sums, token lengths and means are retained; EOS is excluded.

8. **Does confirmation pass?** Selected N/EASY; confirmation pass True. The full unchanged threshold checks are in gate.json. No alternative was selected after confirmation.

9. **Which future claim is licensed?** natural single-trajectory first-hop selection v3.5_executed=false. Error-yield insufficient: True.

10. **What remains before propagation?** Confirmed interface validity and sufficient traceable wrong yield are separate requirements; a new calibration sample is needed if yield is insufficient. Record order, reused people, limited case count, scoring length/termination sensitivity and construction-dependent complexity remain limitations. Any downstream study requires a new preregistered design and matched causal controls; this experiment measures first-hop selections only.

Wrong-state persistence on new development data: L same-wrong 4/4 = **0/72 cells**; R same-wrong 4/4 = **0/72 cells**; wrong R aggregates = **0/67 resolved cells**. These 72 repeated cells belong to 24 base cases. A wrong canonical N answer alone does not establish an order-stable wrong state.

See [supplementary diagnostics](supplementary_diagnostics.md) for zero-inclusive category counts, explicit channel-disagreement denominators, token-length ranges and hypothesis decisions.
