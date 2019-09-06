"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/1_vs_-1.json
"""
import nested_diff


def test_diff():
    a = 1
    b = -1
    diff = {'N': -1, 'O': 1}
    opts = {}
    assert diff == nested_diff.diff(a, b, **opts)


def test_patch():
    a = 1
    b = -1
    diff = {'N': -1, 'O': 1}
    assert b == nested_diff.patch(a, diff)
