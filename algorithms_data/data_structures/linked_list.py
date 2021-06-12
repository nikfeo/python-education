"""
This module describes linked list with head and tail (doubly linked)
"""


class Node:
    """
    Describes Node class with data and next_item info
    """
    def __init__(self, data=None):
        self.data = data
        self.next_data = None


class LinkedList:
    """
    Describes Linked List class
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        if not self.head:
            return 0
        list_length = 0
        current_data = self.head
        while current_data:
            current_data = current_data.next_data
            list_length += 1
        return list_length

    def __str__(self):
        current = self.head
        string = ''
        while current:
            string += str(current.data)
            string += ' --> '
            current = current.next_data
        string += 'None'
        return string

    def __iter__(self):
        item = self.head
        while item:
            yield item.data
            item = item.next_data

    def __getitem__(self, index):
        return self.get(index)

    def prepend(self, new_data):
        """
        Adds new node with new data to the beginning of list
        """
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_data = self.head
            self.head = new_node

    def append(self, new_data):
        """
        Adds new node with new data to the end of list
        """
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_data = new_node
            self.tail = new_node

    def display(self):
        """
        Displays each item of the list on new string
        """
        node_data = self.head
        while node_data:
            print(node_data.data)
            node_data = node_data.next_data

    def lookup(self, data):
        """
        Allows to get index by data
        """
        lookup_data = self.head
        data_index = 0
        while lookup_data:
            if lookup_data.data == data:
                return data_index
            if not lookup_data.next_data:
                # raise ValueError("Lookup data is not in the linked list")
                return False
            else:
                lookup_data = lookup_data.next_data
                data_index += 1
        return data_index

    def get(self, index):
        """
        Allows to get data by index
        """
        position = 0
        get_data = self.head
        if index > len(self):
            raise IndexError("Inddex out of range")
        if index == len(self):
            get_data = self.tail
            return get_data.data
        while position < index:
            get_data = get_data.next_data
            position += 1
        return get_data.data

    def insert(self, new_data, index):
        """
        Inserts data into the list, using index
        """
        if index == 0:
            self.prepend(new_data)
        elif index == len(self):
            self.append(new_data)
        elif index > len(self):
            raise IndexError("Index out of range")
        else:
            new_node = Node(new_data)
            position = 1
            inserted_data = self.head
            while position < index:
                inserted_data = inserted_data.next_data
                position += 1
            new_node.next_data = inserted_data.next_data
            inserted_data.next_data = new_node

    def delete(self, del_index):
        """
        Deletes item from list by index
        """
        if del_index >= len(self):
            raise IndexError("Index out of range")
        elif del_index == 0:
            self.head = self.head.next_data
        else:
            cur_node = self.head
            cur_index = 0
            while cur_index < del_index:
                prev_node = cur_node
                cur_node = cur_node.next_data
                cur_index += 1
                prev_node.next_data = cur_node
                if del_index == len(self) - 1:
                    self.tail = prev_node
            prev_node.next_data = cur_node.next_data
