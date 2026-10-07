# v3.6.1 minimal propagation diagnosis

**MINIMAL_ASSAY_VALIDATED**

Calls: stage_b=160, stage_c=80, unmapped=10, record_order=20. Total 270.

## Stage B: all old cases

| Family | Gold /20 | Wrong /20 | Paired /20 | False UNKNOWN /40 | OTHER+INVALID /40 |
|---|---|---|---|---|---|
| FULL_UNKNOWN | 19 | 20 | 19 | 1 | 0 |
| FULL_NO_UNKNOWN | 20 | 20 | 20 | 0 | 0 |
| MINIMAL_UNKNOWN | 20 | 20 | 20 | 0 | 0 |
| MINIMAL_NO_UNKNOWN | 20 | 20 | 20 | 0 | 0 |

Best descriptive family (all ties): FULL_NO_UNKNOWN, MINIMAL_UNKNOWN, MINIMAL_NO_UNKNOWN. Stage C was fixed independently.
FULL_UNKNOWN uses the new shorter UNKNOWN rule, so it is not a byte-identical replay of v3.6.0.

## Stage C: fresh cases

| Gate | Count | Required | Pass |
|---|---|---|---|
| C1 | 40/40 | ≥39 | True |
| C2 | 40/40 | ≥39 | True |
| C3 | 40/40 | ≥39 | True |
| C4 | 0/80 | =0 | True |
| C5 | 0/80 | ≤1 | True |
| C6 | 10/10 | ≥9 | True |

- A_C: 40/40; Wilson 95% CI [91.2%, 100.0%].
- A_W: 40/40; Wilson 95% CI [91.2%, 100.0%].
- S: 40/40; Wilson 95% CI [91.2%, 100.0%].

Record-order diagnosis: 20/20 unchanged mapped identity; requires ≥19/20; pass=True. This does not alter C1–C6.

STRONGER_MODEL_DIAGNOSTIC_NOT_RUN: Only the existing Qwen3-4B checkpoint is available in configured/default caches; no stronger-model endpoint is configured in the existing inference adapter. No download or ad hoc infrastructure.

Validation, if achieved, concerns only explicit symbolic state-to-outcome following under the minimal prompt. No natural hallucination, multi-hop snowballing, SHAR, internal mechanism or real-world generalization claim.

See diagnosis.md, v360_failure_audit.md, inspection.md, pre_registration.md, prompt_diff_audit.md and machine-readable metrics. Rebuild reporting with `python -m experiments.v3_6_1.report`.
