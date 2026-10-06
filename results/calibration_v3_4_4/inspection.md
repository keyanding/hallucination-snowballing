# Paired case inspection

L is constrained listed choice; N/R are unconstrained free generation. S means per-token mean log-likelihood (EOS excluded). Gold margin = gold minus best wrong. Old diagnostic rows do not borrow prior L outputs into new paired comparisons.

## development / v344-development-01 / EASY

Gold: **Tinnu Anand**. First-hop subquestion (N/R): `Who is the credited director of Film T95882?`. Listed wording: `Which candidate is the credited director of Film T95882?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Tinnu Anand.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Leopoldo Torre Nilsson | Tinnu Anand | True | 1.3398 |
| P2 | Tinnu Anand | Tinnu Anand | True | 3.9978 |
| P3 | Jan Svěrák | Tinnu Anand | True | 2.7125 |
| P4 | Ildikó Enyedi | Tinnu Anand | True | 2.2188 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Tinnu Anand | IN_SET_VALID | Tinnu Anand |
| R1 | Tinnu Anand | IN_SET_VALID | Tinnu Anand |
| R2 | Tinnu Anand | IN_SET_VALID | Ildikó Enyedi |
| R3 | Tinnu Anand | IN_SET_VALID | Leopoldo Torre Nilsson |
| R4 | Tinnu Anand | IN_SET_VALID | Jan Svěrák |

N raw: `"Tinnu Anand"`. R aggregate: Tinnu Anand; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-01 / MID

Gold: **Tinnu Anand**. First-hop subquestion (N/R): `Who is the credited director of Film T95882?`. Listed wording: `Which candidate is the credited director of Film T95882?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Tinnu Anand.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Leopoldo Torre Nilsson | Tinnu Anand | True | 1.5781 |
| P2 | Tinnu Anand | Tinnu Anand | True | 3.8017 |
| P3 | Jan Svěrák | Tinnu Anand | True | 2.8125 |
| P4 | Ildikó Enyedi | Tinnu Anand | True | 2.7522 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Tinnu Anand | IN_SET_VALID | Tinnu Anand |
| R1 | Tinnu Anand | IN_SET_VALID | Tinnu Anand |
| R2 | Tinnu Anand | IN_SET_VALID | Ildikó Enyedi |
| R3 | Tinnu Anand | IN_SET_VALID | Leopoldo Torre Nilsson |
| R4 | Tinnu Anand | IN_SET_VALID | Jan Svěrák |

N raw: `"Tinnu Anand"`. R aggregate: Tinnu Anand; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-01 / HARD

Gold: **Tinnu Anand**. First-hop subquestion (N/R): `Who is the credited director of Film T95882?`. Listed wording: `Which candidate is the credited director of Film T95882?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Tinnu Anand.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | True | -0.1195 |
| P2 | Tinnu Anand | Tinnu Anand | True | 3.5273 |
| P3 | Jan Svěrák | Jan Svěrák | True | -0.5125 |
| P4 | Ildikó Enyedi | Tinnu Anand | True | 0.8347 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Tinnu Anand | IN_SET_VALID | Tinnu Anand |
| R1 | Tinnu Anand | IN_SET_VALID | Tinnu Anand |
| R2 | — | TRUNCATED | Ildikó Enyedi |
| R3 | Tinnu Anand | IN_SET_VALID | Leopoldo Torre Nilsson |
| R4 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |

N raw: `"Tinnu Anand"`. R aggregate: UNSTABLE_OR_UNRESOLVED; R observed identity changes: True; R all four valid: False. L list sensitivity: True; N/L disagreement: none or ineligible.

Diagnostic anomalies (raw only here; full logs preserve every output):

- {"plan_id": "development/v344-development-01/HARD/R2", "F": null, "F_category": "TRUNCATED", "C": null, "S_mean": "Ildikó Enyedi", "S_sum": "Ildikó Enyedi", "raw_f": "Ildikó Enyedi\n\nWait, let's reevaluate.\n\nWe are asked: Who is the credited director of Film T95882?\n\nWe start at Film T95882.\n\nWe follow only **credited-director** links until we reach a record that names a candidate.\n\nGraph-links:\n\n- Film T95882 has credited-director link R33186.\n- R33186 has credited-direct", "note": "Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified."}

## development / v344-development-02 / EASY

Gold: **Leopoldo Torre Nilsson**. First-hop subquestion (N/R): `Who is the credited director of Film T13533?`. Listed wording: `Which candidate is the credited director of Film T13533?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: TIE (missing).

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Yuen Woo-ping | Yuen Woo-ping | True | -1.2148 |
| P2 | Ildikó Enyedi | Yuen Woo-ping | True | -1.1055 |
| P3 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | True | 4.0380 |
| P4 | Tinnu Anand | Leopoldo Torre Nilsson | True | 3.8862 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Leopoldo Torre Nilsson | IN_SET_VALID | Ildikó Enyedi |
| R1 | Leopoldo Torre Nilsson | IN_SET_VALID | Ildikó Enyedi |
| R2 | Leopoldo Torre Nilsson | IN_SET_VALID | Tinnu Anand |
| R3 | Leopoldo Torre Nilsson | IN_SET_VALID | Yuen Woo-ping |
| R4 | Leopoldo Torre Nilsson | IN_SET_VALID | Leopoldo Torre Nilsson |

N raw: `"Leopoldo Torre Nilsson"`. R aggregate: Leopoldo Torre Nilsson; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-02 / MID

Gold: **Leopoldo Torre Nilsson**. First-hop subquestion (N/R): `Who is the credited director of Film T13533?`. Listed wording: `Which candidate is the credited director of Film T13533?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Leopoldo Torre Nilsson.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Yuen Woo-ping | Yuen Woo-ping | True | -1.8789 |
| P2 | Ildikó Enyedi | Leopoldo Torre Nilsson | True | 0.0630 |
| P3 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | True | 3.5067 |
| P4 | Tinnu Anand | Leopoldo Torre Nilsson | True | 2.5067 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Leopoldo Torre Nilsson | IN_SET_VALID | Ildikó Enyedi |
| R1 | Leopoldo Torre Nilsson | IN_SET_VALID | Ildikó Enyedi |
| R2 | Leopoldo Torre Nilsson | IN_SET_VALID | Tinnu Anand |
| R3 | Leopoldo Torre Nilsson | IN_SET_VALID | Yuen Woo-ping |
| R4 | Leopoldo Torre Nilsson | IN_SET_VALID | Leopoldo Torre Nilsson |

N raw: `"Leopoldo Torre Nilsson"`. R aggregate: Leopoldo Torre Nilsson; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-02 / HARD

Gold: **Leopoldo Torre Nilsson**. First-hop subquestion (N/R): `Who is the credited director of Film T13533?`. Listed wording: `Which candidate is the credited director of Film T13533?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: TIE (missing).

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Yuen Woo-ping | Yuen Woo-ping | True | -2.6953 |
| P2 | Ildikó Enyedi | Ildikó Enyedi | True | -0.7433 |
| P3 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | True | 3.2562 |
| P4 | Tinnu Anand | Tinnu Anand | True | -0.3350 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Leopoldo Torre Nilsson | IN_SET_VALID | Ildikó Enyedi |
| R1 | Leopoldo Torre Nilsson | IN_SET_VALID | Ildikó Enyedi |
| R2 | Leopoldo Torre Nilsson | IN_SET_VALID | Tinnu Anand |
| R3 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |
| R4 | Leopoldo Torre Nilsson | IN_SET_VALID | Leopoldo Torre Nilsson |

N raw: `"Leopoldo Torre Nilsson"`. R aggregate: Leopoldo Torre Nilsson; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

Diagnostic anomalies (raw only here; full logs preserve every output):

- {"plan_id": "development/v344-development-02/HARD/L2", "F": null, "F_category": "TRUNCATED", "C": "Ildikó Enyedi", "S_mean": "Ildikó Enyedi", "S_sum": "Ildikó Enyedi", "raw_f": "Ildikó Enyedi\n\nExplanation: We start at Film T13533 and follow only the \"credited-director\" links until we reach a record that names a candidate.\n\n- T13533 has credited-director link R94513.\n- R94513 has credited-director link R31235.\n- R31235 has credited-director link R82097", "note": "Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified."}

## development / v344-development-03 / EASY

Gold: **Walter Hugo Khouri**. First-hop subquestion (N/R): `Who is the credited director of Film T30973?`. Listed wording: `Which candidate is the credited director of Film T30973?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Walter Hugo Khouri.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Robert P. Kerr | Walter Hugo Khouri | True | 2.5585 |
| P2 | León Klimovsky | Walter Hugo Khouri | True | 2.5375 |
| P3 | Walter Hugo Khouri | Walter Hugo Khouri | True | 2.4462 |
| P4 | Vojtěch Jasný | Walter Hugo Khouri | True | 2.2012 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Walter Hugo Khouri | IN_SET_VALID | León Klimovsky |
| R1 | Walter Hugo Khouri | IN_SET_VALID | León Klimovsky |
| R2 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R3 | Walter Hugo Khouri | IN_SET_VALID | Vojtěch Jasný |
| R4 | Walter Hugo Khouri | IN_SET_VALID | Robert P. Kerr |

N raw: `"Walter Hugo Khouri"`. R aggregate: Walter Hugo Khouri; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-03 / MID

Gold: **Walter Hugo Khouri**. First-hop subquestion (N/R): `Who is the credited director of Film T30973?`. Listed wording: `Which candidate is the credited director of Film T30973?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: León Klimovsky.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Robert P. Kerr | Robert P. Kerr | True | -4.1160 |
| P2 | León Klimovsky | León Klimovsky | True | -2.8750 |
| P3 | Walter Hugo Khouri | Walter Hugo Khouri | True | 0.3687 |
| P4 | Vojtěch Jasný | León Klimovsky | True | -1.6438 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | León Klimovsky | IN_SET_VALID | León Klimovsky |
| R1 | León Klimovsky | IN_SET_VALID | León Klimovsky |
| R2 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R3 | Walter Hugo Khouri | IN_SET_VALID | Vojtěch Jasný |
| R4 | Walter Hugo Khouri | IN_SET_VALID | Robert P. Kerr |

N raw: `"León Klimovsky"`. R aggregate: Walter Hugo Khouri; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-03 / HARD

Gold: **Walter Hugo Khouri**. First-hop subquestion (N/R): `Who is the credited director of Film T30973?`. Listed wording: `Which candidate is the credited director of Film T30973?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: TIE (missing).

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Robert P. Kerr | Robert P. Kerr | True | -4.1687 |
| P2 | León Klimovsky | León Klimovsky | True | -4.3031 |
| P3 | Walter Hugo Khouri | Walter Hugo Khouri | True | 0.5687 |
| P4 | Vojtěch Jasný | Vojtěch Jasný | True | -3.5282 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | León Klimovsky | IN_SET_VALID | León Klimovsky |
| R1 | León Klimovsky | IN_SET_VALID | León Klimovsky |
| R2 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R3 | Walter Hugo Khouri | IN_SET_VALID | Vojtěch Jasný |
| R4 | Walter Hugo Khouri | IN_SET_VALID | Robert P. Kerr |

N raw: `"León Klimovsky"`. R aggregate: Walter Hugo Khouri; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-04 / EASY

Gold: **Jan Svěrák**. First-hop subquestion (N/R): `Who is the credited director of Film T92782?`. Listed wording: `Which candidate is the credited director of Film T92782?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Jan Svěrák.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Jan Svěrák | Jan Svěrák | True | 3.8066 |
| P2 | Leopoldo Torre Nilsson | Jan Svěrák | True | 0.2984 |
| P3 | Yuen Woo-ping | Jan Svěrák | True | 0.2500 |
| P4 | Armando Robles Godoy | Jan Svěrák | True | 1.7239 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |
| R1 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |
| R2 | Jan Svěrák | IN_SET_VALID | Armando Robles Godoy |
| R3 | Jan Svěrák | IN_SET_VALID | Yuen Woo-ping |
| R4 | Jan Svěrák | IN_SET_VALID | Leopoldo Torre Nilsson |

N raw: `"Jan Svěrák"`. R aggregate: Jan Svěrák; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-04 / MID

Gold: **Jan Svěrák**. First-hop subquestion (N/R): `Who is the credited director of Film T92782?`. Listed wording: `Which candidate is the credited director of Film T92782?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Jan Svěrák.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Jan Svěrák | Jan Svěrák | True | 3.0605 |
| P2 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | True | -0.2291 |
| P3 | Yuen Woo-ping | Yuen Woo-ping | True | -0.2688 |
| P4 | Armando Robles Godoy | Jan Svěrák | True | 0.9425 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |
| R1 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |
| R2 | Jan Svěrák | IN_SET_VALID | Armando Robles Godoy |
| R3 | Jan Svěrák | IN_SET_VALID | Yuen Woo-ping |
| R4 | Jan Svěrák | IN_SET_VALID | Leopoldo Torre Nilsson |

N raw: `"Jan Svěrák"`. R aggregate: Jan Svěrák; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-04 / HARD

Gold: **Jan Svěrák**. First-hop subquestion (N/R): `Who is the credited director of Film T92782?`. Listed wording: `Which candidate is the credited director of Film T92782?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: TIE (missing).

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Jan Svěrák | Jan Svěrák | True | 2.9375 |
| P2 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | True | -5.0688 |
| P3 | Yuen Woo-ping | Yuen Woo-ping | True | -5.0250 |
| P4 | Armando Robles Godoy | Armando Robles Godoy | True | -1.4813 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |
| R1 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |
| R2 | Jan Svěrák | IN_SET_VALID | Armando Robles Godoy |
| R3 | Jan Svěrák | IN_SET_VALID | Yuen Woo-ping |
| R4 | Jan Svěrák | IN_SET_VALID | Leopoldo Torre Nilsson |

N raw: `"Jan Svěrák"`. R aggregate: Jan Svěrák; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-05 / EASY

