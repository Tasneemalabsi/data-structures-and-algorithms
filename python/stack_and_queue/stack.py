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




