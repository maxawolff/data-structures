"""Implement a graph."""


class Graph(object):
    """Graph data structure."""
    def __init__(self):
        """."""
        self._nodes = []
        self._edges = []

    def nodes(self):
        """."""
        return self._nodes

    def edges(self):
        """."""
        return self._edges

    def add_node(self, val):
        """."""
        self._nodes.append(Node(val))

    def add_edge(self, val1, val2):
        """."""

    def del_node(self, val):
        """."""

    def del_edge(self, val1, val2):
        """."""

    def has_node(self, val):
        """."""

    def neighbors(self, val):
        """."""

    def adjacent(self, val1, val2):
        """."""


class Node(object):
    """Graph node."""
    def __init__(self, val, neighbors=[]):
        """."""
        self.val = val
        self.neighbors = neighbors
