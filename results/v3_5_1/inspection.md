# Case-level injected-state inspection

Same fact, same semantic relevance, different task-role heading; perceived authority not independently isolated.

No upstream model generated the supplied state. Each r2 question is identical across the six arms within its case.

## v351-01: Film T377240

Gold: Rolf Schübel → Stuttgart; donor: Rodrigo Grande → Rosario.

Question: `Based on the supplied context, what is the place of birth of the credited director of Film T377240?`

| Condition | Supplied intermediate | Role | Raw output | Outcome |
|---|---|---|---|---|
| S0 | Rodrigo Grande | baseline | "Stuttgart" | OVERRIDE_TO_GOLD |
| G-CURRENT | Rodrigo Grande | Current-task dossier | "Stuttgart" | OVERRIDE_TO_GOLD |
| G-BACKGROUND | Rodrigo Grande | Background/history dossier | "Stuttgart" | OVERRIDE_TO_GOLD |
| W-CURRENT | Rodrigo Grande | Current-task dossier | "Rosario" | PROPAGATE_WRONG |
| C0 | Rolf Schübel | baseline | "Stuttgart" | GOLD_FOLLOW |
| C-WCURRENT | Rolf Schübel | Current-task dossier | "Rosario" | INDUCED_WRONG |

Paired contrast: {"case_id": "v351-01", "background": "C", "current": "C", "background_category": "VALID", "current_category": "VALID", "delta_OR": 0, "delta_PR": 0, "both_valid": true, "reverse_correct_to_wrong": true}.

## v351-02: Film T381657

Gold: Rolf Schübel → Stuttgart; donor: Helmut Käutner → Düsseldorf.

Question: `Based on the supplied context, what is the place of birth of the credited director of Film T381657?`

| Condition | Supplied intermediate | Role | Raw output | Outcome |
|---|---|---|---|---|
| S0 | Helmut Käutner | baseline | "Düsseldorf" | PROPAGATE_WRONG |
| G-CURRENT | Helmut Käutner | Current-task dossier | "Stuttgart" | OVERRIDE_TO_GOLD |
| G-BACKGROUND | Helmut Käutner | Background/history dossier | "Stuttgart" | OVERRIDE_TO_GOLD |
| W-CURRENT | Helmut Käutner | Current-task dossier | "Düsseldorf" | PROPAGATE_WRONG |
| C0 | Rolf Schübel | baseline | "Stuttgart" | GOLD_FOLLOW |
| C-WCURRENT | Rolf Schübel | Current-task dossier | "Düsseldorf" | INDUCED_WRONG |

Paired contrast: {"case_id": "v351-02", "background": "C", "current": "C", "background_category": "VALID", "current_category": "VALID", "delta_OR": 0, "delta_PR": 0, "both_valid": true, "reverse_correct_to_wrong": true}.

## v351-03: Film T366143

Gold: Fridrikh Ermler → Rēzekne; donor: Helmut Käutner → Düsseldorf.

Question: `Based on the supplied context, what is the place of birth of the credited director of Film T366143?`

| Condition | Supplied intermediate | Role | Raw output | Outcome |
|---|---|---|---|---|
| S0 | Helmut Käutner | baseline | "Düsseldorf" | PROPAGATE_WRONG |
| G-CURRENT | Helmut Käutner | Current-task dossier | "Rēzekne" | OVERRIDE_TO_GOLD |
| G-BACKGROUND | Helmut Käutner | Background/history dossier | "Rēzekne" | OVERRIDE_TO_GOLD |
| W-CURRENT | Helmut Käutner | Current-task dossier | "Düsseldorf" | PROPAGATE_WRONG |
| C0 | Fridrikh Ermler | baseline | "Düsseldorf" | INDUCED_WRONG |
| C-WCURRENT | Fridrikh Ermler | Current-task dossier | "Düsseldorf" | INDUCED_WRONG |

Paired contrast: {"case_id": "v351-03", "background": "C", "current": "C", "background_category": "VALID", "current_category": "VALID", "delta_OR": 0, "delta_PR": 0, "both_valid": true, "reverse_correct_to_wrong": false}.

## v351-04: Film T368981

