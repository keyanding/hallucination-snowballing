# Diagnosis

**STOP_ASSAY_INVALID**

Failed calibration gates: B, E, H.

## All calibration outputs differing from mapping-implied expected output

| Case | Condition | Supplied state | Expected | Observed |
|---|---|---|---|---|
| v360-calibration-012 | C0 | State_M41 | Outcome_W11 | UNKNOWN |
| v360-calibration-017 | C0 | State_J32 | Outcome_E53 | UNKNOWN |
| v360-calibration-001 | C0 | State_D49 | Outcome_F93 | UNKNOWN |
| v360-calibration-006 | LOOKUP_WRONG | State_W27 | Outcome_A15 | UNKNOWN |
| v360-calibration-006 | REVERSE | State_Y82 | Outcome_M73 | UNKNOWN |
| v360-calibration-010 | REVERSE | State_Y20 | Outcome_V88 | UNKNOWN |
| v360-calibration-012 | SWAP | State_M41 | Outcome_A20 | UNKNOWN |

## Invariance interpretation

E and H compare the control output with the same-case C0 output. A control can answer correctly yet fail invariance if C0 was incorrect. Correct-by-condition counts are reported separately in metrics.json.
UNKNOWN is a permitted parse but is incorrect when the supplied state has a mapping. It therefore need not fail G while it can fail B or other correctness gates.

No failed cases were replaced, no prompt or threshold was tuned, and no further model calls were made beyond the gated run. These observations do not identify an internal cause.
