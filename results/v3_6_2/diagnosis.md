# Context robustness diagnosis

**ROBUST_CONTEXT_ASSAY**

The minimal state-propagation primitive remains highly reliable under up to24 irrelevant state-to-outcome records in this synthetic setting.

Monotonic collapse=False; paired success counts K0/K4/K12/K24=[40, 40, 40, 40].
Off-target by K={'0': 0, '4': 0, '12': 0, '24': 0}; total 0/320. These are model outputs; they do not themselves imply infrastructure failure.
Sensitive triggers, when baseline valid: {'K24_gold': False, 'K24_wrong': False, 'K24_paired': False, 'paired_lost_at_least_four': False, 'monotonic_collapse': False, 'off_target_over_two': False}.

## Per-K intervals and complete categories

### K0

- A_C: 40/40; Wilson95% interval [0.9123783988027135, 1.0].
- A_W: 40/40; Wilson95% interval [0.9123783988027135, 1.0].
- S: 40/40; Wilson95% interval [0.9123783988027135, 1.0].
- Categories by arm: {'C0': {'C': 40, 'Cp': 0, 'UNKNOWN': 0, 'OTHER': 0, 'INVALID': 0}, 'W0': {'C': 0, 'Cp': 40, 'UNKNOWN': 0, 'OTHER': 0, 'INVALID': 0}}.

### K4

- A_C: 40/40; Wilson95% interval [0.9123783988027135, 1.0].
- A_W: 40/40; Wilson95% interval [0.9123783988027135, 1.0].
- S: 40/40; Wilson95% interval [0.9123783988027135, 1.0].
- Categories by arm: {'C0': {'C': 40, 'Cp': 0, 'UNKNOWN': 0, 'OTHER': 0, 'INVALID': 0}, 'W0': {'C': 0, 'Cp': 40, 'UNKNOWN': 0, 'OTHER': 0, 'INVALID': 0}}.

### K12

- A_C: 40/40; Wilson95% interval [0.9123783988027135, 1.0].
- A_W: 40/40; Wilson95% interval [0.9123783988027135, 1.0].
- S: 40/40; Wilson95% interval [0.9123783988027135, 1.0].
- Categories by arm: {'C0': {'C': 40, 'Cp': 0, 'UNKNOWN': 0, 'OTHER': 0, 'INVALID': 0}, 'W0': {'C': 0, 'Cp': 40, 'UNKNOWN': 0, 'OTHER': 0, 'INVALID': 0}}.

### K24

- A_C: 40/40; Wilson95% interval [0.9123783988027135, 1.0].
- A_W: 40/40; Wilson95% interval [0.9123783988027135, 1.0].
- S: 40/40; Wilson95% interval [0.9123783988027135, 1.0].
- Categories by arm: {'C0': {'C': 40, 'Cp': 0, 'UNKNOWN': 0, 'OTHER': 0, 'INVALID': 0}, 'W0': {'C': 0, 'Cp': 40, 'UNKNOWN': 0, 'OTHER': 0, 'INVALID': 0}}.

## Paired degradation details

| K vs K0 | ΔC /40 | ΔW /40 | ΔS /40 | Paired lost | Paired gained |
|---|---|---|---|---|---|
| 4 | 0 | 0 | 0 | 0 | 0 |
| 12 | 0 | 0 | 0 | 0 | 0 |
| 24 | 0 | 0 | 0 | 0 | 0 |

### K0 → K4

Paired lost cases: []; gained: [].

C0: correct→incorrect 0/40; incorrect→correct 0/40; correct→paired-wrong-or-UNKNOWN 0/40.

