"""
This module implements hash table, that inherits from linked list
"""

from algorithms_data.data_structures.linked_list import LinkedList


class HashNode:
    """
    Describes HashNode class with data, key and next_data
    """
    def __init__(self, data):
        self.key = None
        self.data = data
        self.next_data = None


class HashTable(LinkedList):
    """
    Describes HashTable class that inherits from LinkedList
    """
    def __init__(self):
        super().__init__()
        self.hash_table_keys = LinkedList()

    @staticmethod
    def hashing(data):
        """
        Hashing function for making keys of Node's data
        :param data: value of node
        :return: hash value inreger
        """
        if isinstance(data, int):
            return data // 5
        else:
            return sum(ord(item) for item in data)

    def __getitem__(self, key):
        return self.lookup(key)

    def __str__(self):
        current = self.head
        string = ''
        while current:
            string += str(current.key)
            string += ': '
            string += str(current.data)
            string += ' || '
            current = current.next_data
        return string

    def lookup(self, key: int):
        """
        Gets data with key (like index in list)
        :param key: integer
        :return: value of node
        """
        curr_node = self.head
        position = 0
        if key not in self.hash_table_keys:
            raise IndexError(f"The key '{key}' does not exist")
            # return False
        while curr_node.next_data:
            if key == curr_node.key:
                return curr_node.data
            curr_node = curr_node.next_data
            position += 1
        return curr_node.data

    def add_item(self, value):
        """
        Adds data to hash table, using value
        Also adds key, that hashes with hashing function
        """
        new_node = HashNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.head.key = self.tail.key = self.hashing(value)
        else:
            self.tail.next_data = new_node
            new_node.key = self.hashing(value)
            self.tail = new_node
        self.hash_table_keys.append(new_node.key)

    def delete(self, key):
        """
        Deletes item from hash table by key
        """
        cur_node = self.head
        # position = 0
        if key not in self.hash_table_keys:
            # raise ValueError(f"The key '{key}' does not exist")
            return False
        elif cur_node.key == key:
            self.head = self.head.next_data
        else:
            while cur_node.key != key:
                prev_node = cur_node
                cur_node = cur_node.next_data
                # position += 1
                prev_node.next_data = cur_node
                if key == self.tail.key:
                    prev_node = HashNode(self.get(len(self.hash_table_keys) - 2))
                    prev_node.key = self.hashing(prev_node.data)
                    self.tail = prev_node
            prev_node.next_data = cur_node.next_data
        del_index = self.hash_table_keys.lookup(key)
        self.hash_table_keys.delete(del_index)
