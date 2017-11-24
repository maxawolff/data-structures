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
        self._depth = 0
        self.nodes = []

    def insert(self, val):
        """Add a node into the bst."""
        if self.head is None:
            new_node = Node(val, depth=1)
            self.head = new_node
            self._depth = 1
            self.nodes.append(new_node)
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
                    new_node = Node(val, depth=current_depth)
                    current_node.left = new_node
                    self.nodes.append(new_node)
                    if current_depth > self._depth:
                        self._depth = current_depth
                    return
            elif val > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                    current_depth += 1
                else:
                    new_node = Node(val, depth=current_depth)
                    current_node.right = new_node
                    self.nodes.append(new_node)
                    if current_depth > self._depth:
                        self._depth = current_depth
                    return
            elif val == current_node.value:
                return

    def search(self, val):
        """."""
        for node in self.nodes:
            if node.value == val:
                return node

    def depth(self):
        """Return the depth of a bst."""
        return self._depth
