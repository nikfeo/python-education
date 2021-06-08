"""
This module describes queue data structure
"""

from algorithms_data.data_structures.linked_list import Node, LinkedList


class Queue(LinkedList):
    """
    Describes class Queue
    """
    def __init__(self):
        super().__init__()

    def enqueue(self, data):
        """
        Adds node to the end of the queue
        """
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.prepend(node.data)

    def dequeue(self):
        """
        Deletes node from the end of list
        """
        if not self.head:
            print("The queue is empty")
            return False
        else:
            self.delete(len(self) - 1)

    def peek(self):
        """
        Shows the tail of the queue
        """
        if not self.head:
            print("The queue is empty")
            return False
        else:
            return self.tail.data


if __name__ == '__main__':
    qq = Queue()
    qq.enqueue(5)
    qq.enqueue(12)
    qq.enqueue(1432)
    print(f"length of queue is: {len(qq)}")
    print(f"Head of the queue is: {qq.head.data}")
    print(f"Tail of the queue is: {qq.tail.data}")
    print(qq)
    print(f"Last item in queue is: {qq.peek()}")
    print('-----------------------')
    print(f"Deleting last item in queue: {qq.dequeue()}")
    print(f"length of queue is: {len(qq)}")
    print(f"Head of the queue is: {qq.head.data}")
    print(f"Tail of the queue is: {qq.tail.data}")
    print(qq)
    print(f"New last item in queue is: {qq.peek()}")
