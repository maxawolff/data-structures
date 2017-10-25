"""Implementation of double linked list."""

from linked_list import LinkedList


class DLL(LinkedList):
    """Double linked list."""

    def __init__(self):
        """On list creation set tail to none."""
        super(DLL, self).__init__()
        self.tail = None
