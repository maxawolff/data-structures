"""Test file for hash table."""

import pytest
from hash_table import HashTable
import pdb


@pytest.fixture
def ht():
    """Make graph to play with."""
    return HashTable(10)


@pytest.fixture
def big_ht():
    """."""
    ht = HashTable(10)
    import io
    f = io.open('words.txt')
    words = f.read()
    words = words.split('\n')
    f.close()
    for word in words:
        ht.set(word, word)
    return ht


@pytest.fixture
def low():
    """."""
    import io
    f = io.open('words.txt')
    words = f.read()
    words = words.split('\n')
    f.close()
    list_of_words = []
    for word in words:
        list_of_words.append(word)
    return list_of_words


def test_init(ht):
    """Test that buckets get made on init."""
    assert len(ht.container) == 10


def test_additive(ht):
    """Test that additive properly hashes a value."""
    assert ht._additive('key') == 9


def test_set_adds_value(ht):
    """Set should properly store a value at a given key."""
    ht.set('foo', 10)
    bucket = ht._additive('foo')
    assert 'foo' in ht.container[bucket]


def test_set_adds_second_value(ht):
    """Set should properly store a value at a given key."""
    ht.set('foo', 10)
    ht.set('hello', 5)
    bucket = ht._additive('hello')  # bucket == 2
    assert 'hello' in ht.container[bucket]


def test_big_ht_has_values(big_ht):
    """Test big ht stores values correctly."""
    assert 'hello' in big_ht.container[2]


def test_get_retrieves_correct_value(ht):
    """Get should return the value stored with the given key."""
    ht.set("test", 3)
    assert ht.get('test') == 3


def test_get_retrieves_correct_value_big_ht(big_ht, low):
    """Get should return the value stored with the given key."""
    for word in low:
        assert big_ht.get(word) == word
