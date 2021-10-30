from stack_and_queue.node import Node
from stack_and_queue.stack import Stack, PseudoQueue
import pytest

def test_import():
    assert Stack

#test pushing one value into a stack
def test_push_one_value(stack):
    #Arrange
    expected = "cat"
    #Act
    actual = stack.top.value
    #Assert
    assert actual == expected
#test pushing multiple values into a stack
def test_push_multiple_values():
    #Arrange
    expected = ["cat",2,1]
    #Act
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push("cat")
    arr=[]
    while stack.top:
        arr.append(stack.top.value)
        stack.top=stack.top.next
    actual = arr

    #Assert
    assert actual == expected

# test popping one value out of a stack
def test_pop(stack):

    actual = stack.pop()
    expected = "cat"
    assert actual == expected

# test empty stack after popping multiple values out of it
def test_pop_multiple_values():
    #Arrange
    expected = True
    #Act
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push("cat")
    stack.pop()
    stack.pop()
    stack.pop()
    actual=stack.is_empty()
    #Assert
    actual == expected

# test the peek of a stack (top value)
def test_peek(stack):
    #Arrange
    expected='cat'
    #Act
    actual=stack.peek()
    #Assert
    assert actual == expected

# instantiate an empty stack
def test_is_empty():
    #Arrange
    expected = True
    #Act
    stack = Stack()
    actual = stack.is_empty()
    assert actual == expected

#test peek of an empty stack raises an exception
def test_peek_an_empty_stack_raises_exception():
    #Arrange
    expected=Exception
    #Act
    stack=Stack()
    #Assert
    with pytest.raises(Exception):
        stack.peek()

#test pop out of an empty stack raises an exception
def test_pop_outof_empty_stack_raises_exception():
    #Arrange
    expected=Exception
    #Act
    stack=Stack()
    #Assert
    with pytest.raises(Exception):
        stack.pop()

# decorator
@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push("cat")

    return stack

#-------------------------------pseudoqueue tests ------------------------------------

# test adding values to the pseudoqueue
def test_enqueue_in_pseudoqueue():

    queue=PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1

# test removing values from the pseudoqueue

def test_dequeue_in_pseudoqueue():

    queue=PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.dequeue() == 1

# test removing values from an empty queue raises an exception
def test_dequeue_from_empty_in_pseudoqueue():

    queue=PseudoQueue()

    with pytest.raises(Exception):
        queue.dequeue()
