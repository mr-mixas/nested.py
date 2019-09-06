"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/deeply_nested_subhash_removed_from_hash.json
"""
import nested_diff


def test_diff():
    a = {'four': 4, 'one': {'two': {'three': 3}}}
    b = {'four': 4}
    diff = {'D': {'four': {'U': 4}, 'one': {'R': {'two': {'three': 3}}}}}
    opts = {}
    assert diff == nested_diff.diff(a, b, **opts)


def test_patch():
    a = {'four': 4, 'one': {'two': {'three': 3}}}
    b = {'four': 4}
    diff = {'D': {'four': {'U': 4}, 'one': {'R': {'two': {'three': 3}}}}}
    assert b == nested_diff.patch(a, diff)
