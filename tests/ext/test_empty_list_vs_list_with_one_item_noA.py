"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/empty_list_vs_list_with_one_item_noA.json
"""
import nested_diff


def test_diff():
    a = []
    b = [0]
    diff = {}
    opts = {'A': False}
    assert diff == nested_diff.diff(a, b, **opts)