Gold: **Feng Xiaoning**. First-hop subquestion (N/R): `Who is the credited director of Film T79932?`. Listed wording: `Which candidate is the credited director of Film T79932?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Feng Xiaoning.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Rolf Schübel | Feng Xiaoning | True | 4.0833 |
| P2 | Fridrikh Ermler | Feng Xiaoning | True | 3.4978 |
| P3 | Feng Xiaoning | Feng Xiaoning | True | 4.4542 |
| P4 | Anil Das | Feng Xiaoning | True | 4.0848 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Feng Xiaoning | IN_SET_VALID | Anil Das |
| R1 | Feng Xiaoning | IN_SET_VALID | Anil Das |
| R2 | Feng Xiaoning | IN_SET_VALID | Rolf Schübel |
| R3 | Feng Xiaoning | IN_SET_VALID | Fridrikh Ermler |
| R4 | Feng Xiaoning | IN_SET_VALID | Feng Xiaoning |

N raw: `"Feng Xiaoning"`. R aggregate: Feng Xiaoning; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-05 / MID

Gold: **Feng Xiaoning**. First-hop subquestion (N/R): `Who is the credited director of Film T79932?`. Listed wording: `Which candidate is the credited director of Film T79932?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Feng Xiaoning.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Rolf Schübel | Feng Xiaoning | True | 3.4188 |
| P2 | Fridrikh Ermler | Feng Xiaoning | True | 3.0848 |
| P3 | Feng Xiaoning | Feng Xiaoning | True | 4.4977 |
| P4 | Anil Das | Feng Xiaoning | True | 3.8918 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Feng Xiaoning | IN_SET_VALID | Anil Das |
| R1 | Feng Xiaoning | IN_SET_VALID | Anil Das |
| R2 | Feng Xiaoning | IN_SET_VALID | Rolf Schübel |
| R3 | Feng Xiaoning | IN_SET_VALID | Fridrikh Ermler |
| R4 | Feng Xiaoning | IN_SET_VALID | Feng Xiaoning |

N raw: `"Feng Xiaoning"`. R aggregate: Feng Xiaoning; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-05 / HARD

Gold: **Feng Xiaoning**. First-hop subquestion (N/R): `Who is the credited director of Film T79932?`. Listed wording: `Which candidate is the credited director of Film T79932?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Feng Xiaoning.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Rolf Schübel | Feng Xiaoning | True | 3.2475 |
| P2 | Fridrikh Ermler | Feng Xiaoning | True | 2.3058 |
| P3 | Feng Xiaoning | Feng Xiaoning | True | 3.9743 |
| P4 | Anil Das | Feng Xiaoning | True | 4.1495 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Feng Xiaoning | IN_SET_VALID | Anil Das |
| R1 | Feng Xiaoning | IN_SET_VALID | Anil Das |
| R2 | Feng Xiaoning | IN_SET_VALID | Rolf Schübel |
| R3 | Feng Xiaoning | IN_SET_VALID | Fridrikh Ermler |
| R4 | Feng Xiaoning | IN_SET_VALID | Feng Xiaoning |

N raw: `"Feng Xiaoning"`. R aggregate: Feng Xiaoning; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-06 / EASY

Gold: **Marcello Fondato**. First-hop subquestion (N/R): `Who is the credited director of Film T39322?`. Listed wording: `Which candidate is the credited director of Film T39322?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Marcello Fondato.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Robert P. Kerr | Marcello Fondato | True | 4.5417 |
| P2 | James Goldstone | Marcello Fondato | True | 5.1953 |
| P3 | Bhappi Sonie | Marcello Fondato | True | 1.7917 |
| P4 | Marcello Fondato | Marcello Fondato | True | 5.3698 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Marcello Fondato | IN_SET_VALID | James Goldstone |
| R1 | Marcello Fondato | IN_SET_VALID | James Goldstone |
| R2 | Marcello Fondato | IN_SET_VALID | Bhappi Sonie |
| R3 | Marcello Fondato | IN_SET_VALID | Marcello Fondato |
| R4 | Marcello Fondato | IN_SET_VALID | Robert P. Kerr |

N raw: `"Marcello Fondato"`. R aggregate: Marcello Fondato; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-06 / MID

Gold: **Marcello Fondato**. First-hop subquestion (N/R): `Who is the credited director of Film T39322?`. Listed wording: `Which candidate is the credited director of Film T39322?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Marcello Fondato.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Robert P. Kerr | Marcello Fondato | True | 3.6719 |
| P2 | James Goldstone | Marcello Fondato | True | 4.4479 |
| P3 | Bhappi Sonie | James Goldstone | True | -1.6877 |
| P4 | Marcello Fondato | Marcello Fondato | True | 4.9427 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Marcello Fondato | IN_SET_VALID | James Goldstone |
| R1 | Marcello Fondato | IN_SET_VALID | James Goldstone |
| R2 | Bhappi Sonie | IN_SET_VALID | Bhappi Sonie |
| R3 | Marcello Fondato | IN_SET_VALID | Marcello Fondato |
| R4 | Marcello Fondato | IN_SET_VALID | Robert P. Kerr |

N raw: `"Marcello Fondato"`. R aggregate: Marcello Fondato; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

Diagnostic anomalies (raw only here; full logs preserve every output):

- {"plan_id": "development/v344-development-06/MID/L3", "F": null, "F_category": "TRUNCATED", "C": "James Goldstone", "S_mean": "James Goldstone", "S_sum": "James Goldstone", "raw_f": "James Goldstone\n\nWait. Let's trace the links properly.\n\nWe start at Film T39322.\n\nT39322 has credited-director link R97071.\n\nR97071 has credited-director link R31498.\n\nR31498 has credited-director link R54307.\n\nR54307 names Marcello Fondato.\n\nSo the credited director of T", "note": "Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified."}

## development / v344-development-06 / HARD

Gold: **Marcello Fondato**. First-hop subquestion (N/R): `Who is the credited director of Film T39322?`. Listed wording: `Which candidate is the credited director of Film T39322?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Marcello Fondato.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Robert P. Kerr | Marcello Fondato | True | 3.6562 |
| P2 | James Goldstone | Marcello Fondato | True | 4.8099 |
| P3 | Bhappi Sonie | James Goldstone | True | -1.2785 |
| P4 | Marcello Fondato | Marcello Fondato | True | 4.8464 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Marcello Fondato | IN_SET_VALID | James Goldstone |
| R1 | Marcello Fondato | IN_SET_VALID | James Goldstone |
| R2 | Bhappi Sonie | IN_SET_VALID | Bhappi Sonie |
| R3 | Marcello Fondato | IN_SET_VALID | Marcello Fondato |
| R4 | Marcello Fondato | IN_SET_VALID | Robert P. Kerr |

N raw: `"Marcello Fondato"`. R aggregate: Marcello Fondato; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-07 / EASY

Gold: **Marcello Fondato**. First-hop subquestion (N/R): `Who is the credited director of Film T51971?`. Listed wording: `Which candidate is the credited director of Film T51971?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Marcello Fondato.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Robert P. Kerr | Marcello Fondato | True | 5.6750 |
| P2 | James Goldstone | Marcello Fondato | True | 5.3313 |
| P3 | Marcello Fondato | Marcello Fondato | True | 4.3750 |
| P4 | León Klimovsky | Marcello Fondato | True | 3.5250 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Marcello Fondato | IN_SET_VALID | Robert P. Kerr |
| R1 | Marcello Fondato | IN_SET_VALID | Robert P. Kerr |
| R2 | Marcello Fondato | IN_SET_VALID | Marcello Fondato |
| R3 | Marcello Fondato | IN_SET_VALID | León Klimovsky |
| R4 | Marcello Fondato | IN_SET_VALID | James Goldstone |

N raw: `"Marcello Fondato"`. R aggregate: Marcello Fondato; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-07 / MID

Gold: **Marcello Fondato**. First-hop subquestion (N/R): `Who is the credited director of Film T51971?`. Listed wording: `Which candidate is the credited director of Film T51971?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Marcello Fondato.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Robert P. Kerr | Marcello Fondato | True | 1.4923 |
| P2 | James Goldstone | James Goldstone | True | -0.7595 |
| P3 | Marcello Fondato | Marcello Fondato | True | 3.0281 |
| P4 | León Klimovsky | León Klimovsky | True | -0.6062 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Marcello Fondato | IN_SET_VALID | Robert P. Kerr |
| R1 | Marcello Fondato | IN_SET_VALID | Robert P. Kerr |
| R2 | Marcello Fondato | IN_SET_VALID | Marcello Fondato |
| R3 | Marcello Fondato | IN_SET_VALID | León Klimovsky |
| R4 | Marcello Fondato | IN_SET_VALID | James Goldstone |

N raw: `"Marcello Fondato"`. R aggregate: Marcello Fondato; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

Diagnostic anomalies (raw only here; full logs preserve every output):

- {"plan_id": "development/v344-development-07/MID/L2", "F": null, "F_category": "TRUNCATED", "C": "James Goldstone", "S_mean": "James Goldstone", "S_sum": "James Goldstone", "raw_f": "James Goldstone\n\nWait. Let's retrace carefully.\n\nWe are to find the credited director of Film T51971.\n\nGiven:\n\n- Film T51971 has credited-director link R67914.\n- Record R67914 has credited-director link R16991.\n- Record R16991 has credited-director link R16202.\n- Record R162", "note": "Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified."}

## development / v344-development-07 / HARD

Gold: **Marcello Fondato**. First-hop subquestion (N/R): `Who is the credited director of Film T51971?`. Listed wording: `Which candidate is the credited director of Film T51971?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: TIE (missing).

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Robert P. Kerr | Robert P. Kerr | True | -1.0184 |
| P2 | James Goldstone | James Goldstone | True | -1.8062 |
| P3 | Marcello Fondato | Marcello Fondato | True | 3.9719 |
| P4 | León Klimovsky | León Klimovsky | True | -1.9812 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Marcello Fondato | IN_SET_VALID | Robert P. Kerr |
| R1 | Marcello Fondato | IN_SET_VALID | Robert P. Kerr |
| R2 | Marcello Fondato | IN_SET_VALID | Marcello Fondato |
| R3 | Marcello Fondato | IN_SET_VALID | León Klimovsky |
| R4 | Marcello Fondato | IN_SET_VALID | James Goldstone |

N raw: `"Marcello Fondato"`. R aggregate: Marcello Fondato; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-08 / EASY

Gold: **Helmut Käutner**. First-hop subquestion (N/R): `Who is the credited director of Film T52893?`. Listed wording: `Which candidate is the credited director of Film T52893?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Helmut Käutner.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Gu Changwei | Helmut Käutner | True | 2.3022 |
| P2 | Helmut Käutner | Helmut Käutner | True | 3.1005 |
| P3 | Anil Das | Helmut Käutner | True | 2.3616 |
| P4 | Fridrikh Ermler | Helmut Käutner | True | 2.0268 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Helmut Käutner | IN_SET_VALID | Fridrikh Ermler |
| R1 | Helmut Käutner | IN_SET_VALID | Fridrikh Ermler |
| R2 | Helmut Käutner | IN_SET_VALID | Helmut Käutner |
| R3 | Helmut Käutner | IN_SET_VALID | Gu Changwei |
| R4 | Helmut Käutner | IN_SET_VALID | Anil Das |

N raw: `"Helmut Käutner"`. R aggregate: Helmut Käutner; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-08 / MID

Gold: **Helmut Käutner**. First-hop subquestion (N/R): `Who is the credited director of Film T52893?`. Listed wording: `Which candidate is the credited director of Film T52893?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Helmut Käutner.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Gu Changwei | Gu Changwei | True | 0.0031 |
| P2 | Helmut Käutner | Helmut Käutner | True | 2.9551 |
| P3 | Anil Das | Helmut Käutner | True | 1.6293 |
| P4 | Fridrikh Ermler | Helmut Käutner | True | 1.3750 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Helmut Käutner | IN_SET_VALID | Fridrikh Ermler |
| R1 | Helmut Käutner | IN_SET_VALID | Fridrikh Ermler |
| R2 | Helmut Käutner | IN_SET_VALID | Helmut Käutner |
| R3 | Helmut Käutner | IN_SET_VALID | Gu Changwei |
| R4 | Helmut Käutner | IN_SET_VALID | Anil Das |

N raw: `"Helmut Käutner"`. R aggregate: Helmut Käutner; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

Diagnostic anomalies (raw only here; full logs preserve every output):

- {"plan_id": "development/v344-development-08/MID/L1", "F": "Gu Changwei", "F_category": "IN_SET_VALID", "C": "Gu Changwei", "S_mean": "Helmut Käutner", "S_sum": "Gu Changwei", "raw_f": "Gu Changwei", "note": "Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified."}

## development / v344-development-08 / HARD

Gold: **Helmut Käutner**. First-hop subquestion (N/R): `Who is the credited director of Film T52893?`. Listed wording: `Which candidate is the credited director of Film T52893?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Fridrikh Ermler.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Gu Changwei | Fridrikh Ermler | True | -2.8444 |
| P2 | Helmut Käutner | Helmut Käutner | True | 1.9687 |
| P3 | Anil Das | Anil Das | True | -2.7005 |
| P4 | Fridrikh Ermler | Fridrikh Ermler | True | -2.5521 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Fridrikh Ermler | IN_SET_VALID | Fridrikh Ermler |
| R1 | Fridrikh Ermler | IN_SET_VALID | Fridrikh Ermler |
| R2 | Helmut Käutner | IN_SET_VALID | Helmut Käutner |
| R3 | Helmut Käutner | IN_SET_VALID | Gu Changwei |
| R4 | Helmut Käutner | IN_SET_VALID | Anil Das |

N raw: `"Fridrikh Ermler"`. R aggregate: Helmut Käutner; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-09 / EASY

