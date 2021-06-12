"""
Module for testing queue.py and stack.py
"""

import pytest

from algorithms_data.data_structures.queue import Queue
from algorithms_data.data_structures.stack import Stack


# Tests for Queue class in module queue.py
# =====================================================
@pytest.fixture
def test_queue():
    test_queue = Queue()
    test_string = 'zlkjhgfdsa'
    for i in test_string:
        test_queue.enqueue(i)
    return test_queue


@pytest.fixture
def empty_test_queue():
    empty_test_queue = Queue()
    return empty_test_queue


def test_len_queue(test_queue, empty_test_queue):
    assert len(test_queue) == 10
    assert len(empty_test_queue) == 0


def test_enqueue(test_queue, empty_test_queue):
    assert test_queue.head.data == 'a'
    assert test_queue.tail.data == 'z'
    # add the item to the head of queue
    test_queue.enqueue('head of the queue, but last to dequeue')
    assert test_queue.head.data == 'head of the queue, but last to dequeue'
    assert test_queue.tail.data == 'z'
    # add the item to the empty queue and test head and tail are equal
    empty_test_queue.enqueue('first and the one item')
    assert empty_test_queue.head.data == 'first and the one item'
    assert empty_test_queue.tail.data == 'first and the one item'


def test_dequeue(test_queue, empty_test_queue):
    assert test_queue.tail.data == 'z'
    # delete last item (tail) of the queue
    test_queue.dequeue()
    assert test_queue.tail.data == 'l'
    assert not empty_test_queue.dequeue()


def test_peek_queue(test_queue, empty_test_queue):
    assert test_queue.peek() == 'z'
    assert not empty_test_queue.peek()


# Tests for Stack class in module stack.py
# =====================================================
@pytest.fixture
def empty_test_stack():
    empty_test_stack = Stack()
    return empty_test_stack


@pytest.fixture
def test_stack():
    test_stack = Stack()
    test_string = 'zlkjhgfdsa'
    for i in test_string:
        test_stack.push(i)
    return test_stack


def test_len_stack(test_stack, empty_test_stack):
    assert len(test_stack) == 10
    assert len(empty_test_stack) == 0


def test_push(test_stack, empty_test_stack):
    assert test_stack.head.data == 'a'
    # add item to the head of the stack
    test_stack.push('top of the stack')
    assert test_stack.head.data == 'top of the stack'
    assert not empty_test_stack.head
    assert not empty_test_stack.tail
    # add the item to the empty stack and test head and tail are equal
    empty_test_stack.push('top of the stack')
    assert empty_test_stack.head.data == 'top of the stack'
    assert empty_test_stack.tail.data == 'top of the stack'


def test_pop(test_stack, empty_test_stack):
    assert test_stack.head.data == 'a'
    # deletes first item (head) of the stack
    test_stack.pop()
    assert test_stack.head.data == 's'
    with pytest.raises(ValueError):
        empty_test_stack.pop()


def test_peek_stack(test_stack, empty_test_stack):
    assert test_stack.peek() == 'a'
    assert not empty_test_stack.peek()
