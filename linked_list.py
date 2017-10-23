"""Linked list."""


class LinkedList(object):
    """Class for a linked list."""

    def __init__(self):
        """On list creation set head to none."""
        self.head = None

    def push(self, val):
        """Push a val to the list."""
        temp_node = Node(val)
        if self.head:
            temp_head = self.head
            temp_node.next = temp_head
            self.head = temp_node
        else:
            self.head = temp_node
        return temp_node.val


class Node(object):
    """Class for node."""

    def __init__(self, val):
        """Create a new node."""
        self.val = val
        self.next = None
