import unittest
from src.prepare import chain
from src.run import parse
from src.evaluate import average, subtract, label


class PipelineTests(unittest.TestCase):
    def test_chain_requires_link_and_answer(self):
        self.assertEqual(chain({"evidences": [["B", "r", "C"], ["A", "r", "B"]], "answer": "C"})[0][0], "A")
        self.assertIsNone(chain({"evidences": [["A", "r", "B"], ["X", "r", "C"]], "answer": "C"}))
        self.assertIsNone(chain({"evidences": [["A", "r", "B"], ["B", "r", "C"]], "answer": "D"}))

    def test_raw_structure_failures_are_not_hidden(self):
        self.assertFalse(parse("unstructured answer")["parse_valid"])
        self.assertTrue(parse("Step 1: a\nStep 2: b\nFinal answer: c")["parse_valid"])
        self.assertTrue(parse("Step 2: b\nFinal answer: c", "fixed")["parse_valid"])
        self.assertFalse(parse("Step 1: rewritten\nStep 2: b\nFinal answer: c", "fixed")["parse_valid"])

    def test_unknown_labels_do_not_become_zero(self):
        self.assertIsNone(average([None, None]))
        self.assertEqual(average([None, True]), 1)
        self.assertIsNone(subtract(None, .5))
        r = label(dict(generated_hop1="It is not B.", hop1_gold="It is B.", injected_hop1="It is C.",
                       generated_hop2="unknown", hop2_gold="gold", final_answer="alias", gold_answer="official", condition="baseline"))
        self.assertIsNone(r["e1"])
        self.assertIsNone(r["e2"])
        self.assertIsNone(r["final_correct"])


if __name__ == "__main__":
    unittest.main()
