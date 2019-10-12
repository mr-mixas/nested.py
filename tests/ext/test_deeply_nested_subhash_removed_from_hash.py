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
    diff = {'D': {'four': {'U': 4}, 'one': {'R': {'two': {'three': 3}}}}}
    target = {'four': 4, 'one': {'two': {'three': 3}}}
    patched = {'four': 4}
    assert patched == nested_diff.patch(target, diff)
