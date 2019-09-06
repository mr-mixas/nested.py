"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/empty_list_vs_empty_hash.json
"""
import nested_diff


def test_diff():
    a = []
    b = {}
    diff = {'N': {}, 'O': []}
    opts = {}
    assert diff == nested_diff.diff(a, b, **opts)


def test_patch():
    a = []
    b = {}
    diff = {'N': {}, 'O': []}
    assert b == nested_diff.patch(a, diff)
