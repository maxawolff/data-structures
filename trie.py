"""Implementation of a trie tree."""
import pdb


class Node(object):
    """Node class for trie tree."""

    def __init__(self, value, children=None, parent=None):
        """."""
        self.value = value
        self.children = []
        self.child_values = []
        self.parent = parent


class Trie(object):
    """Trie tree."""

    def __init__(self, iterable=None):
        """Initiate a trie."""
        self.root = Node('*')
        self._size = 0

    def insert(self, word):
        """Add a word to the trie tree."""
        if self.contains(word):
            return
        current = self.root
        for letter in word:
            if letter not in current.child_values:
                node = Node(letter, parent=current)
                current.children.append(node)
                current.child_values.append(node.value)
                current = node
            else:
                index = current.child_values.index(letter)
                current = current.children[index]
        current.children.append(Node('$', parent=current))
        current.child_values.append('$')
        self._size += 1

    def contains(self, word):
        """Check if a word is in the trie."""
        if not isinstance(word, str):
            raise TypeError("word must be a string")
        current_node = self.root
        for letter in word:
            nodes_visited = 0
            for node in current_node.children:
                if letter == node.value:
                    current_node = node
                    break
                nodes_visited += 1
                if nodes_visited == len(current_node.children):
                    return False
        for node in current_node.children:
            if node.value == '$':
                return True
        return False

    def remove(self, word):
        """Remove a word from the trie tree."""
        if not isinstance(word, str):
            raise TypeError("word must be a string")
        word += '$'
        to_delete = []
        current_node = self.root
        for letter in word:
            if letter in current_node.child_values:
                index = current_node.child_values.index(letter)
                current_node = current_node.children[index]
                to_delete.append(current_node)
            else:
                raise ValueError("That word is not in the trie, therefor it can't be deleted")
        to_delete.reverse()
        for node in to_delete:
            if len(node.children) == 0:
                parent = node.parent
                parent.children.remove(node)
                parent.child_values.remove(node.value)
            else:
                break
        self._size -= 1

    def size(self):
        """Get size of a trie."""
        return self._size
