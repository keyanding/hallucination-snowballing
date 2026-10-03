# v3.4.1 first-hop inspection

All outputs are verbatim; line breaks in tables are rendered as `<br>`. Margin means gold mean log probability minus the best wrong candidate mean, in nats/token. Exact prompts and token scores remain in the three JSONL files. Position rates are observational; this experiment does not swap orders to establish position sensitivity.

## dev-M1-01

Question: Who directed "El Hombre que Vino del Odio"?

Gold: León Klimovsky. Frozen gold position: 1.

Candidates and frozen future targets (not supplied to the model):

- León Klimovsky → place of death → Madrid
- Walter Hugo Khouri → place of death → São Paulo
- Marcello Fondato → place of death → San Felice Circeo
- James Goldstone → place of death → Shaftsbury, Vermont

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M1 | D0 | León Klimovsky | León Klimovsky | León Klimovsky | León Klimovsky | 6.2156 |
| M1 | D1 | León Klimovsky | León Klimovsky | León Klimovsky | León Klimovsky | 5.2813 |
| M1 | D2 | León Klimovsky | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | -0.8187 |
| M1 | D3 | León Klimovsky | León Klimovsky | León Klimovsky | León Klimovsky | 6.5344 |

- M1/D2: first constrained-choice flip.

### Exact D0–D3 evidence (same question and candidates)

D0
```text
Record R967 names James Goldstone.
Record R199 names Walter Hugo Khouri.
Record R489 names León Klimovsky.
Record R467 names Marcello Fondato.
Film "El Hombre que Vino del Odio" has credited-director link R489.
```

D1
```text
Record R967 names James Goldstone.
Record R199 names Walter Hugo Khouri.
Record R489 names León Klimovsky.
Record R467 names Marcello Fondato.
Film "El Hombre que Vino del Odio" has credited-director link R489.
Film "El Hombre que Vino del Odio" has comparison-title link "Red Sky at Morning (1971 film)".
Film "Red Sky at Morning (1971 film)" has credited-director link R967.
```

D2
```text
Record R967 names James Goldstone.
Record R199 names Walter Hugo Khouri.
Record R489 names León Klimovsky.
Record R467 names Marcello Fondato.
Film "El Hombre que Vino del Odio" has reference-director link R967.
Film "El Hombre que Vino del Odio" has credited-director link R489.
```

D3
```text
Film "El Hombre que Vino del Odio" has credited-director link R489.
Record R489 names León Klimovsky.
Record R199 names Walter Hugo Khouri.
Record R467 names Marcello Fondato.
Film "El Hombre que Vino del Odio" has reference-director link R967.
Record R967 names James Goldstone.
```

## dev-M1-02

Question: Who directed "Yodha (1991 film)"?

Gold: Rahul Rawail. Frozen gold position: 4.

Candidates and frozen future targets (not supplied to the model):

- Yuen Woo-ping → father → Yuen Siu-tien
- Ildikó Enyedi → father → György Enyedi
- Jan Svěrák → father → Zdeněk Svěrák
- Rahul Rawail → father → H. S. Rawail

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M1 | D0 | Rahul Rawail | Rahul Rawail | Rahul Rawail | Rahul Rawail | 3.6876 |
| M1 | D1 | Rahul Rawail | Rahul Rawail | Rahul Rawail | Rahul Rawail | 3.2969 |
| M1 | D2 | Rahul Rawail | Rahul Rawail | Rahul Rawail | Rahul Rawail | 3.4782 |
| M1 | D3 | Rahul Rawail | Rahul Rawail | Rahul Rawail | Rahul Rawail | 4.0375 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M1-03

Question: Who directed "And the Spring Comes"?

Gold: Gu Changwei. Frozen gold position: 1.

Candidates and frozen future targets (not supplied to the model):

