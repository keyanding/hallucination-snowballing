# Supplementary diagnostics

These tables add descriptive detail without altering the frozen policy, parser, hypotheses or confirmation decision. Categories with zero observations remain visible.

## Full output taxonomy

| Cohort | Difficulty | Interface | All | Valid | Out of set | Ambiguous | Noncompliant | Truncated | Wrong / valid | Wrong / all |
|---|---|---|---|---|---|---|---|---|---|---|
| development | EASY | L | 96 | 96 | 0 | 0 | 0 | 0 | 3/96 | 3/96 |
| development | EASY | N | 24 | 24 | 0 | 0 | 0 | 0 | 0/24 | 0/24 |
| development | EASY | R | 96 | 96 | 0 | 0 | 0 | 0 | 0/96 | 0/96 |
| development | MID | L | 96 | 94 | 0 | 0 | 0 | 2 | 23/94 | 23/96 |
| development | MID | N | 24 | 24 | 0 | 0 | 0 | 0 | 1/24 | 1/24 |
| development | MID | R | 96 | 96 | 0 | 0 | 0 | 0 | 4/96 | 4/96 |
| development | HARD | L | 96 | 93 | 0 | 0 | 0 | 3 | 49/93 | 49/96 |
| development | HARD | N | 24 | 24 | 0 | 0 | 0 | 0 | 5/24 | 5/24 |
| development | HARD | R | 96 | 95 | 0 | 0 | 0 | 1 | 19/95 | 19/96 |
| old | EASY | N | 6 | 6 | 0 | 0 | 0 | 0 | 0/6 | 0/6 |
| old | EASY | R | 24 | 23 | 0 | 0 | 1 | 0 | 0/23 | 0/24 |
| old | MID | N | 6 | 6 | 0 | 0 | 0 | 0 | 0/6 | 0/6 |
| old | MID | R | 24 | 24 | 0 | 0 | 0 | 0 | 1/24 | 1/24 |
| old | HARD | N | 6 | 6 | 0 | 0 | 0 | 0 | 2/6 | 2/6 |
| old | HARD | R | 24 | 24 | 0 | 0 | 0 | 0 | 6/24 | 6/24 |
| confirmation | EASY | L | 64 | 64 | 0 | 0 | 0 | 0 | 4/64 | 4/64 |
| confirmation | EASY | N | 16 | 16 | 0 | 0 | 0 | 0 | 0/16 | 0/16 |
| confirmation | EASY | R | 64 | 63 | 0 | 0 | 1 | 0 | 0/63 | 0/64 |

L F above is a shadow channel; primary L error rates use C. N/R are unconstrained. No invalid category is treated as a correct semantic response.

## Channel disagreement and token lengths

| Cohort / difficulty / interface | F valid | F vs S disagreements | F vs C | C vs S | S sum vs mean | Input tokens | Graph tokens |
|---|---|---|---|---|---|---|---|
| development/EASY/L | 96 | 0 | 0 | 0 | 0 | [229, 251] | [19, 19] |
| development/EASY/N | 24 | 0 | None | None | 0 | [199, 210] | [19, 19] |
| development/EASY/R | 96 | 0 | None | None | 0 | [199, 210] | [19, 19] |
| development/MID/L | 94 | 1 | 0 | 1 | 1 | [267, 289] | [57, 57] |
| development/MID/N | 24 | 0 | None | None | 0 | [237, 248] | [57, 57] |
| development/MID/R | 96 | 1 | None | None | 0 | [237, 248] | [57, 57] |
| development/HARD/L | 93 | 2 | 0 | 2 | 1 | [438, 460] | [228, 228] |
| development/HARD/N | 24 | 0 | None | None | 0 | [408, 419] | [228, 228] |
| development/HARD/R | 95 | 1 | None | None | 0 | [408, 419] | [228, 228] |
| old/EASY/N | 6 | 0 | None | None | 0 | [198, 207] | [19, 19] |
| old/EASY/R | 23 | 0 | None | None | 0 | [198, 207] | [19, 19] |
| old/MID/N | 6 | 0 | None | None | 0 | [236, 245] | [57, 57] |
| old/MID/R | 24 | 0 | None | None | 0 | [236, 245] | [57, 57] |
| old/HARD/N | 6 | 0 | None | None | 0 | [407, 416] | [228, 228] |
| old/HARD/R | 24 | 0 | None | None | 0 | [407, 416] | [228, 228] |
| confirmation/EASY/L | 64 | 1 | 0 | 1 | 0 | [229, 253] | [19, 19] |
| confirmation/EASY/N | 16 | 0 | None | None | 0 | [199, 211] | [19, 19] |
| confirmation/EASY/R | 63 | 0 | None | None | 0 | [199, 211] | [19, 19] |

