"""
Do not edit manually! Generated by tests/gen_ext_tests.py from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/nested_lists_LCS_onlyU.json
"""

from __future__ import unicode_literals

import nested_diff


def test_diff():
    a = ['a', 'b', 'c', 'e', 'h', 'j', 'l', 'm', 'n', 'p']
    b = ['b', 'c', 'd', 'e', 'f', 'j', 'k', 'l', 'm', 'r', 's', 't']
    diff = {'D': [{'I': 1, 'U': 'b'}, {'U': 'c'}, {'I': 3, 'U': 'e'}, {'I': 5, 'U': 'j'}, {'I': 6, 'U': 'l'}, {'U': 'm'}]}
    opts = {'N': False, 'O': False, 'A': False, 'R': False}
    assert diff == nested_diff.diff(a, b, **opts)
