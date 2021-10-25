from stack_and_queue.node import Node
from stack_and_queue.queue import Queue
from stack_and_queue.stack_queue_animal_shelter import AnimalShelter, Dog, Cat

import pytest

def test_import():
    assert Queue

#test adding one value to a queue
def test_enqueue_one_value():
    #Arrange
    expected = "cat"
    #Act
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("cat")
    actual = queue.rear.value
    #Assert
    assert actual == expected
#test adding multiple values to a queue
def test_enqueue_multiple_values():
    #Arrange
    expected = [1,2,"cat"]
    #Act
    arr=[]
    queue = Queue()
    queue.enqueue(1)
    arr.append(queue.rear.value)
    queue.enqueue(2)
    arr.append(queue.rear.value)
    queue.enqueue("cat")
    arr.append(queue.rear.value)
    actual = arr

    #Assert
    assert actual == expected

# test dequeue one value out of a queue
def test_dequeue_one_value():
    #Arrange
    expected = 1
    #Act
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)

    actual = queue.dequeue()

    assert actual == expected

# test the peek of a queue(rear value)
def test_peek_queue():
    #Arrange
    expected='cat'
    #Act
    queue=Queue()
    queue.enqueue("cat")
    queue.enqueue("abc")
    actual=queue.peek()
    #Assert
    assert actual == expected

# test empty queue after dequeue all values out of it
def test_dequeue_all_values():
    #Arrange
    expected = True
    #Act
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("cat")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    actual=queue.is_empty()
    #Assert
    actual == expected

# instantiate an empty queue
def test_is_empty_for_a_queue():
    #Arrange
    expected = True
    #Act
    queue = Queue()
    actual = queue.is_empty()
    assert actual == expected

#test peek of an empty queue raises an exception
def test_peek_an_empty_queue_raises_exception():
    #Arrange
    expected=Exception
    #Act
    queue=Queue()
    #Assert
    with pytest.raises(Exception):
        queue.peek()

#test dequeue out of an empty queue raises an exception
def test_dequeue_from_empty_queue_raises_exception():
    #Arrange
    expected=Exception
    #Act
    queue=Queue()
    #Assert
    with pytest.raises(Exception):
        queue.dequeue()

#-----------------------------tests for animal-shelter-challenge-------------------------

#test enqueue and dequeue a dog object
def test_dog_object():

    an = AnimalShelter()
    dog = Dog('Rufus')
    an.enqueue(dog)
    actual = an.dequeue('dog')
    assert actual.name == 'Rufus'

#test enqueue and dequeue a cat object
def test_cat_object():

    animal = AnimalShelter()
    cat = Cat('Tom')
    animal.enqueue(cat)
    actual = animal.dequeue('cat')
    assert actual.name == 'Tom'

# test removing from an empty queue raises exception
def test_empty_queue():
    animal = AnimalShelter()
    with pytest.raises(Exception):
        animal.dequeue()

# test if the preferred animal is not a cat or a dog returns null
def test_wrong_name_returns_null():
    animal = AnimalShelter()

    actual=animal.dequeue('not cat or dog')
    assert actual == 'null'

