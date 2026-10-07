# v3.6.1 pre-registration

## Fixed execution
Stage A: all 20 old calibration cases, static only. Stage B: 20 × 2 × 4 = 160 calls. Stage C: 40 × 2 = 80 mapped calls, 10 separate unmapped controls, 20 separate record-order calls. Total 270 new 4B calls. Stage C runs regardless of Stage B results, unless infrastructure fails.
All cases and renderings are frozen before inference; greedy cap16, seed42, fresh chat, no cache or constrained output; same pinned Qwen3/NF4/BF16 stack as v3.6.0. Cases seed361, reverse sample362; call shuffle seeds361/362/363/364. No cap increases or automatic reruns.

## Controlled Stage B factors
All 20 original calibration cases and both states; original mapping associations/order preserved. FULL uses the v3.6.0 prompt minus its UNKNOWN line. The exact new UNKNOWN sentence is appended to FULL/MINIMAL +UNKNOWN variants. Therefore FULL_UNKNOWN is not a byte-identical v3.6.0 replay; comparisons with v3.6.0 also change UNKNOWN wording. Within v3.6.1 matched +/-UNKNOWN pairs differ only by that one line. FULL vs MINIMAL is the specified bundled surface-form manipulation (entity, prose, mapping syntax); it cannot attribute an effect to entity alone.
A_C and A_W denominators20; S20; false-UNKNOWN40. Report all six paired family comparisons, each by C0/W0, exact categories and case outputs. Best descriptive family means maximum total mapped correct/40, all ties retained. No significance tests or post-hoc family choice for Stage C.
P1: report exact accuracy and UNKNOWN deltas for both matched comparisons, with corrected/broken counts. No invented cutoff for 'material'. P2: report matched full/minimal contrasts. P3: MINIMAL_NO_UNKNOWN <39/40 is a diagnostic signal; Section10 governs execution of stronger-model checks (Stage C invalid AND available compatible model).

## Fresh cases
5200 candidates are tokenized before selection. Exclude every suffix from all 60 v3.6.0 cases. For each role select the smallest observed token-count bucket, deterministic shuffle, then lexical constraints only. Equal token counts and character lengths within each state/outcome pair; globally unique IDs, no substrings, no suffix characters shared between any case state and outcome. Gold mapping first20/40, second20/40. Ten controls use fresh disjoint IDs. No entity in Stage C. No outcome-based selection.

## Parser and gates
NFC, outer strip, remove one terminal period only. No case folding or extraction. Exact gold=C, alternative=Cp, exact UNKNOWN; single well-formed Outcome/OUTCOME_[A-Z][0-9]{2} outside case=OTHER; all other outputs or truncations=INVALID. Expected correctness separately recorded. Main denominator40 paired cases, not80 independent units. Wilson95% intervals for A_C/A_W/S.
C1: gold ≥39/40; C2: wrong ≥39/40; C3: paired ≥39/40; C4: mapped UNKNOWN=0/80; C5: OTHER+INVALID≤1/80; C6: unmapped UNKNOWN≥9/10. All six required. Reverse diagnosis: ≥19/20 identical normalized mapped outcomes vs matched primary (both must be C/Cp); correctness separately reported. This is a limitation check, not an additional C gate.
Final decision exactly MINIMAL_ASSAY_VALIDATED, MINIMAL_ASSAY_INVALID or INFRASTRUCTURE_FAILURE. Missing required calls due to infrastructure means INFRASTRUCTURE_FAILURE; no silent retries or partial-rate decisions.

## Stronger-model availability and claim boundary
Local configured/default caches contain only the 4B checkpoint. No compatible stronger model is already available; no new download or ad hoc service. Record STRONGER_MODEL_DIAGNOSTIC_NOT_RUN with reason, and preserve any trigger. If Stage C fails only fallback or there are no mapped failures, the specified matched stronger-model sample is empty and cannot diagnose fallback. No task alteration.
Even validation licenses only reliable explicit symbolic state-to-outcome following under this minimal prompt. It establishes no natural hallucination, multi-hop snowballing, internal mechanism, SHAR behavior, arbitrary-context robustness or real-world reasoning. No next phase automatically.