Gold: **León Klimovsky**. First-hop subquestion (N/R): `Who is the credited director of Film T83397?`. Listed wording: `Which candidate is the credited director of Film T83397?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: León Klimovsky.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Bhappi Sonie | León Klimovsky | True | 3.8568 |
| P2 | Vojtěch Jasný | León Klimovsky | True | 2.6172 |
| P3 | Marcello Fondato | León Klimovsky | True | 1.8063 |
| P4 | León Klimovsky | León Klimovsky | True | 4.4629 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | León Klimovsky | IN_SET_VALID | León Klimovsky |
| R1 | León Klimovsky | IN_SET_VALID | León Klimovsky |
| R2 | León Klimovsky | IN_SET_VALID | Bhappi Sonie |
| R3 | León Klimovsky | IN_SET_VALID | Vojtěch Jasný |
| R4 | León Klimovsky | IN_SET_VALID | Marcello Fondato |

N raw: `"León Klimovsky"`. R aggregate: León Klimovsky; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-09 / MID

Gold: **León Klimovsky**. First-hop subquestion (N/R): `Who is the credited director of Film T83397?`. Listed wording: `Which candidate is the credited director of Film T83397?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: León Klimovsky.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Bhappi Sonie | León Klimovsky | True | 3.5964 |
| P2 | Vojtěch Jasný | León Klimovsky | True | 2.0078 |
| P3 | Marcello Fondato | León Klimovsky | True | 0.9625 |
| P4 | León Klimovsky | León Klimovsky | True | 3.8027 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | León Klimovsky | IN_SET_VALID | León Klimovsky |
| R1 | León Klimovsky | IN_SET_VALID | León Klimovsky |
| R2 | León Klimovsky | IN_SET_VALID | Bhappi Sonie |
| R3 | León Klimovsky | IN_SET_VALID | Vojtěch Jasný |
| R4 | León Klimovsky | IN_SET_VALID | Marcello Fondato |

N raw: `"León Klimovsky"`. R aggregate: León Klimovsky; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-09 / HARD

Gold: **León Klimovsky**. First-hop subquestion (N/R): `Who is the credited director of Film T83397?`. Listed wording: `Which candidate is the credited director of Film T83397?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: León Klimovsky.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Bhappi Sonie | León Klimovsky | True | 1.5937 |
| P2 | Vojtěch Jasný | León Klimovsky | True | 0.3954 |
| P3 | Marcello Fondato | Marcello Fondato | True | -4.1156 |
| P4 | León Klimovsky | León Klimovsky | True | 4.0547 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | León Klimovsky | IN_SET_VALID | León Klimovsky |
| R1 | León Klimovsky | IN_SET_VALID | León Klimovsky |
| R2 | León Klimovsky | IN_SET_VALID | Bhappi Sonie |
| R3 | León Klimovsky | IN_SET_VALID | Vojtěch Jasný |
| R4 | León Klimovsky | IN_SET_VALID | Marcello Fondato |

N raw: `"León Klimovsky"`. R aggregate: León Klimovsky; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

Diagnostic anomalies (raw only here; full logs preserve every output):

- {"plan_id": "development/v344-development-09/HARD/R4", "F": "León Klimovsky", "F_category": "IN_SET_VALID", "C": null, "S_mean": "Marcello Fondato", "S_sum": "Marcello Fondato", "raw_f": "León Klimovsky", "note": "Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified."}

## development / v344-development-10 / EASY

Gold: **Fridrikh Ermler**. First-hop subquestion (N/R): `Who is the credited director of Film T76581?`. Listed wording: `Which candidate is the credited director of Film T76581?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Fridrikh Ermler.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Anil Das | Rodrigo Grande | True | -2.0423 |
| P2 | Fridrikh Ermler | Fridrikh Ermler | True | 2.6250 |
| P3 | Rolf Schübel | Fridrikh Ermler | True | 1.5842 |
| P4 | Rodrigo Grande | Fridrikh Ermler | True | 3.4069 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Fridrikh Ermler | IN_SET_VALID | Rodrigo Grande |
| R1 | Fridrikh Ermler | IN_SET_VALID | Rodrigo Grande |
| R2 | Fridrikh Ermler | IN_SET_VALID | Rolf Schübel |
| R3 | Fridrikh Ermler | IN_SET_VALID | Fridrikh Ermler |
| R4 | Fridrikh Ermler | IN_SET_VALID | Anil Das |

N raw: `"Fridrikh Ermler"`. R aggregate: Fridrikh Ermler; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-10 / MID

Gold: **Fridrikh Ermler**. First-hop subquestion (N/R): `Who is the credited director of Film T76581?`. Listed wording: `Which candidate is the credited director of Film T76581?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Anil Das.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Anil Das | Anil Das | True | -2.6963 |
| P2 | Fridrikh Ermler | Fridrikh Ermler | True | 2.0235 |
| P3 | Rolf Schübel | Rolf Schübel | True | -1.0916 |
| P4 | Rodrigo Grande | Anil Das | True | -3.0603 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Fridrikh Ermler | IN_SET_VALID | Rodrigo Grande |
| R1 | Fridrikh Ermler | IN_SET_VALID | Rodrigo Grande |
| R2 | Fridrikh Ermler | IN_SET_VALID | Rolf Schübel |
| R3 | Fridrikh Ermler | IN_SET_VALID | Fridrikh Ermler |
| R4 | Fridrikh Ermler | IN_SET_VALID | Anil Das |

N raw: `"Fridrikh Ermler"`. R aggregate: Fridrikh Ermler; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: L_WRONG_N_GOLD.

## development / v344-development-10 / HARD

Gold: **Fridrikh Ermler**. First-hop subquestion (N/R): `Who is the credited director of Film T76581?`. Listed wording: `Which candidate is the credited director of Film T76581?`. Partial robustness (same wrong identity 3/4): True.

L class: ORDER_SENSITIVE; modal identity: Rodrigo Grande.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Anil Das | Rodrigo Grande | True | -2.7559 |
| P2 | Fridrikh Ermler | Rodrigo Grande | True | -0.1303 |
| P3 | Rolf Schübel | Rolf Schübel | True | -1.4464 |
| P4 | Rodrigo Grande | Rodrigo Grande | True | -2.2677 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Rodrigo Grande | IN_SET_VALID | Rodrigo Grande |
| R1 | Rodrigo Grande | IN_SET_VALID | Rodrigo Grande |
| R2 | Rolf Schübel | IN_SET_VALID | Rolf Schübel |
| R3 | Fridrikh Ermler | IN_SET_VALID | Fridrikh Ermler |
| R4 | Fridrikh Ermler | IN_SET_VALID | Anil Das |

N raw: `"Rodrigo Grande"`. R aggregate: UNSTABLE_OR_UNRESOLVED; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-11 / EASY

Gold: **Vojtěch Jasný**. First-hop subquestion (N/R): `Who is the credited director of Film T43844?`. Listed wording: `Which candidate is the credited director of Film T43844?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Vojtěch Jasný.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Vojtěch Jasný | Vojtěch Jasný | True | 5.1589 |
| P2 | Bhappi Sonie | Vojtěch Jasný | True | 3.1224 |
| P3 | James Goldstone | Vojtěch Jasný | True | 5.0208 |
| P4 | Robert P. Kerr | Vojtěch Jasný | True | 4.8698 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Vojtěch Jasný | IN_SET_VALID | Vojtěch Jasný |
| R1 | Vojtěch Jasný | IN_SET_VALID | Vojtěch Jasný |
| R2 | Vojtěch Jasný | IN_SET_VALID | Robert P. Kerr |
| R3 | Vojtěch Jasný | IN_SET_VALID | Bhappi Sonie |
| R4 | Vojtěch Jasný | IN_SET_VALID | James Goldstone |

N raw: `"Vojtěch Jasný"`. R aggregate: Vojtěch Jasný; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-11 / MID

Gold: **Vojtěch Jasný**. First-hop subquestion (N/R): `Who is the credited director of Film T43844?`. Listed wording: `Which candidate is the credited director of Film T43844?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Vojtěch Jasný.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Vojtěch Jasný | Vojtěch Jasný | True | 4.5234 |
| P2 | Bhappi Sonie | Vojtěch Jasný | True | 1.7656 |
| P3 | James Goldstone | Vojtěch Jasný | True | 3.0000 |
| P4 | Robert P. Kerr | Vojtěch Jasný | True | 2.9687 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Vojtěch Jasný | IN_SET_VALID | Vojtěch Jasný |
| R1 | Vojtěch Jasný | IN_SET_VALID | Vojtěch Jasný |
| R2 | Vojtěch Jasný | IN_SET_VALID | Robert P. Kerr |
| R3 | Vojtěch Jasný | IN_SET_VALID | Bhappi Sonie |
| R4 | Vojtěch Jasný | IN_SET_VALID | James Goldstone |

N raw: `"Vojtěch Jasný"`. R aggregate: Vojtěch Jasný; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-11 / HARD

Gold: **Vojtěch Jasný**. First-hop subquestion (N/R): `Who is the credited director of Film T43844?`. Listed wording: `Which candidate is the credited director of Film T43844?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: TIE (missing).

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Vojtěch Jasný | Vojtěch Jasný | True | 4.4661 |
| P2 | Bhappi Sonie | Bhappi Sonie | True | -0.4717 |
| P3 | James Goldstone | James Goldstone | True | -1.9648 |
| P4 | Robert P. Kerr | Robert P. Kerr | True | -0.5295 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Vojtěch Jasný | IN_SET_VALID | Vojtěch Jasný |
| R1 | Vojtěch Jasný | IN_SET_VALID | Vojtěch Jasný |
| R2 | Vojtěch Jasný | IN_SET_VALID | Robert P. Kerr |
| R3 | Bhappi Sonie | IN_SET_VALID | Bhappi Sonie |
| R4 | James Goldstone | IN_SET_VALID | James Goldstone |

N raw: `"Vojtěch Jasný"`. R aggregate: UNSTABLE_OR_UNRESOLVED; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-12 / EASY

Gold: **Ildikó Enyedi**. First-hop subquestion (N/R): `Who is the credited director of Film T59052?`. Listed wording: `Which candidate is the credited director of Film T59052?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Ildikó Enyedi.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Tinnu Anand | Ildikó Enyedi | True | 4.9625 |
| P2 | Yuen Woo-ping | Ildikó Enyedi | True | 3.2688 |
| P3 | Armando Robles Godoy | Ildikó Enyedi | True | 4.1250 |
| P4 | Ildikó Enyedi | Ildikó Enyedi | True | 5.6688 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Ildikó Enyedi | IN_SET_VALID | Tinnu Anand |
| R1 | Ildikó Enyedi | IN_SET_VALID | Tinnu Anand |
| R2 | Ildikó Enyedi | IN_SET_VALID | Yuen Woo-ping |
| R3 | Ildikó Enyedi | IN_SET_VALID | Ildikó Enyedi |
| R4 | Ildikó Enyedi | IN_SET_VALID | Armando Robles Godoy |

N raw: `"Ildikó Enyedi"`. R aggregate: Ildikó Enyedi; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-12 / MID

Gold: **Ildikó Enyedi**. First-hop subquestion (N/R): `Who is the credited director of Film T59052?`. Listed wording: `Which candidate is the credited director of Film T59052?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Ildikó Enyedi.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Tinnu Anand | Ildikó Enyedi | True | 1.1564 |
| P2 | Yuen Woo-ping | Yuen Woo-ping | True | -0.9240 |
| P3 | Armando Robles Godoy | Ildikó Enyedi | True | 0.4082 |
| P4 | Ildikó Enyedi | Ildikó Enyedi | True | 4.8531 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Ildikó Enyedi | IN_SET_VALID | Tinnu Anand |
| R1 | Ildikó Enyedi | IN_SET_VALID | Tinnu Anand |
| R2 | Ildikó Enyedi | IN_SET_VALID | Yuen Woo-ping |
| R3 | Ildikó Enyedi | IN_SET_VALID | Ildikó Enyedi |
| R4 | Ildikó Enyedi | IN_SET_VALID | Armando Robles Godoy |

N raw: `"Ildikó Enyedi"`. R aggregate: Ildikó Enyedi; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-12 / HARD

Gold: **Ildikó Enyedi**. First-hop subquestion (N/R): `Who is the credited director of Film T59052?`. Listed wording: `Which candidate is the credited director of Film T59052?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: TIE (missing).

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Tinnu Anand | Tinnu Anand | True | -0.9284 |
| P2 | Yuen Woo-ping | Yuen Woo-ping | True | -2.6576 |
| P3 | Armando Robles Godoy | Armando Robles Godoy | True | -2.3461 |
| P4 | Ildikó Enyedi | Ildikó Enyedi | True | 3.9094 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Ildikó Enyedi | IN_SET_VALID | Tinnu Anand |
| R1 | Ildikó Enyedi | IN_SET_VALID | Tinnu Anand |
| R2 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |
| R3 | Ildikó Enyedi | IN_SET_VALID | Ildikó Enyedi |
| R4 | Ildikó Enyedi | IN_SET_VALID | Armando Robles Godoy |

N raw: `"Ildikó Enyedi"`. R aggregate: Ildikó Enyedi; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-13 / EASY

Gold: **Bhappi Sonie**. First-hop subquestion (N/R): `Who is the credited director of Film T86343?`. Listed wording: `Which candidate is the credited director of Film T86343?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Bhappi Sonie.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Bhappi Sonie | Bhappi Sonie | True | 4.5063 |
| P2 | Marcello Fondato | Bhappi Sonie | True | 4.1001 |
| P3 | León Klimovsky | Bhappi Sonie | True | 2.1188 |
| P4 | Walter Hugo Khouri | Bhappi Sonie | True | 0.4472 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Bhappi Sonie | IN_SET_VALID | Marcello Fondato |
| R1 | Bhappi Sonie | IN_SET_VALID | Marcello Fondato |
| R2 | Bhappi Sonie | IN_SET_VALID | León Klimovsky |
| R3 | Bhappi Sonie | IN_SET_VALID | Walter Hugo Khouri |
| R4 | Bhappi Sonie | IN_SET_VALID | Bhappi Sonie |

