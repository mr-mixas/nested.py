import pytest

from nested_diff import Iterator, diff, _hdict


def test_scalar_diff():
    a = 0
    b = 1

    expected = [(0, None, {'N': 1, 'O': 0}, False)]
    got = list(Iterator().iterate(diff(a, b)))

    assert expected == got


def test_dict_diff():
    a = {'1': 1, '2': {'9': 9, '10': 10}, '3': 3}
    b = {'1': 1, '2': {'9': 8, '10': 10}, '4': 4}

    expected = [
        (0, None, {'D': {'1': {'U': 1}, '3': {'R': 3}, '2': {'D': {'9': {'N': 8, 'O': 9}, '10': {'U': 10}}}, '4': {'A': 4}}}, False),
        (1, '1', {'U': 1}, True),
        (1, '2', {'D': {'9': {'N': 8, 'O': 9}, '10': {'U': 10}}}, True),
        (2, '10', {'U': 10}, True),
        (2, '9', {'N': 8, 'O': 9}, True),
        (1, '3', {'R': 3}, True),
        (1, '4', {'A': 4}, True),
    ]

    got = list(Iterator().iterate(diff(a, b)))

    for i in expected:
        assert i in got

    assert len(got) == 7


def test_dict_diff_keys_sorted():
    a = {'1': 1, '2': {'9': 9, '10': 10}, '3': 3}
    b = {'1': 1, '2': {'9': 8, '10': 10}, '4': 4}

    expected = [
        (0, None, {'D': {'1': {'U': 1}, '3': {'R': 3}, '2': {'D': {'9': {'N': 8, 'O': 9}, '10': {'U': 10}}}, '4': {'A': 4}}}, False),
        (1, '1', {'U': 1}, True),
        (1, '2', {'D': {'9': {'N': 8, 'O': 9}, '10': {'U': 10}}}, True),
        (2, '10', {'U': 10}, True),
        (2, '9', {'N': 8, 'O': 9}, True),
        (1, '3', {'R': 3}, True),
        (1, '4', {'A': 4}, True),
    ]

    got = list(Iterator(sort_keys=True).iterate(diff(a, b)))

    assert expected == got


def test_list_diff():
    a = [0, [1], 3]
    b = [0, [1, 2], 3]

    expected = [
        (0, None, {'D': [{'U': 0}, {'D': [{'U': 1}, {'A': 2}]}, {'U': 3}]}, False),
        (1, 0, {'U': 0}, True),
        (1, 1, {'D': [{'U': 1}, {'A': 2}]}, True),
        (2, 0, {'U': 1}, True),
        (2, 1, {'A': 2}, True),
        (1, 2, {'U': 3}, True),
    ]

    got = list(Iterator().iterate(diff(a, b)))

    assert expected == got


def test_list_diff_noU():
    a = [0, [1], 3]
    b = [0, [1, 2], 3]

    expected = [
        (0, None, {'D': [{'D': [{'A': 2, 'I': 1}], 'I': 1}]}, False),
        (1, 1, {'D': [{'A': 2, 'I': 1}], 'I': 1}, True),
        (2, 1, {'A': 2, 'I': 1}, True),
    ]

    got = list(Iterator().iterate(diff(a, b, U=False)))

    assert expected == got


def test_set_diff():
    a = {0, 1}
    b = {0, 2}

    got = list(Iterator().iterate(diff(a, b)))

    assert len(got) == 4
    assert got[0] == (0, None, {'D': {_hdict('R', 1), _hdict('A', 2), _hdict('U', 0)}}, False)
    assert (1, None, {'R': 1}, False) in got
    assert (1, None, {'A': 2}, False) in got
    assert (1, None, {'U': 0}, False) in got


def test_custom_containers():
    class custom_container(tuple):
        pass

    diff = {'D': custom_container([{'O': 0, 'N': 1}])}

    it = Iterator()
    it.set_iter(custom_container, it.iter_sequence)

    expected = [
        (0, None, {'D': ({'N': 1, 'O': 0},)}, False),
        (1, 0, {'N': 1, 'O': 0}, True)
    ]

    got = list(it.iterate(diff))

    assert expected == got


def test_unknown_containers():
    class unknown_container(tuple):
        pass

    diff = {'D': unknown_container([{'O': 0, 'N': 1}])}

    with pytest.raises(NotImplementedError):
        got = list(Iterator().iterate(diff))