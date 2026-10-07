# Diagnosis

**TWO_HOP_PIPELINE_VALIDATED**

The synthetic modular two-hop pipeline passed: actual inferred states forwarded into the validated Current state interface produced the corresponding outcomes, and counterfactual supplied states predictably switched downstream outcomes.

## Calibration

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

Condition categories: {'U-A': {'B': 40, 'Bp': 0, 'OTHER_STATE': 0, 'INVALID': 0}, 'U-B': {'B': 0, 'Bp': 40, 'OTHER_STATE': 0, 'INVALID': 0}, 'D-A': {'C': 40, 'Cp': 0, 'OTHER_OUTCOME': 0, 'UNKNOWN': 0, 'INVALID': 0}, 'D-B': {'C': 0, 'Cp': 40, 'OTHER_OUTCOME': 0, 'UNKNOWN': 0, 'INVALID': 0}}.
Pipeline outcome categories: {'C': 40, 'Cp': 0, 'OTHER_OUTCOME': 0, 'UNKNOWN': 0, 'INVALID': 0}.
Strict pipeline failure sources: [].

## Paired upstream categories

```json
{
  "B": {
    "B": 0,
    "Bp": 40,
    "OTHER_STATE": 0,
    "INVALID": 0
  },
  "Bp": {
    "B": 0,
    "Bp": 0,
    "OTHER_STATE": 0,
    "INVALID": 0
  },
  "OTHER_STATE": {
    "B": 0,
    "Bp": 0,
    "OTHER_STATE": 0,
    "INVALID": 0
  },
  "INVALID": {
    "B": 0,
    "Bp": 0,
    "OTHER_STATE": 0,
    "INVALID": 0
  }
}
```

## Paired downstream categories

```json
{
  "C": {
    "C": 0,
    "Cp": 40,
    "OTHER_OUTCOME": 0,
    "UNKNOWN": 0,
    "INVALID": 0
  },
  "Cp": {
    "C": 0,
    "Cp": 0,
    "OTHER_OUTCOME": 0,
    "UNKNOWN": 0,
    "INVALID": 0
  },
  "OTHER_OUTCOME": {
    "C": 0,
    "Cp": 0,
    "OTHER_OUTCOME": 0,
    "UNKNOWN": 0,
    "INVALID": 0
  },
  "UNKNOWN": {
    "C": 0,
    "Cp": 0,
    "OTHER_OUTCOME": 0,
    "UNKNOWN": 0,
    "INVALID": 0
  },
  "INVALID": {
    "C": 0,
    "Cp": 0,
    "OTHER_OUTCOME": 0,
    "UNKNOWN": 0,
    "INVALID": 0
  }
}
```

## Separate diagnostics

The matched shell diagnostic yielded VALIDATED 20/20 and RECORDED 17/20. The validated interface had higher observed exact-output accuracy on these cases. This compares complete prompt shells, not the heading alone, on ten fresh cases; it does not establish a unique cause of historical v3.6.3 failures or an internal mechanism.
Integrated execution did not meet the separate readiness threshold.

