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
        node1.neighbors.append((node1, node2))
        node2.neighbors.append((node1, node2))
        self._edges.append((node1, node2))

    def del_node(self, val):
        """Delete and remove edges."""
        del_node = self.has_node(val)
        self._nodes.remove(del_node)

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
        """Remove an edge."""
        for edge in self._edges:
            if edge[0].val == val1 and edge[1].val == val2:
                self._edges.remove(edge)
                del_node1 = edge[0]
            else:
                return 'edge not found'
        for node in self._nodes:
            for neighbor in node.neighbors:
                if del_node1.val == neighbor[0].val or del_node1.val == neighbor[1].val:
                    node.neighbors.remove(neighbor)

    def has_node(self, val):
        """Return the node if found."""
        for node in self._nodes:
            if node.val == val:
                return node
        raise ValueError('node not found')

    def neighbors(self, val):
        """Return list of neighbors for the given node."""
        node = self.has_node(val)
        return node.neighbors

    def adjacent(self, val1, val2):
        """Return True if edge exists."""
        for edge in self._edges:
            if edge[0].val == val1 and edge[1].val == val2:
                return True
            else:
                return False

    def depth_first_traversal(self, start_val):
        """."""
        if not self.has_node(start_val):
            raise ValueError('node not found')
        current = self.has_node(start_val)
        res = [current.val]
        unvisited = []
        for neighbor in current.neighbors:
            if neighbor[0] == current:
                unvisited.append(neighbor[1])

        while unvisited:
            current = unvisited[-1]
            unvisited.remove(current)
            # import pdb; pdb.set_trace()
            if current.val not in res:
                res.append(current.val)
            for neighbor in current.neighbors:
                if neighbor[0] == current:
                    if not neighbor[1].val in res:
                        unvisited.append(neighbor[1])
        return res

    def breadth_first_traversal(self, start_val):
        """."""
        if not self.has_node(start_val):
            raise ValueError('node not found')
        current = self.has_node(start_val)
        res = [current.val]
        unvisited = []
        for neighbor in current.neighbors:
            if neighbor[0] == current:
                unvisited.append(neighbor[1])

        while unvisited:
            current = unvisited[0]
            unvisited.remove(current)
            # import pdb; pdb.set_trace()
            if current.val not in res:
                res.append(current.val)
            for neighbor in current.neighbors:
                if neighbor[0] == current:
                    if not neighbor[1].val in res:
                        unvisited.append(neighbor[1])
        return res


class Node(object):
    """Graph node."""

    def __init__(self, val):
        """."""
        self.val = val
        self.neighbors = []