- Gu Changwei → place of birth → Xi'an
- Rodrigo Grande → place of birth → Rosario
- Anil Das → place of birth → Kottayam
- Rolf Schübel → place of birth → Stuttgart

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M1 | D0 | Gu Changwei | Gu Changwei | Gu Changwei | Gu Changwei | 5.6031 |
| M1 | D1 | Gu Changwei | Gu Changwei | Gu Changwei | Gu Changwei | 3.8125 |
| M1 | D2 | Gu Changwei | Gu Changwei | Gu Changwei | Gu Changwei | 3.4792 |
| M1 | D3 | Gu Changwei | Gu Changwei | Gu Changwei | Gu Changwei | 4.9527 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M1-04

Question: Who directed "Jail Yatra"?

Gold: Bhappi Sonie. Frozen gold position: 2.

Candidates and frozen future targets (not supplied to the model):

- Walter Hugo Khouri → place of death → São Paulo
- Bhappi Sonie → place of death → Mumbai
- León Klimovsky → place of death → Madrid
- James Goldstone → place of death → Shaftsbury, Vermont

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M1 | D0 | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | 5.1032 |
| M1 | D1 | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | 4.1500 |
| M1 | D2 | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | 5.2563 |
| M1 | D3 | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | 4.8156 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M1-05

Question: Who directed "At the End of the Tunnel"?

Gold: Rodrigo Grande. Frozen gold position: 2.

Candidates and frozen future targets (not supplied to the model):

- Gu Changwei → place of birth → Xi'an
- Rodrigo Grande → place of birth → Rosario
- Anil Das → place of birth → Kottayam
- Rolf Schübel → place of birth → Stuttgart

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M1 | D0 | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | 3.6945 |
| M1 | D1 | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | 3.5649 |
| M1 | D2 | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | 3.5508 |
| M1 | D3 | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | Rodrigo Grande | 3.4741 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M1-06

Question: Who directed "Chalta Purza"?

Gold: Bhappi Sonie. Frozen gold position: 3.

Candidates and frozen future targets (not supplied to the model):

- León Klimovsky → place of death → Madrid
- Walter Hugo Khouri → place of death → São Paulo
- Bhappi Sonie → place of death → Mumbai
- James Goldstone → place of death → Shaftsbury, Vermont

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M1 | D0 | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | 5.7219 |
| M1 | D1 | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | 5.3188 |
| M1 | D2 | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | 5.5907 |
| M1 | D3 | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | Bhappi Sonie | 5.5031 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M2-01

Question: Who directed "Red Sky at Morning (1971 film)"?

Gold: James Goldstone. Frozen gold position: 1.

Candidates and frozen future targets (not supplied to the model):

- James Goldstone → place of death → Shaftsbury, Vermont
- Marcello Fondato → place of death → San Felice Circeo
- León Klimovsky → place of death → Madrid
- Walter Hugo Khouri → place of death → São Paulo

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M2 | D0 | James Goldstone | James Goldstone | James Goldstone | James Goldstone | 5.7969 |
| M2 | D1 | James Goldstone | James Goldstone | James Goldstone | James Goldstone | 5.5281 |
| M2 | D2 | James Goldstone | James Goldstone | James Goldstone | James Goldstone | 5.2188 |
| M2 | D3 | James Goldstone | James Goldstone | James Goldstone | James Goldstone | 5.0281 |

No choice flips, format failures, or near-boundary flags in this case.

### Exact D0–D3 evidence (same question and candidates)

D0
```text
Record R505 names James Goldstone.
Record R246 names Walter Hugo Khouri.
Record R569 names León Klimovsky.
Record R758 names Marcello Fondato.
Film "Red Sky at Morning (1971 film)" has credited-director link R505.
```

D1
```text
Record R505 names James Goldstone.
Record R246 names Walter Hugo Khouri.
Record R569 names León Klimovsky.
Record R758 names Marcello Fondato.
Film "Red Sky at Morning (1971 film)" has credited-director link R505.
James Goldstone and Walter Hugo Khouri each has a documented film-directing credit dated within 1950–1999.
```

