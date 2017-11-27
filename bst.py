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
        direction = ''
        if self.head is None:
            new_node = Node(val, depth=1)
            self.head = new_node
            self._depth = 1
            self.nodes.append(new_node)
            self.left_depth = 1
            self.right_depth = 1
        current_node = self.head
        if val == self.head.value:
            return
        current_depth = 2
        while True:
            if val < current_node.value:
                if current_depth == 2:
                    direction = 'left'
                if current_node.left:
                    current_node = current_node.left
                    current_depth += 1
                else:
                    new_node = Node(val, depth=current_depth)
                    current_node.left = new_node
                    self.nodes.append(new_node)
                    if current_depth > self._depth:
                        self._depth = current_depth
                    if direction == 'left' and self.left_depth < current_depth:
                        self.left_depth = current_depth
                    elif direction == 'right' and self.right_depth < current_depth:
                        self.right_depth = current_depth
                    return
            elif val > current_node.value:
                if current_depth == 2:
                    direction = 'right'
                if current_node.right:
                    current_node = current_node.right
                    current_depth += 1
                else:
                    new_node = Node(val, depth=current_depth)
                    current_node.right = new_node
                    self.nodes.append(new_node)
                    if current_depth > self._depth:
                        self._depth = current_depth
                    if direction == 'right' and self.right_depth < current_depth:
                        self.right_depth = current_depth
                    elif direction == 'left' and self.left_depth < current_depth:
                        self.left_depth = current_depth
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

    def contains(self, val):
        """Return true if val is a node in bst."""
        if self.search(val):
            return True
        else:
            return False

    def balance(self):
        """Return balance of tree."""
        return self.right_depth - self.left_depth

    def breadth_first(self):
        """Traverse the bst in breadth first order, returns generator."""
        if not self.head:
            return []
        to_visit = []
        visited = []
        to_visit.append(self.head)
        current_node = self.head
        while to_visit:
            if current_node.left:
                to_visit.append(current_node.left)
            if current_node.right:
                to_visit.append(current_node.right)
            visited.append(current_node.value)
            to_visit.pop(0)
            # pdb.set_trace()
            if to_visit:
                current_node = to_visit[0]
        return (x for x in visited)

    def pre_order(self):
        """Traverse the bst in pre-order, returns generator."""
        to_visit = []
        to_visit.append(self.head)
        current = None
        while to_visit or current:
            if not current:
                current = to_visit.pop()
            else:
                yield current.value
                to_visit.extend([current.right, current.left])
                current = to_visit.pop()

    def in_order(self):
        """Traverse the bst in-order, returns generator."""
        to_visit = []
        current = self.head
        while current or to_visit:
            if current:
                to_visit.append(current)
                current = current.left
            else:
                current = to_visit.pop()
                yield current.value
                current = current.right

    def post_order(self):
        """Traverse the bst in post_order, returns generator."""
        to_visit = []
        current = self.head
        while current or to_visit:
            if current:
                if current.right:
                    to_visit.append(current.right)
                to_visit.append(current)
                current = current.left
            else:
                current = to_visit.pop()
                if to_visit and current.right == to_visit[-1]:
                    to_visit.pop()
                    to_visit.append(current)
                    current = current.right
                else:
                    yield current.value
                    current = None