N raw: `"Bhappi Sonie"`. R aggregate: Bhappi Sonie; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-13 / MID

Gold: **Bhappi Sonie**. First-hop subquestion (N/R): `Who is the credited director of Film T86343?`. Listed wording: `Which candidate is the credited director of Film T86343?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Bhappi Sonie.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Bhappi Sonie | Bhappi Sonie | True | 4.3188 |
| P2 | Marcello Fondato | Bhappi Sonie | True | 3.8657 |
| P3 | León Klimovsky | Bhappi Sonie | True | 0.3571 |
| P4 | Walter Hugo Khouri | Walter Hugo Khouri | True | -0.7235 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Bhappi Sonie | IN_SET_VALID | Marcello Fondato |
| R1 | Bhappi Sonie | IN_SET_VALID | Marcello Fondato |
| R2 | Bhappi Sonie | IN_SET_VALID | León Klimovsky |
| R3 | Bhappi Sonie | IN_SET_VALID | Walter Hugo Khouri |
| R4 | Bhappi Sonie | IN_SET_VALID | Bhappi Sonie |

N raw: `"Bhappi Sonie"`. R aggregate: Bhappi Sonie; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-13 / HARD

Gold: **Bhappi Sonie**. First-hop subquestion (N/R): `Who is the credited director of Film T86343?`. Listed wording: `Which candidate is the credited director of Film T86343?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Marcello Fondato.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Bhappi Sonie | Bhappi Sonie | True | 3.7563 |
| P2 | Marcello Fondato | Marcello Fondato | True | -0.9426 |
| P3 | León Klimovsky | Marcello Fondato | True | -2.2724 |
| P4 | Walter Hugo Khouri | Walter Hugo Khouri | True | -3.6666 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Bhappi Sonie | IN_SET_VALID | Marcello Fondato |
| R1 | Bhappi Sonie | IN_SET_VALID | Marcello Fondato |
| R2 | Bhappi Sonie | IN_SET_VALID | León Klimovsky |
| R3 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R4 | Bhappi Sonie | IN_SET_VALID | Bhappi Sonie |

N raw: `"Bhappi Sonie"`. R aggregate: Bhappi Sonie; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: L_WRONG_N_GOLD.

Diagnostic anomalies (raw only here; full logs preserve every output):

- {"plan_id": "development/v344-development-13/HARD/L2", "F": null, "F_category": "TRUNCATED", "C": "Marcello Fondato", "S_mean": "Marcello Fondato", "S_sum": "Marcello Fondato", "raw_f": "Marcello Fondato\n\nWait. Let's reevaluate.\n\nWe are to find the **credited director** of Film T86343.\n\nWe start at Film T86343 and follow only **credited-director** links until we reach a record that names a candidate.\n\nGraph-link records:\n\n- Film T86343 has credited-director link R70996.\n- R70996 has credited-director link", "note": "Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified."}
- {"plan_id": "development/v344-development-13/HARD/L3", "F": null, "F_category": "TRUNCATED", "C": "Marcello Fondato", "S_mean": "Marcello Fondato", "S_sum": "Marcello Fondato", "raw_f": "Marcello Fondato\n\nExplanation:  \nWe start at Film T86343 and follow only the \"credited-director\" links until we reach a record that names a candidate.\n\n- Film T86343 has credited-director link R70996.\n- R70996 has credited-director link R93825.\n- R93825 has credited-director link R23078", "note": "Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified."}

## development / v344-development-14 / EASY

Gold: **Walter Hugo Khouri**. First-hop subquestion (N/R): `Who is the credited director of Film T30907?`. Listed wording: `Which candidate is the credited director of Film T30907?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Walter Hugo Khouri.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Bhappi Sonie | Walter Hugo Khouri | True | 2.6198 |
| P2 | Robert P. Kerr | Walter Hugo Khouri | True | 3.2109 |
| P3 | Marcello Fondato | Walter Hugo Khouri | True | 0.7188 |
| P4 | Walter Hugo Khouri | Walter Hugo Khouri | True | 4.7370 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R2 | Walter Hugo Khouri | IN_SET_VALID | Bhappi Sonie |
| R3 | Walter Hugo Khouri | IN_SET_VALID | Marcello Fondato |
| R4 | Walter Hugo Khouri | IN_SET_VALID | Robert P. Kerr |

N raw: `"Walter Hugo Khouri"`. R aggregate: Walter Hugo Khouri; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-14 / MID

Gold: **Walter Hugo Khouri**. First-hop subquestion (N/R): `Who is the credited director of Film T30907?`. Listed wording: `Which candidate is the credited director of Film T30907?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Walter Hugo Khouri.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Bhappi Sonie | Walter Hugo Khouri | True | 1.1250 |
| P2 | Robert P. Kerr | Walter Hugo Khouri | True | 0.3475 |
| P3 | Marcello Fondato | Marcello Fondato | True | -0.8375 |
| P4 | Walter Hugo Khouri | Walter Hugo Khouri | True | 4.3620 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R2 | Walter Hugo Khouri | IN_SET_VALID | Bhappi Sonie |
| R3 | Walter Hugo Khouri | IN_SET_VALID | Marcello Fondato |
| R4 | Walter Hugo Khouri | IN_SET_VALID | Robert P. Kerr |

N raw: `"Walter Hugo Khouri"`. R aggregate: Walter Hugo Khouri; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-14 / HARD

Gold: **Walter Hugo Khouri**. First-hop subquestion (N/R): `Who is the credited director of Film T30907?`. Listed wording: `Which candidate is the credited director of Film T30907?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Walter Hugo Khouri.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Bhappi Sonie | Walter Hugo Khouri | True | 0.2216 |
| P2 | Robert P. Kerr | Robert P. Kerr | True | -1.3437 |
| P3 | Marcello Fondato | Marcello Fondato | True | -3.1531 |
| P4 | Walter Hugo Khouri | Walter Hugo Khouri | True | 4.2838 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R2 | Walter Hugo Khouri | IN_SET_VALID | Bhappi Sonie |
| R3 | Walter Hugo Khouri | IN_SET_VALID | Marcello Fondato |
| R4 | Walter Hugo Khouri | IN_SET_VALID | Robert P. Kerr |

N raw: `"Walter Hugo Khouri"`. R aggregate: Walter Hugo Khouri; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-15 / EASY

Gold: **Yuen Woo-ping**. First-hop subquestion (N/R): `Who is the credited director of Film T14409?`. Listed wording: `Which candidate is the credited director of Film T14409?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Yuen Woo-ping.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Jan Svěrák | Yuen Woo-ping | True | 3.8839 |
| P2 | Ildikó Enyedi | Yuen Woo-ping | True | 3.3862 |
| P3 | Armando Robles Godoy | Yuen Woo-ping | True | 4.0625 |
| P4 | Yuen Woo-ping | Yuen Woo-ping | True | 4.6430 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Yuen Woo-ping | IN_SET_VALID | Armando Robles Godoy |
| R1 | Yuen Woo-ping | IN_SET_VALID | Armando Robles Godoy |
| R2 | Yuen Woo-ping | IN_SET_VALID | Ildikó Enyedi |
| R3 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |
| R4 | Yuen Woo-ping | IN_SET_VALID | Jan Svěrák |

N raw: `"Yuen Woo-ping"`. R aggregate: Yuen Woo-ping; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-15 / MID

Gold: **Yuen Woo-ping**. First-hop subquestion (N/R): `Who is the credited director of Film T14409?`. Listed wording: `Which candidate is the credited director of Film T14409?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Yuen Woo-ping.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Jan Svěrák | Yuen Woo-ping | True | 1.0500 |
| P2 | Ildikó Enyedi | Yuen Woo-ping | True | 0.8525 |
| P3 | Armando Robles Godoy | Yuen Woo-ping | True | 1.9896 |
| P4 | Yuen Woo-ping | Yuen Woo-ping | True | 3.6008 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Yuen Woo-ping | IN_SET_VALID | Armando Robles Godoy |
| R1 | Yuen Woo-ping | IN_SET_VALID | Armando Robles Godoy |
| R2 | Yuen Woo-ping | IN_SET_VALID | Ildikó Enyedi |
| R3 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |
| R4 | Yuen Woo-ping | IN_SET_VALID | Jan Svěrák |

N raw: `"Yuen Woo-ping"`. R aggregate: Yuen Woo-ping; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-15 / HARD

Gold: **Yuen Woo-ping**. First-hop subquestion (N/R): `Who is the credited director of Film T14409?`. Listed wording: `Which candidate is the credited director of Film T14409?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Yuen Woo-ping.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Jan Svěrák | Yuen Woo-ping | True | 0.4438 |
| P2 | Ildikó Enyedi | Yuen Woo-ping | True | 1.1785 |
| P3 | Armando Robles Godoy | Yuen Woo-ping | True | 1.6250 |
| P4 | Yuen Woo-ping | Yuen Woo-ping | True | 4.3911 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Yuen Woo-ping | IN_SET_VALID | Armando Robles Godoy |
| R1 | Yuen Woo-ping | IN_SET_VALID | Armando Robles Godoy |
| R2 | Ildikó Enyedi | IN_SET_VALID | Ildikó Enyedi |
| R3 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |
| R4 | Yuen Woo-ping | IN_SET_VALID | Jan Svěrák |

N raw: `"Yuen Woo-ping"`. R aggregate: Yuen Woo-ping; R observed identity changes: True; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-16 / EASY

Gold: **Jan Svěrák**. First-hop subquestion (N/R): `Who is the credited director of Film T64663?`. Listed wording: `Which candidate is the credited director of Film T64663?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Jan Svěrák.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Armando Robles Godoy | Jan Svěrák | True | 0.1195 |
| P2 | Rahul Rawail | Jan Svěrák | True | 0.5616 |
| P3 | Jan Svěrák | Jan Svěrák | True | 2.7519 |
| P4 | Leopoldo Torre Nilsson | Jan Svěrák | True | 1.3789 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Jan Svěrák | IN_SET_VALID | Leopoldo Torre Nilsson |
| R1 | Jan Svěrák | IN_SET_VALID | Leopoldo Torre Nilsson |
| R2 | Jan Svěrák | IN_SET_VALID | Rahul Rawail |
| R3 | Jan Svěrák | IN_SET_VALID | Armando Robles Godoy |
| R4 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |

N raw: `"Jan Svěrák"`. R aggregate: Jan Svěrák; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-16 / MID

Gold: **Jan Svěrák**. First-hop subquestion (N/R): `Who is the credited director of Film T64663?`. Listed wording: `Which candidate is the credited director of Film T64663?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Jan Svěrák.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Armando Robles Godoy | Jan Svěrák | True | 1.2109 |
| P2 | Rahul Rawail | Jan Svěrák | True | 1.6777 |
| P3 | Jan Svěrák | Jan Svěrák | True | 2.6230 |
| P4 | Leopoldo Torre Nilsson | Jan Svěrák | True | 1.4238 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Jan Svěrák | IN_SET_VALID | Leopoldo Torre Nilsson |
| R1 | Jan Svěrák | IN_SET_VALID | Leopoldo Torre Nilsson |
| R2 | Rahul Rawail | IN_SET_VALID | Rahul Rawail |
| R3 | Jan Svěrák | IN_SET_VALID | Armando Robles Godoy |
| R4 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |

N raw: `"Jan Svěrák"`. R aggregate: Jan Svěrák; R observed identity changes: True; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-16 / HARD

Gold: **Jan Svěrák**. First-hop subquestion (N/R): `Who is the credited director of Film T64663?`. Listed wording: `Which candidate is the credited director of Film T64663?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Jan Svěrák.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Armando Robles Godoy | Jan Svěrák | True | -0.0940 |
| P2 | Rahul Rawail | Rahul Rawail | True | -0.2250 |
| P3 | Jan Svěrák | Jan Svěrák | True | 2.4551 |
| P4 | Leopoldo Torre Nilsson | Jan Svěrák | True | -0.0221 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Jan Svěrák | IN_SET_VALID | Leopoldo Torre Nilsson |
| R1 | Jan Svěrák | IN_SET_VALID | Leopoldo Torre Nilsson |
| R2 | Rahul Rawail | IN_SET_VALID | Rahul Rawail |
| R3 | Rahul Rawail | IN_SET_VALID | Armando Robles Godoy |
| R4 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |

N raw: `"Jan Svěrák"`. R aggregate: UNSTABLE_OR_UNRESOLVED; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

Diagnostic anomalies (raw only here; full logs preserve every output):

- {"plan_id": "development/v344-development-16/HARD/L1", "F": "Jan Svěrák", "F_category": "IN_SET_VALID", "C": "Jan Svěrák", "S_mean": "Armando Robles Godoy", "S_sum": "Armando Robles Godoy", "raw_f": "Jan Svěrák", "note": "Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified."}
- {"plan_id": "development/v344-development-16/HARD/L4", "F": "Jan Svěrák", "F_category": "IN_SET_VALID", "C": "Jan Svěrák", "S_mean": "Leopoldo Torre Nilsson", "S_sum": "Jan Svěrák", "raw_f": "Jan Svěrák", "note": "Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified."}

## development / v344-development-17 / EASY

Gold: **Bhappi Sonie**. First-hop subquestion (N/R): `Who is the credited director of Film T31878?`. Listed wording: `Which candidate is the credited director of Film T31878?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Bhappi Sonie.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Robert P. Kerr | Bhappi Sonie | True | 1.4688 |
| P2 | Bhappi Sonie | Bhappi Sonie | True | 4.1188 |
| P3 | León Klimovsky | Bhappi Sonie | True | 1.9813 |
| P4 | Walter Hugo Khouri | Bhappi Sonie | True | 2.2688 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Bhappi Sonie | IN_SET_VALID | Walter Hugo Khouri |
| R1 | Bhappi Sonie | IN_SET_VALID | Walter Hugo Khouri |
| R2 | Bhappi Sonie | IN_SET_VALID | Robert P. Kerr |
| R3 | Bhappi Sonie | IN_SET_VALID | Bhappi Sonie |
| R4 | Bhappi Sonie | IN_SET_VALID | León Klimovsky |

