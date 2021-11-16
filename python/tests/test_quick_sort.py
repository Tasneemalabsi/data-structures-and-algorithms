from quick_sort.quick_sort import quick_sort
import pytest

def test_quick_sort_happy_path():
    # Arrange
    expected = [4, 8, 15, 16, 23, 42]

    # Act
    arr=[8,4,23,42,16,15]
    actual = quick_sort(arr,0,len(arr)-1)

    # Assert
    assert actual == expected

def test_quick_sort_edge_case1():
    # Arrange
    expected = [5,5,5,7,7,12]

    # Act
    arr=[5,12,7,5,5,7]
    actual = quick_sort(arr,0,len(arr)-1)

    # Assert
    assert actual == expected

def test_quick_sort_edge_case2():
    # Arrange
    expected = []

    # Act
    arr=[]
    actual = quick_sort(arr,0,len(arr)-1)

    # Assert
    assert actual == expected

def test_quick_sort_edge_case3():
    # Arrange
    expected = [1]

    # Act
    arr=[1]
    actual = quick_sort(arr,0,len(arr)-1)

    # Assert
    assert actual == expected
