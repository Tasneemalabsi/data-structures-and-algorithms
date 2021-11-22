from hashtables.tree_intersection.tree_intersection import tree_intersection,BinaryTree,Node
import pytest

def test_tree_intersection_one_tree_is_empty():
        tree1 = BinaryTree()
        a_node = Node("foldr")
        b_node = Node("folde")
        c_node = Node(1)
        d_node = Node("folde")
        e_node = Node("file.cs")
        f_node = Node("file.p")
        tree1.root=a_node
        a_node.left = b_node
        a_node.right = c_node
        b_node.left = d_node
        d_node.left = e_node
        c_node.right = f_node

        tree2 = BinaryTree()
        with pytest.raises(Exception):
            tree_intersection(tree1,tree2)

def test_tree_intersection_both_trees_are_empty():
        tree1 = BinaryTree()
        tree2 = BinaryTree()
        with pytest.raises(Exception):
            tree_intersection(tree1,tree2)

def test_tree_happy_path():
    tree1 = BinaryTree()
    a_node = Node(1)
    b_node = Node("anything")
    c_node = Node(3)
    d_node = Node("tasneem")
    e_node = Node(4)
    f_node = Node('file')
    tree1.root=a_node
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    d_node.left = e_node
    c_node.right = f_node

    tree2 = BinaryTree()
    a_node = Node(2)
    b_node = Node('any')
    c_node = Node(4)
    d_node = Node('three')
    e_node = Node("tasneem")
    f_node = Node('fil')
    tree2.root=a_node
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    d_node.left = e_node
    c_node.right = f_node

    expected = ['tasneem',4]
    actual = tree_intersection(tree1,tree2)
    assert actual == expected

def test_tree_intersection_no_common_values():
    tree1 = BinaryTree()
    a_node = Node(1)
    b_node = Node(2)
    c_node = Node(3)
    d_node = Node(4)
    e_node = Node(5)
    f_node = Node(6)
    tree1.root=a_node
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    d_node.left = e_node
    c_node.right = f_node

    tree2 = BinaryTree()
    a_node = Node(7)
    b_node = Node(8)
    c_node = Node(9)
    d_node = Node(10)
    e_node = Node("tasneem")
    f_node = Node('file')
    tree2.root=a_node
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    d_node.left = e_node
    c_node.right = f_node

    expected = []
    actual = tree_intersection(tree1,tree2)
    assert actual == expected







