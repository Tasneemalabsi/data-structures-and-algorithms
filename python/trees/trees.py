"""
This Module defines a Node and a Binary Tree
"""

class Node:
  """
    class for the tree node
    attributes:
    data: the value in the node
    left: left to the root node
    right: right to the root node
  """
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
  """
    class for the implementation of the binary tree
    attributes:
    root: the root of the binary tree
  """

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

  def get_max(self):
    arr = self.bfs()
    max=0
    for i in arr:
        if i>max:
            max = i

    return max




class BinarySearchTree(BinaryTree):
    """
    sub-class from the binary tree class
    methods:
    add: adds a node to the tree
    contains: check if the tree contains a certain value
    """
    def __init__(self):
        super()._init_()

    def add(self, data):
        """
        adds a node to the tree
        Arguments:
        data: the data in the added node
        returns: none
        """
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

    def contains(self, value):
       """
       check if the tree contains a certain value
       Arguments:
       value: the value that is going to be checked
       returns: boolean
       """
       if not self.root:
           raise Exception("no values to be found in the tree")

       else:
            current = self.root
            while current:
                if current.data == value:
                    return True
                elif current.data > value:
                     current = current.left
                elif current.data < value:
                    current = current.right
            return False

# def fizz_buzz_tree(ktree: BinaryTree):
#     arr=ktree.bfs()
#     newArr = []
#     for i in arr:
#         if i % 3 == 0 and i % 5 == 0:
#             newArr.append("FizzBuzz")
#         if i % 3 == 0 and i % 5 :
#             newArr.append("Fizz")
#         elif i % 5 == 0 and i % 3:
#             newArr.append("Buzz")
#         elif i % 5 and i % 3:
#             newArr.append(str(i))

#     new_tree = BinarySearchTree()
#     for i in newArr:
#         new_tree.add(i)
#     print(new_tree.root.data)
#     print(new_tree.root.left.data)
#     print(new_tree.root.right.data)
#     return new_tree




if __name__ == "__main__":
    tree = BinaryTree()
    a_node = Node(7)
    b_node = Node(5)
    c_node = Node(9)
    d_node = Node(13)
    e_node = Node(13)
    f_node = Node(15)
    tree.root=a_node
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    d_node.left = e_node
    c_node.right = f_node
    # print(tree.get_max())
    print(fizz_buzz_tree(tree))
