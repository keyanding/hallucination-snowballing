# v3.6.2 context accumulation robustness

**ROBUST_CONTEXT_ASSAY**

Completed 320/320 main calls and 72/72 position-diagnostic calls.

| K | C0 correct /40 | W0 correct /40 | Paired /40 | UNKNOWN /80 | OTHER+INVALID /80 |
|---|---|---|---|---|---|
| 0 | 40 | 40 | 40 | 0 | 0 |
| 4 | 40 | 40 | 40 | 0 | 0 |
| 12 | 40 | 40 | 40 | 0 | 0 |
| 24 | 40 | 40 | 40 | 0 | 0 |

Primary unit:40 paired base cases. C0/W0 are reported separately. Full categories, Wilson95% intervals and case transitions are in metrics.json.

## Paired changes from K0

| K vs K0 | ΔC /40 | ΔW /40 | ΔS /40 | Paired lost | Paired gained |
|---|---|---|---|---|---|
| 4 | 0 | 0 | 0 | 0 | 0 |
| 12 | 0 | 0 | 0 | 0 | 0 |
| 24 | 0 | 0 | 0 | 0 | 0 |

Paired lost means both C0/W0 correct at K0, but at least one becomes incorrect at that K; gained is the reverse.

## Separate position diagnosis

| K24 position | C0 /12 | W0 /12 | UNKNOWN /24 | OTHER+INVALID /24 |
|---|---|---|---|---|
| beginning | 12 | 12 | 0 | 0 |
| middle | 12 | 12 | 0 | 0 |
| end | 12 | 12 | 0 | 0 |

These12 seeded cases do not alter the main gate. Relevant pair region is balanced across primary cases and held fixed per case at positive K; K0 has only two lines.

## Interpretation

The minimal state-propagation primitive remains highly reliable under up to24 irrelevant state-to-outcome records in this synthetic setting.
No natural hallucination, upstream reasoning layer, SHAR/HalluSE, conflicting evidence or internal-mechanism claim. No next phase was run.

See diagnosis.md, inspection.md, pre_registration.md, position_schedule.json and prompt_diff_audit.md. Recompute with `python -m experiments.v3_6_2.report`.
