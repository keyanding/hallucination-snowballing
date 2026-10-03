# Factorial calibration inspection

Depth and branch count form a partial order. First events below refer to the frozen depth-major display order, not a single difficulty ladder. Margin is gold minus best wrong candidate mean log probability (nats/token). Raw F outputs are verbatim except HTML escaping; all exact prompts are in prompt_plan.json and channel logs.

## dev-01: Film T27036

Which candidate is the credited director of Film T27036?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Walter Hugo Khouri → place of death → São Paulo
- Marcello Fondato → place of death → San Felice Circeo
- James Goldstone → place of death → Shaftsbury, Vermont
- Vojtěch Jasný → place of death → Přerov

| Depth | Branches | Gold | C choice | L top-1 | Margin | Free raw output |
|---|---:|---|---|---|---:|---|
| 1 | 0 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 0.4828 | Walter Hugo Khouri |
| 1 | 1 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 0.6676 | Walter Hugo Khouri |
| 1 | 2 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 0.3553 | Walter Hugo Khouri |
| 2 | 0 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 0.4392 | Walter Hugo Khouri |
| 2 | 1 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 0.0412 | Walter Hugo Khouri |
| 2 | 2 | Walter Hugo Khouri | Vojtěch Jasný | Vojtěch Jasný | -0.1143 | Vojtěch Jasný |
| 3 | 0 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 0.3472 | Walter Hugo Khouri |
| 3 | 1 | Walter Hugo Khouri | Vojtěch Jasný | Vojtěch Jasný | -0.1627 | Vojtěch Jasný |
| 3 | 2 | Walter Hugo Khouri | Vojtěch Jasný | Vojtěch Jasný | -0.2979 | Vojtěch Jasný |
| 4 | 0 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 0.3147 | Walter Hugo Khouri |
| 4 | 1 | Walter Hugo Khouri | Vojtěch Jasný | Vojtěch Jasný | -0.1206 | Vojtěch Jasný |
| 4 | 2 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 0.0152 | Walter Hugo Khouri |

Classification: CASE_NON_MONOTONIC, CASE_BOUNDARY_CROSSING.

- First margin compression: D1B1 → D1B2.
- First near-boundary condition: D1B0.
- First choice flip: D1B2 → D2B2.
- D1B0 → D1B1: non-monotonic margin reversal.
- D1B2 → D2B2: depth-induced correct-to-wrong flip; margin sign boundary crossing.
- D2B1 → D2B2: branches-induced correct-to-wrong flip; margin sign boundary crossing.
- D2B1 → D3B1: depth-induced correct-to-wrong flip; margin sign boundary crossing.
- D3B0 → D3B1: branches-induced correct-to-wrong flip; margin sign boundary crossing.
- D3B1 → D4B1: non-monotonic margin reversal.
- D4B0 → D4B1: branches-induced correct-to-wrong flip; margin sign boundary crossing.
- D3B2 → D4B2: recovery after flip; non-monotonic margin reversal.
- D4B1 → D4B2: recovery after flip; non-monotonic margin reversal.

## dev-02: Film T99426

Which candidate is the credited director of Film T99426?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Marcello Fondato → place of death → San Felice Circeo
- James Goldstone → place of death → Shaftsbury, Vermont
- Walter Hugo Khouri → place of death → São Paulo
- Vojtěch Jasný → place of death → Přerov

| Depth | Branches | Gold | C choice | L top-1 | Margin | Free raw output |
|---|---:|---|---|---|---:|---|
| 1 | 0 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 3.0250 | Vojtěch Jasný |
| 1 | 1 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 2.7937 | Vojtěch Jasný |
| 1 | 2 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 1.8813 | Vojtěch Jasný |
| 2 | 0 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 2.1375 | Vojtěch Jasný |
| 2 | 1 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 1.6625 | Vojtěch Jasný |
| 2 | 2 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 0.9693 | Vojtěch Jasný |
| 3 | 0 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 2.1563 | Vojtěch Jasný |
| 3 | 1 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 1.6188 | Vojtěch Jasný |
| 3 | 2 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 1.0753 | Vojtěch Jasný |
| 4 | 0 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 2.2875 | Vojtěch Jasný |
| 4 | 1 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 1.1253 | Vojtěch Jasný |
| 4 | 2 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 0.3562 | Vojtěch Jasný |

