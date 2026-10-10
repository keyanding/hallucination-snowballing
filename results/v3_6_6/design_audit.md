# Pre-inference structural audit

S1–S5 passed: historical raw recount and both validators;24 HARD/N fixtures;120 fresh graphs/targets and480 source mappings;480 bijective routes,360 exact downstream module-arm pairs;960 fresh IDs and864 tokenized prompts. S6 runtime checked at model load; S7 tested durable dispatch/one-main-call state machine. Maximum504 calls; no yield gate.

## Execution resolutions frozen before inference

This effective spec follows every numeric threshold, seed, parser, stage order and interval in the supplied spec. No new model calls before this freeze. Historical source audit was saved in docs/v3_6_6_preimplementation_audit.json and all four ledger documents updated before constructing the120-case cohort.
Person IDs are SHA256 prefixes of canonical name plus frozen source-row ID; assert uniqueness and stable name mapping. Four names map to four globally fresh STATE IDs and four OUTCOME IDs. Within each case all eight suffixes differ; role token counts/lengths match. This inherits the v3.6.3.1 distinct-suffix rule, not the earlier v3.6.1 stricter character-disjoint constraint. No entity ID is shown downstream; legacy entity fields hold audit-only person IDs. Eight IDs per case are assigned in frozen candidate-array order using seed3665, never predicted-name order. Downstream order60/60 uses that same seeded RNG. All inventory and historical ID exclusions saved.
First-hop parser aliases remain empty. Route provenance additionally includes a hash of the full case identity table; mapping_hash is the hash of the selected prebuilt legacy module, and source raw SHA is retained. Every natural and controlled call matches one of720 frozen module-arm prompts. These are potential prompts, not720 model calls.120 primary plus24 diagnostic and720 module-arm prompts total864 static entries. Actual cap/namespace/call IDs are logged at dispatch. There are120 natural schedule slots, with invalid slots explicitly skipped, and240 controlled schedule slots. All lists are saved. Controlled shuffle seed3664 repeats deterministic shuffles until no adjacent same-case arms; attempts saved.
Classify only after raw persistence. Log CALL_STARTED durably before each generation and CALL_COMPLETED after raw persistence; an unresolved start blocks all reuse. Native process death remains a failed attempt; no automatic resume. Model/revision/version/template mismatch is runtime drift; static hash/bridge mismatch is structural. No early scientific stop.
Intervals use pure-Python inversion of the finite binomial CDF for Clopper-Pearson, avoiding an unavailable SciPy dependency; tests cover endpoint analytic formulas, central cases and paired zero-discordance nonzero widths. Wilson z=1.959963984540054. No alternate narrower interval. On partial data, final UCR is null and cascade bounds are shown; complete-case wrong propagation is explicitly separate. Complete trajectory coverage includes observed invalid first hops with protocol skips; legal forwarding coverage counts returned natural responses/V.
For the diversity part of minimum information, report all-W diversity and additionally the conservative subset with both natural downstream and controlled pair complete; use that jointly complete subset for the5-identities/10-bundles rule. This changes no call schedule or W denominator. Every proportion includes its count and denominator; interval-null reflects empty denominator or incompleteness. Full data retain P+O+T=W; technical missing remains separate.
Information labels, capabilities and technical/collection statuses are separate. Diagnostic has no PRESENTATION_SENSITIVE threshold. Names/real source endpoints audit identity only; actual downstream opaque outcomes are synthetic. Historical frontier failures are not overridden or upgraded.

## Post-inference audit

Frozen inputs/prior artifacts unchanged. Raw/hash/plans and reconstructed routes/journal checked.

{
  "technical_status": "NONE",
  "collection_status": "PROSPECTIVE_COLLECTION_COMPLETE",
  "N_planned": 120,
  "N_attempted": 120,
  "N_observed": 120,
  "V": 118,
  "G": 98,
  "W": 20,
  "stage_counts": {
    "first_hop": 120,
    "natural_downstream": 118,
    "controlled": 240,
    "order_diagnostic": 24
  },
  "capability": "CURRENT_COHORT_CAPABILITY_SUPPORTED",
  "information": "MINIMUM_DESCRIPTIVE_INFORMATION_MET"
}
