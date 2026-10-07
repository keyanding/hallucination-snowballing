# v3.6.3.1 frozen-interface two-hop pipeline

**TWO_HOP_PIPELINE_VALIDATED**

Calls: calibration=80, main_upstream=80, main_downstream=80, pipeline_generated=40, shell_diagnostic=40, integrated=40; total=360. Pipeline skips=0.

| Calibration gate | Count | Minimum | Pass |
|---|---|---|---|
| A | 20/20 | 19 | True |
| B | 20/20 | 19 | True |
| C | 20/20 | 19 | True |
| D | 20/20 | 19 | True |
| E | 20/20 | 19 | True |
| F | 20/20 | 19 | True |
| G | 80/80 | 79 | True |

## Main

| Main metric | Count | Wilson 95% | Gate passed |
|---|---|---|---|
| A_U_A | 40/40 | [91.2%, 100.0%] | True |
| A_U_B | 40/40 | [91.2%, 100.0%] | True |
| A_D_A | 40/40 | [91.2%, 100.0%] | True |
| A_D_B | 40/40 | [91.2%, 100.0%] | True |
| S_D | 40/40 | [91.2%, 100.0%] | True |
| E2E | 40/40 | [91.2%, 100.0%] | True |

G7 OTHER+INVALID=0/160; pass=True.
Downstream C conditional on correct U-A: 40/40. Strict E2E denominator40 includes all skips.

## Shell compatibility diagnostic (non-gating)

| Shell | Exact accuracy | INVALID | Explanation-format | Prefix omission | Truncated |
|---|---|---|---|---|---|
| VALIDATED | 20/20 | 0 | 0 | 0 | 0 |
| RECORDED | 17/20 | 3 | 3 | 0 | 3 |

Paired discordances: RECORDED-only failures=3; VALIDATED-only failures=0. Flags may overlap and are descriptive, not alternate parsing.

INTEGRATED_TWO_HOP_READY=False; evaluated=True.
I-A=7/20; I-B=9/20; paired=2/20.

## Interpretation

The synthetic modular two-hop pipeline passed: actual inferred states forwarded into the validated Current state interface produced the corresponding outcomes, and counterfactual supplied states predictably switched downstream outcomes.
This does not establish natural hallucination propagation, spontaneous error rates, injected/natural-error equivalence, internal neural mechanism, SHAR/HalluSE performance or real-world reasoning. Integrated final-answer accuracy does not prove internal intermediate use. No next phase was run.

See diagnosis.md, interpretation.md, inspection.md and the frozen pre_registration.md.