D2
```text
Record R505 names James Goldstone.
Record R246 names Walter Hugo Khouri.
Record R569 names León Klimovsky.
Record R758 names Marcello Fondato.
Film "Red Sky at Morning (1971 film)" has credited-director link R505.
James Goldstone and Walter Hugo Khouri each has a documented film-directing credit dated within 1950–1999.
James Goldstone and Walter Hugo Khouri each has a documented drama-film directing credit within 1950–1999.
```

D3
```text
Record R505 names James Goldstone.
Record R246 names Walter Hugo Khouri.
Record R569 names León Klimovsky.
Record R758 names Marcello Fondato.
Film "Red Sky at Morning (1971 film)" has credited-director link R505.
James Goldstone and Walter Hugo Khouri each has a documented film-directing credit dated within 1950–1999.
James Goldstone and Walter Hugo Khouri each has a documented drama-film directing credit within 1950–1999.
Walter Hugo Khouri has drama-film directing experience.
The profile for Walter Hugo Khouri includes directing work within 1950–1999.
The comparison profile names Walter Hugo Khouri.
```

## dev-M2-02

Question: Who directed "The Amorous Ones"?

Gold: Walter Hugo Khouri. Frozen gold position: 2.

Candidates and frozen future targets (not supplied to the model):

- Marcello Fondato → place of death → San Felice Circeo
- Walter Hugo Khouri → place of death → São Paulo
- James Goldstone → place of death → Shaftsbury, Vermont
- Vojtěch Jasný → place of death → Přerov

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M2 | D0 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 2.8555 |
| M2 | D1 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 2.8965 |
| M2 | D2 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 2.5781 |
| M2 | D3 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 2.3496 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M2-03

Question: Who directed "On Body and Soul"?

Gold: Ildikó Enyedi. Frozen gold position: 2.

Candidates and frozen future targets (not supplied to the model):

- Yuen Woo-ping → father → Yuen Siu-tien
- Ildikó Enyedi → father → György Enyedi
- Rahul Rawail → father → H. S. Rawail
- Jan Svěrák → father → Zdeněk Svěrák

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M2 | D0 | Ildikó Enyedi | Ildikó Enyedi | Ildikó Enyedi | Ildikó Enyedi | 5.1500 |
| M2 | D1 | Ildikó Enyedi | Ildikó Enyedi | Ildikó Enyedi | Ildikó Enyedi | 5.0594 |
| M2 | D2 | Ildikó Enyedi | Ildikó Enyedi | Ildikó Enyedi | Ildikó Enyedi | 4.6625 |
| M2 | D3 | Ildikó Enyedi | Ildikó Enyedi | Ildikó Enyedi | Ildikó Enyedi | 3.9844 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M2-04

Question: Who directed "Eros, o Deus do Amor"?

Gold: Walter Hugo Khouri. Frozen gold position: 1.

Candidates and frozen future targets (not supplied to the model):

- Walter Hugo Khouri → place of death → São Paulo
- Marcello Fondato → place of death → San Felice Circeo
- Bhappi Sonie → place of death → Mumbai
- James Goldstone → place of death → Shaftsbury, Vermont

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M2 | D0 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 4.8073 |
| M2 | D1 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 4.8047 |
| M2 | D2 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 4.7969 |
| M2 | D3 | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | Walter Hugo Khouri | 4.6510 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M2-05

Question: Who directed "True Legend"?

Gold: Yuen Woo-ping. Frozen gold position: 3.

Candidates and frozen future targets (not supplied to the model):

- Tinnu Anand → father → Inder Raj Anand
- Ildikó Enyedi → father → György Enyedi
- Yuen Woo-ping → father → Yuen Siu-tien
- Jan Svěrák → father → Zdeněk Svěrák

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M2 | D0 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 4.1362 |
| M2 | D1 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 4.2232 |
| M2 | D2 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 4.0558 |
| M2 | D3 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 4.0714 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M2-06

Question: Who directed "The Thousand Faces of Dunjia"?

Gold: Yuen Woo-ping. Frozen gold position: 4.

Candidates and frozen future targets (not supplied to the model):

