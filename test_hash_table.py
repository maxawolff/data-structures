"""Test file for hash table."""

import pytest
from hash_table import HashTable
import pdb


@pytest.fixture
def ht():
    """Make an empty hash table, hash func is additive, size is 10."""
    return HashTable(10)


@pytest.fixture
def ht2():
    """Make an empty hash table, hash func is oat, size is 10."""
    return HashTable(10, func='oat')


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
def big_ht2():
    """."""
    ht2 = HashTable(10, func='oat')
    import io
    f = io.open('words.txt')
    words = f.read()
    words = words.split('\n')
    f.close()
    for word in words:
        ht2.set(word, word)
    return ht2


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


def test_additive_same_for_same_letters(ht):
    """Test that additive properly hashes a value."""
    assert ht._additive('amp') == ht._additive('map')


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


def test_oat_hash_different_same_letters(ht):
    """OAT hash provides different results for keys with the same letters."""
    assert ht._oat('map') != ht._oat('amp')


def test_hash_table_with_oat_at_init(ht2):
    """See if init works properly with oat specified as hash."""
    assert ht2._hash('map') != ht2._hash('amp')


def test_hash_table_with_oat_set(ht2):
    """Set should place key and value in proper place."""
    ht2.set('hello', 1)
    bucket = ht2._oat('hello')  # bucket = 5
    assert 'hello' in ht2.container[bucket]


def test_hash_table_with_oat_set_then_get(ht2):
    """Test if get works after setting."""
    ht2.set('hello', 1)
    assert ht2.get('hello') == 1


def test_big_ht2_has_values(big_ht2):
    """Test big ht stores values correctly."""
    assert 'hello' in big_ht2.container[5]


def test_get_retrieves_correct_value_big_ht2(big_ht2, low):
    """Get should return the value stored with the given key."""
    for word in low:
        assert big_ht2.get(word) == word
