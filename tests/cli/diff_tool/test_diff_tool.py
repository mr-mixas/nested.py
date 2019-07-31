import json
import os
import pytest
import sys

try:
    from unittest import mock
except ImportError:
    import mock

from nested_diff.diff_tool import App as DiffApp


def test_default_diff(capsys, expected, fullname):
    DiffApp(args=(
        fullname('lists.a.json', shared=True),
        fullname('lists.b.json', shared=True),
    )).run()

    captured = capsys.readouterr()
    assert '' == captured.err

    assert expected == captured.out


def test_default_diff_with_tty(capsys, expected, fullname, stringio_tty):
    with mock.patch('sys.stdout.isatty', return_value=True):
        DiffApp(args=(
            fullname('lists.a.json', shared=True),
            fullname('lists.b.json', shared=True),
        )).run()

    captured = capsys.readouterr()
    assert '' == captured.err

    assert expected == captured.out


def test_enable_U_ops(capsys, expected, fullname, PY2):
    DiffApp(args=(
        fullname('lists.a.json', shared=True),
        fullname('lists.b.json', shared=True),
        '--ofmt', 'json',
        '-U', '-U=1', '--U', '--U=1', '--U', '1',
    )).run()

    captured = capsys.readouterr()
    assert '' == captured.err

    if PY2:  # json in python2 emit trailing spaces
        assert json.loads(expected) == json.loads(captured.out)
    else:
        assert expected == captured.out


def test_output_file(capsys, expected, fullname, testfile):
    DiffApp(args=(
        fullname('lists.a.json', shared=True),
        fullname('lists.b.json', shared=True),
        '--ofmt', 'json',
        '--out', fullname('out'),
    )).run()

    captured = capsys.readouterr()
    assert '' == captured.err
    assert '' == captured.out

    assert json.loads(expected) == json.loads(testfile('out'))


def test_json_ofmt_opts(capsys, expected, fullname, PY2):
    DiffApp(args=(
        fullname('lists.a.json', shared=True),
        fullname('lists.b.json', shared=True),
        '--ofmt', 'json',
        '--ofmt-opts', '{"indent": null}',
    )).run()

    captured = capsys.readouterr()
    assert '' == captured.err

    if PY2:  # json in python2 emit trailing spaces
        assert json.loads(expected) == json.loads(captured.out)
    else:
        assert expected == captured.out


def test_ini_ifmt(capsys, expected, fullname, PY2):
    DiffApp(args=(
        fullname('lists.a.ini', shared=True),
        fullname('lists.b.ini', shared=True),
        '--ifmt', 'ini',
        '--ofmt', 'json',
    )).run()

    captured = capsys.readouterr()
    assert '' == captured.err

    if PY2:  # json in python2 emit trailing spaces
        assert json.loads(expected) == json.loads(captured.out)
    else:
        assert expected == captured.out


def test_text_ofmt(capsys, expected, fullname):
    DiffApp(args=(
        fullname('lists.a.json', shared=True),
        fullname('lists.b.json', shared=True),
        '--ofmt', 'text',
    )).run()

    captured = capsys.readouterr()
    assert '' == captured.err
    assert expected == captured.out


def test_term_ofmt(capsys, expected, fullname):
    DiffApp(args=(
        fullname('lists.a.json', shared=True),
        fullname('lists.b.json', shared=True),
        '--ofmt', 'term',
    )).run()

    captured = capsys.readouterr()
    assert '' == captured.err
    assert expected == captured.out


def test_yaml_ifmt(capsys, expected, fullname, PY2):
    DiffApp(args=(
        fullname('lists.a.yaml', shared=True),
        fullname('lists.b.yaml', shared=True),
        '--ifmt', 'yaml',
        '--ofmt', 'json',
    )).run()

    captured = capsys.readouterr()
    assert '' == captured.err

    if PY2:  # json in python2 emit trailing spaces
        assert json.loads(expected) == json.loads(captured.out)
    else:
        assert expected == captured.out


def test_yaml_ofmt(capsys, expected, fullname):
    DiffApp(args=(
        fullname('lists.a.json', shared=True),
        fullname('lists.b.json', shared=True),
        '--ofmt', 'yaml',
    )).run()

    captured = capsys.readouterr()
    assert '' == captured.err
    assert expected == captured.out