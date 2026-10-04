# Candidate-order counterfactual inspection

Each table is one repeated-measures set, not four independent cases. Only the numbered candidate list changes; name records, graph and question are fixed. Full F raw text and all candidate scores remain in the channel JSONL files. Margin is gold minus best wrong mean log probability, in nats/token.

## dev-04 / EASY

Gold: Leopoldo Torre Nilsson. **MIXED_POSITION_IDENTITY** — Order changes choices, with no identity or absolute position selected more than twice.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Tinnu Anand | Armando Robles Godoy | Leopoldo Torre Nilsson | Rahul Rawail | 3 | Tinnu Anand | Tinnu Anand | -0.2110 |
| P2 | Armando Robles Godoy | Leopoldo Torre Nilsson | Rahul Rawail | Tinnu Anand | 2 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | 0.6899 |
| P3 | Leopoldo Torre Nilsson | Rahul Rawail | Tinnu Anand | Armando Robles Godoy | 1 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | 0.2291 |
| P4 | Rahul Rawail | Tinnu Anand | Armando Robles Godoy | Leopoldo Torre Nilsson | 4 | Tinnu Anand | Tinnu Anand | -0.9769 |

ISR=0.50; literal PFR=1/3 (33.3%); strict PFR=0/3 (0.0%); strict conditional PFR=0/2 (0.0%).


Adjacent changes:

- P1→P2: Tinnu Anand → Leopoldo Torre Nilsson; new first=Armando Robles Godoy; literal=False; strict=False.
- P2→P3: Leopoldo Torre Nilsson → Leopoldo Torre Nilsson; new first=Leopoldo Torre Nilsson; literal=True; strict=False.
- P3→P4: Leopoldo Torre Nilsson → Tinnu Anand; new first=Rahul Rawail; literal=False; strict=False.

## dev-04 / MID

Gold: Leopoldo Torre Nilsson. **POSITION_1_LOCKED** — Selection tracks position 1 in at least three orders while switching identities.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Tinnu Anand | Armando Robles Godoy | Leopoldo Torre Nilsson | Rahul Rawail | 3 | Tinnu Anand | Tinnu Anand | -0.4233 |
| P2 | Armando Robles Godoy | Leopoldo Torre Nilsson | Rahul Rawail | Tinnu Anand | 2 | Armando Robles Godoy | Armando Robles Godoy | -0.4007 |
| P3 | Leopoldo Torre Nilsson | Rahul Rawail | Tinnu Anand | Armando Robles Godoy | 1 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | 4.4089 |
| P4 | Rahul Rawail | Tinnu Anand | Armando Robles Godoy | Leopoldo Torre Nilsson | 4 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | 0.1749 |

ISR=0.50; literal PFR=2/3 (66.7%); strict PFR=2/3 (66.7%); strict conditional PFR=2/3 (66.7%).


Adjacent changes:

- P1→P2: Tinnu Anand → Armando Robles Godoy; new first=Armando Robles Godoy; literal=True; strict=True.
- P2→P3: Armando Robles Godoy → Leopoldo Torre Nilsson; new first=Leopoldo Torre Nilsson; literal=True; strict=True.
- P3→P4: Leopoldo Torre Nilsson → Leopoldo Torre Nilsson; new first=Rahul Rawail; literal=False; strict=False.

## dev-04 / HARD

Gold: Leopoldo Torre Nilsson. **POSITION_1_LOCKED** — Selection tracks position 1 in at least three orders while switching identities.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Tinnu Anand | Armando Robles Godoy | Leopoldo Torre Nilsson | Rahul Rawail | 3 | Tinnu Anand | Tinnu Anand | -2.5664 |
| P2 | Armando Robles Godoy | Leopoldo Torre Nilsson | Rahul Rawail | Tinnu Anand | 2 | Armando Robles Godoy | Armando Robles Godoy | -1.2772 |
| P3 | Leopoldo Torre Nilsson | Rahul Rawail | Tinnu Anand | Armando Robles Godoy | 1 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | 3.9031 |
| P4 | Rahul Rawail | Tinnu Anand | Armando Robles Godoy | Leopoldo Torre Nilsson | 4 | Rahul Rawail | Rahul Rawail | -2.2818 |

