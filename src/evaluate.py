"""Conservative labels: unknown is never silently counted as correct."""
import argparse
import csv
import json
from pathlib import Path
from .common import norm, read_jsonl, write_jsonl
from .run import CONDITIONS


def average(values):
    values = [v for v in values if v is not None]
    return sum(values) / len(values) if values else None


def subtract(a, b):
    return a-b if a is not None and b is not None else None


def label(row):
    # Only complete exact statements are auto-labeled. Entity occurrence alone
    # cannot distinguish a claim from a negation, hypothetical, or correction.
    h1 = norm(row["generated_hop1"])
    e1 = False if h1 == norm(row["hop1_gold"]) else True if h1 == norm(row["injected_hop1"]) else None
    e2 = False if norm(row["generated_hop2"]) == norm(row["hop2_gold"]) else None
    final = True if norm(row["final_answer"]) == norm(row["gold_answer"]) else None
    return row | {"e1": e1, "e2": e2, "final_correct": final, "propagation_consistent": None,
                  "replacement_label": "REPAIR" if row["condition"] == "rejection" else None}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="results/smoke/trajectories.jsonl")
    p.add_argument("--output", default="results/smoke")
    p.add_argument("--labels", help="Reviewed CSV using id, condition and 0/1 labels")
    args = p.parse_args()
    rows = [label(r) for r in read_jsonl(args.input)]
    if len({(r['id'], r['condition']) for r in rows}) != len(rows):
        raise ValueError("Duplicate trajectories")
    if args.labels:
        with open(args.labels, encoding="utf-8-sig", newline="") as f:
            manual = {(r["id"], r["condition"]): r for r in csv.DictReader(f)}
        for row in rows:
            m = manual.get((row["id"], row["condition"]), {})
            for key in ("e1", "e2", "final_correct", "propagation_consistent"):
                if m.get(key, "") not in ("", "0", "1"):
                    raise ValueError(f"Invalid {key}: {m[key]}")
                if m.get(key, "") != "":
                    row[key] = bool(int(m[key]))
            if m.get("replacement_label"):
                if m["replacement_label"] not in {"REPAIR", "AVOIDANCE", "NEW_ERROR", "SAME_ERROR", "OTHER"}:
                    raise ValueError("Invalid replacement label")
                row["replacement_label"] = m["replacement_label"]
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    write_jsonl(out / "evaluated.jsonl", rows)
    fields = ["id", "condition", "question", "hop1_gold", "hop2_gold", "injected_hop1", "generated_hop1", "generated_hop2", "final_answer", "gold_answer", "supporting_facts", "e1", "e2", "final_correct", "propagation_consistent", "replacement_label"]
    with (out / "manual_review.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fields, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow(row | {k: "" if row[k] is None else int(row[k]) for k in ("e1", "e2", "final_correct", "propagation_consistent")})
    summary = []
    for condition in CONDITIONS:
        group = [r for r in rows if r["condition"] == condition]
        summary.append({"condition": condition, "n": len(group),
                        "hop1_error_rate": average([r["e1"] for r in group]),
                        "hop2_error_rate": average([r["e2"] for r in group]),
                        "final_accuracy": average([r["final_correct"] for r in group]),
                        "n_hop1_labeled": sum(r["e1"] is not None for r in group),
                        "n_hop2_labeled": sum(r["e2"] is not None for r in group),
                        "n_final_labeled": sum(r["final_correct"] is not None for r in group),
                        "mean_output_tokens": average([r["output_tokens"] for r in group]),
                        "mean_latency": average([r["latency_seconds"] for r in group])})
    with (out / "summary.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, list(summary[0])); w.writeheader(); w.writerows(summary)
    baseline = [r for r in rows if r["condition"] == "baseline"]
    rates = [average([r["e2"] for r in baseline if r["e1"] is flag]) for flag in (True, False)]
    paired = []
    for sid in sorted({r["id"] for r in rows}):
        pair = {r["condition"]: r for r in rows if r["id"] == sid}
        if all(c in pair and pair[c]["e2"] is not None for c in ("injected_error", "rejection")):
            paired.append(int(pair["injected_error"]["e2"]) - int(pair["rejection"]["e2"]))
    metrics = {"P(E2|E1)_baseline": rates[0], "P(E2|not_E1)_baseline": rates[1],
               "Propagation Gap": subtract(*rates), "Intervention Effect": average(paired),
               "intervention_paired_n": len(paired), "note": "E2 is downstream factual error; propagation_consistent is labeled separately. PG uses natural baseline only. Missing labels excluded; report denominators."}
    (out / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(json.dumps(metrics, indent=2))
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(7, 4))
    for i, s in enumerate(summary):
        value = s["hop2_error_rate"]
        ax.bar(i, 0 if value is None else value, color=["#526d82", "#c95f4a", "#458c71"][i])
        ax.text(i, 0.04 if value is None else min(value + .04, 1.08),
                f"{'N/A' if value is None else format(value, '.0%')}\n{s['n_hop2_labeled']}/{s['n']} labeled", ha="center")
    ax.set(xticks=range(3), xticklabels=["Baseline", "Injected error", "Oracle correction"],
           ylim=(0, 1.2), ylabel="Downstream factual error rate", title="Pilot: labeled cases only (not SHARS detection)")
    fig.tight_layout(); fig.savefig(out / "downstream_error.png", dpi=160); plt.close(fig)
    cases = ["# Case studies", "Oracle replacements are supplied gold facts; semantic validity must be reviewed."]
    ids = list(dict.fromkeys(r["id"] for r in rows))[:8]
    for sid in ids:
        group = {r["condition"]: r for r in rows if r["id"] == sid}
        first = next(iter(group.values()))
        cases += [f"\n## {first['question']}", f"Gold chain: {first['hop1_gold']} {first['hop2_gold']}",
                  "| Baseline | Injected error | Oracle correction |", "|---|---|---|"]
        cells = []
        for c in CONDITIONS:
            r = group.get(c)
            cells.append("Missing" if r is None else ("Step 1: " + r["generated_hop1"] + "\n" + r["raw_generation"]).replace("|", "\\|").replace("\n", "<br>"))
        cases.append("| " + " | ".join(cells) + " |")
    (out / "case_studies.md").write_text("\n\n".join(cases), encoding="utf-8")


if __name__ == "__main__":
    main()
