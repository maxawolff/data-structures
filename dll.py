"""Implementation of double linked list."""

from linked_list import LinkedList


class DLL(LinkedList):
    """Double linked list."""

    def __init__(self):
        """On list creation set tail to none."""
        super(DLL, self).__init__()
        self.tail = None

    # def push(self, val):
    #     """Add new item to the head of the double linked list."""
    #     super(DLL, self).push(val)

    def pop(self):
        """Remove and return the head."""
        return super(DLL, self).pop()
