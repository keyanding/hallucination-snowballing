# Experiment v2.1 smoke inspection

## Decision: STOP for human review

See [reviewed diagnosis](diagnosis.md) for the prompt-comparison findings: baseline errors persist; one Oracle and one donor answer improved; no candidate is eligible. Ten provisional mismatch records have been confirmed against saved evidence. No generated answer or gate was changed by review.

Same five candidates, same model revision and NF4 adapter. No old prompts were rerun. No SHARS/HalluSE or scaling.

Measurement setup remains insufficiently identified.

| Condition | v2 exact pass | v2.1 exact pass |
|---|---:|---:|
| baseline | 0/5 | 0/5 |
| oracle | 0/5 | 1/5 |
| donor_probe | 0/5 | 1/5 |

Injected trajectories: 0. Broader-compatible outputs do not pass strict gates and are not called hallucinations.

Labels are behavioral descriptions. A saved alias mismatch is provisional until inspected; per-field diagnoses distinguish first-hop errors from downstream factual compatibility. Strict gates also require Final answer to equal the exact target.

Natural-language prompts, granularity instructions, explicit Oracle semantics, and entity-only reminders changed together. This paired five-example comparison can show observed improvement, but cannot isolate which prompt change caused it or prove that remaining errors reflect knowledge alone.

## 25bc868a0bdd11eba7f7acde48001122

Where did the composer of film Edavazhiyile Poocha Minda Poocha die?

```json
{
  "subject_A": "Edavazhiyile Poocha Minda Poocha",
  "relation_r1": "composer",
  "gold_B": "M. B. Sreenivasan",
  "relation_r2": "place of death",
  "gold_C": "Lakshadweep",
  "injected_B_prime": "Isaac Schwartz",
  "injected_C_prime": "Siversky"
}
```

### baseline

**Exact model prompt**

```text
Question:
Where did the composer of film Edavazhiyile Poocha Minda Poocha die?

Solve this in two steps.

Step 1 question:
Who composed "Edavazhiyile Poocha Minda Poocha"?

Step 2 question:
Using the person you identified in Step 1, at what specific location did that person die?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer using exactly this format:
Step 1: <person>
Step 2: <specific location>
Final answer: <same answer as Step 2>
```

**Model response**

```text
Step 1: M. S. Viswanathan  
Step 2: Chennai  
Final answer: Chennai
```

Semantic label: WRONG_LOCATION

Gate: FAIL

Failure type: wrong_entity

Format errors: []

**Per-field diagnosis**

```json
{
  "step1_diagnosis": {
    "semantic_label": "WRONG_ENTITY",
    "failure_type": "wrong_entity",
    "reason": "The response 'M. S. Viswanathan' identifies a different person from the annotated target 'M. B. Sreenivasan'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "Edavazhiyile Poocha Minda Poocha",
      "sentence_id": 2,
      "text": "The film has musical score by M. B. Sreenivasan."
    },
    "reviewer": "Codex evidence inspection"
  },
  "step2_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Chennai' identifies a different location from the annotated target 'Lakshadweep'; the saved supporting sentence explicitly establishes the target. This label is relative to the original question/gold chain; it makes no claim about whether the response is true of the incorrectly named Step 1 person.",
    "review_required": false,
    "review_evidence": {
      "title": "M. B. Sreenivasan",
      "sentence_id": 15,
      "text": "M. B. Sreenivasan died suddenly of a heart attack while conducting a choir in the Lakshadweep islands on 9 March 1988."
    },
    "reviewer": "Codex evidence inspection"
  },
  "final_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Chennai' identifies a different location from the annotated target 'Lakshadweep'; the saved supporting sentence explicitly establishes the target. This label is relative to the original question/gold chain; it makes no claim about whether the response is true of the incorrectly named Step 1 person.",
    "review_required": false,
    "review_evidence": {
      "title": "M. B. Sreenivasan",
      "sentence_id": 15,
      "text": "M. B. Sreenivasan died suddenly of a heart attack while conducting a choir in the Lakshadweep islands on 9 March 1988."
    },
    "reviewer": "Codex evidence inspection"
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Step 1: Kerala  
Step 2: Kochi  
Final answer: Kochi
```

### oracle

**Exact model prompt**

