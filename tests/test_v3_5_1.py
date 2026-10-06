import unittest
from experiments.v3_5_1.build_cases import make_cases
from experiments.v3_5_1.validate_cases import parse,validate
from experiments.v3_5_1.render_prompts import audit_pair,CONDITIONS,CURRENT,BACKGROUND
from experiments.v3_5_1.analyze import compute,binomial_interval


class FramingPilotTests(unittest.TestCase):
    def test_sources_graphs_and_pair_diffs(self):
        cases,people,_=make_cases()
        self.assertEqual(validate(cases)['verified_real_mappings'],24)
        self.assertEqual(sum(c['record_order'][0]=='B' for c in cases),6)
        for c in cases:
            rows=audit_pair(c)
            self.assertEqual(rows['G-CURRENT']['prompt'].replace(CURRENT,BACKGROUND),rows['G-BACKGROUND']['prompt'])
        fixture=dict(case_id='fixture',A='T64218',B='Helmut Käutner',Bp='Rolf Schübel',C='Düsseldorf',Cp='Stuttgart',record_order=['B','Bp'])
        self.assertEqual(people[fixture['B']]['target'],fixture['C'])
        self.assertEqual(people[fixture['Bp']]['target'],fixture['Cp'])
        self.assertEqual(audit_pair(fixture)['G-CURRENT']['fact'],audit_pair(fixture)['G-BACKGROUND']['fact'])
    def test_parser_does_not_coerce_explanations(self):
        c=dict(C_aliases=['Düsseldorf','Dusseldorf'],Cp_aliases=['Stuttgart'])
        self.assertEqual(parse('Dusseldorf.',c)['identity'],'C')
        self.assertEqual(parse('Stuttgart',c)['identity'],'Cp')
        self.assertEqual(parse('Düsseldorf or Stuttgart',c)['invalid_subtype'],'MULTIPLE')
        self.assertEqual(parse('Düsseldorf. Wait...',c)['parse_category'],'INVALID')
        self.assertEqual(parse('Stuttgart',c,True)['invalid_subtype'],'TRUNCATED')
        self.assertEqual(parse('unknown',c)['parse_category'],'UNKNOWN')
        self.assertEqual(parse('Paris',c)['parse_category'],'OTHER_ANSWER')
    def mock(self,framing_effect=False,fail_state=False):
        cases,_,_=make_cases();rows=[]
        for c in cases:
            for k,p in audit_pair(c).items():
                answer=c['Cp'] if k in ('S0','W-CURRENT','C-WCURRENT') else c['C']
                if framing_effect and k=='G-BACKGROUND':answer=c['Cp']
                if fail_state and k=='S0':answer=c['C']
                rows.append(p|dict(raw_text=answer,truncated=False))
        return compute(cases,rows,True)
    def test_null_and_manipulation_gates(self):
        _,m,g=self.mock()
        self.assertEqual(g['recommendation'],'STOP_UNINFORMATIVE')
        self.assertTrue(g['evidence_dominance'])
        self.assertEqual(m['primary']['transition_2x2']['C']['C'],12)
        _,m,g=self.mock(framing_effect=True)
        self.assertEqual(g['recommendation'],'PILOT_SIGNAL_CONFIRM_SEPARATELY')
        self.assertEqual(m['primary']['delta_OR']['rate'],1)
        _,_,g=self.mock(framing_effect=True,fail_state=True)
        self.assertEqual(g['recommendation'],'STOP_INVALID')
    def test_exact_binomial_boundary(self):
        self.assertAlmostEqual(binomial_interval(4,4)['exact95'][0],.025**.25)
        self.assertEqual(binomial_interval(4,4)['exact95'][1],1)


if __name__=='__main__':unittest.main()
