import copy
import unittest
from collections import Counter
from experiments.v3_6_2.design import make_cases,block,audit_pair,parse,KS,BANDS
from experiments.v3_6_2.analyze import main_metrics,diagnostic_metrics,decide
from experiments.v3_6_2.run import execute


class FixedTokenizer:
    def encode(self,value,**kwargs):
        return [1,2,3,4]


class ContextAssayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases,cls.selected,cls.pool,cls.audit,cls.checks=make_cases(FixedTokenizer(),set())

    def fixtures(self):
        def output(r):
            return r|dict(raw_text=r['expected'],truncated=False,output_token_ids=list(r['expected'].encode()))
        main=[output(r) for c in self.cases for k in KS for r in audit_pair(c,k)]
        diagnostic=[output(r) for c in self.cases if c['case_id'] in self.selected for band in BANDS for r in audit_pair(c,24,band)]
        return main,diagnostic

    def change(self,rows,k,case_index,arm,value='UNKNOWN'):
        row=next(r for r in rows if r['k']==k and r['case_id']==self.cases[case_index]['case_id'] and r['condition']==arm)
        row['raw_text']=value

    def test_fresh_balanced_token_family(self):
        self.assertEqual(len(self.pool),5200)
        self.assertEqual(sum(r['selected'] for r in self.audit),2080)
        self.assertEqual(Counter(c['position_band'] for c in self.cases),dict(beginning=14,middle=13,end=13))
        chosen=[c for c in self.cases if c['case_id'] in self.selected]
        self.assertEqual(Counter(c['position_band'] for c in chosen),dict(beginning=4,middle=4,end=4))
        self.assertEqual(sum(c['record_order'][0]=='gold' for c in chosen),6)
        again=make_cases(FixedTokenizer(),set())
        self.assertEqual(again[0],self.cases)

    def test_nesting_is_deletion_only(self):
        for case in self.cases:
            for a,b in zip(KS,KS[1:]):
                small,large=block(case,a),block(case,b)
                self.assertEqual([r for r in large if r in small],small)
            for k in KS:
                a,b=audit_pair(case,k)
                self.assertEqual(len(a['mappings']),k+2)
                self.assertNotIn('UNKNOWN',a['prompt'])
                self.assertEqual(a['mappings'],b['mappings'])

    def test_parser_distractor_is_other_not_infrastructure(self):
        c=self.cases[0]
        d=c['distractors'][0]['outcome']
        result=parse(d,c,c['gold_outcome'])
        self.assertEqual(result['category'],'OTHER')
        self.assertTrue(result['distractor_output'])
        for raw in (c['gold_outcome'].lower(),c['gold_outcome']+' because',c['gold_outcome']+'..'):
            self.assertEqual(parse(raw,c,c['gold_outcome'])['category'],'INVALID')
        self.assertTrue(parse(' '+c['gold_outcome']+'. ',c,c['gold_outcome'])['correct'])
        self.assertEqual(parse(c['gold_outcome'],c,c['gold_outcome'],True)['category'],'INVALID')

    def test_perfect_is_robust_and_order_diagnostic_separate(self):
        main,diagnostic=self.fixtures()
        parsed,m=main_metrics(self.cases,main)
        _,d=diagnostic_metrics(self.cases,self.selected,diagnostic,parsed)
        self.assertEqual(decide(m)['final_decision'],'ROBUST_CONTEXT_ASSAY')
        self.assertTrue(d['complete'])
        self.assertEqual(len(d['primary_identical_prompt_repeats']),24)
        self.assertTrue(all(x['token_identical'] for x in d['primary_identical_prompt_repeats']))
        self.assertEqual(m['levels']['24']['metrics']['S']['count'],40)
        self.assertAlmostEqual(m['levels']['0']['metrics']['S']['wilson_95'][0],.912378,places=5)

    def test_baseline_arm_threshold_and_priority(self):
        main,_=self.fixtures()
        self.change(main,0,0,'C0')
        self.assertEqual(decide(main_metrics(self.cases,main)[1])['final_decision'],'ROBUST_CONTEXT_ASSAY')
        self.change(main,0,1,'C0')
        for i in range(5):
            self.change(main,24,i,'W0','malformed')
        gate=decide(main_metrics(self.cases,main)[1])
        self.assertEqual(gate['final_decision'],'BASE_ASSAY_REGRESSION')
        self.assertFalse(gate['context_interpretation_allowed'])

    def test_baseline_paired_gate_not_just_arm_rates(self):
        main,_=self.fixtures()
        self.change(main,0,0,'C0')
        self.change(main,0,1,'W0')
        m=main_metrics(self.cases,main)[1]
        self.assertEqual(m['levels']['0']['metrics']['A_C']['count'],39)
        self.assertEqual(m['levels']['0']['metrics']['A_W']['count'],39)
        self.assertEqual(decide(m)['final_decision'],'BASE_ASSAY_REGRESSION')

    def test_K24_threshold_boundaries(self):
        main,_=self.fixtures()
        for i in range(2):
            self.change(main,24,i,'C0')
        self.assertEqual(decide(main_metrics(self.cases,main)[1])['final_decision'],'ROBUST_CONTEXT_ASSAY')
        self.change(main,24,2,'C0')
        self.assertEqual(decide(main_metrics(self.cases,main)[1])['final_decision'],'CONTEXT_SENSITIVE_ASSAY')
        main,_=self.fixtures()
        for i in range(2):
            self.change(main,24,i,'C0')
            self.change(main,24,i+2,'W0')
        m=main_metrics(self.cases,main)[1]
        self.assertEqual(m['levels']['24']['metrics']['A_C']['count'],38)
        self.assertEqual(m['levels']['24']['metrics']['A_W']['count'],38)
        self.assertEqual(m['degradation']['24']['lost_count'],4)
        self.assertTrue(decide(m)['triggers']['K24_paired'])

    def test_monotonic_collapse_requires_two_drops_and_four_losses(self):
        main,_=self.fixtures()
        for k,n in ((4,1),(12,2),(24,4)):
            for i in range(n):
                self.change(main,k,i,'C0')
        m=main_metrics(self.cases,main)[1]
        self.assertEqual(m['paired_success_counts'],[40,39,38,36])
        self.assertTrue(m['monotonic_collapse'])
        main,_=self.fixtures()
        for i in range(4):
            self.change(main,24,i,'C0')
        self.assertFalse(main_metrics(self.cases,main)[1]['monotonic_collapse'])
        main,_=self.fixtures()
        for k,n in ((4,1),(12,2),(24,3)):
            for i in range(n):
                self.change(main,k,i,'C0')
        self.assertFalse(main_metrics(self.cases,main)[1]['monotonic_collapse'])

    def test_off_target_over_two_is_sensitive_with_healthy_baseline(self):
        main,_=self.fixtures()
        self.change(main,4,0,'C0','bad')
        self.change(main,12,1,'W0','bad')
        self.assertEqual(decide(main_metrics(self.cases,main)[1])['final_decision'],'ROBUST_CONTEXT_ASSAY')
        self.change(main,12,2,'W0','bad')
        m=main_metrics(self.cases,main)[1]
        self.assertEqual(m['off_target_by_k'],{'0':0,'4':1,'12':2,'24':0})
        self.assertEqual(decide(m)['final_decision'],'CONTEXT_SENSITIVE_ASSAY')
        self.assertTrue(decide(m)['triggers']['off_target_over_two'])

    def test_exact_discordances_and_deltas(self):
        main,_=self.fixtures()
        self.change(main,0,0,'C0')
        self.change(main,24,1,'C0')
        self.change(main,24,2,'W0')
        m=main_metrics(self.cases,main)[1]
        v=m['degradation']['24']
        self.assertEqual((v['lost_count'],v['gained_count']),(2,1))
        self.assertEqual(v['deltas']['delta_C']['numerator'],0)
        self.assertEqual(v['deltas']['delta_W']['numerator'],-1)
        self.assertEqual(v['deltas']['delta_S']['numerator'],-1)
        self.assertEqual(v['arms']['C0']['correct_to_incorrect'],1)
        self.assertEqual(v['arms']['C0']['incorrect_to_correct'],1)

    def test_real_infrastructure_failure_has_first_priority(self):
        main,_=self.fixtures()
        m=main_metrics(self.cases,main)[1]
        self.assertEqual(decide(m,True)['final_decision'],'INFRASTRUCTURE_FAILURE')
        self.assertEqual(decide(m,diagnostic_complete=False)['final_decision'],'INFRASTRUCTURE_FAILURE')
        self.assertEqual(decide(main_metrics(self.cases,main[:-1])[1])['final_decision'],'INFRASTRUCTURE_FAILURE')
        with self.assertRaises(AssertionError):
            main_metrics(self.cases,main+[main[0]])

    def test_execution_does_not_adapt_to_output(self):
        main,diagnostic=self.fixtures()
        stages=[]
        execute(dict(main=main,position_diagnostic=diagnostic),lambda r:dict(raw_text='bad',truncated=False),lambda stage,r:stages.append(stage))
        self.assertEqual(Counter(stages),dict(main=320,position_diagnostic=72))


if __name__=='__main__':
    unittest.main()
