from stack_and_queue.node import Node
from stack_and_queue.stack import Stack
import pytest

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
# test popping multiple values out of a stack

def test_pop_multiple_values(stack):
    #Arrange
    expected = Exception("This stack is empty")
    #Act
    stack = Stack()
    stack.pop()
    stack.pop()
    stack.pop()
    #Assert
    with pytest.raises(Exception):
        return stack.top.value




# def test_is_empty(stack):
#     assert stack.is_empty() == True

def test_peek(stack):
    actual=stack.peek()
    expected='cat'
    assert actual == expected

# decorator
@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push("cat")

    return stack
