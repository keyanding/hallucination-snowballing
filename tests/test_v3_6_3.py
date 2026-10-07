import copy
import unittest
from experiments.v3_6_3.design import make_cases,audit_pair,render,parse,pipeline,CONDITIONS
from experiments.v3_6_3.analyze import calibration,main_metrics,integrated,order_diagnostic,decide
from experiments.v3_6_3.run import execute


class Tokenizer:
    def encode(self,value,**kwargs):
        return [1,2,3,4]


class TwoHopTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cal,cls.main,cls.iset,cls.oset,_,_=make_cases(Tokenizer(),set())

    def output(self,r,raw=None):
        return r|dict(raw_text=r['expected'] if raw is None else raw,truncated=False)

    def fixtures(self):
        cal=[self.output(render(c,k)) for c in self.cal for k in CONDITIONS]
        up=[self.output(render(c,k)) for c in self.main for k in ('U-GOLD','U-ALT')]
        prop=[self.output(render(c,k)) for c in self.main for k in ('P-GOLD','P-ALT')]
        pipes,logs=[],[]
        for c in self.main:
            r,l=pipeline(c,next(r for r in up if r['case_id']==c['case_id'] and r['condition']=='U-GOLD'))
            pipes.append(self.output(r))
            logs.append(l)
        integ=[self.output(render(c,k)) for c in self.main if c['case_id'] in self.iset for k in ('I-GOLD','I-ALT')]
        order=[self.output(render(c,k,True)) for c in self.main if c['case_id'] in self.oset for k in ('U-GOLD','U-ALT')]
        return cal,up,prop,pipes,logs,integ,order

    def test_exact_pair_diffs_and_disjointness(self):
        seen=[]
        for c in self.cal+self.main:
            seen += [c[r+'_'+role] for r in ('gold','alt') for role in ('entity','state','outcome')]
            for prefix in ('U','P','I'):
                audit_pair(c,prefix)
        self.assertEqual(len(set(seen)),360)
        self.assertEqual((len(self.iset),len(self.oset)),(20,10))

    def test_pipeline_forwards_alternative_and_unmapped_exactly(self):
        c=self.main[0]
        for state in (c['alt_state'],'STATE_Z99'):
            r,l=pipeline(c,self.output(render(c,'U-GOLD'),' '+state+'. '))
            self.assertEqual(r['supplied_state'],state)
            self.assertEqual(l['status'],'CALLED_UNREPAIRED')
            self.assertIn('\n'+state+'\n',r['prompt'])
            if state=='STATE_Z99' and state not in (c['gold_state'],c['alt_state']):
                self.assertIsNone(r['expected'])

    def test_malformed_and_truncated_upstream_skip(self):
        c=self.main[0]
        for raw in ('UNKNOWN','state_a00',c['gold_state']+' because',c['gold_state']+'..'):
            r,l=pipeline(c,self.output(render(c,'U-GOLD'),raw))
            self.assertIsNone(r)
            self.assertEqual(l['status'],'UPSTREAM_INVALID_SKIPPED')
        r=self.output(render(c,'U-GOLD'))
        r['truncated']=True
        self.assertIsNone(pipeline(c,r)[0])

    def test_all_pass(self):
        cr,u,p,pipe,logs,i,o=self.fixtures()
        cal=calibration(self.cal,cr)[1]
        main=main_metrics(self.main,u,p,pipe,logs)[1]
        im=integrated(self.main,self.iset,i)[1]
        om=order_diagnostic(self.main,self.oset,o,u)[1]
        self.assertEqual(decide(cal,main,im,om),'TWO_HOP_PROPAGATION_ASSAY_VALIDATED')
        self.assertTrue(im['ready'])
        self.assertEqual(main['conditional_downstream']['denominator'],40)

    def test_calibration_gates_and_paired_symmetry(self):
        cr,*_=self.fixtures()
        for prefix,gate in (('U','E'),('P','F')):
            rows=copy.deepcopy(cr)
            a=next(r for r in rows if r['case_id']==self.cal[0]['case_id'] and r['condition']==prefix+'-GOLD')
            b=next(r for r in rows if r['case_id']==self.cal[1]['case_id'] and r['condition']==prefix+'-ALT')
            a['raw_text']='bad'
            self.assertTrue(calibration(self.cal,rows)[1]['gates'][gate]['passed'])
            b['raw_text']='bad'
            m=calibration(self.cal,rows)[1]
            self.assertFalse(m['gates'][gate]['passed'])
            self.assertEqual(decide(m,{}, {},{}),'STOP_TWO_HOP_CALIBRATION_INVALID')
        rows=copy.deepcopy(cr)
        rows[0]['raw_text']='bad'
        self.assertTrue(calibration(self.cal,rows)[1]['gates']['G']['passed'])
        rows[1]['raw_text']='bad'
        self.assertFalse(calibration(self.cal,rows)[1]['gates']['G']['passed'])

    def test_upstream_failure_cannot_be_hidden_by_downstream_C(self):
        cr,u,p,pipe,logs,i,o=self.fixtures()
        c=self.main[0]
        ug=next(r for r in u if r['case_id']==c['case_id'] and r['condition']=='U-GOLD')
        ug['raw_text']=c['alt_state']
        r,l=pipeline(c,ug)
        pipe[0]=self.output(r,c['gold_outcome'])
        logs[0]=l
        m=main_metrics(self.main,u,p,pipe,logs)[1]
        self.assertEqual(m['metrics']['E2E']['count'],39)
        self.assertEqual(m['conditional_downstream']['denominator'],39)
        self.assertEqual(m['pipeline_failures'][0]['source'],'UPSTREAM_INCORRECT')
        ug['raw_text']='malformed'
        _,logs[0]=pipeline(c,ug)
        m=main_metrics(self.main,u,p,pipe[1:],logs)[1]
        self.assertTrue(m['complete'])
        self.assertEqual(m['pipeline_skipped'],1)
        self.assertEqual(m['metrics']['E2E']['denominator'],40)

    def test_main_pipeline_and_component_boundaries(self):
        _,u,p,pipe,logs,_,_=self.fixtures()
        for r in pipe[:2]:
            r['raw_text']='UNKNOWN'
        m=main_metrics(self.main,u,p,pipe,logs)[1]
        self.assertTrue(m['gates']['G6'])
        pipe[2]['raw_text']='UNKNOWN'
        self.assertFalse(main_metrics(self.main,u,p,pipe,logs)[1]['gates']['G6'])
        for condition,gate in (('U-GOLD','G1'),('U-ALT','G2'),('P-GOLD','G3'),('P-ALT','G4')):
            rows=copy.deepcopy(u if condition.startswith('U') else p)
            selected=[r for r in rows if r['condition']==condition]
            # Direct counts for upstream tests avoid mutating source-linked pipeline.
            selected[0]['raw_text']='UNKNOWN'
            from experiments.v3_6_3.analyze import component
            _,v=component(self.main,rows+p if condition.startswith('U') else u+rows)
            self.assertEqual(v['correct'][condition],39)
            selected[1]['raw_text']='UNKNOWN'
            _,v=component(self.main,rows+p if condition.startswith('U') else u+rows)
            self.assertEqual(v['correct'][condition],38)

    def test_G7_excludes_unknown_and_pipeline(self):
        _,u,p,pipe,logs,_,_=self.fixtures()
        p[0]['raw_text']='UNKNOWN'
        pipe[0]['raw_text']='bad'
        self.assertEqual(main_metrics(self.main,u,p,pipe,logs)[1]['G7_off_target']['count'],0)
        for r in p[:2]:
            r['raw_text']='bad'
        self.assertTrue(main_metrics(self.main,u,p,pipe,logs)[1]['gates']['G7'])
        p[2]['raw_text']='bad'
        self.assertFalse(main_metrics(self.main,u,p,pipe,logs)[1]['gates']['G7'])

    def test_integrated_readiness_is_separate(self):
        cr,u,p,pipe,logs,i,o=self.fixtures()
        for r in i[:4]:
            r['raw_text']='UNKNOWN'
        im=integrated(self.main,self.iset,i)[1]
        self.assertFalse(im['ready'])
        om=order_diagnostic(self.main,self.oset,o,u)[1]
        self.assertEqual(decide(calibration(self.cal,cr)[1],main_metrics(self.main,u,p,pipe,logs)[1],im,om),'TWO_HOP_PROPAGATION_ASSAY_VALIDATED')

    def test_calibration_failure_prevents_all_main_calls(self):
        cr,u,p,pipe,logs,i,o=self.fixtures()
        plan=dict(calibration=cr,main_upstream=u,main_propagation=p,pipeline_case_order=[c['case_id'] for c in self.main],integrated=i,order_diagnostic=o)
        calls=[]
        gate=execute(plan,self.cal,self.main,lambda r:dict(raw_text='bad',truncated=False),lambda stage,r:calls.append(stage),lambda r:None)
        self.assertFalse(gate['passed'])
        self.assertEqual(calls,['calibration']*80)

    def test_execution_preserves_wrong_state_and_skips_invalid(self):
        cr,u,p,pipe,logs,i,o=self.fixtures()
        plan=dict(calibration=cr,main_upstream=u,main_propagation=p,pipeline_case_order=[c['case_id'] for c in self.main],integrated=i,order_diagnostic=o)
        actual=[]
        def invoke(r):
            value=r['expected']
            if r['split']=='main' and r['condition']=='U-GOLD':
                if r['case_id']==self.main[0]['case_id']:
                    value=self.main[0]['alt_state']
                if r['case_id']==self.main[1]['case_id']:
                    value='bad'
            return dict(raw_text=value,truncated=False)
        execute(plan,self.cal,self.main,invoke,lambda stage,r:actual.append((stage,r)),lambda r:None)
        pipes=[r for stage,r in actual if stage=='pipeline_generated']
        self.assertEqual(len(pipes),39)
        self.assertEqual(pipes[0]['supplied_state'],self.main[0]['alt_state'])
        self.assertEqual(len(actual),339)


if __name__=='__main__':
    unittest.main()
