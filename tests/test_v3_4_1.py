import unittest
from collections import Counter

from src.calibration_choice import CandidateTrie, free_fields
from src.calibration_v3_4_1 import load, select
from src.prepare_v3_4_1 import MECHANISMS, LEVELS, evidence, resolve_rendered


class CalibrationTests(unittest.TestCase):
    def test_trie_prefix_candidate_and_reachability(self):
        trie=CandidateTrie([[1],[1,2],[3,4],[3,5]],99)
        self.assertTrue(trie.audit())
        self.assertEqual(trie.allowed([1]),[2,99])
        self.assertEqual(trie.allowed([3]),[4,5])
        with self.assertRaises(ValueError): trie.allowed([7])
        with self.assertRaises(ValueError): CandidateTrie([[1],[1]],99)

    def test_free_format_not_semantic_error(self):
        names=['Alice','Bob','Carol','Dan']
        self.assertTrue(free_fields('Alice',names)['exact_candidate_only'])
        result=free_fields('The director is Alice.',names)
        self.assertFalse(result['exact_candidate_only'])
        self.assertEqual(result['extractable_candidate'],'Alice')
        self.assertTrue(free_fields('Alice or Bob',names)['contains_multiple_candidates'])
        self.assertIsNone(free_fields('Alice or Bob',names)['extractable_candidate'])
        self.assertFalse(free_fields('Alice',names,True)['exact_candidate_only'])
        self.assertFalse(free_fields('Alicea',names)['contains_exactly_one_candidate'])

    def test_dataset_and_all_rendered_paths(self):
        dev,held=load('dev_cases.json'),load('heldout_cases.json')
        self.assertEqual(len({c['A'] for c in dev+held}),36)
        for m in MECHANISMS:
            group=[c for c in dev if c['mechanism']==m]
            self.assertEqual(len(group),6)
            self.assertEqual(sorted(Counter(c['gold_position'] for c in group).values()),[1,1,2,2])
        self.assertEqual(list(Counter(c['gold_position'] for c in held).values()),[3]*4)
        for c in dev+held:
            self.assertEqual(len({x['target'] for x in c['candidates']}),4)
            self.assertEqual(Counter(evidence(c,'M3','D2')),Counter(evidence(c,'M3','D3')))
            for m in ([c['mechanism']] if c['split']=='dev' else MECHANISMS):
                for d in LEVELS:
                    gold,steps=resolve_rendered(c,m,d)
                    self.assertEqual(gold,c['B'])
                    if m=='M4': self.assertEqual(steps,dict(D0=1,D1=2,D2=3,D3=3)[d])

    def test_frontier_lowest_and_bias_block(self):
        def level(rate):
            return dict(TWER_C=dict(rate=rate),near_boundary=dict(count=4),POSITION_BIAS=False,LCA=dict(rate=1),free_outset=dict(rate=0))
        levels={d:level(r) for d,r in zip(LEVELS,[0,1/3,1/3,.5])}
        self.assertEqual(select(levels)['difficulty'],'D1')
        self.assertTrue(select(levels)['provisional'])
        levels['D3']['POSITION_BIAS']=True
        self.assertFalse(select(levels)['provisional'])
        levels={d:level(0) for d in LEVELS}
        self.assertEqual(select(levels)['status'],'NO_STABLE_FRONTIER_FOUND')
        self.assertEqual(select(levels)['difficulty'],'D0')


if __name__=='__main__': unittest.main()
