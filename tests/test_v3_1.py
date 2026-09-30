import contextlib
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest

from src.common import read_jsonl
from src.experiment_v3_1 import (CONDITIONS, LEVELS, analyze, audit_case, build_prompt,
                                classify, context_block, export_results, prepare, run)
from src.experiment_v3 import parse_answer


class LadderAdapter:
    def __init__(self, cases, override_h3=False, fail_h0=False):
        self.answers={}
        self.calls=[]
        for case in cases:
            for level in LEVELS:
                for condition in CONDITIONS:
                    answer=case['C_prime'] if condition.endswith('_prime') else case['C']
                    if override_h3 and level=='H3' and condition=='state_B_prime':answer=case['C']
                    if fail_h0 and level=='H0' and condition=='direct_B':answer='Unknown'
                    self.answers[build_prompt(case,level,condition)]=answer

    def generate(self,prompt,**kwargs):
        self.calls.append(prompt)
        return dict(raw_generation=self.answers[prompt],truncated=False)


class V31Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=Path(__file__).resolve().parents[1]/'data/candidates_v3_1.jsonl'
        cls.cases=read_jsonl(cls.data)

    def test_fixed_real_case_balance_and_no_identity_reuse(self):
        self.assertEqual(len(self.cases),10)
        self.assertEqual(len({c[k] for c in self.cases for k in ('B','B_prime')}),20)
        self.assertEqual(sum(c['evidence_order']==1 for c in self.cases),5)
        self.assertTrue(all(c['track']=='real' for c in self.cases))

    def test_ladder_is_cumulative_and_pairs_only_change_state(self):
        for c in self.cases:
            self.assertTrue(all(audit_case(c).values()))
            self.assertNotIn('Original task',context_block(c,'H0'))
            self.assertNotIn(c['first_hop_evidence']['text'],context_block(c,'H2'))
            self.assertIn(c['first_hop_evidence']['text'],context_block(c,'H3'))

    def test_audit_rejects_surname_leak_and_wrong_remake(self):
        case=copy.deepcopy(self.cases[0])
        case['neutral_evidence']['text']='The film was praised by '+case['B'].split()[-1]+'.'
        with self.assertRaises(ValueError):audit_case(case)
        case=copy.deepcopy(self.cases[0]);case['neutral_evidence']['title']='Wrong remake'
        with self.assertRaises(ValueError):audit_case(case)

    def test_h3_override_is_valid_and_delta_and_sfir_are_correct(self):
        with tempfile.TemporaryDirectory() as directory,contextlib.redirect_stdout(io.StringIO()):
            out=Path(directory)/'run';prepare(out,self.data)
            records,stopped=run(self.cases,LadderAdapter(self.cases,override_h3=True),out)
            metrics,gate=analyze(self.cases,records,stopped)
            self.assertEqual(len(records),160)
            self.assertTrue(gate['passed'])
            self.assertEqual(metrics['context_levels']['H3']['OR']['rate'],1)
            self.assertEqual(metrics['context_levels']['H3']['delta_PR_from_H0'],-1)
            self.assertEqual(metrics['context_levels']['H3']['SFIR_B_prime']['rate'],1)
            self.assertEqual(metrics['context_levels']['H3']['SFIR_B']['rate'],0)
            export_results(out,self.cases,records)
            self.assertIn('PROPAGATE → OVERRIDE_TO_GOLD',(out/'inspection.md').read_text(encoding='utf-8'))
            with self.assertRaises(FileExistsError):prepare(out,self.data)
            with self.assertRaises(FileExistsError):run(self.cases,LadderAdapter(self.cases),out)

    def test_h0_collapse_stops_without_running_richer_levels(self):
        with tempfile.TemporaryDirectory() as directory,contextlib.redirect_stdout(io.StringIO()):
            adapter=LadderAdapter(self.cases,fail_h0=True)
            rows,stopped=run(self.cases,adapter,Path(directory))
            metrics,gate=analyze(self.cases,rows,stopped)
            self.assertEqual(len(adapter.calls),40)
            self.assertTrue(stopped)
            self.assertFalse(gate['passed'])
            self.assertNotIn('H1',metrics['context_levels'])
            self.assertIsNone(metrics['context_levels']['H0']['SFIR_B']['rate'])

    def test_aliases_and_provisional_unknown_answers(self):
        case=self.cases[1]
        for answer,expected in (('Dusseldorf','EXACT_CORRECT'),('Germany','OUT_OF_CONTEXT_HALLUCINATION'),
                                ('Unknown','UNKNOWN_REJECT'),('<location>','INVALID_OUTPUT')):
            row=case|parse_answer(answer)|dict(condition='state_B')
            label,pending=classify(row)
            self.assertEqual(label,expected)
            self.assertEqual(pending,answer=='Germany')

    def test_incomplete_or_duplicate_matrix_rejected(self):
        with tempfile.TemporaryDirectory() as directory,contextlib.redirect_stdout(io.StringIO()):
            records,_=run(self.cases,LadderAdapter(self.cases),Path(directory))
        with self.assertRaises(ValueError):analyze(self.cases,records[:-1])
        with self.assertRaises(ValueError):analyze(self.cases,records+[records[0]])


if __name__=='__main__':unittest.main()