| Case | K0 category | New category | K0 output | New output |
|---|---|---|---|---|
| v362-001 | C | C | OUTCOME_V44 | OUTCOME_V44 |
| v362-002 | C | C | OUTCOME_R91 | OUTCOME_R91 |
| v362-003 | C | C | OUTCOME_H21 | OUTCOME_H21 |
| v362-004 | C | C | OUTCOME_N39 | OUTCOME_N39 |
| v362-005 | C | C | OUTCOME_G62 | OUTCOME_G62 |
| v362-006 | C | C | OUTCOME_F09 | OUTCOME_F09 |
| v362-007 | C | C | OUTCOME_I67 | OUTCOME_I67 |
| v362-008 | C | C | OUTCOME_A99 | OUTCOME_A99 |
| v362-009 | C | C | OUTCOME_W32 | OUTCOME_W32 |
| v362-010 | C | C | OUTCOME_X55 | OUTCOME_X55 |
| v362-011 | C | C | OUTCOME_V35 | OUTCOME_V35 |
| v362-012 | C | C | OUTCOME_L05 | OUTCOME_L05 |
| v362-013 | C | C | OUTCOME_S33 | OUTCOME_S33 |
| v362-014 | C | C | OUTCOME_F95 | OUTCOME_F95 |
| v362-015 | C | C | OUTCOME_N44 | OUTCOME_N44 |
| v362-016 | C | C | OUTCOME_I97 | OUTCOME_I97 |
| v362-017 | C | C | OUTCOME_Y69 | OUTCOME_Y69 |
| v362-018 | C | C | OUTCOME_L07 | OUTCOME_L07 |
| v362-019 | C | C | OUTCOME_L42 | OUTCOME_L42 |
| v362-020 | C | C | OUTCOME_X99 | OUTCOME_X99 |
| v362-021 | C | C | OUTCOME_M24 | OUTCOME_M24 |
| v362-022 | C | C | OUTCOME_K15 | OUTCOME_K15 |
| v362-023 | C | C | OUTCOME_F06 | OUTCOME_F06 |
| v362-024 | C | C | OUTCOME_Q96 | OUTCOME_Q96 |
| v362-025 | C | C | OUTCOME_N56 | OUTCOME_N56 |
| v362-026 | C | C | OUTCOME_K41 | OUTCOME_K41 |
| v362-027 | C | C | OUTCOME_B74 | OUTCOME_B74 |
| v362-028 | C | C | OUTCOME_O79 | OUTCOME_O79 |
| v362-029 | C | C | OUTCOME_D59 | OUTCOME_D59 |
| v362-030 | C | C | OUTCOME_B87 | OUTCOME_B87 |
| v362-031 | C | C | OUTCOME_W29 | OUTCOME_W29 |
| v362-032 | C | C | OUTCOME_N35 | OUTCOME_N35 |
| v362-033 | C | C | OUTCOME_Y37 | OUTCOME_Y37 |
| v362-034 | C | C | OUTCOME_F71 | OUTCOME_F71 |
| v362-035 | C | C | OUTCOME_B83 | OUTCOME_B83 |
| v362-036 | C | C | OUTCOME_Y61 | OUTCOME_Y61 |
| v362-037 | C | C | OUTCOME_I71 | OUTCOME_I71 |
| v362-038 | C | C | OUTCOME_L92 | OUTCOME_L92 |
| v362-039 | C | C | OUTCOME_P95 | OUTCOME_P95 |
| v362-040 | C | C | OUTCOME_S16 | OUTCOME_S16 |

W0: correct→incorrect 0/40; incorrect→correct 0/40; correct→paired-wrong-or-UNKNOWN 0/40.

