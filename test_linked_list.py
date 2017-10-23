"""Test linked list."""
from linked_list import LinkedList, Node


def test_push():
    """Test for push method."""
    res = LinkedList()
    node = res.push(1)
    assert node == 1


def test_node():
    """Test for node."""
    test_node = Node(1)
    assert test_node.val == 1


def test_init_list():
    """"test_init_list."""
    init = LinkedList()
    assert init.head is None
