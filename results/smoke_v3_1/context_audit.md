# v3.1 pre-inference context construction audit

Ten evidence-reviewed real cases; no model output used in selection. H2 checks apply to its added neutral sentence; controlled facts necessarily contain the two entities and targets. H3 alone adds the first-hop identity evidence. Every added sentence retains its exact source article and sentence index.

Reference order is counterbalanced five/five across cases and fixed across levels. One neutral sentence per case. H3 cumulatively retains H2. No additional order variants are run (160-call design).

## real-01

```json
{
  "A": "Lover's Grief over the Yellow River",
  "r1": "director",
  "B": "Feng Xiaoning",
  "relation": "place of birth",
  "C": "Xi'an",
  "B_prime": "Rolf Schübel",
  "C_prime": "Stuttgart"
}
```

Checks: {"H0_two_downstream_facts_only": true, "H1_task_frame_only": true, "H2_added_text_no_entity_or_target_leak": true, "H2_article_identity_matches": true, "H3_explicit_first_hop": true, "cumulative_context": true, "paired_context_and_question_identical": true}

### Source evidence and alias decisions

```json
{
  "source_id": "df66ea220bdc11eba7f7acde48001122",
  "donor_id": "78249bea0bda11eba7f7acde48001122",
  "first_hop_evidence": {
    "title": "Lover's Grief over the Yellow River",
    "sentence_id": 0,
    "text": "Lover's Grief over the Yellow River  is a 1999 Chinese film directed by Feng Xiaoning."
  },
  "downstream_evidence": {
    "title": "Feng Xiaoning",
    "sentence_id": 4,
    "text": "Feng was born in Xi'an to a family of teachers."
  },
  "donor_first_hop_evidence": {
    "title": "Walerjan Wrobel's Homesickness",
    "sentence_id": 0,
    "text": "Walerjan Wrobel's Homesickness  is a 1991 German drama film directed by Rolf Schübel."
  },
  "donor_downstream_evidence": {
    "title": "Rolf Schübel",
    "sentence_id": 0,
    "text": "Rolf Schübel (born 11 November 1942 in Stuttgart, Germany) is a German film director and screenwriter."
  },
  "neutral_evidence": {
    "title": "Lover's Grief over the Yellow River",
    "sentence_id": 1,
    "text": "It was China's official Best Foreign Language Film submission at the 72nd Academy Awards, but did not receive a nomination."
  },
  "aliases_C": [
    "Xi'an",
    "Xi'an, China",
    "Xi'an, Shaanxi"
  ],
  "aliases_C_prime": [
    "Stuttgart",
    "Stuttgart, Germany"
  ]
}
```

### H0

```text
Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.
```

### H1

```text
Original task:
What is the place of birth of the director of film Lover'S Grief Over The Yellow River?

Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.
```

### H2

```text
Original task:
What is the place of birth of the director of film Lover'S Grief Over The Yellow River?

Additional context:
It was China's official Best Foreign Language Film submission at the 72nd Academy Awards, but did not receive a nomination.

Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.
```

### H3

```text
Original task:
What is the place of birth of the director of film Lover'S Grief Over The Yellow River?

Additional context:
It was China's official Best Foreign Language Film submission at the 72nd Academy Awards, but did not receive a nomination.

Additional evidence:
Lover's Grief over the Yellow River  is a 1999 Chinese film directed by Feng Xiaoning.

Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.
```

## real-02

```json
{
  "A": "Große Freiheit Nr. 7",
  "r1": "director",
  "B": "Helmut Käutner",
  "relation": "place of birth",
  "C": "Düsseldorf",
  "B_prime": "Anil Das",
  "C_prime": "Kottayam"
}
```

Checks: {"H0_two_downstream_facts_only": true, "H1_task_frame_only": true, "H2_added_text_no_entity_or_target_leak": true, "H2_article_identity_matches": true, "H3_explicit_first_hop": true, "cumulative_context": true, "paired_context_and_question_identical": true}

