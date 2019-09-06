"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/one_item_removed_from_the_middle_of_list.json
"""
import nested_diff


def test_diff():
    a = [0, 1, 2]
    b = [0, 2]
    diff = {'D': [{'U': 0}, {'R': 1}, {'U': 2}]}
    opts = {}
    assert diff == nested_diff.diff(a, b, **opts)


def test_patch():
    a = [0, 1, 2]
    b = [0, 2]
    diff = {'D': [{'U': 0}, {'R': 1}, {'U': 2}]}
    assert b == nested_diff.patch(a, diff)
