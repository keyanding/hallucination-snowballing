import copy
import unittest
from experiments.v3_6_4.design import make_cases, render, audit_cases, LEVELS
from experiments.v3_6_4.analyze import parse, metrics, development, order_metrics, decide
from experiments.v3_6_4.run import execute
from experiments.v3_6_4.prepare import ledger_review
from scripts.validated_findings import load, review_spec


class Tokenizer:
    def encode(self, value, **kwargs):
        return [1,2,3,4]


class NaturalFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dev,cls.confirm,cls.audit = make_cases(Tokenizer(),{'STATE_A00'})
        cls.policy = dict(valid_includes_out_of_universe=False)

    def row(self,c,level='EASY',raw=None,truncated=False,permutation=False):
        p=render(c,level,permutation)
        return p|dict(raw_text=p['expected'] if raw is None else raw,truncated=truncated)

    def fixtures(self,wrong=4,cases=None,level='EASY'):
        cases=self.dev if cases is None else cases
        return [self.row(c,level,c['members'][1]['state'] if i<wrong else None) for i,c in enumerate(cases)]

    def plan(self):
        return dict(development=[render(c,k) for k in LEVELS for c in self.dev],
                    confirmation={k:[render(c,k) for c in self.confirm] for k in LEVELS},
                    order_diagnostic={k:[render(c,k,True) for c in self.dev[:8]] for k in LEVELS},policy=self.policy)

    def test_fresh_nested_cases_and_compatibility(self):
        allcases=self.dev+self.confirm
        maps={c['case_id']:{m['state']:m['outcome'] for m in c['members']} for c in allcases}
        self.assertTrue(audit_cases(self.dev,self.confirm,maps)['passed'])
        self.assertFalse(next(a for a in self.audit if a['raw']=='STATE_A00')['selected'])
        self.assertEqual(make_cases(Tokenizer(),{'STATE_A00'})[0],self.dev)
        for c in allcases:
            for k in LEVELS:
                p,q=render(c,k),render(c,k,True)
                self.assertNotEqual(p['records'],q['records'])
                self.assertEqual(sorted(p['records']),sorted(q['records']))

    def test_corrupt_maps_or_duplicate_path_rejected(self):
        maps={c['case_id']:{m['state']:m['outcome'] for m in c['members']} for c in self.dev+self.confirm}
        bad=copy.deepcopy(self.dev)
        bad[0]['members'][1]['marker']=bad[0]['members'][0]['marker']
        with self.assertRaises(AssertionError):audit_cases(bad,self.confirm,maps)
        maps[self.dev[0]['case_id']].pop(self.dev[0]['gold'])
        with self.assertRaises(AssertionError):audit_cases(self.dev,self.confirm,maps)

    def test_exact_parser_and_orthogonal_truncation(self):
        c=self.dev[0]
        p=parse(self.row(c,raw=' \n'+c['gold']+'. '),self.policy)
        self.assertEqual(p['category'],'GOLD')
        for raw in (c['gold'].lower(), 'Answer: '+c['gold'],c['gold']+'..',c['gold'].split('_')[-1],'UNKNOWN'):
            self.assertEqual(parse(self.row(c,raw=raw),self.policy)['category'],'INVALID')
        r=self.row(c,raw=c['members'][1]['state'],truncated=True)
        p=parse(r,self.policy)
        self.assertEqual(p['category'],'TRACEABLE_WRONG')
        self.assertFalse(p['valid'] or p['qualified_wrong'])
        self.assertEqual(parse(self.row(c,raw=c['members'][7]['state']),self.policy)['category'],'OUT_OF_UNIVERSE')

    def test_valid_policy_is_explicit(self):
        r=self.row(self.dev[0],raw='STATE_A00')
        self.assertFalse(parse(r,self.policy)['valid'])
        with self.assertRaises(AssertionError):parse(r,dict(valid_includes_out_of_universe=True))
        r['downstream_compatibility'].pop(r['state_universe'][1])
        with self.assertRaises(AssertionError):parse(r,self.policy)

    def test_exact_development_and_confirmation_yield_boundaries(self):
        ids=[c['case_id'] for c in self.dev]
        self.assertTrue(metrics(self.fixtures(4),ids,self.policy)['passed'])
        self.assertFalse(metrics(self.fixtures(3),ids,self.policy)['passed'])
        self.assertTrue(metrics(self.fixtures(3),ids,self.policy,True)['passed'])
        self.assertFalse(metrics(self.fixtures(2),ids,self.policy,True)['passed'])

    def test_valid_invalid_and_truncation_boundaries(self):
        ids=[c['case_id'] for c in self.dev]
        rows=self.fixtures()
        rows[-1]['raw_text']='bad'
        rows[-2]['raw_text']='STATE_A00'
        m=metrics(rows,ids,self.policy)
        self.assertTrue(m['passed'])
        self.assertEqual(m['valid'],22)
        rows[-3]['raw_text']='STATE_A00'
        self.assertFalse(metrics(rows,ids,self.policy)['passed'])
        rows=self.fixtures()
        rows[-1]['truncated']=True
        self.assertTrue(metrics(rows,ids,self.policy)['passed'])
        rows[-2]['truncated']=True
        self.assertFalse(metrics(rows,ids,self.policy)['passed'])
        rows=self.fixtures()
        rows[0]['truncated']=True
        m=metrics(rows,ids,self.policy)
        self.assertEqual(m['counts']['TRACEABLE_WRONG'],4)
        self.assertEqual(m['qualified_traceable_wrong'],3)
        self.assertFalse(m['passed'])
        rows=self.fixtures()
        rows[-1]['raw_text']=rows[-2]['raw_text']='bad'
        self.assertFalse(metrics(rows,ids,self.policy)['passed'])

    def test_missing_duplicate_and_unexpected_calls(self):
        ids=[c['case_id'] for c in self.dev]
        rows=self.fixtures()
        self.assertFalse(metrics(rows[:-1],ids,self.policy)['complete'])
        with self.assertRaises(AssertionError):metrics(rows+[rows[0]],ids,self.policy)
        with self.assertRaises(AssertionError):metrics([self.row(self.confirm[0])],ids,self.policy)

    def test_easiest_selection_not_maximum_yield(self):
        rows=sum((self.fixtures(n,level=k) for k,n in zip(LEVELS,(4,8,12))),[])
        self.assertEqual(development(rows,self.dev,self.policy)['selected_level'],'EASY')
        rows=sum((self.fixtures(n,level=k) for k,n in zip(LEVELS,(0,4,12))),[])
        self.assertEqual(development(rows,self.dev,self.policy)['selected_level'],'MID')

    def test_stop_at72_and_run104_if_selected_even_when_confirmation_fails(self):
        called=[]
        execute(self.plan(),self.dev,lambda p:dict(raw_text=p['expected'],truncated=False),lambda s,r:called.append(s))
        self.assertEqual(called,['development']*72)
        called=[]
        def invoke(p):
            c=next(c for c in self.dev+self.confirm if c['case_id']==p['case_id'])
            wrong=p['split']=='development' and c in self.dev[:4]
            return dict(raw_text=c['members'][1]['state'] if wrong else p['expected'],truncated=False)
        selected=execute(self.plan(),self.dev,invoke,lambda s,r:called.append(s))
        self.assertEqual(selected,'EASY')
        self.assertEqual(called,['development']*72+['confirmation']*24+['order_diagnostic']*8)

    def test_order_incomparability_wrong_persistence_and_threshold(self):
        originals=self.fixtures()
        ids=[c['case_id'] for c in self.dev[:8]]
        rows=[self.row(c,permutation=True) for c in self.dev[:8]]
        m=order_metrics(rows,originals,ids,'EASY',self.policy)
        self.assertTrue(m['ORDER_SENSITIVE_FRONTIER'])
        self.assertEqual(m['changed_identity'],4)
        rows[0]['raw_text']='prose'
        m=order_metrics(rows,originals,ids,'EASY',self.policy)
        self.assertEqual(m['changed_identity'],3)
        self.assertEqual(m['incomparable_pairs'],1)
        self.assertFalse(m['ORDER_SENSITIVE_FRONTIER'])
        rows[0]['raw_text']=self.dev[0]['members'][2]['state']
        m=order_metrics(rows,originals,ids,'EASY',self.policy)
        self.assertEqual(m['wrong_state_persistent'],1)
        self.assertEqual(m['same_wrong_identity'],0)

    def test_decision_priority_and_non_gating_order(self):
        d=dict(complete=True,selected_level=None)
        c=dict(evaluated=False,complete=False,passed=False)
        o=dict(evaluated=False,complete=False)
        self.assertEqual(decide(d,c,o),'NO_NATURAL_ERROR_FRONTIER')
        self.assertEqual(decide(d,c,o,True),'INFRASTRUCTURE_FAILURE')
        d['selected_level']='HARD'
        self.assertEqual(decide(d,c,o),'INFRASTRUCTURE_FAILURE')
        c.update(complete=True,evaluated=True)
        o.update(complete=True,evaluated=True,ORDER_SENSITIVE_FRONTIER=True)
        self.assertEqual(decide(d,c,o),'NATURAL_ERROR_FRONTIER_NOT_CONFIRMED')
        c['passed']=True
        self.assertEqual(decide(d,c,o),'NATURAL_ERROR_FRONTIER_CONFIRMED')

    def test_full_ledger_review_discloses_modified_components(self):
        data=load()
        r,t=ledger_review(data,'fixture')
        spec='# Prior Findings Review\n\ndocs/validated_findings.md docs/validated_findings.json\n'+t+'\n## Validated Inheritance\n\n## New manipulation\n'
        self.assertTrue(review_spec(data,spec,r,'fixture')['passed'])
        self.assertEqual({x['id'] for x in r['rows'] if x['modified']},{'C02','C04','C05'})


if __name__ == '__main__':
    unittest.main()