Classification: CASE_ALWAYS_EASY.

- First margin compression: D1B0 → D1B1.
- First near-boundary condition: D4B2.
- First choice flip: none.
- D2B0 → D3B0: non-monotonic margin reversal.
- D2B2 → D3B2: non-monotonic margin reversal.
- D3B0 → D4B0: non-monotonic margin reversal.

## dev-03: Film T22820

Which candidate is the credited director of Film T22820?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Rolf Schübel → place of birth → Stuttgart
- Rodrigo Grande → place of birth → Rosario
- Gu Changwei → place of birth → Xi'an
- Anil Das → place of birth → Kottayam

| Depth | Branches | Gold | C choice | L top-1 | Margin | Free raw output |
|---|---:|---|---|---|---:|---|
| 1 | 0 | Rodrigo Grande | Rolf Schübel | Rolf Schübel | -4.0393 | Rolf Schübel |
| 1 | 1 | Rodrigo Grande | Rolf Schübel | Rolf Schübel | -2.2971 | Rolf Schübel |
| 1 | 2 | Rodrigo Grande | Rolf Schübel | Rolf Schübel | -2.0079 | Rolf Schübel |
| 2 | 0 | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | 1.8925 | Rodrigo Grande |
| 2 | 1 | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | 1.2558 | Rodrigo Grande |
| 2 | 2 | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | 1.5842 | Rodrigo Grande |
| 3 | 0 | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | 2.6269 | Rodrigo Grande |
| 3 | 1 | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | 2.2699 | Rodrigo Grande |
| 3 | 2 | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | 2.6984 | Rodrigo Grande |
| 4 | 0 | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | 2.5013 | Rodrigo Grande |
| 4 | 1 | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | 0.0003 | Rodrigo Grande |
| 4 | 2 | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | 0.4129 | Rodrigo Grande |

Classification: CASE_NON_MONOTONIC.

- First margin compression: D2B0 → D2B1.
- First near-boundary condition: D4B1.
- First choice flip: D1B0 → D2B0.
- D1B0 → D1B1: non-monotonic margin reversal.
- D1B1 → D1B2: non-monotonic margin reversal.
- D1B0 → D2B0: recovery after flip; non-monotonic margin reversal.
- D1B1 → D2B1: recovery after flip; non-monotonic margin reversal.
- D1B2 → D2B2: recovery after flip; non-monotonic margin reversal.
- D2B1 → D2B2: non-monotonic margin reversal.
- D2B0 → D3B0: non-monotonic margin reversal.
- D2B1 → D3B1: non-monotonic margin reversal.
- D2B2 → D3B2: non-monotonic margin reversal.
- D3B1 → D3B2: non-monotonic margin reversal.
- D4B1 → D4B2: non-monotonic margin reversal.

## dev-04: Film T34217

Which candidate is the credited director of Film T34217?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Tinnu Anand → father → Inder Raj Anand
- Armando Robles Godoy → father → Daniel Alomía Robles
- Leopoldo Torre Nilsson → father → Leopoldo Torres Ríos
- Rahul Rawail → father → H. S. Rawail

