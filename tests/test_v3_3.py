import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from src.common import read_jsonl
from src import experiment_v3_3 as experiment


class FakeChatAdapter:
    def __init__(self, answers):
        self.answers = answers
        self.calls = []

    def render(self, messages, generation=True):
        text = ''.join('<' + m['role'] + '>\n' + m['content'] + '</end>\n' for m in messages)
        return text + ('<assistant>\n' if generation else '')

    def generate_messages(self, messages):
        prompt = self.render(messages)
        raw = self.answers[prompt]
        self.calls.append(prompt)
        return dict(raw_generation=raw, raw_sha256=experiment.sha(raw), messages=messages,
                    rendered_prompt=prompt, prompt_sha256=experiment.sha(prompt), truncated=False,
                    isolation=dict(fresh_tokenization=True, use_cache=False, past_key_values_supplied=False,
                                   cross_branch_history=False, explicit_checkpoint_messages=len(messages) - 1))


class NaturalBranchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = read_jsonl('data/candidates_v3_3.jsonl')

    def test_replacement_preserves_whitespace_and_only_answer_span(self):
        case = self.cases[0]
        raw = '\n  ' + case['B'] + '  \n'
        self.assertEqual(experiment.replace_state(raw, case['B_prime']), '\n  ' + case['B_prime'] + '  \n')
        self.assertTrue(experiment.audit_pair(case, raw))
        for raw in ('Unknown', 'Step 1: Someone', 'Someone\nBecause something'):
            with self.assertRaises(ValueError):
                experiment.replace_state(raw, case['B'])

    def test_first_hop_classification_and_frozen_lookup(self):
        case = self.cases[0]
        for raw, expected in ((case['B'], 'CORRECT_FIRST_HOP'), (case['B_prime'], 'KNOWN_ALTERNATIVE'),
                              ('Another Person', 'OTHER_WRONG_ENTITY'), ('UNKNOWN', 'UNKNOWN_OR_INVALID')):
            row = experiment.classify_first(case, dict(raw_generation=raw), [])
            self.assertEqual(row['classification'], expected)
        self.assertFalse(experiment.classify_first(case, dict(raw_generation='Another Person'), [])['entity_identity_verified'])

    def test_unfrozen_natural_evidence_rejected(self):
        case = self.cases[0]
        first = dict(classification='OTHER_WRONG_ENTITY', natural_B_hat='Someone', evidence_candidates=[])
        proof = dict(relation=case['relation'], target='Elsewhere')
        with self.assertRaises(ValueError):
            experiment.resolve_pair(case, first, dict(use_natural_wrong=True, evidence=proof))

    def test_full_mock_branches_natural_denominator_and_mirror_gate(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(experiment, 'OUT', Path(folder)), contextlib.redirect_stdout(io.StringIO()):
            out = Path(folder)
            (out / 'branch_audit.pre_inference.md').write_text('Frozen pre-inference audit', encoding='utf-8')
            adapter = FakeChatAdapter({})
            for i, case in enumerate(self.cases):
                raw = case['B_prime'] if i == 0 else case['B']
                adapter.answers[adapter.render([dict(role='user', content=experiment.first_prompt(case))])] = raw
            experiment.phase_a(self.cases, adapter)
            first_rows = read_jsonl(out / 'first_hop_generations.jsonl')
            experiment.make_review_draft(self.cases, first_rows)
            review = json.loads((out / 'eligibility_review.draft.json').read_text(encoding='utf-8'))
            review['passed'] = True
            for case, first in zip(self.cases, first_rows):
                for role, state in (('gold', case['B']), ('wrong', case['B_prime'])):
                    adapter.answers[adapter.render([dict(role='user', content=experiment.control_prompt(case, state))])] = case['C'] if role == 'gold' else case['C_prime']
                    for e in experiment.EVIDENCE:
                        answer = case['C'] if e == 'E1' or (role == 'gold' and e != 'E2') else case['C_prime']
                        messages = experiment.branch_messages(case, first['raw_generation'], state, e)
                        adapter.answers[adapter.render(messages)] = answer
                adapter.answers[adapter.render([dict(role='user', content=experiment.control_prompt(case, case['B_prime'], True))])] = case['C_prime']
            experiment.phase_b(self.cases, adapter, review)
            metrics = json.loads((out / 'metrics.json').read_text(encoding='utf-8'))
            gate = json.loads((out / 'gate.json').read_text(encoding='utf-8'))
            self.assertTrue(gate['passed'])
            self.assertEqual(len(adapter.calls), 168)
            self.assertEqual(metrics['NPR'], dict(count=1, denominator=1, rate=1.0))
            self.assertEqual(metrics['NFER']['count'], 1)
            self.assertEqual(metrics['conditions']['E2']['GSA']['rate'], 0)
            self.assertEqual(metrics['conditions']['E1']['OR']['rate'], 1)
            self.assertEqual(metrics['conditions']['E2']['assessment_counts'], {'STATE_SELECTIVE': 12})
            rows = read_jsonl(out / 'branch_trajectories.jsonl')
            self.assertEqual(sum('B0' in r['logical_branches'] for r in rows), 12)
            resolved = json.loads((out / 'resolved_cases.json').read_text(encoding='utf-8'))
            with self.assertRaises(ValueError):
                experiment.analyze(self.cases, first_rows, rows + [rows[0]], resolved, [])
            # No natural wrong case is required for a passing measurement gate.
            revised = copy.deepcopy(rows)
            for row in revised:
                row['origin'] = 'registered_counterfactual'
            m, _ = experiment.analyze(self.cases, first_rows, revised, resolved, [])
            self.assertIsNone(m['NPR']['rate'])
            # Missing branches cannot masquerade as twelve valid executions.
            partial = [r for r in rows if r['case_id'] in {c['case_id'] for c in self.cases[:7]}]
            _, g = experiment.analyze(self.cases, first_rows, partial, resolved, [])
            self.assertFalse(g['passed'])


if __name__ == '__main__':
    unittest.main()
