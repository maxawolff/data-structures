"""Test linked list."""
from linked_list import LinkedList, Node


def test_case_1():
    """test_case_1."""
    test = LinkedList()
    assert test.val == 0


def test_push():
    """Test for push method."""
    res = LinkedList()
    assert res.push(1) == 1


def test_node():
    """Test for node."""
    test_node = Node(1)
    assert test_node.val == 1