| Depth | Branches | Gold | C choice | L top-1 | Margin | Free raw output |
|---|---:|---|---|---|---:|---|
| 1 | 0 | Leopoldo Torre Nilsson | Tinnu Anand | Tinnu Anand | -0.2110 | Tinnu Anand |
| 1 | 1 | Leopoldo Torre Nilsson | Tinnu Anand | Tinnu Anand | -1.3398 | Tinnu Anand |
| 1 | 2 | Leopoldo Torre Nilsson | Tinnu Anand | Tinnu Anand | -1.5391 | Tinnu Anand |
| 2 | 0 | Leopoldo Torre Nilsson | Tinnu Anand | Tinnu Anand | -0.7772 | Tinnu Anand |
| 2 | 1 | Leopoldo Torre Nilsson | Tinnu Anand | Tinnu Anand | -2.0605 | Tinnu Anand |
| 2 | 2 | Leopoldo Torre Nilsson | Tinnu Anand | Tinnu Anand | -1.3672 | Tinnu Anand |
| 3 | 0 | Leopoldo Torre Nilsson | Tinnu Anand | Tinnu Anand | -0.4233 | Tinnu Anand |
| 3 | 1 | Leopoldo Torre Nilsson | Tinnu Anand | Tinnu Anand | -1.6758 | Tinnu Anand |
| 3 | 2 | Leopoldo Torre Nilsson | Tinnu Anand | Tinnu Anand | -2.2813 | Tinnu Anand |
| 4 | 0 | Leopoldo Torre Nilsson | Tinnu Anand | Tinnu Anand | -0.6166 | Tinnu Anand |
| 4 | 1 | Leopoldo Torre Nilsson | Tinnu Anand | Tinnu Anand | -1.4570 | Tinnu Anand |
| 4 | 2 | Leopoldo Torre Nilsson | Tinnu Anand | Tinnu Anand | -2.5664 | Tinnu Anand |

Classification: CASE_ALWAYS_WRONG.

- First margin compression: D1B0 → D1B1.
- First near-boundary condition: D1B0.
- First choice flip: none.
- D1B2 → D2B2: non-monotonic margin reversal.
- D2B1 → D2B2: non-monotonic margin reversal.
- D2B0 → D3B0: non-monotonic margin reversal.
- D2B1 → D3B1: non-monotonic margin reversal.
- D3B1 → D4B1: non-monotonic margin reversal.

## dev-05: Film T89245

Which candidate is the credited director of Film T89245?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Rolf Schübel → place of birth → Stuttgart
- Feng Xiaoning → place of birth → Xi'an
- Helmut Käutner → place of birth → Düsseldorf
- Fridrikh Ermler → place of birth → Rēzekne

| Depth | Branches | Gold | C choice | L top-1 | Margin | Free raw output |
|---|---:|---|---|---|---:|---|
| 1 | 0 | Helmut Käutner | Helmut Käutner | Helmut Käutner | 3.0219 | Helmut Käutner |
| 1 | 1 | Helmut Käutner | Helmut Käutner | Helmut Käutner | 1.2688 | Helmut Käutner |
| 1 | 2 | Helmut Käutner | Helmut Käutner | Helmut Käutner | 0.6513 | Helmut Käutner |
| 2 | 0 | Helmut Käutner | Helmut Käutner | Helmut Käutner | 1.2438 | Helmut Käutner |
| 2 | 1 | Helmut Käutner | Helmut Käutner | Helmut Käutner | 0.2404 | Helmut Käutner |
| 2 | 2 | Helmut Käutner | Rolf Schübel | Rolf Schübel | -1.9375 | Rolf Schübel |
| 3 | 0 | Helmut Käutner | Rolf Schübel | Rolf Schübel | -0.0393 | Rolf Schübel |
| 3 | 1 | Helmut Käutner | Rolf Schübel | Rolf Schübel | -2.4948 | Rolf Schübel |
| 3 | 2 | Helmut Käutner | Rolf Schübel | Rolf Schübel | -3.3255 | Rolf Schübel |
| 4 | 0 | Helmut Käutner | Rolf Schübel | Rolf Schübel | -1.2965 | Rolf Schübel |
| 4 | 1 | Helmut Käutner | Rolf Schübel | Rolf Schübel | -2.5495 | Rolf Schübel |
| 4 | 2 | Helmut Käutner | Rolf Schübel | Rolf Schübel | -3.3776 | Rolf Schübel |

Classification: CASE_MONOTONIC, CASE_BOUNDARY_CROSSING.

