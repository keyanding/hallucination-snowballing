# Post-inference diagnostic observations

This supplement describes saved outputs; it does not change the frozen parser, cap, cases, thresholds or decisions.

The modular pipeline passed all main gates. Integrated exact-output execution did not meet its separate readiness threshold: I-A 7/20, I-B 9/20 and paired 2/20. All 24 integrated failures were INVALID under the frozen exact-identifier parser; 17 of those outputs were truncated at the unchanged 16-token cap. Observed formats include state-to-outcome chains, entity-to-state-to-outcome chains, explanatory continuation and one omitted OUTCOME_ prefix. No answer was extracted or repaired, even when an expected outcome appeared within a chain. This demonstrates lack of readiness for the tested exact-output interface; these format failures alone do not establish an inability to compute the underlying mapping.

On ten independent matched diagnostic cases, the minimal Current state shell returned exact expected outcomes 20/20. The Recorded intermediate result shell returned 17/20, with three explanatory truncated outputs. All three discordances favored the minimal shell. This is a small descriptive whole-shell comparison; it does not isolate the heading or identify an internal mechanism.

No failed case or call was repeated, no output cap increased, and no natural-first-hop-error experiment was run.
