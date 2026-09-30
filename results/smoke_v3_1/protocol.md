# v3.1 pre-inference protocol

## Frozen sample and evidence review

Ten real 2Wiki compositional cases were selected before generation: four birthplaces, three death places, three fathers. All first hops concern a single explicitly named film director. Twenty distinct intermediate people are used across gold and donor branches. This evidence-selected set is not representative of 2Wiki or open-domain reasoning.

Discovery scanned the local development split using the existing unique-two-hop chain function, rejected conflicting annotated objects, and required explicit director and downstream support plus a candidate neutral sentence. The initial structural pool contained 98 rows (59 birth, 23 death, 16 father), with recurring entities. Manual review selected the ten pairs in `src/prepare_v3_1.py`; the source and donor IDs are fixed, with no fallback selection after generation.

Discovery revealed neutral-sentence false positives from same-title remakes and from partial director names (for example, a sentence mentioning only a surname). The final neutral sentence must come from the exact same article title as the first-hop evidence. Full names, distinctive person-name components, target aliases and explicit relation wording are screened; each selected sentence was inspected. All first-hop source sentences name a single director, and no conflicting downstream object was found in the development evidence graph. These are source-evidence checks, not a claim of exhaustive external biographical validation.

The exact source sentences and approved answer aliases are recorded in `data/candidates_v3_1.jsonl` and `context_audit.md`. Alias handling is fixed before model output: source-backed person names, unaccented orthographic variants, initials spacing, and limited geographic qualifiers identifying the same city/town. Country-only answers are not aliases. No supporting biography or answer-bearing extra sentence is inserted into the controlled reference block.

## Context construction

H0 contains exactly two natural-language downstream facts. H1 prepends the original task only. H2 adds one verbatim neutral sentence from the original film article. H3 retains H2 and adds the original first-hop evidence sentence. H3 can therefore add metadata present in that sentence as well as the director identity; it is an evidence-block intervention, not an isolated single-word treatment.

H2 is neutral in the explicit-answer sense: no gold/donor first-hop identity or target value appears in its added sentence. It can contain country, festival, cast or date associations, as intended by the context-growth experiment; it need not be irrelevant to every possible world-knowledge association.

Each level uses byte-identical context and downstream question in the B/B′ state pair. Only the state field changes. The direct controls use the same context, explicitly name B or B′, and have no state field. The two reference facts are held constant across H0–H3. Fact order alternates across cases (five B-first, five B′-first) and remains fixed within a case. There are no extra order variants, preserving the specified 160-call matrix. This balances position across cases but is not a within-case real-entity order-sensitivity test.

## Runtime and call order

Use the same cached Qwen3-4B-Instruct-2507 revision and NF4/BF16 adapter as v3. Greedy decoding (`do_sample=False`, no temperature sampling), 32 new tokens maximum, thinking disabled, single-user messages and `use_cache=False`. No previous prompts, outputs or KV tensors enter subsequent calls. The existing v3 isolation-tested adapter is reused.

Run H0 through H3 in order. At each level run all direct B calls, all direct B′ calls, all state B calls and all state B′ calls. There are ten cases × four levels × four conditions = 160 planned calls. A pre-H3 calibration collapse stops after that complete level and preserves the partial run; no cases or prompts are retried or replaced.

## Preregistered evaluation

Use the v3 short-answer parser and predeclared complete aliases, without substring answer extraction. A matching C′ under B′ is PROPAGATE; matching C under B′ is OVERRIDE_TO_GOLD. An unrecognized real-entity answer receives only a provisional unsupported label and requires source/context review before interpretation; a mismatch alone is not proof of hallucination. Explicit unknown/refusal and malformed/truncated output are separate outcomes.

CLA B and CLA B′ each use all ten direct calls per completed level; combined CLA uses twenty. GSA, PR, OR and secondary outcomes each use the same ten cases per level. Do not change denominators by selecting a different subset at each level. ΔPR subtracts H0's PR on those same cases. SFIR uses direct-correct/state-wrong contrasts divided by direct-correct controls for that entity and level; at H3 this includes meaningful override, not merely apparatus failure. Per-call `direct_lookup_pass` on a state row is its matched direct control result; `state_adherence_pass` is null on direct rows.

Apply the specification's numeric gate: H0 CLA and GSA ≥90%; at least eight interpretable cases across H0–H2; H1/H2 CLA ≥80%; overall invalid-output rate ≤5%; no systematic placeholder/formatting issue. To make the qualitative stop conditions concrete before inference:

- A case is interpretable across H0–H2 if both direct probes and the gold-state control are exact at all three levels, its alternative-state outputs are parseable (overrides/refusals allowed), and it has no unresolved semantic mismatch.
- H1/H2 GSA must remain ≥80%; a lower value stops progression.
- More than 20% provisional unsupported outputs among either level's combined state calls triggers inspection and stops progression.
- Any copied placeholder/instruction string fails the formatting check.
- H3 CLA and GSA must each remain ≥80% for a fully interpretable H3 contrast, and unsupported state outputs must remain ≤20%. No H3 PR or SFIR-B′ threshold is imposed. H3 override may be 100% without failing the assay.

Report the predefined quantitative checks separately so additional operational criteria are visible. If an unrecognized answer needs review, preserve the original output and bind any derived review to its raw hash. Do not claim spontaneous hallucination or infer internal mechanisms from these externally assigned states.

## Preservation and endpoint

Freeze the dataset, code, threshold policy and context audit before inference. Save hashes of all v1/v2/v2.1/v3 artifacts and verify preservation after execution. Refuse output-directory or model-run overwrite. After inspection and diagnosis, stop; do not begin natural trajectory branching, another model comparison, or SHARS/HalluSE integration.
