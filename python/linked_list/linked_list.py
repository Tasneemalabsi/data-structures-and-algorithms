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

  def append(self, value):
    """
    a method that adds a new node at the end of the linked list

    arguments:
    value : any

    returns: None

    """

    # check if the linked list is empty or not
    if self.head is None:
      self.head=Node(value)

    current =self.head
    # if it's not empty, loop through the linked list until we reach the last node
    while current.next:
      current= current.next
    # creates the new node after the last node in the linked last
    current.next=Node(value)

  def insert_before(self,value,new_value):
    """
    a method that adds a new node before a given value in a specific node

    arguments:
    value : any value in the linked list
    new_value: any

    returns: None

    """
    # declare a variable that indicates if the value we want to insert before exists in the linked-list or not
    value_exists = False
    current = self.head
    # check if the linked list has only one node, so we are going to add the new node to the head of the linked list
    if current and current.data == value:
        new_node = Node(new_value, self.head)
        self.head = new_node
    # else loop through the linked list until we reach the given value
    else:
        while current.next:
            if current.next.data == value:
                value_exists =True
                break
            current=current.next
        # after finding the value, add the node before it, or to the next of the previous value .
        if value_exists:
            new_node=Node(new_value, current.next)
            current.next= new_node
        # if the input value doesn't exist in the linked list, raise an exception
        else:
            raise Exception('the value you entered does not exist in the linked list')

  def insert_after(self,value,new_value):
        """
        a method that adds a new node after a given value in a specific node

        arguments:
        value : any value in the linked list
        new_value: any

        returns: None

        """
        current=self.head
       # loop through the linked list until we find the input value
        while current:
            if current.data==value:
                break
            current=current.next
       # raise an exception if the value doesn't exist
        if current is None:
            raise Exception('node is not found')
       # add a new node after the given value, at the next to this specific value
        new_node = Node(new_value, current.next)
        current.next= new_node






