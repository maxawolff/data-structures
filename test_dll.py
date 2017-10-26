"""Test double linked list."""

import pytest
from dll import DLL
from linked_list import Node


@pytest.fixture
def new_dll():
    """Create a new double linked list."""
    new_dll = DLL()
    return new_dll


def test_dll_on_init_has_tail(new_dll):
    """Test_dll_on_init_has_tail."""
    assert hasattr(new_dll, 'tail')


def test_push_to_dll(new_dll):
    """Test to for push method."""
    new_dll.push(2)
    assert new_dll.head.val == 2


def test_new_dll_head_is_none(new_dll):
    """."""
    assert new_dll.head is None


def test_node_has_prev_pointer():
    """Test for node previous pointer."""
    test_node = Node(1)
    assert test_node.prev is None
#
#
# def test_pop_returns_removes_and_returns_head(new_dll):
#     """Test_pop_returns_removes_and_returns_head."""
#     new_dll.push(4)
#     assert new_dll.pop() == 4
#


def test_remove_node_from_list(new_dll):
    """Test_remove_node_from_list."""
    new_dll.push(1)
    new_dll.push(2)
    new_dll.push(3)
    new_dll.remove(2)
    assert new_dll.head.next.val == 1
