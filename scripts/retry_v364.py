"""User-authorized single retry, with the original zero-call failure untouched."""
import argparse
import json
from pathlib import Path
from experiments.v3_6_4 import prepare, run, report
from experiments.v3_6_0.prepare import digest

ORIGINAL = Path('results/v3_6_4')
TARGET = ORIGINAL/'attempt_02'


def configure():
    manifest = json.loads((TARGET/'retry_authorization.json').read_text(encoding='utf-8'))
    original_verify = prepare.verify
    prepare.OUT = run.OUT = report.OUT = TARGET
    def verify():
        original_verify()
        for path,value in manifest['preserved_original_attempt'].items():
            assert digest(path) == value, path
        for path,value in manifest['copied_inputs'].items():
            assert digest(path) == value, path
        assert digest(__file__) == manifest['retry_wrapper_sha256']
    run.verify = report.verify = verify
    return verify


def prepare_retry():
    assert not TARGET.exists(), 'Only one authorized retry; refuse overwriting'
    prepare.verify()
    state = prepare.load('run_state.json')
    assert state['status'] == 'INFRASTRUCTURE_FAILURE' and sum(state['counts'].values()) == 0
    original_files = {p.as_posix():digest(p) for p in ORIGINAL.iterdir() if p.is_file()}
    TARGET.mkdir()
    copied = {}
    original_manifest = prepare.load('manifest.json')
    for path in original_manifest['frozen']:
        p = Path(path)
        if p.parent == ORIGINAL:
            dest = TARGET/p.name
            dest.write_bytes(p.read_bytes())
            copied[dest.as_posix()] = digest(dest)
    (TARGET/'manifest.json').write_bytes((ORIGINAL/'manifest.json').read_bytes())
    copied[(TARGET/'manifest.json').as_posix()] = digest(TARGET/'manifest.json')
    auth = dict(user_request='这个INFRASTRUCTURE_FAILURE第一次发生，要不重新运行一下试试？',
                authorization='One retry explicitly authorized after zero-call native loading crash; supersedes original no-retry rule for this attempt only.',
                attempt=2,maximum_generation_calls=104,scientific_configuration_changed=False,
                preserved_original_attempt=original_files,copied_inputs=copied,retry_wrapper_sha256=digest(__file__))
    (TARGET/'retry_authorization.json').write_text(json.dumps(auth,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    configure()()
    print('Attempt02 prepared; original failure and all scientific inputs preserved.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action',choices=('prepare','run','report','verify'))
    args = parser.parse_args()
    if args.action == 'prepare':
        prepare_retry()
    else:
        verify = configure()
        verify()
        if args.action == 'run':
            run.run()
        elif args.action == 'report':
            report.report()
        else:
            print('Retry inputs and entire original attempt unchanged.')
