# Pre-inference design audit

| Intention | Feature | Observable check | Failure meaning |
|---|---|---|---|
| Preserve primitive | Exact v3.6.1 minimal template | K0 literal template check and replication | Base regression |
| Add only context | Nested irrelevant mappings | Lower K obtained by deletion only | Confounded intervention |
| Avoid world knowledge | Fresh opaque IDs |2080 unique IDs, no old overlap|Shortcut contamination|
| Avoid fallback interference | No UNKNOWN instruction |All392 prompts checked|Prior brittleness|
| Avoid answer list | Mapping block only |Exact template and regex audit|Candidate artifact|
| Separate region from size | Fixed band, balanced schedule,72 diagnostic calls |14/13/13 positive-K bands; K0 pair order20/20|Position limitation|
| Token balance | Same lexical family |All5200 tokenized, selected tokens/lengths matched|Surface asymmetry|
| Preserve state intervention | Only supplied state changes |196 literal C0/W0 pair checks|Contamination|
| Avoid adaptive optimization | Frozen inputs and user-amended gates |Hash checks|Post-hoc tuning|
| Preserve claim boundary | Context robustness only |Final diagnosis|Unsupported snowballing/SHAR claim|

392 planned calls. UNKNOWN is parsed if generated but never mentioned in a prompt. OTHER/INVALID counts are model outcomes, not infrastructure failure by themselves.