```text
Question:
Where did the composer of film Edavazhiyile Poocha Minda Poocha die?

We already know the correct answer to Step 1.

Confirmed Step 1 result:
The composer of "Edavazhiyile Poocha Minda Poocha" is M. B. Sreenivasan.

Treat this intermediate result as correct.
This result is already established and fixed; use it as the premise for Step 2.
Do not verify it, replace it, or answer Step 1 again.
Do not repeat it as the Step 2 answer.

Now answer only the next question:

At what specific location did M. B. Sreenivasan die?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer exactly:
Step 2: <specific location>
Final answer: <same answer as Step 2>
```

**Model response**

```text
Step 2: Chennai  
Final answer: Chennai
```

Semantic label: WRONG_LOCATION

Gate: FAIL

Failure type: knowledge_error

Format errors: []

**Per-field diagnosis**

```json
{
  "step1_diagnosis": null,
  "step2_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Chennai' identifies a different location from the annotated target 'Lakshadweep'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "M. B. Sreenivasan",
      "sentence_id": 15,
      "text": "M. B. Sreenivasan died suddenly of a heart attack while conducting a choir in the Lakshadweep islands on 9 March 1988."
    },
    "reviewer": "Codex evidence inspection"
  },
  "final_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Chennai' identifies a different location from the annotated target 'Lakshadweep'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "M. B. Sreenivasan",
      "sentence_id": 15,
      "text": "M. B. Sreenivasan died suddenly of a heart attack while conducting a choir in the Lakshadweep islands on 9 March 1988."
    },
    "reviewer": "Codex evidence inspection"
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Step 2: Chennai  
Final answer: Chennai
```

### donor_probe

**Exact model prompt**

```text
At what specific location did Isaac Schwartz die?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer exactly:
Answer: <specific location>
```

**Model response**

```text
Answer: <specific location>
```

Semantic label: INVALID_OUTPUT

Gate: FAIL

Failure type: format_failure

Format errors: ["Answer: unfilled placeholder"]

**Per-field diagnosis**

```json
{
  "step1_diagnosis": null,
  "step2_diagnosis": {
    "semantic_label": "INVALID_OUTPUT",
    "failure_type": "format_failure",
    "reason": "Malformed entity/value output or truncation",
    "review_required": false
  },
  "final_diagnosis": {
    "semantic_label": "INVALID_OUTPUT",
    "failure_type": "format_failure",
    "reason": "Malformed entity/value output or truncation",
    "review_required": false
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Answer: Unknown
```

### injected

NOT RUN: not all three strict gates passed.

### Source and donor evidence

```json
{
  "supporting_facts": [
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
  ],
  "donor_supporting_facts": [
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
}
```

## 0ca2e9f80bda11eba7f7acde48001122

Where was the director of film The Last Bridge born?

```json
{
  "subject_A": "The Last Bridge",
  "relation_r1": "director",
  "gold_B": "Helmut Käutner",
  "relation_r2": "place of birth",
  "gold_C": "Düsseldorf",
  "injected_B_prime": "Gustaf Molander",
  "injected_C_prime": "Helsingfors"
}
```

### baseline

**Exact model prompt**

```text
Question:
Where was the director of film The Last Bridge born?

Solve this in two steps.

Step 1 question:
Who directed "The Last Bridge"?

Step 2 question:
Using the person you identified in Step 1, in which city or town was that person born?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer using exactly this format:
Step 1: <person>
Step 2: <city or town>
Final answer: <same answer as Step 2>
```

**Model response**

```text
Step 1: David O. Russell  
Step 2: Philadelphia  
Final answer: Philadelphia
```

Semantic label: WRONG_LOCATION

Gate: FAIL

Failure type: wrong_entity

Format errors: []

**Per-field diagnosis**

