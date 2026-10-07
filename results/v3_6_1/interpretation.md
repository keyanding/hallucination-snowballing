# Interpretation and limits

**MINIMAL_ASSAY_VALIDATED**. Qwen3-4B followed both mapped states on all 40 fresh cases, with 40/40 paired successes, 10/10 unmapped controls and 20/20 order-invariant outputs. This meets all frozen C1–C6 criteria and the separate order diagnostic. It demonstrates nominal capability for the minimal symbolic primitive under this prompt and identifier family.

The diagnostic evidence favors prompt sensitivity over a blanket inability to execute state-to-outcome lookup. In Stage B, the only failure was v360-calibration-017 / FULL_UNKNOWN / C0: State_J32 should map to Outcome_E53 but returned UNKNOWN. Either removing the UNKNOWN line from FULL or using MINIMAL with UNKNOWN corrected this call. All other calls in those matched comparisons remained correct. However, the advantage is just one of 40 mapped calls; it does not establish a general fallback effect or identify an internal mechanism. MINIMAL_UNKNOWN and MINIMAL_NO_UNKNOWN tied at 40/40, as did FULL_NO_UNKNOWN and MINIMAL_NO_UNKNOWN.

The old v3.6.0 C0 accuracy was 17/20; the new FULL_UNKNOWN C0 accuracy was 19/20. The old failures 001 and 012 recovered and 017 persisted. FULL_UNKNOWN uses a shorter UNKNOWN instruction than v3.6.0, so this is not an exact replication. The four-way replay cannot separately determine why the longer original sentence failed. FULL versus MINIMAL also changes entity scaffolding, prose and mapping syntax together; it does not isolate entity removal.

The old failures were not distinguished by identifier token counts: failed and passed cases all had four tokens for gold state, gold outcome and entity. One of ten first-line and two of ten second-line cases failed C0. The three failed state, outcome and entity suffixes share no identical character at any common suffix position. These observations provide no clear token-count or simple shared-suffix explanation, but cannot exclude other token-identity or surface effects with 20 cases. Full contingency counts and tokens are retained in the static audit.

Old invariance failures should not be mistaken for control-answer error rates: all three ENTITY_LABEL mismatches corrected an incorrect C0, while the five REVERSE mismatches comprise three corrections and two new errors. See the case-level audit for both correctness and invariance.

Stage C changes the identifier family and uses the minimal prompt, so its success does not identify which construction change caused improvement. A 40/40 observed rate has Wilson 95% interval [91.2%,100%]; passing the predefined gate does not prove population accuracy of at least 97.5%. The order check covers only the ten seeded cases.

The stronger-model diagnostic was not triggered because Stage C passed; no compatible stronger checkpoint was locally available either. Its status is STRONGER_MODEL_DIAGNOSTIC_NOT_RUN. No additional model was downloaded or queried. There is no model-size comparison.

No natural hallucination, multi-hop snowballing, SHAR/HalluSE, internal-mechanism, arbitrary-context or real-world-reasoning claim follows. No subsequent phase was run.
