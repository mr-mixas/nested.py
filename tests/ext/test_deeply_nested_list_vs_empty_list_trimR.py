"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/deeply_nested_list_vs_empty_list_trimR.json
"""
import nested_diff


def test_diff():
    a = [[[0, 1]]]
    b = []
    diff = {'D': [{'R': None}]}
    opts = {'trimR': True}
    assert diff == nested_diff.diff(a, b, **opts)


def test_patch():
    diff = {'D': [{'R': None}]}
    target = [[[0, 1]]]
    patched = []
    assert patched == nested_diff.patch(target, diff)
