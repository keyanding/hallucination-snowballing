# v3.1 real-entity context ladder inspection

Smoke gate: PASS; calls: 160/160; stop for review. Codex inspection completed: all responses are one of the supplied targets; no aliases or labels were changed after generation. Nine cases meet the cross-H0–H2 interpretability rule; real-04 has the documented H2 gold-state failure. Human review remains pending.

[Context construction audit](context_audit.md) was saved before inference. [Diagnosis](diagnosis.md) describes the interpretation.

Labels on unrecognized values are provisional until evidence review. SFIR on B′ includes scientifically meaningful OVERRIDE_TO_GOLD; it is not an automatic gate failure. No particular H3 propagation rate is required.

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

| Context | CLA B | CLA B′ | state B | state B′ | Injected label |
|---|---|---|---|---|---|
| H0 | Xi'an | Stuttgart | Xi'an | Stuttgart | PROPAGATE |
| H1 | Xi'an | Stuttgart | Xi'an | Stuttgart | PROPAGATE |
| H2 | Xi'an | Stuttgart | Xi'an | Xi'an | OVERRIDE_TO_GOLD |
| H3 | Xi'an | Stuttgart | Xi'an | Xi'an | OVERRIDE_TO_GOLD |

**Highlights:** H2: PROPAGATE → OVERRIDE_TO_GOLD; H2 state_B_prime: direct-correct → state-wrong (OVERRIDE_TO_GOLD); H3 state_B_prime: direct-correct → state-wrong (OVERRIDE_TO_GOLD)

### H0 / direct_B

**Exact prompt**

```text
Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.

Question:
According to the information above, where was Feng Xiaoning born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / direct_B_prime

**Exact prompt**

```text
Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.

Question:
According to the information above, where was Rolf Schübel born?

Answer with only the requested name or location.
```

**Raw response**

```text
Stuttgart
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / state_B

**Exact prompt**

```text
Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.

Current Step 1 state:
Feng Xiaoning

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H0 / state_B_prime

**Exact prompt**

```text
Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.

Current Step 1 state:
Rolf Schübel

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Stuttgart
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / direct_B

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Lover'S Grief Over The Yellow River?

Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.

Question:
According to the information above, where was Feng Xiaoning born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / direct_B_prime

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Lover'S Grief Over The Yellow River?

Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.

Question:
According to the information above, where was Rolf Schübel born?

Answer with only the requested name or location.
```

**Raw response**

```text
Stuttgart
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / state_B

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Lover'S Grief Over The Yellow River?

Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.

Current Step 1 state:
Feng Xiaoning

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / state_B_prime

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Lover'S Grief Over The Yellow River?

Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.

Current Step 1 state:
Rolf Schübel

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Stuttgart
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / direct_B

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Lover'S Grief Over The Yellow River?

Additional context:
It was China's official Best Foreign Language Film submission at the 72nd Academy Awards, but did not receive a nomination.

Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.

Question:
According to the information above, where was Feng Xiaoning born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / direct_B_prime

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Lover'S Grief Over The Yellow River?

Additional context:
It was China's official Best Foreign Language Film submission at the 72nd Academy Awards, but did not receive a nomination.

Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.

Question:
According to the information above, where was Rolf Schübel born?

Answer with only the requested name or location.
```

**Raw response**

```text
Stuttgart
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / state_B

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Lover'S Grief Over The Yellow River?

Additional context:
It was China's official Best Foreign Language Film submission at the 72nd Academy Awards, but did not receive a nomination.

Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.

Current Step 1 state:
Feng Xiaoning

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / state_B_prime

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Lover'S Grief Over The Yellow River?

Additional context:
It was China's official Best Foreign Language Film submission at the 72nd Academy Awards, but did not receive a nomination.

Reference facts:
1. Feng Xiaoning was born in Xi'an.
2. Rolf Schübel was born in Stuttgart.

Current Step 1 state:
Rolf Schübel

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: OVERRIDE_TO_GOLD; direct lookup pass: True; state adherence pass: False; pending evidence review: False.

### H3 / direct_B

**Exact prompt**

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

Question:
According to the information above, where was Feng Xiaoning born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / direct_B_prime

**Exact prompt**

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

Question:
According to the information above, where was Rolf Schübel born?

Answer with only the requested name or location.
```

**Raw response**

```text
Stuttgart
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / state_B

**Exact prompt**

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

Current Step 1 state:
Feng Xiaoning

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / state_B_prime

**Exact prompt**

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

Current Step 1 state:
Rolf Schübel

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: OVERRIDE_TO_GOLD; direct lookup pass: True; state adherence pass: False; pending evidence review: False.

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

| Context | CLA B | CLA B′ | state B | state B′ | Injected label |
|---|---|---|---|---|---|
| H0 | Düsseldorf | Kottayam | Düsseldorf | Kottayam | PROPAGATE |
| H1 | Düsseldorf | Kottayam | Düsseldorf | Kottayam | PROPAGATE |
| H2 | Düsseldorf | Kottayam | Düsseldorf | Kottayam | PROPAGATE |
| H3 | Düsseldorf | Kottayam | Düsseldorf | Düsseldorf | OVERRIDE_TO_GOLD |

**Highlights:** H3: PROPAGATE → OVERRIDE_TO_GOLD; H3 state_B_prime: direct-correct → state-wrong (OVERRIDE_TO_GOLD)

