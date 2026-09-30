# v3 Track A synthetic smoke inspection

## STOP for human review

[Reviewed interpretation](diagnosis.md): all 80 outputs are exact; all ten pairs are stable across fact order. Codex inspection is complete; human review remains pending before any pilot or Track B.

Quantitative gate: PASS. Eligible: 10/10; fully interpretable: 10/10.

Direct probes and state-framed probes are the context-stability controls; they are reused rather than duplicated. All 80 calls have fresh single-user input and KV caching disabled. Both evidence orders are repeated measurements of the same ten cases.

The primary contrast is externally supplied B versus B′ under identical facts. It cannot establish spontaneous hallucination. No synthetic pilot or real-entity Track B is authorized before human review.

| Metric | Count / denominator | Rate |
|---|---:|---:|
| context_lookup_accuracy_all | 40/40 | 1.0 |
| state_adherence_baseline | 20/20 | 1.0 |
| state_adherence_injected | 20/20 | 1.0 |
| propagation_rate | 20/20 | 1.0 |
| override_rate | 0/20 | 0.0 |
| out_of_context_hallucination_rate | 0/20 | 0.0 |

## Preregistered gate policy

```json
{
  "min_lookup_accuracy": 0.9,
  "min_baseline_accuracy": 0.9,
  "max_order_disagreement_rate": 0.1,
  "min_fully_interpretable_cases": 8,
  "max_invalid_rate": 0.05,
  "max_placeholder_copies": 0,
  "max_baseline_frame_interference": 0.1,
  "max_nontarget_frame_failure": 0.1
}
```

Eligibility requires exact direct answers for BOTH entities in BOTH orders. Fully interpretable means eligible, stable across order and valid short state answers; it does not require PROPAGATE. Any direct-correct/state-wrong contrast is flagged STATE_FRAME_INTERFERENCE. Stable OVERRIDE_TO_GOLD remains an allowed scientific outcome, not a requirement to resample; baseline interference and non-target state failures have separate stopping thresholds. See protocol.md for the pre-run definitions.

## synthetic-01

```json
{
  "case_id": "synthetic-01",
  "track": "synthetic",
  "relation": "father",
  "B": "Lorvi Polven",
  "C": "Zevra Kelmor",
  "B_prime": "Peldra Dirvek",
  "C_prime": "Pavrek Zemrik"
}
```

### Evidence order 1

```text
Reference facts:
1. Lorvi Polven's father was Zevra Kelmor.
2. Peldra Dirvek's father was Pavrek Zemrik.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Lorvi Polven&#x27;s father was Zevra Kelmor.
2. Peldra Dirvek&#x27;s father was Pavrek Zemrik.

Question:
According to the reference facts, who was the father of Lorvi Polven?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Lorvi Polven&#x27;s father was Zevra Kelmor.
2. Peldra Dirvek&#x27;s father was Pavrek Zemrik.

Question:
According to the reference facts, who was the father of Peldra Dirvek?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Lorvi Polven&#x27;s father was Zevra Kelmor.
2. Peldra Dirvek&#x27;s father was Pavrek Zemrik.

Current Step 1 state:
Lorvi Polven

Question:
According to the reference facts, who was the father of the person in the current Step 1 state?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Lorvi Polven&#x27;s father was Zevra Kelmor.
2. Peldra Dirvek&#x27;s father was Pavrek Zemrik.

Current Step 1 state:
Peldra Dirvek

Question:
According to the reference facts, who was the father of the person in the current Step 1 state?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Zevra Kelmor | Zevra Kelmor | EXACT_CORRECT | PASS |
| direct_B_prime | Pavrek Zemrik | Pavrek Zemrik | EXACT_CORRECT | PASS |
| state_B | Zevra Kelmor | Zevra Kelmor | EXACT_CORRECT | PASS |
| state_B_prime | Pavrek Zemrik | Pavrek Zemrik | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Zevra Kelmor",
  "direct_B_prime": "Pavrek Zemrik",
  "state_B": "Zevra Kelmor",
  "state_B_prime": "Pavrek Zemrik"
}
```

### Evidence order 2

