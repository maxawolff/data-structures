"""Linked list."""


class LinkedList(object):
    """Class for a linked list."""

    val = 0

    def push(self, val):
        """Push a val to the list."""
        self.val = val
        return val
