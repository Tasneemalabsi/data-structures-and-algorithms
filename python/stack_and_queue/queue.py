from stack_and_queue.node import Node

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self, value):
        node=Node(value)
        if not self.rear:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node

    def dequeue(self):
        if not self.front:
            raise Exception("This queue is empty")
        current=self.front
        self.front=self.front.next
        current.next=None

        return current.value

    def peek(self):
        if not self.front:
            raise Exception("This queue is empty")
        return self.front.value


    def is_empty(self):
        return not self.front
