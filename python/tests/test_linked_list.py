from linked_list.linked_list import LinkedList


def test_import():
    assert LinkedList

from linked_list.linked_list import Node,  LinkedList
import pytest

def test_node_has_int_data():
    # Arrange any data that you need to run your test
    expected = 1

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = node.data

    # Assert
    assert actual == expected


def test_node_has_str_data():
    # Arrange any data that you need to run your test
    expected = "a"

    # Act on the subject of the test to produce some actual output
    node = Node("a")
    actual = node.data

    # Assert
    assert actual == expected


def test_node_is_a_Node():
    # Arrange any data that you need to run your test
    expected = "Node"

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = type(node).__name__

    # Assert
    assert actual == expected

def test_node_without_value():
  with pytest.raises(TypeError):
    node = Node()


def test_new_linked_list_is_empty():
  expected = None

  ll = LinkedList()
  actual = ll.head

  assert actual == expected

def test_linked_list_insert():
  # Arrange
  expected = 1
  ll = LinkedList()
  # Act
  actual = ll.insert(1)
  #Assert
  actual == expected

def test_linked_list_includes_if_true():
  # Arrange
  expected = True
  ll = LinkedList()
  ll.insert("any")
  # Act
  actual = ll.includes("any")

  #Assert
  assert actual == expected

def test_linked_list_includes_if_false():
  # Arrange
  expected = False
  ll = LinkedList()
  ll.insert("any")
  # Act
  actual = ll.includes("not any")

  #Assert
  assert actual == expected

def test_to_string():
   #Arrange
    expected = "{ d } -> { c } -> { b } -> { a } -> NULL"

    ll = LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')

    ll.insert('d')

    #Act
    actual = ll.to_string()

    #Assert
    assert actual == expected

def test_append():
    #Arrange
    expected_value = 'd'
    #Act
    ll=LinkedList()
    ll.append('d')

    actual =ll.head
    # getting the last node
    while actual.next:

        actual= actual.next

    # Assert
    assert actual.data == expected_value

def test_insert_before():
    ll=LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert_before('a','c')
    expected="{ b } -> { c } -> { a } -> NULL"
    actual=ll.__str__()
    assert actual==expected











