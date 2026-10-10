"""Independent raw-token, route, endpoint and paired-table recount; zero inference."""
import json
import unicodedata
from collections import Counter
from transformers import AutoTokenizer
from experiments.v3_6_6.prepare import OUT,load,write,verify,MODEL,REVISION
from src.interface_v3_4_4 import parse_natural


def rows(name):return [json.loads(s) for s in (OUT/name).read_text(encoding='utf-8').splitlines() if s]


def main():
    verify();m=load('metrics.json');assert m['collection_status']=='PROSPECTIVE_COLLECTION_COMPLETE'
    tok=AutoTokenizer.from_pretrained(MODEL,revision=REVISION,cache_dir='.cache/huggingface',local_files_only=True)
    stages=('first_hop','natural_downstream','controlled','order_diagnostic');raw={s:rows(s+'_raw.jsonl') for s in stages}
    cases=load('cases.json');identity=load('identity_state_map.json');modules=load('downstream_modules.json');schedule=load('call_schedule.json')
    primary={r['case_id']:r for r in raw['first_hop']};natural={r['case_id']:r for r in raw['natural_downstream']};controls={r['call_id']:r for r in raw['controlled']}
    journal=rows('call_journal.jsonl');starts=[r for r in journal if r['status']=='CALL_STARTED'];ends=[r for r in journal if r['status']=='CALL_COMPLETED']
    assert len(starts)==len(ends)==sum(map(len,raw.values()))
    assert len({r['call_id'] for r in starts})==len(starts)
    assert [r['stage'] for r in starts]==sum(([stage]*len(raw[stage]) for stage in stages),[])
    for rs in raw.values():
        for r in rs:
            assert tok.decode(r['output_token_ids'],skip_special_tokens=True)==r['raw_text']
            assert r['truncated']==(r['output_tokens']>=r['cap'] and r['output_token_ids'][-1]!=tok.eos_token_id)
            assert tok.encode(r['rendered_prompt'],add_special_tokens=False)==r['input_token_ids']
    counts=Counter();allpair=Counter();wrongpair=Counter();wrong_persons=Counter();bundles=set();routeorders=Counter()
    normalize=lambda r:None if r['truncated'] else unicodedata.normalize('NFC',r['raw_text']).strip().removesuffix('.')
    for c in cases:
        cid=c['case_id'];r=primary[cid];p=parse_natural(r['raw_text'],[x['name'] for x in c['candidates']],r['truncated'],{})
        table=identity[cid];gold=table['by_name'][c['gold']];wrong=p['strict_valid'] and p['identity']!=c['gold']
        counts['V']+=p['strict_valid'];counts['W']+=wrong;counts['G']+=p['strict_valid'] and not wrong
        alt=p['identity'] if wrong else table['default_alternate'];a=table['by_name'][alt]
        mid=cid+'/'+a['person_id'];assert modules[mid]['alternate']==alt
        cg=controls[cid+'/CONTROL_G'];ca=controls[cid+'/CONTROL_A']
        assert cg['module_id']==ca['module_id']==mid
        assert cg['supplied_state']==gold['state'] and ca['supplied_state']==a['state']
        before,tail=cg['prompt'].split('Current state:\n');_,suffix=tail.split('\n',1)
        assert before+'Current state:\n'+a['state']+'\n'+suffix==ca['prompt']
        YA=int(normalize(ca)==a['outcome']);YG=int(normalize(cg)==a['outcome']);key=f'{YA}{YG}';allpair[key]+=1
        if wrong:wrongpair[key]+=1;wrong_persons[p['identity']]+=1;bundles.add(c['bundle_id'])
        counts['control_G_correct']+=normalize(cg)==gold['outcome'];counts['control_A_correct']+=YA
        counts['paired_correct']+=normalize(cg)==gold['outcome'] and bool(YA)
        if p['strict_valid']:
            nr=natural[cid];assert nr['supplied_state']==table['by_name'][p['identity']]['state'] and nr['module_id']==mid
            assert nr['upstream_provenance']['raw_hash']==r['raw_sha256']
            value=normalize(nr);counts['P']+=wrong and value==a['outcome'];counts['O']+=wrong and value==gold['outcome']
            counts['T']+=wrong and value not in (gold['outcome'],a['outcome'])
            counts['E2E']+=not wrong and value==gold['outcome'];counts['final_gold']+=value==gold['outcome']
        else:assert cid not in natural
    assert len(cases)==len(primary)==120 and len(natural)==counts['V'] and len(controls)==240 and len(raw['order_diagnostic'])==24
    assert counts['P']+counts['O']+counts['T']==counts['W']
    for k in ('V','W','G'):assert counts[k]==m[k]
    for k,key in [('P','UCR'),('E2E','strict_end_to_end_success'),('final_gold','final_gold_rate')]:assert counts[k]==m['proportions'][key]['count']
    for table,key in [(allpair,'all_controlled'),(wrongpair,'natural_wrong_subset')]:
        assert {k:table[k] for k in ('00','01','10','11')}==m['paired'][key]['table']
        n=sum(table.values());assert m['paired'][key]['RD']==((table['10']-table['01'])/n if n else None)
    for k,v in [('G_adherence',counts['control_G_correct']),('A_adherence',counts['control_A_correct']),('paired_both_correct',counts['paired_correct'])]:assert m['capability'][k]['count']==v
    assert len(wrong_persons)==m['information']['all_wrong_identities'] and len(bundles)==m['information']['all_wrong_bundles']
    diagnostic_changes=0;comparable=0
    cby={c['case_id']:c for c in cases}
    for r in raw['order_diagnostic']:
        cid=r['case_id'];c=cby[cid];names=[x['name'] for x in c['candidates']]
        a=parse_natural(primary[cid]['raw_text'],names,primary[cid]['truncated'],{});b=parse_natural(r['raw_text'],names,r['truncated'],{})
        assert cid in schedule['diagnostic_ids']
        assert primary[cid]['prompt'].split('Graph-link records:\n')[1]==r['prompt'].split('Graph-link records:\n')[1]
        if a['strict_valid'] and b['strict_valid']:comparable+=1;diagnostic_changes+=a['identity']!=b['identity']
    assert diagnostic_changes==m['diagnostic']['counts']['changed'] and comparable==m['diagnostic']['counts']['comparable']
    result=dict(passed=True,model_calls_for_verification=0,token_round_trips=sum(map(len,raw.values())),independent_counts=dict(counts),
                all_controlled_table=dict(allpair),wrong_controlled_table=dict(wrongpair),wrong_identity_counts=dict(wrong_persons),wrong_bundles=len(bundles),
                diagnostic_changes=diagnostic_changes,diagnostic_comparable=comparable,prior_artifacts_unchanged=len(load('freeze_manifest.json')['prior_artifacts']),
                original_freeze_unchanged=True)
    write('independent_verification.json',result);print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
