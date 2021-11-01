from trees.trees import Node, BinaryTree, BinarySearchTree, breadth_first
import pytest

# Can successfully instantiate an empty tree
def test_instantiate_empty_tree():
  # Arrange
  # Create tree instance
  tree = BinarySearchTree()
  #Act
  actual = tree.root
  #Assert
  assert actual == None

# Can successfully instantiate a tree with a single root node
def test_add_root_to_tree():
  # Arrange
  # Create tree instance
  expected = 'a'
  tree = BinarySearchTree()
  #Act
  tree.add('a')
  actual = tree.root.data
  #Assert
  assert actual == expected

# Can successfully add a left child and right child to a single root node
def test_add_left_and_right_node():
    #Arrange
    tree = BinarySearchTree()
    tree.add(2)
    tree.add(1)
    tree.add(3)
    #Act
    actual1 = tree.root.left.data
    actual2 = tree.root.right.data

    #Assert
    assert actual1 == 1
    assert actual2 == 3


def test_bfs_2():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for A,B,C,D
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["1", "2", "3", "4"]
  # set actual to return value of bfs call
  actual = tree.bfs()
  # assert actual is same as expected
  assert actual == expected
  print("test_bfs_2 passed")


#Can successfully return a collection from a preorder traversal
def test_pre_order():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for 1,2,3,4
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["1", "2", "4", "3"]
  # set actual to return value of pre_order call
  actual = tree.pre_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_pre_order_ passed")

#Can successfully return a collection from a postorder traversal
def test_post_order():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for 1,2,3,4
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["4", "2", "3", "1"]
  # set actual to return value of post_order call
  actual = tree.post_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_post_order_ passed")

#Can successfully return a collection from an in-order traversal
def test_in_order():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for 1,2,3,4
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["4", "2", "1", "3"]
  # set actual to return value of in_order call
  actual = tree.in_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_in_order_ passed")


def test_bfs():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for A,B,C,D
  a_node = Node('A')
  b_node = Node('B')
  c_node = Node('C')
  d_node = Node('D')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["A", "B", "C", "D"]
  # set actual to return value of bfs call
  actual = tree.bfs()
  # assert actual is same as expected
  assert actual == expected
  print("test_bfs passed")



def test_contains():
    tree = BinarySearchTree()
    tree.add(2)
    tree.add(4)
    tree.add(1)
    assert tree.contains(2) == True
    assert tree.contains(4) == True
    assert tree.contains(1) == True
    assert tree.contains(0) == False

def test_contains_empty_tree_raises_exception():
    tree = BinarySearchTree()
    with pytest.raises(Exception):
        tree.contains(2)

#------------------------------tests for tree max challenge-----------------------------

#test tree max/ happy path
def test_tree_max():
    # Arrange
    expected = 17
    tree = BinaryTree()
    a_node = Node(7)
    b_node = Node(5)
    c_node = Node(9)
    d_node = Node(17)
    e_node = Node(13)
    f_node = Node(15)
    tree.root=a_node
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    d_node.left = e_node
    c_node.right = f_node
    #Act
    actual = tree.get_max()
    #Assert
    assert actual == expected

# test tree max/ edge case
def test_empty_tree_max_raises_exception():
    tree = BinaryTree()
    with pytest.raises(Exception):
        tree.get_max()

#--------------------------tests for breadth first/code challenge 17-------------------

# test tree breadth first/ happy path
def test_breadth_first_function():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for A,B,C,D
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["1", "2", "3", "4"]
  # set actual to return value of bfs call
  actual = breadth_first(tree)
  # assert actual is same as expected
  assert actual == expected

  

# test tree breadth first/ edge case
def test_empty_tree_breadth_first_raises_exception():
    tree = BinaryTree()
    with pytest.raises(Exception):
        breadth_first(tree)






