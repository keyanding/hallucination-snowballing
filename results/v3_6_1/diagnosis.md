# Diagnosis

**MINIMAL_ASSAY_VALIDATED**

## Static audit

See v360_failure_audit.md for all 20 cases and per-identifier tokens. Associations are descriptive; 20 cases cannot identify lexical causes.

## Paired Stage B factors

- UNKNOWN removal, full: mapped accuracy 39/40 → 40/40; false UNKNOWN 1/40 → 0/40; paired corrected 1, broken 0.
- UNKNOWN removal, minimal: mapped accuracy 40/40 → 40/40; false UNKNOWN 0/40 → 0/40; paired corrected 0, broken 0.
- Simplification, UNKNOWN: mapped accuracy 39/40 → 40/40; false UNKNOWN 1/40 → 0/40; paired corrected 1, broken 0.
- Simplification, no UNKNOWN: mapped accuracy 40/40 → 40/40; false UNKNOWN 0/40 → 0/40; paired corrected 0, broken 0.

Directional support for fallback interference in full/minimal matched contrasts: [True, False]. Magnitudes above are descriptive, with no significance or internal-mechanism claim.
Directional support for simplification in UNKNOWN/no-UNKNOWN matched contrasts: [True, False]. This bundles syntax, prose and entity removal; it does not isolate entity scaffolding.
P3 (MINIMAL_NO_UNKNOWN fails more than1/40): False. Stage C runs independently; stronger-model execution is governed by Section10.

## Fresh validation

| Gate | Count | Required | Pass |
|---|---|---|---|
| C1 | 40/40 | ≥39 | True |
| C2 | 40/40 | ≥39 | True |
| C3 | 40/40 | ≥39 | True |
| C4 | 0/80 | =0 | True |
| C5 | 0/80 | ≤1 | True |
| C6 | 10/10 | ≥9 | True |

All cases were selected by frozen lexical/tokenization criteria only. Stage C changes the identifier family as well as using the minimal prompt; it does not by itself separate prompt and dataset causes.
Order: 20/20 unchanged; correct reversed outputs 20/20.

STRONGER_MODEL_DIAGNOSTIC_NOT_RUN. No stronger-model result or model-size causal claim is available.

## Complete paired family transitions

### FULL_UNKNOWN -> FULL_NO_UNKNOWN

| Case | State | Before | After | Before correct | After correct |
|---|---|---|---|---|---|
| v360-calibration-001 | C0 | Outcome_F93 | Outcome_F93 | True | True |
| v360-calibration-001 | W0 | Outcome_I48 | Outcome_I48 | True | True |
| v360-calibration-002 | C0 | Outcome_E87 | Outcome_E87 | True | True |
| v360-calibration-002 | W0 | Outcome_N34 | Outcome_N34 | True | True |
| v360-calibration-003 | C0 | Outcome_L24 | Outcome_L24 | True | True |
| v360-calibration-003 | W0 | Outcome_P70 | Outcome_P70 | True | True |
| v360-calibration-004 | C0 | Outcome_N09 | Outcome_N09 | True | True |
| v360-calibration-004 | W0 | Outcome_I15 | Outcome_I15 | True | True |
| v360-calibration-005 | C0 | Outcome_M36 | Outcome_M36 | True | True |
| v360-calibration-005 | W0 | Outcome_Z51 | Outcome_Z51 | True | True |
| v360-calibration-006 | C0 | Outcome_M73 | Outcome_M73 | True | True |
| v360-calibration-006 | W0 | Outcome_A15 | Outcome_A15 | True | True |
| v360-calibration-007 | C0 | Outcome_R32 | Outcome_R32 | True | True |
| v360-calibration-007 | W0 | Outcome_A64 | Outcome_A64 | True | True |
| v360-calibration-008 | C0 | Outcome_C61 | Outcome_C61 | True | True |
| v360-calibration-008 | W0 | Outcome_H92 | Outcome_H92 | True | True |
| v360-calibration-009 | C0 | Outcome_S45 | Outcome_S45 | True | True |
| v360-calibration-009 | W0 | Outcome_D81 | Outcome_D81 | True | True |
| v360-calibration-010 | C0 | Outcome_V88 | Outcome_V88 | True | True |
| v360-calibration-010 | W0 | Outcome_X40 | Outcome_X40 | True | True |
| v360-calibration-011 | C0 | Outcome_B21 | Outcome_B21 | True | True |
| v360-calibration-011 | W0 | Outcome_C69 | Outcome_C69 | True | True |
| v360-calibration-012 | C0 | Outcome_W11 | Outcome_W11 | True | True |
| v360-calibration-012 | W0 | Outcome_A20 | Outcome_A20 | True | True |
| v360-calibration-013 | C0 | Outcome_D95 | Outcome_D95 | True | True |
| v360-calibration-013 | W0 | Outcome_L31 | Outcome_L31 | True | True |
| v360-calibration-014 | C0 | Outcome_B00 | Outcome_B00 | True | True |
| v360-calibration-014 | W0 | Outcome_A74 | Outcome_A74 | True | True |
| v360-calibration-015 | C0 | Outcome_T88 | Outcome_T88 | True | True |
| v360-calibration-015 | W0 | Outcome_K40 | Outcome_K40 | True | True |
| v360-calibration-016 | C0 | Outcome_X89 | Outcome_X89 | True | True |
| v360-calibration-016 | W0 | Outcome_Q30 | Outcome_Q30 | True | True |
| v360-calibration-017 | C0 | UNKNOWN | Outcome_E53 | False | True |
| v360-calibration-017 | W0 | Outcome_H41 | Outcome_H41 | True | True |
| v360-calibration-018 | C0 | Outcome_M04 | Outcome_M04 | True | True |
| v360-calibration-018 | W0 | Outcome_J28 | Outcome_J28 | True | True |
| v360-calibration-019 | C0 | Outcome_V51 | Outcome_V51 | True | True |
| v360-calibration-019 | W0 | Outcome_W79 | Outcome_W79 | True | True |
| v360-calibration-020 | C0 | Outcome_K93 | Outcome_K93 | True | True |
| v360-calibration-020 | W0 | Outcome_G48 | Outcome_G48 | True | True |