N raw: `"Bhappi Sonie"`. R aggregate: Bhappi Sonie; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-17 / MID

Gold: **Bhappi Sonie**. First-hop subquestion (N/R): `Who is the credited director of Film T31878?`. Listed wording: `Which candidate is the credited director of Film T31878?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Bhappi Sonie.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Robert P. Kerr | Robert P. Kerr | True | -0.4889 |
| P2 | Bhappi Sonie | Bhappi Sonie | True | 3.8406 |
| P3 | León Klimovsky | León Klimovsky | True | -1.1041 |
| P4 | Walter Hugo Khouri | Bhappi Sonie | True | 0.4595 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Bhappi Sonie | IN_SET_VALID | Walter Hugo Khouri |
| R1 | Bhappi Sonie | IN_SET_VALID | Walter Hugo Khouri |
| R2 | Bhappi Sonie | IN_SET_VALID | Robert P. Kerr |
| R3 | Bhappi Sonie | IN_SET_VALID | Bhappi Sonie |
| R4 | Bhappi Sonie | IN_SET_VALID | León Klimovsky |

N raw: `"Bhappi Sonie"`. R aggregate: Bhappi Sonie; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-17 / HARD

Gold: **Bhappi Sonie**. First-hop subquestion (N/R): `Who is the credited director of Film T31878?`. Listed wording: `Which candidate is the credited director of Film T31878?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: TIE (missing).

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Robert P. Kerr | León Klimovsky | True | -2.6901 |
| P2 | Bhappi Sonie | Bhappi Sonie | True | 3.1531 |
| P3 | León Klimovsky | León Klimovsky | True | -0.3663 |
| P4 | Walter Hugo Khouri | Bhappi Sonie | True | 0.8385 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Bhappi Sonie | IN_SET_VALID | Walter Hugo Khouri |
| R1 | Bhappi Sonie | IN_SET_VALID | Walter Hugo Khouri |
| R2 | Robert P. Kerr | IN_SET_VALID | Robert P. Kerr |
| R3 | Bhappi Sonie | IN_SET_VALID | Bhappi Sonie |
| R4 | Bhappi Sonie | IN_SET_VALID | León Klimovsky |

N raw: `"Bhappi Sonie"`. R aggregate: Bhappi Sonie; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-18 / EASY

Gold: **Yuen Woo-ping**. First-hop subquestion (N/R): `Who is the credited director of Film T20146?`. Listed wording: `Which candidate is the credited director of Film T20146?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Yuen Woo-ping.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Jan Svěrák | Yuen Woo-ping | True | 3.4824 |
| P2 | Tinnu Anand | Yuen Woo-ping | True | 3.1125 |
| P3 | Yuen Woo-ping | Yuen Woo-ping | True | 3.6484 |
| P4 | Leopoldo Torre Nilsson | Yuen Woo-ping | True | 3.3398 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Yuen Woo-ping | IN_SET_VALID | Leopoldo Torre Nilsson |
| R1 | Yuen Woo-ping | IN_SET_VALID | Leopoldo Torre Nilsson |
| R2 | Yuen Woo-ping | IN_SET_VALID | Jan Svěrák |
| R3 | Yuen Woo-ping | IN_SET_VALID | Tinnu Anand |
| R4 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |

N raw: `"Yuen Woo-ping"`. R aggregate: Yuen Woo-ping; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-18 / MID

Gold: **Yuen Woo-ping**. First-hop subquestion (N/R): `Who is the credited director of Film T20146?`. Listed wording: `Which candidate is the credited director of Film T20146?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Yuen Woo-ping.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Jan Svěrák | Yuen Woo-ping | True | 2.0957 |
| P2 | Tinnu Anand | Yuen Woo-ping | True | 1.4937 |
| P3 | Yuen Woo-ping | Yuen Woo-ping | True | 3.2461 |
| P4 | Leopoldo Torre Nilsson | Yuen Woo-ping | True | 1.2227 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Yuen Woo-ping | IN_SET_VALID | Leopoldo Torre Nilsson |
| R1 | Yuen Woo-ping | IN_SET_VALID | Leopoldo Torre Nilsson |
| R2 | Yuen Woo-ping | IN_SET_VALID | Jan Svěrák |
| R3 | Yuen Woo-ping | IN_SET_VALID | Tinnu Anand |
| R4 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |

N raw: `"Yuen Woo-ping"`. R aggregate: Yuen Woo-ping; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-18 / HARD

Gold: **Yuen Woo-ping**. First-hop subquestion (N/R): `Who is the credited director of Film T20146?`. Listed wording: `Which candidate is the credited director of Film T20146?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Yuen Woo-ping.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Jan Svěrák | Yuen Woo-ping | True | 1.9687 |
| P2 | Tinnu Anand | Yuen Woo-ping | True | 0.9750 |
| P3 | Yuen Woo-ping | Yuen Woo-ping | True | 3.0840 |
| P4 | Leopoldo Torre Nilsson | Yuen Woo-ping | True | 0.8046 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Yuen Woo-ping | IN_SET_VALID | Leopoldo Torre Nilsson |
| R1 | Yuen Woo-ping | IN_SET_VALID | Leopoldo Torre Nilsson |
| R2 | Yuen Woo-ping | IN_SET_VALID | Jan Svěrák |
| R3 | Yuen Woo-ping | IN_SET_VALID | Tinnu Anand |
| R4 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |

N raw: `"Yuen Woo-ping"`. R aggregate: Yuen Woo-ping; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-19 / EASY

Gold: **Fridrikh Ermler**. First-hop subquestion (N/R): `Who is the credited director of Film T45562?`. Listed wording: `Which candidate is the credited director of Film T45562?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Fridrikh Ermler.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Helmut Käutner | Fridrikh Ermler | True | 1.9584 |
| P2 | Fridrikh Ermler | Fridrikh Ermler | True | 4.8333 |
| P3 | Feng Xiaoning | Fridrikh Ermler | True | 3.8203 |
| P4 | Anil Das | Fridrikh Ermler | True | 3.6510 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Fridrikh Ermler | IN_SET_VALID | Feng Xiaoning |
| R1 | Fridrikh Ermler | IN_SET_VALID | Feng Xiaoning |
| R2 | Fridrikh Ermler | IN_SET_VALID | Helmut Käutner |
| R3 | Fridrikh Ermler | IN_SET_VALID | Fridrikh Ermler |
| R4 | Fridrikh Ermler | IN_SET_VALID | Anil Das |

N raw: `"Fridrikh Ermler"`. R aggregate: Fridrikh Ermler; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-19 / MID

Gold: **Fridrikh Ermler**. First-hop subquestion (N/R): `Who is the credited director of Film T45562?`. Listed wording: `Which candidate is the credited director of Film T45562?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Fridrikh Ermler.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Helmut Käutner | Fridrikh Ermler | True | 0.6231 |
| P2 | Fridrikh Ermler | Fridrikh Ermler | True | 4.3229 |
| P3 | Feng Xiaoning | Fridrikh Ermler | True | 1.6096 |
| P4 | Anil Das | Fridrikh Ermler | True | 1.4814 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Fridrikh Ermler | IN_SET_VALID | Feng Xiaoning |
| R1 | Fridrikh Ermler | IN_SET_VALID | Feng Xiaoning |
| R2 | Fridrikh Ermler | IN_SET_VALID | Helmut Käutner |
| R3 | Fridrikh Ermler | IN_SET_VALID | Fridrikh Ermler |
| R4 | Fridrikh Ermler | IN_SET_VALID | Anil Das |

N raw: `"Fridrikh Ermler"`. R aggregate: Fridrikh Ermler; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-19 / HARD

Gold: **Fridrikh Ermler**. First-hop subquestion (N/R): `Who is the credited director of Film T45562?`. Listed wording: `Which candidate is the credited director of Film T45562?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Fridrikh Ermler.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Helmut Käutner | Fridrikh Ermler | True | 0.0743 |
| P2 | Fridrikh Ermler | Fridrikh Ermler | True | 4.3724 |
| P3 | Feng Xiaoning | Fridrikh Ermler | True | 1.1029 |
| P4 | Anil Das | Fridrikh Ermler | True | 0.9871 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Fridrikh Ermler | IN_SET_VALID | Feng Xiaoning |
| R1 | Fridrikh Ermler | IN_SET_VALID | Feng Xiaoning |
| R2 | Fridrikh Ermler | IN_SET_VALID | Helmut Käutner |
| R3 | Fridrikh Ermler | IN_SET_VALID | Fridrikh Ermler |
| R4 | Fridrikh Ermler | IN_SET_VALID | Anil Das |

N raw: `"Fridrikh Ermler"`. R aggregate: Fridrikh Ermler; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-20 / EASY

Gold: **Jan Svěrák**. First-hop subquestion (N/R): `Who is the credited director of Film T71705?`. Listed wording: `Which candidate is the credited director of Film T71705?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Jan Svěrák.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Jan Svěrák | Jan Svěrák | True | 5.3515 |
| P2 | Armando Robles Godoy | Jan Svěrák | True | 2.5104 |
| P3 | Yuen Woo-ping | Jan Svěrák | True | 1.1937 |
| P4 | Tinnu Anand | Jan Svěrák | True | 2.6562 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |
| R1 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |
| R2 | Jan Svěrák | IN_SET_VALID | Tinnu Anand |
| R3 | Jan Svěrák | IN_SET_VALID | Yuen Woo-ping |
| R4 | Jan Svěrák | IN_SET_VALID | Armando Robles Godoy |

N raw: `"Jan Svěrák"`. R aggregate: Jan Svěrák; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-20 / MID

Gold: **Jan Svěrák**. First-hop subquestion (N/R): `Who is the credited director of Film T71705?`. Listed wording: `Which candidate is the credited director of Film T71705?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Jan Svěrák.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Jan Svěrák | Jan Svěrák | True | 4.2750 |
| P2 | Armando Robles Godoy | Armando Robles Godoy | True | -0.0289 |
| P3 | Yuen Woo-ping | Yuen Woo-ping | True | -1.3375 |
| P4 | Tinnu Anand | Jan Svěrák | True | 0.1312 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |
| R1 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |
| R2 | Jan Svěrák | IN_SET_VALID | Tinnu Anand |
| R3 | Jan Svěrák | IN_SET_VALID | Yuen Woo-ping |
| R4 | Jan Svěrák | IN_SET_VALID | Armando Robles Godoy |

N raw: `"Jan Svěrák"`. R aggregate: Jan Svěrák; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

Diagnostic anomalies (raw only here; full logs preserve every output):

- {"plan_id": "development/v344-development-20/MID/R4", "F": "Jan Svěrák", "F_category": "IN_SET_VALID", "C": null, "S_mean": "Yuen Woo-ping", "S_sum": "Yuen Woo-ping", "raw_f": "Jan Svěrák", "note": "Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified."}

## development / v344-development-20 / HARD

Gold: **Jan Svěrák**. First-hop subquestion (N/R): `Who is the credited director of Film T71705?`. Listed wording: `Which candidate is the credited director of Film T71705?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: TIE (missing).

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Jan Svěrák | Jan Svěrák | True | 4.4817 |
| P2 | Armando Robles Godoy | Armando Robles Godoy | True | -2.0188 |
| P3 | Yuen Woo-ping | Yuen Woo-ping | True | -4.0875 |
| P4 | Tinnu Anand | Tinnu Anand | True | -1.7250 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |
| R1 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |
| R2 | Jan Svěrák | IN_SET_VALID | Tinnu Anand |
| R3 | Jan Svěrák | IN_SET_VALID | Yuen Woo-ping |
| R4 | Yuen Woo-ping | IN_SET_VALID | Armando Robles Godoy |

N raw: `"Jan Svěrák"`. R aggregate: Jan Svěrák; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-21 / EASY

Gold: **Fridrikh Ermler**. First-hop subquestion (N/R): `Who is the credited director of Film T17571?`. Listed wording: `Which candidate is the credited director of Film T17571?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Fridrikh Ermler.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Fridrikh Ermler | Fridrikh Ermler | True | 2.8394 |
| P2 | Rodrigo Grande | Fridrikh Ermler | True | 2.2438 |
| P3 | Rolf Schübel | Fridrikh Ermler | True | 2.6328 |
| P4 | Feng Xiaoning | Fridrikh Ermler | True | 3.3516 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Fridrikh Ermler | IN_SET_VALID | Rolf Schübel |
| R1 | Fridrikh Ermler | IN_SET_VALID | Rolf Schübel |
| R2 | Fridrikh Ermler | IN_SET_VALID | Fridrikh Ermler |
| R3 | Fridrikh Ermler | IN_SET_VALID | Rodrigo Grande |
| R4 | Fridrikh Ermler | IN_SET_VALID | Feng Xiaoning |

N raw: `"Fridrikh Ermler"`. R aggregate: Fridrikh Ermler; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-21 / MID

