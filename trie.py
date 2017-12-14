"""Implementation of a trie tree."""
import pdb


class Node(object):
    """Node class for trie tree."""

    def __init__(self, value, parent=None):
        """."""
        self.value = value
        self.children = []
        self.child_values = []
        self.parent = parent


class Trie(object):
    """Trie tree."""

    def __init__(self):
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
                raise ValueError("That word is not in the trie, therefore it can't be deleted")
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

    def traversal(self, start):
        """Perform a depth first traversal on a trie."""
        if not isinstance(start, str):
            raise ValueError("start point must be a string")
        current_node = self.root
        for letter in start:
            if letter == '*' and current_node.value == self.root:
                break
            if letter not in current_node.child_values:
                raise ValueError("that sequence of letters is not in the tree")
            else:
                index = current_node.child_values.index(letter)
                current_node = current_node.children[index]
        to_visit = []
        to_visit.append(current_node)
        current_node = None
        values = []
        while current_node or to_visit:
            if not current_node:
                current_node = to_visit.pop()
            else:
                # pdb.set_trace()
                if current_node.value != '$':
                    yield current_node.value
                    values.append(current_node.value)
                for node in current_node.children:
                    to_visit.append(node)
                # to_visit.extend([current_node.right, current_node.left])
                if to_visit:
                    current_node = to_visit.pop()
                else:
                    current_node = None