### Source evidence and alias decisions

```json
{
  "source_id": "97d5e6f00bdb11eba7f7acde48001122",
  "donor_id": "35aaea880bdc11eba7f7acde48001122",
  "first_hop_evidence": {
    "title": "Große Freiheit Nr. 7",
    "sentence_id": 1,
    "text": "(Great Freedom No. 7) is a 1944 German musical drama film directed by Helmut Käutner."
  },
  "downstream_evidence": {
    "title": "Helmut Käutner",
    "sentence_id": 0,
    "text": "Helmut Käutner (born 25 March 1908 in Düsseldorf, Germany; died 20 April 1980 in Castellina in Chianti, Italy) was a German film director active mainly in the 1940s and 1950s."
  },
  "donor_first_hop_evidence": {
    "title": "Alice: A True Story",
    "sentence_id": 1,
    "text": "A True Story is a Malayalam psychological film scripted and Directed by Anil Das."
  },
  "donor_downstream_evidence": {
    "title": "Anil Das",
    "sentence_id": 1,
    "text": "Born in Kottayam and settled in Kollam."
  },
  "neutral_evidence": {
    "title": "Große Freiheit Nr. 7",
    "sentence_id": 3,
    "text": "The film is also known as Port of Freedom in the United Kingdom."
  },
  "aliases_C": [
    "Dusseldorf",
    "Dusseldorf, Germany",
    "Düsseldorf",
    "Düsseldorf, Germany"
  ],
  "aliases_C_prime": [
    "Kottayam"
  ]
}
```

### H0

```text
Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.
```

### H1

```text
Original task:
What is the place of birth of the director of film Große Freiheit Nr. 7?

Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.
```

### H2

```text
Original task:
What is the place of birth of the director of film Große Freiheit Nr. 7?

Additional context:
The film is also known as Port of Freedom in the United Kingdom.

Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.
```

### H3

```text
Original task:
What is the place of birth of the director of film Große Freiheit Nr. 7?

Additional context:
The film is also known as Port of Freedom in the United Kingdom.

Additional evidence:
(Great Freedom No. 7) is a 1944 German musical drama film directed by Helmut Käutner.

Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.
```

## real-03

```json
{
  "A": "Arabian Love",
  "r1": "director",
  "B": "Jerome Storm",
  "relation": "place of birth",
  "C": "Denver",
  "B_prime": "Gu Changwei",
  "C_prime": "Xi'an"
}
```

Checks: {"H0_two_downstream_facts_only": true, "H1_task_frame_only": true, "H2_added_text_no_entity_or_target_leak": true, "H2_article_identity_matches": true, "H3_explicit_first_hop": true, "cumulative_context": true, "paired_context_and_question_identical": true}

### Source evidence and alias decisions

```json
{
  "source_id": "c22a48e40bd911eba7f7acde48001122",
  "donor_id": "0bd60cfa0bdd11eba7f7acde48001122",
  "first_hop_evidence": {
    "title": "Arabian Love",
    "sentence_id": 0,
    "text": "Arabian Love is a 1922 American silent drama film directed by Jerome Storm."
  },
  "downstream_evidence": {
    "title": "Jerome Storm",
    "sentence_id": 2,
    "text": "He was born in Denver, Colorado, and died in Desert Hot Springs, California."
  },
  "donor_first_hop_evidence": {
    "title": "Peacock (2005 film)",
    "sentence_id": 0,
    "text": "Peacock  is a 2005 film directed by Gu Changwei, written by Li Qiang."
  },
  "donor_downstream_evidence": {
    "title": "Gu Changwei",
    "sentence_id": 1,
    "text": "Gu was born in Xi'an, Shaanxi in the People's Republic of China."
  },
  "neutral_evidence": {
    "title": "Arabian Love",
    "sentence_id": 1,
    "text": "It is not known whether the film currently survives."
  },
  "aliases_C": [
    "Denver",
    "Denver, Colorado"
  ],
  "aliases_C_prime": [
    "Xi'an",
    "Xi'an, China",
    "Xi'an, Shaanxi"
  ]
}
```

