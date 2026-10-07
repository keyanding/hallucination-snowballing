# v3.6.0 pre-registration

Frozen before any inference. Synthetic opaque cases only; calibration 20, main 40; disjoint identifiers.
Calibration: 160 calls (8 per case), including formal ENTITY_LABEL. Main: 80 calls only after A–H pass. Total maximum 240. No auxiliary model calls.
A ≥38/40 direct lookups; B ≥19/20 C0; C ≥19/20 W0; D ≥19/20 swap; E ≥19/20 reversal invariant; F ≥18/20 UNKNOWN; G ≥159/160 permitted parses; H ≥19/20 entity-label invariant.
E/H require two permitted normalized-identical outputs, compared with same-case C0; correctness is separately reported.
Any A–H failure: STOP_ASSAY_INVALID, zero main calls. Main G1 ≥38/40 C, G2 ≥38/40 Cp, G3 ≥36/40 paired switches, G4 ≤2/40 Cp under C0, G5 ≤2/80 OTHER+INVALID. UNKNOWN reported separately.
Main failure: STOP_MAIN_ASSAY_INVALID; all pass: ASSAY_VALIDATED. No follow-up phases automatically.
Normalization: NFC, outer whitespace, one terminal period; no case folding, no extraction. Truncation INVALID; other well-formed Outcome_[A-Z][0-9]{2} is OTHER. Only exact C/Cp/UNKNOWN permitted.
Wilson 95% intervals for A_C, A_W, S; paired 5×5 transition table; unit 40 base cases. Unrun main rates are null.
Case seed 360; call shuffle seeds 360/361; no adjacent same-case calls. Greedy seed 42, cap 16, fresh chat, use_cache=False, no constrained output. No retuning or replacing cases.
Uniform instruction, frozen verbatim in all templates:
If the supplied working intermediate state has no matching downstream mapping, output UNKNOWN.
Model Qwen/Qwen3-4B-Instruct-2507, revision cdbee75f17c01a7cc42f958dc650907174af0554, same NF4 double quantization and BF16 stack as v3.5.1.
Permitted conclusion only: Under a validated synthetic state-dependent task, externally changing the intermediate state causes a predictable change in the downstream answer.
No claim about natural hallucination, internal mechanisms, SHAR, or arbitrary real tasks.
