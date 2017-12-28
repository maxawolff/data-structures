"""Implementation of a binary search tree."""

import pdb


class Node(object):
    """Node class for binary search tree."""

    def __init__(self, value, left=None, right=None, depth=0, parent=None):
        """."""
        self.value = value
        self.left = left
        self.right = right
        self.depth = depth
        self.parent = parent
        self.balance_factor = 0
        self.lsd = 1  # left sub depth
        self.rsd = 1

    @property
    def balance(self):
        """Return the balance factor."""
        return self.rsd - self.lsd


class BST(object):
    """Binary search tree."""

    def __init__(self, iterable=None):
        """."""
        self.head = None
        self.left_depth = 0
        self.right_depth = 0
        self._depth = 0
        self.nodes = []

    def insert(self, val):
        """Add a node into the bst."""
        direction = ''
        if self.head is None:
            new_node = Node(val, depth=1)
            self.head = new_node
            self._depth = 1
            self.nodes.append(new_node)
            self.left_depth = 1
            self.right_depth = 1
        current_node = self.head
        if val == self.head.value:
            return
        parent = self.head
        current_depth = 2
        while True:
            if val < current_node.value:
                if current_depth == 2:
                    direction = 'left'
                if current_node.left:
                    current_node = current_node.left
                    parent = current_node
                    current_depth += 1
                else:
                    new_node = Node(val, depth=current_depth, parent=parent)
                    current_node.left = new_node
                    self.nodes.append(new_node)
                    if current_depth > self._depth:
                        self._depth = current_depth
                    if direction == 'left' and self.left_depth < current_depth:
                        self.left_depth = current_depth
                    elif direction == 'right' and self.right_depth < current_depth:
                        self.right_depth = current_depth
                    self._adjust_depth(new_node)
                    return
            elif val > current_node.value:
                if current_depth == 2:
                    direction = 'right'
                if current_node.right:
                    current_node = current_node.right
                    parent = current_node
                    current_depth += 1
                else:
                    new_node = Node(val, depth=current_depth, parent=parent)
                    current_node.right = new_node
                    self.nodes.append(new_node)
                    if current_depth > self._depth:
                        self._depth = current_depth
                    if direction == 'right' and self.right_depth < current_depth:
                        self.right_depth = current_depth
                    elif direction == 'left' and self.left_depth < current_depth:
                        self.left_depth = current_depth
                    self._adjust_depth(new_node)
                    return
            elif val == current_node.value:
                return

    def search(self, val):
        """."""
        for node in self.nodes:
            if node.value == val:
                return node

    def depth(self):
        """Return the depth of a bst."""
        return self._depth

    def contains(self, val):
        """Return true if val is a node in bst."""
        if self.search(val):
            return True
        else:
            return False

    def balance(self):
        """Return balance of tree."""
        return self.left_depth - self.right_depth

    def breadth_first(self):
        """Traverse the bst in breadth first order, returns generator."""
        if not self.head:
            yield
        to_visit = []
        to_visit.append(self.head)
        current_node = self.head
        while to_visit:
            if current_node.left:
                to_visit.append(current_node.left)
            if current_node.right:
                to_visit.append(current_node.right)
            yield current_node.value
            to_visit.pop(0)
            # pdb.set_trace()
            if to_visit:
                current_node = to_visit[0]

    def pre_order(self):
        """Traverse the bst in pre-order, returns generator."""
        to_visit = []
        to_visit.append(self.head)
        current = None
        while to_visit or current:
            if not current:
                current = to_visit.pop()
            else:
                yield current.value
                to_visit.extend([current.right, current.left])
                current = to_visit.pop()

    def in_order(self):
        """Traverse the bst in-order, returns generator."""
        to_visit = []
        current = self.head
        while current or to_visit:
            if current:
                to_visit.append(current)
                current = current.left
            else:
                current = to_visit.pop()
                yield current.value
                current = current.right

    def post_order(self):
        """Traverse the bst in post_order, returns generator."""
        to_visit = []
        current = self.head
        while current or to_visit:
            if current:
                if current.right:
                    to_visit.append(current.right)
                to_visit.append(current)
                current = current.left
            else:
                current = to_visit.pop()
                if to_visit and current.right == to_visit[-1]:
                    to_visit.pop()
                    to_visit.append(current)
                    current = current.right
                else:
                    yield current.value
                    current = None

    def delete(self, val):
        """Delete a node of a given value from the bst.

        Replace deleted node with closest number to deleted node
        left most child of right neighbor, not right neighbor
        rather than a direction, compate parent.value to del_node value
        update depth before deletion
        """
        del_node = self.search(val)
        if del_node is None:
            raise ValueError("No node of the given value")
        if del_node == self.head:
            self.head = del_node.right
            fld = self._fld(del_node.right)
            if fld is None:
                fld = del_node.right
            fld.left = del_node.left
            del_node.left.parent = fld
            return
        direction = ""
        if del_node.parent.right is del_node:
            direction = "right"
        else:
            direction = "left"
        if direction == "right":
            if del_node.right is None and del_node.left is None:
                """Del Node has no children."""
                del_node.parent.right = None
                del_node.parent = None
            elif del_node.right and not del_node.left:
                """Del Node has only right child."""
                del_node.parent.right = del_node.right
                del_node.right.parent = del_node.parent
            elif del_node.left and not del_node.right:
                """Del Node has only left child."""
                del_node.parent.right = del_node.left
                del_node.left.parent = del_node.parent
            else:
                """Del Node has both left and right children."""
                del_node.parent.right = del_node.right
                del_node.right.parent = del_node.parent
                fld = self._fld(del_node.right)
                if fld is None:
                    fld = del_node.right
                fld.left = del_node.left
                del_node.left.parent = fld
        if direction == "left":
            if del_node.right is None and del_node.left is None:
                """Del Node has no children."""
                del_node.parent.left = None
                del_node.parent = None
            elif del_node.right and not del_node.left:
                """Del Node has only right child."""
                del_node.parent.left = del_node.right
                del_node.right.parent = del_node.parent
            elif del_node.left and not del_node.right:
                """Del Node has only left child."""
                del_node.parent.left = del_node.left
                del_node.left.parent = del_node.parent
            else:
                """Del Node has both left and right children."""
                del_node.parent.left = del_node.right
                del_node.right.parent = del_node.parent
                fld = self._fld(del_node.right)
                if fld is None:
                    fld = del_node.right
                fld.left = del_node.left
                del_node.left.parent = fld
        self.nodes.remove(del_node)

    def _fld(self, node):
        """Find the furthers left descendent of a given node."""
        node = self.search(node.value)
        if not node:
            raise ValueError("no node of the given value")
        fld = None
        while node.left:
            fld = node.left
            node = node.left
        return fld

    def _adjust_balance_factor(self, node):
        """Adjust the balance factor of all nodes affected by an insertion or deletion."""
        if node.parent.left is None or node.parent.right is None:
            while node.parent:
                parent = node.parent
                if parent.left == node:
                    parent.balance_factor -= 1
                else:
                    parent.balance_factor += 1
                node = node.parent
                if node.balance_factor == -2:
                    pdb.set_trace()
                    self._left_rotation(node)
                    node = node.parent
        else:
            if node.parent.left == node:
                node.parent.balance_factor -= 1
            else:
                node.parent.balance_factor += 1

    def _adjust_depth(self, node):
        """Adjust the left or right depth of a given node's sub-tree."""
        if node.parent.left is None or node.parent.right is None:
            count = 1
            while node.parent:
                # parent = node.parent
                if node.parent.right is None:
                    node.parent.lsd += 1
                elif node.parent.left is None:
                    node.parent.rsd += 1
                node = node.parent
        #         if parent.left == node:
        #             parent.rsd += 1
        #         if parent.right == node:
        #             parent.lsd += 1
        #         node = node.parent
        #         count += 1
        else:
            if node.parent.right == node:
                node.parent.rsd += 1
            else:
                node.parent.lsd += 1

    def _left_rotation(self, node):
        """Perform a left rotation."""
        parent = node.parent
        child = node.left
        gc = child.left
        parent.left = child
        child.parent = parent
        node.parent = child
        node.left = None
        node.balance_factor = 0
        child.balance_factor = 0
        gc.balance_factor = 0

    def size(self):
        """Return the size of the tree."""
        return len(self.nodes)
