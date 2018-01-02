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


@pytest.fixture
def bel():
    """Graph to use with diskstas algorithm."""
    g = Graph()
    g.add_edge('S', 'A', 10)
    g.add_edge('S', 'E', 8)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'A', 1)
    g.add_edge('C', 'B', -2)
    g.add_edge('D', 'C', -1)
    g.add_edge('D', 'A', -4)
    g.add_edge('E', 'D', 1)
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
    assert new_graph._nodes[0].val == 1


def test_newgraph_scope(new_graph):
    """Test fixture."""
    assert new_graph._nodes == []


def test_insert_duplicate_node_raises_error(new_graph):
    """Test_insert_duplicate_node_raises_error."""
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
    """Test_del_node_deletes_nodes."""
    new_graph.add_node(1)
    new_graph.del_node(1)
    assert new_graph._nodes == []


def test_del_node_deletes_node_1(new_graph):
    """Test_del_node_deletes_node_1."""
    new_graph.add_node(1)
    new_graph.add_node(2)
    new_graph.del_node(1)
    assert new_graph._nodes[0].val == 2


def test_del_node_deltes_edge(new_graph):
    """Test_del_node_deltes_edge."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.del_node(1)
    assert ng._edges == []


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
    assert ng._edges == []


def test_remove_edge_also_removes_neighbors():
    """Test_remove_edge_also_removes_neighbors."""
    ng = Graph()
    ng.add_edge(1, 2)
    node1 = ng._nodes[0]
    # node2 = ng._nodes[1]
    ng.del_edge(1, 2)
    assert node1.neighbors == []


def test_graph_depth_first():
    """Test_graph_depth_first."""
    ng = Graph()
    ng.add_edge(1, 2)
    assert ng.depth_first_traversal(1) == [1, 2]


def test_graph_depth_first_large():
    """Test_graph_depth_first_large."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.add_edge(1, 7)
    ng.add_edge(1, 8)
    ng.add_edge(8, 9)
    ng.add_edge(8, 12)
    ng.add_edge(9, 10)
    ng.add_edge(9, 11)
    ng.add_edge(2, 6)
    ng.add_edge(2, 3)
    ng.add_edge(3, 4)
    ng.add_edge(3, 5)
    # print (ng.depth_first_traversal(1))
    assert ng.depth_first_traversal(1) == [1, 8, 12, 9, 11, 10, 7, 2, 3, 5, 4, 6]


def test_graph_depth_first_large_2():
    """Test_graph_depth_first_large_2."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.add_edge(1, 3)
    ng.add_edge(2, 4)
    ng.add_edge(2, 5)
    ng.add_edge(3, 6)
    ng.add_edge(3, 7)
    ng.add_edge(4, 8)
    ng.add_edge(4, 9)
    ng.add_edge(5, 10)
    ng.add_edge(5, 11)
    ng.add_edge(6, 12)
    ng.add_edge(6, 13)
    ng.add_edge(7, 14)
    ng.add_edge(7, 15)
    assert ng.depth_first_traversal(1) == [1, 3, 7, 15, 14, 6, 13, 12, 2, 5, 11, 10, 4, 9, 8]


def test_circular():
    """Test_circular."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.add_edge(1, 3)
    ng.add_edge(3, 1)
    # print (ng.depth_first_traversal(1))
    assert ng.depth_first_traversal(1) == [1, 3, 2]


def test_circular_more_complex():
    """Test_circular_more_complex."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.add_edge(1, 3)
    ng.add_edge(3, 5)
    ng.add_edge(5, 2)
    ng.add_edge(3, 4)
    ng.add_edge(4, 3)
    ng.add_edge(2, 4)
    assert ng.depth_first_traversal(1) == [1, 3, 4, 5, 2]


def test_graph_breadth_first_large():
    """Test_graph_breadth_first_large."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.add_edge(1, 3)
    ng.add_edge(2, 4)
    ng.add_edge(2, 5)
    ng.add_edge(3, 6)
    ng.add_edge(3, 7)
    ng.add_edge(4, 8)
    ng.add_edge(4, 9)
    ng.add_edge(5, 10)
    ng.add_edge(5, 11)
    ng.add_edge(6, 12)
    ng.add_edge(6, 13)
    ng.add_edge(7, 14)
    ng.add_edge(7, 15)
    assert ng.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def test_graph_breadth_first_unbalanced():
    """Test_graph_breadth_first_unbalanced."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.add_edge(1, 3)
    ng.add_edge(1, 4)
    ng.add_edge(2, 5)
    ng.add_edge(2, 6)
    ng.add_edge(5, 8)
    ng.add_edge(8, 10)
    ng.add_edge(4, 7)
    ng.add_edge(7, 9)
    assert ng.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_graph_breadth_first_unbalanced_different_order():
    """Test_graph_breadth_first_unbalanced_different_order."""
    ng = Graph()
    ng.add_edge(8, 10)
    ng.add_edge(1, 2)
    ng.add_edge(7, 9)
    ng.add_edge(1, 4)
    ng.add_edge(2, 5)
    ng.add_edge(2, 6)
    ng.add_edge(5, 8)
    ng.add_edge(1, 3)
    ng.add_edge(4, 7)
    assert ng.breadth_first_traversal(1) == [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]


def test_graph_breadth_first_large_start_at_2():
    """Test_graph_breadth_first_large_start_at_2."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.add_edge(1, 3)
    ng.add_edge(2, 4)
    ng.add_edge(2, 5)
    ng.add_edge(3, 6)
    ng.add_edge(3, 7)
    ng.add_edge(4, 8)
    ng.add_edge(4, 9)
    ng.add_edge(5, 10)
    ng.add_edge(5, 11)
    ng.add_edge(6, 12)
    ng.add_edge(6, 13)
    ng.add_edge(7, 14)
    ng.add_edge(7, 15)
    assert ng.breadth_first_traversal(2) == [2, 4, 5, 8, 9, 10, 11]


