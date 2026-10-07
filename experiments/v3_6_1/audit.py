"""Static, descriptive audit of all old calibration cases; zero inference."""
from collections import Counter, defaultdict
from .design import token_info, normalize


def static_audit(cases, outputs, tokenizer):
    by = {(r['case_id'], r['condition']): r for r in outputs}
    results = []
    for c in cases:
        base = by[c['case_id'], 'C0']
        rev = by[c['case_id'], 'REVERSE']
        ent = by[c['case_id'], 'ENTITY_LABEL']
        def correct(r):
            return not r['truncated'] and normalize(r['raw_text']) == r['expected']
        def invariant(r):
            return not r['truncated'] and not base['truncated'] and normalize(r['raw_text']) == normalize(base['raw_text'])
        flags = dict(C0_failed=not correct(base), REVERSE_failed=not invariant(rev),
                     ENTITY_LABEL_failed=not invariant(ent), REVERSE_incorrect=not correct(rev),
                     ENTITY_LABEL_incorrect=not correct(ent),
                     any_mapped_UNKNOWN=any(r['case_id'] == c['case_id'] and r['condition'] != 'UNMAPPED' and normalize(r['raw_text']) == 'UNKNOWN' for r in outputs))
        ids = []
        for field in ('entity', 'alternate_entity', 'gold_state', 'wrong_state', 'gold_outcome', 'wrong_outcome', 'unmapped_state'):
            role = field.split('_')[0]
            position = c['record_order'].index(role)+1 if role in ('gold', 'wrong') else None
            ids.append(token_info(tokenizer, c[field]) | dict(field=field, mapping_line_position=position,
                       reversed_mapping_line_position=3-position if position else None, entity_token_count=len(tokenizer.encode(c['entity'], add_special_tokens=False)), **flags))
        results.append(dict(case_id=c['case_id'], gold_mapping_position=c['record_order'].index('gold')+1,
                            identifiers=ids, flags=flags, C0=normalize(base['raw_text']), REVERSE=normalize(rev['raw_text']),
                            ENTITY_LABEL=normalize(ent['raw_text']), gold_outcome=c['gold_outcome']))
    groups = {}
    for field in ('gold_state', 'gold_outcome', 'entity'):
        groups[field] = {}
        for failed in (False, True):
            counts = Counter(next(i['token_count'] for i in r['identifiers'] if i['field'] == field) for r in results if r['flags']['C0_failed'] == failed)
            groups[field]['failed' if failed else 'passed'] = dict(counts)
    positions = {str(p): dict(total=sum(r['gold_mapping_position'] == p for r in results), failures=sum(r['gold_mapping_position'] == p and r['flags']['C0_failed'] for r in results)) for p in (1, 2)}
    lexical = {}
    for field in ('gold_state', 'gold_outcome', 'entity'):
        lexical[field] = {}
        for part, index in [('letter', 0), ('tens', 1), ('units', 2)]:
            cells = defaultdict(lambda: dict(total=0, C0_failures=0))
            for r in results:
                raw = next(i['raw'] for i in r['identifiers'] if i['field'] == field)
                key = raw.split('_')[-1][index]
                cells[key]['total'] += 1
                cells[key]['C0_failures'] += r['flags']['C0_failed']
            lexical[field][part] = dict(sorted(cells.items()))
    reversal = dict(total_invariance_failures=sum(r['flags']['REVERSE_failed'] for r in results),
                    C0_wrong_reverse_correct=sum(r['flags']['C0_failed'] and not r['flags']['REVERSE_incorrect'] for r in results),
                    C0_correct_reverse_wrong=sum(not r['flags']['C0_failed'] and r['flags']['REVERSE_incorrect'] for r in results))
    entity = dict(total_invariance_failures=sum(r['flags']['ENTITY_LABEL_failed'] for r in results),
                  C0_wrong_entity_correct=sum(r['flags']['C0_failed'] and not r['flags']['ENTITY_LABEL_incorrect'] for r in results),
                  C0_correct_entity_wrong=sum(not r['flags']['C0_failed'] and r['flags']['ENTITY_LABEL_incorrect'] for r in results))
    data = dict(cases=results, C0_failure_positions=positions, token_count_groups=groups, lexical_contingencies=lexical,
                reversal= reversal, entity_label=entity, note='Descriptive associations among 20 cases, not causal tests. Failure flags distinguish invariance from correctness.')
    md = ['# Static audit of v3.6.0', '', 'All 20 calibration cases; zero new model calls. REVERSE/ENTITY_LABEL failure means failed invariance vs C0; correctness is separately recorded.', '',
          '| Case | Gold line | C0 incorrect | Reverse changed | Reverse incorrect | Entity changed | Entity incorrect | Any mapped UNKNOWN |', '|---|---|---|---|---|---|---|---|']
    for r in results:
        f = r['flags']
        md.append('| '+r['case_id']+' | '+str(r['gold_mapping_position'])+' | '+' | '.join(str(f[k]) for k in ('C0_failed', 'REVERSE_failed', 'REVERSE_incorrect', 'ENTITY_LABEL_failed', 'ENTITY_LABEL_incorrect', 'any_mapped_UNKNOWN'))+' |')
    md += ['', '## Required descriptive checks', '', f'1. C0 failures by gold mapping line: {positions}.',
           f"2. Gold-state token lengths, failed vs passed: {groups['gold_state']}.",
           f"3. Gold-outcome token lengths: {groups['gold_outcome']}.", f"4. Entity token lengths: {groups['entity']}.",
           '5. All IDs share a role prefix by construction. Letter/tens/units contingency counts for all cases are recorded in the JSON; three failures cannot establish a lexical cause.',
           f'6. Reversal transitions: {reversal}.', f'7. Entity-label transitions: {entity}.', '', '## Every identifier', '',
           '| Case | Field | Raw | Token IDs | Tokens | Characters | Mapping line |', '|---|---|---|---|---|---|---|']
    for r in results:
        for i in r['identifiers']:
            md.append(f"| {r['case_id']} | {i['field']} | {i['raw']} | {i['token_ids']} | {i['token_count']} | {i['character_length']} | {i['mapping_line_position']} |")
    return data, '\n'.join(md)+'\n'
