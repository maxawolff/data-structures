"""Test for stack module."""

from stack import Stack
from linked_list import LinkedList


def test_stack_init_has_properties():
    """Test to see if init gives stack instance properties."""
    s = Stack()
    assert s.length == 0


def test_stack_is_subclass_of_linked_list():
    """Test to see if stack is a subclass of linked list."""
    s = Stack()
    assert isinstance(s._stack, LinkedList)


def test_push_val():
    """Test that push pushes to the head."""
    s = Stack()
    s.push(1)
    assert s._stack.head.val == 1
