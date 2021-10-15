class Node:
  """
  A class representing a Node

  Attributes
  ----------


  Methods
  -------
  __init__(data, next_):
      the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the next_

  """

  def __init__(self, data, next_ = None):
    self.data = data
    self.next = next_

class LinkedList:
  """
  A class for creating instances of a Linked List.

  Data and other attributes defined here:

  head: Node | None

  Methods defined here

  insert(value: any)
  contains(value: any) -> bool
  """

  def __init__(self):
    self.head = None

  def insert(self, value):
    """"
    Insert creates a Node with the value that was passed and adds
    it to the head of the linked list shifting all other values down

    arguments:
    value : any

    returns: None
    """
    # create new node
    self.head = Node(value, self.head)

  def includes(self, value):

      """"
    includes checks whether a certain value exists in a node or not

    arguments:
    value : any

    returns: boolean
    """

      current = self.head


      while current:
          if current.data == value:
              return True

          current = current.next

      return False
  def to_string(self):
    """
    to_string shows all the values in the linked list as a string with a specific pattern

    arguments:
    none

    returns: string
    """

    current = self.head

    the_stringified_result = ''

    while current:

      the_stringified_result += "{ " + str(current.data) +" } -> "
      current = current.next
    the_stringified_result=the_stringified_result+"NULL"
    return the_stringified_result
