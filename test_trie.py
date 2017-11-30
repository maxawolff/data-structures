"""Test for trie tree."""
import pytest
import pdb
from trie import Node, Trie


@pytest.fixture
def new_trie():
    """."""
    t = Trie()
    return t


def test_node_class_has_correct_values():
    """Test node object is made correctly."""
    n = Node('t')
    assert n.value == 't'
    assert n.children == []
    assert n.parent is None


def test_insert_one_word_empty_trie(new_trie):
    """Assert hello added correctly into empty tree."""
    new_trie.insert('hello')
    current_node = new_trie.root.children[0]
    assert current_node.value == 'h'
    current_node = current_node.children[0]
    assert current_node.value == 'e'
    current_node = current_node.children[0]
    assert current_node.value == 'l'
    current_node = current_node.children[0]
    assert current_node.value == 'l'
    current_node = current_node.children[0]
    assert current_node.value == 'o'
