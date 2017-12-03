"""Test file for hash table."""

import pytest
from hash_table import HashTable
import pdb


@pytest.fixture
def ht():
    """Make graph to play with."""
    return HashTable(10)


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