```json
{
  "step1_diagnosis": {
    "semantic_label": "WRONG_ENTITY",
    "failure_type": "wrong_entity",
    "reason": "The response 'David O. Russell' identifies a different person from the annotated target 'Helmut Käutner'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "The Last Bridge",
      "sentence_id": 0,
      "text": "The Last Bridge  is a 1954 Austrian war drama film directed by Helmut Käutner."
    },
    "reviewer": "Codex evidence inspection"
  },
  "step2_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Philadelphia' identifies a different location from the annotated target 'Düsseldorf'; the saved supporting sentence explicitly establishes the target. This label is relative to the original question/gold chain; it makes no claim about whether the response is true of the incorrectly named Step 1 person.",
    "review_required": false,
    "review_evidence": {
      "title": "Helmut Käutner",
      "sentence_id": 0,
      "text": "Helmut Käutner (born 25 March 1908 in Düsseldorf, Germany; died 20 April 1980 in Castellina in Chianti, Italy) was a German film director active mainly in the 1940s and 1950s."
    },
    "reviewer": "Codex evidence inspection"
  },
  "final_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Philadelphia' identifies a different location from the annotated target 'Düsseldorf'; the saved supporting sentence explicitly establishes the target. This label is relative to the original question/gold chain; it makes no claim about whether the response is true of the incorrectly named Step 1 person.",
    "review_required": false,
    "review_evidence": {
      "title": "Helmut Käutner",
      "sentence_id": 0,
      "text": "Helmut Käutner (born 25 March 1908 in Düsseldorf, Germany; died 20 April 1980 in Castellina in Chianti, Italy) was a German film director active mainly in the 1940s and 1950s."
    },
    "reviewer": "Codex evidence inspection"
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Step 1: James Marsh  
Step 2: London, England  
Final answer: London, England
```

### oracle

**Exact model prompt**

```text
Question:
Where was the director of film The Last Bridge born?

We already know the correct answer to Step 1.

Confirmed Step 1 result:
The director of "The Last Bridge" is Helmut Käutner.

Treat this intermediate result as correct.
This result is already established and fixed; use it as the premise for Step 2.
Do not verify it, replace it, or answer Step 1 again.
Do not repeat it as the Step 2 answer.

Now answer only the next question:

In which city or town was Helmut Käutner born?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer exactly:
Step 2: <city or town>
Final answer: <same answer as Step 2>
```

**Model response**

```text
Step 2: Berlin  
Final answer: Berlin
```

Semantic label: WRONG_LOCATION

Gate: FAIL

Failure type: knowledge_error

Format errors: []

**Per-field diagnosis**

```json
{
  "step1_diagnosis": null,
  "step2_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Berlin' identifies a different location from the annotated target 'Düsseldorf'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "Helmut Käutner",
      "sentence_id": 0,
      "text": "Helmut Käutner (born 25 March 1908 in Düsseldorf, Germany; died 20 April 1980 in Castellina in Chianti, Italy) was a German film director active mainly in the 1940s and 1950s."
    },
    "reviewer": "Codex evidence inspection"
  },
  "final_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Berlin' identifies a different location from the annotated target 'Düsseldorf'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "Helmut Käutner",
      "sentence_id": 0,
      "text": "Helmut Käutner (born 25 March 1908 in Düsseldorf, Germany; died 20 April 1980 in Castellina in Chianti, Italy) was a German film director active mainly in the 1940s and 1950s."
    },
    "reviewer": "Codex evidence inspection"
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Step 2: Germany  
Final answer: Germany
```

### donor_probe

**Exact model prompt**

```text
In which city or town was Gustaf Molander born?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer exactly:
Answer: <city or town>
```

**Model response**

```text
Answer: Helsinki
```

Semantic label: EXACT_CORRECT

Gate: PASS

Failure type: None

Format errors: []

**Per-field diagnosis**

```json
{
  "step1_diagnosis": null,
  "step2_diagnosis": {
    "semantic_label": "EXACT_CORRECT",
    "failure_type": null,
    "reason": "Complete target/alias match",
    "review_required": false
  },
  "final_diagnosis": {
    "semantic_label": "EXACT_CORRECT",
    "failure_type": null,
    "reason": "Complete target/alias match",
    "review_required": false
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Answer: Sweden
```

### injected

NOT RUN: not all three strict gates passed.

### Source and donor evidence

```json
{
  "supporting_facts": [
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
  ],
  "donor_supporting_facts": [
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
}
```

## f1a04d600bdb11eba7f7acde48001122

What is the place of birth of the director of film Dollar (1938 Film)?

