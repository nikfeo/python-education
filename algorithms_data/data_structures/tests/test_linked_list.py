"""
Module for testing linked_list.py
"""

import pytest

from ..linked_list import LinkedList


@pytest.fixture
def empty_test_list():
    empty_test_list = LinkedList()
    return empty_test_list


@pytest.fixture
def test_list():
    test_list = LinkedList()
    test_string = 'qwertyuiopasdfghjklz'
    for i in test_string:
        test_list.append(i)
    return test_list


def test_len_list(test_list, empty_test_list):
    assert len(test_list) == 20
    assert len(empty_test_list) == 0


def test_prepend(test_list):
    # adds item to the head of the list
    test_list.prepend('im first')
    assert test_list.get(0) == 'im first'


def test_append(test_list):
    # adds item to the end of the list
    test_list.append('im last')
    assert test_list.get(len(test_list) - 1) == 'im last'


def test_lookup(test_list):
    # searches item by value and returns index
    assert test_list.lookup('r') == 3
    # returns False if value is not in the list
    assert not test_list.lookup('m')


def test_get(test_list):
    # searches item by index and returns its value
    assert test_list.get(10) == 'a'
    assert test_list.get(0) == 'q'
    assert test_list.get(len(test_list) - 1) == 'z'
    # returns 'IndexError' if index is out of range
    with pytest.raises(IndexError):
        test_list.get(100)


def test_insert(test_list):
    # inserts item with specified value and index
    test_list.insert('xxx', 10)
    assert test_list.get(10) == 'xxx'
    assert test_list.lookup('xxx') == 10
    assert test_list.tail.data == 'z'
    assert test_list.head.data == 'q'
    # returns 'IndexError' if index is out of range
    with pytest.raises(IndexError):
        test_list.insert('xxx', 100)


def test_delete(test_list):
    assert test_list.get(5) == 'y'
    assert test_list.get(6) == 'u'
    test_list.delete(5)
    assert test_list.get(5) == 'u'
    assert test_list.tail.data == 'z'
    # deletes tail of the list
    test_list.delete(len(test_list) - 1)
    assert test_list.tail.data == 'l'
    assert test_list.head.data == 'q'
    # deletes head of the list
    test_list.delete(0)
    assert test_list.head.data == 'w'
    # returns 'IndexError' if index is out of range
    with pytest.raises(IndexError):
        test_list.delete(50)


def test_iterable(test_list):
    # testing overloaded __iter__ magic method
    help_python_list = []
    for item in test_list:
        help_python_list.append(item)
    assert ''.join(help_python_list) == 'qwertyuiopasdfghjklz'
