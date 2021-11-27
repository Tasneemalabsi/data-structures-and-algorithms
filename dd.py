class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True

            current = current.next

        return False

    def to_string(self):
        current = self.head

        the_stringified_result = ''

        while current:

            the_stringified_result += "{ " + str(current.value) + " } -> "
            current = current.next
        the_stringified_result = the_stringified_result+"NULL"
        return the_stringified_result

    def append (self, value):
        current = self.head
        while current.next:
            node = Node(value, None)
            current = current.next
        current.next = node
    def insert_before(self, value1, value2):
        current = self.head
        if current:
            if current.value == value2:
                self.head = Node(value1,self.head)

            else:
              while current.next:
                  if current.next.value ==value2:
                      node = Node(value1, current.next)
                      current.next = node
                      break
                  current = current.next
    def insert_after(self, value1, value2):
        current = self.head
        while current.next:
            if current.value == value2:
                break
            current = current.next
        node = Node(value1, current.next)
        current.next = node
    def kth_value(self, index):
        current = self.head
        length = -1
        while current:
            length += 1
            current = current.next
        val = ''
        current=self.head
        for i in range(length):
            current = current.next
            if length-i-1 == index:
                val=current.value
                break
        return val

def mergeLists(list1, list2):
    node1=0
    current = list1.head
    current2 = list2.head
    if not list1.head:
        return list2.to_string()
    if not list2.head:
        return list1.to_string()

    while current and current2:

        node1 = current2
        current2 = current2.next
        node1.next = current.next
        current.next = node1

        current = current.next.next

    # if current2:
    #     current = list1.head

    #     while current.next:
    #         current = current.next
    #     current.next = current2.head

    #     current2.head = None

    return list1

def reversed_list(ll:LinkedList):
      current = ll.head
      previous = None
      while current:
        next = current.next
        current.next  = previous
        previous = current
        current = next
      ll.head = previous


      return ll.to_string()

def isPalindrome(ll:LinkedList):
  res = False
  string = ''
  current = ll.head
  while current:
    string += f" {current.value} "
    current = current.next
  if string == string[::-1]:
    res = True
  return res

def duplicate (ll:LinkedList):
  current = ll.head
  while current.next:
    print(current.value)
    if current.value == current.next.value:
      new_current = current.next.next
      current.next = None
      current.next = new_current
    else:
      current = current.next
  return ll













if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(4)
    ll.insert(3)
    ll.insert(2)
    ll.insert(2)
    ll.insert(1)
    ll2 = LinkedList()
    ll2.insert(1)
    ll2.insert(2)
    ll2.insert(17)
    ll2.insert(23)
    # ll2.insert(7)
    rr = LinkedList()
    rr.insert('m')
    rr.insert('o')
    rr.insert('o')
    rr.insert('m')
    # print(reversed_list(ll))
    # print('to string', rr.to_string())
    # print('rrrrr',reversed_list(rr))
    # print('ispalindrome', isPalindrome(rr))
    # print(ll.to_string())
    # print(ll2.to_string())
    # print(mergeLists(ll, ll2).to_string())
    print(duplicate(ll).to_string())



