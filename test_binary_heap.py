"""Test binary heap."""
from binary_heap import Binheap
import pytest


@pytest.fixture
def new_bin():
    """Create an empty tree."""
    return Binheap()


def test_new_tree_first_node_no_head(new_bin):
    """Test_new_tree_first_node_no_parent."""
    assert new_bin.container == []


def test_push_one_val(new_bin):
    """Empty heap should have one item in it."""
    new_bin.push(3)
    assert new_bin.container[0] == 3


def test_push_two_vals_out_of_order(new_bin):
    """Empty heap should have one item in it."""
    new_bin.push(3)
    new_bin.push(10)
    print(new_bin.container)
    assert new_bin.container == [10, 3]


def test_two_vals_backwards(new_bin):
    """Value should get switched when put in out of order."""
    new_bin.push(1)
    new_bin.push(2)
    assert new_bin.container == [2, 1]


def test_three_vals_backwards(new_bin):
    """Value should get switched when put in out of order."""
    new_bin.push(1)
    new_bin.push(2)
    new_bin.push(3)
    print(new_bin.container)
    assert new_bin.container == [3, 1, 2]


def test_four_vals_backwards(new_bin):
    """Value should get switched when put in out of order."""
    new_bin.push(1)
    new_bin.push(2)
    new_bin.push(3)
    new_bin.push(4)
    print(new_bin.container)
    assert new_bin.container == [4, 3, 2, 1]


def test_five_vals_backwards(new_bin):
    """Value should get switched when put in out of order."""
    new_bin.push(1)
    new_bin.push(2)
    new_bin.push(3)
    new_bin.push(4)
    new_bin.push(5)
    print(new_bin.container)
    assert new_bin.container == [5, 4, 3, 2, 1]


def test_ten_vals_backwards(new_bin):
    """."""
    new_bin.push(1)
    new_bin.push(2)
    new_bin.push(3)
    new_bin.push(4)
    new_bin.push(5)
    new_bin.push(6)
    new_bin.push(7)
    new_bin.push(8)
    new_bin.push(9)
    new_bin.push(10)
    print(new_bin.container)
    assert new_bin.container == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def test_15_vals_backwards(new_bin):
    """."""
    new_bin.push(15)
    new_bin.push(2)
    new_bin.push(3)
    new_bin.push(4)
    new_bin.push(5)
    new_bin.push(6)
    new_bin.push(7)
    new_bin.push(8)
    new_bin.push(9)
    new_bin.push(10)
    new_bin.push(11)
    new_bin.push(12)
    new_bin.push(13)
    new_bin.push(14)
    new_bin.push(1)
    print(new_bin.container)
    assert new_bin.container == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
