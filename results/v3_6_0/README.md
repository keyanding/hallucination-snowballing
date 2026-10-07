# v3.6.0 propagation assay validation

**STOP_ASSAY_INVALID**

Calibration: 160/160 calls. Main: 0/80 calls. No auxiliary calls.

## Calibration

| Gate | Count | Required | Pass |
|---|---|---|---|
| A | 39/40 | ≥38 | True |
| B | 17/20 | ≥19 | False |
| C | 20/20 | ≥19 | True |
| D | 19/20 | ≥19 | True |
| E | 15/20 | ≥19 | False |
| F | 20/20 | ≥18 | True |
| G | 160/160 | ≥159 | True |
| H | 17/20 | ≥19 | False |

## Main

Main was not run because calibration failed. Main rates and intervals are null, not zero performance.

## Interpretation

The assay failed its frozen validity gate. No propagation conclusion is licensed.
No evidence here establishes natural hallucination incidence, internal mechanisms, SHAR performance, or generalization to real-world tasks. No Phase II was run.

## Reproducibility

Frozen seed 360; main shuffle 361; greedy generation seed 42; max_new_tokens 16; fresh calls; NF4/BF16 pinned Qwen3-4B.
See spec.md, pre_registration.md, prompt_plan.json, prompt_diff_audit.md, decoding_freeze.json, case_manifest.json and inspection.md.
