"""Test for trie tree."""
import pytest
import pdb
from trie import Node, Trie
import words


@pytest.fixture
def new_trie():
    """."""
    t = Trie()
    return t


@pytest.fixture
def big_trie():
    """."""
    t = Trie()



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


def test_inset_two_words_same_first_letter(new_trie):
    """Insert two words, same starting letter."""
    new_trie.insert('hello')
    new_trie.insert('hola')
    assert len(new_trie.root.children) == 1
    assert new_trie.root.children[0].children[1].value == 'o'


def test_insert_two_words_same_first_three_letters(new_trie):
    """Insert two nodes with the same first three letters."""
    new_trie.insert('hello')
    new_trie.insert('help')
    e_node = new_trie.root.children[0].children[0]
    assert len(e_node.children) == 1
    assert e_node.children[0].value == 'l'
    assert len(e_node.children[0].children) == 2
    assert e_node.children[0].children[0].value == 'l'
    assert e_node.children[0].children[1].value == 'p'
