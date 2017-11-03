"""Test graph."""

import pytest
from graph import Graph, Node


@pytest.fixture
def new_graph():
    """Make graph to play with."""
    return Graph()


@pytest.fixture
def new_node():
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


def test_insert_1node(new_graph):
    """."""
    new_graph.add_node(1)
    assert new_graph._nodes[0].val == 1


def test_newgraph_scope(new_graph):
    """Test fixture."""
    assert new_graph._nodes == []
