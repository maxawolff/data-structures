"""Implementation of a hash table."""


class HashTable(object):
    """class for Hash_Table."""

    def __init__(self, size):
        """Build hash table on initiation."""
        self.size = size
        self.container = []
        for i in range(0, self.size):
            self.container.append([])

    def _additive(self, key):
        """Given a key, perform a hashing algorithm on it."""
        value = 0
        for letter in key:
            value += ord(letter)
        return value % self.size
