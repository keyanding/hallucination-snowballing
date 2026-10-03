import copy
from collections import Counter
import unittest

from src.analysis_v3_4_2 import select, monotonicity, case_diagnostics
from src.graph_v3_4_2 import GRID, audit_prompt, make_cases, name_records, render, key


class GraphCalibrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dev,cls.held=make_cases()

    def test_disjoint_balanced_reproducible_splits(self):
        self.assertEqual((self.dev,self.held),make_cases())
        self.assertEqual(len(self.dev),8)
        self.assertEqual(len(self.held),12)
        self.assertEqual(len({c['target'] for c in self.dev+self.held}),20)
        self.assertEqual(Counter(c['gold_position'] for c in self.dev),{1:2,2:2,3:2,4:2})
        self.assertEqual(Counter(c['gold_position'] for c in self.held),{1:3,2:3,3:3,4:3})

    def test_all_240_graphs_and_prompt_invariants(self):
        for c in self.dev+self.held:
            baseline=render(c,1,0)
            prefix=baseline.split('Graph-link records:')[0]
            suffix=baseline.split('\n\nWhich candidate')[1]
            for d,b in GRID:
                text=render(c,d,b)
                result=audit_prompt(c,d,b,text)
                self.assertEqual(result['unique_queried_endpoint'],c['gold'])
                self.assertEqual(result['link_count'],d*(b+1))
                self.assertEqual(result['path_depth'],d)
                self.assertEqual(text.split('Graph-link records:')[0],prefix)
                self.assertEqual(text.split('\n\nWhich candidate')[1],suffix)
                self.assertTrue(all(line in text for line in name_records(c)))

    def test_duplicate_queried_path_rejected(self):
        c=self.dev[0]
        text=render(c,2,1)
        text+='\nFilm '+c['target']+' has credited-director link '+c['name_nodes'][c['paths'][1]['endpoint']]+'.'
        with self.assertRaises(AssertionError):
            audit_prompt(c,2,1,text)

    def test_branch_label_change_is_ambiguous(self):
        c=self.dev[0]
        text=render(c,3,1).replace('has comparison-director link','has credited-director link')
        with self.assertRaises(AssertionError):
            audit_prompt(c,3,1,text)

    def grid(self):
        return {key(d,b):dict(ER=dict(rate=0),GM=3,NBF=dict(count=0),FCA=dict(rate=1),
                 LCA=dict(rate=1),POSITION_BIAS=False,unique_path_audit=True,C_valid=dict(rate=1)) for d,b in GRID}

    def test_selection_all_thresholds_and_at_most_two(self):
        grid=self.grid()
        for name in ['D1B1','D2B0','D2B1']:
            grid[name].update(ER=dict(rate=.25),GM=.5,NBF=dict(count=3))
        grid['D2B1']['GM']=.4
        result=select(grid)
        self.assertEqual(result['selected'],['D1B1','D2B0'])
        self.assertEqual(result['qualifying_not_selected'],['D2B1'])
        grid['D1B1']['NBF']['count']=2
        self.assertNotIn('D1B1',select(grid)['selected'])
        self.assertEqual(select(grid,True)['selected'],[])

    def test_isolated_flat_cell_has_no_local_support(self):
        grid=self.grid()
        for name in ('D1B1','D2B0','D2B1'):
            grid[name].update(ER=dict(rate=.25),GM=.5,NBF=dict(count=3))
        result=select(grid)['conditions']['D2B1']
        self.assertFalse(result['checks']['local_trend'])
        grid['D1B1']['GM']=.6
        self.assertTrue(select(grid)['conditions']['D2B1']['checks']['local_trend'])

    def test_monotonic_denominators_and_zero_error_ties(self):
        grid=self.grid()
        for d,b in GRID:
            grid[key(d,b)]['GM']=-d-b
        result=monotonicity(grid)
        self.assertEqual(result['depth']['GM']['denominator'],9)
        self.assertEqual(result['branches']['GM']['denominator'],8)
        self.assertEqual(result['depth']['ER']['rate'],1)
        self.assertEqual(result['depth']['strictly_increasing_ER'],0)

    def test_boundary_and_recovery_can_coexist(self):
        rows=[]
        for d,b in GRID:
            gm=-.5 if (d,b)==(2,1) else 2
            rows.append(dict(depth=d,branches=b,gold='A',C=dict(selected_candidate='B' if gm<0 else 'A'),
                             L=dict(scores=[dict(candidate='A',mean_logprob_per_token=gm),dict(candidate='B',mean_logprob_per_token=0)])))
        result=case_diagnostics(rows)
        self.assertIn('CASE_BOUNDARY_CROSSING',result['labels'])
        self.assertIn('CASE_NON_MONOTONIC',result['labels'])
        self.assertTrue(any(c['recovery'] for c in result['comparisons']))


if __name__=='__main__':
    unittest.main()