### H0 / direct_B

**Exact prompt**

```text
Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.

Question:
According to the information above, where was Helmut Käutner born?

Answer with only the requested name or location.
```

**Raw response**

```text
Düsseldorf
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / direct_B_prime

**Exact prompt**

```text
Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.

Question:
According to the information above, where was Anil Das born?

Answer with only the requested name or location.
```

**Raw response**

```text
Kottayam
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / state_B

**Exact prompt**

```text
Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.

Current Step 1 state:
Helmut Käutner

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Düsseldorf
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H0 / state_B_prime

**Exact prompt**

```text
Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.

Current Step 1 state:
Anil Das

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Kottayam
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / direct_B

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Große Freiheit Nr. 7?

Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.

Question:
According to the information above, where was Helmut Käutner born?

Answer with only the requested name or location.
```

**Raw response**

```text
Düsseldorf
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / direct_B_prime

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Große Freiheit Nr. 7?

Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.

Question:
According to the information above, where was Anil Das born?

Answer with only the requested name or location.
```

**Raw response**

```text
Kottayam
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / state_B

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Große Freiheit Nr. 7?

Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.

Current Step 1 state:
Helmut Käutner

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Düsseldorf
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / state_B_prime

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Große Freiheit Nr. 7?

Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.

Current Step 1 state:
Anil Das

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Kottayam
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / direct_B

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Große Freiheit Nr. 7?

Additional context:
The film is also known as Port of Freedom in the United Kingdom.

Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.

Question:
According to the information above, where was Helmut Käutner born?

Answer with only the requested name or location.
```

**Raw response**

```text
Düsseldorf
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / direct_B_prime

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Große Freiheit Nr. 7?

Additional context:
The film is also known as Port of Freedom in the United Kingdom.

Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.

Question:
According to the information above, where was Anil Das born?

Answer with only the requested name or location.
```

**Raw response**

```text
Kottayam
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / state_B

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Große Freiheit Nr. 7?

Additional context:
The film is also known as Port of Freedom in the United Kingdom.

Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.

Current Step 1 state:
Helmut Käutner

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Düsseldorf
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / state_B_prime

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Große Freiheit Nr. 7?

Additional context:
The film is also known as Port of Freedom in the United Kingdom.

Reference facts:
1. Anil Das was born in Kottayam.
2. Helmut Käutner was born in Düsseldorf.

Current Step 1 state:
Anil Das

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Kottayam
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / direct_B

**Exact prompt**

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

Question:
According to the information above, where was Helmut Käutner born?

Answer with only the requested name or location.
```

**Raw response**

```text
Düsseldorf
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / direct_B_prime

**Exact prompt**

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

Question:
According to the information above, where was Anil Das born?

Answer with only the requested name or location.
```

**Raw response**

```text
Kottayam
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / state_B

**Exact prompt**

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

Current Step 1 state:
Helmut Käutner

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Düsseldorf
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / state_B_prime

**Exact prompt**

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

Current Step 1 state:
Anil Das

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Düsseldorf
```

Label: OVERRIDE_TO_GOLD; direct lookup pass: True; state adherence pass: False; pending evidence review: False.

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

| Context | CLA B | CLA B′ | state B | state B′ | Injected label |
|---|---|---|---|---|---|
| H0 | Denver | Xi'an | Denver | Xi'an | PROPAGATE |
| H1 | Denver | Xi'an | Denver | Xi'an | PROPAGATE |
| H2 | Denver | Xi'an | Denver | Xi'an | PROPAGATE |
| H3 | Denver | Xi'an | Denver | Denver | OVERRIDE_TO_GOLD |

**Highlights:** H3: PROPAGATE → OVERRIDE_TO_GOLD; H3 state_B_prime: direct-correct → state-wrong (OVERRIDE_TO_GOLD)

### H0 / direct_B

**Exact prompt**

```text
Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.

Question:
According to the information above, where was Jerome Storm born?

Answer with only the requested name or location.
```

**Raw response**

```text
Denver
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / direct_B_prime

**Exact prompt**

```text
Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.

Question:
According to the information above, where was Gu Changwei born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / state_B

**Exact prompt**

```text
Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.

Current Step 1 state:
Jerome Storm

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Denver
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H0 / state_B_prime

**Exact prompt**

```text
Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.

Current Step 1 state:
Gu Changwei

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / direct_B

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Arabian Love?

Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.

Question:
According to the information above, where was Jerome Storm born?

Answer with only the requested name or location.
```

**Raw response**

```text
Denver
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / direct_B_prime

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Arabian Love?

Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.

Question:
According to the information above, where was Gu Changwei born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / state_B

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Arabian Love?

Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.

Current Step 1 state:
Jerome Storm

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Denver
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / state_B_prime

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Arabian Love?

Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.

Current Step 1 state:
Gu Changwei

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / direct_B

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Arabian Love?

Additional context:
It is not known whether the film currently survives.

Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.

Question:
According to the information above, where was Jerome Storm born?

Answer with only the requested name or location.
```

**Raw response**

```text
Denver
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / direct_B_prime

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Arabian Love?

Additional context:
It is not known whether the film currently survives.

Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.

Question:
According to the information above, where was Gu Changwei born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / state_B

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Arabian Love?

Additional context:
It is not known whether the film currently survives.

Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.

Current Step 1 state:
Jerome Storm

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Denver
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / state_B_prime

**Exact prompt**

```text
Original task:
What is the place of birth of the director of film Arabian Love?