Gold: Fridrikh Ermler → Rēzekne; donor: Gu Changwei → Xi'an.

Question: `Based on the supplied context, what is the place of birth of the credited director of Film T368981?`

| Condition | Supplied intermediate | Role | Raw output | Outcome |
|---|---|---|---|---|
| S0 | Gu Changwei | baseline | "Xi'an" | PROPAGATE_WRONG |
| G-CURRENT | Gu Changwei | Current-task dossier | "Rēzekne" | OVERRIDE_TO_GOLD |
| G-BACKGROUND | Gu Changwei | Background/history dossier | "Rēzekne" | OVERRIDE_TO_GOLD |
| W-CURRENT | Gu Changwei | Current-task dossier | "Xi'an" | PROPAGATE_WRONG |
| C0 | Fridrikh Ermler | baseline | "Unknown" | UNKNOWN |
| C-WCURRENT | Fridrikh Ermler | Current-task dossier | "Xi'an" | INDUCED_WRONG |

Paired contrast: {"case_id": "v351-04", "background": "C", "current": "C", "background_category": "VALID", "current_category": "VALID", "delta_OR": 0, "delta_PR": 0, "both_valid": true, "reverse_correct_to_wrong": false}.

## v351-05: Film T399418

Gold: Rodrigo Grande → Rosario; donor: Feng Xiaoning → Xi'an.

Question: `Based on the supplied context, what is the place of birth of the credited director of Film T399418?`

| Condition | Supplied intermediate | Role | Raw output | Outcome |
|---|---|---|---|---|
| S0 | Feng Xiaoning | baseline | "Xi'an" | PROPAGATE_WRONG |
| G-CURRENT | Feng Xiaoning | Current-task dossier | "Rosario" | OVERRIDE_TO_GOLD |
| G-BACKGROUND | Feng Xiaoning | Background/history dossier | "Rosario" | OVERRIDE_TO_GOLD |
| W-CURRENT | Feng Xiaoning | Current-task dossier | "Xi'an" | PROPAGATE_WRONG |
| C0 | Rodrigo Grande | baseline | "Rosario" | GOLD_FOLLOW |
| C-WCURRENT | Rodrigo Grande | Current-task dossier | "Xi'an" | INDUCED_WRONG |

Paired contrast: {"case_id": "v351-05", "background": "C", "current": "C", "background_category": "VALID", "current_category": "VALID", "delta_OR": 0, "delta_PR": 0, "both_valid": true, "reverse_correct_to_wrong": true}.

## v351-06: Film T368478

Gold: Rolf Schübel → Stuttgart; donor: Anil Das → Kottayam.

Question: `Based on the supplied context, what is the place of birth of the credited director of Film T368478?`

| Condition | Supplied intermediate | Role | Raw output | Outcome |
|---|---|---|---|---|
| S0 | Anil Das | baseline | "Stuttgart" | OVERRIDE_TO_GOLD |
| G-CURRENT | Anil Das | Current-task dossier | "Stuttgart" | OVERRIDE_TO_GOLD |
| G-BACKGROUND | Anil Das | Background/history dossier | "Stuttgart" | OVERRIDE_TO_GOLD |
| W-CURRENT | Anil Das | Current-task dossier | "Kottayam" | PROPAGATE_WRONG |
| C0 | Rolf Schübel | baseline | "Stuttgart" | GOLD_FOLLOW |
| C-WCURRENT | Rolf Schübel | Current-task dossier | "Kottayam" | INDUCED_WRONG |

Paired contrast: {"case_id": "v351-06", "background": "C", "current": "C", "background_category": "VALID", "current_category": "VALID", "delta_OR": 0, "delta_PR": 0, "both_valid": true, "reverse_correct_to_wrong": true}.

## v351-07: Film T394378

Gold: Helmut Käutner → Düsseldorf; donor: Rodrigo Grande → Rosario.

Question: `Based on the supplied context, what is the place of birth of the credited director of Film T394378?`

