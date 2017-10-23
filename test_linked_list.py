"""Test linked list."""
from linked_list import LinkedList, Node


def test_push():
    """Test for push method."""
    res = LinkedList()
    node = res.push(1)
    assert node == res.head.val


def test_node():
    """Test for node."""
    test_node = Node(1)
    assert test_node.val == 1


def test_init_list():
    """"test_init_list."""
    init = LinkedList()
    assert init.head is None


def test_empty_list_length():
    """Test size() on empty list."""
    test_list = LinkedList()
    assert test_list.size() == 0


def test_length_with_two_nodes():
    """test_length_with_two_nodes."""
    test_list = LinkedList()
    node1 = Node(2)
    node2 = Node(3)
    test_list.push(node1)
    test_list.push(node2)
    assert test_list.size() == 2


def test_empty_list_length_with_len():
    """Test size() on empty list using len method."""
    test_list = LinkedList()
    assert len(test_list) == 0


def test_display():
    """test_display."""
    test_list = LinkedList()
    test_list.push(1)
    test_list.push(2)
    test_list.push(3)
    assert test_list.display() == '3, 2, 1'