Additional context:
It is not known whether the film currently survives.

Reference facts:
1. Jerome Storm was born in Denver.
2. Gu Changwei was born in Xi'an.

Current Step 1 state:
Gu Changwei

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / direct_B

**Exact prompt**

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

Question:
According to the information above, where was Jerome Storm born?

Answer with only the requested name or location.
```

**Raw response**

```text
Denver
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / direct_B_prime

**Exact prompt**

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

Question:
According to the information above, where was Gu Changwei born?

Answer with only the requested name or location.
```

**Raw response**

```text
Xi'an
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / state_B

**Exact prompt**

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

Current Step 1 state:
Jerome Storm

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Denver
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / state_B_prime

**Exact prompt**

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

Current Step 1 state:
Gu Changwei

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Denver
```

Label: OVERRIDE_TO_GOLD; direct lookup pass: True; state adherence pass: False; pending evidence review: False.

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

| Context | CLA B | CLA B′ | state B | state B′ | Injected label |
|---|---|---|---|---|---|
| H0 | Rosario | Rēzekne | Rosario | Rēzekne | PROPAGATE |
| H1 | Rosario | Rēzekne | Rosario | Rēzekne | PROPAGATE |
| H2 | Rosario | Rēzekne | Rēzekne | Rēzekne | PROPAGATE |
| H3 | Rosario | Rēzekne | Rosario | Rosario | OVERRIDE_TO_GOLD |

**Highlights:** H2 state_B: direct-correct → state-wrong (OTHER_CONTEXT_TARGET); H2: gold-state failure; H3: PROPAGATE → OVERRIDE_TO_GOLD; H3 state_B_prime: direct-correct → state-wrong (OVERRIDE_TO_GOLD)

### H0 / direct_B

**Exact prompt**

```text
Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.

Question:
According to the information above, where was Rodrigo Grande born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rosario
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / direct_B_prime

**Exact prompt**

```text
Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.

Question:
According to the information above, where was Fridrikh Ermler born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rēzekne
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / state_B

**Exact prompt**

```text
Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.

Current Step 1 state:
Rodrigo Grande

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rosario
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H0 / state_B_prime

**Exact prompt**

```text
Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.

Current Step 1 state:
Fridrikh Ermler

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rēzekne
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / direct_B

**Exact prompt**

```text
Original task:
Where was the director of film At The End Of The Tunnel born?

Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.

Question:
According to the information above, where was Rodrigo Grande born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rosario
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / direct_B_prime

**Exact prompt**

```text
Original task:
Where was the director of film At The End Of The Tunnel born?

Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.

Question:
According to the information above, where was Fridrikh Ermler born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rēzekne
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / state_B

**Exact prompt**

```text
Original task:
Where was the director of film At The End Of The Tunnel born?

Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.

Current Step 1 state:
Rodrigo Grande

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rosario
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / state_B_prime

**Exact prompt**

```text
Original task:
Where was the director of film At The End Of The Tunnel born?

Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.

Current Step 1 state:
Fridrikh Ermler

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rēzekne
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / direct_B

**Exact prompt**

```text
Original task:
Where was the director of film At The End Of The Tunnel born?

Additional context:
The film won best movie at the Seattle International Film Festival in 2017.

Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.

Question:
According to the information above, where was Rodrigo Grande born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rosario
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / direct_B_prime

**Exact prompt**

```text
Original task:
Where was the director of film At The End Of The Tunnel born?

Additional context:
The film won best movie at the Seattle International Film Festival in 2017.

Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.

Question:
According to the information above, where was Fridrikh Ermler born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rēzekne
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / state_B

**Exact prompt**

```text
Original task:
Where was the director of film At The End Of The Tunnel born?

Additional context:
The film won best movie at the Seattle International Film Festival in 2017.

Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.

Current Step 1 state:
Rodrigo Grande

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rēzekne
```

Label: OTHER_CONTEXT_TARGET; direct lookup pass: True; state adherence pass: False; pending evidence review: False.

### H2 / state_B_prime

**Exact prompt**

```text
Original task:
Where was the director of film At The End Of The Tunnel born?

Additional context:
The film won best movie at the Seattle International Film Festival in 2017.

Reference facts:
1. Fridrikh Ermler was born in Rēzekne.
2. Rodrigo Grande was born in Rosario.

Current Step 1 state:
Fridrikh Ermler

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rēzekne
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / direct_B

**Exact prompt**

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

Question:
According to the information above, where was Rodrigo Grande born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rosario
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / direct_B_prime

**Exact prompt**

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

Question:
According to the information above, where was Fridrikh Ermler born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rēzekne
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / state_B

**Exact prompt**

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

Current Step 1 state:
Rodrigo Grande

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rosario
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / state_B_prime

**Exact prompt**

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

Current Step 1 state:
Fridrikh Ermler

Question:
Using the current Step 1 state and the information above, where was that person born?