| Condition | Supplied intermediate | Role | Raw output | Outcome |
|---|---|---|---|---|
| S0 | Rodrigo Grande | baseline | "Rosario" | PROPAGATE_WRONG |
| G-CURRENT | Rodrigo Grande | Current-task dossier | "Düsseldorf" | OVERRIDE_TO_GOLD |
| G-BACKGROUND | Rodrigo Grande | Background/history dossier | "Düsseldorf" | OVERRIDE_TO_GOLD |
| W-CURRENT | Rodrigo Grande | Current-task dossier | "Rosario" | PROPAGATE_WRONG |
| C0 | Helmut Käutner | baseline | "Düsseldorf" | GOLD_FOLLOW |
| C-WCURRENT | Helmut Käutner | Current-task dossier | "Rosario" | INDUCED_WRONG |

Paired contrast: {"case_id": "v351-07", "background": "C", "current": "C", "background_category": "VALID", "current_category": "VALID", "delta_OR": 0, "delta_PR": 0, "both_valid": true, "reverse_correct_to_wrong": true}.

## v351-08: Film T392529

Gold: Anil Das → Kottayam; donor: Rodrigo Grande → Rosario.

Question: `Based on the supplied context, what is the place of birth of the credited director of Film T392529?`

| Condition | Supplied intermediate | Role | Raw output | Outcome |
|---|---|---|---|---|
| S0 | Rodrigo Grande | baseline | "Rosario" | PROPAGATE_WRONG |
| G-CURRENT | Rodrigo Grande | Current-task dossier | "Kottayam" | OVERRIDE_TO_GOLD |
| G-BACKGROUND | Rodrigo Grande | Background/history dossier | "Kottayam" | OVERRIDE_TO_GOLD |
| W-CURRENT | Rodrigo Grande | Current-task dossier | "Rosario" | PROPAGATE_WRONG |
| C0 | Anil Das | baseline | "Kottayam" | GOLD_FOLLOW |
| C-WCURRENT | Anil Das | Current-task dossier | "Rosario" | INDUCED_WRONG |

Paired contrast: {"case_id": "v351-08", "background": "C", "current": "C", "background_category": "VALID", "current_category": "VALID", "delta_OR": 0, "delta_PR": 0, "both_valid": true, "reverse_correct_to_wrong": true}.

## v351-09: Film T399350

Gold: Rolf Schübel → Stuttgart; donor: Feng Xiaoning → Xi'an.

Question: `Based on the supplied context, what is the place of birth of the credited director of Film T399350?`

| Condition | Supplied intermediate | Role | Raw output | Outcome |
|---|---|---|---|---|
| S0 | Feng Xiaoning | baseline | "Xi'an" | PROPAGATE_WRONG |
| G-CURRENT | Feng Xiaoning | Current-task dossier | "Stuttgart" | OVERRIDE_TO_GOLD |
| G-BACKGROUND | Feng Xiaoning | Background/history dossier | "Stuttgart" | OVERRIDE_TO_GOLD |
| W-CURRENT | Feng Xiaoning | Current-task dossier | "Xi'an" | PROPAGATE_WRONG |
| C0 | Rolf Schübel | baseline | "Stuttgart" | GOLD_FOLLOW |
| C-WCURRENT | Rolf Schübel | Current-task dossier | "Xi'an" | INDUCED_WRONG |

Paired contrast: {"case_id": "v351-09", "background": "C", "current": "C", "background_category": "VALID", "current_category": "VALID", "delta_OR": 0, "delta_PR": 0, "both_valid": true, "reverse_correct_to_wrong": true}.

## v351-10: Film T367568

Gold: Feng Xiaoning → Xi'an; donor: Helmut Käutner → Düsseldorf.

Question: `Based on the supplied context, what is the place of birth of the credited director of Film T367568?`

| Condition | Supplied intermediate | Role | Raw output | Outcome |
|---|---|---|---|---|
| S0 | Helmut Käutner | baseline | "Düsseldorf" | PROPAGATE_WRONG |
| G-CURRENT | Helmut Käutner | Current-task dossier | "Xi'an" | OVERRIDE_TO_GOLD |
| G-BACKGROUND | Helmut Käutner | Background/history dossier | "Xi'an" | OVERRIDE_TO_GOLD |
| W-CURRENT | Helmut Käutner | Current-task dossier | "Düsseldorf" | PROPAGATE_WRONG |
| C0 | Feng Xiaoning | baseline | "Düsseldorf" | INDUCED_WRONG |
| C-WCURRENT | Feng Xiaoning | Current-task dossier | "Düsseldorf" | INDUCED_WRONG |

