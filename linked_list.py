"""Linked list."""


class LinkedList(object):
    """Class for a linked list."""

    val = 0

    def push(self, val):
        """Push a val to the list."""
        self.val = val
        return val


class Node(object):
    """Class for node."""

    def __init__(self, val):
        """Create a new node."""
        self.val = val
        self.next = None