### H0

```text
Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.
```

### H1

```text
Original task:
What is the place of birth of the director of film Arabian Love?

Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.
```

### H2

```text
Original task:
What is the place of birth of the director of film Arabian Love?

Additional context:
It is not known whether the film currently survives.

Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.
```

### H3

```text
Original task:
What is the place of birth of the director of film Arabian Love?

Additional context:
It is not known whether the film currently survives.

Additional evidence:
Arabian Love is a 1922 American silent drama film directed by Jerome Storm.

Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.
```

## real-04

```json
{
  "A": "At the End of the Tunnel",
  "r1": "director",
  "B": "Rodrigo Grande",
  "relation": "place of birth",
  "C": "Rosario",
  "B_prime": "Fridrikh Ermler",
  "C_prime": "Rēzekne"
}
```

Checks: {"H0_two_downstream_facts_only": true, "H1_task_frame_only": true, "H2_added_text_no_entity_or_target_leak": true, "H2_article_identity_matches": true, "H3_explicit_first_hop": true, "cumulative_context": true, "paired_context_and_question_identical": true}

### Source evidence and alias decisions

```json
{
  "source_id": "c40d35580bda11eba7f7acde48001122",
  "donor_id": "751ba0980bd911eba7f7acde48001122",
  "first_hop_evidence": {
    "title": "At the End of the Tunnel",
    "sentence_id": 0,
    "text": "At the End of the Tunnel  is a 2016 Argentine crime thriller film directed by Rodrigo Grande."
  },
  "downstream_evidence": {
    "title": "Rodrigo Grande",
    "sentence_id": 0,
    "text": "Rodrigo Grande (born February 10, 1974 in Rosario, Santa Fe Province) is an Argentine film director and screenplay writer."
  },
  "donor_first_hop_evidence": {
    "title": "The House in the Snow-Drifts",
    "sentence_id": 0,
    "text": "The House in the Snow-Drifts  is a 1928 Soviet drama film directed by Fridrikh Ermler."
  },
  "donor_downstream_evidence": {
    "title": "Fridrikh Ermler",
    "sentence_id": 0,
    "text": "Fridrikh Markovich Ermler (born Vladimir Markovich Breslav; 13 May 1898 in Rēzekne – 12 July 1967 in Leningrad) was a Soviet film director, actor, and screenwriter."
  },
  "neutral_evidence": {
    "title": "At the End of the Tunnel",
    "sentence_id": 1,
    "text": "The film won best movie at the Seattle International Film Festival in 2017."
  },
  "aliases_C": [
    "Rosario",
    "Rosario, Santa Fe",
    "Rosario, Santa Fe Province"
  ],
  "aliases_C_prime": [
    "Rezekne",
    "Rēzekne"
  ]
}
```

### H0

```text
Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.
```

### H1

```text
Original task:
Where was the director of film At The End Of The Tunnel born?

Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.
```

### H2

```text
Original task:
Where was the director of film At The End Of The Tunnel born?

Additional context:
The film won best movie at the Seattle International Film Festival in 2017.

Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.
```

### H3

```text
Original task:
Where was the director of film At The End Of The Tunnel born?

Additional context:
The film won best movie at the Seattle International Film Festival in 2017.

Additional evidence:
At the End of the Tunnel  is a 2016 Argentine crime thriller film directed by Rodrigo Grande.

Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.
```

## real-05

```json
{
  "A": "In the Line of Duty 4: Witness",
  "r1": "director",
  "B": "Yuen Woo-ping",
  "relation": "father",
  "C": "Yuen Siu-tien",
  "B_prime": "Rahul Rawail",
  "C_prime": "H. S. Rawail"
}
```

