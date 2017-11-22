"""Implementation of a binary search tree."""

import pdb


class Node(object):
    """Node class for binary search tree."""

    def __init__(self, value, left=None, right=None, depth=0):
        """."""
        self.value = value
        self.left = left
        self.right = right
        self.depth = depth


class BST(object):
    """Binary search tree."""

    def __init__(self, iterable=None):
        """."""
        self.head = None
        self.left_depth = 0
        self.right_depth = 0
        self.depth = 0

    def insert(self, val):
        """Add a node into the bst."""
        if self.head is None:
            self.head = Node(val, depth=1)
            self.depth = 1
        current_node = self.head
        if val == self.head.value:
            return
        current_depth = 2
        while True:
            if val < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                    current_depth += 1
                else:
                    current_node.left = Node(val, depth=current_depth)
                    if current_depth > self.depth:
                        self.depth = current_depth
                    return
            elif val > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                    current_depth += 1
                else:
                    current_node.right = Node(val, depth=current_depth)
                    if current_depth > self.depth:
                        self.depth = current_depth
                    return
            elif val == current_node.value:
                return