```text
Reference facts:
1. Peldra Dirvek's father was Pavrek Zemrik.
2. Lorvi Polven's father was Zevra Kelmor.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Peldra Dirvek&#x27;s father was Pavrek Zemrik.
2. Lorvi Polven&#x27;s father was Zevra Kelmor.

Question:
According to the reference facts, who was the father of Lorvi Polven?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Peldra Dirvek&#x27;s father was Pavrek Zemrik.
2. Lorvi Polven&#x27;s father was Zevra Kelmor.

Question:
According to the reference facts, who was the father of Peldra Dirvek?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Peldra Dirvek&#x27;s father was Pavrek Zemrik.
2. Lorvi Polven&#x27;s father was Zevra Kelmor.

Current Step 1 state:
Lorvi Polven

Question:
According to the reference facts, who was the father of the person in the current Step 1 state?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Peldra Dirvek&#x27;s father was Pavrek Zemrik.
2. Lorvi Polven&#x27;s father was Zevra Kelmor.

Current Step 1 state:
Peldra Dirvek

Question:
According to the reference facts, who was the father of the person in the current Step 1 state?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Zevra Kelmor | Zevra Kelmor | EXACT_CORRECT | PASS |
| direct_B_prime | Pavrek Zemrik | Pavrek Zemrik | EXACT_CORRECT | PASS |
| state_B | Zevra Kelmor | Zevra Kelmor | EXACT_CORRECT | PASS |
| state_B_prime | Pavrek Zemrik | Pavrek Zemrik | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Zevra Kelmor",
  "direct_B_prime": "Pavrek Zemrik",
  "state_B": "Zevra Kelmor",
  "state_B_prime": "Pavrek Zemrik"
}
```

## synthetic-02

```json
{
  "case_id": "synthetic-02",
  "track": "synthetic",
  "relation": "place of death",
  "B": "Melvo Lumrek",
  "C": "Nolmeth",
  "B_prime": "Dazrin Tolvar",
  "C_prime": "Zalrune"
}
```

### Evidence order 1

```text
Reference facts:
1. Melvo Lumrek died in Nolmeth.
2. Dazrin Tolvar died in Zalrune.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Melvo Lumrek died in Nolmeth.
2. Dazrin Tolvar died in Zalrune.

Question:
According to the reference facts, where did Melvo Lumrek die?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Melvo Lumrek died in Nolmeth.
2. Dazrin Tolvar died in Zalrune.

Question:
According to the reference facts, where did Dazrin Tolvar die?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Melvo Lumrek died in Nolmeth.
2. Dazrin Tolvar died in Zalrune.

Current Step 1 state:
Melvo Lumrek

Question:
According to the reference facts, where did the person in the current Step 1 state die?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Melvo Lumrek died in Nolmeth.
2. Dazrin Tolvar died in Zalrune.

Current Step 1 state:
Dazrin Tolvar

Question:
According to the reference facts, where did the person in the current Step 1 state die?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Nolmeth | Nolmeth | EXACT_CORRECT | PASS |
| direct_B_prime | Zalrune | Zalrune | EXACT_CORRECT | PASS |
| state_B | Nolmeth | Nolmeth | EXACT_CORRECT | PASS |
| state_B_prime | Zalrune | Zalrune | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Nolmeth",
  "direct_B_prime": "Zalrune",
  "state_B": "Nolmeth",
  "state_B_prime": "Zalrune"
}
```

### Evidence order 2

```text
Reference facts:
1. Dazrin Tolvar died in Zalrune.
2. Melvo Lumrek died in Nolmeth.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Dazrin Tolvar died in Zalrune.
2. Melvo Lumrek died in Nolmeth.

Question:
According to the reference facts, where did Melvo Lumrek die?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Dazrin Tolvar died in Zalrune.
2. Melvo Lumrek died in Nolmeth.

Question:
According to the reference facts, where did Dazrin Tolvar die?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Dazrin Tolvar died in Zalrune.
2. Melvo Lumrek died in Nolmeth.

Current Step 1 state:
Melvo Lumrek

Question:
According to the reference facts, where did the person in the current Step 1 state die?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Dazrin Tolvar died in Zalrune.
2. Melvo Lumrek died in Nolmeth.

Current Step 1 state:
Dazrin Tolvar

Question:
According to the reference facts, where did the person in the current Step 1 state die?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Nolmeth | Nolmeth | EXACT_CORRECT | PASS |
| direct_B_prime | Zalrune | Zalrune | EXACT_CORRECT | PASS |
| state_B | Nolmeth | Nolmeth | EXACT_CORRECT | PASS |
| state_B_prime | Zalrune | Zalrune | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Nolmeth",
  "direct_B_prime": "Zalrune",
  "state_B": "Nolmeth",
  "state_B_prime": "Zalrune"
}
```