def test_graph_depth_first_large_2_start_at_2():
    """Test_graph_depth_first_large_2_start_at_2."""
    ng = Graph()
    ng.add_edge(1, 2)
    ng.add_edge(1, 3)
    ng.add_edge(2, 4)
    ng.add_edge(2, 5)
    ng.add_edge(3, 6)
    ng.add_edge(3, 7)
    ng.add_edge(4, 8)
    ng.add_edge(4, 9)
    ng.add_edge(5, 10)
    ng.add_edge(5, 11)
    ng.add_edge(6, 12)
    ng.add_edge(6, 13)
    ng.add_edge(7, 14)
    ng.add_edge(7, 15)
    assert ng.depth_first_traversal(2) == [2, 5, 11, 10, 4, 9, 8]


def test_zero_edge_weight():
    """Test default weight."""
    ng = Graph()
    ng.add_edge(1, 2)
    assert ng._edges[0][2] == 0


def test_edge_weight():
    """Test correct weight."""
    ng = Graph()
    ng.add_edge(1, 2, 1)
    assert ng._edges[0][2] == 1


def test_edge_weight_not_num():
    """Test incorrect weight."""
    ng = Graph()
    with pytest.raises(ValueError):
        ng.add_edge(1, 2, 'qwoei')


def test_dijkstra(dgraph):
    """."""
    res = dgraph.dijkstra('A')
    assert res['D'] == ['A', 'C', 'B', 'D', 9]
    assert res['A'] == ['A', 0]
    assert res['B'] == ['A', 'C', 'B', 8]


def test_traversal2(dgraph):
    """."""
    res = dgraph.depth_first_traversal2("A")
    for node in res:
        print(node)
    assert len(res) == 4


def test_dijkstra_g3_f(g3):
    """."""
    res = g3.dijkstra('A')
    assert res['F'] == ['A', 'B', 'E', 'F', 11]


def test_dijkstra_g3_e(g3):
    """."""
    res = g3.dijkstra('A')
    assert res['E'] == ['A', 'B', 'E', 8]


def test_dijkstra_g3_d(g3):
    """."""
    res = g3.dijkstra('A')
    assert res['D'] == ['A', 'C', 'D', 5]


def test_dijkstra_g4_g(g4):
    """."""
    res = g4.dijkstra('A')
    assert res['G'] == ['A', 'E', 'G', 12]


def test_dijkstra_g4_f(g4):
    """."""
    res = g4.dijkstra('A')
    assert res['F'] == ['A', 'E', 'D', 'F', 10]


def test_dijkstra_g4_f_start_at_c(g4):
    """."""
    res = g4.dijkstra('C')
    assert res['F'] == ['C', 'E', 'D', 'F', 11]


def test_dijkstra_g4_g_start_at_c(g4):
    """."""
    res = g4.dijkstra('C')
    assert res['G'] == ['C', 'E', 'G', 13]


def test_dijkstra_g4_start_at_c_no_a(g4):
    """."""
    res = g4.dijkstra('C')
    with pytest.raises(KeyError):
        res["A"]


def test_shortest_path_end_ae(g3):
    """."""
    res = g3.dijkstra_end('A', 'E')
    assert res == ['A', 'B', 'E', 8]


def test_shortest_path_end_af(g3):
    """."""
    res = g3.dijkstra_end('A', 'F')
    assert res == ['A', 'B', 'E', 'F', 11]


def test_shortest_path_end_bf(g3):
    """."""
    res = g3.dijkstra_end('B', 'F')
    assert res == ['B', 'E', 'F', 9]


def test_shortest_path_end_be(g3):
    """."""
    res = g3.dijkstra_end('B', 'D')
    assert res == ['B', 'E', 'D', 7]


def test_shortest_path_end_g4ae(g4):
    """."""
    res = g4.dijkstra_end('A', 'G')
    assert res == ['A', 'E', 'G', 12]


def test_shortest_path_end_g4af(g4):
    """."""
    res = g4.dijkstra_end('A', 'F')
    assert res == ['A', 'E', 'D', 'F', 10]


def test_shortest_path_end_g4bg(g4):
    """."""
    res = g4.dijkstra_end('B', 'G')
    assert res == ['B', 'D', 'G', 15]


def test_belman_ford(bel):
    """."""
    res = bel.belman_ford('S', 'C')