### FULL_UNKNOWN -> MINIMAL_UNKNOWN

| Case | State | Before | After | Before correct | After correct |
|---|---|---|---|---|---|
| v360-calibration-001 | C0 | Outcome_F93 | Outcome_F93 | True | True |
| v360-calibration-001 | W0 | Outcome_I48 | Outcome_I48 | True | True |
| v360-calibration-002 | C0 | Outcome_E87 | Outcome_E87 | True | True |
| v360-calibration-002 | W0 | Outcome_N34 | Outcome_N34 | True | True |
| v360-calibration-003 | C0 | Outcome_L24 | Outcome_L24 | True | True |
| v360-calibration-003 | W0 | Outcome_P70 | Outcome_P70 | True | True |
| v360-calibration-004 | C0 | Outcome_N09 | Outcome_N09 | True | True |
| v360-calibration-004 | W0 | Outcome_I15 | Outcome_I15 | True | True |
| v360-calibration-005 | C0 | Outcome_M36 | Outcome_M36 | True | True |
| v360-calibration-005 | W0 | Outcome_Z51 | Outcome_Z51 | True | True |
| v360-calibration-006 | C0 | Outcome_M73 | Outcome_M73 | True | True |
| v360-calibration-006 | W0 | Outcome_A15 | Outcome_A15 | True | True |
| v360-calibration-007 | C0 | Outcome_R32 | Outcome_R32 | True | True |
| v360-calibration-007 | W0 | Outcome_A64 | Outcome_A64 | True | True |
| v360-calibration-008 | C0 | Outcome_C61 | Outcome_C61 | True | True |
| v360-calibration-008 | W0 | Outcome_H92 | Outcome_H92 | True | True |
| v360-calibration-009 | C0 | Outcome_S45 | Outcome_S45 | True | True |
| v360-calibration-009 | W0 | Outcome_D81 | Outcome_D81 | True | True |
| v360-calibration-010 | C0 | Outcome_V88 | Outcome_V88 | True | True |
| v360-calibration-010 | W0 | Outcome_X40 | Outcome_X40 | True | True |
| v360-calibration-011 | C0 | Outcome_B21 | Outcome_B21 | True | True |
| v360-calibration-011 | W0 | Outcome_C69 | Outcome_C69 | True | True |
| v360-calibration-012 | C0 | Outcome_W11 | Outcome_W11 | True | True |
| v360-calibration-012 | W0 | Outcome_A20 | Outcome_A20 | True | True |
| v360-calibration-013 | C0 | Outcome_D95 | Outcome_D95 | True | True |
| v360-calibration-013 | W0 | Outcome_L31 | Outcome_L31 | True | True |
| v360-calibration-014 | C0 | Outcome_B00 | Outcome_B00 | True | True |
| v360-calibration-014 | W0 | Outcome_A74 | Outcome_A74 | True | True |
| v360-calibration-015 | C0 | Outcome_T88 | Outcome_T88 | True | True |
| v360-calibration-015 | W0 | Outcome_K40 | Outcome_K40 | True | True |
| v360-calibration-016 | C0 | Outcome_X89 | Outcome_X89 | True | True |
| v360-calibration-016 | W0 | Outcome_Q30 | Outcome_Q30 | True | True |
| v360-calibration-017 | C0 | UNKNOWN | Outcome_E53 | False | True |
| v360-calibration-017 | W0 | Outcome_H41 | Outcome_H41 | True | True |
| v360-calibration-018 | C0 | Outcome_M04 | Outcome_M04 | True | True |
| v360-calibration-018 | W0 | Outcome_J28 | Outcome_J28 | True | True |
| v360-calibration-019 | C0 | Outcome_V51 | Outcome_V51 | True | True |
| v360-calibration-019 | W0 | Outcome_W79 | Outcome_W79 | True | True |
| v360-calibration-020 | C0 | Outcome_K93 | Outcome_K93 | True | True |
| v360-calibration-020 | W0 | Outcome_G48 | Outcome_G48 | True | True |