Answer with only the requested name or location.
```

**Raw response**

```text
Rosario
```

Label: OVERRIDE_TO_GOLD; direct lookup pass: True; state adherence pass: False; pending evidence review: False.

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

| Context | CLA B | CLA B′ | state B | state B′ | Injected label |
|---|---|---|---|---|---|
| H0 | Yuen Siu-tien | H. S. Rawail | Yuen Siu-tien | H. S. Rawail | PROPAGATE |
| H1 | Yuen Siu-tien | H. S. Rawail | Yuen Siu-tien | H. S. Rawail | PROPAGATE |
| H2 | Yuen Siu-tien | H. S. Rawail | Yuen Siu-tien | H. S. Rawail | PROPAGATE |
| H3 | Yuen Siu-tien | H. S. Rawail | Yuen Siu-tien | Yuen Siu-tien | OVERRIDE_TO_GOLD |

**Highlights:** H3: PROPAGATE → OVERRIDE_TO_GOLD; H3 state_B_prime: direct-correct → state-wrong (OVERRIDE_TO_GOLD)

### H0 / direct_B

**Exact prompt**

```text
Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.

Question:
According to the information above, who was the father of Yuen Woo-ping?

Answer with only the requested name or location.
```

**Raw response**

```text
Yuen Siu-tien
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / direct_B_prime

**Exact prompt**

```text
Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.

Question:
According to the information above, who was the father of Rahul Rawail?

Answer with only the requested name or location.
```

**Raw response**

```text
H. S. Rawail
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / state_B

**Exact prompt**

```text
Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.

Current Step 1 state:
Yuen Woo-ping

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Yuen Siu-tien
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H0 / state_B_prime

**Exact prompt**

```text
Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.

Current Step 1 state:
Rahul Rawail

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
H. S. Rawail
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / direct_B

**Exact prompt**

```text
Original task:
Who is the father of the director of film In The Line Of Duty 4: Witness?

Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.

Question:
According to the information above, who was the father of Yuen Woo-ping?

Answer with only the requested name or location.
```

**Raw response**

```text
Yuen Siu-tien
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / direct_B_prime

**Exact prompt**

```text
Original task:
Who is the father of the director of film In The Line Of Duty 4: Witness?

Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.

Question:
According to the information above, who was the father of Rahul Rawail?

Answer with only the requested name or location.
```

**Raw response**

```text
H. S. Rawail
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / state_B

**Exact prompt**

```text
Original task:
Who is the father of the director of film In The Line Of Duty 4: Witness?

Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.

Current Step 1 state:
Yuen Woo-ping

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Yuen Siu-tien
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / state_B_prime

**Exact prompt**

```text
Original task:
Who is the father of the director of film In The Line Of Duty 4: Witness?

Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.

Current Step 1 state:
Rahul Rawail

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
H. S. Rawail
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / direct_B

**Exact prompt**

```text
Original task:
Who is the father of the director of film In The Line Of Duty 4: Witness?

Additional context:
The film was released in the Hong Kong on 21 July 1989.

Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.

Question:
According to the information above, who was the father of Yuen Woo-ping?

Answer with only the requested name or location.
```

**Raw response**

```text
Yuen Siu-tien
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / direct_B_prime

**Exact prompt**

```text
Original task:
Who is the father of the director of film In The Line Of Duty 4: Witness?

Additional context:
The film was released in the Hong Kong on 21 July 1989.

Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.

Question:
According to the information above, who was the father of Rahul Rawail?

Answer with only the requested name or location.
```

**Raw response**

```text
H. S. Rawail
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / state_B

**Exact prompt**

```text
Original task:
Who is the father of the director of film In The Line Of Duty 4: Witness?

Additional context:
The film was released in the Hong Kong on 21 July 1989.

Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.

Current Step 1 state:
Yuen Woo-ping

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Yuen Siu-tien
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / state_B_prime

**Exact prompt**

```text
Original task:
Who is the father of the director of film In The Line Of Duty 4: Witness?

Additional context:
The film was released in the Hong Kong on 21 July 1989.

Reference facts:
1. Yuen Woo-ping's father was Yuen Siu-tien.
2. Rahul Rawail's father was H. S. Rawail.

Current Step 1 state:
Rahul Rawail

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
H. S. Rawail
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / direct_B

**Exact prompt**

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

Question:
According to the information above, who was the father of Yuen Woo-ping?

Answer with only the requested name or location.
```

**Raw response**

```text
Yuen Siu-tien
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / direct_B_prime

**Exact prompt**

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

Question:
According to the information above, who was the father of Rahul Rawail?

Answer with only the requested name or location.
```

**Raw response**

```text
H. S. Rawail
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / state_B

**Exact prompt**

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

Current Step 1 state:
Yuen Woo-ping

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Yuen Siu-tien
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / state_B_prime

**Exact prompt**

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

Current Step 1 state:
Rahul Rawail

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Yuen Siu-tien
```

Label: OVERRIDE_TO_GOLD; direct lookup pass: True; state adherence pass: False; pending evidence review: False.

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

| Context | CLA B | CLA B′ | state B | state B′ | Injected label |
|---|---|---|---|---|---|
| H0 | György Enyedi | Daniel Alomía Robles | György Enyedi | Daniel Alomía Robles | PROPAGATE |
| H1 | György Enyedi | Daniel Alomía Robles | György Enyedi | Daniel Alomía Robles | PROPAGATE |
| H2 | György Enyedi | Daniel Alomía Robles | György Enyedi | Daniel Alomía Robles | PROPAGATE |
| H3 | György Enyedi | Daniel Alomía Robles | György Enyedi | Daniel Alomía Robles | PROPAGATE |

