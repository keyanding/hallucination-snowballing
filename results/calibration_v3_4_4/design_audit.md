# v3.4.4 pre-inference design audit

| Design intention | Implemented intervention | Pre-run validity check | Observable outcome | What would falsify it / limit interpretation |
|---|---|---|---|---|
| Separate option artifacts from semantics | L four option rotations; evidence fixed | Exact invariant prefix/suffix, graph solution | Changed C identity and matched position score shift | No changes/positive shift fails H1 |
| Measure natural no-list selection | N omits list; unconstrained F primary | Exact N vs L diff and no trie call | Strict coverage and wrong/all plus wrong/valid | Invalid output is not a correct answer |
| Check residual record order | R rotates complete name-record lines | IDs move with names; graph/query identical | Record sensitivity and earliest-record selection | No identity changes fails H2; record flag rejects natural policy |
| Separate format failures | Frozen exact parser and categories | Unit tests plus independent cap smoke | Five exclusive categories; extraction supplementary | Explanations/truncation cannot establish completed natural choice |
| Counterbalance identity positions | Every name every L/R position; gold baseline balanced | All rotations audited; hashes frozen | Identity-matched first-position mean-score shift | Token length and identity remain cross-person confounds |
| Test complexity interaction | Same cases EASY/MID/HARD | Graph tokens/depth/branches logged | Paired case trajectories and bootstrap | Mixed/nonpositive differences limit H3; length not isolated |
| Prevent selection overfit | 24 fresh development, 16 untouched confirmation | New targets/nodes/bundles and split hashes | Single policy+difficulty confirmation | No retuning; reused people limit external validity |
| Keep wrong states traceable | Frozen real r2 evidence; synthetic first hop | 184 source mappings checked against source coordinates | Stable wrong identities can map to r2 later | No downstream execution or propagation inference |
| Interpret scores correctly | Same prompt F/C/S; sums and means; EOS excluded | Token boundaries/trie, frozen replay harness | Rank disagreement and gold margins | Mean scores are not choice probabilities |
| Make failure informative | Full planned dataset even poor empirical results | Fixed gate, denominators and route rules | Usability and wrong yield separate | No target-error chasing or automatic v3.5 |

Actual prompt plan SHA256: `1cf1834c9ddaee9d66395e3aff2ba8ae532f0170a5d529db6dff2ab16d4f8f76`; exact per-cell prompt diffs/hashes: `prompt_diff_audit.md` (SHA256 `655163380c7eb405b72e64b2ee05945d46d6147f6fa67f95e45da3b462a7d9e7`). All 1170 plans validated before inference.

## Frozen policy and falsifiable hypotheses