### FULL_UNKNOWN -> MINIMAL_NO_UNKNOWN

| Case | State | Before | After | Before correct | After correct |
|---|---|---|---|---|---|
| v360-calibration-001 | C0 | Outcome_F93 | Outcome_F93 | True | True |
| v360-calibration-001 | W0 | Outcome_I48 | Outcome_I48 | True | True |
| v360-calibration-002 | C0 | Outcome_E87 | Outcome_E87 | True | True |
| v360-calibration-002 | W0 | Outcome_N34 | Outcome_N34 | True | True |
| v360-calibration-003 | C0 | Outcome_L24 | Outcome_L24 | True | True |
| v360-calibration-003 | W0 | Outcome_P70 | Outcome_P70 | True | True |
| v360-calibration-004 | C0 | Outcome_N09 | Outcome_N09 | True | True |
| v360-calibration-004 | W0 | Outcome_I15 | Outcome_I15 | True | True |
| v360-calibration-005 | C0 | Outcome_M36 | Outcome_M36 | True | True |
| v360-calibration-005 | W0 | Outcome_Z51 | Outcome_Z51 | True | True |
| v360-calibration-006 | C0 | Outcome_M73 | Outcome_M73 | True | True |
| v360-calibration-006 | W0 | Outcome_A15 | Outcome_A15 | True | True |
| v360-calibration-007 | C0 | Outcome_R32 | Outcome_R32 | True | True |
| v360-calibration-007 | W0 | Outcome_A64 | Outcome_A64 | True | True |
| v360-calibration-008 | C0 | Outcome_C61 | Outcome_C61 | True | True |
| v360-calibration-008 | W0 | Outcome_H92 | Outcome_H92 | True | True |
| v360-calibration-009 | C0 | Outcome_S45 | Outcome_S45 | True | True |
| v360-calibration-009 | W0 | Outcome_D81 | Outcome_D81 | True | True |
| v360-calibration-010 | C0 | Outcome_V88 | Outcome_V88 | True | True |
| v360-calibration-010 | W0 | Outcome_X40 | Outcome_X40 | True | True |
| v360-calibration-011 | C0 | Outcome_B21 | Outcome_B21 | True | True |
| v360-calibration-011 | W0 | Outcome_C69 | Outcome_C69 | True | True |
| v360-calibration-012 | C0 | Outcome_W11 | Outcome_W11 | True | True |
| v360-calibration-012 | W0 | Outcome_A20 | Outcome_A20 | True | True |
| v360-calibration-013 | C0 | Outcome_D95 | Outcome_D95 | True | True |
| v360-calibration-013 | W0 | Outcome_L31 | Outcome_L31 | True | True |
| v360-calibration-014 | C0 | Outcome_B00 | Outcome_B00 | True | True |
| v360-calibration-014 | W0 | Outcome_A74 | Outcome_A74 | True | True |
| v360-calibration-015 | C0 | Outcome_T88 | Outcome_T88 | True | True |
| v360-calibration-015 | W0 | Outcome_K40 | Outcome_K40 | True | True |
| v360-calibration-016 | C0 | Outcome_X89 | Outcome_X89 | True | True |
| v360-calibration-016 | W0 | Outcome_Q30 | Outcome_Q30 | True | True |
| v360-calibration-017 | C0 | UNKNOWN | Outcome_E53 | False | True |
| v360-calibration-017 | W0 | Outcome_H41 | Outcome_H41 | True | True |
| v360-calibration-018 | C0 | Outcome_M04 | Outcome_M04 | True | True |
| v360-calibration-018 | W0 | Outcome_J28 | Outcome_J28 | True | True |
| v360-calibration-019 | C0 | Outcome_V51 | Outcome_V51 | True | True |
| v360-calibration-019 | W0 | Outcome_W79 | Outcome_W79 | True | True |
| v360-calibration-020 | C0 | Outcome_K93 | Outcome_K93 | True | True |
| v360-calibration-020 | W0 | Outcome_G48 | Outcome_G48 | True | True |