```json
{
  "evaluated": true,
  "shells": {
    "VALIDATED": {
      "exact_accuracy": {
        "count": 20,
        "denominator": 20,
        "rate": 1.0
      },
      "by_state": {
        "D-A": {
          "count": 10,
          "denominator": 10,
          "rate": 1.0
        },
        "D-B": {
          "count": 10,
          "denominator": 10,
          "rate": 1.0
        }
      },
      "invalid_count": 0,
      "explanation_format_count": 0,
      "prefix_omission_count": 0,
      "truncation_count": 0,
      "category_counts": {
        "C": 10,
        "Cp": 10,
        "OTHER_OUTCOME": 0,
        "UNKNOWN": 0,
        "INVALID": 0
      }
    },
    "RECORDED": {
      "exact_accuracy": {
        "count": 17,
        "denominator": 20,
        "rate": 0.85
      },
      "by_state": {
        "D-A": {
          "count": 9,
          "denominator": 10,
          "rate": 0.9
        },
        "D-B": {
          "count": 8,
          "denominator": 10,
          "rate": 0.8
        }
      },
      "invalid_count": 3,
      "explanation_format_count": 3,
      "prefix_omission_count": 0,
      "truncation_count": 3,
      "category_counts": {
        "C": 9,
        "Cp": 8,
        "OTHER_OUTCOME": 0,
        "UNKNOWN": 0,
        "INVALID": 3
      }
    }
  },
  "paired_transitions": [
    {
      "case_id": "v3631-diagnostic-001",
      "condition": "D-A",
      "validated": "C",
      "recorded": "C",
      "validated_output": "OUTCOME_B38",
      "recorded_output": "OUTCOME_B38",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-001",
      "condition": "D-B",
      "validated": "Cp",
      "recorded": "Cp",
      "validated_output": "OUTCOME_M93",
      "recorded_output": "OUTCOME_M93",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-002",
      "condition": "D-A",
      "validated": "C",
      "recorded": "INVALID",
      "validated_output": "OUTCOME_W41",
      "recorded_output": "The outcome implied by the recorded intermediate result STATE_Q22 is OUTCOME_W",
      "validated_correct": true,
      "recorded_correct": false
    },
    {
      "case_id": "v3631-diagnostic-002",
      "condition": "D-B",
      "validated": "Cp",
      "recorded": "Cp",
      "validated_output": "OUTCOME_Y35",
      "recorded_output": "OUTCOME_Y35",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-003",
      "condition": "D-A",
      "validated": "C",
      "recorded": "C",
      "validated_output": "OUTCOME_O42",
      "recorded_output": "OUTCOME_O42",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-003",
      "condition": "D-B",
      "validated": "Cp",
      "recorded": "Cp",
      "validated_output": "OUTCOME_V68",
      "recorded_output": "OUTCOME_V68",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-004",
      "condition": "D-A",
      "validated": "C",
      "recorded": "C",
      "validated_output": "OUTCOME_R47",
      "recorded_output": "OUTCOME_R47",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-004",
      "condition": "D-B",
      "validated": "Cp",
      "recorded": "Cp",
      "validated_output": "OUTCOME_K06",
      "recorded_output": "OUTCOME_K06",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-005",
      "condition": "D-A",
      "validated": "C",
      "recorded": "C",
      "validated_output": "OUTCOME_C85",
      "recorded_output": "OUTCOME_C85",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-005",
      "condition": "D-B",
      "validated": "Cp",
      "recorded": "Cp",
      "validated_output": "OUTCOME_F00",
      "recorded_output": "OUTCOME_F00",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-006",
      "condition": "D-A",
      "validated": "C",
      "recorded": "C",
      "validated_output": "OUTCOME_S50",
      "recorded_output": "OUTCOME_S50",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-006",
      "condition": "D-B",
      "validated": "Cp",
      "recorded": "Cp",
      "validated_output": "OUTCOME_D48",
      "recorded_output": "OUTCOME_D48",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-007",
      "condition": "D-A",
      "validated": "C",
      "recorded": "C",
      "validated_output": "OUTCOME_L28",
      "recorded_output": "OUTCOME_L28",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-007",
      "condition": "D-B",
      "validated": "Cp",
      "recorded": "INVALID",
      "validated_output": "OUTCOME_L17",
      "recorded_output": "The outcome implied by the recorded intermediate result STATE_R02 is OUTCOME_L",
      "validated_correct": true,
      "recorded_correct": false
    },
    {
      "case_id": "v3631-diagnostic-008",
      "condition": "D-A",
      "validated": "C",
      "recorded": "C",
      "validated_output": "OUTCOME_A27",
      "recorded_output": "OUTCOME_A27",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-008",
      "condition": "D-B",
      "validated": "Cp",
      "recorded": "Cp",
      "validated_output": "OUTCOME_D92",
      "recorded_output": "OUTCOME_D92",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-009",
      "condition": "D-A",
      "validated": "C",
      "recorded": "C",
      "validated_output": "OUTCOME_Q04",
      "recorded_output": "OUTCOME_Q04",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-009",
      "condition": "D-B",
      "validated": "Cp",
      "recorded": "INVALID",
      "validated_output": "OUTCOME_D06",
      "recorded_output": "The recorded intermediate result is STATE_O28.  \n\nDownstream mapping: STATE",
      "validated_correct": true,
      "recorded_correct": false
    },
    {
      "case_id": "v3631-diagnostic-010",
      "condition": "D-A",
      "validated": "C",
      "recorded": "C",
      "validated_output": "OUTCOME_H48",
      "recorded_output": "OUTCOME_H48",
      "validated_correct": true,
      "recorded_correct": true
    },
    {
      "case_id": "v3631-diagnostic-010",
      "condition": "D-B",
      "validated": "Cp",
      "recorded": "Cp",
      "validated_output": "OUTCOME_X63",
      "recorded_output": "OUTCOME_X63",
      "validated_correct": true,
      "recorded_correct": true
    }
  ],
  "recorded_only_failures": 3,
  "validated_only_failures": 0,
  "non_gating": true,
  "counts_may_overlap": true
}
```

## Boundary

D-A/D-B differ only by Current state. PIPELINE-A forwards actual normalized U-A, including wrong/unmapped well-formed states; INVALID upstream skips without replacement. Strict E2E requires both U-A=B and pipeline=C.
This does not establish natural hallucination propagation, spontaneous error rates, injected/natural-error equivalence, internal neural mechanism, SHAR/HalluSE performance or real-world reasoning. Integrated final-answer accuracy does not prove internal intermediate use. No next phase was run.
