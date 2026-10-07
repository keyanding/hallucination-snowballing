# v3.6.3 two-hop propagation assay

**STOP_TWO_HOP_CALIBRATION_INVALID**

Calls: calibration=80, main_upstream=0, main_propagation=0, pipeline_generated=0, integrated=0, order_diagnostic=0; total=80. Pipeline skips=0.

| Calibration gate | Count | Minimum | Pass |
|---|---|---|---|
| A | 20/20 | 19 | True |
| B | 20/20 | 19 | True |
| C | 18/20 | 19 | False |
| D | 19/20 | 19 | True |
| E | 20/20 | 19 | True |
| F | 17/20 | 19 | False |
| G | 77/80 | 79 | False |

Main rates/intervals are null because main was not evaluated. Readiness=false with evaluated=false is not a failed integrated test.

## Interpretation

Calibration failed; main and all secondary calls were not run. No main propagation conclusion is licensed.
Integrated final-answer success does not establish internal use of an intermediate state. No spontaneous hallucination, natural snowballing, SHAR/HalluSE or real-world generalization claim. No subsequent phase was run.

See diagnosis.md, inspection.md, pre_registration.md and gate.json. Rebuild reporting with `python -m experiments.v3_6_3.report`.
