# Experiment v2 smoke inspection

## Reviewed decision: STOP

The three model shards were SHA-256 verified against official Hugging Face metadata. The native BF16 probe answered the trivial question but automatically offloaded layers to CPU and left only about 306 MiB free VRAM. NF4 with BF16 compute passed a real CUDA kernel check and the same trivial generation, with the entire model on GPU. The actual smoke run peaked at about 3.29 GiB reserved VRAM; no runtime error or truncation occurred. Model revision: `cdbee75f17c01a7cc42f958dc650907174af0554`.

| Eligibility check | Passed / considered |
|---|---:|
| Baseline chain | 0 / 5 |
| Oracle downstream | 0 / 5 |
| Donor downstream | 0 / 5 |
| All three gates | 0 / 5 |
| Injected trajectories executed | 0 |

All 15 probe outputs fit the line parser, but formatting did not establish semantic success. Evidence-based inspection confirms that none of the five baselines returned the annotated first entity. The composer query returned **Kerala** as a composer; other baselines named different people. The performer response included relation arrows rather than only an entity and named a different performer.

Oracle failures are heterogeneous. **Chennai** conflicts with the annotated Lakshadweep death location; **Stockholm** conflicts with Helsingfors/Helsinki; the father query repeats Leopoldo Torre Nilsson instead of returning his father. **Germany** for Düsseldorf and **Iceland** for Reykjavík are broader, geographically compatible responses, not automatically false facts. They still fail the required city-level target. This exposes residual answer-granularity ambiguity in the phrase "place of birth" as well as factual-knowledge and instruction-execution limitations.

Donor probes returned two Unknown answers, Sweden/Germany instead of the expected cities, and Rock Island, Illinois rather than the annotated St. Louis, Missouri. None establishes the required `r2(B')=C'` capability. These are capability-screen results; they are not NEW_HALLUCINATION classifications of injected trajectories.

**No propagation intervention was executed. All propagation/recovery/new-hallucination/reject rates are null, not zero.** The v2 gate is failed, and no larger experiment is authorized. This result does not show that propagation is absent. It does not isolate whether NF4, base-model knowledge, prompt semantics, or dataset obscurity contributes most; no native-vs-NF4 capability comparison was performed, and the trivial load test does not validate factual accuracy.

For a later reviewed revision, explicitly request the evidence's location granularity, use more familiar or self-contained relational tasks, and/or test a stronger instruction model. Do not quietly resample more candidates until a desired effect appears. The fixed five were not replaced after seeing outputs. The initial preparation-only candidate list and the reasons for refining it before generation are preserved in `candidate_review.md`.

Codex performed this evidence-based inspection; human review is still required. V1 artifacts remain unchanged.

Candidates: 5; passing all gates: 0; injected: 0.

Greedy controlled-state experiment; no SHARS/HalluSE. Stop for human review. Gate labels use complete entity matching, not substring overlap.

## 25bc868a0bdd11eba7f7acde48001122

Where did the composer of film Edavazhiyile Poocha Minda Poocha die?

```text
A = Edavazhiyile Poocha Minda Poocha
r1 = composer
B = M. B. Sreenivasan
r2 = place of death
C = Lakshadweep
B' = Isaac Schwartz
C' = Siversky
```

### baseline

Input: A = Edavazhiyile Poocha Minda Poocha; no intermediate entity is supplied.

Subquestion 1 (A → B): Apply relation "composer" to "Edavazhiyile Poocha Minda Poocha".

Subquestion 2 (generated Step 1 → Step 2): Apply relation "place of death" to the entity returned in Step 1.

Both subquestions are in ONE model call, not two separate calls. The final answer must repeat Step 2.

Observed Step 1 output used by the requested composition: Kerala

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Question: Where did the composer of film Edavazhiyile Poocha Minda Poocha die?

Solve this using exactly the two specified relations.

Step 1 task:
Apply relation "composer" to "Edavazhiyile Poocha Minda Poocha".
Return the resulting entity only.

Step 2 task:
Apply relation "place of death" to the entity returned in Step 1.
Return the resulting entity/value only.

Final answer:
Return the Step 2 result only.

