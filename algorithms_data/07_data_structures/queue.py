"""
This module describes queue data structure
"""

from linked_list import Node, LinkedList


class Queue(LinkedList):
    """
    Describes class Queue
    """
    def __init__(self):
        super().__init__()

    def __len__(self):
        if not self.head:
            return 0
        queue_length = 0
        current_data = self.head
        while current_data:
            current_data = current_data.next_data
            queue_length += 1
        return queue_length

    def enqueue(self, data):
        """
         Adds node to the end of the queue
         """
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next_data = node
            self.tail = node

    def dequeue(self):
        """
        Deletes node from the end of list
        """
        if not self.head:
            print("The queue is empty")
        else:
            self.delete(len(self) - 1)

    def peek(self):
        """
        Shows the tail of the queue
        """
        if not self.head:
            print("The queue is empty")
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
    qq.display()
    qq.peek()
    print(f"Last item in queue is: {qq.peek()}")
    print('-----------------------')
    print(f"Deleting last item in queue: {qq.dequeue()}")
    print(f"length of queue is: {len(qq)}")
    print(f"Head of the queue is: {qq.head.data}")
    print(f"Tail of the queue is: {qq.tail.data}")
    qq.display()
    print(f"New last item in queue is: {qq.peek()}")
