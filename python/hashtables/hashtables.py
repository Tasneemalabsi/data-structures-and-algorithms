import re

class Node:
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
        self.head = Node(value, self.head)


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

def repeated_word(string):
    """
    takes a string as an input then returns the first repeated word in this string

    Args:
        string

    Returns:
        string
    """
    hash = HashTable()
    lower_case_string = string.lower()
    arr = lower_case_string.split(" ")
    counter = 1
    result = ''
    for word in arr:
        new_word = re.sub(r'[^\w\s]', '', word)
        if hash.contains(new_word):
            counter += 1
            hash.add(new_word, counter)
        else:
            hash.add(new_word, counter)
        res = hash.get(new_word)
        if res > 1:
            result =  new_word
            break
    return result

def left_join(hash1:HashTable, hash2:HashTable):
    arr = []
    











if __name__ == "__main__":
    print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))









