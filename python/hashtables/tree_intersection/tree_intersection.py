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



class BinaryTree:
  """
    class for the implementation of the binary tree
    attributes:
    root: the root of the binary tree
  """

  def _init_(self):
    self.root = None


class ListNode:
    def __init__(self, value=None, next_=None):
        """
      Initalization the Node
      """
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        """
        The constructor method for the linked list. Initializes the head of a linked list to None.
        """
        self.head = None

    def insert(self, value):
        """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """
        self.head = ListNode(value, self.head)


class HashTable:
    def __init__(self, size=1024):
        """
        Initalization of Hash table

        """
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value pari in a Node at that index.
        """
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        """
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.

        Arg: Takes the key and value
        Return : No return value
        """

        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()
        my_value = [key,value]
        self.__buckets[index].insert(my_value)

    def get(self, key):
      """
      Retrieve the most recent value of in our hashmap for the given key

      Arguments: key str
      Returns: value any
      """
      index = self.__hash(key)
      if self.__buckets[index]:
        linked_list = self.__buckets[index]
        current = linked_list.head
        while current:
          if current.value[0] == key:
            return current.value[1]
          current = current.next
      return None

    def contains(self, key):
        """
        method checks if a certain key exists in the table or not
        Arguments: key
        Return: boolean
        """
        index = self.__hash(key)
        if self.__buckets[index]:
            linked_list = self.__buckets[index]
            current = linked_list.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        return False


def tree_intersection(tree1:BinaryTree, tree2:BinaryTree):
    if (not tree1.root) or (not tree2.root):
        raise Exception('input tree is empty')
    arr=[]
    hash = HashTable()
    def walk(node:Node):
        try:
            if node:
                hash.add(str(node.data),None)
            if node.left:
                walk(node.left)
            if node.right:
                walk(node.right)
        except:
            raise Exception('tree is empty')

    walk(tree1.root)

    def walk2(node:Node):
        try:
            if node:
                if hash.contains(str(node.data)):
                    arr.append(node.data)
            if node.left:
                walk2(node.left)
            if node.right:
                walk2(node.right)
            return arr
        except:
            raise Exception('tree is empty')
    return walk2(tree2.root)



if __name__ == "__main__":
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
    a_node = Node("folder")
    b_node = Node('any')
    c_node = Node(11)
    d_node = Node('three')
    e_node = Node("any")
    f_node = Node("file.py")
    tree2.root=a_node
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    d_node.left = e_node
    c_node.right = f_node
    print(tree_intersection(tree1, tree2))