ISR=0.25; literal PFR=3/3 (100.0%); strict PFR=3/3 (100.0%); strict conditional PFR=3/3 (100.0%).

- P2: free format failure; raw F: Armando Robles Godoy<br><br>Wait. Let's reevaluate.<br><br>We are to find the **credited director** of Film T34217.<br><br>We start at Film T34217 and follow only **credited-director** links until we reach a record that names a candidate.<br><br>Graph-link records:<br><br>- Film T34217 has credited-director link R87885.<br>- R87885 has credited-director

Adjacent changes:

- P1→P2: Tinnu Anand → Armando Robles Godoy; new first=Armando Robles Godoy; literal=True; strict=True.
- P2→P3: Armando Robles Godoy → Leopoldo Torre Nilsson; new first=Leopoldo Torre Nilsson; literal=True; strict=True.
- P3→P4: Leopoldo Torre Nilsson → Rahul Rawail; new first=Rahul Rawail; literal=True; strict=True.

## dev-07 / EASY

Gold: Walter Hugo Khouri. **UNSTABLE_OTHER** — Not captured by the stable-identity/position-1/mixed rules; inspect the four responses.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | León Klimovsky | Walter Hugo Khouri | Marcello Fondato | James Goldstone | 2 | León Klimovsky | León Klimovsky | -0.9188 |
| P2 | Walter Hugo Khouri | Marcello Fondato | James Goldstone | León Klimovsky | 1 | Walter Hugo Khouri | Walter Hugo Khouri | 5.8063 |
| P3 | Marcello Fondato | James Goldstone | León Klimovsky | Walter Hugo Khouri | 4 | Walter Hugo Khouri | Walter Hugo Khouri | 1.6313 |
| P4 | James Goldstone | León Klimovsky | Walter Hugo Khouri | Marcello Fondato | 3 | Walter Hugo Khouri | Walter Hugo Khouri | 4.0000 |

ISR=0.75; literal PFR=1/3 (33.3%); strict PFR=1/3 (33.3%); strict conditional PFR=1/2 (50.0%).


Adjacent changes:

- P1→P2: León Klimovsky → Walter Hugo Khouri; new first=Walter Hugo Khouri; literal=True; strict=True.
- P2→P3: Walter Hugo Khouri → Walter Hugo Khouri; new first=Marcello Fondato; literal=False; strict=False.
- P3→P4: Walter Hugo Khouri → Walter Hugo Khouri; new first=James Goldstone; literal=False; strict=False.

## dev-07 / MID

Gold: Walter Hugo Khouri. **UNSTABLE_OTHER** — Not captured by the stable-identity/position-1/mixed rules; inspect the four responses.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | León Klimovsky | Walter Hugo Khouri | Marcello Fondato | James Goldstone | 2 | León Klimovsky | León Klimovsky | -0.4188 |
| P2 | Walter Hugo Khouri | Marcello Fondato | James Goldstone | León Klimovsky | 1 | Walter Hugo Khouri | Walter Hugo Khouri | 4.3219 |
| P3 | Marcello Fondato | James Goldstone | León Klimovsky | Walter Hugo Khouri | 4 | Walter Hugo Khouri | Walter Hugo Khouri | 0.1125 |
| P4 | James Goldstone | León Klimovsky | Walter Hugo Khouri | Marcello Fondato | 3 | Walter Hugo Khouri | Walter Hugo Khouri | 2.1356 |

ISR=0.75; literal PFR=1/3 (33.3%); strict PFR=1/3 (33.3%); strict conditional PFR=1/2 (50.0%).


Adjacent changes:

