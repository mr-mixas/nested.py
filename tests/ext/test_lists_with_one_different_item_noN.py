"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/lists_with_one_different_item_noN.json
"""
import nested_diff


def test_diff():
    a = [0]
    b = [1]
    diff = {'D': [{'O': 0}]}
    opts = {'N': False}
    assert diff == nested_diff.diff(a, b, **opts)
