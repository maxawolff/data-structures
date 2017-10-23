"""Test linked list."""
from linked_list import LinkedList


def test_case_1():
    """test_case_1."""
    test = LinkedList()
    assert test.val == 0


def test_push():
    """Test for push method."""
    assert LinkedList(1) == 1
