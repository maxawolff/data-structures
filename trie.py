"""Implementation of a trie tree."""


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
        self.depth = 0

    def insert(self, word):
        """Add a word to the trie tree."""
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
        current.children.append(Node('$'))
        self.depth += 1
