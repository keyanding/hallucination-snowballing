# Changelog

## 2026-10-07 — v3.6.0 propagation assay validation

Added the isolated synthetic state-dependent assay with 20 calibration and 40 frozen main cases, exact state-only prompt differences, eight calibration controls and strict parsing. User amendments were frozen before inference: formal entity-label gate H and uniform UNKNOWN rule; 160 calibration calls, 80 conditional main calls. B=17/20, E=15/20 and H=17/20 failed: STOP_ASSAY_INVALID. Main remained untouched. All 90 tests and independent output checks pass; 312 previous result files remain unchanged.

## 2026-10-06 — v3.5.1 task-role framing pilot

Added a separate six-condition injected-state pilot, explicit city mappings, heading-only prompt audits, independent capability checks, and fixed paired analysis. Completed72 main calls and16 auxiliary checks. C0=9/12 failed the10/12 gate: STOP_INVALID. Both framing arms produced12/12 gold answers; no mechanistic or spontaneous-hallucination conclusion is licensed. No automatic follow-up. Earlier experiment artifacts remain unchanged.