Checks: {"H0_two_downstream_facts_only": true, "H1_task_frame_only": true, "H2_added_text_no_entity_or_target_leak": true, "H2_article_identity_matches": true, "H3_explicit_first_hop": true, "cumulative_context": true, "paired_context_and_question_identical": true}

### Source evidence and alias decisions

```json
{
  "source_id": "4772896e0bdd11eba7f7acde48001122",
  "donor_id": "ba289b440bdb11eba7f7acde48001122",
  "first_hop_evidence": {
    "title": "In the Line of Duty 4: Witness",
    "sentence_id": 1,
    "text": "Witness (aka In the Line of Duty) is a 1989 Hong Kong action film directed by Yuen Woo-ping, starring Donnie Yen, Michael Wong and Cynthia Khan."
  },
  "downstream_evidence": {
    "title": "Yuen Woo-ping",
    "sentence_id": 4,
    "text": "Yuen is also a son of Yuen Siu-tien, a renowned martial arts film actor."
  },
  "donor_first_hop_evidence": {
    "title": "Biwi-O-Biwi",
    "sentence_id": 1,
    "text": "Produced by Raj Kapoor and directed by Rahul Rawail."
  },
  "donor_downstream_evidence": {
    "title": "Rahul Rawail",
    "sentence_id": 3,
    "text": "He is son of film director H. S. Rawail and his son Bharat is an upcoming director."
  },
  "neutral_evidence": {
    "title": "In the Line of Duty 4: Witness",
    "sentence_id": 2,
    "text": "The film was released in the Hong Kong on 21 July 1989."
  },
  "aliases_C": [
    "Yuen Siu-tien"
  ],
  "aliases_C_prime": [
    "H S Rawail",
    "H. S. Rawail",
    "H.S. Rawail"
  ]
}
```

### H0

```text
Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.
```

### H1

```text
Original task:
Who is the father of the director of film In The Line Of Duty 4: Witness?

Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.
```

### H2

```text
Original task:
Who is the father of the director of film In The Line Of Duty 4: Witness?

Additional context:
The film was released in the Hong Kong on 21 July 1989.

Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.
```

### H3

```text
Original task:
Who is the father of the director of film In The Line Of Duty 4: Witness?

Additional context:
The film was released in the Hong Kong on 21 July 1989.

Additional evidence:
Witness (aka In the Line of Duty) is a 1989 Hong Kong action film directed by Yuen Woo-ping, starring Donnie Yen, Michael Wong and Cynthia Khan.

Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.
```

## real-06

```json
{
  "A": "My 20th Century",
  "r1": "director",
  "B": "Ildikó Enyedi",
  "relation": "father",
  "C": "György Enyedi",
  "B_prime": "Armando Robles Godoy",
  "C_prime": "Daniel Alomía Robles"
}
```

Checks: {"H0_two_downstream_facts_only": true, "H1_task_frame_only": true, "H2_added_text_no_entity_or_target_leak": true, "H2_article_identity_matches": true, "H3_explicit_first_hop": true, "cumulative_context": true, "paired_context_and_question_identical": true}

### Source evidence and alias decisions

```json
{
  "source_id": "52376a780bdc11eba7f7acde48001122",
  "donor_id": "b26e04e80bdb11eba7f7acde48001122",
  "first_hop_evidence": {
    "title": "My 20th Century",
    "sentence_id": 0,
    "text": "My 20th Century  is a 1989 Hungarian comedy-drama film written and directed by Ildikó Enyedi."
  },
  "downstream_evidence": {
    "title": "Ildikó Enyedi",
    "sentence_id": 2,
    "text": "Her father, György Enyedi, was a geographer and economist who played a major role in the long- term development of regional science."
  },
  "donor_first_hop_evidence": {
    "title": "Mirage (1972 film)",
    "sentence_id": 0,
    "text": "Mirage  is a 1972 Peruvian drama film directed by Armando Robles Godoy."
  },
  "donor_downstream_evidence": {
    "title": "Armando Robles Godoy",
    "sentence_id": 1,
    "text": "He was son of the Peruvian composer Daniel Alomía Robles and Carmela Godoy."
  },
  "neutral_evidence": {
    "title": "My 20th Century",
    "sentence_id": 1,
    "text": "It premiered at the Toronto Festival of Festivals."
  },
  "aliases_C": [
    "Gyorgy Enyedi",
    "György Enyedi"
  ],
  "aliases_C_prime": [
    "Daniel Alomia Robles",
    "Daniel Alomía Robles"
  ]
}
```

