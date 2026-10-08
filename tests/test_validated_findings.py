"""Regression checks for ledger contracts; no model or historical result writes."""
import copy
import unittest
from scripts.validated_findings import load, review_spec, validate_data, render, audit, changelog, ROOT


class LedgerProtocolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=load()

    def fixture(self):
        rows=[]
        for item in self.data['findings']+self.data['validated_components']:
            status=item['status']
            treatment='AVOIDED' if status=='ACTIVE_WARNING' else 'FROZEN_REUSE' if status=='FROZEN_REUSE' else 'NOT_RELEVANT'
            rows.append(dict(id=item['id'],ledger_status=status,treatment=treatment,rationale='本测试只验证协议字段，未授权真实实验。',modified=False))
        review=dict(ledger_sha256='fixture-hash',latest_completed_version=self.data['future_spec_protocol']['latest_incorporated_version'],rows=rows)
        return review

    def spec(self,review):
        lines=['# Prior Findings Review','','docs/validated_findings.md','docs/validated_findings.json','',
               '| Finding / Component | Ledger status | Treatment in this experiment | Rationale |','|---|---|---|---|']
        for r in review['rows']:
            lines.append('| '+' | '.join(r[k] for k in ('id','ledger_status','treatment','rationale'))+' |')
        return '\n'.join(lines)+'\n\n## Validated Inheritance\n\n## New manipulation\n'

    def check(self,r):
        return review_spec(self.data,self.spec(r),r,'fixture-hash')

    def test_complete_review(self):
        self.assertTrue(self.check(self.fixture())['passed'])

    def test_missing_warning_or_component_is_rejected(self):
        for target in ('F14','C01'):
            r=self.fixture();r['rows']=[v for v in r['rows'] if v['id']!=target]
            with self.assertRaises(AssertionError):self.check(r)

    def test_warning_cannot_be_ignored_or_overridden(self):
        for treatment in ('NOT_RELEVANT','OVERRIDDEN','FROZEN_REUSE','TARGETED'):
            r=self.fixture();next(x for x in r['rows'] if x['id']=='F14')['treatment']=treatment
            with self.assertRaises(AssertionError):self.check(r)

    def test_modified_component_requires_evidence_and_gate(self):
        r=self.fixture();c=next(x for x in r['rows'] if x['id']=='C01');c['modified']=True
        with self.assertRaises(AssertionError):self.check(r)
        c['treatment']='INTENTIONALLY_RETESTED';c['modification']={}
        with self.assertRaises(AssertionError):self.check(r)
        c['modification']=dict(component='C01',prior_evidence=['experiments/v3_6_1/design.py'],reason='独立诊断新输出协议',prior_conclusion_no_longer_applies='旧shell精确合规不能迁移',revalidation_gate='推理前固定独立格式/准确率门槛')
        self.assertTrue(self.check(r)['passed'])
        c['modification']['prior_evidence']=['invented.txt']
        with self.assertRaises(AssertionError):self.check(r)

    def test_stale_ledger_or_omitted_previous_experiment_rejected(self):
        for field,value in (('ledger_sha256','stale'),('latest_completed_version','v3.6.3')):
            r=self.fixture();r[field]=value
            with self.assertRaises(AssertionError):self.check(r)

    def test_markdown_and_review_must_agree(self):
        r=self.fixture();s=self.spec(r).replace('| F14 | ACTIVE_WARNING | AVOIDED |','| F14 | ACTIVE_WARNING | NOT_RELEVANT |')
        with self.assertRaises(AssertionError):review_spec(self.data,s,r,'fixture-hash')
        with self.assertRaises(AssertionError):review_spec(self.data,'# New study\n'+self.spec(r),r,'fixture-hash')

    def test_duplicate_id_and_invented_status_rejected(self):
        r=self.fixture();r['rows'].append(copy.deepcopy(r['rows'][0]))
        with self.assertRaises(AssertionError):self.check(r)
        r=self.fixture();r['rows'][0]['ledger_status']='FROZEN_REUSE'
        with self.assertRaises(AssertionError):self.check(r)

    def test_actual_ledger_consistent_and_historical_hashes_unchanged(self):
        self.assertTrue(validate_data(self.data))
        for name,content in (('validated_findings.md',render(self.data)),('validated_findings_audit.md',audit(self.data)),('validated_findings_CHANGELOG.md',changelog(self.data))):
            self.assertEqual((ROOT/'docs'/name).read_text(encoding='utf-8'),content)


if __name__=='__main__':
    unittest.main()
