from typing import Hashable
from hashtables.hashtables import HashTable

#test adding a key/value to your hashtable results in the value being in the data structure
def test_add_method_works():
        hashtable = HashTable()
        hashtable.add('Tasneem','Al-Absi')
        expected = True
        actual = hashtable.contains('Tasneem')
        assert actual == expected

#test retrieving based on a key returns the value stored
def test_get_method_works():
        hashtable = HashTable()
        hashtable.add('Tasneem','Al-Absi')
        expected = 'Al-Absi'
        actual = hashtable.get('Tasneem')
        assert actual == expected

#test successfully returns null for a key that does not exist in the hashtable
def test_get_returns_none_for_key_not_found():
        hashtable = HashTable()
        hashtable.add('Tasneem','Al-Absi')
        expected = None
        actual = hashtable.get('whatever')
        assert actual == expected

#test successfully handle a collision within the hashtable
def test_handle_collision():
        hashtable = HashTable()
        hashtable.add('cd','anything')
        hashtable.add('dc','whatever')
        expected1 = 369
        expected2 = 369

        actual1 = hashtable._HashTable__hash('cd')
        actual2 = hashtable._HashTable__hash('dc')
        assert actual1 == expected1
        assert actual2 == expected2

#test successfully retrieve a value from a bucket within the hashtable that has a collision
def test_return_value_in_collision():
        hashtable = HashTable()
        hashtable.add('cd','anything')
        hashtable.add('cd','whatever')
        expected = 'whatever'

        actual = hashtable.get('cd')
        assert actual == expected

#test successfully hash a key to an in-range value
def test_hash_key_in_range_value():
        hashtable = HashTable()
        hashtable.add('whatever','great word')
        expected = 970
        actual = hashtable._HashTable__hash('whatever')
        assert actual == expected