### H0

```text
Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.
```

### H1

```text
Original task:
Who is the father of the director of film My 20Th Century?

Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.
```

### H2

```text
Original task:
Who is the father of the director of film My 20Th Century?

Additional context:
It premiered at the Toronto Festival of Festivals.

Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.
```

### H3

```text
Original task:
Who is the father of the director of film My 20Th Century?

Additional context:
It premiered at the Toronto Festival of Festivals.

Additional evidence:
My 20th Century  is a 1989 Hungarian comedy-drama film written and directed by Ildikó Enyedi.

Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.
```

## real-07

```json
{
  "A": "Duniya Meri Jeb Mein",
  "r1": "director",
  "B": "Tinnu Anand",
  "relation": "father",
  "C": "Inder Raj Anand",
  "B_prime": "Leopoldo Torre Nilsson",
  "C_prime": "Leopoldo Torres Ríos"
}
```

Checks: {"H0_two_downstream_facts_only": true, "H1_task_frame_only": true, "H2_added_text_no_entity_or_target_leak": true, "H2_article_identity_matches": true, "H3_explicit_first_hop": true, "cumulative_context": true, "paired_context_and_question_identical": true}

### Source evidence and alias decisions

```json
{
  "source_id": "f0faeb9a0bdb11eba7f7acde48001122",
  "donor_id": "5b1e1f240bdc11eba7f7acde48001122",
  "first_hop_evidence": {
    "title": "Duniya Meri Jeb Mein",
    "sentence_id": 0,
    "text": "Duniya Meri Jeb Mein is a 1979 Bollywood action film directed by Tinnu Anand."
  },
  "downstream_evidence": {
    "title": "Tinnu Anand",
    "sentence_id": 1,
    "text": "He is the son of veteran writer Inder Raj Anand, brother of producer Bittu Anand and uncle of director Siddharth Anand."
  },
  "donor_first_hop_evidence": {
    "title": "La caída",
    "sentence_id": 0,
    "text": "La caída is a 1959 Argentine drama film directed by Leopoldo Torre Nilsson."
  },
  "donor_downstream_evidence": {
    "title": "Leopoldo Torre Nilsson",
    "sentence_id": 1,
    "text": "Born as Leopoldo Torres Nilsson (he later changed his paternal surname from Torres to Torre) was the son of Argentine pioneer film director Leopoldo Torres Ríos, with whom he collaborated between 1939 and 1949."
  },
  "neutral_evidence": {
    "title": "Duniya Meri Jeb Mein",
    "sentence_id": 1,
    "text": "The film stars Shashi Kapoor and Rishi Kapoor."
  },
  "aliases_C": [
    "Inder Raj Anand"
  ],
  "aliases_C_prime": [
    "Leopoldo Torres Rios",
    "Leopoldo Torres Ríos"
  ]
}
```

### H0

```text
Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.
```

### H1

```text
Original task:
Who is the father of the director of film Duniya Meri Jeb Mein?

Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.
```

### H2

```text
Original task:
Who is the father of the director of film Duniya Meri Jeb Mein?

Additional context:
The film stars Shashi Kapoor and Rishi Kapoor.

Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.
```

### H3

```text
Original task:
Who is the father of the director of film Duniya Meri Jeb Mein?

Additional context:
The film stars Shashi Kapoor and Rishi Kapoor.

Additional evidence:
Duniya Meri Jeb Mein is a 1979 Bollywood action film directed by Tinnu Anand.

Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.
```