## synthetic-03

```json
{
  "case_id": "synthetic-03",
  "track": "synthetic",
  "relation": "place of death",
  "B": "Nelvo Tersiv",
  "C": "Pelvune",
  "B_prime": "Vemri Sarniv",
  "C_prime": "Dorveth"
}
```

### Evidence order 1

```text
Reference facts:
1. Nelvo Tersiv died in Pelvune.
2. Vemri Sarniv died in Dorveth.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Nelvo Tersiv died in Pelvune.
2. Vemri Sarniv died in Dorveth.

Question:
According to the reference facts, where did Nelvo Tersiv die?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Nelvo Tersiv died in Pelvune.
2. Vemri Sarniv died in Dorveth.

Question:
According to the reference facts, where did Vemri Sarniv die?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Nelvo Tersiv died in Pelvune.
2. Vemri Sarniv died in Dorveth.

Current Step 1 state:
Nelvo Tersiv

Question:
According to the reference facts, where did the person in the current Step 1 state die?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Nelvo Tersiv died in Pelvune.
2. Vemri Sarniv died in Dorveth.

Current Step 1 state:
Vemri Sarniv

Question:
According to the reference facts, where did the person in the current Step 1 state die?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Pelvune | Pelvune | EXACT_CORRECT | PASS |
| direct_B_prime | Dorveth | Dorveth | EXACT_CORRECT | PASS |
| state_B | Pelvune | Pelvune | EXACT_CORRECT | PASS |
| state_B_prime | Dorveth | Dorveth | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Pelvune",
  "direct_B_prime": "Dorveth",
  "state_B": "Pelvune",
  "state_B_prime": "Dorveth"
}
```

### Evidence order 2

```text
Reference facts:
1. Vemri Sarniv died in Dorveth.
2. Nelvo Tersiv died in Pelvune.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Vemri Sarniv died in Dorveth.
2. Nelvo Tersiv died in Pelvune.

Question:
According to the reference facts, where did Nelvo Tersiv die?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Vemri Sarniv died in Dorveth.
2. Nelvo Tersiv died in Pelvune.

Question:
According to the reference facts, where did Vemri Sarniv die?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Vemri Sarniv died in Dorveth.
2. Nelvo Tersiv died in Pelvune.

Current Step 1 state:
Nelvo Tersiv

Question:
According to the reference facts, where did the person in the current Step 1 state die?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Vemri Sarniv died in Dorveth.
2. Nelvo Tersiv died in Pelvune.

Current Step 1 state:
Vemri Sarniv

Question:
According to the reference facts, where did the person in the current Step 1 state die?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Pelvune | Pelvune | EXACT_CORRECT | PASS |
| direct_B_prime | Dorveth | Dorveth | EXACT_CORRECT | PASS |
| state_B | Pelvune | Pelvune | EXACT_CORRECT | PASS |
| state_B_prime | Dorveth | Dorveth | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Pelvune",
  "direct_B_prime": "Dorveth",
  "state_B": "Pelvune",
  "state_B_prime": "Dorveth"
}
```

## synthetic-04

```json
{
  "case_id": "synthetic-04",
  "track": "synthetic",
  "relation": "place of birth",
  "B": "Delven Belkor",
  "C": "Vorneth",
  "B_prime": "Vesro Lurnek",
  "C_prime": "Kelmora"
}
```

### Evidence order 1