Gold: **Fridrikh Ermler**. First-hop subquestion (N/R): `Who is the credited director of Film T17571?`. Listed wording: `Which candidate is the credited director of Film T17571?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: TIE (missing).

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Fridrikh Ermler | Fridrikh Ermler | True | 0.2064 |
| P2 | Rodrigo Grande | Rodrigo Grande | True | -0.9729 |
| P3 | Rolf Schübel | Rolf Schübel | True | -0.5368 |
| P4 | Feng Xiaoning | Feng Xiaoning | True | -0.5708 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Fridrikh Ermler | IN_SET_VALID | Rolf Schübel |
| R1 | Fridrikh Ermler | IN_SET_VALID | Rolf Schübel |
| R2 | Fridrikh Ermler | IN_SET_VALID | Fridrikh Ermler |
| R3 | Fridrikh Ermler | IN_SET_VALID | Rodrigo Grande |
| R4 | Fridrikh Ermler | IN_SET_VALID | Feng Xiaoning |

N raw: `"Fridrikh Ermler"`. R aggregate: Fridrikh Ermler; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-21 / HARD

Gold: **Fridrikh Ermler**. First-hop subquestion (N/R): `Who is the credited director of Film T17571?`. Listed wording: `Which candidate is the credited director of Film T17571?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Feng Xiaoning.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Fridrikh Ermler | Fridrikh Ermler | True | 1.9766 |
| P2 | Rodrigo Grande | Feng Xiaoning | True | -0.3571 |
| P3 | Rolf Schübel | Rolf Schübel | True | -1.2859 |
| P4 | Feng Xiaoning | Feng Xiaoning | True | -0.3862 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Fridrikh Ermler | IN_SET_VALID | Rolf Schübel |
| R1 | Fridrikh Ermler | IN_SET_VALID | Rolf Schübel |
| R2 | Fridrikh Ermler | IN_SET_VALID | Fridrikh Ermler |
| R3 | Fridrikh Ermler | IN_SET_VALID | Rodrigo Grande |
| R4 | Fridrikh Ermler | IN_SET_VALID | Feng Xiaoning |

N raw: `"Fridrikh Ermler"`. R aggregate: Fridrikh Ermler; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: L_WRONG_N_GOLD.

## development / v344-development-22 / EASY

Gold: **Yuen Woo-ping**. First-hop subquestion (N/R): `Who is the credited director of Film T72677?`. Listed wording: `Which candidate is the credited director of Film T72677?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Yuen Woo-ping.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Leopoldo Torre Nilsson | Yuen Woo-ping | True | 2.7813 |
| P2 | Yuen Woo-ping | Yuen Woo-ping | True | 3.6387 |
| P3 | Tinnu Anand | Yuen Woo-ping | True | 4.3086 |
| P4 | Armando Robles Godoy | Yuen Woo-ping | True | 2.4687 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Yuen Woo-ping | IN_SET_VALID | Tinnu Anand |
| R1 | Yuen Woo-ping | IN_SET_VALID | Tinnu Anand |
| R2 | Yuen Woo-ping | IN_SET_VALID | Armando Robles Godoy |
| R3 | Yuen Woo-ping | IN_SET_VALID | Leopoldo Torre Nilsson |
| R4 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |

N raw: `"Yuen Woo-ping"`. R aggregate: Yuen Woo-ping; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-22 / MID

Gold: **Yuen Woo-ping**. First-hop subquestion (N/R): `Who is the credited director of Film T72677?`. Listed wording: `Which candidate is the credited director of Film T72677?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Yuen Woo-ping.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Leopoldo Torre Nilsson | Yuen Woo-ping | True | 1.4531 |
| P2 | Yuen Woo-ping | Yuen Woo-ping | True | 3.5566 |
| P3 | Tinnu Anand | Yuen Woo-ping | True | 3.1758 |
| P4 | Armando Robles Godoy | Yuen Woo-ping | True | 1.8965 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Yuen Woo-ping | IN_SET_VALID | Tinnu Anand |
| R1 | Yuen Woo-ping | IN_SET_VALID | Tinnu Anand |
| R2 | Yuen Woo-ping | IN_SET_VALID | Armando Robles Godoy |
| R3 | Yuen Woo-ping | IN_SET_VALID | Leopoldo Torre Nilsson |
| R4 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |

N raw: `"Yuen Woo-ping"`. R aggregate: Yuen Woo-ping; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-22 / HARD

Gold: **Yuen Woo-ping**. First-hop subquestion (N/R): `Who is the credited director of Film T72677?`. Listed wording: `Which candidate is the credited director of Film T72677?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: TIE (missing).

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | True | -1.0442 |
| P2 | Yuen Woo-ping | Yuen Woo-ping | True | 3.4414 |
| P3 | Tinnu Anand | Tinnu Anand | True | -1.0188 |
| P4 | Armando Robles Godoy | Armando Robles Godoy | True | -0.1344 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Yuen Woo-ping | IN_SET_VALID | Tinnu Anand |
| R1 | Yuen Woo-ping | IN_SET_VALID | Tinnu Anand |
| R2 | Yuen Woo-ping | IN_SET_VALID | Armando Robles Godoy |
| R3 | Yuen Woo-ping | IN_SET_VALID | Leopoldo Torre Nilsson |
| R4 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |

N raw: `"Yuen Woo-ping"`. R aggregate: Yuen Woo-ping; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-23 / EASY

Gold: **Fridrikh Ermler**. First-hop subquestion (N/R): `Who is the credited director of Film T98590?`. Listed wording: `Which candidate is the credited director of Film T98590?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Fridrikh Ermler.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Anil Das | Fridrikh Ermler | True | 2.8673 |
| P2 | Rodrigo Grande | Fridrikh Ermler | True | 1.7718 |
| P3 | Gu Changwei | Fridrikh Ermler | True | 3.9688 |
| P4 | Fridrikh Ermler | Fridrikh Ermler | True | 4.6042 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Fridrikh Ermler | IN_SET_VALID | Gu Changwei |
| R1 | Fridrikh Ermler | IN_SET_VALID | Gu Changwei |
| R2 | Fridrikh Ermler | IN_SET_VALID | Fridrikh Ermler |
| R3 | Fridrikh Ermler | IN_SET_VALID | Anil Das |
| R4 | Fridrikh Ermler | IN_SET_VALID | Rodrigo Grande |

N raw: `"Fridrikh Ermler"`. R aggregate: Fridrikh Ermler; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-23 / MID

Gold: **Fridrikh Ermler**. First-hop subquestion (N/R): `Who is the credited director of Film T98590?`. Listed wording: `Which candidate is the credited director of Film T98590?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: TIE (missing).

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Anil Das | Rodrigo Grande | True | -0.5998 |
| P2 | Rodrigo Grande | Rodrigo Grande | True | -1.6382 |
| P3 | Gu Changwei | Fridrikh Ermler | True | 2.8125 |
| P4 | Fridrikh Ermler | Fridrikh Ermler | True | 3.4375 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Fridrikh Ermler | IN_SET_VALID | Gu Changwei |
| R1 | Fridrikh Ermler | IN_SET_VALID | Gu Changwei |
| R2 | Fridrikh Ermler | IN_SET_VALID | Fridrikh Ermler |
| R3 | Fridrikh Ermler | IN_SET_VALID | Anil Das |
| R4 | Rodrigo Grande | IN_SET_VALID | Rodrigo Grande |

N raw: `"Fridrikh Ermler"`. R aggregate: Fridrikh Ermler; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-23 / HARD

Gold: **Fridrikh Ermler**. First-hop subquestion (N/R): `Who is the credited director of Film T98590?`. Listed wording: `Which candidate is the credited director of Film T98590?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: TIE (missing).

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Anil Das | Anil Das | True | -1.5123 |
| P2 | Rodrigo Grande | Rodrigo Grande | True | -2.5959 |
| P3 | Gu Changwei | Gu Changwei | True | -1.7812 |
| P4 | Fridrikh Ermler | Fridrikh Ermler | True | 0.2488 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Gu Changwei | IN_SET_VALID | Gu Changwei |
| R1 | Gu Changwei | IN_SET_VALID | Gu Changwei |
| R2 | Fridrikh Ermler | IN_SET_VALID | Fridrikh Ermler |
| R3 | Fridrikh Ermler | IN_SET_VALID | Anil Das |
| R4 | Rodrigo Grande | IN_SET_VALID | Rodrigo Grande |

N raw: `"Gu Changwei"`. R aggregate: UNSTABLE_OR_UNRESOLVED; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## development / v344-development-24 / EASY

Gold: **Rahul Rawail**. First-hop subquestion (N/R): `Who is the credited director of Film T74644?`. Listed wording: `Which candidate is the credited director of Film T74644?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Rahul Rawail.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Rahul Rawail | Rahul Rawail | True | 2.1813 |
| P2 | Yuen Woo-ping | Rahul Rawail | True | 1.8875 |
| P3 | Ildikó Enyedi | Rahul Rawail | True | 1.9500 |
| P4 | Leopoldo Torre Nilsson | Rahul Rawail | True | 1.9863 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Rahul Rawail | IN_SET_VALID | Yuen Woo-ping |
| R1 | Rahul Rawail | IN_SET_VALID | Yuen Woo-ping |
| R2 | Rahul Rawail | IN_SET_VALID | Rahul Rawail |
| R3 | Rahul Rawail | IN_SET_VALID | Ildikó Enyedi |
| R4 | Rahul Rawail | IN_SET_VALID | Leopoldo Torre Nilsson |

N raw: `"Rahul Rawail"`. R aggregate: Rahul Rawail; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-24 / MID

Gold: **Rahul Rawail**. First-hop subquestion (N/R): `Who is the credited director of Film T74644?`. Listed wording: `Which candidate is the credited director of Film T74644?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Rahul Rawail.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Rahul Rawail | Rahul Rawail | True | 2.0625 |
| P2 | Yuen Woo-ping | Rahul Rawail | True | 2.1687 |
| P3 | Ildikó Enyedi | Rahul Rawail | True | 0.8062 |
| P4 | Leopoldo Torre Nilsson | Rahul Rawail | True | 0.8710 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Rahul Rawail | IN_SET_VALID | Yuen Woo-ping |
| R1 | Rahul Rawail | IN_SET_VALID | Yuen Woo-ping |
| R2 | Rahul Rawail | IN_SET_VALID | Rahul Rawail |
| R3 | Rahul Rawail | IN_SET_VALID | Ildikó Enyedi |
| R4 | Rahul Rawail | IN_SET_VALID | Leopoldo Torre Nilsson |

N raw: `"Rahul Rawail"`. R aggregate: Rahul Rawail; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## development / v344-development-24 / HARD

Gold: **Rahul Rawail**. First-hop subquestion (N/R): `Who is the credited director of Film T74644?`. Listed wording: `Which candidate is the credited director of Film T74644?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Yuen Woo-ping.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Rahul Rawail | Rahul Rawail | True | 0.8312 |
| P2 | Yuen Woo-ping | Yuen Woo-ping | True | -3.9093 |
| P3 | Ildikó Enyedi | Yuen Woo-ping | True | -3.8229 |
| P4 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | True | -3.7393 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |
| R1 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |
| R2 | Rahul Rawail | IN_SET_VALID | Rahul Rawail |
| R3 | Rahul Rawail | IN_SET_VALID | Ildikó Enyedi |
| R4 | Rahul Rawail | IN_SET_VALID | Leopoldo Torre Nilsson |

N raw: `"Yuen Woo-ping"`. R aggregate: Rahul Rawail; R observed identity changes: True; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## confirmation / v344-confirmation-01 / EASY

Gold: **León Klimovsky**. First-hop subquestion (N/R): `Who is the credited director of Film T16005?`. Listed wording: `Which candidate is the credited director of Film T16005?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: León Klimovsky.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Robert P. Kerr | León Klimovsky | True | 3.1719 |
| P2 | Vojtěch Jasný | León Klimovsky | True | 2.1914 |
| P3 | Marcello Fondato | León Klimovsky | True | 2.1563 |
| P4 | León Klimovsky | León Klimovsky | True | 3.9121 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | León Klimovsky | IN_SET_VALID | Robert P. Kerr |
| R1 | León Klimovsky | IN_SET_VALID | Robert P. Kerr |
| R2 | León Klimovsky | IN_SET_VALID | Vojtěch Jasný |
| R3 | León Klimovsky | IN_SET_VALID | León Klimovsky |
| R4 | León Klimovsky | IN_SET_VALID | Marcello Fondato |

N raw: `"León Klimovsky"`. R aggregate: León Klimovsky; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## confirmation / v344-confirmation-02 / EASY

Gold: **Armando Robles Godoy**. First-hop subquestion (N/R): `Who is the credited director of Film T34219?`. Listed wording: `Which candidate is the credited director of Film T34219?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Armando Robles Godoy.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Yuen Woo-ping | Armando Robles Godoy | True | 3.1938 |
| P2 | Ildikó Enyedi | Rahul Rawail | True | 0.0808 |
| P3 | Armando Robles Godoy | Armando Robles Godoy | True | 3.2545 |
| P4 | Rahul Rawail | Armando Robles Godoy | True | 2.6138 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Armando Robles Godoy | IN_SET_VALID | Ildikó Enyedi |
| R1 | Armando Robles Godoy | IN_SET_VALID | Ildikó Enyedi |
| R2 | Armando Robles Godoy | IN_SET_VALID | Yuen Woo-ping |
| R3 | Armando Robles Godoy | IN_SET_VALID | Armando Robles Godoy |
| R4 | Armando Robles Godoy | IN_SET_VALID | Rahul Rawail |

N raw: `"Armando Robles Godoy"`. R aggregate: Armando Robles Godoy; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

Diagnostic anomalies (raw only here; full logs preserve every output):

- {"plan_id": "confirmation/v344-confirmation-02/EASY/L2", "F": "Rahul Rawail", "F_category": "IN_SET_VALID", "C": "Rahul Rawail", "S_mean": "Armando Robles Godoy", "S_sum": "Armando Robles Godoy", "raw_f": "Rahul Rawail", "note": "Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified."}

## confirmation / v344-confirmation-03 / EASY

Gold: **Jan Svěrák**. First-hop subquestion (N/R): `Who is the credited director of Film T68568?`. Listed wording: `Which candidate is the credited director of Film T68568?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Jan Svěrák.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Jan Svěrák | Jan Svěrák | True | 4.1094 |
| P2 | Rahul Rawail | Jan Svěrák | True | 2.7727 |
| P3 | Armando Robles Godoy | Jan Svěrák | True | 2.0052 |
| P4 | Ildikó Enyedi | Jan Svěrák | True | 1.9419 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Jan Svěrák | IN_SET_VALID | Armando Robles Godoy |
| R1 | Jan Svěrák | IN_SET_VALID | Armando Robles Godoy |
| R2 | Jan Svěrák | IN_SET_VALID | Jan Svěrák |
| R3 | Jan Svěrák | IN_SET_VALID | Ildikó Enyedi |
| R4 | Jan Svěrák | IN_SET_VALID | Rahul Rawail |