- P1→P2: León Klimovsky → Walter Hugo Khouri; new first=Walter Hugo Khouri; literal=True; strict=True.
- P2→P3: Walter Hugo Khouri → Walter Hugo Khouri; new first=Marcello Fondato; literal=False; strict=False.
- P3→P4: Walter Hugo Khouri → Walter Hugo Khouri; new first=James Goldstone; literal=False; strict=False.

## dev-07 / HARD

Gold: Walter Hugo Khouri. **POSITION_1_LOCKED** — Selection tracks position 1 in at least three orders while switching identities.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | León Klimovsky | Walter Hugo Khouri | Marcello Fondato | James Goldstone | 2 | León Klimovsky | León Klimovsky | -2.8063 |
| P2 | Walter Hugo Khouri | Marcello Fondato | James Goldstone | León Klimovsky | 1 | Walter Hugo Khouri | Walter Hugo Khouri | 4.5219 |
| P3 | Marcello Fondato | James Goldstone | León Klimovsky | Walter Hugo Khouri | 4 | Marcello Fondato | Marcello Fondato | -1.4313 |
| P4 | James Goldstone | León Klimovsky | Walter Hugo Khouri | Marcello Fondato | 3 | Walter Hugo Khouri | Walter Hugo Khouri | 1.5533 |

ISR=0.50; literal PFR=2/3 (66.7%); strict PFR=2/3 (66.7%); strict conditional PFR=2/3 (66.7%).


Adjacent changes:

- P1→P2: León Klimovsky → Walter Hugo Khouri; new first=Walter Hugo Khouri; literal=True; strict=True.
- P2→P3: Walter Hugo Khouri → Marcello Fondato; new first=Marcello Fondato; literal=True; strict=True.
- P3→P4: Marcello Fondato → Walter Hugo Khouri; new first=James Goldstone; literal=False; strict=False.

## dev-05 / EASY

Gold: Helmut Käutner. **GOLD_STABLE** — Gold identity survives all four list positions.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Rolf Schübel | Feng Xiaoning | Helmut Käutner | Fridrikh Ermler | 3 | Helmut Käutner | Helmut Käutner | 3.0219 |
| P2 | Feng Xiaoning | Helmut Käutner | Fridrikh Ermler | Rolf Schübel | 2 | Helmut Käutner | Helmut Käutner | 3.0078 |
| P3 | Helmut Käutner | Fridrikh Ermler | Rolf Schübel | Feng Xiaoning | 1 | Helmut Käutner | Helmut Käutner | 2.1797 |
| P4 | Fridrikh Ermler | Rolf Schübel | Feng Xiaoning | Helmut Käutner | 4 | Helmut Käutner | Helmut Käutner | 2.5470 |

ISR=1.00; literal PFR=1/3 (33.3%); strict PFR=0/3 (0.0%); strict conditional PFR=0/1 (0.0%).


Adjacent changes:

- P1→P2: Helmut Käutner → Helmut Käutner; new first=Feng Xiaoning; literal=False; strict=False.
- P2→P3: Helmut Käutner → Helmut Käutner; new first=Helmut Käutner; literal=True; strict=False.
- P3→P4: Helmut Käutner → Helmut Käutner; new first=Fridrikh Ermler; literal=False; strict=False.

## dev-05 / MID

Gold: Helmut Käutner. **UNSTABLE_OTHER** — Not captured by the stable-identity/position-1/mixed rules; inspect the four responses.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Rolf Schübel | Feng Xiaoning | Helmut Käutner | Fridrikh Ermler | 3 | Rolf Schübel | Rolf Schübel | -0.0393 |
| P2 | Feng Xiaoning | Helmut Käutner | Fridrikh Ermler | Rolf Schübel | 2 | Helmut Käutner | Helmut Käutner | 0.1577 |
| P3 | Helmut Käutner | Fridrikh Ermler | Rolf Schübel | Feng Xiaoning | 1 | Helmut Käutner | Helmut Käutner | 1.9923 |
| P4 | Fridrikh Ermler | Rolf Schübel | Feng Xiaoning | Helmut Käutner | 4 | Helmut Käutner | Helmut Käutner | 0.1651 |