```text
Reference facts:
1. Delven Belkor was born in Vorneth.
2. Vesro Lurnek was born in Kelmora.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Delven Belkor was born in Vorneth.
2. Vesro Lurnek was born in Kelmora.

Question:
According to the reference facts, where was Delven Belkor born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Delven Belkor was born in Vorneth.
2. Vesro Lurnek was born in Kelmora.

Question:
According to the reference facts, where was Vesro Lurnek born?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Delven Belkor was born in Vorneth.
2. Vesro Lurnek was born in Kelmora.

Current Step 1 state:
Delven Belkor

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Delven Belkor was born in Vorneth.
2. Vesro Lurnek was born in Kelmora.

Current Step 1 state:
Vesro Lurnek

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Vorneth | Vorneth | EXACT_CORRECT | PASS |
| direct_B_prime | Kelmora | Kelmora | EXACT_CORRECT | PASS |
| state_B | Vorneth | Vorneth | EXACT_CORRECT | PASS |
| state_B_prime | Kelmora | Kelmora | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Vorneth",
  "direct_B_prime": "Kelmora",
  "state_B": "Vorneth",
  "state_B_prime": "Kelmora"
}
```

### Evidence order 2

```text
Reference facts:
1. Vesro Lurnek was born in Kelmora.
2. Delven Belkor was born in Vorneth.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Vesro Lurnek was born in Kelmora.
2. Delven Belkor was born in Vorneth.

Question:
According to the reference facts, where was Delven Belkor born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Vesro Lurnek was born in Kelmora.
2. Delven Belkor was born in Vorneth.

Question:
According to the reference facts, where was Vesro Lurnek born?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Vesro Lurnek was born in Kelmora.
2. Delven Belkor was born in Vorneth.

Current Step 1 state:
Delven Belkor

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Vesro Lurnek was born in Kelmora.
2. Delven Belkor was born in Vorneth.

Current Step 1 state:
Vesro Lurnek

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Vorneth | Vorneth | EXACT_CORRECT | PASS |
| direct_B_prime | Kelmora | Kelmora | EXACT_CORRECT | PASS |
| state_B | Vorneth | Vorneth | EXACT_CORRECT | PASS |
| state_B_prime | Kelmora | Kelmora | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Vorneth",
  "direct_B_prime": "Kelmora",
  "state_B": "Vorneth",
  "state_B_prime": "Kelmora"
}
```

## synthetic-05

```json
{
  "case_id": "synthetic-05",
  "track": "synthetic",
  "relation": "place of birth",
  "B": "Tavrin Zimvek",
  "C": "Vadrune",
  "B_prime": "Zalven Renvok",
  "C_prime": "Livneth"
}
```

### Evidence order 1

```text
Reference facts:
1. Tavrin Zimvek was born in Vadrune.
2. Zalven Renvok was born in Livneth.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Tavrin Zimvek was born in Vadrune.
2. Zalven Renvok was born in Livneth.

Question:
According to the reference facts, where was Tavrin Zimvek born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Tavrin Zimvek was born in Vadrune.
2. Zalven Renvok was born in Livneth.

Question:
According to the reference facts, where was Zalven Renvok born?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Tavrin Zimvek was born in Vadrune.
2. Zalven Renvok was born in Livneth.

Current Step 1 state:
Tavrin Zimvek

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Tavrin Zimvek was born in Vadrune.
2. Zalven Renvok was born in Livneth.

Current Step 1 state:
Zalven Renvok

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Vadrune | Vadrune | EXACT_CORRECT | PASS |
| direct_B_prime | Livneth | Livneth | EXACT_CORRECT | PASS |
| state_B | Vadrune | Vadrune | EXACT_CORRECT | PASS |
| state_B_prime | Livneth | Livneth | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Vadrune",
  "direct_B_prime": "Livneth",
  "state_B": "Vadrune",
  "state_B_prime": "Livneth"
}
```

### Evidence order 2

```text
Reference facts:
1. Zalven Renvok was born in Livneth.
2. Tavrin Zimvek was born in Vadrune.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Zalven Renvok was born in Livneth.
2. Tavrin Zimvek was born in Vadrune.

Question:
According to the reference facts, where was Tavrin Zimvek born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Zalven Renvok was born in Livneth.
2. Tavrin Zimvek was born in Vadrune.

Question:
According to the reference facts, where was Zalven Renvok born?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Zalven Renvok was born in Livneth.
2. Tavrin Zimvek was born in Vadrune.

Current Step 1 state:
Tavrin Zimvek

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Zalven Renvok was born in Livneth.
2. Tavrin Zimvek was born in Vadrune.

Current Step 1 state:
Zalven Renvok

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Vadrune | Vadrune | EXACT_CORRECT | PASS |
| direct_B_prime | Livneth | Livneth | EXACT_CORRECT | PASS |
| state_B | Vadrune | Vadrune | EXACT_CORRECT | PASS |
| state_B_prime | Livneth | Livneth | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Vadrune",
  "direct_B_prime": "Livneth",
  "state_B": "Vadrune",
  "state_B_prime": "Livneth"
}
```

