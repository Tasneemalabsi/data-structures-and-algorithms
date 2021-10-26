from stack_and_queue.stack import Node
from stack_and_queue.stack_queue_brackets.stack_queue_brackets import validate_brackets
import pytest


#test balanced input string returns true
def test_balanced_string_returns_true():
    #Arrange
    expected = True
    #Act
    str = "()[[Extra Characters]]"
    actual = validate_brackets(str)
    #Assert
    assert actual == expected

#test unbalanced input string returns false
def test_unbalanced_string_returns_false():
    #Arrange
    expected = False
    #Act
    str = "[({}]"
    actual = validate_brackets(str)
    #Assert
    assert actual == expected

#test one character string returns false
def test_one_bracket_string_returns_false():
    #Arrange
    expected = False
    #Act
    str = "["
    actual = validate_brackets(str)
    #Assert
    assert actual == expected

#test input empty string raises exception
def test_empty_string_raises_exception():
    with pytest.raises(Exception):
        validate_brackets("")
