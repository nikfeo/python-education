"""
This module implements binary search tree
"""

from random import randint


class Node:
    """
    Describes class Node for Binary Tree
    """
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinaryTree:
    """
    Discribes class BinaryTree
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Inserts node into the tree with specified value
        """
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        """
        Help private recursive function for insert()
        """
        if value < cur_node.value:
            if not cur_node.left_child:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if not cur_node.right_child:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value is already exist")

    def height(self):
        """
        Allows to check out current height of tree
        """
        if self.root:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        """
        Help private recursive function for height()
        """
        if not cur_node:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def lookup(self, value):
        """
        Returns True if the value exist in the tree
        """
        if self.root:
            return self._lookup(value, self.root)
        else:
            return False, value

    def _lookup(self, value, cur_node):
        """
        Help private recursive function for lookup() function
        """
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child:
            return self._lookup(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child:
            return self._lookup(value, cur_node.right_child)
        return False, value

    def find(self, value):
        """
        Returns the node with specified value
        """
        if self.root:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        """
        Help private recursive function for find() function
        """
        if value == cur_node.value == self.root.value:
            if cur_node.right_child and cur_node.left_child:
                return f'sought node: {cur_node.value} is root, left child: {cur_node.left_child.value}, ' \
                       f'right child: {cur_node.right_child.value}'
            else:
                return f'sought node: {cur_node.value} is root and has no children'
        elif value == cur_node.value and not cur_node.left_child and not cur_node.right_child:
            return f'sought node: {cur_node.value}, parent: {cur_node.parent.value}, no children'
        elif value == cur_node.value and cur_node.left_child and not cur_node.right_child:
            return f'sought node: {cur_node.value}, parent: {cur_node.parent.value},' \
                   f' only left child: {cur_node.left_child.value}'
        elif value == cur_node.value and cur_node.right_child and not cur_node.left_child:
            return f'sought node: {cur_node.value}, parent: {cur_node.parent.value},' \
                   f' only right child: {cur_node.right_child.value}'
        elif value == cur_node.value and cur_node.right_child and cur_node.left_child:
            return f'sought node: {cur_node.value}, parent: {cur_node.parent.value},' \
                   f' left child: {cur_node.left_child.value}, right child: {cur_node.right_child.value}'
        elif value < cur_node.value and cur_node.left_child:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value):
        """
        Help function for deleting node
        Returns value argument in lookup() function to use it in delete_node()
        """
        return self.delete_node(self.lookup(value))

    def delete_node(self, node):
        """
        Deletes node. Includes some help functions
        Has 3 cases based on the structure of the tree and deleting node
        CASE 1: node has no children
        CASE 2: node has only one child
        CASE 3: node has two children
        """
        def min_value_node(n):
            """
            Returns the node with min value in tree, rooted at input node
            """
            current = n
            while current.left_child:
                current = current.left_child
            return current

        def num_children(n):
            """
            Returns number of children for specified node
            """
            num_children = 0
            if n.left_child:
                num_children += 1
            if n.right_child:
                num_children += 1
            return num_children
        # get the parent of the deleting node
        node_parent = node.parent
        # get the number of children of the deleting node
        node_children = num_children(node)
        if not node_children:
            # remove reference to the node from the parent
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None
        # CASE 2: node has only one child
        if node_children == 1:
            # get the single child node
            if node.left_child:
                child = node.left_child
            else:
                child = node.right_child
            # replace deleting node with its child
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child
            # correct the parent pointer in node
            child.parent = node_parent
        # CASE 3: node has two children
        if node_children == 2:
            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)
            # copy the value of inorder successor to the node formerly
            # holding the deleting value
            node.value = successor.value
            # than deleting copy value of successor
            self.delete_node(successor)

    def show_tree(self):
        """
        Prints all values of all nodes in the tree
        """
        if self.root:
            self._show_tree(self.root)
        else:
            print('The tree is empty!')

    def _show_tree(self, cur_node):
        """
        Help private recursive function for show_tree() function
        """
        if cur_node:
            print(f"  {str(cur_node.value)}")
            print_children = ''
            if cur_node.left_child:
                print_children += str(cur_node.left_child.value) + '/' + ' '
            if not cur_node.left_child:
                print_children += '_/ '
            if cur_node.right_child:
                print_children += '\\' + str(cur_node.right_child.value)
            if not cur_node.right_child:
                print_children += '\\_'
            print(f"{print_children}")
            self._show_tree(cur_node.left_child)
            self._show_tree(cur_node.right_child)


random_list = [7, 5, 152, 384, 450, 235, 399, 154, 316, 174, 244,
               498, 55, 245, 68, 81, 411, 95, 307, 363, 483, 453, 348, 191]


if __name__ == '__main__':
    test_tree = BinaryTree()
    for i in random_list:
        test_tree.insert(i)
    # print(f"Tree height is: {test_tree.height()}")
    # print(test_tree.lookup(30))
    # test_tree.delete_value(3)
    test_tree.show_tree()
    test_tree.delete_value(152)
    print(test_tree.lookup(152))
    test_tree.show_tree()
    print(test_tree.lookup(411))
