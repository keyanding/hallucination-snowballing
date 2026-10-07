"""Pre-inference enforcement of explicit experimental inheritance."""

CLASSIFICATIONS = {'FROZEN_REUSE', 'INTENTIONALLY_RETESTED', 'NOT_RELEVANT'}


def validate(spec, rows):
    assert '## Validated Inheritance' in spec
    assert spec.index('## Validated Inheritance') < spec.index('## New manipulation')
    assert rows and len({r['component'] for r in rows}) == len(rows)
    for row in rows:
        assert row['classification'] in CLASSIFICATIONS
        assert all(row[k] for k in ('component', 'prior_version', 'prior_result', 'treatment', 'validation'))
        if row['modified']:
            assert row['classification'] == 'INTENTIONALLY_RETESTED'
            assert row['reason'] and row['prior_conclusion_no_longer_applies']
        if row['classification'] == 'FROZEN_REUSE':
            assert not row['modified']
    return True
