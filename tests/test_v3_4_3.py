import unittest

from src.analysis_v3_4_3 import classify, set_summary, analyze, CASE_IDS, CONDITIONS
from src.calibration_v3_4_3 import build_plan, rotate_prompt, split_prompt


def fake_rows(choices, cid='dev-04', difficulty='EASY', boost=0):
    names=['A','B','C','D']
    rows=[]
    for i,choice in enumerate(choices):
        order=names[i:]+names[:i]
        scores=[dict(candidate=name,mean_logprob_per_token=(0 if name=='A' else -1)+(boost if p==0 else 0)) for p,name in enumerate(order)]
        top=max(scores,key=lambda s:s['mean_logprob_per_token'])['candidate']
        rows.append(dict(case_id=cid,difficulty=difficulty,permutation=i+1,gold='A',gold_position=order.index('A')+1,
            C=dict(candidate_order=order,selected_candidate=choice,exact_allowed_candidate=True),
            L=dict(scores=scores,top_candidate_by_mean_logprob=top),
            F=dict(exact_candidate_only=True,strict_candidate=choice,contains_exactly_one_candidate=True,extractable_candidate=choice,truncated=False,out_of_set_name=None)))
    return rows


class OrderControlTests(unittest.TestCase):
    def test_exact_72_order_only_plans(self):
        cases,plans=build_plan()
        self.assertEqual([c['case_id'] for c in cases],list(CASE_IDS))
        self.assertEqual(len(plans),72)
        for cid in CASE_IDS:
            for difficulty in CONDITIONS:
                group=[p for p in plans if p['case_id']==cid and p['difficulty']==difficulty]
                left,names,right=split_prompt(group[0]['prompt'])
                self.assertEqual(len(group),4)
                for p in group:
                    a,b,c=split_prompt(p['prompt'])
                    self.assertEqual(a,left)
                    self.assertEqual(c,right)
                    self.assertEqual(set(b),set(names))
                    self.assertEqual(p['gold'],group[0]['gold'])
                for name in names:
                    self.assertEqual({p['candidate_order'].index(name)+1 for p in group},{1,2,3,4})

    def test_rotation_round_trip_and_bad_list(self):
        text='Intro\n\nCandidate names:\n1. A\n2. B\n3. C\n4. D\n\nCandidate-name records:\nEvidence'
        self.assertEqual(rotate_prompt(text,1)[0],text)
        self.assertEqual(rotate_prompt(text,2)[1],['B','C','D','A'])
        with self.assertRaises(AssertionError):
            split_prompt(text.replace('4. D','4. A'))
        with self.assertRaises(AssertionError):
            rotate_prompt(text,5)

    def test_classification_priority(self):
        self.assertEqual(classify(fake_rows(['A']*4)),'GOLD_STABLE')
        self.assertEqual(classify(fake_rows(['B']*4)),'IDENTITY_LOCKED')
        self.assertEqual(classify(fake_rows(['A','B','C','B'])),'POSITION_1_LOCKED')
        self.assertEqual(classify(fake_rows(['A','A','B','B'])),'MIXED_POSITION_IDENTITY')
        self.assertEqual(classify(fake_rows(['B','C','D','A'])),'UNSTABLE_OTHER')

    def test_identity_lock_not_strict_position_following(self):
        s=set_summary(fake_rows(['C']*4))
        self.assertEqual(s['ISR'],1)
        self.assertEqual(s['PFR']['count'],1)
        self.assertEqual(s['PFR']['denominator'],3)
        self.assertEqual(s['strict_PFR']['count'],0)
        self.assertEqual(s['strict_conditional_PFR']['rate'],0)

    def test_pure_position_following(self):
        s=set_summary(fake_rows(['A','B','C','D']))
        self.assertEqual(s['ISR'],.25)
        self.assertEqual(s['PFR']['rate'],1)
        self.assertEqual(s['strict_PFR']['rate'],1)
        self.assertEqual(s['classification'],'POSITION_1_LOCKED')

    def test_identity_matched_delta_and_zero_sum(self):
        s=set_summary(fake_rows(['A','B','C','D'],boost=2))
        for effect in s['identity_position_effects'].values():
            self.assertAlmostEqual(effect['delta_by_position']['1'],2)
            for p in ('2','3','4'):
                self.assertAlmostEqual(effect['delta_by_position'][p],-2/3)
            self.assertAlmostEqual(sum(effect['delta_by_position'].values()),0)

    def test_repeated_measures_denominators(self):
        rows=[r for cid in CASE_IDS for d in CONDITIONS for r in fake_rows(['A','B','C','D'],cid,d,boost=2)]
        m=analyze(rows)
        self.assertEqual(m['overall']['prompt_count'],72)
        self.assertEqual(m['overall']['set_count'],18)
        self.assertEqual(m['overall']['case_count'],6)
        self.assertEqual(m['overall']['PFR']['denominator'],54)
        self.assertEqual(m['overall']['GPA']['1']['denominator'],18)
        self.assertEqual(m['overall']['GPA']['1']['rate'],1)
        self.assertEqual(m['overall']['GPA']['2']['rate'],0)
        self.assertTrue(m['descriptive_outcome_flags']['A_strong_position'])
        self.assertFalse(m['frontier_salvage']['MID']['heuristic_frontier_like'])
        self.assertFalse(any(m['diagnostic_routes'].values()))

    def test_stable_gold_counterbalances_selection_positions(self):
        rows=[r for cid in CASE_IDS for d in CONDITIONS for r in fake_rows(['A']*4,cid,d)]
        m=analyze(rows)
        self.assertEqual(m['overall']['mean_ISR'],1)
        self.assertTrue(all(v['rate']==.25 for v in m['overall']['PSR'].values()))
        self.assertTrue(all(v['rate']==1 for v in m['overall']['GPA'].values()))
        self.assertEqual(m['overall']['classifications'],{'GOLD_STABLE':18})


if __name__=='__main__':
    unittest.main()