```json
{
  "subject_A": "Dollar",
  "relation_r1": "director",
  "gold_B": "Gustaf Molander",
  "relation_r2": "place of birth",
  "gold_C": "Helsingfors",
  "injected_B_prime": "Helmut Käutner",
  "injected_C_prime": "Düsseldorf"
}
```

### baseline

**Exact model prompt**

```text
Question:
What is the place of birth of the director of film Dollar (1938 Film)?

Solve this in two steps.

Step 1 question:
Who directed "Dollar"?

Step 2 question:
Using the person you identified in Step 1, in which city or town was that person born?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer using exactly this format:
Step 1: <person>
Step 2: <city or town>
Final answer: <same answer as Step 2>
```

**Model response**

```text
Step 1: William A. Wellman  
Step 2: Chicago  
Final answer: Chicago
```

Semantic label: WRONG_LOCATION

Gate: FAIL

Failure type: wrong_entity

Format errors: []

**Per-field diagnosis**

```json
{
  "step1_diagnosis": {
    "semantic_label": "WRONG_ENTITY",
    "failure_type": "wrong_entity",
    "reason": "The response 'William A. Wellman' identifies a different person from the annotated target 'Gustaf Molander'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "Dollar (1938 film)",
      "sentence_id": 0,
      "text": "Dollar is a 1938 Swedish comedy film directed by Gustaf Molander and starring Ingrid Bergman, Georg Rydeberg and Tutta Rolf."
    },
    "reviewer": "Codex evidence inspection"
  },
  "step2_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Chicago' identifies a different location from the annotated target 'Helsingfors'; the saved supporting sentence explicitly establishes the target. This label is relative to the original question/gold chain; it makes no claim about whether the response is true of the incorrectly named Step 1 person.",
    "review_required": false,
    "review_evidence": {
      "title": "Gustaf Molander",
      "sentence_id": 4,
      "text": "Gustaf Molander was born in Helsingfors (now Helsinki) in the Grand Duchy of Finland (in the Russian Empire), where his father was working at the Swedish Theatre."
    },
    "reviewer": "Codex evidence inspection"
  },
  "final_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Chicago' identifies a different location from the annotated target 'Helsingfors'; the saved supporting sentence explicitly establishes the target. This label is relative to the original question/gold chain; it makes no claim about whether the response is true of the incorrectly named Step 1 person.",
    "review_required": false,
    "review_evidence": {
      "title": "Gustaf Molander",
      "sentence_id": 4,
      "text": "Gustaf Molander was born in Helsingfors (now Helsinki) in the Grand Duchy of Finland (in the Russian Empire), where his father was working at the Swedish Theatre."
    },
    "reviewer": "Codex evidence inspection"
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Step 1: John Ford  
Step 2: Wisconsin  
Final answer: Wisconsin
```

### oracle

**Exact model prompt**

```text
Question:
What is the place of birth of the director of film Dollar (1938 Film)?

We already know the correct answer to Step 1.

Confirmed Step 1 result:
The director of "Dollar" is Gustaf Molander.

Treat this intermediate result as correct.
This result is already established and fixed; use it as the premise for Step 2.
Do not verify it, replace it, or answer Step 1 again.
Do not repeat it as the Step 2 answer.

Now answer only the next question:

In which city or town was Gustaf Molander born?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer exactly:
Step 2: <city or town>
Final answer: <same answer as Step 2>
```

**Model response**

```text
Step 2: Stockholm  
Final answer: Stockholm
```

Semantic label: WRONG_LOCATION

Gate: FAIL

Failure type: knowledge_error

Format errors: []

**Per-field diagnosis**

```json
{
  "step1_diagnosis": null,
  "step2_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Stockholm' identifies a different location from the annotated target 'Helsingfors'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "Gustaf Molander",
      "sentence_id": 4,
      "text": "Gustaf Molander was born in Helsingfors (now Helsinki) in the Grand Duchy of Finland (in the Russian Empire), where his father was working at the Swedish Theatre."
    },
    "reviewer": "Codex evidence inspection"
  },
  "final_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Stockholm' identifies a different location from the annotated target 'Helsingfors'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "Gustaf Molander",
      "sentence_id": 4,
      "text": "Gustaf Molander was born in Helsingfors (now Helsinki) in the Grand Duchy of Finland (in the Russian Empire), where his father was working at the Swedish Theatre."
    },
    "reviewer": "Codex evidence inspection"
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Step 2: Stockholm, Sweden  
Final answer: Stockholm, Sweden
```

