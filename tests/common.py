import os
import pytest

import nested_diff


def do_test_function(test, func):

    if 'raises' in test:
        with test['raises']:
            func(test)
    else:
        # ensure diff is correct
        diff_opts = test.get('diff_opts', {})
        diff_should_be = nested_diff.diff(test['a'], test['b'], **diff_opts)
        if test.get('diff', {}) != diff_should_be:
            raise ValueError(diff_should_be)

        assert test['result'] == func(test)


def iterate_test_suite(tests_map, results_mod, func):
    results_map = {} if 'CANONIZE' in os.environ else results_mod.RESULTS

    for name, test in sorted(tests_map.items()):
        if 'CANONIZE' in os.environ:
            try:
                test['result'] = func(test)
                results_map[name] = {'result': test['result']}
            except Exception as e:
                results_map[name] = {
                    'raises': e if type(e) is type else type(e),
                }
        else:
            try:
                test['result'] = results_map[name]['result']
            except KeyError:
                test['raises'] = pytest.raises(results_map[name]['raises'])

        if 'result' in test or 'raises' in test:
            marks = []
        else:
            marks = [pytest.mark.xfail]

        yield pytest.param(test, func, id=name, marks=marks)

    if 'CANONIZE' in os.environ:
        save_test_suite(results_mod.__file__, results_map)


def save_test_suite(filename, results):
    with open(filename, 'w') as f:
        f.write('''"""
Autogenerated, do not edit manually!

"""
import sys


RESULTS = {
''')

        for k, v in sorted(results.items()):
            t = 'result' if 'result' in v else 'raises'
            if 'raises' in v:
                t = 'raises'
                r = v['raises'].__name__
            else:
                t = 'result'
                r = repr(v['result'])

            f.write("""\
    '{name}': {{
        '{type}': {result},
    }},
""".format(name=k, type=t, result=r))

        f.write("""}


if __name__ == '__main__':
    names = sys.argv[1:] if len(sys.argv) > 1 else sorted(RESULTS.keys())
    headers = len(names) > 1

    for name in names:
        if headers:
            print('========== ' + name + ' ==========')
        print(RESULTS[name].get('result', None), end='')
""")
