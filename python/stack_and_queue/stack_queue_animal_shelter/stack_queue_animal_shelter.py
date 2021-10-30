from stack_and_queue.queue import Queue

class AnimalShelter:
    """
    A class for creating queues for dogs and cats.

    Data and other attributes defined here:

    dog_queue: Queue instance
    cat_queue: Queue instance

    """
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        """
        this method looks at the added animal, if it is a dog object it adds a dog to the dog queue and if it's a cat it adds a cat to the cat queue

        arguments:
        animal: object/ either a dog or a cat
        """
        if isinstance(animal, Dog):
            self.dog_queue.enqueue(animal)
        elif isinstance(animal,Cat):
            self.cat_queue.enqueue(animal)


    def dequeue(self, pref):
        """
        this method looks at the animal that is going to get adopted, if it is a dog object it removes a dog from the dog queue and if it's a cat it removes a cat from the cat queue

        arguments:
        pref: string
        returns: string
        """
        if not self.dog_queue or not self.cat_queue:
            raise Exception("the animal queue is empty")
        if pref == 'dog':
           return self.dog_queue.dequeue()
        elif pref == 'cat':
           return self.cat_queue.dequeue()
        else:
            return "null"



class Dog:
    """
    this class creates instances of dog objects
    arguments:
    name: string
    """
    def __init__(self, name):
        self.name = name
class Cat:
    """
    this class creates instances of cat objects
    arguments:
    name: string
    """
    def __init__(self, name):
        self.name = name