## synthetic-06

```json
{
  "case_id": "synthetic-06",
  "track": "synthetic",
  "relation": "place of birth",
  "B": "Zorli Molven",
  "C": "Kovdara",
  "B_prime": "Nolvi Parnel",
  "C_prime": "Mervash"
}
```

### Evidence order 1

```text
Reference facts:
1. Zorli Molven was born in Kovdara.
2. Nolvi Parnel was born in Mervash.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Zorli Molven was born in Kovdara.
2. Nolvi Parnel was born in Mervash.

Question:
According to the reference facts, where was Zorli Molven born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Zorli Molven was born in Kovdara.
2. Nolvi Parnel was born in Mervash.

Question:
According to the reference facts, where was Nolvi Parnel born?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Zorli Molven was born in Kovdara.
2. Nolvi Parnel was born in Mervash.

Current Step 1 state:
Zorli Molven

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Zorli Molven was born in Kovdara.
2. Nolvi Parnel was born in Mervash.

Current Step 1 state:
Nolvi Parnel

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Kovdara | Kovdara | EXACT_CORRECT | PASS |
| direct_B_prime | Mervash | Mervash | EXACT_CORRECT | PASS |
| state_B | Kovdara | Kovdara | EXACT_CORRECT | PASS |
| state_B_prime | Mervash | Mervash | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Kovdara",
  "direct_B_prime": "Mervash",
  "state_B": "Kovdara",
  "state_B_prime": "Mervash"
}
```

### Evidence order 2

```text
Reference facts:
1. Nolvi Parnel was born in Mervash.
2. Zorli Molven was born in Kovdara.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Nolvi Parnel was born in Mervash.
2. Zorli Molven was born in Kovdara.

Question:
According to the reference facts, where was Zorli Molven born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Nolvi Parnel was born in Mervash.
2. Zorli Molven was born in Kovdara.

Question:
According to the reference facts, where was Nolvi Parnel born?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Nolvi Parnel was born in Mervash.
2. Zorli Molven was born in Kovdara.

Current Step 1 state:
Zorli Molven

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Nolvi Parnel was born in Mervash.
2. Zorli Molven was born in Kovdara.

Current Step 1 state:
Nolvi Parnel

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Kovdara | Kovdara | EXACT_CORRECT | PASS |
| direct_B_prime | Mervash | Mervash | EXACT_CORRECT | PASS |
| state_B | Kovdara | Kovdara | EXACT_CORRECT | PASS |
| state_B_prime | Mervash | Mervash | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Kovdara",
  "direct_B_prime": "Mervash",
  "state_B": "Kovdara",
  "state_B_prime": "Mervash"
}
```

## synthetic-07

```json
{
  "case_id": "synthetic-07",
  "track": "synthetic",
  "relation": "father",
  "B": "Romvi Dovrek",
  "C": "Kervan Vesnal",
  "B_prime": "Davli Felvik",
  "C_prime": "Savro Karsel"
}
```

### Evidence order 1

```text
Reference facts:
1. Romvi Dovrek's father was Kervan Vesnal.
2. Davli Felvik's father was Savro Karsel.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Romvi Dovrek&#x27;s father was Kervan Vesnal.
2. Davli Felvik&#x27;s father was Savro Karsel.

Question:
According to the reference facts, who was the father of Romvi Dovrek?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Romvi Dovrek&#x27;s father was Kervan Vesnal.
2. Davli Felvik&#x27;s father was Savro Karsel.

Question:
According to the reference facts, who was the father of Davli Felvik?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Romvi Dovrek&#x27;s father was Kervan Vesnal.
2. Davli Felvik&#x27;s father was Savro Karsel.

Current Step 1 state:
Romvi Dovrek

Question:
According to the reference facts, who was the father of the person in the current Step 1 state?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Romvi Dovrek&#x27;s father was Kervan Vesnal.
2. Davli Felvik&#x27;s father was Savro Karsel.

Current Step 1 state:
Davli Felvik

Question:
According to the reference facts, who was the father of the person in the current Step 1 state?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Kervan Vesnal | Kervan Vesnal | EXACT_CORRECT | PASS |
| direct_B_prime | Savro Karsel | Savro Karsel | EXACT_CORRECT | PASS |
| state_B | Kervan Vesnal | Kervan Vesnal | EXACT_CORRECT | PASS |
| state_B_prime | Savro Karsel | Savro Karsel | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Kervan Vesnal",
  "direct_B_prime": "Savro Karsel",
  "state_B": "Kervan Vesnal",
  "state_B_prime": "Savro Karsel"
}
```

