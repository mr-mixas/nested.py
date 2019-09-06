"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/one_item_inserted_in_the_middle_of_list_noU.json
"""
import nested_diff


def test_diff():
    a = [0, 2]
    b = [0, 1, 2]
    diff = {'D': [{'I': 1, 'A': 1}]}
    opts = {'U': False}
    assert diff == nested_diff.diff(a, b, **opts)


def test_patch():
    a = [0, 2]
    b = [0, 1, 2]
    diff = {'D': [{'I': 1, 'A': 1}]}
    assert b == nested_diff.patch(a, diff)
