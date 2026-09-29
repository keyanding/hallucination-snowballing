"""Conservative evidence-chain selection; never invent missing hops."""
import argparse
import json
import random
import re
import zipfile
from collections import Counter, defaultdict
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


def prepare_v2(source, output, n=5, seed=42, aliases_archive="data/source.zip"):
    """Small pre-model pool; evidence-backed donors with same relation and era."""
    if not 3 <= n <= 5:
        raise ValueError("V2 smoke preparation is restricted to 3–5 candidates")
    if Path(output).exists():
        raise FileExistsError(output)
    data = json.loads(Path(source).read_text(encoding="utf-8"))
    aliases = {}
    with zipfile.ZipFile(aliases_archive) as archive:
        for line in archive.read("id_aliases.json").decode("utf-8").splitlines():
            record = json.loads(line)
            aliases[record["Q_id"]] = record["aliases"]
    # Cross-dataset known multi-valued relations are unsafe for exact gates.
    objects = defaultdict(set)
    for row in data:
        for s, r, o in row.get("evidences", []):
            objects[(norm(s), r)].add(norm(o))
    pool, excluded = [], Counter()
    ambiguous = {"spouse", "occupation", "award received", "educated at", "employer",
                 "child", "sibling", "genre", "cast member"}
    for row in data:
        path = chain(row)
        if row.get("type") != "compositional" or not path:
            excluded["not_explicit_compositional_chain"] += 1
            continue
        a, b = path
        if a[1] in ambiguous or b[1] in ambiguous:
            excluded["potentially_multivalued_relation"] += 1
            continue
        if any(len(objects[(norm(t[0]), t[1])]) != 1 for t in path):
            excluded["conflicting_or_multiple_dataset_objects"] += 1
            continue
        context = dict(row["context"])
        try:
            support = [{"title": title, "sentence_id": index, "text": context[title][index]}
                       for title, index in row["supporting_facts"]]
        except (KeyError, IndexError, TypeError):
            excluded["invalid_support"] += 1
            continue
        text = norm(" ".join(x["text"] for x in support))
        if not all(norm(e) in text for e in (a[2], b[2])):
            excluded["entities_not_explicit"] += 1
            continue
        # A state containing a birth town is not the same entity as the town.
        # Also reject supporting sentences that only mention a location without
        # expressing the annotated birth/death relation (observed in this data).
        if b[1] == "place of birth" and not re.search(
                r"\bborn\b[^.!?]{0,100}?\bin\s+(?:the\s+)?" + re.escape(norm(b[2])) + r"\b", text):
            excluded["birth_relation_or_location_granularity_unclear"] += 1
            continue
        if b[1] == "place of death" and not re.search(
                r"\b(?:died|death)\b[^.!?]{0,160}" + re.escape(norm(b[2])) + r"\b", text):
            excluded["death_relation_not_explicit_in_support"] += 1
            continue
        # Dates in the intermediate entity's biographical lead provide a
        # conservative era proxy. Missing years are excluded, not invented.
        paragraphs = [sents for title, sents in row["context"] if norm(title) == norm(a[2])]
        years = re.findall(r"\b(1[0-9]{3}|20[0-2][0-9])\b", " ".join(paragraphs[0][:1]) if paragraphs else "")
        if not years:
            excluded["no_intermediate_era_anchor"] += 1
            continue
        work_year, work_kind = None, None
        if a[1] in {"composer", "director", "creator", "performer", "author", "screenwriter"}:
            titles = [s for title, s in row["context"] if norm(re.sub(r"\s*\([^)]*\)\s*$", "", title)) == norm(a[0])]
            work_lead = " ".join(titles[0][:3]) if titles else ""
            dates = re.findall(r"\b(1[0-9]{3}|20[0-2][0-9])\b", work_lead)
            if not dates:
                excluded["no_work_year_for_donor_plausibility"] += 1
                continue
            work_year = int(dates[0])
            kinds = re.findall(r"\b(film|song|novel|opera|album|play)\b", work_lead.lower())
            work_kind = kinds[0] if kinds else "unspecified_work"
        ids = row.get("evidences_id", [])
        idmap = {}
        for triple, identifiers in zip(row["evidences"], ids):
            idmap[triple[0]] = identifiers[0]
            idmap[triple[2]] = identifiers[2]
        def names(entity):
            # Alias lists occasionally contain polluted entries. Retain only
            # reasonably long textual aliases; all matches are logged for review.
            return sorted({entity} | {x for x in aliases.get(idmap.get(entity), [])
                                      if len(x) >= 4 and any(c.isalpha() for c in x) and norm(x) in text})
        pool.append(dict(id=row["_id"], question=row["question"], subject_A=a[0], relation_r1=a[1],
                         gold_B=a[2], relation_r2=b[1], gold_C=b[2], gold_hop1_fact=fact(a),
                         gold_hop2_fact=fact(b), supporting_facts=support, evidence_chain=path,
                         aliases_B=names(a[2]), aliases_C=names(b[2]), era_anchor=min(map(int, years)),
                         work_year=work_year, work_kind=work_kind,
                         era_evidence=paragraphs[0][0], relation_type=f"{a[1]} -> {b[1]}"))
    frequency = Counter(r["gold_B"] for r in pool)
    rng = random.Random(seed)
    rng.shuffle(pool)
    # Deliberately knowledge-friendly pilot: recurring entities first. This is
    # pre-outcome selection, not a representative or random benchmark estimate.
    ordered = sorted(pool, key=lambda r: -frequency[r["gold_B"]])
    selected, used = [], set()
    for row in ordered:
        if row["gold_B"] in used:
            continue
        donors = [d for d in pool if d["relation_type"] == row["relation_type"]
                  and norm(d["gold_B"]) not in {norm(row["gold_B"]), norm(row["subject_A"])}
                  and norm(d["gold_C"]) != norm(row["gold_C"])
                  and abs(d["era_anchor"]-row["era_anchor"]) <= 40
                  and d["work_kind"] == row["work_kind"]
                  and (row["work_year"] is None or 18 <= row["work_year"]-d["era_anchor"] <= 85)
                  and norm(d["gold_B"]) not in norm(str(row["supporting_facts"]))
                  and not ({norm(x) for x in d["aliases_C"]} & {norm(x) for x in row["aliases_C"]})]
        if not donors:
            continue
        donor = sorted(donors, key=lambda d: (-frequency[d["gold_B"]], abs(d["era_anchor"]-row["era_anchor"]), d["id"]))[0]
        row = row | dict(injected_B_prime=donor["gold_B"], injected_C_prime=donor["gold_C"],
            injected_hop1_fact=fact([row["subject_A"], row["relation_r1"], donor["gold_B"]]),
            injected_hop2_fact=donor["gold_hop2_fact"], donor_id=donor["id"],
            donor_supporting_facts=donor["supporting_facts"], donor_evidence_chain=donor["evidence_chain"],
            donor_era_anchor=donor["era_anchor"], donor_era_evidence=donor["era_evidence"],
            aliases_B_prime=donor["aliases_B"], aliases_C_prime=donor["aliases_C"],
            candidate_validation=dict(structural_chain_valid=True, gold_entities_explicit=True,
                donor_relation_matches=True, era_difference_max_40=True,
                work_domain_matches=True, donor_adult_in_work_year=True,
                falsity_basis="single annotated object; supporting evidence requires inspection"))
        selected.append(row); used.add(row["gold_B"])
        if len(selected) == n:
            break
    if len(selected) != n:
        raise ValueError(f"Only {len(selected)} compatible candidates")
    write_jsonl(output, selected)
    manifest = dict(version=2, n=n, seed=seed, source_sha256=digest(source), candidates_sha256=digest(output),
                    selection="highest recurring intermediate entities, distinct B; same r1/r2 and work domain, within 40-year era proxy, adult in work year; birth/death support and granularity checks; no model-based selection",
                    structural_pool=len(pool), exclusions=dict(excluded), alias_source_sha256=digest(aliases_archive))
    Path(output).with_suffix(".manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--source", default="data/dev.json")
    p.add_argument("--output")
    p.add_argument("--n", type=int)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--version", choices=["v1", "v2"], default="v2")
    args = vars(p.parse_args())
    version = args.pop("version")
    args["output"] = args["output"] or ("data/candidates_v2.jsonl" if version == "v2" else "data/pilot.jsonl")
    args["n"] = args["n"] or (5 if version == "v2" else 40)
    (prepare_v2 if version == "v2" else prepare)(**args)