- Ildikó Enyedi → father → György Enyedi
- Tinnu Anand → father → Inder Raj Anand
- Jan Svěrák → father → Zdeněk Svěrák
- Yuen Woo-ping → father → Yuen Siu-tien

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M2 | D0 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 4.1808 |
| M2 | D1 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 3.7656 |
| M2 | D2 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 3.4196 |
| M2 | D3 | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | Yuen Woo-ping | 3.5670 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M3-01

Question: Who directed "Peacock (2005 film)"?

Gold: Gu Changwei. Frozen gold position: 4.

Candidates and frozen future targets (not supplied to the model):

- Rolf Schübel → place of birth → Stuttgart
- Anil Das → place of birth → Kottayam
- Rodrigo Grande → place of birth → Rosario
- Gu Changwei → place of birth → Xi'an

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M3 | D0 | Gu Changwei | Gu Changwei | Gu Changwei | Gu Changwei | 5.4276 |
| M3 | D1 | Gu Changwei | Gu Changwei | Gu Changwei | Gu Changwei | 6.0120 |
| M3 | D2 | Gu Changwei | Gu Changwei | Gu Changwei | Gu Changwei | 4.3001 |
| M3 | D3 | Gu Changwei | Gu Changwei | Gu Changwei | Gu Changwei | 4.9946 |

No choice flips, format failures, or near-boundary flags in this case.

### Exact D0–D3 evidence (same question and candidates)

D0
```text
Record R471 names Anil Das.
Record R951 names Rodrigo Grande.
Record R214 names Rolf Schübel.
Film "Peacock (2005 film)" has credited-director link R926.
Record R926 names Gu Changwei.
```

D1
```text
Film "Peacock (2005 film)" has credited-director link R926.
Record R926 names Gu Changwei.
Record R471 names Anil Das.
Record R951 names Rodrigo Grande.
Record R214 names Rolf Schübel.
Catalog entries are written as separate statements.
The index groups records into sections.
```

D2
```text
Film "Peacock (2005 film)" has credited-director link R926.
Record R926 names Gu Changwei.
Record R471 names Anil Das.
Record R951 names Rodrigo Grande.
Record R214 names Rolf Schübel.
Catalog entries are written as separate statements.
The index groups records into sections.
Film "Peacock (2005 film)" has reference-director link R471.
```

D3
```text
Film "Peacock (2005 film)" has credited-director link R926.
Record R926 names Gu Changwei.
Record R951 names Rodrigo Grande.
Record R214 names Rolf Schübel.
Catalog entries are written as separate statements.
The index groups records into sections.
Film "Peacock (2005 film)" has reference-director link R471.
Record R471 names Anil Das.
```

## dev-M3-02

Question: Who directed "The Pipes"?

Gold: Vojtěch Jasný. Frozen gold position: 2.

Candidates and frozen future targets (not supplied to the model):

- Walter Hugo Khouri → place of death → São Paulo
- Vojtěch Jasný → place of death → Přerov
- Marcello Fondato → place of death → San Felice Circeo
- James Goldstone → place of death → Shaftsbury, Vermont

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M3 | D0 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 6.4219 |
| M3 | D1 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 6.3094 |
| M3 | D2 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 5.1469 |
| M3 | D3 | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | Vojtěch Jasný | 5.3720 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M3-03

Question: Who directed "Biwi-O-Biwi"?

Gold: Rahul Rawail. Frozen gold position: 3.

Candidates and frozen future targets (not supplied to the model):

- Tinnu Anand → father → Inder Raj Anand
- Yuen Woo-ping → father → Yuen Siu-tien
- Rahul Rawail → father → H. S. Rawail
- Ildikó Enyedi → father → György Enyedi

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M3 | D0 | Rahul Rawail | Rahul Rawail | Rahul Rawail | Rahul Rawail | 3.9889 |
| M3 | D1 | Rahul Rawail | Rahul Rawail | Rahul Rawail | Rahul Rawail | 3.9625 |
| M3 | D2 | Rahul Rawail | Rahul Rawail | Rahul Rawail | Rahul Rawail | 3.7433 |
| M3 | D3 | Rahul Rawail | Rahul Rawail | Rahul Rawail | Rahul Rawail | 3.8751 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M3-04

