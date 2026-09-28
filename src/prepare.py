"""Conservative evidence-chain selection; never invent missing hops."""
import argparse
import json
import random
from pathlib import Path
from .common import digest, fact, norm, write_jsonl


def chain(row):
    edges = row.get("evidences", [])
    if len(edges) != 2 or any(len(t) != 3 for t in edges):
        return None
    paths = [(a, b) for a, b in (edges, edges[::-1])
             if norm(a[2]) == norm(b[0]) and norm(b[2]) == norm(row["answer"])
             and len({norm(a[0]), norm(a[2]), norm(b[2])}) == 3]
    return paths[0] if len(paths) == 1 else None


def prepare(source, output, n=40, seed=42):
    data = json.loads(Path(source).read_text(encoding="utf-8"))
    pool, flagged = [], []
    for row in data:
        path = chain(row)
        if not path:
            flagged.append({"id": row["_id"], "reason": "not_unique_two_edge_chain"})
            continue
        a, b = path
        # Single biological-parent relations make falsity more defensible than
        # director/writer substitutions (which can have multiple valid objects).
        if a[1] not in {"father", "mother"}:
            flagged.append({"id": row["_id"], "reason": "first_relation_outside_conservative_scope"})
            continue
        context = dict(row["context"])
        try:
            support = [{"title": t, "sentence_id": i, "text": context[t][i]}
                       for t, i in row["supporting_facts"]]
        except (KeyError, IndexError, TypeError):
            flagged.append({"id": row["_id"], "reason": "invalid_support_reference"})
            continue
        text = norm(" ".join(s["text"] for s in support))
        if not all(norm(e) in text for e in (a[2], b[2])):
            flagged.append({"id": row["_id"], "reason": "entities_not_explicit_in_support"})
            continue
        pool.append({"id": row["_id"], "question": row["question"], "gold_answer": row["answer"],
                     "supporting_facts": support, "evidence_chain": [a, b],
                     "evidence_ids": row.get("evidences_id", []),
                     "hop1_gold": fact(a), "hop2_gold": fact(b),
                     "relation_type": f"{a[1]} -> {b[1]}", "relevant_entities": [a[0], a[2], b[2]]})
    rng = random.Random(seed)
    eligible = []
    for row in pool:
        a, b = row["evidence_chain"]
        donors = [d for d in pool if d["relation_type"] == row["relation_type"]
                  and norm(d["evidence_chain"][0][2]) != norm(a[2])
                  and norm(d["gold_answer"]) != norm(row["gold_answer"])
                  and norm(d["evidence_chain"][0][2]) not in norm(str(row["supporting_facts"]))]
        if not donors:
            flagged.append({"id": row["id"], "reason": "no_compatible_donor"})
            continue
        donor = rng.choice(sorted(donors, key=lambda d: d["id"]))
        replacement = donor["evidence_chain"][0][2]
        row.update(injected_hop1=fact([a[0], a[1], replacement]), replacement_entity=replacement,
                   donor_id=donor["id"], donor_chain=donor["evidence_chain"],
                   injection_validation="dataset_parent_relation_contradiction; inspect before experiment")
        eligible.append(row)
    if len(eligible) < n:
        raise ValueError(f"Only {len(eligible)} eligible examples; requested {n}")
    selected = rng.sample(sorted(eligible, key=lambda d: d["id"]), n)
    write_jsonl(output, selected)
    write_jsonl(Path(output).with_name("flagged.jsonl"), flagged)
    manifest = {"source_sha256": digest(source), "seed": seed, "n": n,
                "eligible": len(eligible), "total": len(data),
                "source_url": "https://www.dropbox.com/s/ms2m13252h6xubs/data_ids_april7.zip?dl=1"}
    Path(output).with_suffix(".manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--source", default="data/dev.json")
    p.add_argument("--output", default="data/pilot.jsonl")
    p.add_argument("--n", type=int, default=40)
    p.add_argument("--seed", type=int, default=42)
    prepare(**vars(p.parse_args()))
