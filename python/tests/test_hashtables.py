from typing import Hashable
from hashtables.hashtables import HashTable, repeated_word

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

#-----------------------------tests from challenge31: repeated word---------------------------

#test happy path-1:
def test_repeated_word_happy_path():
    expected = "a"
    actual = repeated_word("Once upon a time, there was a brave princess who...")
    assert actual == expected

#test happy path-2:
def test_repeated_word_handle_upper_lower_cases():
    expected = "it"
    actual = repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")
    assert actual == expected

#test happy path-3:
def test_repeated_word_handle_words_with_punctuation():
    expected = "summer"
    actual = repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    assert actual == expected

#test edge case-1:
def test_repeated_word_empty_input_string():
    expected = ""
    actual = repeated_word("")
    assert actual == expected

#test edge case-2:
def test_repeated_word_one_word_input():
    expected = ""
    actual = repeated_word("once")
    assert actual == expected

#test edge case-3:
def test_repeated_word_no_repeated_words():
    expected = ""
    actual = repeated_word("once upon a time")
    assert actual == expected