ISR=0.75; literal PFR=1/3 (33.3%); strict PFR=0/3 (0.0%); strict conditional PFR=0/2 (0.0%).


Adjacent changes:

- P1→P2: Rolf Schübel → Helmut Käutner; new first=Feng Xiaoning; literal=False; strict=False.
- P2→P3: Helmut Käutner → Helmut Käutner; new first=Helmut Käutner; literal=True; strict=False.
- P3→P4: Helmut Käutner → Helmut Käutner; new first=Fridrikh Ermler; literal=False; strict=False.

## dev-05 / HARD

Gold: Helmut Käutner. **POSITION_1_LOCKED** — Selection tracks position 1 in at least three orders while switching identities.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Rolf Schübel | Feng Xiaoning | Helmut Käutner | Fridrikh Ermler | 3 | Rolf Schübel | Rolf Schübel | -3.3776 |
| P2 | Feng Xiaoning | Helmut Käutner | Fridrikh Ermler | Rolf Schübel | 2 | Feng Xiaoning | Feng Xiaoning | -2.3776 |
| P3 | Helmut Käutner | Fridrikh Ermler | Rolf Schübel | Feng Xiaoning | 1 | Feng Xiaoning | Feng Xiaoning | -0.1120 |
| P4 | Fridrikh Ermler | Rolf Schübel | Feng Xiaoning | Helmut Käutner | 4 | Fridrikh Ermler | Fridrikh Ermler | -2.1530 |

ISR=0.50; literal PFR=2/3 (66.7%); strict PFR=1/3 (33.3%); strict conditional PFR=1/2 (50.0%).


Adjacent changes:

- P1→P2: Rolf Schübel → Feng Xiaoning; new first=Feng Xiaoning; literal=True; strict=True.
- P2→P3: Feng Xiaoning → Feng Xiaoning; new first=Helmut Käutner; literal=False; strict=False.
- P3→P4: Feng Xiaoning → Fridrikh Ermler; new first=Fridrikh Ermler; literal=True; strict=False.

## dev-01 / EASY

Gold: Walter Hugo Khouri. **GOLD_STABLE** — Gold identity survives all four list positions.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Walter Hugo Khouri | Marcello Fondato | James Goldstone | Vojtěch Jasný | 1 | Walter Hugo Khouri | Walter Hugo Khouri | 0.4828 |
| P2 | Marcello Fondato | James Goldstone | Vojtěch Jasný | Walter Hugo Khouri | 4 | Walter Hugo Khouri | Walter Hugo Khouri | 1.5742 |
| P3 | James Goldstone | Vojtěch Jasný | Walter Hugo Khouri | Marcello Fondato | 3 | Walter Hugo Khouri | Walter Hugo Khouri | 1.3789 |
| P4 | Vojtěch Jasný | Walter Hugo Khouri | Marcello Fondato | James Goldstone | 2 | Walter Hugo Khouri | Walter Hugo Khouri | 1.1844 |

ISR=1.00; literal PFR=0/3 (0.0%); strict PFR=0/3 (0.0%); strict conditional PFR=0/1 (0.0%).


Adjacent changes:

- P1→P2: Walter Hugo Khouri → Walter Hugo Khouri; new first=Marcello Fondato; literal=False; strict=False.
- P2→P3: Walter Hugo Khouri → Walter Hugo Khouri; new first=James Goldstone; literal=False; strict=False.
- P3→P4: Walter Hugo Khouri → Walter Hugo Khouri; new first=Vojtěch Jasný; literal=False; strict=False.

## dev-01 / MID

Gold: Walter Hugo Khouri. **POSITION_1_LOCKED** — Selection tracks position 1 in at least three orders while switching identities.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Walter Hugo Khouri | Marcello Fondato | James Goldstone | Vojtěch Jasný | 1 | Walter Hugo Khouri | Walter Hugo Khouri | 0.3472 |
| P2 | Marcello Fondato | James Goldstone | Vojtěch Jasný | Walter Hugo Khouri | 4 | Marcello Fondato | Marcello Fondato | -0.2500 |
| P3 | James Goldstone | Vojtěch Jasný | Walter Hugo Khouri | Marcello Fondato | 3 | James Goldstone | James Goldstone | -0.2339 |
| P4 | Vojtěch Jasný | Walter Hugo Khouri | Marcello Fondato | James Goldstone | 2 | Walter Hugo Khouri | Walter Hugo Khouri | 0.1374 |

