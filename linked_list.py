"""Linked list."""


class LinkedList(object):
    """Class for a linked list."""

    def __init__(self):
        """On list creation set head to none."""
        self.head = None
        self.length = 0

    def push(self, val):
        """Push a val to the list."""
        self.head = Node(val, self.head)
        self.length += 1

    def pop(self):
        """Remove the head of the list and return it."""
        if self.head is None:
            raise IndexError("List is empty, cannot pop from an empty list")
        val = self.head
        self.head = self.head.next
        self.length -= 1
        return val

    def size(self):
        """Return the length of the list."""
        return self.length

    def display(self):
        """Display the list."""
        return self.__str__()

    def __len__(self):
        """Redifine the built in len function for the list."""
        return self.length

    def __str__(self):
        """Return a tuple list."""
        thing = ''
        thing += str(self.head.val)
        current_node = self.head
        while current_node.next:
            thing += ', ' + str(current_node.next.val)
            current_node = current_node.next
        return thing


class Node(object):
    """Class for node."""

    def __init__(self, val, next=None):
        """Create a new node."""
        self.val = val
        self.next = next
