class Node_kAry:
    """
    class for the k_ary tree node
    attributes:
    value: the value in the node
    children: list of the root's children nodes

    methods:
    add_child(): to add a child node to the children of the root's node
    """
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self,child):
        self.children.append(child)

class kary_tree:
    """
    class for the implementation of the k ary tree
    attributes:
    root: the root of the k ary tree
    """
    def __init__(self, root=None):
        self.root = root

    def preorder(self, node, arr= None):
        """
        A k ary tree method which returns a list of items that it contains

        input: node|Node

        output: tree items

        sub method : walk () to make the recursion staff
        """
        if not node:
            return arr
        if arr == None:
             arr = []
        arr.append(node.value)
        for child in node.children:
            self.preorder(child, arr)
        return arr



def tree_fizz_buzz(ktree: kary_tree):
    """
    this function takes a k ary tree as an input and replaces the node value with 'fizz' if the node's value is divisible by 3, 'buzz' if it's divisible by 5, and fizzbuzz if it's divisible by both, if none it replaces it with the number as a string
    Arguments:
    ktree: k-ary tree tree
    returns: k-ary tree (list of values)
    """
    if not ktree.root:
      raise Exception("tree is empty")

    else:

      def walk(root: Node_kAry):

        if root:
          if root.value % 3 == 0 and root.value % 5 == 0:
              node = Node_kAry("FizzBuzz")
          if root.value % 3 == 0 and root.value % 5 :
              node = Node_kAry("Fizz")
          elif root.value % 5 == 0 and root.value % 3:
              node = Node_kAry("Buzz")
          elif root.value % 5 and root.value % 3:
              node = Node_kAry(str(root.value))
          if root.children:
            for child in root.children:
                child1 = walk(child)
                node.children.append(child1)

        return node
      tree = kary_tree()
      tree.root = walk(ktree.root)
      return tree.preorder(tree.root)




if __name__ == "__main__":
    node=Node_kAry(1)
    node.add_child(Node_kAry(15))
    node.add_child(Node_kAry(3))
    node.add_child(Node_kAry(4))
    node.add_child(Node_kAry(5))
    tree = kary_tree()
    tree.root = node
    print(tree.preorder(tree.root))
    print(tree_fizz_buzz(tree))









