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
    for i in range(len(hash1._HashTable__buckets)):
        if hash1._HashTable__buckets[i]:
            print(i)
            if hash2.contains(hash1._HashTable__buckets[i].head.value[0]):
                arr.append([hash1._HashTable__buckets[i].head.value[0],hash1._HashTable__buckets[i].head.value[1],hash2._HashTable__buckets[i].head.value[1]])
            else:
                arr.append([hash1._HashTable__buckets[i].head.value[0],hash1._HashTable__buckets[i].head.value[1],None])

    return arr


def unique_characters(string):
    if not string:
        raise Exception("string is empty")
    hash = HashTable()
    new_string = string.replace(" ", "")
    for character in new_string.lower():
        if hash.contains(character):
                return False
        hash.add(character,None)

    return True

def most_common(string):
    hash = HashTable()
    arr = []
    new = string.lower()
    arr2 = new.split(" ")
    counter = 0
    for character in arr2:
       character = character.strip('.')
       if not hash.contains(character):
        hash.add(character,counter)
       else:
           hash.add(character,counter+1)
       arr.append(hash.get(character))
       if max(arr) == hash.get(character):
           res = character
           break

    return res





if __name__ == "__main__":
    print(unique_characters("tasneem"))







