from insertion_sort.insertion_sort import insertion_sort
import pytest

def test_insertion_sort_happy_path():
    # Arrange
    expected = [4, 8, 15, 16, 23, 42]

    # Act
    arr=[8,4,23,42,16,15]
    actual = insertion_sort(arr)

    # Assert
    assert actual == expected

def test_insertion_sort_edge_case1():
    # Arrange
    expected = [5,5,5,7,7,12]

    # Act
    arr=[5,12,7,5,5,7]
    actual = insertion_sort(arr)

    # Assert
    assert actual == expected

def test_insertion_sort_edge_case2():
    # Arrange
    expected = []

    # Act
    arr=[]
    actual = insertion_sort(arr)

    # Assert
    assert actual == expected

def test_insertion_sort_edge_case3():
    # Arrange
    expected = [-2,5,8,12,18,20]

    # Act
    arr=[20,18,12,8,5,-2]
    actual = insertion_sort(arr)

    # Assert
    assert actual == expected
