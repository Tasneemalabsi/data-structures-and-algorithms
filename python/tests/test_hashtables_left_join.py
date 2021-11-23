from hashtables.hashtables_left_join.hashtables_left_join import HashTable,left_join
import pytest

def test_left_join_happy_path():
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

    expected = [['doo', 'dd', 'd'], ['foo', 'ff', None], ['moo', 'mm', 'm'], ['soo', 'ss', None]]
    actual = left_join(hash1, hash2)
    assert actual == expected

def test_left_join_second_table_empty():
    hash1 = HashTable()
    hash1.add('foo','ff')
    hash1.add('moo','mm')
    hash1.add('doo','dd')
    hash1.add('soo','ss')
    hash2 = HashTable()


    expected = [['doo', 'dd', None], ['foo', 'ff', None], ['moo', 'mm', None], ['soo', 'ss', None]]
    actual = left_join(hash1, hash2)
    assert actual == expected

def test_left_join_first_table_empty():
    hash1 = HashTable()
    hash2 = HashTable()
    hash2.add('fo','ff')
    hash2.add('moo','m')
    hash2.add('doo','d')
    hash2.add('so','s')


    expected = []
    actual = left_join(hash1, hash2)
    assert actual == expected
