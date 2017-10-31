"""Implementation of binary search tree."""


class Binheap(object):
    """Binary search tree."""

    def __init__(self):
        """."""
        self.head = None


class BinNode(object):
    """Node for binary heap."""

    def __init__(self, val, parent=None, left=None, right=None):
        """Initialization of binheap node."""
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