### FULL_NO_UNKNOWN -> MINIMAL_UNKNOWN

| Case | State | Before | After | Before correct | After correct |
|---|---|---|---|---|---|
| v360-calibration-001 | C0 | Outcome_F93 | Outcome_F93 | True | True |
| v360-calibration-001 | W0 | Outcome_I48 | Outcome_I48 | True | True |
| v360-calibration-002 | C0 | Outcome_E87 | Outcome_E87 | True | True |
| v360-calibration-002 | W0 | Outcome_N34 | Outcome_N34 | True | True |
| v360-calibration-003 | C0 | Outcome_L24 | Outcome_L24 | True | True |
| v360-calibration-003 | W0 | Outcome_P70 | Outcome_P70 | True | True |
| v360-calibration-004 | C0 | Outcome_N09 | Outcome_N09 | True | True |
| v360-calibration-004 | W0 | Outcome_I15 | Outcome_I15 | True | True |
| v360-calibration-005 | C0 | Outcome_M36 | Outcome_M36 | True | True |
| v360-calibration-005 | W0 | Outcome_Z51 | Outcome_Z51 | True | True |
| v360-calibration-006 | C0 | Outcome_M73 | Outcome_M73 | True | True |
| v360-calibration-006 | W0 | Outcome_A15 | Outcome_A15 | True | True |
| v360-calibration-007 | C0 | Outcome_R32 | Outcome_R32 | True | True |
| v360-calibration-007 | W0 | Outcome_A64 | Outcome_A64 | True | True |
| v360-calibration-008 | C0 | Outcome_C61 | Outcome_C61 | True | True |
| v360-calibration-008 | W0 | Outcome_H92 | Outcome_H92 | True | True |
| v360-calibration-009 | C0 | Outcome_S45 | Outcome_S45 | True | True |
| v360-calibration-009 | W0 | Outcome_D81 | Outcome_D81 | True | True |
| v360-calibration-010 | C0 | Outcome_V88 | Outcome_V88 | True | True |
| v360-calibration-010 | W0 | Outcome_X40 | Outcome_X40 | True | True |
| v360-calibration-011 | C0 | Outcome_B21 | Outcome_B21 | True | True |
| v360-calibration-011 | W0 | Outcome_C69 | Outcome_C69 | True | True |
| v360-calibration-012 | C0 | Outcome_W11 | Outcome_W11 | True | True |
| v360-calibration-012 | W0 | Outcome_A20 | Outcome_A20 | True | True |
| v360-calibration-013 | C0 | Outcome_D95 | Outcome_D95 | True | True |
| v360-calibration-013 | W0 | Outcome_L31 | Outcome_L31 | True | True |
| v360-calibration-014 | C0 | Outcome_B00 | Outcome_B00 | True | True |
| v360-calibration-014 | W0 | Outcome_A74 | Outcome_A74 | True | True |
| v360-calibration-015 | C0 | Outcome_T88 | Outcome_T88 | True | True |
| v360-calibration-015 | W0 | Outcome_K40 | Outcome_K40 | True | True |
| v360-calibration-016 | C0 | Outcome_X89 | Outcome_X89 | True | True |
| v360-calibration-016 | W0 | Outcome_Q30 | Outcome_Q30 | True | True |
| v360-calibration-017 | C0 | Outcome_E53 | Outcome_E53 | True | True |
| v360-calibration-017 | W0 | Outcome_H41 | Outcome_H41 | True | True |
| v360-calibration-018 | C0 | Outcome_M04 | Outcome_M04 | True | True |
| v360-calibration-018 | W0 | Outcome_J28 | Outcome_J28 | True | True |
| v360-calibration-019 | C0 | Outcome_V51 | Outcome_V51 | True | True |
| v360-calibration-019 | W0 | Outcome_W79 | Outcome_W79 | True | True |
| v360-calibration-020 | C0 | Outcome_K93 | Outcome_K93 | True | True |
| v360-calibration-020 | W0 | Outcome_G48 | Outcome_G48 | True | True |