N raw: `"Jan Svěrák"`. R aggregate: Jan Svěrák; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## confirmation / v344-confirmation-04 / EASY

Gold: **Walter Hugo Khouri**. First-hop subquestion (N/R): `Who is the credited director of Film T13991?`. Listed wording: `Which candidate is the credited director of Film T13991?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Walter Hugo Khouri.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Marcello Fondato | Walter Hugo Khouri | True | 1.9688 |
| P2 | Walter Hugo Khouri | Walter Hugo Khouri | True | 5.5906 |
| P3 | Robert P. Kerr | Walter Hugo Khouri | True | 4.6953 |
| P4 | León Klimovsky | Walter Hugo Khouri | True | 2.2875 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R2 | Walter Hugo Khouri | IN_SET_VALID | Marcello Fondato |
| R3 | Walter Hugo Khouri | IN_SET_VALID | León Klimovsky |
| R4 | Walter Hugo Khouri | IN_SET_VALID | Robert P. Kerr |

N raw: `"Walter Hugo Khouri"`. R aggregate: Walter Hugo Khouri; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## confirmation / v344-confirmation-05 / EASY

Gold: **Anil Das**. First-hop subquestion (N/R): `Who is the credited director of Film T83771?`. Listed wording: `Which candidate is the credited director of Film T83771?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Anil Das.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Rodrigo Grande | Anil Das | True | 2.8438 |
| P2 | Gu Changwei | Anil Das | True | 1.0142 |
| P3 | Anil Das | Anil Das | True | 2.2422 |
| P4 | Helmut Käutner | Anil Das | True | 1.9193 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Anil Das | IN_SET_VALID | Rodrigo Grande |
| R1 | Anil Das | IN_SET_VALID | Rodrigo Grande |
| R2 | Anil Das | IN_SET_VALID | Anil Das |
| R3 | Anil Das | IN_SET_VALID | Gu Changwei |
| R4 | Anil Das | IN_SET_VALID | Helmut Käutner |

N raw: `"Anil Das"`. R aggregate: Anil Das; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## confirmation / v344-confirmation-06 / EASY

Gold: **Walter Hugo Khouri**. First-hop subquestion (N/R): `Who is the credited director of Film T21269?`. Listed wording: `Which candidate is the credited director of Film T21269?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Walter Hugo Khouri.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Vojtěch Jasný | Walter Hugo Khouri | True | 1.5560 |
| P2 | Walter Hugo Khouri | Walter Hugo Khouri | True | 3.0078 |
| P3 | León Klimovsky | Walter Hugo Khouri | True | 2.6367 |
| P4 | Marcello Fondato | Walter Hugo Khouri | True | 2.4250 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R2 | Walter Hugo Khouri | IN_SET_VALID | Vojtěch Jasný |
| R3 | Walter Hugo Khouri | IN_SET_VALID | León Klimovsky |
| R4 | Walter Hugo Khouri | IN_SET_VALID | Marcello Fondato |

N raw: `"Walter Hugo Khouri"`. R aggregate: Walter Hugo Khouri; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## confirmation / v344-confirmation-07 / EASY

Gold: **Robert P. Kerr**. First-hop subquestion (N/R): `Who is the credited director of Film T98395?`. Listed wording: `Which candidate is the credited director of Film T98395?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Robert P. Kerr.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Robert P. Kerr | Robert P. Kerr | True | 3.7090 |
| P2 | Bhappi Sonie | Robert P. Kerr | True | 3.1484 |
| P3 | Marcello Fondato | Robert P. Kerr | True | 2.6500 |
| P4 | Vojtěch Jasný | Robert P. Kerr | True | 2.2656 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Robert P. Kerr | IN_SET_VALID | Bhappi Sonie |
| R1 | Robert P. Kerr | IN_SET_VALID | Bhappi Sonie |
| R2 | Robert P. Kerr | IN_SET_VALID | Robert P. Kerr |
| R3 | Robert P. Kerr | IN_SET_VALID | Vojtěch Jasný |
| R4 | Robert P. Kerr | IN_SET_VALID | Marcello Fondato |

N raw: `"Robert P. Kerr"`. R aggregate: Robert P. Kerr; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## confirmation / v344-confirmation-08 / EASY

Gold: **Helmut Käutner**. First-hop subquestion (N/R): `Who is the credited director of Film T13391?`. Listed wording: `Which candidate is the credited director of Film T13391?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Helmut Käutner.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Helmut Käutner | Helmut Käutner | True | 0.1851 |
| P2 | Feng Xiaoning | Helmut Käutner | True | 2.6028 |
| P3 | Fridrikh Ermler | Helmut Käutner | True | 2.2645 |
| P4 | Rodrigo Grande | Helmut Käutner | True | 4.5040 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Helmut Käutner | IN_SET_VALID | Rodrigo Grande |
| R1 | Helmut Käutner | IN_SET_VALID | Rodrigo Grande |
| R2 | Helmut Käutner | IN_SET_VALID | Helmut Käutner |
| R3 | Helmut Käutner | IN_SET_VALID | Fridrikh Ermler |
| R4 | Helmut Käutner | IN_SET_VALID | Feng Xiaoning |

N raw: `"Helmut Käutner"`. R aggregate: Helmut Käutner; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## confirmation / v344-confirmation-09 / EASY

Gold: **Armando Robles Godoy**. First-hop subquestion (N/R): `Who is the credited director of Film T78497?`. Listed wording: `Which candidate is the credited director of Film T78497?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Armando Robles Godoy.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Armando Robles Godoy | Armando Robles Godoy | True | 3.4336 |
| P2 | Tinnu Anand | Armando Robles Godoy | True | 0.9378 |
| P3 | Jan Svěrák | Armando Robles Godoy | True | 1.4500 |
| P4 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | True | -0.2391 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Armando Robles Godoy | IN_SET_VALID | Tinnu Anand |
| R1 | Armando Robles Godoy | IN_SET_VALID | Tinnu Anand |
| R2 | — | NONCOMPLIANT | Jan Svěrák |
| R3 | Armando Robles Godoy | IN_SET_VALID | Leopoldo Torre Nilsson |
| R4 | Armando Robles Godoy | IN_SET_VALID | Armando Robles Godoy |

N raw: `"Armando Robles Godoy"`. R aggregate: UNSTABLE_OR_UNRESOLVED; R observed identity changes: False; R all four valid: False. L list sensitivity: True; N/L disagreement: none or ineligible.

Diagnostic anomalies (raw only here; full logs preserve every output):

- {"plan_id": "confirmation/v344-confirmation-09/EASY/R2", "F": null, "F_category": "NONCOMPLIANT", "C": null, "S_mean": "Armando Robles Godoy", "S_sum": "Armando Robles Godoy", "raw_f": "Armando Robles Godoy.", "note": "Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified."}

## confirmation / v344-confirmation-10 / EASY

Gold: **Vojtěch Jasný**. First-hop subquestion (N/R): `Who is the credited director of Film T85889?`. Listed wording: `Which candidate is the credited director of Film T85889?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Vojtěch Jasný.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Bhappi Sonie | Vojtěch Jasný | True | 3.7240 |
| P2 | Walter Hugo Khouri | Vojtěch Jasný | True | 3.2414 |
| P3 | James Goldstone | Vojtěch Jasný | True | 3.4792 |
| P4 | Vojtěch Jasný | Vojtěch Jasný | True | 4.6198 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Vojtěch Jasný | IN_SET_VALID | Bhappi Sonie |
| R1 | Vojtěch Jasný | IN_SET_VALID | Bhappi Sonie |
| R2 | Vojtěch Jasný | IN_SET_VALID | Walter Hugo Khouri |
| R3 | Vojtěch Jasný | IN_SET_VALID | James Goldstone |
| R4 | Vojtěch Jasný | IN_SET_VALID | Vojtěch Jasný |

N raw: `"Vojtěch Jasný"`. R aggregate: Vojtěch Jasný; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## confirmation / v344-confirmation-11 / EASY

Gold: **James Goldstone**. First-hop subquestion (N/R): `Who is the credited director of Film T80908?`. Listed wording: `Which candidate is the credited director of Film T80908?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: James Goldstone.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Vojtěch Jasný | James Goldstone | True | 2.4922 |
| P2 | Bhappi Sonie | James Goldstone | True | 2.6406 |
| P3 | James Goldstone | James Goldstone | True | 3.8438 |
| P4 | León Klimovsky | James Goldstone | True | 2.3125 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | James Goldstone | IN_SET_VALID | James Goldstone |
| R1 | James Goldstone | IN_SET_VALID | James Goldstone |
| R2 | James Goldstone | IN_SET_VALID | Bhappi Sonie |
| R3 | James Goldstone | IN_SET_VALID | Vojtěch Jasný |
| R4 | James Goldstone | IN_SET_VALID | León Klimovsky |

N raw: `"James Goldstone"`. R aggregate: James Goldstone; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## confirmation / v344-confirmation-12 / EASY

Gold: **Rahul Rawail**. First-hop subquestion (N/R): `Who is the credited director of Film T83379?`. Listed wording: `Which candidate is the credited director of Film T83379?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Rahul Rawail.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Leopoldo Torre Nilsson | Rahul Rawail | True | 1.6328 |
| P2 | Jan Svěrák | Rahul Rawail | True | 3.4160 |
| P3 | Tinnu Anand | Tinnu Anand | True | -0.5688 |
| P4 | Rahul Rawail | Rahul Rawail | True | 3.4531 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Rahul Rawail | IN_SET_VALID | Rahul Rawail |
| R1 | Rahul Rawail | IN_SET_VALID | Rahul Rawail |
| R2 | Rahul Rawail | IN_SET_VALID | Jan Svěrák |
| R3 | Rahul Rawail | IN_SET_VALID | Tinnu Anand |
| R4 | Rahul Rawail | IN_SET_VALID | Leopoldo Torre Nilsson |

N raw: `"Rahul Rawail"`. R aggregate: Rahul Rawail; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## confirmation / v344-confirmation-13 / EASY

Gold: **Helmut Käutner**. First-hop subquestion (N/R): `Who is the credited director of Film T51919?`. Listed wording: `Which candidate is the credited director of Film T51919?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Helmut Käutner.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Rodrigo Grande | Helmut Käutner | True | 2.8189 |
| P2 | Rolf Schübel | Helmut Käutner | True | 1.2563 |
| P3 | Gu Changwei | Helmut Käutner | True | 2.1461 |
| P4 | Helmut Käutner | Helmut Käutner | True | 3.7830 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Helmut Käutner | IN_SET_VALID | Rodrigo Grande |
| R1 | Helmut Käutner | IN_SET_VALID | Rodrigo Grande |
| R2 | Helmut Käutner | IN_SET_VALID | Gu Changwei |
| R3 | Helmut Käutner | IN_SET_VALID | Rolf Schübel |
| R4 | Helmut Käutner | IN_SET_VALID | Helmut Käutner |

N raw: `"Helmut Käutner"`. R aggregate: Helmut Käutner; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## confirmation / v344-confirmation-14 / EASY

Gold: **Rahul Rawail**. First-hop subquestion (N/R): `Who is the credited director of Film T26132?`. Listed wording: `Which candidate is the credited director of Film T26132?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Rahul Rawail.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Ildikó Enyedi | Rahul Rawail | True | 3.2130 |
| P2 | Leopoldo Torre Nilsson | Rahul Rawail | True | 2.0684 |
| P3 | Rahul Rawail | Rahul Rawail | True | 3.4621 |
| P4 | Armando Robles Godoy | Rahul Rawail | True | 2.9902 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Rahul Rawail | IN_SET_VALID | Ildikó Enyedi |
| R1 | Rahul Rawail | IN_SET_VALID | Ildikó Enyedi |
| R2 | Rahul Rawail | IN_SET_VALID | Armando Robles Godoy |
| R3 | Rahul Rawail | IN_SET_VALID | Rahul Rawail |
| R4 | Rahul Rawail | IN_SET_VALID | Leopoldo Torre Nilsson |

N raw: `"Rahul Rawail"`. R aggregate: Rahul Rawail; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## confirmation / v344-confirmation-15 / EASY

Gold: **Leopoldo Torre Nilsson**. First-hop subquestion (N/R): `Who is the credited director of Film T72869?`. Listed wording: `Which candidate is the credited director of Film T72869?`. Partial robustness (same wrong identity 3/4): False.

L class: ORDER_SENSITIVE; modal identity: Leopoldo Torre Nilsson.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Ildikó Enyedi | Ildikó Enyedi | True | -0.1355 |
| P2 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | True | 2.0500 |
| P3 | Armando Robles Godoy | Leopoldo Torre Nilsson | True | 1.9115 |
| P4 | Tinnu Anand | Leopoldo Torre Nilsson | True | 3.2946 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Leopoldo Torre Nilsson | IN_SET_VALID | Tinnu Anand |
| R1 | Leopoldo Torre Nilsson | IN_SET_VALID | Tinnu Anand |
| R2 | Leopoldo Torre Nilsson | IN_SET_VALID | Ildikó Enyedi |
| R3 | Leopoldo Torre Nilsson | IN_SET_VALID | Leopoldo Torre Nilsson |
| R4 | Leopoldo Torre Nilsson | IN_SET_VALID | Armando Robles Godoy |

N raw: `"Leopoldo Torre Nilsson"`. R aggregate: Leopoldo Torre Nilsson; R observed identity changes: False; R all four valid: True. L list sensitivity: True; N/L disagreement: none or ineligible.

## confirmation / v344-confirmation-16 / EASY

Gold: **Robert P. Kerr**. First-hop subquestion (N/R): `Who is the credited director of Film T77924?`. Listed wording: `Which candidate is the credited director of Film T77924?`. Partial robustness (same wrong identity 3/4): False.

L class: ALL_CORRECT; modal identity: Robert P. Kerr.

| Rotation | First option | C chosen identity | C valid | Gold margin |
|---|---|---|---|---|
| P1 | Bhappi Sonie | Robert P. Kerr | True | 2.8021 |
| P2 | Robert P. Kerr | Robert P. Kerr | True | 1.7552 |
| P3 | León Klimovsky | Robert P. Kerr | True | 1.5885 |
| P4 | Marcello Fondato | Robert P. Kerr | True | 1.7625 |

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Robert P. Kerr | IN_SET_VALID | Bhappi Sonie |
| R1 | Robert P. Kerr | IN_SET_VALID | Bhappi Sonie |
| R2 | Robert P. Kerr | IN_SET_VALID | León Klimovsky |
| R3 | Robert P. Kerr | IN_SET_VALID | Marcello Fondato |
| R4 | Robert P. Kerr | IN_SET_VALID | Robert P. Kerr |

N raw: `"Robert P. Kerr"`. R aggregate: Robert P. Kerr; R observed identity changes: False; R all four valid: True. L list sensitivity: False; N/L disagreement: none or ineligible.

## old / dev-04 / EASY

Gold: **Leopoldo Torre Nilsson**. First-hop subquestion (N/R): `Who is the credited director of Film T34217?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Leopoldo Torre Nilsson | IN_SET_VALID | Armando Robles Godoy |
| R1 | Leopoldo Torre Nilsson | IN_SET_VALID | Armando Robles Godoy |
| R2 | Leopoldo Torre Nilsson | IN_SET_VALID | Rahul Rawail |
| R3 | Leopoldo Torre Nilsson | IN_SET_VALID | Leopoldo Torre Nilsson |
| R4 | Leopoldo Torre Nilsson | IN_SET_VALID | Tinnu Anand |

