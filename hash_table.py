"""Implementation of a hash table."""
import pdb


class HashTable(object):
    """class for Hash_Table."""

    def __init__(self, size, func=None):
        """Build hash table on initiation."""
        self.size = size
        self.container = []
        for i in range(0, self.size):
            self.container.append({})
        if func is None or func == 'a':
            self.func = 'a'
        elif func == 'oat':
            self.func = 'oat'
        else:
            raise ValueError("please enter a valid hash funcition, see README")

    def _additive(self, key):
        """Given a key, perform a hashing algorithm on it."""
        value = 0
        for letter in key:
            value += ord(letter)
        return value % self.size

    def _hash(self, key):
        """Hash a given key."""
        if self.func == 'a':
            bucket = self._additive(key)
        elif self.func == 'oat':
            bucket = self._oat(key)
        return bucket

    def set(self, key, val):
        """Set a value in the hash table."""
        if not type(key) == str:
            raise TypeError('key must be a string')
        bucket = self._hash(key)
        self.container[bucket][key] = val

    def get(self, key):
        """Get the value for a given key."""
        if not type(key) == str:
            raise TypeError('key must be a string')
        bucket = self._hash(key)
        try:
            return self.container[bucket][key]
        except KeyError:
            return None

    def _oat(self, key):
        """Hash a given key using the one at a time hash."""
        value = 0
        for letter in key:
            value += ord(letter)
            value += (value << 10)
            value ^= (value >> 6)
        value += (value << 3)
        value ^= (value >> 11)
        value += (value << 15)
        return value % self.size
