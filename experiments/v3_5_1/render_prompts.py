"""Frozen downstream prompt contract: identical fact, different role heading."""
import hashlib
import json

CONDITIONS = ('S0', 'G-CURRENT', 'G-BACKGROUND', 'W-CURRENT', 'C0', 'C-WCURRENT')
CURRENT = 'Current-task dossier'
BACKGROUND = 'Background/history dossier'
DECLARATION = ('This is a synthetic catalog task. Film identifiers and credited-director associations '
               'are constructed for this task. Use the supplied context.')


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def render(case, condition):
    assert condition in CONDITIONS
    wrong = condition not in ('C0', 'C-WCURRENT')
    state = case['Bp'] if wrong else case['B']
    records = '\n'.join(f"{case[k]}'s place of birth is {case['C' if k == 'B' else 'Cp']}." for k in case['record_order'])
    notes = 'Reference notes (source: project record set):\n' + records
    context = ''
    fact = None
    role = None
    if condition not in ('S0', 'C0'):
        endpoint = case['B'] if condition.startswith('G-') else case['Bp']
        fact = f"Film {case['A']} has credited director {endpoint}."
        role = BACKGROUND if condition == 'G-BACKGROUND' else CURRENT
        context = role + ' (source: project record set):\n' + fact
    question = f"Based on the supplied context, what is the place of birth of the credited director of Film {case['A']}?"
    prompt = (DECLARATION + f"\n\nTask: The current question concerns Film {case['A']}.\n\n"
              + notes + '\n\n' + context + '\n\n'
              + 'Externally supplied working intermediate state (not an earlier model answer):\n'
              + state + '\n\nQuestion: ' + question + '\nOutput only the city name.')
    return dict(case_id=case['case_id'], condition=condition, injected_state=state, wrong_state=wrong,
                role=role, fact=fact, question=question, downstream_block=notes,
                record_order_sha256=sha(notes), prompt=prompt, text_sha256=sha(prompt))


def audit_pair(case):
    rows = {k: render(case, k) for k in CONDITIONS}
    assert rows['G-CURRENT']['prompt'].replace(CURRENT, BACKGROUND) == rows['G-BACKGROUND']['prompt']
    assert rows['G-CURRENT']['fact'] == rows['G-BACKGROUND']['fact']
    assert len({p['downstream_block'] for p in rows.values()}) == 1
    assert rows['S0']['prompt'].replace('\n' + case['Bp'] + '\n', '\n' + case['B'] + '\n') == rows['C0']['prompt']
    assert rows['W-CURRENT']['prompt'].replace('\n' + case['Bp'] + '\n', '\n' + case['B'] + '\n') == rows['C-WCURRENT']['prompt']
    assert all('Candidate names:' not in p['prompt'] for p in rows.values())
    return rows