### donor_probe

**Exact model prompt**

```text
In which city or town was Helmut Käutner born?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer exactly:
Answer: <city or town>
```

**Model response**

```text
Answer: Berlin
```

Semantic label: WRONG_LOCATION

Gate: FAIL

Failure type: knowledge_error

Format errors: []

**Per-field diagnosis**

```json
{
  "step1_diagnosis": null,
  "step2_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Berlin' identifies a different location from the annotated target 'Düsseldorf'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "Helmut Käutner",
      "sentence_id": 0,
      "text": "Helmut Käutner (born 25 March 1908 in Düsseldorf, Germany; died 20 April 1980 in Castellina in Chianti, Italy) was a German film director active mainly in the 1940s and 1950s."
    },
    "reviewer": "Codex evidence inspection"
  },
  "final_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Berlin' identifies a different location from the annotated target 'Düsseldorf'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "Helmut Käutner",
      "sentence_id": 0,
      "text": "Helmut Käutner (born 25 March 1908 in Düsseldorf, Germany; died 20 April 1980 in Castellina in Chianti, Italy) was a German film director active mainly in the 1940s and 1950s."
    },
    "reviewer": "Codex evidence inspection"
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Answer: Germany
```

### injected

NOT RUN: not all three strict gates passed.

### Source and donor evidence

```json
{
  "supporting_facts": [
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
  ],
  "donor_supporting_facts": [
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
}
```

## e61479860bda11eba7f7acde48001122

What is the place of birth of the performer of song Pluto (Song)?

```json
{
  "subject_A": "Pluto",
  "relation_r1": "performer",
  "gold_B": "Björk",
  "relation_r2": "place of birth",
  "gold_C": "Reykjavík",
  "injected_B_prime": "Chuck Berry",
  "injected_C_prime": "St. Louis, Missouri"
}
```

### baseline

**Exact model prompt**

```text
Question:
What is the place of birth of the performer of song Pluto (Song)?

Solve this in two steps.

Step 1 question:
Who performed or recorded the song "Pluto"?

Step 2 question:
Using the person you identified in Step 1, in which city or town was that person born?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer using exactly this format:
Step 1: <person>
Step 2: <city or town>
Final answer: <same answer as Step 2>
```

**Model response**

```text
Step 1: The Weeknd  
Step 2: Sault Ste. Marie  
Final answer: Sault Ste. Marie
```

Semantic label: WRONG_LOCATION

Gate: FAIL

Failure type: wrong_entity

Format errors: []

**Per-field diagnosis**

```json
{
  "step1_diagnosis": {
    "semantic_label": "WRONG_ENTITY",
    "failure_type": "wrong_entity",
    "reason": "The response 'The Weeknd' identifies a different person from the annotated target 'Björk'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "Pluto (song)",
      "sentence_id": 0,
      "text": "\"Pluto\" is a song by Icelandic musician Björk."
    },
    "reviewer": "Codex evidence inspection"
  },
  "step2_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Sault Ste. Marie' identifies a different location from the annotated target 'Reykjavík'; the saved supporting sentence explicitly establishes the target. This label is relative to the original question/gold chain; it makes no claim about whether the response is true of the incorrectly named Step 1 person.",
    "review_required": false,
    "review_evidence": {
      "title": "Björk",
      "sentence_id": 2,
      "text": "Born and raised in Reykjavík, Björk began her music career at the age of 11 and first gained international recognition as the lead singer of the alternative rock band"
    },
    "reviewer": "Codex evidence inspection"
  },
  "final_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Sault Ste. Marie' identifies a different location from the annotated target 'Reykjavík'; the saved supporting sentence explicitly establishes the target. This label is relative to the original question/gold chain; it makes no claim about whether the response is true of the incorrectly named Step 1 person.",
    "review_required": false,
    "review_evidence": {
      "title": "Björk",
      "sentence_id": 2,
      "text": "Born and raised in Reykjavík, Björk began her music career at the age of 11 and first gained international recognition as the lead singer of the alternative rock band"
    },
    "reviewer": "Codex evidence inspection"
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Step 1: Pluto (song) → performer → Bruno Mars  
Step 2: Bruno Mars → place of birth → White Plains, New York  
Final answer: White Plains, New York
```