Question: Who directed "Love on the Cloud"?

Gold: Gu Changwei. Frozen gold position: 1.

Candidates and frozen future targets (not supplied to the model):

- Gu Changwei → place of birth → Xi'an
- Anil Das → place of birth → Kottayam
- Rolf Schübel → place of birth → Stuttgart
- Rodrigo Grande → place of birth → Rosario

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M3 | D0 | Gu Changwei | Gu Changwei | Gu Changwei | Gu Changwei | 4.9813 |
| M3 | D1 | Gu Changwei | Gu Changwei | Gu Changwei | Gu Changwei | 5.6997 |
| M3 | D2 | Gu Changwei | Gu Changwei | Gu Changwei | Gu Changwei | 3.9144 |
| M3 | D3 | Gu Changwei | Gu Changwei | Gu Changwei | Gu Changwei | 5.1206 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M3-05

Question: Who directed "A Trip to Chinatown (film)"?

Gold: Robert P. Kerr. Frozen gold position: 1.

Candidates and frozen future targets (not supplied to the model):

- Robert P. Kerr → place of death → Porterville
- Vojtěch Jasný → place of death → Přerov
- León Klimovsky → place of death → Madrid
- James Goldstone → place of death → Shaftsbury, Vermont

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M3 | D0 | Robert P. Kerr | Robert P. Kerr | Robert P. Kerr | Robert P. Kerr | 3.9043 |
| M3 | D1 | Robert P. Kerr | Robert P. Kerr | Robert P. Kerr | Robert P. Kerr | 4.2500 |
| M3 | D2 | Robert P. Kerr | Robert P. Kerr | Robert P. Kerr | Robert P. Kerr | 4.0664 |
| M3 | D3 | Robert P. Kerr | Robert P. Kerr | Robert P. Kerr | Robert P. Kerr | 4.1270 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M3-06

Question: Who directed "The Marihuana Story"?

Gold: León Klimovsky. Frozen gold position: 2.

Candidates and frozen future targets (not supplied to the model):

- Marcello Fondato → place of death → San Felice Circeo
- León Klimovsky → place of death → Madrid
- James Goldstone → place of death → Shaftsbury, Vermont
- Vojtěch Jasný → place of death → Přerov

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M3 | D0 | León Klimovsky | León Klimovsky | León Klimovsky | León Klimovsky | 3.1348 |
| M3 | D1 | León Klimovsky | León Klimovsky | León Klimovsky | León Klimovsky | 3.9023 |
| M3 | D2 | León Klimovsky | León Klimovsky | León Klimovsky | León Klimovsky | 3.3066 |
| M3 | D3 | León Klimovsky | León Klimovsky | León Klimovsky | León Klimovsky | 3.7617 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M4-01

Question: Who directed "The Protagonists (1968 film)"?

Gold: Marcello Fondato. Frozen gold position: 3.

Candidates and frozen future targets (not supplied to the model):

- Vojtěch Jasný → place of death → Přerov
- Walter Hugo Khouri → place of death → São Paulo
- Marcello Fondato → place of death → San Felice Circeo
- James Goldstone → place of death → Shaftsbury, Vermont

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M4 | D0 | Marcello Fondato | Marcello Fondato | Marcello Fondato | Marcello Fondato | 3.7871 |
| M4 | D1 | Marcello Fondato | Marcello Fondato | Marcello Fondato | Marcello Fondato | 3.5820 |
| M4 | D2 | Marcello Fondato | Marcello Fondato | Marcello Fondato | Marcello Fondato | 3.0605 |
| M4 | D3 | Marcello Fondato | Marcello Fondato | Marcello Fondato | Marcello Fondato | 2.3184 |

No choice flips, format failures, or near-boundary flags in this case.

### Exact D0–D3 evidence (same question and candidates)

D0
```text
Record R774 names Marcello Fondato.
Record R196 names Vojtěch Jasný.
Record R199 names Walter Hugo Khouri.
Record R541 names James Goldstone.
Film "The Protagonists (1968 film)" has credited-director link R774.
```

