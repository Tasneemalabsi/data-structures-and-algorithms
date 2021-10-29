"""
This Module defines a Node and a Binary Tree
"""

class Node:
  def __init__ (self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)

class BinaryTree:

  def _init_(self):
    self.root = None

  def bfs(self):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items
    """
    # Queue breadth <-- new Queue()
    breadth = Queue()
    # breadth.enqueue(root)
    breadth.enqueue(self.root)

    list_of_items = []

    while breadth.peek():
      front = breadth.dequeue()
      list_of_items += [front.data]

      if front.left:
        breadth.enqueue(front.left)

      if front.right:
        breadth.enqueue(front.right)

    return list_of_items

  def pre_order(self):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items

    sub method : walk () to make the recursion staff
    """
    list_of_items = []
    def walk(node):
      if node:
        list_of_items.append(node.data)
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def in_order(self):
    """
    function to in order the list using Trees
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        list_of_items.append(node.data)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def post_order(self):
    """
    A binary tree method which returns a list of items in post order

    input: None

    output: tree items
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)
        list_of_items.append(node.data)

    walk(self.root)
    return list_of_items

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super()._init_()

    def add(self, data):
        node=Node(data)
        if not self.root:
            self.root=node

        else:
            current = self.root
            while current:
                if self.root.data > data:
                    if not current.left:
                        current.left=node
                    else:
                        current = current.left
                        break

                elif self.root.data < data:
                    if not current.right:
                        current.right = node
                    else:
                        current=current.right
                        break

    def contains(self,value):
    
        if self.root.data == value:
          return True
        elif self.root.data < value:
          if self.root.right == None:
               return False
          else:
               return BinarySearchTree.contains(self.root.right,value)
        #root.right.value == value #I am using == to return True or
                                     #False
        else:
          if self.root.left == None:
              return False
          else:
              return BinarySearchTree.contains(self.root.left,value)



if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.add(3)
    tree.add(2)
    tree.add(5)
    print(tree.root.data)
    # print(tree.root.left.data)
    # print(tree.root.right.data)
