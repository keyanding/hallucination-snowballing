import unittest
from src.interface_v3_4_4 import parse_natural
from src.analysis_v3_4_4 import modal, natural_gate, cell_summary, summarize
from src.prepare_v3_4_4 import make_cases, plans_for


class V344Tests(unittest.TestCase):
    def test_parser_categories(self):
        names=['Ada Vale','Ben Cove','Cara Reed','Dion Lake']
        for raw,trunc,expected in [('Ada Vale',False,'IN_SET_VALID'),(' Ada Vale\n',False,'IN_SET_VALID'),
            ('Eve Hill',False,'OUT_OF_SET'),('Ada Vale or Ben Cove',False,'AMBIGUOUS'),
            ('The answer is Ada Vale.',False,'NONCOMPLIANT'),('Ada Vale\nWait...',False,'NONCOMPLIANT'),
            ('Ada Vale',True,'TRUNCATED'),('',False,'NONCOMPLIANT')]:
            self.assertEqual(parse_natural(raw,names,trunc)['category'],expected)
        self.assertEqual(parse_natural('A. Vale',names,aliases={'A. Vale':'Ada Vale'})['identity'],'Ada Vale')
        self.assertIsNone(parse_natural('Ada Vale because...',names)['identity'])
    def test_modal_ties(self):
        self.assertIsNone(modal(['a','a','b','b']))
        self.assertEqual(modal(['a','a','a','b']),'a')
    def test_fresh_cases_and_invariance(self):
        dev,confirmation,old=make_cases()
        self.assertEqual((len(dev),len(confirmation)),(24,16))
        self.assertFalse({c['target'] for c in dev+confirmation}&{c['target'] for c in old})
        self.assertEqual(len({tuple(sorted(p['name'] for p in c['candidates'])) for c in dev+confirmation}),40)
        plans=plans_for(dev,'development')
        self.assertEqual(len(plans),648)
        for p in plans:
            if p['interface']=='N':
                self.assertNotIn('\n\nCandidate names:\n',p['prompt'])
                r=next(q for q in plans if q['case_id']==p['case_id'] and q['difficulty']==p['difficulty'] and q['interface']=='R' and q['rotation']==1)
                self.assertEqual(p['prompt'],r['prompt'])
    def test_aggregate_never_uses_invalid_fourth_vote(self):
        names=['Ada Vale','Ben Cove','Cara Reed','Dion Lake']
        def row(interface, rotation, identity, valid=True):
            return dict(case_id='mock',difficulty='EASY',gold=names[0],interface=interface,
                rotation=rotation,candidate_order=names,record_order=names[rotation-1:]+names[:rotation-1],
                F=dict(identity=identity if valid else None,strict_valid=valid,category='IN_SET_VALID' if valid else 'NONCOMPLIANT'),
                C=dict(selected_candidate=identity),S=dict(scores=[dict(candidate=n,mean_logprob_per_token=-i) for i,n in enumerate(names)]))
        rows=[row('N',1,names[1])]+[row('R',i,names[1],i!=4) for i in range(1,5)]
        c=cell_summary(rows)
        self.assertIsNone(c['R']['aggregate'])
        self.assertFalse(c['R']['stable_three_of_four'])
        stats=summarize([c])
        self.assertEqual(stats['R_wrong_given_valid']['denominator'],3)
        self.assertEqual(stats['R_wrong_all']['denominator'],4)
        rows[-1]=row('R',4,names[0])
        c=cell_summary(rows)
        self.assertEqual(c['R']['aggregate'],names[1])
        self.assertEqual(c['R']['wrong_label'],'AGGREGATED_TRACEABLE_WRONG')
        self.assertFalse(c['R']['stable_four_of_four'])

    def test_gate_threshold_and_missing_agreement(self):
        stats={k:{'rate':v,'count':1} for k,v in [('N_coverage',.9),('R_stable_three_of_four',.75),('R_stable_four_of_four',.5),('R_earliest',.39),('N_L_agreement',.85),('N_wrong_all',.1)]}
        self.assertTrue(natural_gate(stats,'N')['passed'])
        stats['R_earliest']['rate']=.4
        self.assertFalse(natural_gate(stats,'N')['passed'])
        stats['R_earliest']['rate']=.39
        stats['N_L_agreement']['rate']=None
        self.assertFalse(natural_gate(stats,'N')['passed'])


if __name__=='__main__':
    unittest.main()
