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
    # create a new node
    new_node = Node(value)
    # check if the linked list is empty or not
    if self.head is None:
      self.head=Node(value)

    current =self.head

    while current.next:
      current= current.next

    current.next=new_node

  def insert_before(self,value,new_value):
      value_exists = False
      current = self.head
      if current and current.data == value:
          new_node = Node(new_value, self.head)
          self.head = new_node
      else:
        while current.next:
            if current.next.data == value:
                value_exists =True
                break
            current=current.next
        if value_exists:
            new_node=Node(new_value, current.next)
            current.next= new_node
        else:
            raise Exception('the value you entered does not exist in the linked list')

#   def insert_after(self,value,new_value):
#       value_exists = False
#       current = self.head
#       if current and current.data == value:
#           new_node = Node(new_value, self.head)
#           self.head = new_node
#       else:
#         while current.next:
#             if current.next.data == value:
#                 value_exists =True
#                 break
#             current=current.next
#         if value_exists:
#             new_node=Node(new_value, current.next)
#             current.next= new_node
#         else:
#             raise Exception('the value you entered does not exist in the linked list')

  def insert_after(self,value,new_value):
        current=self.head
        while current:
            if current.data==value:
                break
            current=current.next
        if current is None:
            raise Exception('node is not found')
        new_node = Node(new_value, current.next)
        current.next= new_node