## real-08

```json
{
  "A": "The Pipes",
  "r1": "director",
  "B": "Vojtěch Jasný",
  "relation": "place of death",
  "C": "Přerov",
  "B_prime": "Robert P. Kerr",
  "C_prime": "Porterville"
}
```

Checks: {"H0_two_downstream_facts_only": true, "H1_task_frame_only": true, "H2_added_text_no_entity_or_target_leak": true, "H2_article_identity_matches": true, "H3_explicit_first_hop": true, "cumulative_context": true, "paired_context_and_question_identical": true}

### Source evidence and alias decisions

```json
{
  "source_id": "73def83e0bdd11eba7f7acde48001122",
  "donor_id": "8dfa2e9e0bda11eba7f7acde48001122",
  "first_hop_evidence": {
    "title": "The Pipes",
    "sentence_id": 0,
    "text": "The Pipes  is a 1966 Czechoslovak film directed by Vojtěch Jasný."
  },
  "downstream_evidence": {
    "title": "Vojtěch Jasný",
    "sentence_id": 8,
    "text": "He died in Přerov in November 2019, fifteen days shy of his 94th birthday."
  },
  "donor_first_hop_evidence": {
    "title": "A Trip to Chinatown (film)",
    "sentence_id": 2,
    "text": "The movie was scripted by Beatrice Van from Charles Hale Hoyt's hit Broadway musical of the same name and directed by Robert P. Kerr."
  },
  "donor_downstream_evidence": {
    "title": "Robert P. Kerr",
    "sentence_id": 2,
    "text": "He was born in Burlington, Colorado and died in Porterville, California from a heart attack."
  },
  "neutral_evidence": {
    "title": "The Pipes",
    "sentence_id": 1,
    "text": "It was entered into the 1966 Cannes Film Festival."
  },
  "aliases_C": [
    "Prerov",
    "Přerov"
  ],
  "aliases_C_prime": [
    "Porterville",
    "Porterville, California"
  ]
}
```

### H0

```text
Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.
```

### H1

```text
Original task:
Where was the place of death of the director of film The Pipes?

Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.
```

### H2

```text
Original task:
Where was the place of death of the director of film The Pipes?

Additional context:
It was entered into the 1966 Cannes Film Festival.

Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.
```

### H3

```text
Original task:
Where was the place of death of the director of film The Pipes?

Additional context:
It was entered into the 1966 Cannes Film Festival.

Additional evidence:
The Pipes  is a 1966 Czechoslovak film directed by Vojtěch Jasný.

Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.
```

## real-09

```json
{
  "A": "The Protagonists",
  "r1": "director",
  "B": "Marcello Fondato",
  "relation": "place of death",
  "C": "San Felice Circeo",
  "B_prime": "James Goldstone",
  "C_prime": "Shaftsbury, Vermont"
}
```

Checks: {"H0_two_downstream_facts_only": true, "H1_task_frame_only": true, "H2_added_text_no_entity_or_target_leak": true, "H2_article_identity_matches": true, "H3_explicit_first_hop": true, "cumulative_context": true, "paired_context_and_question_identical": true}

### Source evidence and alias decisions

```json
{
  "source_id": "e043b86e0bda11eba7f7acde48001122",
  "donor_id": "e1cfab340bda11eba7f7acde48001122",
  "first_hop_evidence": {
    "title": "The Protagonists (1968 film)",
    "sentence_id": 0,
    "text": "The Protagonists  is a 1968 Italian drama film directed by Marcello Fondato."
  },
  "downstream_evidence": {
    "title": "Marcello Fondato",
    "sentence_id": 4,
    "text": "He was born in Rome, Italy and died in San Felice Circeo of a cerebral hemorrhage aged 84."
  },
  "donor_first_hop_evidence": {
    "title": "Red Sky at Morning (1971 film)",
    "sentence_id": 1,
    "text": "Directed by James Goldstone, it stars Richard Thomas, Catherine Burns, and Desi Arnaz, Jr."
  },
  "donor_downstream_evidence": {
    "title": "James Goldstone",
    "sentence_id": 0,
    "text": "James Goldstone (born June 8, 1931 in Los Angeles, California; died November 5, 1999 in Shaftsbury, Vermont) was an American film and television director whose career spanned over thirty years."
  },
  "neutral_evidence": {
    "title": "The Protagonists (1968 film)",
    "sentence_id": 1,
    "text": "It was listed to compete at the 1968 Cannes Film Festival, but the festival was cancelled due to the events of May 1968 in France."
  },
  "aliases_C": [
    "San Felice Circeo"
  ],
  "aliases_C_prime": [
    "Shaftsbury",
    "Shaftsbury, Vermont"
  ]
}
```

