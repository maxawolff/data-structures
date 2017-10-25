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
    assert s.top.val == 1


def test_push_val2():
    """Test that push pushes to the head."""
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.top.next.val == 1


def test_pop():
    """Test that pop will remove and return a value."""
    s = Stack()
    s.push(1)
    assert s.pop() == 1


def test_length():
    """Test that the length function is working."""
    s = Stack()
    s.push(1)
    s.push(2)
    assert len(s) == 2