### oracle

**Exact model prompt**

```text
Question:
What is the place of birth of the performer of song Pluto (Song)?

We already know the correct answer to Step 1.

Confirmed Step 1 result:
The performer of the song "Pluto" is Björk.

Treat this intermediate result as correct.
This result is already established and fixed; use it as the premise for Step 2.
Do not verify it, replace it, or answer Step 1 again.
Do not repeat it as the Step 2 answer.

Now answer only the next question:

In which city or town was Björk born?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer exactly:
Step 2: <city or town>
Final answer: <same answer as Step 2>
```

**Model response**

```text
Step 2: Reykjavík  
Final answer: Reykjavík
```

Semantic label: EXACT_CORRECT

Gate: PASS

Failure type: None

Format errors: []

**Per-field diagnosis**

```json
{
  "step1_diagnosis": null,
  "step2_diagnosis": {
    "semantic_label": "EXACT_CORRECT",
    "failure_type": null,
    "reason": "Complete target/alias match",
    "review_required": false
  },
  "final_diagnosis": {
    "semantic_label": "EXACT_CORRECT",
    "failure_type": null,
    "reason": "Complete target/alias match",
    "review_required": false
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Step 2: Iceland  
Final answer: Iceland
```

### donor_probe

**Exact model prompt**

```text
In which city or town was Chuck Berry born?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer exactly:
Answer: <city or town>
```

**Model response**

```text
Answer: Rock Island
```

Semantic label: WRONG_LOCATION

Gate: FAIL

Failure type: knowledge_error

Format errors: []

**Per-field diagnosis**

```json
{
  "step1_diagnosis": null,
  "step2_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Rock Island' identifies a different location from the annotated target 'St. Louis, Missouri'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "Chuck Berry",
      "sentence_id": 4,
      "text": "Born into a middle-class African-American family in St. Louis, Missouri, Berry had an interest in music from an early age and gave his first public performance at Sumner High School."
    },
    "reviewer": "Codex evidence inspection"
  },
  "final_diagnosis": {
    "semantic_label": "WRONG_LOCATION",
    "failure_type": "knowledge_error",
    "reason": "The response 'Rock Island' identifies a different location from the annotated target 'St. Louis, Missouri'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "Chuck Berry",
      "sentence_id": 4,
      "text": "Born into a middle-class African-American family in St. Louis, Missouri, Berry had an interest in music from an early age and gave his first public performance at Sumner High School."
    },
    "reviewer": "Codex evidence inspection"
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Answer: Rock Island, Illinois
```

### injected

NOT RUN: not all three strict gates passed.

### Source and donor evidence

```json
{
  "supporting_facts": [
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
  ],
  "donor_supporting_facts": [
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
}
```

## 5b1e1f240bdc11eba7f7acde48001122

Who is the father of the director of film La Caída?

```json
{
  "subject_A": "La caída",
  "relation_r1": "director",
  "gold_B": "Leopoldo Torre Nilsson",
  "relation_r2": "father",
  "gold_C": "Leopoldo Torres Ríos",
  "injected_B_prime": "Armando Robles Godoy",
  "injected_C_prime": "Daniel Alomía Robles"
}
```

### baseline

**Exact model prompt**

```text
Question:
Who is the father of the director of film La Caída?

Solve this in two steps.

Step 1 question:
Who directed "La caída"?

Step 2 question:
Using the person you identified in Step 1, who was that person's father?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer using exactly this format:
Step 1: <person>
Step 2: <person>
Final answer: <same answer as Step 2>
```

**Model response**

```text
Step 1: Pablo Larrain  
Step 2: Pablo Larrain's father is not publicly known or relevant to the film industry. However, the question asks for the father of the director of "La caída", and Pablo Larrain's father is not a widely documented public figure in film.  

But upon correction: Pablo Larrain's father is actually **Luis Larrain**, a well-known Chilean filmmaker and director.  

Final correction:  

Step 1: Pablo Larrain  
Step 2: Luis Larrain  
Final answer: Luis Larrain
```

Semantic label: INVALID_OUTPUT

