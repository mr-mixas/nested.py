"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/empty_string_vs_0.json
"""
import nested_diff


def test_diff():
    a = ''
    b = 0
    diff = {'N': 0, 'O': ''}
    opts = {}
    assert diff == nested_diff.diff(a, b, **opts)


def test_patch():
    a = ''
    b = 0
    diff = {'N': 0, 'O': ''}
    assert b == nested_diff.patch(a, diff)