```json
{
  "seed": 344,
  "generation_seed": 42,
  "interfaces": [
    "L",
    "N",
    "R"
  ],
  "strict_coverage_min": 0.9,
  "record_three_of_four_min": 0.75,
  "record_four_of_four_min": 0.5,
  "earliest_record_flag": 0.4,
  "agreement_min": 0.85,
  "aliases": {},
  "natural_parser": "TRUNCATED first; exact canonical/approved alias; multiple mentions AMBIGUOUS; conservative name-shaped unknown OUT_OF_SET; rest NONCOMPLIANT. Supplementary extraction never changes primary.",
  "L_aggregate": "Unique modal C identity; ties missing. Three-of-four wrong is not robust wrong.",
  "R_aggregate": "All four strictly valid and at least three agree, otherwise UNSTABLE_OR_UNRESOLVED.",
  "route_order": [
    "N",
    "R",
    "L"
  ],
  "difficulty_tiebreak": [
    "EASY",
    "MID",
    "HARD"
  ],
  "selection": "First route with a passing difficulty; easiest passing difficulty. Never maximize wrong yield. L fallback requires C validity, at least 75% identity-stable cells and first fraction below 40%; admits forced-choice selection only.",
  "record_flag_rule": "Flag >=40% earliest among valid R rejects N/R gate; no discretionary override. Report identity-matched scores and per-case effects as investigation.",
  "N_gate": "N coverage >=90%; R 3/4 >=75%, 4/4 >=50%; no record flag; N versus unique L mode agreement >=85% among strict N with non-tied L.",
  "R_gate": "R aggregate coverage >=90%; same record-stability thresholds and flag; N versus L agreement >=85%.",
  "wrong_yield": "At least one strict wrong N or wrong R aggregate required for observed traceable wrong yield; separate from interface usability. Zero yield never triggers retuning.",
  "confirmation": "One chosen difficulty. L4+N1 for all 16; add R4 if selected N or R. No confirmation if no policy. Apply same route gate; no fallback or retuning after confirmation.",
  "cap_smoke": "Four independent format tasks at 96. If any truncated, repeat all four at 192. Choose 192 only in that case. No experimental case enters smoke. L always 96.",
  "duplicates": "N and R1 are identical prompts but are independently evaluated and retained, as budgeted.",
  "budget": {
    "development_renderings": 648,
    "old_diagnostic_renderings": 90,
    "development_channel_evaluations": 1584,
    "old_channel_evaluations": 180,
    "confirmation_L_renderings": 80,
    "confirmation_NR_renderings": 144
  },
  "score": "EOS excluded; raw sum and mean/token both retained. Mean/token is not a probability; no normalized choice probabilities claimed.",
  "bootstrap": "2000 seeded case-resampling replicates; percentile 95% intervals; rotations/depths never independent units.",
  "hypotheses": {
    "H1": "New L identity changes plus positive mean identity-matched first-position score shift; otherwise unsupported.",
    "H2": "R identity changes among strict outputs demonstrate residual record-order effect; no such changes fails to support effect.",
    "H3": "Paired HARD minus EASY L sensitivity and first-position rate positive; nonpositive results fail directional hypothesis; mixed cases limit consistency.",
    "H4": "Report both stable-wrong and changing sets separately; zero stable-wrong does not establish such subtype."
  }
}
```

## Post-run design audit

| Design intention | Achieved? | Numerical evidence | Limitations |
|---|---|---|---|
| Separate option artifacts | Measured | {'EASY': {'count': 2, 'denominator': 24, 'rate': 0.08333333333333333}, 'MID': {'count': 14, 'denominator': 24, 'rate': 0.5833333333333334}, 'HARD': {'count': 20, 'denominator': 24, 'rate': 0.8333333333333334}} | No internal mechanism inference |
| Natural no-list primary | Measured | {'EASY': {'count': 24, 'denominator': 24, 'rate': 1.0}, 'MID': {'count': 24, 'denominator': 24, 'rate': 1.0}, 'HARD': {'count': 24, 'denominator': 24, 'rate': 1.0}} | Wrong rates conditional on coverage |
| Residual record order | Measured | {'EASY': {'count': 24, 'denominator': 96, 'rate': 0.25}, 'MID': {'count': 28, 'denominator': 96, 'rate': 0.2916666666666667}, 'HARD': {'count': 41, 'denominator': 95, 'rate': 0.43157894736842106}} | Threshold is heuristic |
| Strict format taxonomy | Verified | {'EASY': {'IN_SET_VALID': 24}, 'MID': {'IN_SET_VALID': 24}, 'HARD': {'IN_SET_VALID': 24}} | Conservative unknown-name detector |
| Counterbalance | Verified | Every identity occupies each of four L/R positions; all 1170 planned renderings audited | Identity token lengths differ |
| Complexity interaction | Measured | {'HARD_minus_EASY_mean': 0.75, 'case_bootstrap_95': [0.5416666666666666, 0.9166666666666666], 'positive': 18, 'zero': 6, 'negative': 0, 'denominator': 24} | Depth/branches/length covary |
| Fresh split | Verified | 24 development; confirmation queried 16/16 | People reused; only one policy/difficulty |
| Frozen r2 traceability | Verified | 184 candidate mappings checked; 40 new bundles | No downstream inference |
| Score interpretation | Verified | 14 diagnostic anomaly rows; exact harness replay | EOS excluded; no probabilities |
| Meaningful failure | Completed | 738 development+old renderings; 144 confirmation; gate True | No target error-rate tuning |