| Case | K0 category | New category | K0 output | New output |
|---|---|---|---|---|
| v362-001 | Cp | Cp | OUTCOME_I44 | OUTCOME_I44 |
| v362-002 | Cp | Cp | OUTCOME_P02 | OUTCOME_P02 |
| v362-003 | Cp | Cp | OUTCOME_P45 | OUTCOME_P45 |
| v362-004 | Cp | Cp | OUTCOME_B88 | OUTCOME_B88 |
| v362-005 | Cp | Cp | OUTCOME_Q28 | OUTCOME_Q28 |
| v362-006 | Cp | Cp | OUTCOME_D96 | OUTCOME_D96 |
| v362-007 | Cp | Cp | OUTCOME_D56 | OUTCOME_D56 |
| v362-008 | Cp | Cp | OUTCOME_F88 | OUTCOME_F88 |
| v362-009 | Cp | Cp | OUTCOME_H07 | OUTCOME_H07 |
| v362-010 | Cp | Cp | OUTCOME_P65 | OUTCOME_P65 |
| v362-011 | Cp | Cp | OUTCOME_N55 | OUTCOME_N55 |
| v362-012 | Cp | Cp | OUTCOME_O57 | OUTCOME_O57 |
| v362-013 | Cp | Cp | OUTCOME_X07 | OUTCOME_X07 |
| v362-014 | Cp | Cp | OUTCOME_N90 | OUTCOME_N90 |
| v362-015 | Cp | Cp | OUTCOME_O26 | OUTCOME_O26 |
| v362-016 | Cp | Cp | OUTCOME_F32 | OUTCOME_F32 |
| v362-017 | Cp | Cp | OUTCOME_Q86 | OUTCOME_Q86 |
| v362-018 | Cp | Cp | OUTCOME_K34 | OUTCOME_K34 |
| v362-019 | Cp | Cp | OUTCOME_O39 | OUTCOME_O39 |
| v362-020 | Cp | Cp | OUTCOME_X22 | OUTCOME_X22 |
| v362-021 | Cp | Cp | OUTCOME_X36 | OUTCOME_X36 |
| v362-022 | Cp | Cp | OUTCOME_W75 | OUTCOME_W75 |
| v362-023 | Cp | Cp | OUTCOME_P39 | OUTCOME_P39 |
| v362-024 | Cp | Cp | OUTCOME_F96 | OUTCOME_F96 |
| v362-025 | Cp | Cp | OUTCOME_I22 | OUTCOME_I22 |
| v362-026 | Cp | Cp | OUTCOME_T10 | OUTCOME_T10 |
| v362-027 | Cp | Cp | OUTCOME_H14 | OUTCOME_H14 |
| v362-028 | Cp | Cp | OUTCOME_F11 | OUTCOME_F11 |
| v362-029 | Cp | Cp | OUTCOME_R44 | OUTCOME_R44 |
| v362-030 | Cp | Cp | OUTCOME_T21 | OUTCOME_T21 |
| v362-031 | Cp | Cp | OUTCOME_D82 | OUTCOME_D82 |
| v362-032 | Cp | Cp | OUTCOME_A61 | OUTCOME_A61 |
| v362-033 | Cp | Cp | OUTCOME_S73 | OUTCOME_S73 |
| v362-034 | Cp | Cp | OUTCOME_D78 | OUTCOME_D78 |
| v362-035 | Cp | Cp | OUTCOME_T38 | OUTCOME_T38 |
| v362-036 | Cp | Cp | OUTCOME_R60 | OUTCOME_R60 |
| v362-037 | Cp | Cp | OUTCOME_C73 | OUTCOME_C73 |
| v362-038 | Cp | Cp | OUTCOME_G35 | OUTCOME_G35 |
| v362-039 | Cp | Cp | OUTCOME_N26 | OUTCOME_N26 |
| v362-040 | Cp | Cp | OUTCOME_D58 | OUTCOME_D58 |

### K0 → K12

Paired lost cases: []; gained: [].

C0: correct→incorrect 0/40; incorrect→correct 0/40; correct→paired-wrong-or-UNKNOWN 0/40.

