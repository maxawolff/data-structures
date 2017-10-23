"""Linked list."""


class LinkedList(object):
    """Class for a linked list."""

    def __init__(self):
        """On list creation set head to none."""
        self.head = None
        self.length = 0

    def push(self, val):
        """Push a val to the list."""
        temp_node = Node(val)
        if self.head:
            temp_head = self.head
            temp_node.next = temp_head
            self.head = temp_node
        else:
            self.head = temp_node
        self.length += 1
        return temp_node.val

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

    def __init__(self, val):
        """Create a new node."""
        self.val = val
        self.next = None
