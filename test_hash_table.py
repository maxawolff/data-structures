"""Test file for hash table."""

import pytest
from hash_table import HashTable


def test_init():
    """Test that buckets get made on init."""
    h = HashTable(10)
    assert len(h.container) == 10


def test_additive():
    """Test that additive properly hashes a value."""
    h = HashTable(10)
    assert h._additive('key') == 9