### FULL_NO_UNKNOWN -> MINIMAL_NO_UNKNOWN

| Case | State | Before | After | Before correct | After correct |
|---|---|---|---|---|---|
| v360-calibration-001 | C0 | Outcome_F93 | Outcome_F93 | True | True |
| v360-calibration-001 | W0 | Outcome_I48 | Outcome_I48 | True | True |
| v360-calibration-002 | C0 | Outcome_E87 | Outcome_E87 | True | True |
| v360-calibration-002 | W0 | Outcome_N34 | Outcome_N34 | True | True |
| v360-calibration-003 | C0 | Outcome_L24 | Outcome_L24 | True | True |
| v360-calibration-003 | W0 | Outcome_P70 | Outcome_P70 | True | True |
| v360-calibration-004 | C0 | Outcome_N09 | Outcome_N09 | True | True |
| v360-calibration-004 | W0 | Outcome_I15 | Outcome_I15 | True | True |
| v360-calibration-005 | C0 | Outcome_M36 | Outcome_M36 | True | True |
| v360-calibration-005 | W0 | Outcome_Z51 | Outcome_Z51 | True | True |
| v360-calibration-006 | C0 | Outcome_M73 | Outcome_M73 | True | True |
| v360-calibration-006 | W0 | Outcome_A15 | Outcome_A15 | True | True |
| v360-calibration-007 | C0 | Outcome_R32 | Outcome_R32 | True | True |
| v360-calibration-007 | W0 | Outcome_A64 | Outcome_A64 | True | True |
| v360-calibration-008 | C0 | Outcome_C61 | Outcome_C61 | True | True |
| v360-calibration-008 | W0 | Outcome_H92 | Outcome_H92 | True | True |
| v360-calibration-009 | C0 | Outcome_S45 | Outcome_S45 | True | True |
| v360-calibration-009 | W0 | Outcome_D81 | Outcome_D81 | True | True |
| v360-calibration-010 | C0 | Outcome_V88 | Outcome_V88 | True | True |
| v360-calibration-010 | W0 | Outcome_X40 | Outcome_X40 | True | True |
| v360-calibration-011 | C0 | Outcome_B21 | Outcome_B21 | True | True |
| v360-calibration-011 | W0 | Outcome_C69 | Outcome_C69 | True | True |
| v360-calibration-012 | C0 | Outcome_W11 | Outcome_W11 | True | True |
| v360-calibration-012 | W0 | Outcome_A20 | Outcome_A20 | True | True |
| v360-calibration-013 | C0 | Outcome_D95 | Outcome_D95 | True | True |
| v360-calibration-013 | W0 | Outcome_L31 | Outcome_L31 | True | True |
| v360-calibration-014 | C0 | Outcome_B00 | Outcome_B00 | True | True |
| v360-calibration-014 | W0 | Outcome_A74 | Outcome_A74 | True | True |
| v360-calibration-015 | C0 | Outcome_T88 | Outcome_T88 | True | True |
| v360-calibration-015 | W0 | Outcome_K40 | Outcome_K40 | True | True |
| v360-calibration-016 | C0 | Outcome_X89 | Outcome_X89 | True | True |
| v360-calibration-016 | W0 | Outcome_Q30 | Outcome_Q30 | True | True |
| v360-calibration-017 | C0 | Outcome_E53 | Outcome_E53 | True | True |
| v360-calibration-017 | W0 | Outcome_H41 | Outcome_H41 | True | True |
| v360-calibration-018 | C0 | Outcome_M04 | Outcome_M04 | True | True |
| v360-calibration-018 | W0 | Outcome_J28 | Outcome_J28 | True | True |
| v360-calibration-019 | C0 | Outcome_V51 | Outcome_V51 | True | True |
| v360-calibration-019 | W0 | Outcome_W79 | Outcome_W79 | True | True |
| v360-calibration-020 | C0 | Outcome_K93 | Outcome_K93 | True | True |
| v360-calibration-020 | W0 | Outcome_G48 | Outcome_G48 | True | True |