### H0

```text
Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.
```

### H1

```text
Original task:
Where was the place of death of the director of film The Protagonists (1968 Film)?

Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.
```

### H2

```text
Original task:
Where was the place of death of the director of film The Protagonists (1968 Film)?

Additional context:
It was listed to compete at the 1968 Cannes Film Festival, but the festival was cancelled due to the events of May 1968 in France.

Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.
```

### H3

```text
Original task:
Where was the place of death of the director of film The Protagonists (1968 Film)?

Additional context:
It was listed to compete at the 1968 Cannes Film Festival, but the festival was cancelled due to the events of May 1968 in France.

Additional evidence:
The Protagonists  is a 1968 Italian drama film directed by Marcello Fondato.

Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.
```

## real-10

```json
{
  "A": "The Marihuana Story",
  "r1": "director",
  "B": "León Klimovsky",
  "relation": "place of death",
  "C": "Madrid",
  "B_prime": "Bhappi Sonie",
  "C_prime": "Mumbai"
}
```

Checks: {"H0_two_downstream_facts_only": true, "H1_task_frame_only": true, "H2_added_text_no_entity_or_target_leak": true, "H2_article_identity_matches": true, "H3_explicit_first_hop": true, "cumulative_context": true, "paired_context_and_question_identical": true}

### Source evidence and alias decisions

```json
{
  "source_id": "c5e7570c0bdd11eba7f7acde48001122",
  "donor_id": "b0a2e8ba0bd911eba7f7acde48001122",
  "first_hop_evidence": {
    "title": "The Marihuana Story",
    "sentence_id": 0,
    "text": "The Marihuana Story  is a 1950 Argentine film directed by León Klimovsky."
  },
  "downstream_evidence": {
    "title": "León Klimovsky",
    "sentence_id": 16,
    "text": "He died the following year in Madrid from a heart attack."
  },
  "donor_first_hop_evidence": {
    "title": "Chalta Purza",
    "sentence_id": 0,
    "text": "Chalta Purza  is a 1977 Bollywood action thriller film directed by Bhappi Sonie."
  },
  "donor_downstream_evidence": {
    "title": "Bhappi Sonie",
    "sentence_id": 1,
    "text": "He died on 5 September 2001, while undergoing a heart bypass surgery at Nanavati Hospital, in Mumbai, at the age of 73."
  },
  "neutral_evidence": {
    "title": "The Marihuana Story",
    "sentence_id": 1,
    "text": "It was entered into the 1951 Cannes Film Festival."
  },
  "aliases_C": [
    "Madrid"
  ],
  "aliases_C_prime": [
    "Mumbai"
  ]
}
```

### H0

```text
Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.
```

### H1

```text
Original task:
Where did the director of film The Marihuana Story die?

Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.
```

### H2

```text
Original task:
Where did the director of film The Marihuana Story die?

Additional context:
It was entered into the 1951 Cannes Film Festival.

Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.
```

### H3

```text
Original task:
Where did the director of film The Marihuana Story die?

Additional context:
It was entered into the 1951 Cannes Film Festival.

Additional evidence:
The Marihuana Story  is a 1950 Argentine film directed by León Klimovsky.

Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.
```