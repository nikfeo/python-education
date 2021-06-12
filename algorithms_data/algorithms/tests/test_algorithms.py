"""
Module for testing algorithms: recusive factorial, binary search, quick search
"""

import pytest
from random import randint

from algorithms_data.algorithms.rec_factorial import factorial
from algorithms_data.algorithms.binary_search import binary_search
from algorithms_data.algorithms.quick_sort import quick_sort_rec, quick_sort_iter


# Tests for recursive factorial
# =============================================================
@pytest.mark.parametrize('test_value, expected', [(3, 6), (5, 120),
                                                  (18, 6402373705728000)])
def test_factorial(test_value, expected):
    assert factorial(test_value) == expected


def test_not_integer():
    """
    Testing for raising TypeError with not integer argument
    """
    test_values_str = '12.6m*H-=./z!_&? '
    for i in test_values_str:
        with pytest.raises(TypeError):
            factorial(i)


def test_negative_value():
    """
    Testing for raising ValueError with negative integer of '0' argument
    """
    test_values_list = [0, -3, -50]
    for i in test_values_list:
        with pytest.raises(ValueError):
            factorial(i)


# Tests for quick sort algorithm
# =============================================================

@pytest.fixture
def test_list_1():
    test_list_1 = [3, 6, 8, 3, 0, 2, 3, 5, 8, 10, 11, 1, 19]
    return test_list_1


def test_quick_sort_recursive(test_list_1):
    test_list_2 = []
    for i in range(100):
        value = randint(0, 500)
        test_list_2.append(value)
    assert quick_sort_rec(test_list_1) == sorted(test_list_1)
    assert quick_sort_rec(test_list_2) == sorted(test_list_2)


def test_quick_sort_iterable(test_list_1):
    test_list_2 = []
    for i in range(100):
        value = randint(0, 500)
        test_list_2.append(value)
    assert quick_sort_iter(test_list_1) == sorted(test_list_1)
    assert quick_sort_iter(test_list_2) == sorted(test_list_2)


# Tests for binary search algorithm
# =============================================================

@pytest.fixture
def test_list_3():
    test_list_3 = [312, 232, 679, 0, 858, 3, 640, 519, 248, 860, 853,
                   229, 491, 135, 14, 55, -34, 21, 684, 853, 752, 978]
    return quick_sort_rec(test_list_3)


def test_binary_search(test_list_3):
    assert binary_search(14, test_list_3) == 14
    assert binary_search(-34, test_list_3) == -34
    assert binary_search(0, test_list_3) == 0
