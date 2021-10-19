from linked_list.linked_list import LinkedList, zipLists

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

#kth value test 1
def test_kth_value_greater_than_length():
    #Arrange
    expected=Exception('the index is out of range')
    #Act
    ll=LinkedList()
    ll.append('a')
    ll.append('b')
    ll.append('c')
    #Assert
    with pytest.raises(Exception):
        ll.kth_value(3)

#kth value test 2
def test_kth_value_equals_length():
    #Arrange
    expected= Exception('the index is out of range')

    #Act
    ll=LinkedList()
    ll.append('a')
    ll.append('a')
    #Assert
    with pytest.raises(Exception):
        ll.kth_value(2)

#kth value test 3
def test_kth_value_is_negative():
     #Arrange
    expected= Exception('the index is out of range')
    #Act
    ll=LinkedList()
    ll.append('a')
    ll.append('b')
    #Assert
    with pytest.raises(Exception):
        ll.kth_value(-1)
#kth value test 4
def test_linkedlist_length_is_one():
     #Arrange
    expected= ('a')
    #Act
    ll=LinkedList()
    ll.append('a')
    actual=ll.kth_value(0)
    #Assert
    assert actual==expected

#kth value test 5
def test_happy_path_k_in_middle():
     #Arrange
    excepted='b'
     #Act
    ll=LinkedList()
    ll.append('a')
    ll.append('b')
    ll.append('c')
    actual=ll.kth_value(1)
    #Assert
    assert excepted==actual

#test zip when two lists are the same size

def test_zip_list():
    #Arrange
    expected = "{ a } -> { d } -> { b } -> { e } -> { c } -> { f } -> NULL"

    list1 = LinkedList()
    list1.insert("a")
    list1.insert("b")
    list1.insert("c")
    list2 = LinkedList()
    list2.insert("d")
    list2.insert("e")
    list2.insert("f")


    #Act
    actual = zipLists(list1, list2)

    #Assert
    assert actual == expected

#test zip when one list has no values

def test_zip_list_one_with_no_values():
    #Arrange
    expected = "{ f } -> { e } -> { d } -> NULL"

    list1 = LinkedList()
    list2 = LinkedList()
    list2.insert("d")
    list2.insert("e")
    list2.insert("f")


    #Act
    actual = zipLists(list1, list2)

    #Assert
    assert actual == expected

# test zip when two lists are empty

def test_zip_list_two_lists_have_no_values():
    #Arrange
    expected = "NULL"

    list1 = LinkedList()
    list2 = LinkedList()

    #Act
    actual = zipLists(list1, list2)

    #Assert
    assert actual == expected