Gate: FAIL

Failure type: format_failure

Format errors: ["Expected exactly 3 nonempty lines", "Final answer: missing, empty, or out-of-order field"]

**Per-field diagnosis**

```json
{
  "step1_diagnosis": null,
  "step2_diagnosis": {
    "semantic_label": "INVALID_OUTPUT",
    "failure_type": "format_failure",
    "reason": "Malformed entity/value output or truncation",
    "review_required": false
  },
  "final_diagnosis": {
    "semantic_label": "INVALID_OUTPUT",
    "failure_type": "format_failure",
    "reason": "Malformed entity/value output or truncation",
    "review_required": false
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Step 1: Alonso Cánovas  
Step 2: José Cánovas  
Final answer: José Cánovas
```

### oracle

**Exact model prompt**

```text
Question:
Who is the father of the director of film La Caída?

We already know the correct answer to Step 1.

Confirmed Step 1 result:
The director of "La caída" is Leopoldo Torre Nilsson.

Treat this intermediate result as correct.
This result is already established and fixed; use it as the premise for Step 2.
Do not verify it, replace it, or answer Step 1 again.
Do not repeat it as the Step 2 answer.

Now answer only the next question:

Who was Leopoldo Torre Nilsson's father?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer exactly:
Step 2: <person>
Final answer: <same answer as Step 2>
```

**Model response**

```text
Step 2: José Torre Nilsson  
Final answer: José Torre Nilsson
```

Semantic label: WRONG_ENTITY

Gate: FAIL

Failure type: wrong_entity

Format errors: []

**Per-field diagnosis**

```json
{
  "step1_diagnosis": null,
  "step2_diagnosis": {
    "semantic_label": "WRONG_ENTITY",
    "failure_type": "wrong_entity",
    "reason": "The response 'José Torre Nilsson' identifies a different person from the annotated target 'Leopoldo Torres Ríos'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "Leopoldo Torre Nilsson",
      "sentence_id": 1,
      "text": "Born as Leopoldo Torres Nilsson (he later changed his paternal surname from Torres to Torre) was the son of Argentine pioneer film director Leopoldo Torres Ríos, with whom he collaborated between 1939 and 1949."
    },
    "reviewer": "Codex evidence inspection"
  },
  "final_diagnosis": {
    "semantic_label": "WRONG_ENTITY",
    "failure_type": "wrong_entity",
    "reason": "The response 'José Torre Nilsson' identifies a different person from the annotated target 'Leopoldo Torres Ríos'; the saved supporting sentence explicitly establishes the target.",
    "review_required": false,
    "review_evidence": {
      "title": "Leopoldo Torre Nilsson",
      "sentence_id": 1,
      "text": "Born as Leopoldo Torres Nilsson (he later changed his paternal surname from Torres to Torre) was the son of Argentine pioneer film director Leopoldo Torres Ríos, with whom he collaborated between 1939 and 1949."
    },
    "reviewer": "Codex evidence inspection"
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Step 2: Leopoldo Torre Nilsson

Final answer: Leopoldo Torre Nilsson
```

### donor_probe

**Exact model prompt**

```text
Who was Armando Robles Godoy's father?

Return only the requested entity/value in each field, without explanations or relation chains.

Answer exactly:
Answer: <person>
```

**Model response**

```text
Answer: <person>
```

Semantic label: INVALID_OUTPUT

Gate: FAIL

Failure type: format_failure

Format errors: ["Answer: unfilled placeholder"]

**Per-field diagnosis**

```json
{
  "step1_diagnosis": null,
  "step2_diagnosis": {
    "semantic_label": "INVALID_OUTPUT",
    "failure_type": "format_failure",
    "reason": "Malformed entity/value output or truncation",
    "review_required": false
  },
  "final_diagnosis": {
    "semantic_label": "INVALID_OUTPUT",
    "failure_type": "format_failure",
    "reason": "Malformed entity/value output or truncation",
    "review_required": false
  }
}
```

**Previous v2 response (read from saved log, not rerun)**

```text
Answer: Unknown
```

### injected

NOT RUN: not all three strict gates passed.

### Source and donor evidence

```json
{
  "supporting_facts": [
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
  ],
  "donor_supporting_facts": [
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
}
```