Paired contrast: {"case_id": "v351-10", "background": "C", "current": "C", "background_category": "VALID", "current_category": "VALID", "delta_OR": 0, "delta_PR": 0, "both_valid": true, "reverse_correct_to_wrong": false}.

## v351-11: Film T373560

Gold: Fridrikh Ermler → Rēzekne; donor: Feng Xiaoning → Xi'an.

Question: `Based on the supplied context, what is the place of birth of the credited director of Film T373560?`

| Condition | Supplied intermediate | Role | Raw output | Outcome |
|---|---|---|---|---|
| S0 | Feng Xiaoning | baseline | "Xi'an" | PROPAGATE_WRONG |
| G-CURRENT | Feng Xiaoning | Current-task dossier | "Rēzekne" | OVERRIDE_TO_GOLD |
| G-BACKGROUND | Feng Xiaoning | Background/history dossier | "Rēzekne" | OVERRIDE_TO_GOLD |
| W-CURRENT | Feng Xiaoning | Current-task dossier | "Xi'an" | PROPAGATE_WRONG |
| C0 | Fridrikh Ermler | baseline | "Rēzekne" | GOLD_FOLLOW |
| C-WCURRENT | Fridrikh Ermler | Current-task dossier | "Xi'an" | INDUCED_WRONG |

Paired contrast: {"case_id": "v351-11", "background": "C", "current": "C", "background_category": "VALID", "current_category": "VALID", "delta_OR": 0, "delta_PR": 0, "both_valid": true, "reverse_correct_to_wrong": true}.

## v351-12: Film T387137

Gold: Helmut Käutner → Düsseldorf; donor: Anil Das → Kottayam.

Question: `Based on the supplied context, what is the place of birth of the credited director of Film T387137?`

| Condition | Supplied intermediate | Role | Raw output | Outcome |
|---|---|---|---|---|
| S0 | Anil Das | baseline | "Düsseldorf" | OVERRIDE_TO_GOLD |
| G-CURRENT | Anil Das | Current-task dossier | "Düsseldorf" | OVERRIDE_TO_GOLD |
| G-BACKGROUND | Anil Das | Background/history dossier | "Düsseldorf" | OVERRIDE_TO_GOLD |
| W-CURRENT | Anil Das | Current-task dossier | "Kottayam" | PROPAGATE_WRONG |
| C0 | Helmut Käutner | baseline | "Düsseldorf" | GOLD_FOLLOW |
| C-WCURRENT | Helmut Käutner | Current-task dossier | "Kottayam" | INDUCED_WRONG |

Paired contrast: {"case_id": "v351-12", "background": "C", "current": "C", "background_category": "VALID", "current_category": "VALID", "delta_OR": 0, "delta_PR": 0, "both_valid": true, "reverse_correct_to_wrong": true}.

## Exact matched sample prompts

### G-CURRENT

```text
This is a synthetic catalog task. Film identifiers and credited-director associations are constructed for this task. Use the supplied context.

Task: The current question concerns Film T377240.

Reference notes (source: project record set):
Rodrigo Grande's place of birth is Rosario.
Rolf Schübel's place of birth is Stuttgart.

Current-task dossier (source: project record set):
Film T377240 has credited director Rolf Schübel.

Externally supplied working intermediate state (not an earlier model answer):
Rodrigo Grande

Question: Based on the supplied context, what is the place of birth of the credited director of Film T377240?
Output only the city name.
```

### G-BACKGROUND

```text
This is a synthetic catalog task. Film identifiers and credited-director associations are constructed for this task. Use the supplied context.

Task: The current question concerns Film T377240.

Reference notes (source: project record set):
Rodrigo Grande's place of birth is Rosario.
Rolf Schübel's place of birth is Stuttgart.

Background/history dossier (source: project record set):
Film T377240 has credited director Rolf Schübel.

Externally supplied working intermediate state (not an earlier model answer):
Rodrigo Grande

Question: Based on the supplied context, what is the place of birth of the credited director of Film T377240?
Output only the city name.
```
