"""
Do not edit manually! Generated from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/1_vs_1_as_string.json
"""

from __future__ import unicode_literals
import nested_diff


def test_1_vs_1_as_string():
    a = 1
    b = '1'
    diff = {'N': '1', 'O': 1}
    opts = {}
    assert diff == nested_diff.diff(a, b, **opts)