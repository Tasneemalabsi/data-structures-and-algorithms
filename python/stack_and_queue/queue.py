from stack_and_queue.node import Node

class Queue:

    """
    A class for creating instances of a Nodes.

    Data and other attributes defined here:

    front: Node | None
    rear: Node | None

    """

    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self, value):
        """"
        enqueue creates a Node with the value that was passed and adds
        it to the rear of the queue shift al the nodes

        arguments:
        value : any

        returns: None
        """
        node=Node(value)
        if not self.rear:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node

    def dequeue(self):
        """"
        dequeue removes a Node with the value at the front and shifts all the nodes


        returns: the value in the removed node
        """
        if not self.front:
            raise Exception("This queue is empty")
        current=self.front
        self.front=self.front.next
        current.next=None

        return current.value

    def peek(self):
        """"
        peek returns the value in the node located at the front


        returns: value
        """
        if not self.front:
            raise Exception("This queue is empty")
        return self.front.value


    def is_empty(self):
        """"
        is_empty checks if the queue is empty or not


        returns: boolean
        """
        return not self.front




