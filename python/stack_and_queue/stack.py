from stack_and_queue.node import Node


class Stack:

    """
    A class for creating instances of a Stack.

    Data and other attributes defined here:

    top: Node | None

    """

    def __init__(self):
        self.top=None

    def push(self, value):
        """"
        push creates a Node with the value that was passed and adds
        it to the top of the stack shifting all other values down

        arguments:
        value : any

        returns: None
        """
        node=Node(value)
        node.next=self.top
        self.top=node

    def pop(self):

        """"
        pop removes a Node with the value at the top and shifts all the nodes up


        returns: the value in the removed node
        """
        if self.top == None:
            raise Exception("This stack is empty")
        else:

            temp=self.top
            self.top=self.top.next
            temp.next=None

            return temp.value

    def peek(self):

        """"
        peek returns the value in the node located at the top of a stack


        returns: value
        """
        if not self.top:
            raise Exception("This stack is empty")
        return self.top.value


    def is_empty(self):
        """"
        is_empty checks if the stack is empty or not


        returns: boolean
        """
        return self.top == None


class PseudoQueue:
    """
    A class for creating instances of a psudoqueue, a queue created using two stack instances.

    Data and other attributes defined here:

    self.stack_front: instance of a stack
    self.stack_rear: stack instance

    """
    def __init__(self):
        self.stack_front =Stack()
        self.stack_rear =Stack()

    def enqueue(self, value):
        """"
        enqueue creates a Node with the value that was passed and adds
        it to the rear of the queue shift al the nodes

        arguments:
        value : any

        returns: None
        """
        self.stack_front.push(value)

    def dequeue(self):
        """"
        dequeue removes a Node with the value at the front and shifts all the nodes


        returns: the value in the removed node
        """
        if not self.stack_front.top:
            raise Exception('the queue is empty')
        while self.stack_front.top:
            self.stack_rear.push(self.stack_front.pop())
        removed_value = self.stack_rear.pop()
        while self.stack_rear.top:
            self.stack_front.push(self.stack_rear.pop())

        return removed_value

    def peek(self):
        """"
        peek returns the value in the node located at the front


        returns: value
        """
        # this method is used for testing the enqueue method, it's not required in the challenge
        while self.stack_front.top:
            self.stack_rear.push(self.stack_front.pop())

        peek_value = self.stack_rear.top.value
        while self.stack_rear.top:
            self.stack_front.push(self.stack_rear.pop())

        return peek_value