ISR=0.50; literal PFR=2/3 (66.7%); strict PFR=2/3 (66.7%); strict conditional PFR=2/3 (66.7%).

- P2: free format failure; raw F: Marcello Fondato<br><br>Wait. Let's retrace carefully.<br><br>We are to find the credited director of Film T27036.<br><br>Given:<br><br>- Film T27036 has credited-director link R84293.<br>- R84293 has credited-director link R99750.<br>- R99750 has credited-director link R85881.<br>- R8588
- P3: free format failure; raw F: James Goldstone<br><br>Wait. Let's retrace carefully.<br><br>We are to find the credited director of Film T27036.<br><br>Given:<br><br>- Film T27036 has credited-director link R84293.<br>- R84293 has credited-director link R99750.<br>- R99750 has credited-director link R85881.<br>- Record R85881

Adjacent changes:

- P1→P2: Walter Hugo Khouri → Marcello Fondato; new first=Marcello Fondato; literal=True; strict=True.
- P2→P3: Marcello Fondato → James Goldstone; new first=James Goldstone; literal=True; strict=True.
- P3→P4: James Goldstone → Walter Hugo Khouri; new first=Vojtěch Jasný; literal=False; strict=False.

## dev-01 / HARD

Gold: Walter Hugo Khouri. **POSITION_1_LOCKED** — Selection tracks position 1 in at least three orders while switching identities.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Walter Hugo Khouri | Marcello Fondato | James Goldstone | Vojtěch Jasný | 1 | Walter Hugo Khouri | Walter Hugo Khouri | 0.0152 |
| P2 | Marcello Fondato | James Goldstone | Vojtěch Jasný | Walter Hugo Khouri | 4 | Marcello Fondato | Marcello Fondato | -3.3313 |
| P3 | James Goldstone | Vojtěch Jasný | Walter Hugo Khouri | Marcello Fondato | 3 | James Goldstone | James Goldstone | -3.3082 |
| P4 | Vojtěch Jasný | Walter Hugo Khouri | Marcello Fondato | James Goldstone | 2 | Vojtěch Jasný | Vojtěch Jasný | -3.2188 |

ISR=0.25; literal PFR=3/3 (100.0%); strict PFR=3/3 (100.0%); strict conditional PFR=3/3 (100.0%).

- P2: free format failure; raw F: Marcello Fondato<br><br>Explanation:  <br>We start at Film T27036 and follow only "credited-director" links until we reach a record that names a candidate.<br><br>- Film T27036 has credited-director link R84293.<br>- Record R84293 has credited-director link R99750.<br>- Record R99750 has credited-director link R4970

Adjacent changes:

- P1→P2: Walter Hugo Khouri → Marcello Fondato; new first=Marcello Fondato; literal=True; strict=True.
- P2→P3: Marcello Fondato → James Goldstone; new first=James Goldstone; literal=True; strict=True.
- P3→P4: James Goldstone → Vojtěch Jasný; new first=Vojtěch Jasný; literal=True; strict=True.

## dev-06 / EASY

Gold: Gu Changwei. **GOLD_STABLE** — Gold identity survives all four list positions.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Rolf Schübel | Rodrigo Grande | Anil Das | Gu Changwei | 4 | Gu Changwei | Gu Changwei | 3.2844 |
| P2 | Rodrigo Grande | Anil Das | Gu Changwei | Rolf Schübel | 3 | Gu Changwei | Gu Changwei | 3.8985 |
| P3 | Anil Das | Gu Changwei | Rolf Schübel | Rodrigo Grande | 2 | Gu Changwei | Gu Changwei | 3.7083 |
| P4 | Gu Changwei | Rolf Schübel | Rodrigo Grande | Anil Das | 1 | Gu Changwei | Gu Changwei | 4.3031 |