F comparisons exclude invalid outputs; C/S and sum/mean denominators are all renderings in the corresponding stratum. S excludes EOS. N/R candidate scores are diagnostic and impose no choice restriction on F. Mean normalization changes length weighting; no score is reported as calibrated probability. Case-bootstrap intervals describe this small case sample and do not model dependence from reused people. Zero-event bootstrap intervals can collapse to zero; they do not establish a zero population event rate.

## Gold-margin distributions and matched position shifts

S remains available when F is invalid; these are unconditional score diagnostics. Quartiles describe all renderings, while shift intervals resample whole cases.

| Cohort / difficulty / interface | Gold margin min / Q1 / median / Q3 / max | First-position shift mean [case-bootstrap 95%] |
|---|---|---|
| confirmation/EASY/L | -0.5688 / 1.9363 / 2.6083 / 3.2645 / 5.5906 | 1.3663 [1.0711, 1.6567] |
| confirmation/EASY/N | 0.4226 / 3.1300 / 3.2617 / 3.5326 / 4.6594 | not manipulated |
| confirmation/EASY/R | 0.4226 / 2.7799 / 3.1590 / 3.7376 / 5.0507 | 0.8586 [0.6947, 1.0502] |
| development/EASY/L | -2.0423 / 2.0958 / 3.1065 / 4.0837 / 5.6750 | 1.3865 [1.1446, 1.6468] |
| development/EASY/N | 1.7304 / 3.2676 / 3.7299 / 4.3036 / 4.9578 | not manipulated |
| development/EASY/R | 1.1719 / 2.9898 / 3.5676 / 4.1844 / 6.4798 | 0.7438 [0.6278, 0.8539] |
| development/MID/L | -4.1160 / -0.0049 / 1.4868 / 3.0666 / 4.9427 | 2.0034 [1.6826, 2.3218] |
| development/MID/N | -2.2125 / 2.0830 / 2.8324 / 3.4711 / 4.0252 | not manipulated |
| development/MID/R | -2.4158 / 2.1644 / 2.7406 / 3.2820 / 4.2531 | 0.8557 [0.6626, 1.0500] |
| development/HARD/L | -5.0688 / -1.9906 / -0.2800 / 1.9707 / 4.8464 | 2.7470 [2.4032, 3.0621] |
| development/HARD/N | -3.9037 / 1.2426 / 2.8422 / 3.4121 / 4.2214 | not manipulated |
| development/HARD/R | -3.9037 / 0.5147 / 2.4548 / 3.4076 / 5.1719 | 1.6647 [1.4054, 1.9293] |
| old/EASY/N | 2.4306 / 2.9225 / 3.6824 / 4.2789 / 4.7979 | not manipulated |
| old/EASY/R | 1.2428 / 2.7677 / 3.6824 / 4.1866 / 6.1835 | 0.7562 [0.5588, 0.9605] |
| old/MID/N | 1.6585 / 2.8087 / 3.2697 / 3.4820 / 3.8688 | not manipulated |
| old/MID/R | -0.9875 / 2.2103 / 2.7978 / 3.4211 / 3.9513 | 0.8085 [0.5298, 1.0896] |
| old/HARD/N | -0.5914 / 0.4633 / 2.8995 / 3.5834 / 4.2635 | not manipulated |
| old/HARD/R | -1.4297 / 0.1855 / 2.3243 / 3.5438 / 4.6225 | 1.4543 [0.9721, 1.9671] |

## Hypothesis decisions

Absent registered patterns are labeled unsupported, not rescued by a different metric.

- H1: **supported descriptively**. Identity changes on new L rotations plus positive aggregate identity-matched first-position score shift.
- H2: **supported descriptively**. At least two strict identities across equivalent R presentations, separately from invalid outputs.
- H3: **supported descriptively**. Paired HARD minus EASY positive for both L sensitivity and L first fraction; intervals and mixed cases reported, not a significance claim.
- H4: **unsupported / registered pattern absent**. Requires both 4/4 same-wrong sets and identity-changing sets within L or R, analyzed separately. A 3/4 wrong aggregate is not 4/4 robustness.

## Exploratory persistence across all nine matched observations

The same wrong identity across L1–L4 C, N F and R1–R4 F (all natural outputs strict-valid). This stronger post-run descriptive check was not used for selection:

```json
[]
```

## Artifact lifecycle

The original manifest freezes both design_audit.md and its identical pre-inference copy. The specification also requires appending a post-run table to design_audit.md. Its pre-inference prefix remains byte-identical and verifiable through design_audit.pre_inference.md; the independent verifier explicitly checks that prefix instead of falsely requiring the completed report to have the old whole-file hash. No prompt, parser, policy, generator, model parameter or source hash changed. Use scripts/verify_calibration_v3_4_4.py for post-report verification.
