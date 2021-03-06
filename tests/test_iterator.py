from nested_diff import Iterator, diff


def test_get_iterator__final_diff():
    got = list(Iterator().get_iterator({'U': 1}))
    assert [({'U': 1}, None, None)] == got


def test_get_iterator__nested_diff():
    d = {'D': [{'U': 1}, {'A': 2}]}
    expected = [
        (d, 0, {'U': 1}),
        (d, 1, {'A': 2}),
    ]

    got = list(Iterator().get_iterator(d))
    assert expected == got


def test_scalar_diff():
    a = 0
    b = 1
    d = diff(a, b)

    expected = [(d, None, None, 0)]
    got = list(Iterator().iterate(d))

    assert expected == got


def test_dict_diff():
    a = {'1': 1, '2': {'9': 9, '10': 10}, '3': 3}
    b = {'1': 1, '2': {'9': 8, '10': 10}, '4': 4}
    d = diff(a, b)

    expected = [
        (d, '1', d['D']['1'], 0),
        (d['D']['1'], None, None, 1),

        (d, '2', d['D']['2'], 0),
        (d['D']['2'], '10', d['D']['2']['D']['10'], 1),
        (d['D']['2']['D']['10'], None, None, 2),
        (d['D']['2'], '9', d['D']['2']['D']['9'], 1),
        (d['D']['2']['D']['9'], None, None, 2),

        (d, '3', d['D']['3'], 0),
        (d['D']['3'], None, None, 1),

        (d, '4', d['D']['4'], 0),
        (d['D']['4'], None, None, 1),
    ]

    got = list(Iterator().iterate(d))

    for i in expected:
        assert i in got

    assert len(got) == 11


def test_dict_diff__keys_sorted():
    a = {'1': 1, '2': {'9': 9, '10': 10}, '3': 3}
    b = {'1': 1, '2': {'9': 8, '10': 10}, '4': 4}
    d = diff(a, b)

    expected = [
        (d, '1', d['D']['1'], 0),
        (d['D']['1'], None, None, 1),

        (d, '2', d['D']['2'], 0),
        (d['D']['2'], '10', d['D']['2']['D']['10'], 1),
        (d['D']['2']['D']['10'], None, None, 2),
        (d['D']['2'], '9', d['D']['2']['D']['9'], 1),
        (d['D']['2']['D']['9'], None, None, 2),

        (d, '3', d['D']['3'], 0),
        (d['D']['3'], None, None, 1),

        (d, '4', d['D']['4'], 0),
        (d['D']['4'], None, None, 1),
    ]

    got = list(Iterator(sort_keys=True).iterate(d))

    assert expected == got


def test_list_diff():
    a = [0, [1], 3]
    b = [0, [1, 2], 3]
    d = diff(a, b)

    expected = [
        (d, 0, d['D'][0], 0),
        (d['D'][0], None, None, 1),

        (d, 1, d['D'][1], 0),
        (d['D'][1], 0, d['D'][1]['D'][0], 1),
        (d['D'][1]['D'][0], None, None, 2),
        (d['D'][1], 1, d['D'][1]['D'][1], 1),
        (d['D'][1]['D'][1], None, None, 2),

        (d, 2, d['D'][2], 0),
        (d['D'][2], None, None, 1),
    ]

    got = list(Iterator().iterate(d))

    assert expected == got


def test_list_diff__noU():
    a = [0, [1], 3]
    b = [0, [1, 2], 3]
    d = diff(a, b, U=False)

    expected = [
        (d, 1, d['D'][0], 0),
        (d['D'][0], 1, d['D'][0]['D'][0], 1),
        (d['D'][0]['D'][0], None, None, 2),
    ]

    got = list(Iterator().iterate(d))

    assert expected == got


def test_set_diff():
    a = {0, 1}
    b = {0, 2}
    d = diff(a, b)

    expected = [
        ({'D': [{'U': 0}, {'R': 1}, {'A': 2}], 'E': set()}, None, None, 0),
    ]

    got = list(Iterator().iterate(d))

    assert expected == got


def test_custom_containers():
    class custom_container(tuple):
        pass

    d = {'D': custom_container([{'O': 0, 'N': 1}])}

    it = Iterator()
    it.set_iterator(custom_container, it.iterate_sequence_diff)

    expected = [
        (d, 0, d['D'][0], 0),
        (d['D'][0], None, None, 1),
    ]

    got = list(it.iterate(d))

    assert expected == got


def test_unknown_containers():
    class unknown_container(tuple):
        pass

    d = {'D': unknown_container([{'O': 0, 'N': 1}])}

    expected = [(d, None, None, 0)]  # final (not iterated)

    got = list(Iterator().iterate(d))

    assert expected == got
