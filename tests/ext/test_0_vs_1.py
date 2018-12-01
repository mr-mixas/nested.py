"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/0_vs_1.json
"""

from __future__ import unicode_literals

import nested_diff


def test_diff():
    a = 0
    b = 1
    diff = {'N': 1, 'O': 0}
    opts = {}
    assert diff == nested_diff.diff(a, b, **opts)


def test_patch():
    a = 0
    b = 1
    diff = {'N': 1, 'O': 0}
    assert b == nested_diff.patch(a, diff)