- First margin compression: D1B0 → D1B1.
- First near-boundary condition: D1B2.
- First choice flip: D1B2 → D2B2.
- D1B2 → D2B2: depth-induced correct-to-wrong flip; margin sign boundary crossing.
- D2B1 → D2B2: branches-induced correct-to-wrong flip; margin sign boundary crossing.
- D2B0 → D3B0: depth-induced correct-to-wrong flip; margin sign boundary crossing.
- D2B1 → D3B1: depth-induced correct-to-wrong flip; margin sign boundary crossing.

## dev-06: Film T12112

Which candidate is the credited director of Film T12112?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Rolf Schübel → place of birth → Stuttgart
- Rodrigo Grande → place of birth → Rosario
- Anil Das → place of birth → Kottayam
- Gu Changwei → place of birth → Xi'an

| Depth | Branches | Gold | C choice | L top-1 | Margin | Free raw output |
|---|---:|---|---|---|---:|---|
| 1 | 0 | Gu Changwei | Gu Changwei | Gu Changwei | 3.2844 | Gu Changwei |
| 1 | 1 | Gu Changwei | Gu Changwei | Gu Changwei | 1.7001 | Gu Changwei |
| 1 | 2 | Gu Changwei | Gu Changwei | Gu Changwei | 4.0501 | Gu Changwei |
| 2 | 0 | Gu Changwei | Gu Changwei | Rolf Schübel | -0.0676 | Gu Changwei |
| 2 | 1 | Gu Changwei | Gu Changwei | Gu Changwei | 2.7039 | Gu Changwei |
| 2 | 2 | Gu Changwei | Gu Changwei | Gu Changwei | 2.2877 | Gu Changwei |
| 3 | 0 | Gu Changwei | Gu Changwei | Gu Changwei | 2.7094 | Gu Changwei |
| 3 | 1 | Gu Changwei | Gu Changwei | Gu Changwei | 2.1563 | Gu Changwei |
| 3 | 2 | Gu Changwei | Gu Changwei | Gu Changwei | 3.0626 | Gu Changwei |
| 4 | 0 | Gu Changwei | Gu Changwei | Gu Changwei | 2.2625 | Gu Changwei |
| 4 | 1 | Gu Changwei | Gu Changwei | Gu Changwei | 2.6595 | Gu Changwei |
| 4 | 2 | Gu Changwei | Gu Changwei | Gu Changwei | 2.9250 | Gu Changwei |

Classification: CASE_ALWAYS_EASY.

- First margin compression: D1B0 → D1B1.
- First near-boundary condition: D2B0.
- First choice flip: none.
- D1B1 → D1B2: non-monotonic margin reversal.
- D1B1 → D2B1: non-monotonic margin reversal.
- D2B0 → D2B1: non-monotonic margin reversal.
- D2B0 → D3B0: non-monotonic margin reversal.
- D2B2 → D3B2: non-monotonic margin reversal.
- D3B1 → D3B2: non-monotonic margin reversal.
- D3B1 → D4B1: non-monotonic margin reversal.
- D4B0 → D4B1: non-monotonic margin reversal.
- D4B1 → D4B2: non-monotonic margin reversal.

## dev-07: Film T66029

Which candidate is the credited director of Film T66029?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- León Klimovsky → place of death → Madrid
- Walter Hugo Khouri → place of death → São Paulo
- Marcello Fondato → place of death → San Felice Circeo
- James Goldstone → place of death → Shaftsbury, Vermont

