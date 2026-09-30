import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import Mock

from src.experiment_v3 import (CONDITIONS, IndependentHFAdapter, analyze, audit_prompts, build_prompt, export_results,
                               label_output, make_synthetic_cases, parse_answer, prepare, run)


class ContextAdapter:
    def __init__(self, cases, override=False):
        self.outputs = {}
        self.calls = []
        for case in cases:
            for condition in CONDITIONS:
                for order in (1, 2):
                    answer = case['C_prime'] if condition.endswith('_prime') else case['C']
                    if override and condition == 'state_B_prime':
                        answer = case['C']
                    self.outputs[build_prompt(case, condition, order)] = answer

    def generate(self, prompt, **kwargs):
        self.calls.append(prompt)
        return dict(raw_generation=self.outputs[prompt], truncated=False)


class V3Tests(unittest.TestCase):
    def setUp(self):
        self.cases = make_synthetic_cases()

    def get_records(self, override=False):
        with tempfile.TemporaryDirectory() as directory, contextlib.redirect_stdout(io.StringIO()):
            return run(self.cases, ContextAdapter(self.cases, override), Path(directory))

    def test_fixed_balanced_distinct_dataset(self):
        self.assertEqual(self.cases, make_synthetic_cases())
        self.assertNotEqual(self.cases, make_synthetic_cases(7))
        self.assertEqual(len({row[k] for row in self.cases for k in ('B', 'C', 'B_prime', 'C_prime')}), 40)

    def test_only_state_changes_and_order_preserves_question(self):
        self.assertTrue(audit_prompts(self.cases)['state_field_only_difference'])
        for case in self.cases:
            for condition in CONDITIONS:
                first, second = (build_prompt(case, condition, order) for order in (1, 2))
                self.assertEqual(first.split('\n\n', 1)[1], second.split('\n\n', 1)[1])
                for banned in ('oracle', 'injected', 'false', 'hallucination', '<', '>'):
                    self.assertNotIn(banned, first)

    def test_complete_perfect_run_and_artifacts(self):
        with tempfile.TemporaryDirectory() as directory, contextlib.redirect_stdout(io.StringIO()):
            out = Path(directory) / 'smoke'
            prepare(out, 42)
            adapter = ContextAdapter(self.cases)
            records = run(self.cases, adapter, out)
            self.assertEqual(len(adapter.calls), 80)
            self.assertTrue(all('Current Step 1 state' not in p for p in adapter.calls[:40]))
            metrics, gate = analyze(self.cases, records)
            self.assertTrue(gate['passed'])
            self.assertEqual(metrics['propagation_rate'], dict(count=20, denominator=20, rate=1.0))
            self.assertFalse(gate['scale_authorized'])
            export_results(out, self.cases, records)
            self.assertEqual(json.loads((out / 'gate.json').read_text())['eligible_cases'], 10)
            self.assertIn('<table>', (out / 'inspection.md').read_text(encoding='utf-8'))
            with self.assertRaises(FileExistsError):
                run(self.cases, adapter, out)
            with self.assertRaises(FileExistsError):
                prepare(out, 42)

    def test_gate_does_not_require_desired_propagation_outcome(self):
        metrics, gate = analyze(self.cases, self.get_records(override=True))
        self.assertTrue(gate['passed'])
        self.assertEqual(metrics['propagation_rate']['rate'], 0)
        self.assertEqual(metrics['override_rate']['rate'], 1)
        self.assertEqual(len(metrics['state_frame_interference']), 20)

    def test_lookup_failure_excludes_case_both_orders(self):
        records = self.get_records()
        records[0].update(gate_pass=False, label='UNKNOWN_REJECT', parsed_answer='Unknown')
        metrics, _ = analyze(self.cases, records)
        self.assertEqual(metrics['eligible_cases'], 9)
        self.assertEqual(metrics['propagation_rate']['denominator'], 18)
        self.assertEqual(metrics['context_lookup_accuracy_all']['count'], 39)

    def test_state_frame_and_order_failures_block_gate(self):
        records = self.get_records()
        for row in records:
            if row['condition'] == 'state_B' and row['evidence_order'] == 2:
                row.update(gate_pass=False, parsed_answer=row['C_prime'], label='OTHER_CONTEXT_TARGET')
        metrics, gate = analyze(self.cases, records)
        self.assertFalse(gate['passed'])
        self.assertFalse(gate['quantitative_checks']['baseline_frame'])
        self.assertFalse(gate['quantitative_checks']['evidence_order'])
        self.assertEqual(len(metrics['state_frame_interference']), 10)

    def test_zero_eligible_null_rates_and_incomplete_matrix(self):
        records = self.get_records()
        for row in records:
            if row['condition'].startswith('direct'):
                row.update(gate_pass=False, label='UNKNOWN_REJECT')
        metrics, gate = analyze(self.cases, records)
        self.assertFalse(gate['passed'])
        self.assertIsNone(metrics['propagation_rate']['rate'])
        with self.assertRaises(ValueError):
            analyze(self.cases, records[:-1])
        with self.assertRaises(ValueError):
            analyze(self.cases, records + [records[0]])

    def test_short_answer_outcomes_keep_refusals_and_invalid_separate(self):
        case = self.cases[0]
        for answer, label in ((case['C_prime'], 'PROPAGATE'), (case['C'], 'OVERRIDE_TO_GOLD'),
                              ('Zextravo', 'OUT_OF_CONTEXT_HALLUCINATION'), ('Unknown', 'UNKNOWN_REJECT'),
                              ('', 'UNKNOWN_REJECT'), ('<person>', 'INVALID_OUTPUT'),
                              ('Answer: Zextravo', 'INVALID_OUTPUT'), ('A → B', 'INVALID_OUTPUT')):
            row = case | parse_answer(answer) | dict(condition='state_B_prime', expected_answer=case['C_prime'])
            self.assertEqual(label_output(row), label)
        self.assertFalse(parse_answer(case['C'], truncated=True)['parse_valid'])

    def test_actual_adapter_path_has_fresh_messages_and_no_cache(self):
        class Inputs(dict):
            def __init__(self, text):
                self.input_ids = SimpleNamespace(shape=(1, 3))
                super().__init__(input_ids=self.input_ids, test_prompt=text)

            def to(self, device):
                return self

        class Output:
            def __getitem__(self, key):
                return SimpleNamespace(numel=lambda: 2)

        adapter = object.__new__(IndependentHFAdapter)
        adapter.torch = SimpleNamespace(manual_seed=Mock(), cuda=SimpleNamespace(is_available=lambda: False),
                                        inference_mode=contextlib.nullcontext)
        adapter.quantization, adapter.compute_dtype = '4bit-nf4', 'torch.bfloat16'
        adapter.model = SimpleNamespace(device='test', generate=Mock(return_value=Output()))
        adapter.tokenizer = Mock(side_effect=lambda text, **kwargs: Inputs(text))
        adapter.tokenizer.eos_token_id = 1
        adapter.tokenizer.apply_chat_template.side_effect = lambda messages, **kwargs: messages[0]['content']
        adapter.tokenizer.decode.return_value = 'Shortname'
        for prompt in ('first independent prompt', 'second independent prompt'):
            result = adapter.generate(prompt)
            self.assertFalse(result['isolation']['use_cache'])
            self.assertEqual(result['isolation']['previous_messages'], 0)
        calls = adapter.tokenizer.apply_chat_template.call_args_list
        self.assertEqual(calls[1].args[0], [{'role': 'user', 'content': 'second independent prompt'}])
        self.assertIsNot(calls[0].args[0], calls[1].args[0])
        for call in adapter.model.generate.call_args_list:
            self.assertFalse(call.kwargs['use_cache'])
            self.assertFalse(call.kwargs['do_sample'])
            self.assertNotIn('past_key_values', call.kwargs)


if __name__ == '__main__':
    unittest.main()