ISR=1.00; literal PFR=1/3 (33.3%); strict PFR=0/3 (0.0%); strict conditional PFR=N/A (no eligible comparisons).


Adjacent changes:

- P1→P2: Gu Changwei → Gu Changwei; new first=Rodrigo Grande; literal=False; strict=False.
- P2→P3: Gu Changwei → Gu Changwei; new first=Anil Das; literal=False; strict=False.
- P3→P4: Gu Changwei → Gu Changwei; new first=Gu Changwei; literal=True; strict=False.

## dev-06 / MID

Gold: Gu Changwei. **UNSTABLE_OTHER** — Not captured by the stable-identity/position-1/mixed rules; inspect the four responses.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Rolf Schübel | Rodrigo Grande | Anil Das | Gu Changwei | 4 | Gu Changwei | Gu Changwei | 2.7094 |
| P2 | Rodrigo Grande | Anil Das | Gu Changwei | Rolf Schübel | 3 | Gu Changwei | Gu Changwei | 1.8656 |
| P3 | Anil Das | Gu Changwei | Rolf Schübel | Rodrigo Grande | 2 | Anil Das | Anil Das | -2.7083 |
| P4 | Gu Changwei | Rolf Schübel | Rodrigo Grande | Anil Das | 1 | Gu Changwei | Gu Changwei | 3.1969 |

ISR=0.75; literal PFR=2/3 (66.7%); strict PFR=1/3 (33.3%); strict conditional PFR=1/1 (100.0%).


Adjacent changes:

- P1→P2: Gu Changwei → Gu Changwei; new first=Rodrigo Grande; literal=False; strict=False.
- P2→P3: Gu Changwei → Anil Das; new first=Anil Das; literal=True; strict=False.
- P3→P4: Anil Das → Gu Changwei; new first=Gu Changwei; literal=True; strict=True.

## dev-06 / HARD

Gold: Gu Changwei. **GOLD_STABLE** — Gold identity survives all four list positions.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Rolf Schübel | Rodrigo Grande | Anil Das | Gu Changwei | 4 | Gu Changwei | Gu Changwei | 2.9250 |
| P2 | Rodrigo Grande | Anil Das | Gu Changwei | Rolf Schübel | 3 | Gu Changwei | Gu Changwei | 4.5619 |
| P3 | Anil Das | Gu Changwei | Rolf Schübel | Rodrigo Grande | 2 | Gu Changwei | Gu Changwei | 1.3542 |
| P4 | Gu Changwei | Rolf Schübel | Rodrigo Grande | Anil Das | 1 | Gu Changwei | Gu Changwei | 5.6626 |

ISR=1.00; literal PFR=1/3 (33.3%); strict PFR=0/3 (0.0%); strict conditional PFR=N/A (no eligible comparisons).


Adjacent changes:

- P1→P2: Gu Changwei → Gu Changwei; new first=Rodrigo Grande; literal=False; strict=False.
- P2→P3: Gu Changwei → Gu Changwei; new first=Anil Das; literal=False; strict=False.
- P3→P4: Gu Changwei → Gu Changwei; new first=Gu Changwei; literal=True; strict=False.

## dev-08 / EASY

Gold: Yuen Woo-ping. **GOLD_STABLE** — Gold identity survives all four list positions.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Yuen Woo-ping | Tinnu Anand | Ildikó Enyedi | Rahul Rawail | 1 | Yuen Woo-ping | Yuen Woo-ping | 4.6496 |
| P2 | Tinnu Anand | Ildikó Enyedi | Rahul Rawail | Yuen Woo-ping | 4 | Yuen Woo-ping | Yuen Woo-ping | 3.4188 |
| P3 | Ildikó Enyedi | Rahul Rawail | Yuen Woo-ping | Tinnu Anand | 3 | Yuen Woo-ping | Yuen Woo-ping | 2.2946 |
| P4 | Rahul Rawail | Yuen Woo-ping | Tinnu Anand | Ildikó Enyedi | 2 | Yuen Woo-ping | Yuen Woo-ping | 3.8505 |

