"""Implementation of a stack."""


from linked_list import LinkedList, Node


class Stack(object):
    """Class for a stack."""

    def __init__(self, iterable=None):
        """Function to create an instance of a stack."""
        self.length = 0
        self.head = None
        self._stack = LinkedList()

    def pop(self):
        """Use LinkedList pop method."""
        self._stack.pop()

    def push(self, val):
        """Use push method from LinkedList."""
        self._stack.push(val)