Output exactly:
Step 1: ...
Step 2: ...
Final answer: ...
```

**Model response**

```text
Step 1: Kerala  
Step 2: Kochi  
Final answer: Kochi
```

FAIL

### oracle

Supplied intermediate (Step 1): M. B. Sreenivasan

Step 1 task shown as context: Apply relation "composer" to "Edavazhiyile Poocha Minda Poocha"; its result is supplied, not requested again.

Subquestion (B → C): Apply relation "place of death" to "M. B. Sreenivasan".

The final answer must repeat Step 2.

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Question: Where did the composer of film Edavazhiyile Poocha Minda Poocha die?

Solve this using exactly the two specified relations.

The result of Step 1 is supplied below.

Step 1 task:
Apply relation "composer" to "Edavazhiyile Poocha Minda Poocha".

Step 1: M. B. Sreenivasan

Step 2 task:
Apply relation "place of death" to the entity supplied in Step 1.
Use the supplied Step 1 entity as the input to Step 2. Return the resulting entity/value only.

Final answer: Return the Step 2 result only.

Output exactly:
Step 2: ...
Final answer: ...
```

**Model response**

```text
Step 2: Chennai  
Final answer: Chennai
```

FAIL

### donor_probe

Input entity for donor probe (B'): Isaac Schwartz

Subquestion (B′ → C′): Apply relation "place of death" to "Isaac Schwartz".

This is an independent one-relation call. B′ is explicitly present in the prompt; no Step 1 result is prefilled.

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Apply relation "place of death" to "Isaac Schwartz". Return the resulting entity/value only.
Output exactly:
Answer: ...
```

**Model response**

```text
Answer: Unknown
```

FAIL

### injected

NOT RUN — pre-intervention gates not all passed.

### Supporting evidence

```json
[
  {
    "title": "Edavazhiyile Poocha Minda Poocha",
    "sentence_id": 2,
    "text": "The film has musical score by M. B. Sreenivasan."
  },
  {
    "title": "M. B. Sreenivasan",
    "sentence_id": 15,
    "text": "M. B. Sreenivasan died suddenly of a heart attack while conducting a choir in the Lakshadweep islands on 9 March 1988."
  }
]
```

### Donor evidence

```json
[
  {
    "title": "The Straw Hat",
    "sentence_id": 2,
    "text": "The film's music was composed by Isaac Schwartz."
  },
  {
    "title": "Isaac Schwartz",
    "sentence_id": 18,
    "text": "Schwartz died in Siversky, near Saint Petersburg, Russian Federation, on 27 December 2009, aged 86."
  }
]
```

## 0ca2e9f80bda11eba7f7acde48001122

Where was the director of film The Last Bridge born?

```text
A = The Last Bridge
r1 = director
B = Helmut Käutner
r2 = place of birth
C = Düsseldorf
B' = Gustaf Molander
C' = Helsingfors
```

### baseline

Input: A = The Last Bridge; no intermediate entity is supplied.

Subquestion 1 (A → B): Apply relation "director" to "The Last Bridge".

Subquestion 2 (generated Step 1 → Step 2): Apply relation "place of birth" to the entity returned in Step 1.

Both subquestions are in ONE model call, not two separate calls. The final answer must repeat Step 2.

Observed Step 1 output used by the requested composition: James Marsh

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Question: Where was the director of film The Last Bridge born?

Solve this using exactly the two specified relations.

Step 1 task:
Apply relation "director" to "The Last Bridge".
Return the resulting entity only.

Step 2 task:
Apply relation "place of birth" to the entity returned in Step 1.
Return the resulting entity/value only.

Final answer:
Return the Step 2 result only.

Output exactly:
Step 1: ...
Step 2: ...
Final answer: ...
```

**Model response**

```text
Step 1: James Marsh  
Step 2: London, England  
Final answer: London, England
```

FAIL

### oracle

Supplied intermediate (Step 1): Helmut Käutner

Step 1 task shown as context: Apply relation "director" to "The Last Bridge"; its result is supplied, not requested again.

Subquestion (B → C): Apply relation "place of birth" to "Helmut Käutner".

The final answer must repeat Step 2.

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Question: Where was the director of film The Last Bridge born?

Solve this using exactly the two specified relations.

The result of Step 1 is supplied below.

Step 1 task:
Apply relation "director" to "The Last Bridge".

Step 1: Helmut Käutner

Step 2 task:
Apply relation "place of birth" to the entity supplied in Step 1.
Use the supplied Step 1 entity as the input to Step 2. Return the resulting entity/value only.

Final answer: Return the Step 2 result only.

Output exactly:
Step 2: ...
Final answer: ...
```

**Model response**

```text
Step 2: Germany  
Final answer: Germany
```

FAIL

### donor_probe

Input entity for donor probe (B'): Gustaf Molander

Subquestion (B′ → C′): Apply relation "place of birth" to "Gustaf Molander".

This is an independent one-relation call. B′ is explicitly present in the prompt; no Step 1 result is prefilled.

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Apply relation "place of birth" to "Gustaf Molander". Return the resulting entity/value only.
Output exactly:
Answer: ...
```

**Model response**

```text
Answer: Sweden
```

FAIL

### injected

NOT RUN — pre-intervention gates not all passed.

### Supporting evidence

```json
[
  {
    "title": "The Last Bridge",
    "sentence_id": 0,
    "text": "The Last Bridge  is a 1954 Austrian war drama film directed by Helmut Käutner."
  },
  {
    "title": "Helmut Käutner",
    "sentence_id": 0,
    "text": "Helmut Käutner (born 25 March 1908 in Düsseldorf, Germany; died 20 April 1980 in Castellina in Chianti, Italy) was a German film director active mainly in the 1940s and 1950s."
  }
]
```

### Donor evidence

```json
[
  {
    "title": "Parisiennes (film)",
    "sentence_id": 0,
    "text": "Parisiennes or The Doctor's Women  is a 1928 German-Swedish silent film directed by Gustaf Molander and starring Margit Manstad, Ruth Weyher and Fred Louis Lerch."
  },
  {
    "title": "Gustaf Molander",
    "sentence_id": 4,
    "text": "Gustaf Molander was born in Helsingfors (now Helsinki) in the Grand Duchy of Finland (in the Russian Empire), where his father was working at the Swedish Theatre."
  }
]
```

## f1a04d600bdb11eba7f7acde48001122

What is the place of birth of the director of film Dollar (1938 Film)?

```text
A = Dollar
r1 = director
B = Gustaf Molander
r2 = place of birth
C = Helsingfors
B' = Helmut Käutner
C' = Düsseldorf
```

### baseline

Input: A = Dollar; no intermediate entity is supplied.

Subquestion 1 (A → B): Apply relation "director" to "Dollar".

Subquestion 2 (generated Step 1 → Step 2): Apply relation "place of birth" to the entity returned in Step 1.

Both subquestions are in ONE model call, not two separate calls. The final answer must repeat Step 2.

Observed Step 1 output used by the requested composition: John Ford

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Question: What is the place of birth of the director of film Dollar (1938 Film)?

Solve this using exactly the two specified relations.

Step 1 task:
Apply relation "director" to "Dollar".
Return the resulting entity only.

Step 2 task:
Apply relation "place of birth" to the entity returned in Step 1.
Return the resulting entity/value only.

Final answer:
Return the Step 2 result only.

Output exactly:
Step 1: ...
Step 2: ...
Final answer: ...
```

**Model response**

```text
Step 1: John Ford  
Step 2: Wisconsin  
Final answer: Wisconsin
```

FAIL

### oracle

Supplied intermediate (Step 1): Gustaf Molander

Step 1 task shown as context: Apply relation "director" to "Dollar"; its result is supplied, not requested again.

Subquestion (B → C): Apply relation "place of birth" to "Gustaf Molander".

The final answer must repeat Step 2.

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Question: What is the place of birth of the director of film Dollar (1938 Film)?

Solve this using exactly the two specified relations.

The result of Step 1 is supplied below.

Step 1 task:
Apply relation "director" to "Dollar".

Step 1: Gustaf Molander

Step 2 task:
Apply relation "place of birth" to the entity supplied in Step 1.
Use the supplied Step 1 entity as the input to Step 2. Return the resulting entity/value only.

Final answer: Return the Step 2 result only.

Output exactly:
Step 2: ...
Final answer: ...
```

**Model response**

```text
Step 2: Stockholm, Sweden  
Final answer: Stockholm, Sweden
```

FAIL

### donor_probe

Input entity for donor probe (B'): Helmut Käutner

Subquestion (B′ → C′): Apply relation "place of birth" to "Helmut Käutner".

This is an independent one-relation call. B′ is explicitly present in the prompt; no Step 1 result is prefilled.

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Apply relation "place of birth" to "Helmut Käutner". Return the resulting entity/value only.
Output exactly:
Answer: ...
```

**Model response**

```text
Answer: Germany
```

FAIL

### injected

NOT RUN — pre-intervention gates not all passed.

### Supporting evidence

```json
[
  {
    "title": "Dollar (1938 film)",
    "sentence_id": 0,
    "text": "Dollar is a 1938 Swedish comedy film directed by Gustaf Molander and starring Ingrid Bergman, Georg Rydeberg and Tutta Rolf."
  },
  {
    "title": "Gustaf Molander",
    "sentence_id": 4,
    "text": "Gustaf Molander was born in Helsingfors (now Helsinki) in the Grand Duchy of Finland (in the Russian Empire), where his father was working at the Swedish Theatre."
  }
]
```

### Donor evidence

```json
[
  {
    "title": "The Last Bridge",
    "sentence_id": 0,
    "text": "The Last Bridge  is a 1954 Austrian war drama film directed by Helmut Käutner."
  },
  {
    "title": "Helmut Käutner",
    "sentence_id": 0,
    "text": "Helmut Käutner (born 25 March 1908 in Düsseldorf, Germany; died 20 April 1980 in Castellina in Chianti, Italy) was a German film director active mainly in the 1940s and 1950s."
  }
]
```

## e61479860bda11eba7f7acde48001122

What is the place of birth of the performer of song Pluto (Song)?

```text
A = Pluto
r1 = performer
B = Björk
r2 = place of birth
C = Reykjavík
B' = Chuck Berry
C' = St. Louis, Missouri
```

### baseline

Input: A = Pluto; no intermediate entity is supplied.

Subquestion 1 (A → B): Apply relation "performer" to "Pluto".

Subquestion 2 (generated Step 1 → Step 2): Apply relation "place of birth" to the entity returned in Step 1.

Both subquestions are in ONE model call, not two separate calls. The final answer must repeat Step 2.

Observed Step 1 output used by the requested composition: Pluto (song) → performer → Bruno Mars

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Question: What is the place of birth of the performer of song Pluto (Song)?

Solve this using exactly the two specified relations.

Step 1 task:
Apply relation "performer" to "Pluto".
Return the resulting entity only.

Step 2 task:
Apply relation "place of birth" to the entity returned in Step 1.
Return the resulting entity/value only.

Final answer:
Return the Step 2 result only.

Output exactly:
Step 1: ...
Step 2: ...
Final answer: ...
```

**Model response**

```text
Step 1: Pluto (song) → performer → Bruno Mars  
Step 2: Bruno Mars → place of birth → White Plains, New York  
Final answer: White Plains, New York
```

FAIL

### oracle

Supplied intermediate (Step 1): Björk

Step 1 task shown as context: Apply relation "performer" to "Pluto"; its result is supplied, not requested again.

Subquestion (B → C): Apply relation "place of birth" to "Björk".

The final answer must repeat Step 2.

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Question: What is the place of birth of the performer of song Pluto (Song)?

Solve this using exactly the two specified relations.

The result of Step 1 is supplied below.

Step 1 task:
Apply relation "performer" to "Pluto".

Step 1: Björk

Step 2 task:
Apply relation "place of birth" to the entity supplied in Step 1.
Use the supplied Step 1 entity as the input to Step 2. Return the resulting entity/value only.

Final answer: Return the Step 2 result only.

Output exactly:
Step 2: ...
Final answer: ...
```

**Model response**

```text
Step 2: Iceland  
Final answer: Iceland
```

FAIL

### donor_probe

Input entity for donor probe (B'): Chuck Berry

Subquestion (B′ → C′): Apply relation "place of birth" to "Chuck Berry".

This is an independent one-relation call. B′ is explicitly present in the prompt; no Step 1 result is prefilled.

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Apply relation "place of birth" to "Chuck Berry". Return the resulting entity/value only.
Output exactly:
Answer: ...
```

**Model response**

```text
Answer: Rock Island, Illinois
```

FAIL

### injected

NOT RUN — pre-intervention gates not all passed.

### Supporting evidence

```json
[
  {
    "title": "Pluto (song)",
    "sentence_id": 0,
    "text": "\"Pluto\" is a song by Icelandic musician Björk."
  },
  {
    "title": "Björk",
    "sentence_id": 2,
    "text": "Born and raised in Reykjavík, Björk began her music career at the age of 11 and first gained international recognition as the lead singer of the alternative rock band"
  }
]
```

### Donor evidence

```json
[
  {
    "title": "Wee Wee Hours",
    "sentence_id": 0,
    "text": "\"Wee Wee Hours\" is a song written and recorded by Chuck Berry in 1955."
  },
  {
    "title": "Chuck Berry",
    "sentence_id": 4,
    "text": "Born into a middle-class African-American family in St. Louis, Missouri, Berry had an interest in music from an early age and gave his first public performance at Sumner High School."
  }
]
```

## 5b1e1f240bdc11eba7f7acde48001122

Who is the father of the director of film La Caída?

```text
A = La caída
r1 = director
B = Leopoldo Torre Nilsson
r2 = father
C = Leopoldo Torres Ríos
B' = Armando Robles Godoy
C' = Daniel Alomía Robles
```

### baseline

Input: A = La caída; no intermediate entity is supplied.

Subquestion 1 (A → B): Apply relation "director" to "La caída".

Subquestion 2 (generated Step 1 → Step 2): Apply relation "father" to the entity returned in Step 1.

Both subquestions are in ONE model call, not two separate calls. The final answer must repeat Step 2.

Observed Step 1 output used by the requested composition: Alonso Cánovas

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Question: Who is the father of the director of film La Caída?

Solve this using exactly the two specified relations.

Step 1 task:
Apply relation "director" to "La caída".
Return the resulting entity only.

Step 2 task:
Apply relation "father" to the entity returned in Step 1.
Return the resulting entity/value only.

Final answer:
Return the Step 2 result only.

Output exactly:
Step 1: ...
Step 2: ...
Final answer: ...
```

**Model response**

```text
Step 1: Alonso Cánovas  
Step 2: José Cánovas  
Final answer: José Cánovas
```

FAIL

### oracle

Supplied intermediate (Step 1): Leopoldo Torre Nilsson

Step 1 task shown as context: Apply relation "director" to "La caída"; its result is supplied, not requested again.

Subquestion (B → C): Apply relation "father" to "Leopoldo Torre Nilsson".

The final answer must repeat Step 2.

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Question: Who is the father of the director of film La Caída?

Solve this using exactly the two specified relations.

The result of Step 1 is supplied below.

Step 1 task:
Apply relation "director" to "La caída".

Step 1: Leopoldo Torre Nilsson

Step 2 task:
Apply relation "father" to the entity supplied in Step 1.
Use the supplied Step 1 entity as the input to Step 2. Return the resulting entity/value only.

Final answer: Return the Step 2 result only.

Output exactly:
Step 2: ...
Final answer: ...
```

**Model response**

```text
Step 2: Leopoldo Torre Nilsson

Final answer: Leopoldo Torre Nilsson
```

FAIL

### donor_probe

Input entity for donor probe (B'): Armando Robles Godoy

Subquestion (B′ → C′): Apply relation "father" to "Armando Robles Godoy".

This is an independent one-relation call. B′ is explicitly present in the prompt; no Step 1 result is prefilled.

**Exact prompt sent to the model (from trajectories.jsonl)**

```text
Apply relation "father" to "Armando Robles Godoy". Return the resulting entity/value only.
Output exactly:
Answer: ...
```

**Model response**

```text
Answer: Unknown
```

FAIL

### injected

NOT RUN — pre-intervention gates not all passed.

### Supporting evidence

```json
[
  {
    "title": "La caída",
    "sentence_id": 0,
    "text": "La caída is a 1959 Argentine drama film directed by Leopoldo Torre Nilsson."
  },
  {
    "title": "Leopoldo Torre Nilsson",
    "sentence_id": 1,
    "text": "Born as Leopoldo Torres Nilsson (he later changed his paternal surname from Torres to Torre) was the son of Argentine pioneer film director Leopoldo Torres Ríos, with whom he collaborated between 1939 and 1949."
  }
]
```

### Donor evidence

```json
[
  {
    "title": "Mirage (1972 film)",
    "sentence_id": 0,
    "text": "Mirage  is a 1972 Peruvian drama film directed by Armando Robles Godoy."
  },
  {
    "title": "Armando Robles Godoy",
    "sentence_id": 1,
    "text": "He was son of the Peruvian composer Daniel Alomía Robles and Carmela Godoy."
  }
]
```
