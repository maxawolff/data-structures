"""Test for bst."""
import pytest


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
