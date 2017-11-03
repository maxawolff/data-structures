"""Test graph."""

import pytest
from graph import Graph, Node
import pdb


@pytest.fixture
def new_graph():
    """Make graph to play with."""
    return Graph()


@pytest.fixture
def new_node():
    """A node."""
    return Node(1)


def test_new_emty_graph_nodes(new_graph):
    """Test_new_emty_graph_nodes."""
    assert new_graph._nodes == []


def test_new_emty_graph_edges(new_graph):
    """Test_new_emty_graph_edges."""
    assert new_graph._edges == []


def test_node_neighbors(new_node):
    """Test_node_neighbors."""
    assert new_node.neighbors == []


def test_only_one_edge(new_graph):
    """."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    # node2 = ng._nodes[1]
    with pytest.raises(IndexError):
        print(node1.neighbors[1][0].val)


def test_insert_1node(new_graph):
    """."""
    new_graph.add_node(1)
    assert new_graph._nodes[0].val == 1


def test_newgraph_scope(new_graph):
    """Test fixture."""
    assert new_graph._nodes == []


def test_insert_duplicate_node_raises_error(new_graph):
    """."""
    new_graph.add_node(1)
    with pytest.raises(ValueError):
        new_graph.add_node(1)


def test_add_edge_empty_graph_makes_nodes(new_graph):
    """Should make two new nodes and add to nodes list."""
    new_graph.add_edge(1, 2)
    assert len(new_graph._nodes) == 2


def test_add_edge_empty_graph_makes_edge(new_graph):
    """Should add an edge."""
    new_graph.add_edge(1, 2)
    assert new_graph._edges[0][0].val == 1
    assert new_graph._edges[0][1].val == 2


def test_add_edge_existing_nodes(new_graph):
    """Test_add_edge_existing_nodes."""
    new_graph.add_node(1)
    new_graph.add_node(2)
    new_graph.add_edge(1, 2)
    assert new_graph._edges[0][0].val == 1
    assert new_graph._edges[0][1].val == 2


def test_add_existing_edge(new_graph):
    """Test_add_existing_edge."""
    new_graph.add_node(1)
    new_graph.add_node(2)
    new_graph.add_edge(1, 2)
    assert new_graph.add_edge(1, 2) == 'Edge already exists'


def test_add_existing_edge_reversed(new_graph):
    """Test_add_existing_edge_reversed."""
    new_graph.add_node(1)
    new_graph.add_node(2)
    new_graph.add_edge(1, 2)
    new_graph.add_edge(2, 1)
    assert new_graph._edges[1][0].val == 2
    assert new_graph._edges[1][1].val == 1


def test_add_edge_existing_node(new_graph):
    """Test_add_edge_existing_nod."""
    new_graph.add_node(1)
    new_graph.add_edge(1, 2)
    assert new_graph._edges[0][0].val == 1
    assert new_graph._edges[0][1].val == 2


def test_del_node_deletes_nodes(new_graph):
    """."""
    new_graph.add_node(1)
    new_graph.del_node(1)
    assert new_graph._nodes == []


def test_del_node_deletes_node_1(new_graph):
    """."""
    new_graph.add_node(1)
    new_graph.add_node(2)
    new_graph.del_node(1)
    assert new_graph._nodes[0].val == 2


def test_del_node_deltes_edge(new_graph):
    """."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.del_node(1)
    assert ng._edges == []


def test_del_node_deltes_neighbor(new_graph):
    """."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    node2 = ng._nodes[1]
    assert node1.neighbors[0][0].val == node1.val
    assert node1.neighbors[0][1].val == node2.val