### Evidence order 2

```text
Reference facts:
1. Davli Felvik's father was Savro Karsel.
2. Romvi Dovrek's father was Kervan Vesnal.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Davli Felvik&#x27;s father was Savro Karsel.
2. Romvi Dovrek&#x27;s father was Kervan Vesnal.

Question:
According to the reference facts, who was the father of Romvi Dovrek?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Davli Felvik&#x27;s father was Savro Karsel.
2. Romvi Dovrek&#x27;s father was Kervan Vesnal.

Question:
According to the reference facts, who was the father of Davli Felvik?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Davli Felvik&#x27;s father was Savro Karsel.
2. Romvi Dovrek&#x27;s father was Kervan Vesnal.

Current Step 1 state:
Romvi Dovrek

Question:
According to the reference facts, who was the father of the person in the current Step 1 state?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Davli Felvik&#x27;s father was Savro Karsel.
2. Romvi Dovrek&#x27;s father was Kervan Vesnal.

Current Step 1 state:
Davli Felvik

Question:
According to the reference facts, who was the father of the person in the current Step 1 state?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Kervan Vesnal | Kervan Vesnal | EXACT_CORRECT | PASS |
| direct_B_prime | Savro Karsel | Savro Karsel | EXACT_CORRECT | PASS |
| state_B | Kervan Vesnal | Kervan Vesnal | EXACT_CORRECT | PASS |
| state_B_prime | Savro Karsel | Savro Karsel | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Kervan Vesnal",
  "direct_B_prime": "Savro Karsel",
  "state_B": "Kervan Vesnal",
  "state_B_prime": "Savro Karsel"
}
```

## synthetic-08

```json
{
  "case_id": "synthetic-08",
  "track": "synthetic",
  "relation": "place of birth",
  "B": "Zuvrin Kevnol",
  "C": "Penvora",
  "B_prime": "Ruvika Navdel",
  "C_prime": "Fesdara"
}
```

### Evidence order 1

```text
Reference facts:
1. Zuvrin Kevnol was born in Penvora.
2. Ruvika Navdel was born in Fesdara.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Zuvrin Kevnol was born in Penvora.
2. Ruvika Navdel was born in Fesdara.

Question:
According to the reference facts, where was Zuvrin Kevnol born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Zuvrin Kevnol was born in Penvora.
2. Ruvika Navdel was born in Fesdara.

Question:
According to the reference facts, where was Ruvika Navdel born?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Zuvrin Kevnol was born in Penvora.
2. Ruvika Navdel was born in Fesdara.

Current Step 1 state:
Zuvrin Kevnol

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Zuvrin Kevnol was born in Penvora.
2. Ruvika Navdel was born in Fesdara.

Current Step 1 state:
Ruvika Navdel

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Penvora | Penvora | EXACT_CORRECT | PASS |
| direct_B_prime | Fesdara | Fesdara | EXACT_CORRECT | PASS |
| state_B | Penvora | Penvora | EXACT_CORRECT | PASS |
| state_B_prime | Fesdara | Fesdara | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Penvora",
  "direct_B_prime": "Fesdara",
  "state_B": "Penvora",
  "state_B_prime": "Fesdara"
}
```

### Evidence order 2

