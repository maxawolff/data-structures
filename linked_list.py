"""Linked list."""


class LinkedList(object):
    """Class for a linked list."""

    def __init__(self, iterable=None):
        """On list creation set head to none."""
        self.head = None
        self.length = 0
        if isinstance(iterable, (str, tuple, list)):
            for i in iterable:
                self.push(i)

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

    def search(self, val):
        """Search list for given value and return the node."""
        current = self.head
        while current:
            if current.val == val:
                return current
            current = current.next

    def remove(self, node):
        """Remove a node from the linked list."""
        current = self.head
        node_to_remove = None
        while current:
            if current.next == node:
                node_to_remove = current.next
                self.length -= 1
                current.next = current.next.next
            current = current.next

        if node_to_remove is None:
            raise IndexError("Node was not found in list")

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
        thing = '('
        thing += str(self.head.val)
        current_node = self.head
        while current_node.next:
            thing += ', ' + str(current_node.next.val)
            current_node = current_node.next
        thing += ')'
        return thing


class Node(object):
    """Class for node."""

    def __init__(self, val, next=None, prev=None):
        """Create a new node."""
        self.val = val
        self.next = next
        self.prev = prev
