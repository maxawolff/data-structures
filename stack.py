"""Implementation of a stack."""


from linked_list import LinkedList, Node


class Stack(LinkedList):
    """Class for a stack."""

    def __init__(self, iterable=None):
        """Function to create an instance of a stack."""
        self.length = 0
