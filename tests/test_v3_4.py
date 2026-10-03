import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from src.common import read_jsonl
from src import experiment_v3_4 as exp


class FakeAdapter:
    def __init__(self):
        self.answers = {}
        self.calls = []

    def render(self, messages, generation=True):
        return ''.join('<' + m['role'] + '>\n' + m['content'] + '</end>\n' for m in messages) + ('<assistant>\n' if generation else '')

    def generate_messages(self, messages):
        prompt = self.render(messages)
        self.calls.append(prompt)
        answer = self.answers[prompt]
        return dict(raw_generation=answer, raw_sha256=exp.sha(answer), messages=messages,
                    rendered_prompt=prompt, prompt_sha256=exp.sha(prompt), truncated=False,
                    isolation=dict(use_cache=False, past_key_values_supplied=False, cross_branch_history=False))


class UniverseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = read_jsonl(exp.DATA)

    def adapter(self, wrong_count=6, fail_lookup=False):
        adapter = FakeAdapter()
        for i, case in enumerate(self.cases):
            natural = case['registered_wrong'] if i < wrong_count else case['B']
            values = {p['name']: p['target'] for p in case['candidates']}
            adapter.answers[adapter.render([dict(role='user', content=exp.first_prompt(case))])] = natural
            for p in case['candidates']:
                answer = 'Unknown' if fail_lookup and i < 2 else p['target']
                adapter.answers[adapter.render([dict(role='user', content=exp.lookup_prompt(case, p['name']))])] = answer
            for state in (natural, case['B'], case['registered_wrong']):
                adapter.answers[adapter.render(exp.branch_messages(case, natural, state))] = values[state]
            adapter.answers[adapter.render([dict(role='user', content=exp.lookup_prompt(case, natural, True))])] = values[natural]
        return adapter

    def test_candidate_uniqueness_and_no_direct_answer_leak(self):
        for case in self.cases:
            self.assertTrue(all(exp.audit_case(case).values()))
        case = copy.deepcopy(self.cases[0])
        case['candidates'][0]['target'] = case['candidates'][1]['target']
        with self.assertRaises(AssertionError):
            exp.audit_case(case)
        case = copy.deepcopy(self.cases[0])
        case['first_hop_evidence'].append(f'"{case["A"]}" was directed by {case["B"]}.')
        with self.assertRaises(AssertionError):
            exp.audit_case(case)

    def test_out_of_set_never_coerced_and_malformed_separate(self):
        case = self.cases[0]
        for raw, label in ((case['B'], 'CORRECT_FIRST_HOP'), (case['registered_wrong'], 'TRACEABLE_WRONG_CANDIDATE'),
                           ('Person outside the universe', 'OUT_OF_SET_ENTITY'), (case['B'] + '.', 'OUT_OF_SET_ENTITY'),
                           ('Step 1: ' + case['B'], 'INVALID_OUTPUT')):
            self.assertEqual(exp.classify_first(case, dict(raw_generation=raw))['first_hop_label'], label)

    def test_insufficient_error_yield_stops_before_downstream(self):
        with tempfile.TemporaryDirectory() as d, patch.object(exp, 'OUT', Path(d)), contextlib.redirect_stdout(io.StringIO()):
            adapter = self.adapter(wrong_count=4)
            exp.run(self.cases, adapter)
            self.assertEqual(len(adapter.calls), 20)
            self.assertEqual((Path(d) / 'branch_trajectories.jsonl').read_bytes(), b'')
            metrics = json.loads((Path(d) / 'metrics.json').read_text())
            gate = json.loads((Path(d) / 'gate.json').read_text())
            self.assertIsNone(metrics['NPR']['rate'])
            self.assertIsNone(metrics['CLA_all']['rate'])
            self.assertFalse(gate['passed'])

    def test_full_run_causal_switch_and_deduplication(self):
        with tempfile.TemporaryDirectory() as d, patch.object(exp, 'OUT', Path(d)), contextlib.redirect_stdout(io.StringIO()):
            adapter = self.adapter()
            exp.run(self.cases, adapter)
            metrics = json.loads((Path(d) / 'metrics.json').read_text())
            gate = json.loads((Path(d) / 'gate.json').read_text())
            logical = json.loads((Path(d) / 'logical_branches.json').read_text())
            self.assertEqual(len(adapter.calls), 146)
            self.assertTrue(gate['passed'])
            self.assertEqual(metrics['NPR'], dict(count=6, denominator=6, rate=1.0))
            self.assertEqual(metrics['SCS']['rate'], 1)
            self.assertEqual(metrics['CCS']['rate'], 1)
            self.assertEqual(logical[self.cases[0]['case_id']]['N0'], logical[self.cases[0]['case_id']]['W0'])
            self.assertEqual(logical[self.cases[-1]['case_id']]['N0'], logical[self.cases[-1]['case_id']]['C0'])

    def test_lookup_failure_stops_before_branch_interpretation(self):
        with tempfile.TemporaryDirectory() as d, patch.object(exp, 'OUT', Path(d)), contextlib.redirect_stdout(io.StringIO()):
            adapter = self.adapter(fail_lookup=True)
            exp.run(self.cases, adapter)
            metrics = json.loads((Path(d) / 'metrics.json').read_text())
            self.assertEqual(len(adapter.calls), 100)
            self.assertEqual(metrics['CLA_all']['rate'], 0.9)
            self.assertIsNone(metrics['NPR']['rate'])

    def test_all_registered_targets_traced(self):
        case = self.cases[0]
        wrong = case['registered_wrong']
        other = next(p for p in case['candidates'] if p['name'] not in (case['B'], wrong))
        row = exp.parse_answer(other['target'])
        self.assertEqual(exp.downstream_label(case, row, wrong)[0], 'OTHER_CANDIDATE_TARGET')
        self.assertEqual(exp.downstream_label(case, exp.parse_answer('Unsupported Place'), wrong)[0], 'OUT_OF_UNIVERSE')


if __name__ == '__main__':
    unittest.main()