| Depth | Branches | Gold | C choice | L top-1 | Margin | Free raw output |
|---|---:|---|---|---|---:|---|
| 1 | 0 | Walter Hugo Khouri | León Klimovsky | León Klimovsky | -0.9188 | León Klimovsky |
| 1 | 1 | Walter Hugo Khouri | León Klimovsky | León Klimovsky | -2.2438 | León Klimovsky |
| 1 | 2 | Walter Hugo Khouri | León Klimovsky | León Klimovsky | -1.7562 | León Klimovsky |
| 2 | 0 | Walter Hugo Khouri | León Klimovsky | León Klimovsky | -1.0438 | León Klimovsky |
| 2 | 1 | Walter Hugo Khouri | León Klimovsky | León Klimovsky | -2.2438 | León Klimovsky |
| 2 | 2 | Walter Hugo Khouri | León Klimovsky | León Klimovsky | -1.9937 | León Klimovsky |
| 3 | 0 | Walter Hugo Khouri | León Klimovsky | León Klimovsky | -0.4188 | León Klimovsky |
| 3 | 1 | Walter Hugo Khouri | León Klimovsky | León Klimovsky | -2.4562 | León Klimovsky |
| 3 | 2 | Walter Hugo Khouri | León Klimovsky | León Klimovsky | -2.3062 | León Klimovsky |
| 4 | 0 | Walter Hugo Khouri | León Klimovsky | León Klimovsky | -0.2063 | León Klimovsky |
| 4 | 1 | Walter Hugo Khouri | León Klimovsky | León Klimovsky | -2.9313 | León Klimovsky |
| 4 | 2 | Walter Hugo Khouri | León Klimovsky | León Klimovsky | -2.8063 | León Klimovsky |

Classification: CASE_ALWAYS_WRONG.

- First margin compression: D1B0 → D1B1.
- First near-boundary condition: D3B0.
- First choice flip: none.
- D1B1 → D1B2: non-monotonic margin reversal.
- D2B1 → D2B2: non-monotonic margin reversal.
- D2B0 → D3B0: non-monotonic margin reversal.
- D3B1 → D3B2: non-monotonic margin reversal.
- D3B0 → D4B0: non-monotonic margin reversal.
- D4B1 → D4B2: non-monotonic margin reversal.

## dev-08: Film T49524

Which candidate is the credited director of Film T49524?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Yuen Woo-ping → father → Yuen Siu-tien
- Tinnu Anand → father → Inder Raj Anand
- Ildikó Enyedi → father → György Enyedi
- Rahul Rawail → father → H. S. Rawail

| Depth | Branches | Gold | C choice | L top-1 | Margin | Free raw output |
|---|---:|---|---|---|---:|---|
| 1 | 0 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 4.6496 | Yuen Woo-ping |
| 1 | 1 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 4.5608 | Yuen Woo-ping |
| 1 | 2 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 4.5573 | Yuen Woo-ping |
| 2 | 0 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 3.7072 | Yuen Woo-ping |
| 2 | 1 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 4.1077 | Yuen Woo-ping |
| 2 | 2 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 4.3458 | Yuen Woo-ping |
| 3 | 0 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 3.8174 | Yuen Woo-ping |
| 3 | 1 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 3.8916 | Yuen Woo-ping |
| 3 | 2 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 3.9823 | Yuen Woo-ping |
| 4 | 0 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 3.7691 | Yuen Woo-ping |
| 4 | 1 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 3.8720 | Yuen Woo-ping |
| 4 | 2 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 3.9326 | Yuen Woo-ping |

Classification: CASE_ALWAYS_EASY.

- First margin compression: D1B0 → D1B1.
- First near-boundary condition: none.
- First choice flip: none.
- D2B0 → D2B1: non-monotonic margin reversal.
- D2B1 → D2B2: non-monotonic margin reversal.
- D2B0 → D3B0: non-monotonic margin reversal.
- D3B0 → D3B1: non-monotonic margin reversal.
- D3B1 → D3B2: non-monotonic margin reversal.
- D4B0 → D4B1: non-monotonic margin reversal.
- D4B1 → D4B2: non-monotonic margin reversal.

## heldout-01: Film T98300

Which candidate is the credited director of Film T98300?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Anil Das → place of birth → Kottayam
- Rodrigo Grande → place of birth → Rosario
- Gu Changwei → place of birth → Xi'an
- Rolf Schübel → place of birth → Stuttgart

Not evaluated: no development frontier qualified. No twelve-condition held-out grid was run.

## heldout-02: Film T95720

Which candidate is the credited director of Film T95720?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Armando Robles Godoy → father → Daniel Alomía Robles
- Rahul Rawail → father → H. S. Rawail
- Tinnu Anand → father → Inder Raj Anand
- Leopoldo Torre Nilsson → father → Leopoldo Torres Ríos