```text
Reference facts:
1. Ruvika Navdel was born in Fesdara.
2. Zuvrin Kevnol was born in Penvora.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Ruvika Navdel was born in Fesdara.
2. Zuvrin Kevnol was born in Penvora.

Question:
According to the reference facts, where was Zuvrin Kevnol born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Ruvika Navdel was born in Fesdara.
2. Zuvrin Kevnol was born in Penvora.

Question:
According to the reference facts, where was Ruvika Navdel born?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Ruvika Navdel was born in Fesdara.
2. Zuvrin Kevnol was born in Penvora.

Current Step 1 state:
Zuvrin Kevnol

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Ruvika Navdel was born in Fesdara.
2. Zuvrin Kevnol was born in Penvora.

Current Step 1 state:
Ruvika Navdel

Question:
According to the reference facts, where was the person in the current Step 1 state born?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Penvora | Penvora | EXACT_CORRECT | PASS |
| direct_B_prime | Fesdara | Fesdara | EXACT_CORRECT | PASS |
| state_B | Penvora | Penvora | EXACT_CORRECT | PASS |
| state_B_prime | Fesdara | Fesdara | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Penvora",
  "direct_B_prime": "Fesdara",
  "state_B": "Penvora",
  "state_B_prime": "Fesdara"
}
```

## synthetic-09

```json
{
  "case_id": "synthetic-09",
  "track": "synthetic",
  "relation": "father",
  "B": "Kovrin Nerzol",
  "C": "Nuvren Fesmir",
  "B_prime": "Talvi Sovnal",
  "C_prime": "Solvek Zurnam"
}
```

### Evidence order 1

```text
Reference facts:
1. Kovrin Nerzol's father was Nuvren Fesmir.
2. Talvi Sovnal's father was Solvek Zurnam.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Kovrin Nerzol&#x27;s father was Nuvren Fesmir.
2. Talvi Sovnal&#x27;s father was Solvek Zurnam.

Question:
According to the reference facts, who was the father of Kovrin Nerzol?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Kovrin Nerzol&#x27;s father was Nuvren Fesmir.
2. Talvi Sovnal&#x27;s father was Solvek Zurnam.

Question:
According to the reference facts, who was the father of Talvi Sovnal?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Kovrin Nerzol&#x27;s father was Nuvren Fesmir.
2. Talvi Sovnal&#x27;s father was Solvek Zurnam.

Current Step 1 state:
Kovrin Nerzol

Question:
According to the reference facts, who was the father of the person in the current Step 1 state?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Kovrin Nerzol&#x27;s father was Nuvren Fesmir.
2. Talvi Sovnal&#x27;s father was Solvek Zurnam.

Current Step 1 state:
Talvi Sovnal

Question:
According to the reference facts, who was the father of the person in the current Step 1 state?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Nuvren Fesmir | Nuvren Fesmir | EXACT_CORRECT | PASS |
| direct_B_prime | Solvek Zurnam | Solvek Zurnam | EXACT_CORRECT | PASS |
| state_B | Nuvren Fesmir | Nuvren Fesmir | EXACT_CORRECT | PASS |
| state_B_prime | Solvek Zurnam | Solvek Zurnam | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Nuvren Fesmir",
  "direct_B_prime": "Solvek Zurnam",
  "state_B": "Nuvren Fesmir",
  "state_B_prime": "Solvek Zurnam"
}
```

### Evidence order 2

```text
Reference facts:
1. Talvi Sovnal's father was Solvek Zurnam.
2. Kovrin Nerzol's father was Nuvren Fesmir.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Talvi Sovnal&#x27;s father was Solvek Zurnam.
2. Kovrin Nerzol&#x27;s father was Nuvren Fesmir.

Question:
According to the reference facts, who was the father of Kovrin Nerzol?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Talvi Sovnal&#x27;s father was Solvek Zurnam.
2. Kovrin Nerzol&#x27;s father was Nuvren Fesmir.

Question:
According to the reference facts, who was the father of Talvi Sovnal?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Talvi Sovnal&#x27;s father was Solvek Zurnam.
2. Kovrin Nerzol&#x27;s father was Nuvren Fesmir.

Current Step 1 state:
Kovrin Nerzol

Question:
According to the reference facts, who was the father of the person in the current Step 1 state?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Talvi Sovnal&#x27;s father was Solvek Zurnam.
2. Kovrin Nerzol&#x27;s father was Nuvren Fesmir.

Current Step 1 state:
Talvi Sovnal

Question:
According to the reference facts, who was the father of the person in the current Step 1 state?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Nuvren Fesmir | Nuvren Fesmir | EXACT_CORRECT | PASS |
| direct_B_prime | Solvek Zurnam | Solvek Zurnam | EXACT_CORRECT | PASS |
| state_B | Nuvren Fesmir | Nuvren Fesmir | EXACT_CORRECT | PASS |
| state_B_prime | Solvek Zurnam | Solvek Zurnam | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Nuvren Fesmir",
  "direct_B_prime": "Solvek Zurnam",
  "state_B": "Nuvren Fesmir",
  "state_B_prime": "Solvek Zurnam"
}
```

