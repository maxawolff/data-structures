"""Test binary heap."""
from binary_heap import Binheap
import pytest


@pytest.fixture
def new_bin():
    """Create an empty tree."""
    return Binheap()


def test_new_tree_first_node_no_parent(new_bin):
    """Test_new_tree_first_node_no_parent."""
    assert new_bin.parent is None
