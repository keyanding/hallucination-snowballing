import copy
import unittest
from experiments.v3_6_5.design import make_cases,render,parse_natural,audit_prompt
from experiments.v3_6_5.analyze import parse,metrics,diagnostic,decide
from experiments.v3_6_5.run import execute
from experiments.v3_6_5.prepare import review,POLICY
from scripts.validated_findings import load,review_spec


class HardNReplicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.dev,cls.conf,cls.reuse=make_cases()

    def row(self,c,wrong=False,rotation=1):
        p=render(c,rotation)
        return p|dict(raw_text=next(n for n in p['names'] if n!=p['gold']) if wrong else p['gold'],truncated=False)

    def fixtures(self,n=4,cases=None):
        return [self.row(c,i<n) for i,c in enumerate(self.dev if cases is None else cases)]

    def test_fresh_graphs_bundles_and_historical_semantics(self):
        cases=self.dev+self.conf
        self.assertEqual(len({c['target'] for c in cases}),48)
        self.assertEqual(len({n for c in cases for n in list(c['name_nodes'].values())+[n for p in c['paths'] for n in p['nodes']]}),624)
        self.assertEqual(self.reuse['fresh_bundles'],40)
        self.assertEqual(len(self.reuse['reused_bundles']),8)
        self.assertEqual(len({tuple(sorted(p['name'] for p in c['candidates'])) for c in cases}),48)
        for c in cases:
            a,b=render(c),render(c,2)
            self.assertEqual(a['graph_audit']['path_depth'],4)
            self.assertEqual(a['graph_audit']['link_count'],12)
            self.assertEqual(a['prompt'].split('\n\nGraph-link records:\n')[1],b['prompt'].split('\n\nGraph-link records:\n')[1])
            self.assertEqual(sorted(l for l in a['prompt'].splitlines() if ' names ' in l),sorted(l for l in b['prompt'].splitlines() if ' names ' in l))

    def test_wrong_graph_link_detected(self):
        c=self.dev[0];p=render(c)
        broken=p['prompt'].replace('credited-director link','associated-director link')
        with self.assertRaises(AssertionError):audit_prompt(c,4,2,broken)

    def test_parser_exact_historical_precedence(self):
        r=self.row(self.dev[0]);gold=r['gold'];other=next(n for n in r['names'] if n!=gold)
        for raw,truncated in [(gold,False),(' '+gold+' ',False),(gold+'.',False),(gold.lower(),False),(gold+' and '+other,False),('The answer is '+gold,False),('Jane Doe',False),(gold,True)]:
            r.update(raw_text=raw,truncated=truncated)
            old=parse_natural(raw,r['names'],truncated,{})
            got=parse(r,{})
            self.assertEqual(got['strict_valid'],old['strict_valid'])
            self.assertEqual(got['identity'],old['identity'])
        self.assertEqual(parse(r,{})['category'],'TRUNCATED')

    def test_no_prose_extraction_and_missing_mapping(self):
        r=self.row(self.dev[0]);r['raw_text']='The answer is '+r['gold']
        self.assertFalse(parse(r,{})['strict_valid'])
        r['downstream_endpoints'].pop(r['names'][0])
        with self.assertRaises(AssertionError):parse(r,{})

    def test_gate_boundaries(self):
        ids=[c['case_id'] for c in self.dev]
        self.assertTrue(metrics(self.fixtures(4),ids,{})['passed'])
        self.assertFalse(metrics(self.fixtures(3),ids,{})['passed'])
        self.assertTrue(metrics(self.fixtures(3),ids,{},True)['passed'])
        self.assertFalse(metrics(self.fixtures(2),ids,{},True)['passed'])
        rows=self.fixtures();rows[-1]['raw_text']=rows[-2]['raw_text']='UNKNOWN'
        self.assertTrue(metrics(rows,ids,{})['passed'])
        rows[-3]['raw_text']='UNKNOWN'
        self.assertFalse(metrics(rows,ids,{})['passed'])

    def test_truncation_invalidates_exact_wrong(self):
        rows=self.fixtures();rows[0]['truncated']=True
        m=metrics(rows,[c['case_id'] for c in self.dev],{})
        self.assertEqual(m['traceable_wrong'],3)
        self.assertEqual(m['counts']['TRUNCATED'],1)
        self.assertFalse(m['passed'])

    def test_missing_duplicate_calls(self):
        rows=self.fixtures();ids=[c['case_id'] for c in self.dev]
        self.assertFalse(metrics(rows[:-1],ids,{})['complete'])
        with self.assertRaises(AssertionError):metrics(rows+[rows[0]],ids,{})

    def plan(self):
        return dict(development=[render(c) for c in self.dev],confirmation=[render(c) for c in self.conf],
                    presentation_diagnostic=[render(c,2) for c in self.dev[:8]],policy=POLICY)

    def test_failed_development_still_runs8_diagnostics_after_classification(self):
        events=[]
        execute(self.plan(),self.dev,{},lambda p:dict(raw_text=p['gold'],truncated=False),lambda s,r:events.append(s),lambda m:events.append('CLASSIFIED'))
        self.assertEqual(events,['development']*24+['CLASSIFIED']+['presentation_diagnostic']*8)

    def test_successful_development_runs56_calls_and_diagnostic_cannot_rescue_gate(self):
        events=[]
        ids={c['case_id'] for c in self.dev[:4]}
        def invoke(p):return dict(raw_text=next(n for n in p['names'] if n!=p['gold']) if p['case_id'] in ids else p['gold'],truncated=False)
        execute(self.plan(),self.dev,{},invoke,lambda s,r:events.append(s),lambda m:None)
        self.assertEqual(events,['development']*24+['presentation_diagnostic']*8+['confirmation']*24)

    def test_diagnostic_identity_and_strict_coverage(self):
        primary=self.fixtures();rows=[self.row(c,rotation=2) for c in self.dev[:8]]
        ids=[c['case_id'] for c in self.dev[:8]]
        m=diagnostic(rows,primary,ids,{})
        self.assertEqual(m['changed_identity'],4);self.assertTrue(m['PRESENTATION_SENSITIVE'])
        rows[0]['raw_text']='The answer is '+rows[0]['gold']
        m=diagnostic(rows,primary,ids,{})
        self.assertEqual(m['comparable'],7);self.assertFalse(m['PRESENTATION_SENSITIVE'])

    def test_decision_precedence(self):
        d=dict(complete=True,passed=False);c=dict(evaluated=False,complete=False,passed=False);g=dict(complete=True,evaluated=True)
        self.assertEqual(decide(d,c,g,POLICY),'HARD_N_SIGNAL_NOT_REPLICATED')
        self.assertEqual(decide(d,c,g,POLICY,True),'INFRASTRUCTURE_FAILURE')
        d['passed']=True
        self.assertEqual(decide(d,c,g,POLICY),'INFRASTRUCTURE_FAILURE')
        c.update(evaluated=True,complete=True)
        self.assertEqual(decide(d,c,g,POLICY),'HARD_N_CONFIRMATION_FAILED')
        c['passed']=True
        self.assertEqual(decide(d,c,g,POLICY),'HARD_N_NATURAL_ERROR_SIGNAL_CONFIRMED')

    def test_complete_ledger_review(self):
        d=load();r,t=review(d,'hash')
        spec='# Prior Findings Review\n\ndocs/validated_findings.md docs/validated_findings.json\n'+t+'\n## Validated Inheritance\n\n## New manipulation\n'
        self.assertTrue(review_spec(d,spec,r,'hash')['passed'])


if __name__=='__main__':unittest.main()
