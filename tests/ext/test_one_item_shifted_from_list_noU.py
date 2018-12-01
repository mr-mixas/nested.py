"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/one_item_shifted_from_list_noU.json
"""

from __future__ import unicode_literals

import nested_diff


def test_diff():
    a = [0, 1]
    b = [1]
    diff = {'D': [{'R': 0}]}
    opts = {'U': False}
    assert diff == nested_diff.diff(a, b, **opts)


def test_patch():
    a = [0, 1]
    b = [1]
    diff = {'D': [{'R': 0}]}
    assert b == nested_diff.patch(a, diff)
