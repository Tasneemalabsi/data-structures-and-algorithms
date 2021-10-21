from stack_and_queue.node import Node


class Stack:

    def __init__(self):
        self.top=None

    def push(self, value):
        node=Node(value)
        node.next=self.top
        self.top=node

    def pop(self):
        if self.top == None:
            raise Exception("This stack is empty")
        temp=self.top
        self.top=self.top.next
        temp.next=None

        return temp.value

    def peek(self):
        if not self.top:
            raise Exception("This stack is empty")
        return self.top.value


    def is_empty(self):
        return self.top == None