**Highlights:** No outcome transitions, framing failures or gold-state failures.

### H0 / direct_B

**Exact prompt**

```text
Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.

Question:
According to the information above, who was the father of Ildikó Enyedi?

Answer with only the requested name or location.
```

**Raw response**

```text
György Enyedi
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / direct_B_prime

**Exact prompt**

```text
Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.

Question:
According to the information above, who was the father of Armando Robles Godoy?

Answer with only the requested name or location.
```

**Raw response**

```text
Daniel Alomía Robles
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / state_B

**Exact prompt**

```text
Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.

Current Step 1 state:
Ildikó Enyedi

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
György Enyedi
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H0 / state_B_prime

**Exact prompt**

```text
Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.

Current Step 1 state:
Armando Robles Godoy

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Daniel Alomía Robles
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / direct_B

**Exact prompt**

```text
Original task:
Who is the father of the director of film My 20Th Century?

Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.

Question:
According to the information above, who was the father of Ildikó Enyedi?

Answer with only the requested name or location.
```

**Raw response**

```text
György Enyedi
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / direct_B_prime

**Exact prompt**

```text
Original task:
Who is the father of the director of film My 20Th Century?

Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.

Question:
According to the information above, who was the father of Armando Robles Godoy?

Answer with only the requested name or location.
```

**Raw response**

```text
Daniel Alomía Robles
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / state_B

**Exact prompt**

```text
Original task:
Who is the father of the director of film My 20Th Century?

Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.

Current Step 1 state:
Ildikó Enyedi

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
György Enyedi
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / state_B_prime

**Exact prompt**

```text
Original task:
Who is the father of the director of film My 20Th Century?

Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.

Current Step 1 state:
Armando Robles Godoy

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Daniel Alomía Robles
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / direct_B

**Exact prompt**

```text
Original task:
Who is the father of the director of film My 20Th Century?

Additional context:
It premiered at the Toronto Festival of Festivals.

Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.

Question:
According to the information above, who was the father of Ildikó Enyedi?

Answer with only the requested name or location.
```

**Raw response**

```text
György Enyedi
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / direct_B_prime

**Exact prompt**

```text
Original task:
Who is the father of the director of film My 20Th Century?

Additional context:
It premiered at the Toronto Festival of Festivals.

Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.

Question:
According to the information above, who was the father of Armando Robles Godoy?

Answer with only the requested name or location.
```

**Raw response**

```text
Daniel Alomía Robles
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / state_B

**Exact prompt**

```text
Original task:
Who is the father of the director of film My 20Th Century?

Additional context:
It premiered at the Toronto Festival of Festivals.

Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.

Current Step 1 state:
Ildikó Enyedi

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
György Enyedi
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / state_B_prime

**Exact prompt**

```text
Original task:
Who is the father of the director of film My 20Th Century?

Additional context:
It premiered at the Toronto Festival of Festivals.

Reference facts:
1. Armando Robles Godoy's father was Daniel Alomía Robles.
2. Ildikó Enyedi's father was György Enyedi.

Current Step 1 state:
Armando Robles Godoy

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Daniel Alomía Robles
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / direct_B

**Exact prompt**

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

Question:
According to the information above, who was the father of Ildikó Enyedi?

Answer with only the requested name or location.
```

**Raw response**

```text
György Enyedi
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / direct_B_prime

**Exact prompt**

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

Question:
According to the information above, who was the father of Armando Robles Godoy?

Answer with only the requested name or location.
```

**Raw response**

```text
Daniel Alomía Robles
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / state_B

**Exact prompt**

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

Current Step 1 state:
Ildikó Enyedi

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
György Enyedi
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / state_B_prime

**Exact prompt**

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

Current Step 1 state:
Armando Robles Godoy

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Daniel Alomía Robles
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

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

| Context | CLA B | CLA B′ | state B | state B′ | Injected label |
|---|---|---|---|---|---|
| H0 | Inder Raj Anand | Leopoldo Torres Ríos | Inder Raj Anand | Leopoldo Torres Ríos | PROPAGATE |
| H1 | Inder Raj Anand | Leopoldo Torres Ríos | Inder Raj Anand | Leopoldo Torres Ríos | PROPAGATE |
| H2 | Inder Raj Anand | Leopoldo Torres Ríos | Inder Raj Anand | Leopoldo Torres Ríos | PROPAGATE |
| H3 | Inder Raj Anand | Leopoldo Torres Ríos | Inder Raj Anand | Leopoldo Torres Ríos | PROPAGATE |

**Highlights:** No outcome transitions, framing failures or gold-state failures.

### H0 / direct_B

**Exact prompt**

```text
Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.

Question:
According to the information above, who was the father of Tinnu Anand?

Answer with only the requested name or location.
```

**Raw response**

```text
Inder Raj Anand
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / direct_B_prime

**Exact prompt**

```text
Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.

Question:
According to the information above, who was the father of Leopoldo Torre Nilsson?

Answer with only the requested name or location.
```

**Raw response**

```text
Leopoldo Torres Ríos
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / state_B

**Exact prompt**

```text
Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.

Current Step 1 state:
Tinnu Anand

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Inder Raj Anand
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H0 / state_B_prime

**Exact prompt**

```text
Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.

Current Step 1 state:
Leopoldo Torre Nilsson

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Leopoldo Torres Ríos
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / direct_B