D1
```text
Record R774 names Marcello Fondato.
Record R196 names Vojtěch Jasný.
Record R199 names Walter Hugo Khouri.
Record R541 names James Goldstone.
Film "The Protagonists (1968 film)" has credited-director link Q462.
Record Q462 has credited-director link R774.
```

D2
```text
Record R774 names Marcello Fondato.
Record R196 names Vojtěch Jasný.
Record R199 names Walter Hugo Khouri.
Record R541 names James Goldstone.
Film "The Protagonists (1968 film)" has credited-director link Q462.
Record Q462 has credited-director link Q533.
Record Q533 has credited-director link R774.
```

D3
```text
Record R774 names Marcello Fondato.
Record R196 names Vojtěch Jasný.
Record R199 names Walter Hugo Khouri.
Record R541 names James Goldstone.
Film "The Protagonists (1968 film)" has credited-director link Q462.
Record Q462 has credited-director link Q533.
Record Q533 has credited-director link R774.
Record Q462 has comparison-director link R199.
```

## dev-M4-02

Question: Who directed "Lover's Grief over the Yellow River"?

Gold: Feng Xiaoning. Frozen gold position: 2.

Candidates and frozen future targets (not supplied to the model):

- Anil Das → place of birth → Kottayam
- Feng Xiaoning → place of birth → Xi'an
- Rolf Schübel → place of birth → Stuttgart
- Rodrigo Grande → place of birth → Rosario

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M4 | D0 | Feng Xiaoning | Feng Xiaoning | Feng Xiaoning | Feng Xiaoning | 5.2289 |
| M4 | D1 | Feng Xiaoning | Feng Xiaoning | Feng Xiaoning | Feng Xiaoning | 4.9931 |
| M4 | D2 | Feng Xiaoning | Feng Xiaoning | Feng Xiaoning | Feng Xiaoning | 4.5670 |
| M4 | D3 | Feng Xiaoning | Feng Xiaoning | Feng Xiaoning | Feng Xiaoning | 4.4474 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M4-03

Question: Who directed "Monday's Child (film)"?

Gold: Leopoldo Torre Nilsson. Frozen gold position: 1.

Candidates and frozen future targets (not supplied to the model):

- Leopoldo Torre Nilsson → father → Leopoldo Torres Ríos
- Rahul Rawail → father → H. S. Rawail
- Tinnu Anand → father → Inder Raj Anand
- Armando Robles Godoy → father → Daniel Alomía Robles

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M4 | D0 | Leopoldo Torre Nilsson | Tinnu Anand | Tinnu Anand | Tinnu Anand | -0.1982 |
| M4 | D1 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | 1.5813 |
| M4 | D2 | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | Leopoldo Torre Nilsson | 1.6938 |
| M4 | D3 | Leopoldo Torre Nilsson | Tinnu Anand | Tinnu Anand | Tinnu Anand | -0.5065 |

- M4/D0: near-zero/boundary margin (absolute value ≤0.5).
- M4/D1: first constrained-choice flip.

## dev-M4-04

Question: Who directed "Alice: A True Story"?

Gold: Anil Das. Frozen gold position: 4.

Candidates and frozen future targets (not supplied to the model):

- Rodrigo Grande → place of birth → Rosario
- Rolf Schübel → place of birth → Stuttgart
- Gu Changwei → place of birth → Xi'an
- Anil Das → place of birth → Kottayam

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M4 | D0 | Anil Das | Anil Das | Anil Das | Anil Das | 3.9792 |
| M4 | D1 | Anil Das | Anil Das | Anil Das | Anil Das | 3.8229 |
| M4 | D2 | Anil Das | Anil Das | Anil Das | Anil Das | 0.0677 |
| M4 | D3 | Anil Das | Rolf Schübel | Rolf Schübel | Rolf Schübel | -0.5553 |

- M4/D2: near-zero/boundary margin (absolute value ≤0.5).
- M4/D3: first constrained-choice flip.

