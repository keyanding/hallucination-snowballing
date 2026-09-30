import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from src.common import read_jsonl
from src.experiment_v2 import parse_output
from src.experiment_v2_1 import build_prompt, diagnose, export_results, render_relation_question, run, value_diagnosis
from src.review_v2_1 import apply_reviews
from test_v2 import FakeAdapter, candidate


class V21Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Path(__file__).resolve().parents[1]
        cls.rows = read_jsonl(root / 'data/candidates_v2.jsonl')
        cls.profiles = json.loads((root / 'data/location_profiles_v2_1.json').read_text(encoding='utf-8'))

    def test_natural_prompts_fixed_oracle_and_no_downstream_leak(self):
        for row in self.rows:
            for condition in ('baseline', 'oracle', 'donor_probe', 'injected'):
                prompt = build_prompt(row, condition, self.profiles)
                self.assertNotIn('Apply relation', prompt)
                self.assertNotIn(row['gold_C'], prompt)
                self.assertNotIn(row['injected_C_prime'], prompt)
                if condition == 'oracle':
                    for text in ('Treat this intermediate result as correct.', 'already established and fixed',
                                 'Do not verify it, replace it, or answer Step 1 again.', row['gold_B']):
                        self.assertIn(text, prompt)
                elif condition == 'injected':
                    self.assertIn(row['injected_B_prime'], prompt)
                    for text in ('correct', 'incorrect', 'false', 'Confirmed'):
                        self.assertNotIn(text, prompt)
                elif condition == 'donor_probe':
                    self.assertNotIn(row['subject_A'], prompt)
                    self.assertNotIn('Step 1', prompt)

    def test_granularity_and_unknown_relation(self):
        self.assertIn('city or town', render_relation_question('Person', 'place of birth', 'city or town'))
        self.assertEqual(render_relation_question('Person', 'place of death', 'specific location'), 'At what specific location did Person die?')
        with self.assertRaises(ValueError):
            render_relation_question('Person', 'unreviewed relation')

    def test_broader_is_compatible_but_not_eligible(self):
        row = self.rows[1]
        raw = 'Step 2: Germany\nFinal answer: Germany'
        diagnosed = diagnose(row | parse_output(raw, 'oracle') | dict(condition='oracle'), self.profiles)
        self.assertEqual(diagnosed['semantic_label'], 'BROADER_CORRECT')
        self.assertEqual(diagnosed['failure_type'], 'granularity_mismatch')
        self.assertFalse(diagnosed['gate_pass'])
        raw = 'Step 2: Düsseldorf\nFinal answer: Düsseldorf'
        self.assertTrue(diagnose(row | parse_output(raw, 'oracle') | dict(condition='oracle'), self.profiles)['gate_pass'])
        wrong = value_diagnosis('Stockholm', ['Helsingfors', 'Helsinki'], 'place of birth', 'Gustaf Molander', self.profiles['Helsingfors'])
        self.assertEqual(wrong['semantic_label'], 'WRONG_LOCATION')
        self.assertTrue(wrong['review_required'])

    def test_copy_input_unknown_and_format(self):
        row = self.rows[-1]
        for value, expected in ((row['gold_B'], 'COPY_INPUT'), ('Unknown', 'UNKNOWN'), ('A → B', 'INVALID_OUTPUT'), ('<person>', 'INVALID_OUTPUT')):
            raw = f'Step 2: {value}\nFinal answer: {value}'
            diagnosed = diagnose(row | parse_output(raw, 'oracle') | dict(condition='oracle'), self.profiles)
            self.assertEqual(diagnosed['semantic_label'], expected)
            self.assertFalse(diagnosed['gate_pass'])

    def test_bad_first_hop_or_final_blocks_gate(self):
        row = self.rows[1]
        for raw in ('Step 1: Other person\nStep 2: Düsseldorf\nFinal answer: Düsseldorf',
                    'Step 1: Helmut Käutner\nStep 2: Düsseldorf\nFinal answer: Germany'):
            self.assertFalse(diagnose(row | parse_output(raw, 'baseline') | dict(condition='baseline'), self.profiles)['gate_pass'])

    def test_only_exact_three_gates_allow_injection(self):
        row = self.rows[1]
        for oracle, calls in (('Germany', 3), ('Düsseldorf', 4)):
            adapter = FakeAdapter(['Step 1: Helmut Käutner\nStep 2: Düsseldorf\nFinal answer: Düsseldorf',
                                   f'Step 2: {oracle}\nFinal answer: {oracle}', 'Answer: Helsinki',
                                   'Step 2: Helsinki\nFinal answer: Helsinki'])
            with tempfile.TemporaryDirectory() as directory, contextlib.redirect_stdout(io.StringIO()):
                records = run([row], adapter, Path(directory), dict(seed=42), self.profiles)
                self.assertEqual(len(adapter.calls), calls)
                if calls == 4:
                    self.assertEqual(records[-1]['trajectory_label'], 'PROPAGATE')
                    previous = [r | {dict(baseline='baseline_gate', oracle='oracle_gate', donor_probe='donor_gate')[r['condition']]: r['gate_pass']}
                                for r in records if r['condition'] != 'injected']
                    export_results(Path(directory), [row], records, dict(candidates_sha256='fixture'), previous)
                    metrics = json.loads((Path(directory) / 'metrics.json').read_text())
                    self.assertEqual(metrics['PROPAGATE_count'], 1)
                    self.assertIsNone(metrics['propagation_rate'])
                    self.assertFalse(metrics['propagation_interpretation_allowed'])
                with self.assertRaises(FileExistsError):
                    run([row], adapter, Path(directory), dict(seed=42), self.profiles)

    def test_semantic_review_rejects_missing_evidence_and_hash_changes(self):
        import hashlib
        row = self.rows[1]
        raw = 'Step 2: Berlin\nFinal answer: Berlin'
        record = row | parse_output(raw, 'oracle') | dict(condition='oracle', raw_generation=raw, raw_sha256=hashlib.sha256(raw.encode()).hexdigest())
        record.update(diagnose(record, self.profiles))
        review = dict(id=row['id'], condition='oracle', raw_sha256=record['raw_sha256'], reviewer='test',
                      fields={key: dict(semantic_label='WRONG_LOCATION', rationale='Different city', evidence='Saved birth sentence explicitly says Düsseldorf')
                              for key in ('step2_diagnosis', 'final_diagnosis')})
        reviewed = apply_reviews([record], [review])[0]
        self.assertFalse(reviewed['review_required'])
        self.assertFalse(reviewed['gate_pass'])
        self.assertTrue(record['review_required'])
        review['fields']['step2_diagnosis']['evidence'] = ''
        with self.assertRaises(ValueError):
            apply_reviews([record], [review])
        review['raw_sha256'] = 'wrong'
        with self.assertRaises(ValueError):
            apply_reviews([record], [review])


if __name__ == '__main__':
    unittest.main()