**Exact prompt**

```text
Original task:
Who is the father of the director of film Duniya Meri Jeb Mein?

Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.

Question:
According to the information above, who was the father of Tinnu Anand?

Answer with only the requested name or location.
```

**Raw response**

```text
Inder Raj Anand
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / direct_B_prime

**Exact prompt**

```text
Original task:
Who is the father of the director of film Duniya Meri Jeb Mein?

Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.

Question:
According to the information above, who was the father of Leopoldo Torre Nilsson?

Answer with only the requested name or location.
```

**Raw response**

```text
Leopoldo Torres Ríos
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / state_B

**Exact prompt**

```text
Original task:
Who is the father of the director of film Duniya Meri Jeb Mein?

Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.

Current Step 1 state:
Tinnu Anand

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Inder Raj Anand
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / state_B_prime

**Exact prompt**

```text
Original task:
Who is the father of the director of film Duniya Meri Jeb Mein?

Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.

Current Step 1 state:
Leopoldo Torre Nilsson

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Leopoldo Torres Ríos
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / direct_B

**Exact prompt**

```text
Original task:
Who is the father of the director of film Duniya Meri Jeb Mein?

Additional context:
The film stars Shashi Kapoor and Rishi Kapoor.

Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.

Question:
According to the information above, who was the father of Tinnu Anand?

Answer with only the requested name or location.
```

**Raw response**

```text
Inder Raj Anand
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / direct_B_prime

**Exact prompt**

```text
Original task:
Who is the father of the director of film Duniya Meri Jeb Mein?

Additional context:
The film stars Shashi Kapoor and Rishi Kapoor.

Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.

Question:
According to the information above, who was the father of Leopoldo Torre Nilsson?

Answer with only the requested name or location.
```

**Raw response**

```text
Leopoldo Torres Ríos
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / state_B

**Exact prompt**

```text
Original task:
Who is the father of the director of film Duniya Meri Jeb Mein?

Additional context:
The film stars Shashi Kapoor and Rishi Kapoor.

Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.

Current Step 1 state:
Tinnu Anand

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Inder Raj Anand
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / state_B_prime

**Exact prompt**

```text
Original task:
Who is the father of the director of film Duniya Meri Jeb Mein?

Additional context:
The film stars Shashi Kapoor and Rishi Kapoor.

Reference facts:
1. Tinnu Anand's father was Inder Raj Anand.
2. Leopoldo Torre Nilsson's father was Leopoldo Torres Ríos.

Current Step 1 state:
Leopoldo Torre Nilsson

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Leopoldo Torres Ríos
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / direct_B

**Exact prompt**

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

Question:
According to the information above, who was the father of Tinnu Anand?

Answer with only the requested name or location.
```

**Raw response**

```text
Inder Raj Anand
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / direct_B_prime

**Exact prompt**

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

Question:
According to the information above, who was the father of Leopoldo Torre Nilsson?

Answer with only the requested name or location.
```

**Raw response**

```text
Leopoldo Torres Ríos
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / state_B

**Exact prompt**

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

Current Step 1 state:
Tinnu Anand

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Inder Raj Anand
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / state_B_prime

**Exact prompt**

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

Current Step 1 state:
Leopoldo Torre Nilsson

Question:
Using the current Step 1 state and the information above, who was the father of that person?

Answer with only the requested name or location.
```

**Raw response**

```text
Leopoldo Torres Ríos
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

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

| Context | CLA B | CLA B′ | state B | state B′ | Injected label |
|---|---|---|---|---|---|
| H0 | Přerov | Porterville | Přerov | Porterville | PROPAGATE |
| H1 | Přerov | Porterville | Přerov | Porterville | PROPAGATE |
| H2 | Přerov | Porterville | Přerov | Porterville | PROPAGATE |
| H3 | Přerov | Porterville | Přerov | Přerov | OVERRIDE_TO_GOLD |

**Highlights:** H3: PROPAGATE → OVERRIDE_TO_GOLD; H3 state_B_prime: direct-correct → state-wrong (OVERRIDE_TO_GOLD)

### H0 / direct_B

**Exact prompt**

```text
Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.

Question:
According to the information above, where did Vojtěch Jasný die?

Answer with only the requested name or location.
```

**Raw response**

```text
Přerov
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / direct_B_prime

**Exact prompt**

```text
Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.

Question:
According to the information above, where did Robert P. Kerr die?

Answer with only the requested name or location.
```

**Raw response**

```text
Porterville
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / state_B

**Exact prompt**

```text
Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.

Current Step 1 state:
Vojtěch Jasný

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Přerov
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H0 / state_B_prime

**Exact prompt**

```text
Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.

Current Step 1 state:
Robert P. Kerr

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Porterville
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / direct_B

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Pipes?

Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.

Question:
According to the information above, where did Vojtěch Jasný die?

Answer with only the requested name or location.
```

**Raw response**

```text
Přerov
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / direct_B_prime

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Pipes?

Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.

Question:
According to the information above, where did Robert P. Kerr die?

Answer with only the requested name or location.
```

**Raw response**

```text
Porterville
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / state_B

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Pipes?

Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.

Current Step 1 state:
Vojtěch Jasný

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Přerov
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / state_B_prime

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Pipes?

Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.

Current Step 1 state:
Robert P. Kerr

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Porterville
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / direct_B

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Pipes?

