"""Implement a graph."""

import pdb


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
            self._nodes.append(node1)
        if node2 == 0:
            node2 = Node(val2)
            self._nodes.append(node2)
        if node1 == node2:
            raise ValueError("You cannot connect a node to itself")
        for edge in self._edges:
            if edge == (node1, node2):
                return 'Edge already exists'
        # pdb.set_trace()
        node1.neighbors.append((node1, node2))  # should only add nieghbors for node 1, but it adds them to both for some reason
        # pdb.set_trace()
        node2.neighbors.append((node1, node2))
        # pdb.set_trace()
        self._edges.append((node1, node2))

    def del_node(self, val):
        """Delete and remove edges."""
        del_node = 0
        for node in self._nodes:
            if node.val == val:
                del_node = node
                self._nodes.remove(node)
        for edge in self._edges:
            if del_node.val == edge[0].val or del_node.val == edge[1].val:
                self._edges.remove(edge)
        for node in self._nodes:
            for neighbor in node.neighbors:
                if del_node.val == neighbor[0].val or del_node.val == neighbor[1].val:
                    node.neighbors.remove(neighbor)
        if del_node == 0:
            raise ValueError('node not found')

    def del_edge(self, val1, val2):
        """."""

    def has_node(self, val):
        """."""
        for node in self._nodes:
            if node.val == val:
                return node
            raise ValueError('node not found')

    def neighbors(self, val):
        """."""

    def adjacent(self, val1, val2):
        """."""


class Node(object):
    """Graph node."""

    def __init__(self, val):
        """."""
        self.val = val
        self.neighbors = []