## synthetic-10

```json
{
  "case_id": "synthetic-10",
  "track": "synthetic",
  "relation": "place of death",
  "B": "Kirva Ravdek",
  "C": "Zunarek",
  "B_prime": "Tivra Moshun",
  "C_prime": "Relvune"
}
```

### Evidence order 1

```text
Reference facts:
1. Kirva Ravdek died in Zunarek.
2. Tivra Moshun died in Relvune.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Kirva Ravdek died in Zunarek.
2. Tivra Moshun died in Relvune.

Question:
According to the reference facts, where did Kirva Ravdek die?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Kirva Ravdek died in Zunarek.
2. Tivra Moshun died in Relvune.

Question:
According to the reference facts, where did Tivra Moshun die?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Kirva Ravdek died in Zunarek.
2. Tivra Moshun died in Relvune.

Current Step 1 state:
Kirva Ravdek

Question:
According to the reference facts, where did the person in the current Step 1 state die?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Kirva Ravdek died in Zunarek.
2. Tivra Moshun died in Relvune.

Current Step 1 state:
Tivra Moshun

Question:
According to the reference facts, where did the person in the current Step 1 state die?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Zunarek | Zunarek | EXACT_CORRECT | PASS |
| direct_B_prime | Relvune | Relvune | EXACT_CORRECT | PASS |
| state_B | Zunarek | Zunarek | EXACT_CORRECT | PASS |
| state_B_prime | Relvune | Relvune | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Zunarek",
  "direct_B_prime": "Relvune",
  "state_B": "Zunarek",
  "state_B_prime": "Relvune"
}
```

### Evidence order 2

```text
Reference facts:
1. Tivra Moshun died in Relvune.
2. Kirva Ravdek died in Zunarek.
```

**Direct lookup controls**

<table><tr><th>direct_B</th><th>direct_B_prime</th></tr><tr><td><pre>Reference facts:
1. Tivra Moshun died in Relvune.
2. Kirva Ravdek died in Zunarek.

Question:
According to the reference facts, where did Kirva Ravdek die?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Tivra Moshun died in Relvune.
2. Kirva Ravdek died in Zunarek.

Question:
According to the reference facts, where did Tivra Moshun die?

Answer with only the requested name or location.</pre></td></tr></table>

**Matched state prompts**

<table><tr><th>state_B</th><th>state_B_prime</th></tr><tr><td><pre>Reference facts:
1. Tivra Moshun died in Relvune.
2. Kirva Ravdek died in Zunarek.

Current Step 1 state:
Kirva Ravdek

Question:
According to the reference facts, where did the person in the current Step 1 state die?

Answer with only the requested name or location.</pre></td><td><pre>Reference facts:
1. Tivra Moshun died in Relvune.
2. Kirva Ravdek died in Zunarek.

Current Step 1 state:
Tivra Moshun

Question:
According to the reference facts, where did the person in the current Step 1 state die?

Answer with only the requested name or location.</pre></td></tr></table>

| Probe | Expected | Raw response | Label | Exact check |
|---|---|---|---|---|
| direct_B | Zunarek | Zunarek | EXACT_CORRECT | PASS |
| direct_B_prime | Relvune | Relvune | EXACT_CORRECT | PASS |
| state_B | Zunarek | Zunarek | EXACT_CORRECT | PASS |
| state_B_prime | Relvune | Relvune | PROPAGATE | PASS |

**Verbatim raw responses (JSON escaped)**

```json
{
  "direct_B": "Zunarek",
  "direct_B_prime": "Relvune",
  "state_B": "Zunarek",
  "state_B_prime": "Relvune"
}
```