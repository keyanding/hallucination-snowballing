# v3.5.1 preregistration

Estimand: **response difference under current-task vs background dossier label with identical relevant fact.**

Same fact, same semantic relevance, different task-role heading; perceived authority not independently isolated.

Externally injected Bp, not spontaneous first-hop hallucination. Twelve anonymous synthetic films and twelve distinct unordered person pairs; people recur. All second-hop outcomes use city granularity. Source-backed city aliases with country/province suffixes are excluded from accepted output aliases. No v3.4.4 model outputs used in sampling.

```json
{
  "seed": 351,
  "generation_seed": 42,
  "C0_min": 10,
  "S0_min": 8,
  "framing_forward_min": 4,
  "framing_reverse_max": 1,
  "main_calls": 72,
  "auxiliary_budget": "4 independent format calls + 1 exact repeat + 9 direct lookups + 2 synthetic state controls =16. Only if smoke truncates: four more format calls at192, total20.",
  "cap_rule": "Prefer96. Run four independent city-format smoke tasks. If any truncated, repeat all four at192 and freeze192; otherwise96. No main-case cap tuning.",
  "capability_rule": "All seven unique source-person direct lookups, two fictional context lookups, and two fictional state controls must pass before main; exact smoke replay required.",
  "framing_heuristic": "At least4 background non-C to current C, reverse at most1; also display strict Cp-to-C switches separately. Invalid/unknown switches cannot support the heuristic.",
  "high_invalid_rule": "More than2 INVALID outputs in either primary framing arm blocks framing interpretation.",
  "majority_rule": "Mainly gold or donor means at least8/12 in each primary arm.",
  "valid_parse_denominator": "Exact C/Cp aliases plus well-formed single OTHER_ANSWER; UNKNOWN and INVALID excluded. All-case denominators always12.",
  "uncertainty": "For at least4 strict C/Cp discordances report exact95% Clopper-Pearson interval for forward share, plus two-sided sign/binomial p descriptively; fewer: counts only.",
  "order": "Seed351 shuffle all72 condition/case calls before inference; downstream record order balanced6 gold-first/6 donor-first and fixed per case.",
  "followup": "Only STOP_INVALID, STOP_UNINFORMATIVE, PILOT_SIGNAL_CONFIRM_SEPARATELY; no additional labels, order perturbations, confirmation, or v3.5.2 automatically.",
  "normalization": "Unicode NFC, casefold, outer whitespace, one final period; city-only frozen aliases; no extraction from explanatory text.",
  "limitations": "Distinct pairs and anonymous targets; seven people reused, so not twelve disjoint entity populations. Provided context is available; synthetic lookups show capability, not proof every main city retrieval used context."
}
```
