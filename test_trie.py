"""Test for trie tree."""
import pytest
import pdb
from trie import Node, Trie


@pytest.fixture
def new_trie():
    """."""
    t = Trie()
    return t


@pytest.fixture
def small_trie():
    """."""
    t = Trie()
    t.insert("ape")
    t.insert("apple")
    t.insert("app")
    t.insert("apples")
    t.insert("halfway")
    t.insert("half")
    t.insert("halt")
    t.insert("hello")
    return t


@pytest.fixture
def big_trie():
    """."""
    t = Trie()
    import io
    f = io.open('words.txt')
    words = f.read()
    words = words.split('\n')
    f.close()
    for word in words:
        t.insert(word)
    return t


@pytest.fixture
def low():
    """."""
    import io
    f = io.open('words.txt')
    words = f.read()
    words = words.split('\n')
    f.close()
    list_of_words = []
    for word in words:
        list_of_words.append(word)
    return list_of_words


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


def test_many_words(big_trie):
    """Test trie was made correctly out of all words."""
    assert big_trie.size() > 10000


def test_contains_returns_false_on_word_not_found(new_trie):
    """Contain returns false on word not found."""
    assert new_trie.contains('word') is False


def test_contains_raise_error_on_bad_type(new_trie):
    """Contain returns false on word not found."""
    with pytest.raises(TypeError):
        new_trie.contains(4)


def test_contains_returns_true_on_only_word(new_trie):
    """Contain returns false on word not found."""
    new_trie.insert("yes")
    assert new_trie.contains('yes') is True


def test_contains_returns_true_on_two_words(new_trie):
    """Contain returns false on word not found."""
    new_trie.insert("yes")
    new_trie.insert("yellow")
    assert new_trie.contains('yellow') is True


def test_contains_returns_false_similar_words(new_trie):
    """Contain returns false on word not found."""
    new_trie.insert("yes")
    new_trie.insert("yellow")
    assert new_trie.contains('yeller') is False


def test_list_of_words(low):
    """Test words are properly added to list of words."""
    assert 'water' in low


def test_contains_returns_true_big_trie(big_trie, low):
    """Contain method works with a million inserts."""
    import random
    assert big_trie.contains('test') is True
    for x in range(0, 100):
        pos = len(low)
        rand = random.randint(0, pos)
        word = low[rand]
        assert big_trie.contains(word)


def test_remove_one_word(new_trie):
    """Try to remove the only word from a trie."""
    new_trie.insert('word')
    new_trie.remove('word')
    assert len(new_trie.root.children) == 0
    assert new_trie.contains('word') is False


def test_remove_several_word(new_trie):
    """Try to remove the only word from a trie."""
    new_trie.insert('word')
    new_trie.insert('world')
    new_trie.insert('wonder')
    new_trie.insert('whale')
    new_trie.remove('word')
    assert new_trie.contains('word') is False
    assert len(new_trie.root.children[0].children[0].children[0].children) == 1


def test_remove_word_from_several_words_affects_size(new_trie):
    """Try to remove the only word from a trie."""
    new_trie.insert('word')
    new_trie.insert('world')
    new_trie.insert('wonder')
    new_trie.insert('whale')
    new_trie.remove('word')
    assert new_trie.size() == 3


def test_remove_one_word_from_all_the_words(big_trie):
    """Remove one word from a trie with a billion words."""
    big_trie.remove('hello')
    assert big_trie.contains('hello') is False


def test_add_duplicate_word(new_trie):
    """Adding a duplicate word should be ignored."""
    new_trie.insert('hello')
    new_trie.insert('hello')
    assert new_trie.size() == 1
    assert len(new_trie.root.children) == 1


# def test_traverse_finds_end_of_start_word(big_trie):
#     """Test traverse finds starting point."""
#     assert big_trie.traversal('hel') == 'l'


# def test_traversal_errors_word_not_in_trie(new_trie):
#     """Should raise a value error when start not in trie."""
#     new_trie.insert("hello")
#     gen = new_trie.traversal('a')
#     with pytest.raises(ValueError):
#         next(gen)


def test_traversal_given_one_letter(small_trie):
    """Should return all of the letters after the given letter."""
    gen = small_trie.traversal('a')
    values = []
    while True:
        try:
            values.append(next(gen))
        except StopIteration:
            break
    assert values == ['a', 'p', 'p', 'l', 'e', 's', 'e']


def test_traversal_given_other_first_letter(small_trie):
    """Should return all of the letters after the given letter."""
    gen = small_trie.traversal('h')
    values = []
    while True:
        try:
            values.append(next(gen))
        except StopIteration:
            break
    assert values == ['h', 'e', 'l', 'l', 'o', 'a', 'l', 't', 'f' 'w', 'a', 'y']


def test_traversal_whole_trie(small_trie):
    """Should return all of the letters after the given letter."""
    gen = small_trie.traversal('*')
    values = []
    while True:
        try:
            values.append(next(gen))
        except StopIteration:
            break
    assert values == ['h', 'e', 'l', 'l', 'o', 'a', 'l', 't', 'f' 'w', 'a', 'y']
