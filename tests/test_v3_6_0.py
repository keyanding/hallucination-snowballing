import copy
import unittest
from unittest.mock import patch
from experiments.v3_6_0.design import make_cases, audit, parse, shuffled, UNKNOWN_RULE
from experiments.v3_6_0.analyze import calibration_metrics, main_metrics, decide, wilson
from experiments.v3_6_0.run import execute


class AssayTests(unittest.TestCase):
    def fixtures(self):
        cal, main = make_cases()
        def rows(cases, calibration):
            return [r | dict(raw_text=r['expected'], truncated=False) for c in cases for k, r in audit(c, True).items() if calibration or k in ('C0', 'W0')]
        return cal, main, rows(cal, True), rows(main, False)

    def test_disjoint_balanced_diffs_and_uniform_rule(self):
        cal, main = make_cases()
        self.assertEqual((len(cal), len(main)), (20, 40))
        for c in cal+main:
            for r in audit(c, True).values():
                self.assertEqual(r['prompt'].count(UNKNOWN_RULE), 1)
                self.assertFalse(r['auxiliary'])
        self.assertEqual(make_cases(), (cal, main))

    def test_parser_strictness_and_truncation(self):
        c = make_cases()[0][0]
        self.assertEqual(parse(' \n'+c['gold_outcome']+'. ', c)['category'], 'C')
        for raw in (c['gold_outcome'].lower(), c['gold_outcome']+' because...', c['gold_outcome']+'..', 'unknown', 'UNKNOWN or '+c['gold_outcome']):
            self.assertEqual(parse(raw, c)['category'], 'INVALID')
        self.assertEqual(parse(c['gold_outcome'], c, True)['category'], 'INVALID')
        other = next('Outcome_'+a+'00' for a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if 'Outcome_'+a+'00' not in (c['gold_outcome'], c['wrong_outcome']))
        self.assertEqual(parse(other, c)['category'], 'OTHER')
        self.assertEqual(parse('UNKNOWN.', c)['category'], 'UNKNOWN')

    def test_all_pass_and_paired_statistics(self):
        cal, main, cr, mr = self.fixtures()
        _, cm = calibration_metrics(cal, cr)
        _, mm = main_metrics(main, mr)
        self.assertEqual(decide(cm, mm), 'ASSAY_VALIDATED')
        self.assertEqual(mm['paired_transitions']['C']['Cp'], 40)
        self.assertEqual(mm['metrics']['delta_state']['rate'], 1)
        self.assertAlmostEqual(wilson(40, 40)[0], .912378, places=5)

    def test_each_calibration_gate_threshold(self):
        cal, _, rows, _ = self.fixtures()
        controls = dict(A=('LOOKUP_GOLD', 3), B=('C0', 2), C=('W0', 2), D=('SWAP', 2), E=('REVERSE', 2), F=('UNMAPPED', 3), H=('ENTITY_LABEL', 2))
        for gate, (condition, failures) in controls.items():
            changed = copy.deepcopy(rows)
            targets = [r for r in changed if r['condition'] == condition]
            for r in targets[:failures-1]:
                r['raw_text'] = 'UNKNOWN' if condition != 'UNMAPPED' else cal[0]['gold_outcome']
            _, metrics = calibration_metrics(cal, changed)
            self.assertTrue(metrics['gates'][gate]['passed'], gate)
            targets[failures-1]['raw_text'] = 'UNKNOWN' if condition != 'UNMAPPED' else cal[0]['gold_outcome']
            _, metrics = calibration_metrics(cal, changed)
            self.assertFalse(metrics['gates'][gate]['passed'], gate)
            self.assertEqual(decide(metrics, {}), 'STOP_ASSAY_INVALID')

    def test_parse_gate_159_of_160(self):
        cal, _, rows, _ = self.fixtures()
        rows[0]['raw_text'] = 'explanation'
        self.assertTrue(calibration_metrics(cal, rows)[1]['gates']['G']['passed'])
        rows[1]['raw_text'] = 'explanation'
        self.assertFalse(calibration_metrics(cal, rows)[1]['gates']['G']['passed'])

    def test_entity_invariance_is_same_case_comparison(self):
        cal, _, rows, _ = self.fixtures()
        for r in rows:
            if r['condition'] in ('C0', 'ENTITY_LABEL'):
                r['raw_text'] = cal[int(r['case_id'][-3:])-1]['wrong_outcome']
        cm = calibration_metrics(cal, rows)[1]
        self.assertEqual(cm['gates']['H']['count'], 20)
        self.assertFalse(cm['gates']['B']['passed'])

    def test_main_gate_boundaries_and_unknown_separate(self):
        _, main, _, rows = self.fixtures()
        for r in rows:
            if int(r['case_id'][-3:]) <= 2:
                r['raw_text'] = 'UNKNOWN'
        mm = main_metrics(main, rows)[1]
        self.assertTrue(mm['passed'])
        self.assertEqual(mm['other_plus_invalid']['count'], 0)
        next(r for r in rows if r['condition'] == 'C0' and r['case_id'].endswith('003'))['raw_text'] = 'UNKNOWN'
        self.assertFalse(main_metrics(main, rows)[1]['gates']['G1'])
        empty = main_metrics(main, [])[1]
        self.assertIsNone(empty['metrics']['S']['rate'])
        self.assertIsNone(empty['metrics']['S']['wilson_95'])

    def test_remaining_main_gate_boundaries(self):
        _, main, _, original = self.fixtures()
        rows = copy.deepcopy(original)
        for r in rows:
            i = int(r['case_id'][-3:])
            if (r['condition'] == 'C0' and i <= 2) or (r['condition'] == 'W0' and 3 <= i <= 4):
                r['raw_text'] = 'UNKNOWN'
        mm = main_metrics(main, rows)[1]
        self.assertEqual(mm['metrics']['S']['count'], 36)
        self.assertTrue(mm['gates']['G3'])
        next(r for r in rows if r['condition'] == 'W0' and r['case_id'].endswith('005'))['raw_text'] = 'UNKNOWN'
        mm = main_metrics(main, rows)[1]
        self.assertFalse(mm['gates']['G2'])
        self.assertFalse(mm['gates']['G3'])
        rows = copy.deepcopy(original)
        for r in rows:
            if r['condition'] == 'C0' and int(r['case_id'][-3:]) <= 2:
                r['raw_text'] = main[int(r['case_id'][-3:])-1]['wrong_outcome']
        self.assertTrue(main_metrics(main, rows)[1]['gates']['G4'])
        next(r for r in rows if r['condition'] == 'C0' and r['case_id'].endswith('003'))['raw_text'] = main[2]['wrong_outcome']
        self.assertFalse(main_metrics(main, rows)[1]['gates']['G4'])
        rows = copy.deepcopy(original)
        for r in rows[:2]:
            r['raw_text'] = 'malformed'
        self.assertTrue(main_metrics(main, rows)[1]['gates']['G5'])
        rows[2]['raw_text'] = 'malformed'
        self.assertFalse(main_metrics(main, rows)[1]['gates']['G5'])

    def test_call_order_and_failed_calibration_never_runs_main(self):
        cal, _, rows, mainrows = self.fixtures()
        schedule, _ = shuffled(rows, 360)
        self.assertTrue(all(a['case_id'] != b['case_id'] for a, b in zip(schedule, schedule[1:])))
        invoked = []
        def invoke(row):
            invoked.append(row['split'])
            return dict(raw_text='broken', truncated=False)
        with patch('experiments.v3_6_0.run.load', return_value=cal), patch('experiments.v3_6_0.run.write'):
            self.assertFalse(execute(dict(calibration=rows, main=mainrows), invoke, lambda *args: None))
        self.assertEqual(invoked, ['calibration']*160)


if __name__ == '__main__':
    unittest.main()
