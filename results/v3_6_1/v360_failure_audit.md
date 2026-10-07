# Static audit of v3.6.0

All 20 calibration cases; zero new model calls. REVERSE/ENTITY_LABEL failure means failed invariance vs C0; correctness is separately recorded.

| Case | Gold line | C0 incorrect | Reverse changed | Reverse incorrect | Entity changed | Entity incorrect | Any mapped UNKNOWN |
|---|---|---|---|---|---|---|---|
| v360-calibration-001 | 1 | True | True | False | True | False | True |
| v360-calibration-002 | 1 | False | False | False | False | False | False |
| v360-calibration-003 | 2 | False | False | False | False | False | False |
| v360-calibration-004 | 1 | False | False | False | False | False | False |
| v360-calibration-005 | 2 | False | False | False | False | False | False |
| v360-calibration-006 | 1 | False | True | True | False | False | True |
| v360-calibration-007 | 2 | False | False | False | False | False | False |
| v360-calibration-008 | 1 | False | False | False | False | False | False |
| v360-calibration-009 | 1 | False | False | False | False | False | False |
| v360-calibration-010 | 1 | False | True | True | False | False | True |
| v360-calibration-011 | 1 | False | False | False | False | False | False |
| v360-calibration-012 | 2 | True | True | False | True | False | True |
| v360-calibration-013 | 2 | False | False | False | False | False | False |
| v360-calibration-014 | 1 | False | False | False | False | False | False |
| v360-calibration-015 | 1 | False | False | False | False | False | False |
| v360-calibration-016 | 2 | False | False | False | False | False | False |
| v360-calibration-017 | 2 | True | True | False | True | False | True |
| v360-calibration-018 | 2 | False | False | False | False | False | False |
| v360-calibration-019 | 2 | False | False | False | False | False | False |
| v360-calibration-020 | 2 | False | False | False | False | False | False |

## Required descriptive checks

1. C0 failures by gold mapping line: {'1': {'total': 10, 'failures': 1}, '2': {'total': 10, 'failures': 2}}.
2. Gold-state token lengths, failed vs passed: {'passed': {4: 17}, 'failed': {4: 3}}.
3. Gold-outcome token lengths: {'passed': {4: 17}, 'failed': {4: 3}}.
4. Entity token lengths: {'passed': {4: 17}, 'failed': {4: 3}}.
5. All IDs share a role prefix by construction. Letter/tens/units contingency counts for all cases are recorded in the JSON; three failures cannot establish a lexical cause.
6. Reversal transitions: {'total_invariance_failures': 5, 'C0_wrong_reverse_correct': 3, 'C0_correct_reverse_wrong': 2}.
7. Entity-label transitions: {'total_invariance_failures': 3, 'C0_wrong_entity_correct': 3, 'C0_correct_entity_wrong': 0}.

## Every identifier