| Case | K0 category | New category | K0 output | New output |
|---|---|---|---|---|
| v362-001 | C | C | OUTCOME_V44 | OUTCOME_V44 |
| v362-002 | C | C | OUTCOME_R91 | OUTCOME_R91 |
| v362-003 | C | C | OUTCOME_H21 | OUTCOME_H21 |
| v362-004 | C | C | OUTCOME_N39 | OUTCOME_N39 |
| v362-005 | C | C | OUTCOME_G62 | OUTCOME_G62 |
| v362-006 | C | C | OUTCOME_F09 | OUTCOME_F09 |
| v362-007 | C | C | OUTCOME_I67 | OUTCOME_I67 |
| v362-008 | C | C | OUTCOME_A99 | OUTCOME_A99 |
| v362-009 | C | C | OUTCOME_W32 | OUTCOME_W32 |
| v362-010 | C | C | OUTCOME_X55 | OUTCOME_X55 |
| v362-011 | C | C | OUTCOME_V35 | OUTCOME_V35 |
| v362-012 | C | C | OUTCOME_L05 | OUTCOME_L05 |
| v362-013 | C | C | OUTCOME_S33 | OUTCOME_S33 |
| v362-014 | C | C | OUTCOME_F95 | OUTCOME_F95 |
| v362-015 | C | C | OUTCOME_N44 | OUTCOME_N44 |
| v362-016 | C | C | OUTCOME_I97 | OUTCOME_I97 |
| v362-017 | C | C | OUTCOME_Y69 | OUTCOME_Y69 |
| v362-018 | C | C | OUTCOME_L07 | OUTCOME_L07 |
| v362-019 | C | C | OUTCOME_L42 | OUTCOME_L42 |
| v362-020 | C | C | OUTCOME_X99 | OUTCOME_X99 |
| v362-021 | C | C | OUTCOME_M24 | OUTCOME_M24 |
| v362-022 | C | C | OUTCOME_K15 | OUTCOME_K15 |
| v362-023 | C | C | OUTCOME_F06 | OUTCOME_F06 |
| v362-024 | C | C | OUTCOME_Q96 | OUTCOME_Q96 |
| v362-025 | C | C | OUTCOME_N56 | OUTCOME_N56 |
| v362-026 | C | C | OUTCOME_K41 | OUTCOME_K41 |
| v362-027 | C | C | OUTCOME_B74 | OUTCOME_B74 |
| v362-028 | C | C | OUTCOME_O79 | OUTCOME_O79 |
| v362-029 | C | C | OUTCOME_D59 | OUTCOME_D59 |
| v362-030 | C | C | OUTCOME_B87 | OUTCOME_B87 |
| v362-031 | C | C | OUTCOME_W29 | OUTCOME_W29 |
| v362-032 | C | C | OUTCOME_N35 | OUTCOME_N35 |
| v362-033 | C | C | OUTCOME_Y37 | OUTCOME_Y37 |
| v362-034 | C | C | OUTCOME_F71 | OUTCOME_F71 |
| v362-035 | C | C | OUTCOME_B83 | OUTCOME_B83 |
| v362-036 | C | C | OUTCOME_Y61 | OUTCOME_Y61 |
| v362-037 | C | C | OUTCOME_I71 | OUTCOME_I71 |
| v362-038 | C | C | OUTCOME_L92 | OUTCOME_L92 |
| v362-039 | C | C | OUTCOME_P95 | OUTCOME_P95 |
| v362-040 | C | C | OUTCOME_S16 | OUTCOME_S16 |

W0: correct→incorrect 0/40; incorrect→correct 0/40; correct→paired-wrong-or-UNKNOWN 0/40.

