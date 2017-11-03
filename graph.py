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
        for node in self._nodes:
            if node.val == val:
                raise ValueError("Nodes must have unique values")
        self._nodes.append(Node(val))

    def add_edge(self, val1, val2):
        """Add a connection between two nodes, val1 points to val2."""
        node1 = 0
        node2 = 0
        for node in self._nodes:
            if node.val == val1:
                node1 = node
            if node.val == val2:
                node2 = node
        if node1 == 0:
            node1 = Node(val1)
            self.add_node(node1.val)
        if node2 == 0:
            node2 = Node(val2)
            self.add_node(node2.val)
        if node1 == node2:
            raise ValueError("You cannot connect a node to itself")
        node1.neighbors.append((node1, node2))
        node2.neighbors.append((node1, node2))
        self._edges.append((node1, node2))

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