Not evaluated: no development frontier qualified. No twelve-condition held-out grid was run.

## heldout-03: Film T95252

Which candidate is the credited director of Film T95252?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- James Goldstone → place of death → Shaftsbury, Vermont
- Vojtěch Jasný → place of death → Přerov
- León Klimovsky → place of death → Madrid
- Robert P. Kerr → place of death → Porterville

Not evaluated: no development frontier qualified. No twelve-condition held-out grid was run.

## heldout-04: Film T86022

Which candidate is the credited director of Film T86022?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Marcello Fondato → place of death → San Felice Circeo
- Walter Hugo Khouri → place of death → São Paulo
- James Goldstone → place of death → Shaftsbury, Vermont
- Bhappi Sonie → place of death → Mumbai

Not evaluated: no development frontier qualified. No twelve-condition held-out grid was run.

## heldout-05: Film T67908

Which candidate is the credited director of Film T67908?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Walter Hugo Khouri → place of death → São Paulo
- Vojtěch Jasný → place of death → Přerov
- Marcello Fondato → place of death → San Felice Circeo
- James Goldstone → place of death → Shaftsbury, Vermont

Not evaluated: no development frontier qualified. No twelve-condition held-out grid was run.

## heldout-06: Film T26659

Which candidate is the credited director of Film T26659?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Rahul Rawail → father → H. S. Rawail
- Ildikó Enyedi → father → György Enyedi
- Yuen Woo-ping → father → Yuen Siu-tien
- Jan Svěrák → father → Zdeněk Svěrák

Not evaluated: no development frontier qualified. No twelve-condition held-out grid was run.

## heldout-07: Film T12244

Which candidate is the credited director of Film T12244?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Rahul Rawail → father → H. S. Rawail
- Jan Svěrák → father → Zdeněk Svěrák
- Ildikó Enyedi → father → György Enyedi
- Yuen Woo-ping → father → Yuen Siu-tien

Not evaluated: no development frontier qualified. No twelve-condition held-out grid was run.

## heldout-08: Film T43431

Which candidate is the credited director of Film T43431?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Armando Robles Godoy → father → Daniel Alomía Robles
- Rahul Rawail → father → H. S. Rawail
- Tinnu Anand → father → Inder Raj Anand
- Leopoldo Torre Nilsson → father → Leopoldo Torres Ríos

Not evaluated: no development frontier qualified. No twelve-condition held-out grid was run.

## heldout-09: Film T86852

Which candidate is the credited director of Film T86852?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Marcello Fondato → place of death → San Felice Circeo
- James Goldstone → place of death → Shaftsbury, Vermont
- Vojtěch Jasný → place of death → Přerov
- León Klimovsky → place of death → Madrid

Not evaluated: no development frontier qualified. No twelve-condition held-out grid was run.

## heldout-10: Film T24647

Which candidate is the credited director of Film T24647?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Jan Svěrák → father → Zdeněk Svěrák
- Yuen Woo-ping → father → Yuen Siu-tien
- Tinnu Anand → father → Inder Raj Anand
- Ildikó Enyedi → father → György Enyedi

Not evaluated: no development frontier qualified. No twelve-condition held-out grid was run.

## heldout-11: Film T59129

Which candidate is the credited director of Film T59129?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Walter Hugo Khouri → place of death → São Paulo
- James Goldstone → place of death → Shaftsbury, Vermont
- León Klimovsky → place of death → Madrid
- Marcello Fondato → place of death → San Felice Circeo

Not evaluated: no development frontier qualified. No twelve-condition held-out grid was run.

## heldout-12: Film T86034

Which candidate is the credited director of Film T86034?

Candidates and frozen downstream mappings (targets are not supplied in prompts):

- Rolf Schübel → place of birth → Stuttgart
- Anil Das → place of birth → Kottayam
- Helmut Käutner → place of birth → Düsseldorf
- Feng Xiaoning → place of birth → Xi'an

Not evaluated: no development frontier qualified. No twelve-condition held-out grid was run.
