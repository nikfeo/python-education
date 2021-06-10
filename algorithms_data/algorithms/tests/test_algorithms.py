"""
Module for testing algorithms: recusive factorial, binary search, quick search
"""

import pytest

from algorithms_data.algorithms.rec_factorial import factorial
from algorithms_data.algorithms.binary_search import binary_search


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
    :return:
    """
    test_values_list = [0, -3, -50]
    for i in test_values_list:
        with pytest.raises(ValueError):
            factorial(i)


# Tests for binary search algorithms
# =============================================================