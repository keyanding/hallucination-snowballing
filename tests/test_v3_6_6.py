import copy
import math
import unittest
from experiments.v3_6_6.design import make_cases,make_mappings,first_prompt,down_prompt,route,first_parse,sha
from experiments.v3_6_6.analyze import analyze,cp,paired,proportion
from experiments.v3_6_6.run import execute,STAGES
from experiments.v3_6_6.prepare import review,inheritance
from experiments.inheritance import validate
from scripts.validated_findings import load,review_spec


class Tokenizer:
    def encode(self,s,**kwargs):return [1,2,3,4]


class ProspectiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases,cls.fresh=make_cases();cls.identity,cls.modules,cls.audit=make_mappings(cls.cases,Tokenizer())
        ids=[c['case_id'] for c in cls.cases]
        cls.schedule=dict(first_hop=ids,natural_downstream=ids,controlled=[dict(case_id=cid,arm=a) for a in ('G','A') for cid in ids],diagnostic_ids=ids[:24],order_diagnostic=ids[:24])
        cls.plans={}
        for c in cls.cases:
            cls.plans[c['case_id']+'/FIRST']=first_prompt(c)
            cls.plans[c['case_id']+'/DIAGNOSTIC']=first_prompt(c,True)
        for mid,m in cls.modules.items():
            for arm in ('G','A'):cls.plans[mid+'/'+arm]=down_prompt(m,arm)

    def raw(self,value,truncated=False):return dict(raw_text=value,raw_sha256=sha(value),truncated=truncated)

    def fixtures(self,wrong=0,invalid=0,diagnostic_wrong=False):
        result={s:[] for s in STAGES};cby={c['case_id']:c for c in self.cases};events=[];logs=[]
        wrongids=set(self.schedule['first_hop'][:wrong]);invalidids=set(self.schedule['first_hop'][wrong:wrong+invalid])
        def invoke(p):
            c=cby[p['case_id']]
            if p['cap']==96:
                value=next(n for n in self.identity[c['case_id']]['by_name'] if n!=c['gold']) if c['case_id'] in wrongids or diagnostic_wrong and p['call_id'].endswith('DIAGNOSTIC') else c['gold']
                if c['case_id'] in invalidids:value='The answer is '+c['gold']
            else:value=p['expected']
            return self.raw(value)
        execute(self.cases,self.identity,self.modules,self.schedule,self.plans,invoke,lambda s,r:result[s].append(r),events.append,logs.append)
        return result,events,logs

    def metrics(self,raw):return analyze(self.cases,self.identity,self.modules,raw,self.schedule)

    def test_full_bijection_inverse_and_three_branches(self):
        self.assertEqual(len(self.modules),360)
        selected=[a['raw'] for a in self.audit['candidates'] if a['selected']];self.assertEqual(len(set(selected)),960)
        for c in self.cases:
            cid=c['case_id'];m=self.identity[cid]
            self.assertEqual(len({v['state'].split('_')[-1] for v in m['by_name'].values()}|{v['outcome'].split('_')[-1] for v in m['by_name'].values()}),8)
            for name,v in m['by_name'].items():
                self.assertEqual(m['by_state'][v['state']],name);self.assertEqual(m['by_outcome'][v['outcome']],name)
                module,p,log=route(c,self.raw(name),self.identity,self.modules)
                self.assertEqual(p['supplied_state'],v['state'])
                if name!=c['gold']:self.assertEqual(module['alternate'],name)
                self.assertNotIn(name,p['prompt'])

    def test_cf_only_current_state_diff(self):
        for m in self.modules.values():
            a,b=down_prompt(m,'G'),down_prompt(m,'A');prefix,tail=a['prompt'].split('Current state:\n');_,suffix=tail.split('\n',1)
            self.assertEqual(prefix+'Current state:\n'+b['supplied_state']+'\n'+suffix,b['prompt'])

    def test_historical_name_parser_no_repair(self):
        c=self.cases[0]
        self.assertEqual(first_parse(self.raw(' '+c['gold']+' '),c)['category'],'GOLD')
        for value in ('The answer is '+c['gold'],c['gold']+'.','UNKNOWN'):
            self.assertFalse(first_parse(self.raw(value),c)['strict_valid'])
        self.assertEqual(first_parse(self.raw(c['gold'],True),c)['category'],'TRUNCATED')
        self.assertEqual(first_parse(None,c)['category'],'MISSING')

    def test_gold_wrong_forward_invalid_skips_controls_still_full(self):
        raw,events,logs=self.fixtures(3,2)
        self.assertEqual([len(raw[k]) for k in STAGES],[120,118,240,24])
        self.assertEqual(len(logs),120)
        self.assertEqual(sum(x['natural_status'].startswith('SKIPPED') for x in logs),2)
        for log in logs[:3]:self.assertEqual(log['first_category'],'WRONG')
        statuses=[e['status'] for e in events]
        self.assertEqual(statuses.count('CALL_STARTED'),502)
        self.assertEqual(statuses.count('CALL_COMPLETED'),502)

    def test_zero_wrong_null_and_no_diagnostic_denominator_contamination(self):
        raw,_,_=self.fixtures(diagnostic_wrong=True);m=self.metrics(raw)
        self.assertEqual(m['W'],0);self.assertIsNone(m['proportions']['conditional_propagation']['rate'])
        self.assertEqual(m['proportions']['UCR']['rate'],0)
        self.assertEqual(m['information']['status'],'NO_ESTIMABLE_CONDITIONAL_TRAJECTORY')
        self.assertEqual(m['collection_status'],'PROSPECTIVE_COLLECTION_COMPLETE')

    def test_full_propagation_and_paired_rd(self):
        raw,_,_=self.fixtures(24);m=self.metrics(raw)
        self.assertEqual(m['proportions']['conditional_propagation']['count'],24)
        self.assertEqual(m['proportions']['UCR']['count'],24)
        self.assertEqual(m['proportions']['strict_end_to_end_success']['count'],96)
        self.assertEqual(m['paired']['all_controlled']['RD'],1)
        self.assertEqual(m['paired']['natural_wrong_subset']['n_pairs'],24)
        self.assertEqual(m['capability']['status'],'CURRENT_COHORT_CAPABILITY_SUPPORTED')

    def test_override_is_not_strict_e2e(self):
        raw,_,_=self.fixtures(1);cid=raw['natural_downstream'][0]['case_id'];module=route(self.cases[0],raw['first_hop'][0],self.identity,self.modules)[0]
        raw['natural_downstream'][0].update(self.raw(module['legacy']['outcome_a']))
        m=self.metrics(raw)
        self.assertEqual(m['natural_wrong_counts']['OVERRIDE'],1)
        self.assertEqual(m['proportions']['strict_end_to_end_success']['count'],119)
        self.assertEqual(m['proportions']['final_gold_rate']['count'],120)

    def test_missing_bounds_not_other_or_zero(self):
        raw,_,_=self.fixtures(1);raw['first_hop'].pop();raw['natural_downstream']=raw['natural_downstream'][1:-1]
        raw['controlled']=[r for r in raw['controlled'] if r['case_id']!=self.cases[-1]['case_id'] and r['case_id']!=self.cases[0]['case_id']]
        m=self.metrics(raw)
        self.assertEqual(m['cascade_missing_bounds']['uncertain_cases'],2)
        self.assertAlmostEqual(m['cascade_missing_bounds']['upper'],2/120)
        self.assertIsNone(m['proportions']['UCR']['rate']);self.assertEqual(m['natural_wrong_counts']['MISSING'],1)
        self.assertEqual(m['capability']['status'],'NOT_FULLY_EVALUATED')

    def test_invalid_control_counts_binary_zero_not_missing(self):
        raw,_,_=self.fixtures(1)
        r=next(r for r in raw['controlled'] if r['call_id']==self.cases[0]['case_id']+'/CONTROL_A');r.update(self.raw('UNKNOWN'))
        m=self.metrics(raw)
        self.assertEqual(m['paired']['all_controlled']['n_pairs'],120)
        self.assertEqual(m['paired']['natural_wrong_subset']['table']['00'],1)

    def test_low_information_does_not_stop_collection(self):
        raw,_,_=self.fixtures(3);m=self.metrics(raw)
        self.assertEqual(m['information']['status'],'LOW_INFORMATION_CONDITIONAL_ESTIMATE')
        self.assertEqual(m['stage_counts']['controlled'],240)
        self.assertEqual(m['collection_status'],'PROSPECTIVE_COLLECTION_COMPLETE')

    def test_duplicate_main_dispatch_rejected_before_second_call(self):
        s=copy.deepcopy(self.schedule);s['first_hop'].insert(1,s['first_hop'][0]);calls=[]
        def invoke(p):calls.append(p);return self.raw(self.cases[0]['gold'])
        with self.assertRaises(AssertionError):execute(self.cases,self.identity,self.modules,s,self.plans,invoke,lambda s,r:None,lambda r:None,lambda r:None)
        self.assertEqual(len(calls),1)

    def test_cp_endpoints_and_paired_zero_discordance_width(self):
        self.assertAlmostEqual(cp(0,120)[1],1-.0125**(1/120),12)
        self.assertAlmostEqual(cp(120,120)[0],.0125**(1/120),12)
        lo,hi=cp(5,10);self.assertAlmostEqual(lo,1-hi,12)
        self.assertAlmostEqual(sum(math.comb(10,k)*lo**k*(1-lo)**(10-k) for k in range(5,11)),.0125,12)
        p=paired([(0,0)]*120);self.assertEqual(p['RD'],0);self.assertLess(p['paired95'][0],0);self.assertGreater(p['paired95'][1],0)
        self.assertIsNone(paired([])['RD']);self.assertIsNone(proportion(0,0)['wilson95'])

    def test_paired_discordances_not_independent_arms(self):
        p=paired([(1,0)]*3+[(0,1)]+[(1,1)]*2+[(0,0)]*4)
        self.assertEqual(p['table'],{'00':4,'01':1,'10':3,'11':2});self.assertEqual(p['RD'],.2)

    def test_both_inheritance_validators(self):
        d=load();r,t=review(d,'hash');spec='# Prior Findings Review\n\ndocs/validated_findings.md docs/validated_findings.json\n'+t+'\n## Validated Inheritance\n\n## New manipulation\n'
        self.assertTrue(review_spec(d,spec,r,'hash')['passed']);self.assertTrue(validate(spec,inheritance()))


if __name__=='__main__':unittest.main()
