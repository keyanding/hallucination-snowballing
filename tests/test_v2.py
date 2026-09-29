import contextlib
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from src.experiment_v2 import MODEL, build_prompt, classify, gate_success, parse_output, run, validate_load_test
from src.prepare import prepare_v2
from src.review_v2 import apply_reviews


def candidate():
    return dict(id="test", question="Where was A's father born?", subject_A="A", relation_r1="father",
                gold_B="B", relation_r2="place of birth", gold_C="C", injected_B_prime="B prime",
                injected_C_prime="C prime", aliases_B=["B"], aliases_C=["C"], aliases_C_prime=["C prime"],
                supporting_facts=[], donor_supporting_facts=[])


class FakeAdapter:
    def __init__(self, outputs):
        self.outputs = iter(outputs)
        self.calls = []

    def generate(self, prompt, seed):
        self.calls.append(prompt)
        return dict(raw_generation=next(self.outputs), input_tokens=1, output_tokens=1,
                    latency_seconds=0, truncated=False)


class V2Tests(unittest.TestCase):
    def test_native_automatic_offload_does_not_bypass_nf4_gate(self):
        with self.assertRaises(ValueError):
            validate_load_test(dict(success=True, model_name=MODEL, raw_generation="4",
                requested_quantization="native", quantization="cpu-offload", comfortable=False))

    def test_prepare_keeps_evidence_donors_and_rejects_shortcuts(self):
        rows = []
        for i in range(4):
            a, b, c = f"Work {i}", f"Person {i}", f"City {i}"
            rows.append(dict(_id=str(i), type="compositional", question=f"Where was the creator of {a} born?",
                answer=c, evidences=[[a,"creator",b],[b,"place of birth",c]], evidences_id=[],
                context=[[a,[f"{a} is a 1930 film created by {b}."]],[b,[f"{b} (born 190{i}) was born in {c}."]]],
                supporting_facts=[[a,0],[b,0]]))
        rows.append(dict(_id="shortcut", type="compositional", answer="Dad", evidences=[["Child","mother","Mom"],["Mom","spouse","Dad"]]))
        with tempfile.TemporaryDirectory() as directory, contextlib.redirect_stdout(io.StringIO()):
            root = Path(directory)
            source = root / "dev.json"; source.write_text(json.dumps(rows),encoding="utf-8")
            archive = root / "source.zip"
            with zipfile.ZipFile(archive,"w") as z: z.writestr("id_aliases.json", "")
            target = root / "candidates.jsonl"
            prepare_v2(source, target, n=3, aliases_archive=archive)
            candidates = [json.loads(line) for line in target.read_text().splitlines()]
            self.assertEqual(len(candidates),3)
            for row in candidates:
                self.assertNotEqual(row["gold_C"],row["injected_C_prime"])
                self.assertEqual(row["relation_r2"], row["donor_evidence_chain"][1][1])
                self.assertNotEqual(row["id"], "shortcut")
            with self.assertRaises(FileExistsError): prepare_v2(source,target,n=3,aliases_archive=archive)

    def test_review_requires_evidence_for_new_hallucination(self):
        import hashlib
        raw = "Step 2: D\nFinal answer: D"
        row = candidate() | {"condition":"injected", "raw_generation":raw}
        review = dict(id="test",raw_sha256=hashlib.sha256(raw.encode()).hexdigest(),label="NEW_HALLUCINATION",reviewer="test",rationale="Different value")
        with self.assertRaises(ValueError): apply_reviews([row],[review])
        review["unsupportedness_evidence"]="Fixture statement contradicts the complete synthetic relation table."
        self.assertEqual(apply_reviews([row],[review])[0]["trajectory_label"],"NEW_HALLUCINATION")

    def test_prompts_define_relations_without_gold_leakage(self):
        row = candidate()
        injected = build_prompt(row, "injected")
        self.assertIn('Apply relation "place of birth"', injected)
        self.assertIn("Step 1: B prime", injected)
        self.assertNotIn("C prime", injected)
        self.assertNotIn("false", injected)
        self.assertNotIn("Question:", build_prompt(row, "donor_probe"))

    def test_exact_entities_not_substrings_or_repeated_labels(self):
        row = candidate() | parse_output("Step 1: B\nStep 2: Not C\nFinal answer: Not C", "baseline")
        self.assertFalse(gate_success(row, "baseline"))
        self.assertFalse(parse_output("Step 2: C\nStep 2: C", "oracle")["parse_valid"])
        self.assertFalse(parse_output("Explanation\nStep 2: C\nFinal answer: C", "oracle")["parse_valid"])

    def test_classification_preserves_unknowns_and_invalid(self):
        for value, expected in (("C prime", "PROPAGATE"), ("C", "RECOVER"), ("D", None)):
            raw = f"Step 2: {value}\nFinal answer: {value}"
            row = candidate() | parse_output(raw, "injected") | {"raw_generation": raw}
            self.assertEqual(classify(row)[0], expected)
        row = candidate() | parse_output("I don't know", "injected") | {"raw_generation": "I don't know"}
        self.assertEqual(classify(row)[0], "REJECT_UNCERTAIN")
        row["raw_generation"] = "unparseable"
        self.assertEqual(classify(row)[0], "INVALID_OUTPUT")

    def test_failed_gate_prevents_injection_and_zero_denominator(self):
        for failed in range(3):
            outputs = ["Step 1: B\nStep 2: C\nFinal answer: C", "Step 2: C\nFinal answer: C", "Answer: C prime"]
            outputs[failed] = "wrong"
            adapter = FakeAdapter(outputs)
            with tempfile.TemporaryDirectory() as directory, contextlib.redirect_stdout(io.StringIO()):
                out = Path(directory)
                run([candidate()], adapter, out, {"seed": 42, "candidates_sha256": "fixture"})
                metrics = json.loads((out / "metrics.json").read_text())
                self.assertEqual(len(adapter.calls), 3)
                self.assertEqual(metrics["number_passing_all_gates"], 0)
                self.assertIsNone(metrics["propagation_rate"])

    def test_successful_gates_allow_one_injection(self):
        adapter = FakeAdapter(["Step 1: B\nStep 2: C\nFinal answer: C", "Step 2: C\nFinal answer: C",
                               "Answer: C prime", "Step 2: C prime\nFinal answer: C prime"])
        with tempfile.TemporaryDirectory() as directory, contextlib.redirect_stdout(io.StringIO()):
            rows = run([candidate()], adapter, Path(directory), {"seed": 42, "candidates_sha256": "fixture"})
            self.assertEqual(rows[-1]["trajectory_label"], "PROPAGATE")
            self.assertTrue(all(rows[-1][k] for k in ("baseline_gate", "oracle_gate", "donor_gate")))


if __name__ == "__main__":
    unittest.main()