| Case | K0 category | New category | K0 output | New output |
|---|---|---|---|---|
| v362-001 | Cp | Cp | OUTCOME_I44 | OUTCOME_I44 |
| v362-002 | Cp | Cp | OUTCOME_P02 | OUTCOME_P02 |
| v362-003 | Cp | Cp | OUTCOME_P45 | OUTCOME_P45 |
| v362-004 | Cp | Cp | OUTCOME_B88 | OUTCOME_B88 |
| v362-005 | Cp | Cp | OUTCOME_Q28 | OUTCOME_Q28 |
| v362-006 | Cp | Cp | OUTCOME_D96 | OUTCOME_D96 |
| v362-007 | Cp | Cp | OUTCOME_D56 | OUTCOME_D56 |
| v362-008 | Cp | Cp | OUTCOME_F88 | OUTCOME_F88 |
| v362-009 | Cp | Cp | OUTCOME_H07 | OUTCOME_H07 |
| v362-010 | Cp | Cp | OUTCOME_P65 | OUTCOME_P65 |
| v362-011 | Cp | Cp | OUTCOME_N55 | OUTCOME_N55 |
| v362-012 | Cp | Cp | OUTCOME_O57 | OUTCOME_O57 |
| v362-013 | Cp | Cp | OUTCOME_X07 | OUTCOME_X07 |
| v362-014 | Cp | Cp | OUTCOME_N90 | OUTCOME_N90 |
| v362-015 | Cp | Cp | OUTCOME_O26 | OUTCOME_O26 |
| v362-016 | Cp | Cp | OUTCOME_F32 | OUTCOME_F32 |
| v362-017 | Cp | Cp | OUTCOME_Q86 | OUTCOME_Q86 |
| v362-018 | Cp | Cp | OUTCOME_K34 | OUTCOME_K34 |
| v362-019 | Cp | Cp | OUTCOME_O39 | OUTCOME_O39 |
| v362-020 | Cp | Cp | OUTCOME_X22 | OUTCOME_X22 |
| v362-021 | Cp | Cp | OUTCOME_X36 | OUTCOME_X36 |
| v362-022 | Cp | Cp | OUTCOME_W75 | OUTCOME_W75 |
| v362-023 | Cp | Cp | OUTCOME_P39 | OUTCOME_P39 |
| v362-024 | Cp | Cp | OUTCOME_F96 | OUTCOME_F96 |
| v362-025 | Cp | Cp | OUTCOME_I22 | OUTCOME_I22 |
| v362-026 | Cp | Cp | OUTCOME_T10 | OUTCOME_T10 |
| v362-027 | Cp | Cp | OUTCOME_H14 | OUTCOME_H14 |
| v362-028 | Cp | Cp | OUTCOME_F11 | OUTCOME_F11 |
| v362-029 | Cp | Cp | OUTCOME_R44 | OUTCOME_R44 |
| v362-030 | Cp | Cp | OUTCOME_T21 | OUTCOME_T21 |
| v362-031 | Cp | Cp | OUTCOME_D82 | OUTCOME_D82 |
| v362-032 | Cp | Cp | OUTCOME_A61 | OUTCOME_A61 |
| v362-033 | Cp | Cp | OUTCOME_S73 | OUTCOME_S73 |
| v362-034 | Cp | Cp | OUTCOME_D78 | OUTCOME_D78 |
| v362-035 | Cp | Cp | OUTCOME_T38 | OUTCOME_T38 |
| v362-036 | Cp | Cp | OUTCOME_R60 | OUTCOME_R60 |
| v362-037 | Cp | Cp | OUTCOME_C73 | OUTCOME_C73 |
| v362-038 | Cp | Cp | OUTCOME_G35 | OUTCOME_G35 |
| v362-039 | Cp | Cp | OUTCOME_N26 | OUTCOME_N26 |
| v362-040 | Cp | Cp | OUTCOME_D58 | OUTCOME_D58 |

### K0 → K24

Paired lost cases: []; gained: [].

C0: correct→incorrect 0/40; incorrect→correct 0/40; correct→paired-wrong-or-UNKNOWN 0/40.

