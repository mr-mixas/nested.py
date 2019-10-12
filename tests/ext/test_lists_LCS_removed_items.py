"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/lists_LCS_removed_items.json
"""
import nested_diff


def test_diff():
    a = [0, 1, 2, 3, 4, 5, 6, 7]
    b = [2, 3, 5]
    diff = {'D': [{'R': 0}, {'R': 1}, {'U': 2}, {'U': 3}, {'R': 4}, {'U': 5}, {'R': 6}, {'R': 7}]}
    opts = {}
    assert diff == nested_diff.diff(a, b, **opts)


def test_patch():
    diff = {'D': [{'R': 0}, {'R': 1}, {'U': 2}, {'U': 3}, {'R': 4}, {'U': 5}, {'R': 6}, {'R': 7}]}
    target = [0, 1, 2, 3, 4, 5, 6, 7]
    patched = [2, 3, 5]
    assert patched == nested_diff.patch(target, diff)
