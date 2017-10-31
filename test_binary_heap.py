"""Test binary heap."""
from binary_heap import Binheap, BinNode
import pytest


@pytest.fixture
def new_bin():
    """Create an empty tree."""
    return Binheap()


@pytest.fixture
def new_node():
    """Create an empty tree."""
    return BinNode(5)


def test_new_tree_first_node_no_head(new_bin):
    """Test_new_tree_first_node_no_parent."""
    assert new_bin.head is None


def test_new_node_has_val_and_parent(new_node):
    """Test that node has attributes that it should."""
    assert new_node.val == 5
    assert new_node.parent is None


def test_new_node_has_left_and_right(new_node):
    """Test that node has attributes that it should."""
    assert new_node.left is None
    assert new_node.right is None
