"""
This module describes stack data structure
"""

from algorithms_data.data_structures.linked_list import Node, LinkedList


class Stack(LinkedList):
    """
    Describes class Stack
    """
    def __init__(self):
        super().__init__()

    def push(self, data):
        """
        Adds node to the end (head) of stack
        """
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next_data = self.head
            self.head = node

    def pop(self):
        """
        Removes node from stack
        """
        if not self.head:
            # print("Stack is empty")
            raise ValueError("Stack is empty")
        else:
            self.delete(0)

    def peek(self):
        """
        Shows the tail of the queue
        """
        if not self.head:
            print("The stack is empty")
            return False
        else:
            return self.head.data


if __name__ == '__main__':
    st = Stack()
    st.push(3)
    st.push(12)
    st.push('fdasaase')
    st.push(864.1)
    print(st)
    print(f"Last item in stack is: {st.peek()}")
    print(f"length of stack is: {len(st)}")
    print('-----------------------')
    print(f"Deleting last item in queue: {st.head.data}")
    st.pop()
    print(f"New stack: {st}")
    print(f"length of new stack is: {len(st)}")
