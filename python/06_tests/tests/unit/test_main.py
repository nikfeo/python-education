import pytest

from software_testing.main import *


@pytest.mark.parametrize('test_arg,expected',
                         [(1, 'odd'),
                          (10, 'even'),
                          (-4, 'even'),
                          (1.0, 'odd')])
def test_even_odd(test_arg, expected):
    assert even_odd(test_arg) == expected


def test_even_odd_none_arg():
    test_arg = None

    with pytest.raises(TypeError):
        even_odd(test_arg)


@pytest.mark.parametrize('test_arg,expected',
                         [((1, 2, 3), 6),
                          ((1.3, 4.9, 13.8), 20.0)])
def test_sum_all(test_arg, expected):
    assert sum_all(*test_arg) == expected


def test_sum_all_none_arg():
    test_arg = None

    with pytest.raises(TypeError):
        sum_all(test_arg)
