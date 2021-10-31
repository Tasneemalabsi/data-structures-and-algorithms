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

    def __init__(self, data, next_=None):
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

            the_stringified_result += "{ " + str(current.data) + " } -> "
            current = current.next
        the_stringified_result = the_stringified_result+"NULL"
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
            self.head = Node(value)

        current = self.head
        # if it's not empty, loop through the linked list until we reach the last node
        while current.next:
            current = current.next
        # creates the new node after the last node in the linked last
        current.next = Node(value)

    def insert_before(self, value, new_value):
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
                    value_exists = True
                    break
                current = current.next
            # after finding the value, add the node before it, or to the next of the previous value .
            if value_exists:
                new_node = Node(new_value, current.next)
                current.next = new_node
            # if the input value doesn't exist in the linked list, raise an exception
            else:
                raise Exception(
                    'the value you entered does not exist in the linked list')

    def insert_after(self, value, new_value):
        """
        a method that adds a new node after a given value in a specific node

        arguments:
        value : any value in the linked list
        new_value: any

        returns: None

        """
        current = self.head
       # loop through the linked list until we find the input value
        while current:
            if current.data == value:
                break
            current = current.next
       # raise an exception if the value doesn't exist
        if current is None:
            raise Exception('node is not found')
       # add a new node after the given value, at the next to this specific value
        new_node = Node(new_value, current.next)
        current.next = new_node

    def kth_value(self, index):
        """
        this method finds the node located at the kth value of a linked list, this k value starts counting from the tail of the list

        arguments:
        index : integer positive number which is the kth value from the end

        returns: value, the data in the node located at the input kth value

        """
        current = self.head
        length = -1
        while current:
            length = length+1
            current = current.next
        if index >= length:
            raise Exception('the index is out of range')
        if index < 0:
            raise Exception('the index is out of range')
        current = self.head
        for i in range(length - index):

            current = current.next
        print(current.data)
        return current.data


def zipLists(list1:LinkedList, list2:LinkedList):

    """
    this function takes two linked lists as arguments and returns a merged alternative list of theses two lists
    arguments:
    list2 : the first linked list
    list1: the second linked list
    returns: merged linked list
    """
    node1=0
    current = list1.head
    if not list1.head:
        return list2.to_string()
    if not list2.head:
        return list1.to_string()

    while current.next and list2.head:
        
        node1 = list2.head
        list2.head = list2.head.next
        node1.next = current.next
        current.next = node1

        current = current.next.next

    if list2.head:
        current = list1.head

        while current.next:
            current = current.next
        current.next = list2.head

        list2.head = None

    return list1.to_string()






#the technical interview practice question
def reversed_list(list: LinkedList):
    current = list.head
    new_list = LinkedList()
    while current:
        new_list.insert(current.data)
        current = current.next
    return new_list.to_string()



if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert(5)
    l1.append(7)
    l1.append(8)
    l1.append(9)
    l1.append(10)
    l2 = LinkedList()
    l2.insert(1)
    l2.append(2)
    # l2.append(3)
    # l2.append(4)
    # l2.append(11)
    # l2.append(12)
    print(zipLists(l1,l2))
