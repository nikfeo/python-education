"""
Module for testing module hash_table.py
"""

import pytest

from algorithms_data.data_structures.hash_table import HashTable

checking_dict = {73: 'I', 438: 'love', 674: 'python', 327: 'for',
                 321: 'the', 411: 'lack', 213: 'of', 559: 'curly',
                 624: 'braces', 454: 'just', 444: 'four', 639: 'spaces'}


@pytest.fixture
def test_hash_table():
    test_hash_table = HashTable()
    test_list = ['I', 'love', 'python', 'for', 'the', 'lack', 'of', 'curly', 'braces',
                 'just', 'four', 'spaces']
    for i in test_list:
        test_hash_table.add_item(i)
    return test_hash_table


@pytest.mark.parametrize('testing, expected',
                         [('I', 73), ('just', 454), ('spaces', 639),
                          ('python', 674), ('braces', 624), ('four', 444)])
def test_hashing(test_hash_table, testing, expected):
    # test hash function
    assert test_hash_table.hashing(testing) == expected


def test_len_hash_table(test_hash_table):
    assert len(test_hash_table) == 12


def test_add_item(test_hash_table):
    test_hash_table.add_item('javascript')
    assert test_hash_table.hashing('javascript') == 1079
    assert test_hash_table[1079] == 'javascript'
    # tests for the added key in the list 'hash_table_keys"
    assert 1079 in test_hash_table.hash_table_keys


def test_lookup(test_hash_table):
    assert test_hash_table.lookup(411) == 'lack'
    assert test_hash_table[411] == 'lack'
    with pytest.raises(IndexError):
        test_hash_table.lookup(1765653)


def test_delete(test_hash_table):
    test_hash_table.delete(327)
    assert 327 not in test_hash_table.hash_table_keys
    with pytest.raises(IndexError):
        test_hash_table.lookup(327)
    assert test_hash_table.tail.key == 639
    test_hash_table.delete(639)
    assert test_hash_table.tail.data == 'four'
    assert test_hash_table.tail.key == 444
