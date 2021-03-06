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
# append one node at the end
def test_append_one_nodes():
    #Arrange
    expected="{ b } -> { a } -> { c } -> NULL"
    #Act
    ll=LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.append('c') #append
    actual=ll.to_string()
    #Assert
    assert actual==expected

# append multiple nodes

def test_append_multiple_nodes():
    #Arrange
    expected="{ b } -> { a } -> { c } -> { d } -> { e } -> NULL"
    #Act
    ll=LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.append('c') #append
    ll.append('d') #append
    ll.append('e') #append
    actual=ll.to_string()
    #Assert
    assert actual==expected

# test inserting before a node located at the middle of the linked list
def test_insert_before_node_in_the_middle():
    #Arrange
    expected="{ c } -> { d } -> { b } -> { a } -> NULL"
    #Act
    ll=LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    ll.insert_before('b','d')
    actual=ll.to_string()
    #Assert
    assert actual==expected

# test inserting a node before the first node of a linked list

def test_insert_before_node_at_the_first():
    #Arrange
    expected="{ d } -> { c } -> { b } -> { a } -> NULL"
    #Act
    ll=LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    ll.insert_before('c','d')
    actual=ll.to_string()
    #Assert
    assert actual==expected
# test inserting a node after a node located at the middle of a linked list

def test_insert_after_node_in_the_middle():
    #Arrange
    expected="{ c } -> { b } -> { d } -> { a } -> NULL"
    #Act
    ll=LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    ll.insert_after('b','d')
    actual=ll.to_string()
    #Assert
    assert actual==expected

# test inserting a node after the last node of a linked list

def test_insert_after_at_the_end():
    #Arrange
    expected="{ c } -> { b } -> { a } -> { d } -> NULL"
    #Act
    ll=LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    ll.insert_after('a','d')
    actual=ll.to_string()
    #Assert
    assert actual==expected








