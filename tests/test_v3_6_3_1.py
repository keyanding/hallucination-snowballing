import copy
import unittest
from unittest.mock import patch
from experiments.v3_6_3_1.design import make_cases, audit_pair, render, parse, pipeline, identifiers, CONDITIONS, to_legacy
from experiments.v3_6_3_1.analyze import calibration, main_metrics, integrated, shell_diagnostic, shell_flags, decide
from experiments.v3_6_3_1.run import execute
from experiments.v3_6_3_1.prepare import inheritance
from experiments.inheritance import validate
from experiments.v3_6_3.design import parse as old_parse, render as old_render


class Tokenizer:
    def encode(self,value,**kwargs):
        return [1,2,3,4]


class FrozenPipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cal,cls.main,cls.diag,cls.iset,_,_=make_cases(Tokenizer(),{'STATE_A00'})

    def output(self,r,raw=None):
        return r|dict(raw_text=r['expected'] if raw is None else raw,truncated=False)

    def fixtures(self):
        cal=[self.output(render(c,k)) for c in self.cal for k in CONDITIONS]
        up=[self.output(render(c,k)) for k in ('U-A','U-B') for c in self.main]
        down=[self.output(render(c,k)) for c in self.main for k in ('D-A','D-B')]
        pipes,logs=[],[]
        for c in self.main:
            r,l=pipeline(c,next(r for r in up if r['case_id']==c['case_id'] and r['condition']=='U-A'))
            pipes.append(self.output(r))
            logs.append(l)
        integ=[self.output(render(c,k)) for c in self.main if c['case_id'] in self.iset for k in ('I-A','I-B')]
        shell=[self.output(render(c,k,s)) for c in self.diag for k in ('D-A','D-B') for s in ('VALIDATED','RECORDED')]
        return cal,up,down,pipes,logs,integ,shell

    def plan(self):
        cr,u,d,p,l,i,s=self.fixtures()
        return dict(calibration=cr,main_upstream=u,main_downstream=d,pipeline_case_order=[c['case_id'] for c in self.main],integrated=i,shell_diagnostic=s)

    def test_inherited_bytes_and_fresh_cases(self):
        allcases=self.cal+self.main+self.diag
        self.assertEqual(len(identifiers(allcases)),420)
        self.assertNotIn('STATE_A00',identifiers(allcases))
        self.assertEqual(len(self.iset),20)
        self.assertTrue(set(self.iset)<={c['case_id'] for c in self.main})
        for c in allcases:
            for prefix in ('U','D','I'):
                audit_pair(c,prefix)
            audit_pair(c,'D','RECORDED')
            self.assertEqual(render(c,'U-A')['prompt'],old_render(to_legacy(c),'U-GOLD')['prompt'])
            self.assertEqual(render(c,'I-B')['prompt'],old_render(to_legacy(c),'I-ALT')['prompt'])

    def test_changed_downstream_wording_fails_audit(self):
        from experiments.v3_6_3_1 import design
        original=design.minimal_render
        def modified(*args,**kwargs):
            r=original(*args,**kwargs)
            return r|dict(prompt=r['prompt'].replace('mapped outcome','result'))
        with patch.object(design,'minimal_render',modified):
            with self.assertRaises(AssertionError):
                audit_pair(self.main[0],'D')

    def test_parser_is_inherited_and_not_repaired(self):
        c=self.main[0]
        for up in (False,True):
            for truncated in (False,True):
                for raw in (c['state_a'],c['outcome_b']+'.','UNKNOWN','STATE_Z99','OUTCOME_Z99','Z99', 'Answer: '+c['outcome_a'], c['state_a'].lower(),c['state_a']+'..'):
                    self.assertEqual(parse(raw,c,up,truncated),old_parse(raw,to_legacy(c),up,truncated))

    def test_pipeline_forwards_alternative_and_unmapped_without_repair(self):
        c=self.main[0]
        for state in (c['state_b'],'STATE_Z99'):
            r,l=pipeline(c,self.output(render(c,'U-A'),' '+state+'. '))
            self.assertEqual(r['supplied_state'],state)
            self.assertEqual(l['status'],'CALLED_UNREPAIRED')
            self.assertIn('Current state:\n'+state+'\n',r['prompt'])
            self.assertNotIn('UNKNOWN',r['prompt'])
            self.assertNotIn('Recorded',r['prompt'])
            if state not in (c['state_a'],c['state_b']):
                self.assertIsNone(r['expected'])
        for raw in ('UNKNOWN','K04','state_k04','Answer: '+c['state_a'],c['state_a']+'..'):
            self.assertIsNone(pipeline(c,self.output(render(c,'U-A'),raw))[0])
        self.assertIsNone(pipeline(c,self.output(render(c,'U-A'))|dict(truncated=True))[0])

    def test_all_pass_and_renamed_metrics(self):
        cr,u,d,p,l,i,s=self.fixtures()
        cal=calibration(self.cal,cr)[1]
        main=main_metrics(self.main,u,d,p,l)[1]
        im=integrated(self.main,self.iset,i)[1]
        sm=shell_diagnostic(self.diag,s)[1]
        self.assertEqual(decide(cal,main,sm,im),'TWO_HOP_PIPELINE_VALIDATED')
        self.assertTrue(im['ready'])
        self.assertEqual(im['I_A']['count'],20)
        self.assertEqual(im['I_B']['count'],20)
        self.assertEqual(main['metrics']['A_U_A']['count'],40)
        self.assertEqual(main['metrics']['A_U_B']['count'],40)
        self.assertEqual(main['metrics']['S_D']['count'],40)
        self.assertIn('D',main['tables'])

    def test_strict_e2e_and_skip_denominators(self):
        cr,u,d,p,l,i,s=self.fixtures()
        c=self.main[0]
        u[0]['raw_text']=c['state_b']
        r,l[0]=pipeline(c,u[0])
        p[0]=self.output(r,c['outcome_a'])
        m=main_metrics(self.main,u,d,p,l)[1]
        self.assertEqual(m['metrics']['E2E']['count'],39)
        self.assertEqual(m['conditional_downstream']['denominator'],39)
        self.assertEqual(m['pipeline_failures'][0]['source'],'UPSTREAM_INCORRECT')
        u[0]['raw_text']='invalid'
        _,l[0]=pipeline(c,u[0])
        m=main_metrics(self.main,u,d,p[1:],l)[1]
        self.assertTrue(m['complete'])
        self.assertEqual(m['pipeline_skipped'],1)
        self.assertEqual(m['metrics']['E2E']['denominator'],40)
        for idx,c in enumerate(self.main):
            u[idx]['raw_text']='invalid'
            _,l[idx]=pipeline(c,u[idx])
        m=main_metrics(self.main,u,d,[],l)[1]
        self.assertIsNone(m['conditional_downstream']['rate'])

    def test_shell_descriptive_flags_and_pairing(self):
        *_,s=self.fixtures()
        c=self.diag[0]
        recorded=[r for r in s if r['shell']=='RECORDED']
        recorded[0]['raw_text']=c['outcome_a'].split('_')[-1]
        recorded[1]['raw_text']='The outcome is '+c['outcome_b']
        recorded[1]['truncated']=True
        _,m=shell_diagnostic(self.diag,s)
        self.assertEqual(m['shells']['RECORDED']['invalid_count'],2)
        self.assertEqual(m['shells']['RECORDED']['prefix_omission_count'],1)
        self.assertEqual(m['shells']['RECORDED']['explanation_format_count'],1)
        self.assertEqual(m['shells']['RECORDED']['truncation_count'],1)
        self.assertEqual(m['recorded_only_failures'],2)
        self.assertEqual(m['validated_only_failures'],0)
        with self.assertRaises(AssertionError):
            shell_diagnostic(self.diag,s+[s[0]])

    def test_diagnostic_accuracy_never_changes_main_decision(self):
        cr,u,d,p,l,i,s=self.fixtures()
        for r in i+s:
            r['raw_text']='invalid'
        im=integrated(self.main,self.iset,i)[1]
        sm=shell_diagnostic(self.diag,s)[1]
        self.assertFalse(im['ready'])
        self.assertEqual(decide(calibration(self.cal,cr)[1],main_metrics(self.main,u,d,p,l)[1],sm,im),'TWO_HOP_PIPELINE_VALIDATED')

    def test_calibration_failure_stops_all_other_stages(self):
        actual=[]
        execute(self.plan(),self.cal,self.main,lambda r:dict(raw_text='bad',truncated=False),lambda s,r:actual.append(s),lambda r:self.fail('unexpected pipeline'))
        self.assertEqual(actual,['calibration']*80)

    def test_main_failure_still_runs_shell_and_skips_integrated(self):
        actual=[]
        def invoke(r):
            value=r['expected']
            if r['split']=='main' and r['condition']=='U-A':
                if r['case_id']==self.main[0]['case_id']:
                    value=self.main[0]['state_b']
                if r['case_id']==self.main[1]['case_id']:
                    value='bad'
            return dict(raw_text=value,truncated=False)
        execute(self.plan(),self.cal,self.main,invoke,lambda s,r:actual.append((s,r)),lambda r:None)
        stages=[s for s,r in actual]
        self.assertEqual(len(actual),319)
        self.assertEqual(stages.count('shell_diagnostic'),40)
        self.assertNotIn('integrated',stages)
        pipes=[r for s,r in actual if s=='pipeline_generated']
        self.assertEqual(pipes[0]['supplied_state'],self.main[0]['state_b'])

    def test_successful_execution_order_and_budget(self):
        actual=[]
        execute(self.plan(),self.cal,self.main,lambda r:dict(raw_text=r['expected'],truncated=False),lambda s,r:actual.append(s),lambda r:None)
        self.assertEqual(len(actual),360)
        self.assertEqual(actual[-80:-40],['shell_diagnostic']*40)
        self.assertEqual(actual[-40:],['integrated']*40)

    def test_gate_precedence_and_required_diagnostics(self):
        self.assertEqual(decide(dict(complete=True,passed=False),{}, {},{}),'STOP_V3631_CALIBRATION_INVALID')
        self.assertEqual(decide(dict(complete=True,passed=False),{}, {},{},True),'INFRASTRUCTURE_FAILURE')
        self.assertEqual(decide(dict(complete=True,passed=True),dict(complete=True,passed=False),dict(evaluated=True),dict(evaluated=False)),'TWO_HOP_PIPELINE_INVALID')
        self.assertEqual(decide(dict(complete=True,passed=True),dict(complete=True,passed=True),dict(evaluated=True),dict(evaluated=False)),'INFRASTRUCTURE_FAILURE')
        self.assertEqual(decide(dict(complete=True,passed=True),dict(complete=True,passed=False),dict(evaluated=False),{}),'INFRASTRUCTURE_FAILURE')

    def test_inheritance_workflow_rejects_silent_modifications(self):
        spec='## Validated Inheritance\n\n## New manipulation'
        rows=inheritance()
        self.assertTrue(validate(spec,rows))
        with self.assertRaises(AssertionError):
            validate('## New manipulation\n## Validated Inheritance',rows)
        rows[0]['modified']=True
        with self.assertRaises(AssertionError):
            validate(spec,rows)
        rows[0].update(classification='INTENTIONALLY_RETESTED',reason='Explicit test',prior_conclusion_no_longer_applies='New interface unvalidated')
        self.assertTrue(validate(spec,rows))


if __name__=='__main__':
    unittest.main()