Additional context:
It was entered into the 1966 Cannes Film Festival.

Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.

Question:
According to the information above, where did Vojtěch Jasný die?

Answer with only the requested name or location.
```

**Raw response**

```text
Přerov
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / direct_B_prime

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Pipes?

Additional context:
It was entered into the 1966 Cannes Film Festival.

Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.

Question:
According to the information above, where did Robert P. Kerr die?

Answer with only the requested name or location.
```

**Raw response**

```text
Porterville
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / state_B

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Pipes?

Additional context:
It was entered into the 1966 Cannes Film Festival.

Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.

Current Step 1 state:
Vojtěch Jasný

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Přerov
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / state_B_prime

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Pipes?

Additional context:
It was entered into the 1966 Cannes Film Festival.

Reference facts:
1. Robert P. Kerr died in Porterville.
2. Vojtěch Jasný died in Přerov.

Current Step 1 state:
Robert P. Kerr

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Porterville
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / direct_B

**Exact prompt**

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

Question:
According to the information above, where did Vojtěch Jasný die?

Answer with only the requested name or location.
```

**Raw response**

```text
Přerov
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / direct_B_prime

**Exact prompt**

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

Question:
According to the information above, where did Robert P. Kerr die?

Answer with only the requested name or location.
```

**Raw response**

```text
Porterville
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / state_B

**Exact prompt**

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

Current Step 1 state:
Vojtěch Jasný

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Přerov
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / state_B_prime

**Exact prompt**

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

Current Step 1 state:
Robert P. Kerr

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Přerov
```

Label: OVERRIDE_TO_GOLD; direct lookup pass: True; state adherence pass: False; pending evidence review: False.

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

| Context | CLA B | CLA B′ | state B | state B′ | Injected label |
|---|---|---|---|---|---|
| H0 | San Felice Circeo | Shaftsbury, Vermont | San Felice Circeo | Shaftsbury, Vermont | PROPAGATE |
| H1 | San Felice Circeo | Shaftsbury, Vermont | San Felice Circeo | Shaftsbury, Vermont | PROPAGATE |
| H2 | San Felice Circeo | Shaftsbury, Vermont | San Felice Circeo | Shaftsbury, Vermont | PROPAGATE |
| H3 | San Felice Circeo | Shaftsbury, Vermont | San Felice Circeo | San Felice Circeo | OVERRIDE_TO_GOLD |

**Highlights:** H3: PROPAGATE → OVERRIDE_TO_GOLD; H3 state_B_prime: direct-correct → state-wrong (OVERRIDE_TO_GOLD)

### H0 / direct_B

**Exact prompt**

```text
Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.

Question:
According to the information above, where did Marcello Fondato die?

Answer with only the requested name or location.
```

**Raw response**

```text
San Felice Circeo
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / direct_B_prime

**Exact prompt**

```text
Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.

Question:
According to the information above, where did James Goldstone die?

Answer with only the requested name or location.
```

**Raw response**

```text
Shaftsbury, Vermont
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / state_B

**Exact prompt**

```text
Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.

Current Step 1 state:
Marcello Fondato

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
San Felice Circeo
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H0 / state_B_prime

**Exact prompt**

```text
Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.

Current Step 1 state:
James Goldstone

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Shaftsbury, Vermont
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / direct_B

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Protagonists (1968 Film)?

Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.

Question:
According to the information above, where did Marcello Fondato die?

Answer with only the requested name or location.
```

**Raw response**

```text
San Felice Circeo
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / direct_B_prime

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Protagonists (1968 Film)?

Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.

Question:
According to the information above, where did James Goldstone die?

Answer with only the requested name or location.
```

**Raw response**

```text
Shaftsbury, Vermont
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / state_B

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Protagonists (1968 Film)?

Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.

Current Step 1 state:
Marcello Fondato

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
San Felice Circeo
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / state_B_prime

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Protagonists (1968 Film)?

Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.

Current Step 1 state:
James Goldstone

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Shaftsbury, Vermont
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / direct_B

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Protagonists (1968 Film)?

Additional context:
It was listed to compete at the 1968 Cannes Film Festival, but the festival was cancelled due to the events of May 1968 in France.

Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.

Question:
According to the information above, where did Marcello Fondato die?

Answer with only the requested name or location.
```

**Raw response**

```text
San Felice Circeo
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / direct_B_prime

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Protagonists (1968 Film)?

Additional context:
It was listed to compete at the 1968 Cannes Film Festival, but the festival was cancelled due to the events of May 1968 in France.

Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.

Question:
According to the information above, where did James Goldstone die?

Answer with only the requested name or location.
```

**Raw response**

```text
Shaftsbury, Vermont
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / state_B

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Protagonists (1968 Film)?

Additional context:
It was listed to compete at the 1968 Cannes Film Festival, but the festival was cancelled due to the events of May 1968 in France.

Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.

Current Step 1 state:
Marcello Fondato

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
San Felice Circeo
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / state_B_prime

**Exact prompt**

```text
Original task:
Where was the place of death of the director of film The Protagonists (1968 Film)?

Additional context:
It was listed to compete at the 1968 Cannes Film Festival, but the festival was cancelled due to the events of May 1968 in France.

Reference facts:
1. Marcello Fondato died in San Felice Circeo.
2. James Goldstone died in Shaftsbury, Vermont.

