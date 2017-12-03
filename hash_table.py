"""Implementation of a hash table."""


class HashTable(object):
    """class for Hash_Table."""

    def __init__(self, size, func='None'):
        """Build hash table on initiation."""
        self.size = size
        self.container = []
        for i in range(0, self.size):
            self.container.append({})
        if func is None:
            self.func = self._additive

    def _additive(self, key):
        """Given a key, perform a hashing algorithm on it."""
        value = 0
        for letter in key:
            value += ord(letter)
        return value % self.size

    def set(self, key, val):
        """Set a value in the hash table."""
        if not type(key) == str:
            raise TypeError('key must be a string')
        bucket = self.func(key)
        self.container[bucket]['key'] = val


