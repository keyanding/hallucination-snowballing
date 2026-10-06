# Development-only interface policy

Frozen before confirmation inference.

```json
{
  "route": "N",
  "difficulty": "EASY",
  "gates": {
    "EASY": {
      "N": {
        "passed": true,
        "checks": {
          "coverage": true,
          "record_three_of_four": true,
          "record_four_of_four": true,
          "no_earliest_record_flag": true,
          "N_L_agreement": true
        },
        "observed_wrong_yield": 0
      },
      "R": {
        "passed": true,
        "checks": {
          "coverage": true,
          "record_three_of_four": true,
          "record_four_of_four": true,
          "no_earliest_record_flag": true,
          "N_L_agreement": true
        },
        "observed_wrong_yield": 0
      }
    },
    "MID": {
      "N": {
        "passed": true,
        "checks": {
          "coverage": true,
          "record_three_of_four": true,
          "record_four_of_four": true,
          "no_earliest_record_flag": true,
          "N_L_agreement": true
        },
        "observed_wrong_yield": 1
      },
      "R": {
        "passed": true,
        "checks": {
          "coverage": true,
          "record_three_of_four": true,
          "record_four_of_four": true,
          "no_earliest_record_flag": true,
          "N_L_agreement": true
        },
        "observed_wrong_yield": 0
      }
    },
    "HARD": {
      "N": {
        "passed": false,
        "checks": {
          "coverage": true,
          "record_three_of_four": true,
          "record_four_of_four": false,
          "no_earliest_record_flag": false,
          "N_L_agreement": true
        },
        "observed_wrong_yield": 5
      },
      "R": {
        "passed": false,
        "checks": {
          "coverage": false,
          "record_three_of_four": true,
          "record_four_of_four": false,
          "no_earliest_record_flag": false,
          "N_L_agreement": true
        },
        "observed_wrong_yield": 0
      }
    }
  },
  "development_gate": {
    "passed": true,
    "checks": {
      "coverage": true,
      "record_three_of_four": true,
      "record_four_of_four": true,
      "no_earliest_record_flag": true,
      "N_L_agreement": true
    },
    "observed_wrong_yield": 0
  },
  "claim": "natural single-trajectory first-hop selection",
  "confirmation_with_R": true,
  "v3_5_executed": false,
  "created_utc": "2026-10-06T06:55:54.722708+00:00",
  "development_metrics_sha256": "638852dda4c69cf046f333500e194dcdd3817e02413ae6ba76d91bd5db849452",
  "confirmation_calls_so_far": 0
}
```
