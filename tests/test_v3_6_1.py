import copy
import unittest
from experiments.v3_6_0.design import make_cases
from experiments.v3_6_1.design import build_cases, audit_pair, render, parse, FAMILIES, RULE
from experiments.v3_6_1.analyze import stage_b, stage_c, decision
from experiments.v3_6_1.run import execute


class FixedTokenizer:
    def encode(self, text, **kwargs):
        return [1, 2, 3, 4]


class MinimalAssayTests(unittest.TestCase):
    def fixtures(self):
        old, oldmain = make_cases()
        cases, controls, _, _, _ = build_cases(FixedTokenizer(), old+oldmain)
        def output(row):
            return row | dict(raw_text=row['expected'], truncated=False)
        b = [output(r) for c in old for f in FAMILIES for r in audit_pair(c, f)]
        c = [output(r) for case in cases for r in audit_pair(case)]
        u = [output(render(case, 'UNMAPPED')) for case in controls]
        rev = [output(r) for case in cases[:10] for r in audit_pair(case, reverse=True)]
        return old, cases, controls, b, c, u, rev

    def test_token_and_lexical_selection_is_deterministic(self):
        old = sum(make_cases(), [])
        a = build_cases(FixedTokenizer(), old)
        b = build_cases(FixedTokenizer(), old)
        self.assertEqual(a, b)
        self.assertEqual(len(a[2]), 5200)
        self.assertEqual(sum(r['selected'] for r in a[3]), 210)
        self.assertFalse(a[4]['selection_uses_model_outputs'])

    def test_controlled_unknown_factor_and_state_diffs(self):
        for case in make_cases()[0]:
            for shape in ('FULL', 'MINIMAL'):
                a, b = audit_pair(case, shape+'_NO_UNKNOWN')
                self.assertNotIn('UNKNOWN', a['prompt'])
                self.assertEqual(a['prompt']+'\n'+RULE, render(case, 'C0', shape+'_UNKNOWN')['prompt'])
                self.assertEqual(a['mappings'], b['mappings'])

    def test_parser_has_no_casefold_or_extraction(self):
        c = dict(gold_outcome='OUTCOME_A12', wrong_outcome='OUTCOME_Z45', expected='OUTCOME_A12')
        self.assertTrue(parse(' OUTCOME_A12. ', c)['correct'])
        for raw in ('outcome_a12', 'OUTCOME_A12 because...', 'OUTCOME_A12..', 'unknown'):
            self.assertEqual(parse(raw, c)['category'], 'INVALID')
        self.assertEqual(parse('OUTCOME_B67', c)['category'], 'OTHER')
        self.assertEqual(parse('OUTCOME_A12', c, True)['category'], 'INVALID')

    def test_full_pass_and_ties_are_reported(self):
        old, cases, controls, b, c, u, rev = self.fixtures()
        bm, cm = stage_b(old, b)[1], stage_c(cases, controls, c, u, rev)[1]
        self.assertEqual(decision(bm, cm), 'MINIMAL_ASSAY_VALIDATED')
        self.assertEqual(bm['best_descriptive_conditions'], list(FAMILIES))
        self.assertEqual(cm['record_order']['count'], 20)
        self.assertEqual(cm['metrics']['S']['count'], 40)

    def test_C1_C2_C3_boundaries(self):
        _, cases, controls, _, base, u, rev = self.fixtures()
        c = copy.deepcopy(base)
        c[0]['raw_text'] = c[1]['expected']
        c[1]['raw_text'] = base[0]['expected']
        m = stage_c(cases, controls, c, u, rev)[1]
        self.assertTrue(all(m['gates'][k] for k in ('C1', 'C2', 'C3')))
        c[2]['raw_text'] = c[3]['expected']
        m = stage_c(cases, controls, c, u, rev)[1]
        self.assertFalse(m['gates']['C1'])
        self.assertFalse(m['gates']['C3'])
        self.assertTrue(m['gates']['C2'])
        c[3]['raw_text'] = base[2]['expected']
        self.assertFalse(stage_c(cases, controls, c, u, rev)[1]['gates']['C2'])

    def test_C3_fails_with_disjoint_single_arm_errors(self):
        _, cases, controls, _, c, u, rev = self.fixtures()
        c[0]['raw_text'] = c[1]['expected']
        c[3]['raw_text'] = c[2]['expected']
        m = stage_c(cases, controls, c, u, rev)[1]
        self.assertTrue(m['gates']['C1'] and m['gates']['C2'])
        self.assertFalse(m['gates']['C3'])

    def test_C4_C5_C6_boundaries(self):
        _, cases, controls, _, c, u, rev = self.fixtures()
        c[0]['raw_text'] = 'UNKNOWN'
        m = stage_c(cases, controls, c, u, rev)[1]
        self.assertFalse(m['gates']['C4'])
        self.assertTrue(m['gates']['C5'])
        c[0]['raw_text'] = 'explanation'
        self.assertTrue(stage_c(cases, controls, c, u, rev)[1]['gates']['C5'])
        c[1]['raw_text'] = 'explanation'
        self.assertFalse(stage_c(cases, controls, c, u, rev)[1]['gates']['C5'])
        u[0]['raw_text'] = controls[0]['gold_outcome']
        self.assertTrue(stage_c(cases, controls, c, u, rev)[1]['gates']['C6'])
        u[1]['raw_text'] = controls[1]['gold_outcome']
        self.assertFalse(stage_c(cases, controls, c, u, rev)[1]['gates']['C6'])

    def test_order_is_separate_and_requires_mapped_identity(self):
        old, cases, controls, b, c, u, rev = self.fixtures()
        rev[0]['raw_text'] = 'UNKNOWN'
        self.assertTrue(stage_c(cases, controls, c, u, rev)[1]['record_order']['passed'])
        rev[1]['raw_text'] = 'UNKNOWN'
        cm = stage_c(cases, controls, c, u, rev)[1]
        self.assertFalse(cm['record_order']['passed'])
        self.assertEqual(decision(stage_b(old, b)[1], cm), 'MINIMAL_ASSAY_VALIDATED')

    def test_exact_paired_family_transitions_and_P3(self):
        old, _, _, b, _, _, _ = self.fixtures()
        selected = [r for r in b if r['family'] == 'MINIMAL_NO_UNKNOWN']
        selected[0]['raw_text'] = 'UNKNOWN'
        self.assertFalse(stage_b(old, b)[1]['P3'])
        selected[1]['raw_text'] = 'UNKNOWN'
        m = stage_b(old, b)[1]
        self.assertTrue(m['P3'])
        t = m['paired_transitions']['MINIMAL_UNKNOWN -> MINIMAL_NO_UNKNOWN']
        self.assertEqual(t['broken'], 2)
        self.assertEqual(t['corrected'], 0)
        self.assertEqual(len(t['cases']), 40)

    def test_stage_B_errors_do_not_block_stage_C(self):
        _, _, _, b, c, u, rev = self.fixtures()
        seen = []
        plans = dict(stage_b=b, stage_c=c, unmapped=u, record_order=rev)
        execute(plans, lambda row:dict(raw_text='INVALID', truncated=False), lambda stage, row:seen.append(stage))
        self.assertEqual(len(seen), 270)
        self.assertEqual(seen.count('stage_c'), 80)

    def test_incomplete_is_infrastructure_failure(self):
        old, cases, controls, b, c, u, rev = self.fixtures()
        bm = stage_b(old, b)[1]
        self.assertEqual(decision(bm, stage_c(cases, controls, c[:-1], u, rev)[1]), 'INFRASTRUCTURE_FAILURE')
        self.assertEqual(decision(bm, stage_c(cases, controls, c, u, rev[:-1])[1]), 'INFRASTRUCTURE_FAILURE')
        with self.assertRaises(AssertionError):
            stage_b(old, b+[b[0]])


if __name__ == '__main__':
    unittest.main()
