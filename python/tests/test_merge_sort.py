from merge_sort.merge_sort import merge_sort
import pytest

def test_merge_sort_happy_path():
    # Arrange
    expected = [4, 8, 15, 16, 23, 42]

    # Act
    arr=[8,4,23,42,16,15]
    actual = merge_sort(arr)

    # Assert
    assert actual == expected

def test_merge_sort_edge_case1():
    # Arrange
    expected = [5,5,5,7,7,12]

    # Act
    arr=[5,12,7,5,5,7]
    actual = merge_sort(arr)

    # Assert
    assert actual == expected

def test_merge_sort_edge_case2():
    # Arrange
    expected = []

    # Act
    arr=[]
    actual = merge_sort(arr)

    # Assert
    assert actual == expected

def test_merge_sort_edge_case3():
    # Arrange
    expected = [1]

    # Act
    arr=[1]
    actual = merge_sort(arr)

    # Assert
    assert actual == expected
