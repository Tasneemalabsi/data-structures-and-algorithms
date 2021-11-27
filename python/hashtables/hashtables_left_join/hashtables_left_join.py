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

    def get_buckets_keys(self):
        arr = []
        for i in self.__buckets:
            if i:
                arr.append(i.head.value[0])
        return arr



def left_join(hash1:HashTable, hash2:HashTable):
    arr = []
    keys = hash1.get_buckets_keys()
    for i in keys:
        value1 = hash1.get(i)
        if hash2.contains(i):
                value2 = hash2.get(i)
                arr.append([i, value1, value2])
        else:
            arr.append([i,value1,None])

    return arr









if __name__ == "__main__":
    hash1 = HashTable()
    hash1.add('foo','ff')
    hash1.add('moo','mm')
    hash1.add('doo','dd')
    hash1.add('soo','ss')
    hash2 = HashTable()
    hash2.add('fo','ff')
    hash2.add('moo','m')
    hash2.add('doo','d')
    hash2.add('so','s')
    print(left_join(hash1,hash2))
