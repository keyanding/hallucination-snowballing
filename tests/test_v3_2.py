import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest

from src.common import read_jsonl
from src.experiment_v3_1 import build_prompt as old_prompt
from src.experiment_v3_2 import ABLATIONS, CONDITIONS, analyze, audit_case, build_prompt, export_results, run


class AblationAdapter:
    def __init__(self,cases,plans,fail_cla=False,fail_gsa=False):
        self.answers={};self.calls=[]
        for case in cases:
            for a in ABLATIONS:
                for k in CONDITIONS:
                    answer=case['C_prime'] if k.endswith('_prime') else case['C']
                    if k=='state_B_prime' and a in ('C4','C6b'):answer=case['C']
                    if fail_cla and a=='C2' and k=='direct_B':answer='Unknown'
                    if fail_gsa and a in ('C5','C6a') and k=='state_B':answer=case['C_prime']
                    self.answers[build_prompt(case,a,k,plans[case['case_id']])]=answer

    def generate(self,prompt,**kwargs):
        self.calls.append(prompt)
        return dict(raw_generation=self.answers[prompt],truncated=False)


class V32Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root=Path(__file__).resolve().parents[1]
        cls.cases=read_jsonl(root/'data/candidates_v3_1.jsonl')
        cls.plans=json.loads((root/'results/smoke_v3_2/ablation_plan.json').read_text(encoding='utf-8'))

    def test_matching_and_exact_old_baselines(self):
        for c in self.cases:
            p=self.plans[c['case_id']]
            self.assertTrue(all(audit_case(c,p).values()))
            for k in CONDITIONS:
                self.assertEqual(build_prompt(c,'C0',k,p),old_prompt(c,'H0',k))
                self.assertEqual(build_prompt(c,'C1',k,p),old_prompt(c,'H1',k))
                self.assertNotEqual(build_prompt(c,'C4',k,p),old_prompt(c,'H3',k))
            for key in ('C2','C3'):
                self.assertLessEqual(abs(p['block_tokens'][key]-p['block_tokens']['C4']),2)

    def test_contamination_or_asymmetric_claim_rejected(self):
        c=self.cases[0]
        for key,value in (('C2','A note mentions '+c['C']),('C3',c['A']+' was directed by '+c['B']),
                          ('C5','For this task, '+self.plans[c['case_id']]['blocks']['C5'])):
            plan=copy.deepcopy(self.plans[c['case_id']]);plan['blocks'][key]=value
            with self.assertRaises((ValueError,AssertionError)):
                audit_case(c,plan)

    def test_all_contrasts_and_conflict_recency_without_gate_bias(self):
        with tempfile.TemporaryDirectory() as directory,contextlib.redirect_stdout(io.StringIO()):
            out=Path(directory);adapter=AblationAdapter(self.cases,self.plans)
            rows,stopped=run(self.cases,self.plans,adapter,out)
            metrics,gate=analyze(self.cases,rows,stopped)
            self.assertEqual(len(adapter.calls),320)
            self.assertTrue(gate['passed'])
            self.assertEqual(metrics['primary_contrasts'],dict(length_effect=0,gold_entity_activation=0,gold_relational_evidence=-1,alternative_support=1))
            self.assertTrue(all(p['order_sensitive'] and p['follows_last_both'] for p in metrics['conflict_order_pairs']))
            export_results(out,self.cases,rows,stopped)
            self.assertIn('order-sensitive conflict resolution',(out/'inspection.md').read_text(encoding='utf-8'))
            with self.assertRaises(FileExistsError):run(self.cases,self.plans,adapter,out)

    def test_lookup_collapse_stops_and_future_contrasts_are_null(self):
        with tempfile.TemporaryDirectory() as directory,contextlib.redirect_stdout(io.StringIO()):
            rows,stopped=run(self.cases,self.plans,AblationAdapter(self.cases,self.plans,fail_cla=True),Path(directory))
        metrics,gate=analyze(self.cases,rows,stopped)
        self.assertEqual(len(rows),120)
        self.assertFalse(gate['passed'])
        self.assertTrue(stopped)
        self.assertIsNone(metrics['primary_contrasts']['gold_relational_evidence'])
        self.assertNotIn('C3',metrics['conditions'])

    def test_multiple_gold_state_failures_stop_without_relaxing_gate(self):
        with tempfile.TemporaryDirectory() as directory,contextlib.redirect_stdout(io.StringIO()):
            rows,stopped=run(self.cases,self.plans,AblationAdapter(self.cases,self.plans,fail_gsa=True),Path(directory))
        metrics,gate=analyze(self.cases,rows,stopped)
        self.assertEqual(len(rows),280)
        self.assertFalse(gate['quantitative_checks']['GSA_all'])
        self.assertEqual(metrics['conflict_order_pairs'],[])
        self.assertTrue(stopped)

    def test_partial_or_duplicate_matrix_rejected(self):
        with tempfile.TemporaryDirectory() as directory,contextlib.redirect_stdout(io.StringIO()):
            rows,_=run(self.cases,self.plans,AblationAdapter(self.cases,self.plans),Path(directory))
        with self.assertRaises(ValueError):analyze(self.cases,rows[:-1])
        with self.assertRaises(ValueError):analyze(self.cases,rows+[rows[0]])


if __name__=='__main__':unittest.main()