N raw: `"Leopoldo Torre Nilsson"`. R aggregate: Leopoldo Torre Nilsson; R observed identity changes: False; R all four valid: True.

## old / dev-04 / MID

Gold: **Leopoldo Torre Nilsson**. First-hop subquestion (N/R): `Who is the credited director of Film T34217?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Leopoldo Torre Nilsson | IN_SET_VALID | Armando Robles Godoy |
| R1 | Leopoldo Torre Nilsson | IN_SET_VALID | Armando Robles Godoy |
| R2 | Leopoldo Torre Nilsson | IN_SET_VALID | Rahul Rawail |
| R3 | Leopoldo Torre Nilsson | IN_SET_VALID | Leopoldo Torre Nilsson |
| R4 | Leopoldo Torre Nilsson | IN_SET_VALID | Tinnu Anand |

N raw: `"Leopoldo Torre Nilsson"`. R aggregate: Leopoldo Torre Nilsson; R observed identity changes: False; R all four valid: True.

## old / dev-04 / HARD

Gold: **Leopoldo Torre Nilsson**. First-hop subquestion (N/R): `Who is the credited director of Film T34217?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Leopoldo Torre Nilsson | IN_SET_VALID | Armando Robles Godoy |
| R1 | Leopoldo Torre Nilsson | IN_SET_VALID | Armando Robles Godoy |
| R2 | Rahul Rawail | IN_SET_VALID | Rahul Rawail |
| R3 | Leopoldo Torre Nilsson | IN_SET_VALID | Leopoldo Torre Nilsson |
| R4 | Leopoldo Torre Nilsson | IN_SET_VALID | Tinnu Anand |

N raw: `"Leopoldo Torre Nilsson"`. R aggregate: Leopoldo Torre Nilsson; R observed identity changes: True; R all four valid: True.

## old / dev-07 / EASY

Gold: **Walter Hugo Khouri**. First-hop subquestion (N/R): `Who is the credited director of Film T66029?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R2 | Walter Hugo Khouri | IN_SET_VALID | James Goldstone |
| R3 | — | NONCOMPLIANT | León Klimovsky |
| R4 | Walter Hugo Khouri | IN_SET_VALID | Marcello Fondato |

N raw: `"Walter Hugo Khouri"`. R aggregate: UNSTABLE_OR_UNRESOLVED; R observed identity changes: False; R all four valid: False.

Diagnostic anomalies (raw only here; full logs preserve every output):

- {"plan_id": "old/dev-07/EASY/R3", "F": null, "F_category": "NONCOMPLIANT", "C": null, "S_mean": "Walter Hugo Khouri", "S_sum": "Walter Hugo Khouri", "raw_f": "Walter Hugo Khouri.", "note": "Teacher-forced score ranking, greedy decoding and length normalization are different operations; no internal cause identified."}

## old / dev-07 / MID

Gold: **Walter Hugo Khouri**. First-hop subquestion (N/R): `Who is the credited director of Film T66029?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R2 | Walter Hugo Khouri | IN_SET_VALID | James Goldstone |
| R3 | Walter Hugo Khouri | IN_SET_VALID | León Klimovsky |
| R4 | Walter Hugo Khouri | IN_SET_VALID | Marcello Fondato |

N raw: `"Walter Hugo Khouri"`. R aggregate: Walter Hugo Khouri; R observed identity changes: False; R all four valid: True.

## old / dev-07 / HARD

Gold: **Walter Hugo Khouri**. First-hop subquestion (N/R): `Who is the credited director of Film T66029?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R1 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R2 | Walter Hugo Khouri | IN_SET_VALID | James Goldstone |
| R3 | Walter Hugo Khouri | IN_SET_VALID | León Klimovsky |
| R4 | Marcello Fondato | IN_SET_VALID | Marcello Fondato |

N raw: `"Walter Hugo Khouri"`. R aggregate: Walter Hugo Khouri; R observed identity changes: True; R all four valid: True.

## old / dev-05 / EASY

Gold: **Helmut Käutner**. First-hop subquestion (N/R): `Who is the credited director of Film T89245?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Helmut Käutner | IN_SET_VALID | Feng Xiaoning |
| R1 | Helmut Käutner | IN_SET_VALID | Feng Xiaoning |
| R2 | Helmut Käutner | IN_SET_VALID | Helmut Käutner |
| R3 | Helmut Käutner | IN_SET_VALID | Fridrikh Ermler |
| R4 | Helmut Käutner | IN_SET_VALID | Rolf Schübel |

N raw: `"Helmut Käutner"`. R aggregate: Helmut Käutner; R observed identity changes: False; R all four valid: True.

## old / dev-05 / MID

Gold: **Helmut Käutner**. First-hop subquestion (N/R): `Who is the credited director of Film T89245?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Helmut Käutner | IN_SET_VALID | Feng Xiaoning |
| R1 | Helmut Käutner | IN_SET_VALID | Feng Xiaoning |
| R2 | Helmut Käutner | IN_SET_VALID | Helmut Käutner |
| R3 | Helmut Käutner | IN_SET_VALID | Fridrikh Ermler |
| R4 | Helmut Käutner | IN_SET_VALID | Rolf Schübel |

N raw: `"Helmut Käutner"`. R aggregate: Helmut Käutner; R observed identity changes: False; R all four valid: True.

## old / dev-05 / HARD

Gold: **Helmut Käutner**. First-hop subquestion (N/R): `Who is the credited director of Film T89245?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Feng Xiaoning | IN_SET_VALID | Feng Xiaoning |
| R1 | Feng Xiaoning | IN_SET_VALID | Feng Xiaoning |
| R2 | Helmut Käutner | IN_SET_VALID | Helmut Käutner |
| R3 | Feng Xiaoning | IN_SET_VALID | Fridrikh Ermler |
| R4 | Helmut Käutner | IN_SET_VALID | Rolf Schübel |

N raw: `"Feng Xiaoning"`. R aggregate: UNSTABLE_OR_UNRESOLVED; R observed identity changes: True; R all four valid: True.

## old / dev-01 / EASY

Gold: **Walter Hugo Khouri**. First-hop subquestion (N/R): `Who is the credited director of Film T27036?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Walter Hugo Khouri | IN_SET_VALID | Vojtěch Jasný |
| R1 | Walter Hugo Khouri | IN_SET_VALID | Vojtěch Jasný |
| R2 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R3 | Walter Hugo Khouri | IN_SET_VALID | James Goldstone |
| R4 | Walter Hugo Khouri | IN_SET_VALID | Marcello Fondato |

N raw: `"Walter Hugo Khouri"`. R aggregate: Walter Hugo Khouri; R observed identity changes: False; R all four valid: True.

## old / dev-01 / MID

Gold: **Walter Hugo Khouri**. First-hop subquestion (N/R): `Who is the credited director of Film T27036?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Walter Hugo Khouri | IN_SET_VALID | Vojtěch Jasný |
| R1 | Walter Hugo Khouri | IN_SET_VALID | Vojtěch Jasný |
| R2 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R3 | Walter Hugo Khouri | IN_SET_VALID | James Goldstone |
| R4 | Walter Hugo Khouri | IN_SET_VALID | Marcello Fondato |

N raw: `"Walter Hugo Khouri"`. R aggregate: Walter Hugo Khouri; R observed identity changes: False; R all four valid: True.

## old / dev-01 / HARD

Gold: **Walter Hugo Khouri**. First-hop subquestion (N/R): `Who is the credited director of Film T27036?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Vojtěch Jasný | IN_SET_VALID | Vojtěch Jasný |
| R1 | Vojtěch Jasný | IN_SET_VALID | Vojtěch Jasný |
| R2 | Walter Hugo Khouri | IN_SET_VALID | Walter Hugo Khouri |
| R3 | Walter Hugo Khouri | IN_SET_VALID | James Goldstone |
| R4 | Walter Hugo Khouri | IN_SET_VALID | Marcello Fondato |

N raw: `"Vojtěch Jasný"`. R aggregate: Walter Hugo Khouri; R observed identity changes: True; R all four valid: True.

## old / dev-06 / EASY

Gold: **Gu Changwei**. First-hop subquestion (N/R): `Who is the credited director of Film T12112?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Gu Changwei | IN_SET_VALID | Rolf Schübel |
| R1 | Gu Changwei | IN_SET_VALID | Rolf Schübel |
| R2 | Gu Changwei | IN_SET_VALID | Rodrigo Grande |
| R3 | Gu Changwei | IN_SET_VALID | Anil Das |
| R4 | Gu Changwei | IN_SET_VALID | Gu Changwei |

N raw: `"Gu Changwei"`. R aggregate: Gu Changwei; R observed identity changes: False; R all four valid: True.

## old / dev-06 / MID

Gold: **Gu Changwei**. First-hop subquestion (N/R): `Who is the credited director of Film T12112?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Gu Changwei | IN_SET_VALID | Rolf Schübel |
| R1 | Gu Changwei | IN_SET_VALID | Rolf Schübel |
| R2 | Gu Changwei | IN_SET_VALID | Rodrigo Grande |
| R3 | Gu Changwei | IN_SET_VALID | Anil Das |
| R4 | Gu Changwei | IN_SET_VALID | Gu Changwei |

N raw: `"Gu Changwei"`. R aggregate: Gu Changwei; R observed identity changes: False; R all four valid: True.

## old / dev-06 / HARD

Gold: **Gu Changwei**. First-hop subquestion (N/R): `Who is the credited director of Film T12112?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Gu Changwei | IN_SET_VALID | Rolf Schübel |
| R1 | Gu Changwei | IN_SET_VALID | Rolf Schübel |
| R2 | Gu Changwei | IN_SET_VALID | Rodrigo Grande |
| R3 | Gu Changwei | IN_SET_VALID | Anil Das |
| R4 | Gu Changwei | IN_SET_VALID | Gu Changwei |

N raw: `"Gu Changwei"`. R aggregate: Gu Changwei; R observed identity changes: False; R all four valid: True.

## old / dev-08 / EASY

Gold: **Yuen Woo-ping**. First-hop subquestion (N/R): `Who is the credited director of Film T49524?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |
| R1 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |
| R2 | Yuen Woo-ping | IN_SET_VALID | Ildikó Enyedi |
| R3 | Yuen Woo-ping | IN_SET_VALID | Tinnu Anand |
| R4 | Yuen Woo-ping | IN_SET_VALID | Rahul Rawail |

N raw: `"Yuen Woo-ping"`. R aggregate: Yuen Woo-ping; R observed identity changes: False; R all four valid: True.

## old / dev-08 / MID

Gold: **Yuen Woo-ping**. First-hop subquestion (N/R): `Who is the credited director of Film T49524?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |
| R1 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |
| R2 | Yuen Woo-ping | IN_SET_VALID | Ildikó Enyedi |
| R3 | Yuen Woo-ping | IN_SET_VALID | Tinnu Anand |
| R4 | Rahul Rawail | IN_SET_VALID | Rahul Rawail |

N raw: `"Yuen Woo-ping"`. R aggregate: Yuen Woo-ping; R observed identity changes: True; R all four valid: True.

## old / dev-08 / HARD

Gold: **Yuen Woo-ping**. First-hop subquestion (N/R): `Who is the credited director of Film T49524?`.

| Interface | Strict identity | Category | First name record |
|---|---|---|---|
| N1 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |
| R1 | Yuen Woo-ping | IN_SET_VALID | Yuen Woo-ping |
| R2 | Yuen Woo-ping | IN_SET_VALID | Ildikó Enyedi |
| R3 | Tinnu Anand | IN_SET_VALID | Tinnu Anand |
| R4 | Yuen Woo-ping | IN_SET_VALID | Rahul Rawail |

N raw: `"Yuen Woo-ping"`. R aggregate: Yuen Woo-ping; R observed identity changes: True; R all four valid: True.