| Case | Field | Raw | Token IDs | Tokens | Characters | Mapping line |
|---|---|---|---|---|---|---|
| v360-calibration-001 | entity | Entity_J44 | [3030, 10598, 19, 19] | 4 | 10 | None |
| v360-calibration-001 | alternate_entity | Entity_M55 | [3030, 1245, 20, 20] | 4 | 10 | None |
| v360-calibration-001 | gold_state | State_D49 | [1397, 1557, 19, 24] | 4 | 9 | 1 |
| v360-calibration-001 | wrong_state | State_J94 | [1397, 10598, 24, 19] | 4 | 9 | 2 |
| v360-calibration-001 | gold_outcome | Outcome_F93 | [73380, 1400, 24, 18] | 4 | 11 | 1 |
| v360-calibration-001 | wrong_outcome | Outcome_I48 | [73380, 7959, 19, 23] | 4 | 11 | 2 |
| v360-calibration-001 | unmapped_state | State_W42 | [1397, 2763, 19, 17] | 4 | 9 | None |
| v360-calibration-002 | entity | Entity_H61 | [3030, 2039, 21, 16] | 4 | 10 | None |
| v360-calibration-002 | alternate_entity | Entity_D22 | [3030, 1557, 17, 17] | 4 | 10 | None |
| v360-calibration-002 | gold_state | State_C68 | [1397, 920, 21, 23] | 4 | 9 | 1 |
| v360-calibration-002 | wrong_state | State_K13 | [1397, 10102, 16, 18] | 4 | 9 | 2 |
| v360-calibration-002 | gold_outcome | Outcome_E87 | [73380, 2089, 23, 22] | 4 | 11 | 1 |
| v360-calibration-002 | wrong_outcome | Outcome_N34 | [73380, 1604, 18, 19] | 4 | 11 | 2 |
| v360-calibration-002 | unmapped_state | State_S67 | [1397, 1098, 21, 22] | 4 | 9 | None |
| v360-calibration-003 | entity | Entity_F60 | [3030, 1400, 21, 15] | 4 | 10 | None |
| v360-calibration-003 | alternate_entity | Entity_W16 | [3030, 2763, 16, 21] | 4 | 10 | None |
| v360-calibration-003 | gold_state | State_Z38 | [1397, 12302, 18, 23] | 4 | 9 | 2 |
| v360-calibration-003 | wrong_state | State_Z43 | [1397, 12302, 19, 18] | 4 | 9 | 1 |
| v360-calibration-003 | gold_outcome | Outcome_L24 | [73380, 2351, 17, 19] | 4 | 11 | 2 |
| v360-calibration-003 | wrong_outcome | Outcome_P70 | [73380, 1088, 22, 15] | 4 | 11 | 1 |
| v360-calibration-003 | unmapped_state | State_T72 | [1397, 1139, 22, 17] | 4 | 9 | None |
| v360-calibration-004 | entity | Entity_G19 | [3030, 2646, 16, 24] | 4 | 10 | None |
| v360-calibration-004 | alternate_entity | Entity_L30 | [3030, 2351, 18, 15] | 4 | 10 | None |
| v360-calibration-004 | gold_state | State_O94 | [1397, 2232, 24, 19] | 4 | 9 | 1 |
| v360-calibration-004 | wrong_state | State_M06 | [1397, 1245, 15, 21] | 4 | 9 | 2 |
| v360-calibration-004 | gold_outcome | Outcome_N09 | [73380, 1604, 15, 24] | 4 | 11 | 1 |
| v360-calibration-004 | wrong_outcome | Outcome_I15 | [73380, 7959, 16, 20] | 4 | 11 | 2 |
| v360-calibration-004 | unmapped_state | State_S38 | [1397, 1098, 18, 23] | 4 | 9 | None |
| v360-calibration-005 | entity | Entity_D18 | [3030, 1557, 16, 23] | 4 | 10 | None |
| v360-calibration-005 | alternate_entity | Entity_I24 | [3030, 7959, 17, 19] | 4 | 10 | None |
| v360-calibration-005 | gold_state | State_R64 | [1397, 2568, 21, 19] | 4 | 9 | 2 |
| v360-calibration-005 | wrong_state | State_R00 | [1397, 2568, 15, 15] | 4 | 9 | 1 |
| v360-calibration-005 | gold_outcome | Outcome_M36 | [73380, 1245, 18, 21] | 4 | 11 | 2 |
| v360-calibration-005 | wrong_outcome | Outcome_Z51 | [73380, 12302, 20, 16] | 4 | 11 | 1 |
| v360-calibration-005 | unmapped_state | State_E86 | [1397, 2089, 23, 21] | 4 | 9 | None |
| v360-calibration-006 | entity | Entity_V79 | [3030, 2334, 22, 24] | 4 | 10 | None |
| v360-calibration-006 | alternate_entity | Entity_G37 | [3030, 2646, 18, 22] | 4 | 10 | None |
| v360-calibration-006 | gold_state | State_Y82 | [1397, 10626, 23, 17] | 4 | 9 | 1 |
| v360-calibration-006 | wrong_state | State_W27 | [1397, 2763, 17, 22] | 4 | 9 | 2 |
| v360-calibration-006 | gold_outcome | Outcome_M73 | [73380, 1245, 22, 18] | 4 | 11 | 1 |
| v360-calibration-006 | wrong_outcome | Outcome_A15 | [73380, 1566, 16, 20] | 4 | 11 | 2 |
| v360-calibration-006 | unmapped_state | State_N95 | [1397, 1604, 24, 20] | 4 | 9 | None |
| v360-calibration-007 | entity | Entity_N53 | [3030, 1604, 20, 18] | 4 | 10 | None |
| v360-calibration-007 | alternate_entity | Entity_G54 | [3030, 2646, 20, 19] | 4 | 10 | None |
| v360-calibration-007 | gold_state | State_T18 | [1397, 1139, 16, 23] | 4 | 9 | 2 |
| v360-calibration-007 | wrong_state | State_E40 | [1397, 2089, 19, 15] | 4 | 9 | 1 |
| v360-calibration-007 | gold_outcome | Outcome_R32 | [73380, 2568, 18, 17] | 4 | 11 | 2 |
| v360-calibration-007 | wrong_outcome | Outcome_A64 | [73380, 1566, 21, 19] | 4 | 11 | 1 |
| v360-calibration-007 | unmapped_state | State_X38 | [1397, 6859, 18, 23] | 4 | 9 | None |
| v360-calibration-008 | entity | Entity_E79 | [3030, 2089, 22, 24] | 4 | 10 | None |
| v360-calibration-008 | alternate_entity | Entity_Z91 | [3030, 12302, 24, 16] | 4 | 10 | None |
| v360-calibration-008 | gold_state | State_H25 | [1397, 2039, 17, 20] | 4 | 9 | 1 |
| v360-calibration-008 | wrong_state | State_P32 | [1397, 1088, 18, 17] | 4 | 9 | 2 |
| v360-calibration-008 | gold_outcome | Outcome_C61 | [73380, 920, 21, 16] | 4 | 11 | 1 |
| v360-calibration-008 | wrong_outcome | Outcome_H92 | [73380, 2039, 24, 17] | 4 | 11 | 2 |
| v360-calibration-008 | unmapped_state | State_N96 | [1397, 1604, 24, 21] | 4 | 9 | None |
| v360-calibration-009 | entity | Entity_E83 | [3030, 2089, 23, 18] | 4 | 10 | None |
| v360-calibration-009 | alternate_entity | Entity_Q05 | [3030, 13337, 15, 20] | 4 | 10 | None |
| v360-calibration-009 | gold_state | State_J02 | [1397, 10598, 15, 17] | 4 | 9 | 1 |
| v360-calibration-009 | wrong_state | State_H06 | [1397, 2039, 15, 21] | 4 | 9 | 2 |
| v360-calibration-009 | gold_outcome | Outcome_S45 | [73380, 1098, 19, 20] | 4 | 11 | 1 |
| v360-calibration-009 | wrong_outcome | Outcome_D81 | [73380, 1557, 23, 16] | 4 | 11 | 2 |
| v360-calibration-009 | unmapped_state | State_U03 | [1397, 6665, 15, 18] | 4 | 9 | None |
| v360-calibration-010 | entity | Entity_E59 | [3030, 2089, 20, 24] | 4 | 10 | None |
| v360-calibration-010 | alternate_entity | Entity_L13 | [3030, 2351, 16, 18] | 4 | 10 | None |
| v360-calibration-010 | gold_state | State_Y20 | [1397, 10626, 17, 15] | 4 | 9 | 1 |
| v360-calibration-010 | wrong_state | State_A36 | [1397, 1566, 18, 21] | 4 | 9 | 2 |
| v360-calibration-010 | gold_outcome | Outcome_V88 | [73380, 2334, 23, 23] | 4 | 11 | 1 |
| v360-calibration-010 | wrong_outcome | Outcome_X40 | [73380, 6859, 19, 15] | 4 | 11 | 2 |
| v360-calibration-010 | unmapped_state | State_U30 | [1397, 6665, 18, 15] | 4 | 9 | None |
| v360-calibration-011 | entity | Entity_L33 | [3030, 2351, 18, 18] | 4 | 10 | None |
| v360-calibration-011 | alternate_entity | Entity_S16 | [3030, 1098, 16, 21] | 4 | 10 | None |
| v360-calibration-011 | gold_state | State_J91 | [1397, 10598, 24, 16] | 4 | 9 | 1 |
| v360-calibration-011 | wrong_state | State_I31 | [1397, 7959, 18, 16] | 4 | 9 | 2 |
| v360-calibration-011 | gold_outcome | Outcome_B21 | [73380, 1668, 17, 16] | 4 | 11 | 1 |
| v360-calibration-011 | wrong_outcome | Outcome_C69 | [73380, 920, 21, 24] | 4 | 11 | 2 |
| v360-calibration-011 | unmapped_state | State_F89 | [1397, 1400, 23, 24] | 4 | 9 | None |
| v360-calibration-012 | entity | Entity_R10 | [3030, 2568, 16, 15] | 4 | 10 | None |
| v360-calibration-012 | alternate_entity | Entity_X55 | [3030, 6859, 20, 20] | 4 | 10 | None |
| v360-calibration-012 | gold_state | State_M41 | [1397, 1245, 19, 16] | 4 | 9 | 2 |
| v360-calibration-012 | wrong_state | State_E16 | [1397, 2089, 16, 21] | 4 | 9 | 1 |
| v360-calibration-012 | gold_outcome | Outcome_W11 | [73380, 2763, 16, 16] | 4 | 11 | 2 |
| v360-calibration-012 | wrong_outcome | Outcome_A20 | [73380, 1566, 17, 15] | 4 | 11 | 1 |
| v360-calibration-012 | unmapped_state | State_O89 | [1397, 2232, 23, 24] | 4 | 9 | None |
| v360-calibration-013 | entity | Entity_A61 | [3030, 1566, 21, 16] | 4 | 10 | None |
| v360-calibration-013 | alternate_entity | Entity_X07 | [3030, 6859, 15, 22] | 4 | 10 | None |
| v360-calibration-013 | gold_state | State_Z41 | [1397, 12302, 19, 16] | 4 | 9 | 2 |
| v360-calibration-013 | wrong_state | State_V34 | [1397, 2334, 18, 19] | 4 | 9 | 1 |
| v360-calibration-013 | gold_outcome | Outcome_D95 | [73380, 1557, 24, 20] | 4 | 11 | 2 |
| v360-calibration-013 | wrong_outcome | Outcome_L31 | [73380, 2351, 18, 16] | 4 | 11 | 1 |
| v360-calibration-013 | unmapped_state | State_F29 | [1397, 1400, 17, 24] | 4 | 9 | None |
| v360-calibration-014 | entity | Entity_U55 | [3030, 6665, 20, 20] | 4 | 10 | None |
| v360-calibration-014 | alternate_entity | Entity_T09 | [3030, 1139, 15, 24] | 4 | 10 | None |
| v360-calibration-014 | gold_state | State_F19 | [1397, 1400, 16, 24] | 4 | 9 | 1 |
| v360-calibration-014 | wrong_state | State_L73 | [1397, 2351, 22, 18] | 4 | 9 | 2 |
| v360-calibration-014 | gold_outcome | Outcome_B00 | [73380, 1668, 15, 15] | 4 | 11 | 1 |
| v360-calibration-014 | wrong_outcome | Outcome_A74 | [73380, 1566, 22, 19] | 4 | 11 | 2 |
| v360-calibration-014 | unmapped_state | State_N21 | [1397, 1604, 17, 16] | 4 | 9 | None |
| v360-calibration-015 | entity | Entity_I23 | [3030, 7959, 17, 18] | 4 | 10 | None |
| v360-calibration-015 | alternate_entity | Entity_F24 | [3030, 1400, 17, 19] | 4 | 10 | None |
| v360-calibration-015 | gold_state | State_R43 | [1397, 2568, 19, 18] | 4 | 9 | 1 |
| v360-calibration-015 | wrong_state | State_X78 | [1397, 6859, 22, 23] | 4 | 9 | 2 |
| v360-calibration-015 | gold_outcome | Outcome_T88 | [73380, 1139, 23, 23] | 4 | 11 | 1 |
| v360-calibration-015 | wrong_outcome | Outcome_K40 | [73380, 10102, 19, 15] | 4 | 11 | 2 |
| v360-calibration-015 | unmapped_state | State_L96 | [1397, 2351, 24, 21] | 4 | 9 | None |
| v360-calibration-016 | entity | Entity_R01 | [3030, 2568, 15, 16] | 4 | 10 | None |
| v360-calibration-016 | alternate_entity | Entity_P78 | [3030, 1088, 22, 23] | 4 | 10 | None |
| v360-calibration-016 | gold_state | State_B20 | [1397, 1668, 17, 15] | 4 | 9 | 2 |
| v360-calibration-016 | wrong_state | State_D05 | [1397, 1557, 15, 20] | 4 | 9 | 1 |
| v360-calibration-016 | gold_outcome | Outcome_X89 | [73380, 6859, 23, 24] | 4 | 11 | 2 |
| v360-calibration-016 | wrong_outcome | Outcome_Q30 | [73380, 13337, 18, 15] | 4 | 11 | 1 |
| v360-calibration-016 | unmapped_state | State_D90 | [1397, 1557, 24, 15] | 4 | 9 | None |
| v360-calibration-017 | entity | Entity_K46 | [3030, 10102, 19, 21] | 4 | 10 | None |
| v360-calibration-017 | alternate_entity | Entity_B59 | [3030, 1668, 20, 24] | 4 | 10 | None |
| v360-calibration-017 | gold_state | State_J32 | [1397, 10598, 18, 17] | 4 | 9 | 2 |
| v360-calibration-017 | wrong_state | State_I11 | [1397, 7959, 16, 16] | 4 | 9 | 1 |
| v360-calibration-017 | gold_outcome | Outcome_E53 | [73380, 2089, 20, 18] | 4 | 11 | 2 |
| v360-calibration-017 | wrong_outcome | Outcome_H41 | [73380, 2039, 19, 16] | 4 | 11 | 1 |
| v360-calibration-017 | unmapped_state | State_V08 | [1397, 2334, 15, 23] | 4 | 9 | None |
| v360-calibration-018 | entity | Entity_P02 | [3030, 1088, 15, 17] | 4 | 10 | None |
| v360-calibration-018 | alternate_entity | Entity_W35 | [3030, 2763, 18, 20] | 4 | 10 | None |
| v360-calibration-018 | gold_state | State_D36 | [1397, 1557, 18, 21] | 4 | 9 | 2 |
| v360-calibration-018 | wrong_state | State_Q80 | [1397, 13337, 23, 15] | 4 | 9 | 1 |
| v360-calibration-018 | gold_outcome | Outcome_M04 | [73380, 1245, 15, 19] | 4 | 11 | 2 |
| v360-calibration-018 | wrong_outcome | Outcome_J28 | [73380, 10598, 17, 23] | 4 | 11 | 1 |
| v360-calibration-018 | unmapped_state | State_L86 | [1397, 2351, 23, 21] | 4 | 9 | None |
| v360-calibration-019 | entity | Entity_A34 | [3030, 1566, 18, 19] | 4 | 10 | None |
| v360-calibration-019 | alternate_entity | Entity_O18 | [3030, 2232, 16, 23] | 4 | 10 | None |
| v360-calibration-019 | gold_state | State_M70 | [1397, 1245, 22, 15] | 4 | 9 | 2 |
| v360-calibration-019 | wrong_state | State_T91 | [1397, 1139, 24, 16] | 4 | 9 | 1 |
| v360-calibration-019 | gold_outcome | Outcome_V51 | [73380, 2334, 20, 16] | 4 | 11 | 2 |
| v360-calibration-019 | wrong_outcome | Outcome_W79 | [73380, 2763, 22, 24] | 4 | 11 | 1 |
| v360-calibration-019 | unmapped_state | State_D75 | [1397, 1557, 22, 20] | 4 | 9 | None |
| v360-calibration-020 | entity | Entity_P81 | [3030, 1088, 23, 16] | 4 | 10 | None |
| v360-calibration-020 | alternate_entity | Entity_U89 | [3030, 6665, 23, 24] | 4 | 10 | None |
| v360-calibration-020 | gold_state | State_D25 | [1397, 1557, 17, 20] | 4 | 9 | 2 |
| v360-calibration-020 | wrong_state | State_M13 | [1397, 1245, 16, 18] | 4 | 9 | 1 |
| v360-calibration-020 | gold_outcome | Outcome_K93 | [73380, 10102, 24, 18] | 4 | 11 | 2 |
| v360-calibration-020 | wrong_outcome | Outcome_G48 | [73380, 2646, 19, 23] | 4 | 11 | 1 |
| v360-calibration-020 | unmapped_state | State_G69 | [1397, 2646, 21, 24] | 4 | 9 | None |