| Case | K0 category | New category | K0 output | New output |
|---|---|---|---|---|
| v362-001 | C | C | OUTCOME_V44 | OUTCOME_V44 |
| v362-002 | C | C | OUTCOME_R91 | OUTCOME_R91 |
| v362-003 | C | C | OUTCOME_H21 | OUTCOME_H21 |
| v362-004 | C | C | OUTCOME_N39 | OUTCOME_N39 |
| v362-005 | C | C | OUTCOME_G62 | OUTCOME_G62 |
| v362-006 | C | C | OUTCOME_F09 | OUTCOME_F09 |
| v362-007 | C | C | OUTCOME_I67 | OUTCOME_I67 |
| v362-008 | C | C | OUTCOME_A99 | OUTCOME_A99 |
| v362-009 | C | C | OUTCOME_W32 | OUTCOME_W32 |
| v362-010 | C | C | OUTCOME_X55 | OUTCOME_X55 |
| v362-011 | C | C | OUTCOME_V35 | OUTCOME_V35 |
| v362-012 | C | C | OUTCOME_L05 | OUTCOME_L05 |
| v362-013 | C | C | OUTCOME_S33 | OUTCOME_S33 |
| v362-014 | C | C | OUTCOME_F95 | OUTCOME_F95 |
| v362-015 | C | C | OUTCOME_N44 | OUTCOME_N44 |
| v362-016 | C | C | OUTCOME_I97 | OUTCOME_I97 |
| v362-017 | C | C | OUTCOME_Y69 | OUTCOME_Y69 |
| v362-018 | C | C | OUTCOME_L07 | OUTCOME_L07 |
| v362-019 | C | C | OUTCOME_L42 | OUTCOME_L42 |
| v362-020 | C | C | OUTCOME_X99 | OUTCOME_X99 |
| v362-021 | C | C | OUTCOME_M24 | OUTCOME_M24 |
| v362-022 | C | C | OUTCOME_K15 | OUTCOME_K15 |
| v362-023 | C | C | OUTCOME_F06 | OUTCOME_F06 |
| v362-024 | C | C | OUTCOME_Q96 | OUTCOME_Q96 |
| v362-025 | C | C | OUTCOME_N56 | OUTCOME_N56 |
| v362-026 | C | C | OUTCOME_K41 | OUTCOME_K41 |
| v362-027 | C | C | OUTCOME_B74 | OUTCOME_B74 |
| v362-028 | C | C | OUTCOME_O79 | OUTCOME_O79 |
| v362-029 | C | C | OUTCOME_D59 | OUTCOME_D59 |
| v362-030 | C | C | OUTCOME_B87 | OUTCOME_B87 |
| v362-031 | C | C | OUTCOME_W29 | OUTCOME_W29 |
| v362-032 | C | C | OUTCOME_N35 | OUTCOME_N35 |
| v362-033 | C | C | OUTCOME_Y37 | OUTCOME_Y37 |
| v362-034 | C | C | OUTCOME_F71 | OUTCOME_F71 |
| v362-035 | C | C | OUTCOME_B83 | OUTCOME_B83 |
| v362-036 | C | C | OUTCOME_Y61 | OUTCOME_Y61 |
| v362-037 | C | C | OUTCOME_I71 | OUTCOME_I71 |
| v362-038 | C | C | OUTCOME_L92 | OUTCOME_L92 |
| v362-039 | C | C | OUTCOME_P95 | OUTCOME_P95 |
| v362-040 | C | C | OUTCOME_S16 | OUTCOME_S16 |

W0: correct→incorrect 0/40; incorrect→correct 0/40; correct→paired-wrong-or-UNKNOWN 0/40.

