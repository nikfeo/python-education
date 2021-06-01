"""
This module describes singly linked list
"""


class LinkedList:
    """
    Describes singly linked list
    """
    head = None
    tail = None

    class Node:
        """
        Describes Node class with data and next_item info
        """
        data = None
        next_item = None

        def __init__(self, item, next_item=None):
            self.item = item
            self.next_item = next_item

    def __len__(self):
        """
        Calculates length of the list and returns integer
        """
        if not self.head:
            return 0
        length = 1
        node = self.head
        while node.next_item:
            length += 1
            node = node.next_item
        return length

    def append(self, data):
        """
        Adds new node with data to the end of list
        """
        node = self.Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next_item = node
            self.tail = node

    def prepend(self, data):
        """
        Adds new node with data to the beginning of list
        """
        node = self.Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.next_item = node
            self.head = node

    def display(self):
        """
        Displays each item of the list on new string
        """
        node = self.head
        while node.next_item:
            print(node.item)
            node = node.next_item
        print(node.item)

    def insert(self, item, index):
        """
        Inserts item in list, using index
        """
        position = 0
        node = self.head
        previous_node = self.head
        while position < index:
            previous_node = node
            node = node.next_item
            position += 1
        previous_node.next_item = self.Node(item, next_item=node)
        return item

    def get(self, index):
        """
        Allows to get item by index
        """
        position = 0
        node = self.head
        if index == len(self) - 1:
            node = self.tail
            return node.item
        while position < index:
            node = node.next_item
            position += 1
        return node.item

    def delete(self, index):
        """
        Deletes item from list by index
        """
        if index == 0:
            self.head = self.head.next_item
        node = self.head
        position = 0
        prev_node = node
        while position < index:
            prev_node = node
            node = node.next_item
            position += 1
        prev_node.next_item = node.next_item
        item = node.item
        del node
        return item


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1213)
    ll.append(78967)
    ll.append('dsadas')
    ll.insert(42343245236543, 2)
    print(ll.get(2), '\n')

    ll.display()
    print(len(ll), '\n')

    ll.delete(0)
    ll.display()

    print('\n', ll.get(0))
    print(ll.get(1))
    print(ll.get(2))
