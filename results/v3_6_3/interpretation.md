# Interpretation and calibration failures

**STOP_TWO_HOP_CALIBRATION_INVALID**. The experiment stopped after exactly 80 calibration calls. No main, generated-pipeline, integrated or order-diagnostic call ran.

Upstream lookup was correct 20/20 in both U-GOLD and U-ALT, with 20/20 paired upstream success. Failures occurred in the recorded-result downstream prompt: P-GOLD 18/20, P-ALT 19/20, paired downstream 17/20. Parse validity was 77/80. Gates C,F,G failed; A,B,D,E passed.

## All three invalid outputs

| Case | Condition | Expected | Raw output (JSON string) | Tokens | Truncated |
|---|---|---|---|---|---|
| v363-calibration-019 | P-GOLD | OUTCOME_L59 | "The recorded intermediate result is STATE_L28.  \nThe downstream mapping is STATE" | 16 | True |
| v363-calibration-014 | P-GOLD | OUTCOME_M55 | "M55" | 4 | False |
| v363-calibration-001 | P-ALT | OUTCOME_L16 | "STATE_Y10 implies OUTCOME_L16." | 12 | False |

One output began an explanation and reached the frozen 16-token cap. Another emitted only the identifier suffix M55, omitting OUTCOME_. The third expressed the mapping in a sentence instead of emitting only the outcome. All are INVALID under the frozen parser. No identifier was extracted from prose, no prefix was repaired, and no cap increase or rerun was performed.

The observations localize the measured calibration failure to output compliance in the new downstream recorded-result interface. They do not establish an inability to compute the upstream mapping: both upstream arms passed. Nor do they establish successful propagation, since the complete downstream calibration gate failed.

The P prompt changes the introduction, state heading, placement and output instruction from the earlier validated minimal shell, as specified. New identifiers also differ. Across-version results therefore cannot identify which wording, surface form or token identity caused the failure, and do not isolate an internal mechanism.

INTEGRATED_TWO_HOP_READY=false is paired with integrated_evaluated=false. This is an unrun diagnostic, not observed integrated failure. The real-state forwarding implementation was covered by unit tests, including alternative/unmapped passthrough and invalid-state skips, but received no experimental main calls after the calibration stop.

All 124 tests passed; independent verification checked 7800 candidate tokenizations and 80 exact output/token round trips. All 410 historical result files remain unchanged. No natural hallucination, snowballing, SHAR/HalluSE or mechanism conclusion is licensed. No next phase ran.
