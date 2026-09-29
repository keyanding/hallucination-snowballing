# V2 preregistered smoke protocol

This namespace preserves v1 and tests controlled relational composition with Qwen3-4B-Instruct-2507. No SHARS detector, uncertainty score, rejection threshold, or automatic resampling is used.

Execution order: environment record; native load/short-generation probe; NF4 if native lacks headroom; prepare 3–5 fixed candidates; all baseline probes; all oracle probes; all donor probes; inject only for pairs passing all three. Stop for human review after generating inspection and gate files. Do not search through further candidates after observing gate failures in this smoke run.

Native is considered comfortable only with at least 1 GiB of measured free VRAM after the short generation and without CPU/disk offload. A successful quantized CUDA kernel and trivial generation are required before NF4 experiments. Greedy decoding, max_new_tokens=128, seed=42, chat template, thinking disabled. CPU offload, if needed, must be explicitly reported.

Candidate selection is based on dataset structure/evidence, before model outcomes. Original questions must be compositional; parent/spouse shortcuts are excluded. Donor mappings must be supported by explicit dataset triples. Entity aliases must come from evidence or be separately reviewed; substring matching is not an entity gate. A novel third answer is not automatically a hallucination: unsupportedness and ambiguity require review. These constraints may reduce the eligible count to zero; that is a capability/identifiability result, not a propagation-rate result.

Primary label denominators use only injected eligible examples; missing classifications and invalid outputs are reported explicitly. Zero eligible examples yields null propagation/recovery/new-hallucination/reject rates, never 0%. Baseline, oracle, and donor success rates describe candidate selection; they do not demonstrate the intervention mechanism. Prompted use of a supplied entity is a controlled-state intervention, not an estimate of naturally arising hallucination frequency.
