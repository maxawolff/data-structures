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


def test_new_empty_graph_nodes(new_graph):
    """Test_new_emty_graph_nodes."""
    assert new_graph._nodes == []


def test_new_empty_graph_edges(new_graph):
    """Test_new_emty_graph_edges."""
    assert new_graph._edges == []


def test_node_neighbors(new_node):
    """Test_node_neighbors."""
    assert new_node.neighbors == []


<<<<<<< HEAD
def test_only_one_edge():
    """."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    # node2 = ng._nodes[1]
    with pytest.raises(IndexError):
        print(node1.neighbors[1][0].val)


=======
>>>>>>> f93b4fac9b4540f4bf91046e346f4cc1e4aff976
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


def test_add_edge_empty_graph_makes_nodes():
    """Should make two new nodes and add to nodes list."""
    ng = Graph()
    ng.add_edge(1, 2)
    assert len(ng._nodes) == 2


def test_add_edge_empty_graph_makes_edge():
    """Should add an edge."""
    ng = Graph()
    ng.add_edge(1, 2)
    assert ng._edges[0][0].val == 1
    assert ng._edges[0][1].val == 2


def test_add_edge_existing_nodes():
    """Test_add_edge_existing_nodes."""
    ng = Graph()
    ng.add_node(1)
    ng.add_node(2)
    ng.add_edge(1, 2)
    assert ng._edges[0][0].val == 1
    assert ng._edges[0][1].val == 2


def test_add_existing_edge():
    """Test_add_existing_edge."""
    ng = Graph()
    ng.add_node(1)
    ng.add_node(2)
    ng.add_edge(1, 2)
    assert ng.add_edge(1, 2) == 'Edge already exists'


def test_add_existing_edge_reversed():
    """Test_add_existing_edge_reversed."""
    ng = Graph
    ng.add_node(1)
    ng.add_node(2)
    ng.add_edge(1, 2)
    ng.add_edge(2, 1)
    assert ng._edges[1][0].val == 2
    assert ng._edges[1][1].val == 1


def test_add_edge_existing_node():
    """Test_add_edge_existing_nod."""
    ng = Graph()
    ng.add_node(1)
    ng.add_edge(1, 2)
    assert ng._edges[0][0].val == 1
    assert ng._edges[0][1].val == 2


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


def test_del_node_deltes_edge():
    """."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.del_node(1)
    assert ng._edges == []


def test_del_node_deltes_neighbor():
    """."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    node2 = ng._nodes[1]
    assert node1.neighbors[0][0].val == node1.val
    assert node1.neighbors[0][1].val == node2.val


def test_only_one_edge(new_graph):
    """."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    with pytest.raises(IndexError):
        print(node1.neighbors[1][0].val)


def test_neighbors_function_returns_list_of_neighbors(new_graph):
    """."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    nlist = ng.neighbors(1)
    assert nlist[0][0] == node1


def test_adjacent_returns_true(new_graph):
    """."""
    ng = Graph()
    ng.add_edge(1, 2)
    assert ng.adjacent(1, 2) is True


def test_remove_edge(new_graph):
    """."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.del_edge(1, 2)
    assert ng._edges == []


def test_remove_edge_also_removes_neighbors():
    """."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    # node2 = ng._nodes[1]
    ng.del_edge(1, 2)
    assert node1.neighbors == []