## dev-M4-05

Question: Who directed "Walerjan Wrobel's Homesickness"?

Gold: Rolf Schübel. Frozen gold position: 1.

Candidates and frozen future targets (not supplied to the model):

- Rolf Schübel → place of birth → Stuttgart
- Anil Das → place of birth → Kottayam
- Helmut Käutner → place of birth → Düsseldorf
- Feng Xiaoning → place of birth → Xi'an

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M4 | D0 | Rolf Schübel | Rolf Schübel | Rolf Schübel | Rolf Schübel | 6.3411 |
| M4 | D1 | Rolf Schübel | Rolf Schübel | Rolf Schübel | Rolf Schübel | 5.9583 |
| M4 | D2 | Rolf Schübel | Rolf Schübel | Rolf Schübel | Rolf Schübel | 5.6003 |
| M4 | D3 | Rolf Schübel | Rolf Schübel | Rolf Schübel | Rolf Schübel | 5.3373 |

No choice flips, format failures, or near-boundary flags in this case.

## dev-M4-06

Question: Who directed "Jigsaw (1968 film)"?

Gold: James Goldstone. Frozen gold position: 2.

Candidates and frozen future targets (not supplied to the model):

- Walter Hugo Khouri → place of death → São Paulo
- James Goldstone → place of death → Shaftsbury, Vermont
- Marcello Fondato → place of death → San Felice Circeo
- Vojtěch Jasný → place of death → Přerov

| Mechanism | Difficulty | Gold | Free | Constrained | Likelihood top-1 | Margin |
|---|---|---|---|---|---|---|
| M4 | D0 | James Goldstone | James Goldstone | James Goldstone | James Goldstone | 3.8350 |
| M4 | D1 | James Goldstone | James Goldstone | James Goldstone | James Goldstone | 3.7363 |
| M4 | D2 | James Goldstone | James Goldstone | James Goldstone | James Goldstone | 3.1348 |
| M4 | D3 | James Goldstone | James Goldstone | James Goldstone | James Goldstone | 2.5820 |

No choice flips, format failures, or near-boundary flags in this case.

## heldout-shared-01

Question: Who directed "Legend of a Fighter"?

Gold: Yuen Woo-ping. Frozen gold position: 4.

Candidates and frozen future targets (not supplied to the model):

- Rahul Rawail → father → H. S. Rawail
- Tinnu Anand → father → Inder Raj Anand
- Ildikó Enyedi → father → György Enyedi
- Yuen Woo-ping → father → Yuen Siu-tien

Not evaluated: no development regime qualified for held-out confirmation.

## heldout-shared-02

Question: Who directed "My 20th Century"?

Gold: Ildikó Enyedi. Frozen gold position: 1.

Candidates and frozen future targets (not supplied to the model):

- Ildikó Enyedi → father → György Enyedi
- Jan Svěrák → father → Zdeněk Svěrák
- Rahul Rawail → father → H. S. Rawail
- Yuen Woo-ping → father → Yuen Siu-tien

Not evaluated: no development regime qualified for held-out confirmation.

## heldout-shared-03

Question: Who directed "Mirage (1972 film)"?

Gold: Armando Robles Godoy. Frozen gold position: 2.

Candidates and frozen future targets (not supplied to the model):

- Leopoldo Torre Nilsson → father → Leopoldo Torres Ríos
- Armando Robles Godoy → father → Daniel Alomía Robles
- Tinnu Anand → father → Inder Raj Anand
- Rahul Rawail → father → H. S. Rawail

Not evaluated: no development regime qualified for held-out confirmation.

## heldout-shared-04

Question: Who directed "Homage at Siesta Time"?

Gold: Leopoldo Torre Nilsson. Frozen gold position: 2.

Candidates and frozen future targets (not supplied to the model):

- Armando Robles Godoy → father → Daniel Alomía Robles
- Leopoldo Torre Nilsson → father → Leopoldo Torres Ríos
- Tinnu Anand → father → Inder Raj Anand
- Rahul Rawail → father → H. S. Rawail

