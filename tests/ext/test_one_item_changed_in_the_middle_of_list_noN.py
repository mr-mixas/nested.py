"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/one_item_changed_in_the_middle_of_list_noN.json
"""
import nested_diff


def test_diff():
    a = [0, 1, 2]
    b = [0, 9, 2]
    diff = {'D': [{'U': 0}, {'O': 1}, {'U': 2}]}
    opts = {'N': False}
    assert diff == nested_diff.diff(a, b, **opts)
