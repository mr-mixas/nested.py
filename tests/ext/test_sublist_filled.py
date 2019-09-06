"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/sublist_filled.json
"""
import nested_diff


def test_diff():
    a = [[]]
    b = [[0]]
    diff = {'D': [{'D': [{'A': 0}]}]}
    opts = {}
    assert diff == nested_diff.diff(a, b, **opts)


def test_patch():
    a = [[]]
    b = [[0]]
    diff = {'D': [{'D': [{'A': 0}]}]}
    assert b == nested_diff.patch(a, diff)
