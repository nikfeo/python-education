"""
Module for testing binary_tree.py
"""

import pytest

from algorithms_data.data_structures.binary_tree import BinaryTree

random_list = [7, 5, 152, 384, 450, 235, 399, 154, 316, 174, 244,
               498, 55, 245, 68, 81, 411, 95, 307, 363, 483, 453, 348, 191]


@pytest.fixture
def test_binary_tree():
    test_binary_tree = BinaryTree()
    for i in random_list:
        test_binary_tree.insert(i)
    return test_binary_tree


def test_lookup(test_binary_tree):
    assert test_binary_tree.lookup(411).value == 411
    assert test_binary_tree.lookup(666) == (False, 666)


def test_find(test_binary_tree):
    assert test_binary_tree.find(450) == 'sought node: 450, parent: 384, ' \
                                         'left child: 399, right child: 498'
    assert test_binary_tree.find(7) == 'sought node: 7 is root, left child: 5, right child: 152'
    assert test_binary_tree.find(399) == 'sought node: 399, parent: 450, only right child: 411'
    assert test_binary_tree.find(363) == 'sought node: 363, parent: 316, only left child: 348'


def test_insert(test_binary_tree):
    test_binary_tree.insert(999)
    assert test_binary_tree.lookup(999).value == 999
    assert test_binary_tree.find(999) == 'sought node: 999, parent: 498, no children'


def test_delete_value(test_binary_tree):
    assert test_binary_tree.find(7) == 'sought node: 7 is root, left child: 5, right child: 152'
    for i in random_list:
        if i > 7:
            test_binary_tree.delete_value(i)
    for i in random_list:
        if i > 7:
            assert test_binary_tree.lookup(i) == (False, i)
    assert test_binary_tree.find(7) == 'sought node: 7 is root and has no children'







