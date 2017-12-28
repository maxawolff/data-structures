"""Test graph."""

import pytest
from graph2 import Graph, Node
import pdb


@pytest.fixture
def new_graph():
    """Make graph to play with."""
    return Graph()


@pytest.fixture
def new_node():
    """A node."""
    return Node(1)


@pytest.fixture
def dgraph():
    """Graph to use with diskstas algorithm."""
    g = Graph()
    g.add_edge('A', 'B', 12)
    g.add_edge('A', 'C', 5)
    g.add_edge('C', 'B', 3)
    g.add_edge('C', 'D', 10)
    g.add_edge('B', 'D', 1)
    return g


@pytest.fixture
def g3():
    """Graph to use with diskstas algorithm."""
    g = Graph()
    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 1)
    g.add_edge('B', 'C', 9)
    g.add_edge('B', 'E', 6)
    g.add_edge('C', 'D', 4)
    g.add_edge('D', 'F', 8)
    g.add_edge('E', 'D', 1)
    g.add_edge('E', 'F', 3)
    return g


@pytest.fixture
def g4():
    """Graph to use with diskstas algorithm."""
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 3)
    g.add_edge('A', 'E', 7)
    g.add_edge('B', 'C', 6)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 11)
    g.add_edge('C', 'E', 8)
    g.add_edge('E', 'D', 1)
    g.add_edge('D', 'F', 2)
    g.add_edge('E', 'G', 5)
    g.add_edge('D', 'G', 10)
    return g


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
    """Test_insert_1node."""
    new_graph.add_node(1)
    assert new_graph.nodes()[0] == 1


def test_insert_duplicate_node_raises_error(new_graph):
    """Test_insert_duplicate_node_raises_error."""
    new_graph.add_node(1)
    with pytest.raises(ValueError):
        new_graph.add_node(1)


def test_add_edge_empty_graph_makes_nodes(new_graph):
    """Should make two new nodes and add to nodes list."""
    new_graph.add_edge(1, 2)
    assert len(new_graph.nodes()) == 2


def test_add_edge_empty_graph_makes_edge(new_graph):
    """Should add an edge."""
    new_graph.add_edge(1, 2)
    assert new_graph.edges()[0][0] == 1
    assert new_graph.edges()[0][1] == 2


def test_add_edge_existing_nodes(new_graph):
    """Test_add_edge_existing_nodes."""
    new_graph.add_node(1)
    new_graph.add_node(2)
    new_graph.add_edge(1, 2)
    assert new_graph.edges()[0][0] == 1
    assert new_graph.edges()[0][1] == 2


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
    assert new_graph.edges()[1][0] == 2
    assert new_graph.edges()[1][1] == 1


def test_add_edge_existing_node(new_graph):
    """Test_add_edge_existing_nod."""
    new_graph.add_node(1)
    new_graph.add_edge(1, 2)
    assert new_graph._edges[0][0].val == 1
    assert new_graph._edges[0][1].val == 2


def test_del_node_deletes_nodes(new_graph):
    """Test_del_node_deletes_nodes."""
    new_graph.add_node(1)
    new_graph.del_node(1)
    assert new_graph.nodes() == []


def test_del_node_deletes_node_1(new_graph):
    """Test_del_node_deletes_node_1."""
    new_graph.add_node(1)
    new_graph.add_node(2)
    new_graph.del_node(1)
    assert new_graph.nodes()[0] == 2


def test_del_node_deltes_edge(new_graph):
    """Test_del_node_deltes_edge."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.del_node(1)
    assert ng.edges() == []


def test_del_node_deltes_neighbor(new_graph):
    """Test_del_node_deltes_neighbor."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    node2 = ng._nodes[1]
    assert node1.neighbors[0][0].val == node1.val
    assert node1.neighbors[0][1].val == node2.val


def test_only_one_edge(new_graph):
    """Test_only_one_edge."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    with pytest.raises(IndexError):
        print(node1.neighbors[1][0].val)


def test_neighbors_function_returns_list_of_neighbors(new_graph):
    """Test_neighbors_function_returns_list_of_neighbors."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    nlist = ng.neighbors(1)
    assert nlist[0][0] == node1


def test_adjacent_returns_true(new_graph):
    """Test_adjacent_returns_true."""
    ng = Graph()
    ng.add_edge(1, 2)
    assert ng.adjacent(1, 2) is True


def test_remove_edge(new_graph):
    """Test_remove_edge."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.del_edge(1, 2)
    assert ng.edges() == []


def test_remove_edge_also_removes_neighbors():
    """Test_remove_edge_also_removes_neighbors."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    ng.del_edge(1, 2)
    assert node1.neighbors == []


def test_graph_weighted_edges():
    """Test weighted edges are correctly implemented."""
    g = Graph()
    g.add_edge('a', 'b', 5)
    assert g.edges()[0][2] == 5
    assert g.edges()[0] == ('a', 'b', 5)


def test_graph_weighted_edges_default_to_0():
    """Test weighted edges are correctly implemented."""
    g = Graph()
    g.add_edge('a', 'b')
    assert g.edges()[0][2] == 0
    assert g.edges()[0] == ('a', 'b', 0)
