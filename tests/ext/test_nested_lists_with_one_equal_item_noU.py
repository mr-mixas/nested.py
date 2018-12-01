"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/nested_lists_with_one_equal_item_noU.json
"""

from __future__ import unicode_literals

import nested_diff


def test_diff():
    a = [[0]]
    b = [[0]]
    diff = {}
    opts = {'U': False}
    assert diff == nested_diff.diff(a, b, **opts)


def test_patch():
    a = [[0]]
    b = [[0]]
    diff = {}
    assert b == nested_diff.patch(a, diff)