Current Step 1 state:
James Goldstone

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Shaftsbury, Vermont
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / direct_B

**Exact prompt**

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

Question:
According to the information above, where did Marcello Fondato die?

Answer with only the requested name or location.
```

**Raw response**

```text
San Felice Circeo
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / direct_B_prime

**Exact prompt**

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

Question:
According to the information above, where did James Goldstone die?

Answer with only the requested name or location.
```

**Raw response**

```text
Shaftsbury, Vermont
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / state_B

**Exact prompt**

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

Current Step 1 state:
Marcello Fondato

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
San Felice Circeo
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / state_B_prime

**Exact prompt**

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

Current Step 1 state:
James Goldstone

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
San Felice Circeo
```

Label: OVERRIDE_TO_GOLD; direct lookup pass: True; state adherence pass: False; pending evidence review: False.

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

| Context | CLA B | CLA B′ | state B | state B′ | Injected label |
|---|---|---|---|---|---|
| H0 | Madrid | Mumbai | Madrid | Mumbai | PROPAGATE |
| H1 | Madrid | Mumbai | Madrid | Mumbai | PROPAGATE |
| H2 | Madrid | Mumbai | Madrid | Mumbai | PROPAGATE |
| H3 | Madrid | Mumbai | Madrid | Madrid | OVERRIDE_TO_GOLD |

**Highlights:** H3: PROPAGATE → OVERRIDE_TO_GOLD; H3 state_B_prime: direct-correct → state-wrong (OVERRIDE_TO_GOLD)

### H0 / direct_B

**Exact prompt**

```text
Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.

Question:
According to the information above, where did León Klimovsky die?

Answer with only the requested name or location.
```

**Raw response**

```text
Madrid
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / direct_B_prime

**Exact prompt**

```text
Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.

Question:
According to the information above, where did Bhappi Sonie die?

Answer with only the requested name or location.
```

**Raw response**

```text
Mumbai
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H0 / state_B

**Exact prompt**

```text
Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.

Current Step 1 state:
León Klimovsky

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Madrid
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H0 / state_B_prime

**Exact prompt**

```text
Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.

Current Step 1 state:
Bhappi Sonie

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Mumbai
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / direct_B

**Exact prompt**

```text
Original task:
Where did the director of film The Marihuana Story die?

Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.

Question:
According to the information above, where did León Klimovsky die?

Answer with only the requested name or location.
```

**Raw response**

```text
Madrid
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / direct_B_prime

**Exact prompt**

```text
Original task:
Where did the director of film The Marihuana Story die?

Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.

Question:
According to the information above, where did Bhappi Sonie die?

Answer with only the requested name or location.
```

**Raw response**

```text
Mumbai
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H1 / state_B

**Exact prompt**

```text
Original task:
Where did the director of film The Marihuana Story die?

Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.

Current Step 1 state:
León Klimovsky

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Madrid
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H1 / state_B_prime

**Exact prompt**

```text
Original task:
Where did the director of film The Marihuana Story die?

Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.

Current Step 1 state:
Bhappi Sonie

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Mumbai
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / direct_B

**Exact prompt**

```text
Original task:
Where did the director of film The Marihuana Story die?

Additional context:
It was entered into the 1951 Cannes Film Festival.

Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.

Question:
According to the information above, where did León Klimovsky die?

Answer with only the requested name or location.
```

**Raw response**

```text
Madrid
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / direct_B_prime

**Exact prompt**

```text
Original task:
Where did the director of film The Marihuana Story die?

Additional context:
It was entered into the 1951 Cannes Film Festival.

Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.

Question:
According to the information above, where did Bhappi Sonie die?

Answer with only the requested name or location.
```

**Raw response**

```text
Mumbai
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H2 / state_B

**Exact prompt**

```text
Original task:
Where did the director of film The Marihuana Story die?

Additional context:
It was entered into the 1951 Cannes Film Festival.

Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.

Current Step 1 state:
León Klimovsky

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Madrid
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H2 / state_B_prime

**Exact prompt**

```text
Original task:
Where did the director of film The Marihuana Story die?

Additional context:
It was entered into the 1951 Cannes Film Festival.

Reference facts:
1. Bhappi Sonie died in Mumbai.
2. León Klimovsky died in Madrid.

Current Step 1 state:
Bhappi Sonie

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Mumbai
```

Label: PROPAGATE; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / direct_B

**Exact prompt**

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

Question:
According to the information above, where did León Klimovsky die?

Answer with only the requested name or location.
```

**Raw response**

```text
Madrid
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / direct_B_prime

**Exact prompt**

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

Question:
According to the information above, where did Bhappi Sonie die?

Answer with only the requested name or location.
```

**Raw response**

```text
Mumbai
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: None; pending evidence review: False.

### H3 / state_B

**Exact prompt**

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

Current Step 1 state:
León Klimovsky

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Madrid
```

Label: EXACT_CORRECT; direct lookup pass: True; state adherence pass: True; pending evidence review: False.

### H3 / state_B_prime

**Exact prompt**

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

Current Step 1 state:
Bhappi Sonie

Question:
Using the current Step 1 state and the information above, where did that person die?

Answer with only the requested name or location.
```

**Raw response**

```text
Madrid
```

Label: OVERRIDE_TO_GOLD; direct lookup pass: True; state adherence pass: False; pending evidence review: False.