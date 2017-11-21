"""Implementation of a binary search tree."""

import pdb


class Node(object):
    """Node class for binary search tree."""

    def __init__(self, value, left=None, right=None):
        """."""
        self.value = value
        self.left = left
        self.right = right


class BST(object):
    """Binary search tree."""

    def __init__(self, iterable=None):
        """."""
        self.head = None

    def insert(self, val):
        """Add a node into the bst."""
        if self.head is None:
            self.head = Node(val)
        current_node = self.head
        if val == self.head.value:
            return
        while True:
            if val < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = Node(val)
                    return
            elif val > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = Node(val)
                    return
            elif val == current_node.value:
                return