| Case | K0 category | New category | K0 output | New output |
|---|---|---|---|---|
| v362-001 | Cp | Cp | OUTCOME_I44 | OUTCOME_I44 |
| v362-002 | Cp | Cp | OUTCOME_P02 | OUTCOME_P02 |
| v362-003 | Cp | Cp | OUTCOME_P45 | OUTCOME_P45 |
| v362-004 | Cp | Cp | OUTCOME_B88 | OUTCOME_B88 |
| v362-005 | Cp | Cp | OUTCOME_Q28 | OUTCOME_Q28 |
| v362-006 | Cp | Cp | OUTCOME_D96 | OUTCOME_D96 |
| v362-007 | Cp | Cp | OUTCOME_D56 | OUTCOME_D56 |
| v362-008 | Cp | Cp | OUTCOME_F88 | OUTCOME_F88 |
| v362-009 | Cp | Cp | OUTCOME_H07 | OUTCOME_H07 |
| v362-010 | Cp | Cp | OUTCOME_P65 | OUTCOME_P65 |
| v362-011 | Cp | Cp | OUTCOME_N55 | OUTCOME_N55 |
| v362-012 | Cp | Cp | OUTCOME_O57 | OUTCOME_O57 |
| v362-013 | Cp | Cp | OUTCOME_X07 | OUTCOME_X07 |
| v362-014 | Cp | Cp | OUTCOME_N90 | OUTCOME_N90 |
| v362-015 | Cp | Cp | OUTCOME_O26 | OUTCOME_O26 |
| v362-016 | Cp | Cp | OUTCOME_F32 | OUTCOME_F32 |
| v362-017 | Cp | Cp | OUTCOME_Q86 | OUTCOME_Q86 |
| v362-018 | Cp | Cp | OUTCOME_K34 | OUTCOME_K34 |
| v362-019 | Cp | Cp | OUTCOME_O39 | OUTCOME_O39 |
| v362-020 | Cp | Cp | OUTCOME_X22 | OUTCOME_X22 |
| v362-021 | Cp | Cp | OUTCOME_X36 | OUTCOME_X36 |
| v362-022 | Cp | Cp | OUTCOME_W75 | OUTCOME_W75 |
| v362-023 | Cp | Cp | OUTCOME_P39 | OUTCOME_P39 |
| v362-024 | Cp | Cp | OUTCOME_F96 | OUTCOME_F96 |
| v362-025 | Cp | Cp | OUTCOME_I22 | OUTCOME_I22 |
| v362-026 | Cp | Cp | OUTCOME_T10 | OUTCOME_T10 |
| v362-027 | Cp | Cp | OUTCOME_H14 | OUTCOME_H14 |
| v362-028 | Cp | Cp | OUTCOME_F11 | OUTCOME_F11 |
| v362-029 | Cp | Cp | OUTCOME_R44 | OUTCOME_R44 |
| v362-030 | Cp | Cp | OUTCOME_T21 | OUTCOME_T21 |
| v362-031 | Cp | Cp | OUTCOME_D82 | OUTCOME_D82 |
| v362-032 | Cp | Cp | OUTCOME_A61 | OUTCOME_A61 |
| v362-033 | Cp | Cp | OUTCOME_S73 | OUTCOME_S73 |
| v362-034 | Cp | Cp | OUTCOME_D78 | OUTCOME_D78 |
| v362-035 | Cp | Cp | OUTCOME_T38 | OUTCOME_T38 |
| v362-036 | Cp | Cp | OUTCOME_R60 | OUTCOME_R60 |
| v362-037 | Cp | Cp | OUTCOME_C73 | OUTCOME_C73 |
| v362-038 | Cp | Cp | OUTCOME_G35 | OUTCOME_G35 |
| v362-039 | Cp | Cp | OUTCOME_N26 | OUTCOME_N26 |
| v362-040 | Cp | Cp | OUTCOME_D58 | OUTCOME_D58 |

## Position diagnosis

| K24 position | C0 /12 | W0 /12 | UNKNOWN /24 | OTHER+INVALID /24 |
|---|---|---|---|---|
| beginning | 12 | 12 | 0 | 0 |
| middle | 12 | 12 | 0 | 0 |
| end | 12 | 12 | 0 | 0 |

Complete per-case position transitions are recorded in position_diagnostic_metrics.json. Differences within this12-case subset diagnose sensitivity to moving the pair; they do not identify an internal retrieval mechanism.
Identical primary/secondary K24 prompts: 24; token-identical repeats: 24.

## Limits

Same-case nested records preserve ordering and pair region, but longer context necessarily changes absolute distances. K0 cannot balance three regions with only two mappings. The K24 diagnostic is the prespecified12-case subset, not a new40-case replication. Each state/outcome is arbitrary; the findings do not establish real-world factual reasoning or natural hallucination propagation.