ISR=1.00; literal PFR=0/3 (0.0%); strict PFR=0/3 (0.0%); strict conditional PFR=0/1 (0.0%).


Adjacent changes:

- P1→P2: Yuen Woo-ping → Yuen Woo-ping; new first=Tinnu Anand; literal=False; strict=False.
- P2→P3: Yuen Woo-ping → Yuen Woo-ping; new first=Ildikó Enyedi; literal=False; strict=False.
- P3→P4: Yuen Woo-ping → Yuen Woo-ping; new first=Rahul Rawail; literal=False; strict=False.

## dev-08 / MID

Gold: Yuen Woo-ping. **GOLD_STABLE** — Gold identity survives all four list positions.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Yuen Woo-ping | Tinnu Anand | Ildikó Enyedi | Rahul Rawail | 1 | Yuen Woo-ping | Yuen Woo-ping | 3.8174 |
| P2 | Tinnu Anand | Ildikó Enyedi | Rahul Rawail | Yuen Woo-ping | 4 | Yuen Woo-ping | Yuen Woo-ping | 2.4562 |
| P3 | Ildikó Enyedi | Rahul Rawail | Yuen Woo-ping | Tinnu Anand | 3 | Yuen Woo-ping | Yuen Woo-ping | 1.6875 |
| P4 | Rahul Rawail | Yuen Woo-ping | Tinnu Anand | Ildikó Enyedi | 2 | Yuen Woo-ping | Yuen Woo-ping | 2.5907 |

ISR=1.00; literal PFR=0/3 (0.0%); strict PFR=0/3 (0.0%); strict conditional PFR=0/1 (0.0%).


Adjacent changes:

- P1→P2: Yuen Woo-ping → Yuen Woo-ping; new first=Tinnu Anand; literal=False; strict=False.
- P2→P3: Yuen Woo-ping → Yuen Woo-ping; new first=Ildikó Enyedi; literal=False; strict=False.
- P3→P4: Yuen Woo-ping → Yuen Woo-ping; new first=Rahul Rawail; literal=False; strict=False.

## dev-08 / HARD

Gold: Yuen Woo-ping. **GOLD_STABLE** — Gold identity survives all four list positions.

| Permutation | Pos1 | Pos2 | Pos3 | Pos4 | Gold pos | C choice | L top-1 | Gold margin |
|---|---|---|---|---|---:|---|---|---:|
| P1 | Yuen Woo-ping | Tinnu Anand | Ildikó Enyedi | Rahul Rawail | 1 | Yuen Woo-ping | Yuen Woo-ping | 3.9326 |
| P2 | Tinnu Anand | Ildikó Enyedi | Rahul Rawail | Yuen Woo-ping | 4 | Yuen Woo-ping | Yuen Woo-ping | 1.6312 |
| P3 | Ildikó Enyedi | Rahul Rawail | Yuen Woo-ping | Tinnu Anand | 3 | Yuen Woo-ping | Yuen Woo-ping | 0.9464 |
| P4 | Rahul Rawail | Yuen Woo-ping | Tinnu Anand | Ildikó Enyedi | 2 | Yuen Woo-ping | Yuen Woo-ping | 1.1750 |

ISR=1.00; literal PFR=0/3 (0.0%); strict PFR=0/3 (0.0%); strict conditional PFR=0/1 (0.0%).


Adjacent changes:

- P1→P2: Yuen Woo-ping → Yuen Woo-ping; new first=Tinnu Anand; literal=False; strict=False.
- P2→P3: Yuen Woo-ping → Yuen Woo-ping; new first=Ildikó Enyedi; literal=False; strict=False.
- P3→P4: Yuen Woo-ping → Yuen Woo-ping; new first=Rahul Rawail; literal=False; strict=False.