Not evaluated: no development regime qualified for held-out confirmation.

## heldout-shared-05

Question: Who directed "The Ride (1994 film)"?

Gold: Jan Svěrák. Frozen gold position: 3.

Candidates and frozen future targets (not supplied to the model):

- Rahul Rawail → father → H. S. Rawail
- Ildikó Enyedi → father → György Enyedi
- Jan Svěrák → father → Zdeněk Svěrák
- Yuen Woo-ping → father → Yuen Siu-tien

Not evaluated: no development regime qualified for held-out confirmation.

## heldout-shared-06

Question: Who directed "The Palace of Angels"?

Gold: Walter Hugo Khouri. Frozen gold position: 1.

Candidates and frozen future targets (not supplied to the model):

- Walter Hugo Khouri → place of death → São Paulo
- James Goldstone → place of death → Shaftsbury, Vermont
- León Klimovsky → place of death → Madrid
- Marcello Fondato → place of death → San Felice Circeo

Not evaluated: no development regime qualified for held-out confirmation.

## heldout-shared-07

Question: Who directed "They Only Kill Their Masters"?

Gold: James Goldstone. Frozen gold position: 3.

Candidates and frozen future targets (not supplied to the model):

- Walter Hugo Khouri → place of death → São Paulo
- León Klimovsky → place of death → Madrid
- James Goldstone → place of death → Shaftsbury, Vermont
- Marcello Fondato → place of death → San Felice Circeo

Not evaluated: no development regime qualified for held-out confirmation.

## heldout-shared-08

Question: Who directed "The Female: Seventy Times Seven"?

Gold: Leopoldo Torre Nilsson. Frozen gold position: 3.

Candidates and frozen future targets (not supplied to the model):

- Rahul Rawail → father → H. S. Rawail
- Armando Robles Godoy → father → Daniel Alomía Robles
- Leopoldo Torre Nilsson → father → Leopoldo Torres Ríos
- Tinnu Anand → father → Inder Raj Anand

Not evaluated: no development regime qualified for held-out confirmation.

## heldout-shared-09

Question: Who directed "Redhead (1962 film)"?

Gold: Helmut Käutner. Frozen gold position: 4.

Candidates and frozen future targets (not supplied to the model):

- Rolf Schübel → place of birth → Stuttgart
- Feng Xiaoning → place of birth → Xi'an
- Fridrikh Ermler → place of birth → Rēzekne
- Helmut Käutner → place of birth → Düsseldorf

Not evaluated: no development regime qualified for held-out confirmation.

## heldout-shared-10

Question: Who directed "Summer Skin (film)"?

Gold: Leopoldo Torre Nilsson. Frozen gold position: 2.

Candidates and frozen future targets (not supplied to the model):

- Rahul Rawail → father → H. S. Rawail
- Leopoldo Torre Nilsson → father → Leopoldo Torres Ríos
- Tinnu Anand → father → Inder Raj Anand
- Armando Robles Godoy → father → Daniel Alomía Robles

Not evaluated: no development regime qualified for held-out confirmation.

## heldout-shared-11

Question: Who directed "Duniya Meri Jeb Mein"?

Gold: Tinnu Anand. Frozen gold position: 4.

Candidates and frozen future targets (not supplied to the model):

- Yuen Woo-ping → father → Yuen Siu-tien
- Armando Robles Godoy → father → Daniel Alomía Robles
- Rahul Rawail → father → H. S. Rawail
- Tinnu Anand → father → Inder Raj Anand

Not evaluated: no development regime qualified for held-out confirmation.

## heldout-shared-12

Question: Who directed "In the Line of Duty 4: Witness"?

Gold: Yuen Woo-ping. Frozen gold position: 1.

Candidates and frozen future targets (not supplied to the model):

- Yuen Woo-ping → father → Yuen Siu-tien
- Rahul Rawail → father → H. S. Rawail
- Ildikó Enyedi → father → György Enyedi
- Tinnu Anand → father → Inder Raj Anand

Not evaluated: no development regime qualified for held-out confirmation.