### MINIMAL_UNKNOWN -> MINIMAL_NO_UNKNOWN

| Case | State | Before | After | Before correct | After correct |
|---|---|---|---|---|---|
| v360-calibration-001 | C0 | Outcome_F93 | Outcome_F93 | True | True |
| v360-calibration-001 | W0 | Outcome_I48 | Outcome_I48 | True | True |
| v360-calibration-002 | C0 | Outcome_E87 | Outcome_E87 | True | True |
| v360-calibration-002 | W0 | Outcome_N34 | Outcome_N34 | True | True |
| v360-calibration-003 | C0 | Outcome_L24 | Outcome_L24 | True | True |
| v360-calibration-003 | W0 | Outcome_P70 | Outcome_P70 | True | True |
| v360-calibration-004 | C0 | Outcome_N09 | Outcome_N09 | True | True |
| v360-calibration-004 | W0 | Outcome_I15 | Outcome_I15 | True | True |
| v360-calibration-005 | C0 | Outcome_M36 | Outcome_M36 | True | True |
| v360-calibration-005 | W0 | Outcome_Z51 | Outcome_Z51 | True | True |
| v360-calibration-006 | C0 | Outcome_M73 | Outcome_M73 | True | True |
| v360-calibration-006 | W0 | Outcome_A15 | Outcome_A15 | True | True |
| v360-calibration-007 | C0 | Outcome_R32 | Outcome_R32 | True | True |
| v360-calibration-007 | W0 | Outcome_A64 | Outcome_A64 | True | True |
| v360-calibration-008 | C0 | Outcome_C61 | Outcome_C61 | True | True |
| v360-calibration-008 | W0 | Outcome_H92 | Outcome_H92 | True | True |
| v360-calibration-009 | C0 | Outcome_S45 | Outcome_S45 | True | True |
| v360-calibration-009 | W0 | Outcome_D81 | Outcome_D81 | True | True |
| v360-calibration-010 | C0 | Outcome_V88 | Outcome_V88 | True | True |
| v360-calibration-010 | W0 | Outcome_X40 | Outcome_X40 | True | True |
| v360-calibration-011 | C0 | Outcome_B21 | Outcome_B21 | True | True |
| v360-calibration-011 | W0 | Outcome_C69 | Outcome_C69 | True | True |
| v360-calibration-012 | C0 | Outcome_W11 | Outcome_W11 | True | True |
| v360-calibration-012 | W0 | Outcome_A20 | Outcome_A20 | True | True |
| v360-calibration-013 | C0 | Outcome_D95 | Outcome_D95 | True | True |
| v360-calibration-013 | W0 | Outcome_L31 | Outcome_L31 | True | True |
| v360-calibration-014 | C0 | Outcome_B00 | Outcome_B00 | True | True |
| v360-calibration-014 | W0 | Outcome_A74 | Outcome_A74 | True | True |
| v360-calibration-015 | C0 | Outcome_T88 | Outcome_T88 | True | True |
| v360-calibration-015 | W0 | Outcome_K40 | Outcome_K40 | True | True |
| v360-calibration-016 | C0 | Outcome_X89 | Outcome_X89 | True | True |
| v360-calibration-016 | W0 | Outcome_Q30 | Outcome_Q30 | True | True |
| v360-calibration-017 | C0 | Outcome_E53 | Outcome_E53 | True | True |
| v360-calibration-017 | W0 | Outcome_H41 | Outcome_H41 | True | True |
| v360-calibration-018 | C0 | Outcome_M04 | Outcome_M04 | True | True |
| v360-calibration-018 | W0 | Outcome_J28 | Outcome_J28 | True | True |
| v360-calibration-019 | C0 | Outcome_V51 | Outcome_V51 | True | True |
| v360-calibration-019 | W0 | Outcome_W79 | Outcome_W79 | True | True |
| v360-calibration-020 | C0 | Outcome_K93 | Outcome_K93 | True | True |
| v360-calibration-020 | W0 | Outcome_G48 | Outcome_G48 | True | True |
