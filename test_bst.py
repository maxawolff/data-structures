"""Test for bst."""
import pytest
import pdb


@pytest.fixture
def new_bst():
    """."""
    from bst import BST
    b = BST()
    b.insert(20)
    return b


@pytest.fixture
def bst_d1():
    """."""
    from bst import BST
    b = BST()
    b.insert(20)
    b.insert(10)
    b.insert(30)
    return b


def test_node_has_val():
    """."""
    from bst import Node
    n = Node(4)
    assert n.value == 4


def test_bst_add_one_node_becomes_head():
    """Adding one node should make it the head."""
    from bst import BST
    b = BST()
    b.insert(4)
    assert b.head.value == 4


def test_bst_add_two_nodes_second_smaller(new_bst):
    """Adding a node smaller than the head should set left."""
    new_bst.insert(8)
    assert new_bst.head.left.value == 8


def test_bst_add_two_nodes_second_largeer(new_bst):
    """Adding a node larger than the head should set left."""
    new_bst.insert(30)
    assert new_bst.head.right.value == 30


def test_bst_depth_of_1(bst_d1):
    """BST with left and right value."""
    assert bst_d1.head.right.value == 30
    assert bst_d1.head.left.value == 10


def test_bst_d1_add_left_left(bst_d1):
    """Add a value to the left of the left of head."""
    bst_d1.insert(5)
    assert bst_d1.head.left.left.value == 5


def test_bst_d1_add_left_left_left(bst_d1):
    """Add a value to the left of the left of head."""
    bst_d1.insert(5)
    bst_d1.insert(2)
    assert bst_d1.head.left.left.left.value == 2


def test_bst_d1_add_left_left_left_and_right(bst_d1):
    """Add a value to the left of the left of head."""
    bst_d1.insert(5)
    bst_d1.insert(2)
    bst_d1.insert(4)
    assert bst_d1.head.left.left.left.value == 2
    assert bst_d1.head.left.left.left.right.value == 4


def test_empty_bst_depth_0():
    """An empty bst should have depth 0."""
    from bst import BST
    b = BST()
    assert b.depth == 0


def test_bst_depth_of_one(new_bst):
    """Bst with one node should have depth of 1."""
    assert new_bst.depth == 1
    assert new_bst.head.depth == 1


def test_bst_depth_two_nodes_is_2(new_bst):
    """Bst with one node should have depth of 1."""
    new_bst.insert(1)
    assert new_bst.depth == 2
    assert new_bst.head.left.depth == 2


def test_bst_depth_three_nodes_is_2_when_balanced(new_bst):
    """Bst with one node should have depth of 1."""
    new_bst.insert(1)
    new_bst.insert(30)
    assert new_bst.depth == 2
    assert new_bst.head.right.depth == 2


def test_bst_depth_three_nodes_is_3_when_unbalanced(new_bst):
    """Bst with one node should have depth of 1."""
    new_bst.insert(1)
    new_bst.insert(5)
    assert new_bst.depth == 3
    assert new_bst.head.left.right.depth == 3


def test_search_one_node(new_bst):
    """Search for the one node in a bst."""
    assert new_bst.search(20).value == 20


def test_search_one_node_wrong_value_returns_none(new_bst):
    """Search for a node not in a bst."""
    assert new_bst.search(21) is None


def test_search_several_nodes(bst_d1):
    """Search one of the nodes in a bst."""
    assert bst_d1.search(30).value == 30
    assert bst_d1.search(20).value == 20


def test_search_several_nodes_wrong_node(bst_d1):
    """Searching for a node not present returns none."""
    assert bst_d1.search(100000) is None
