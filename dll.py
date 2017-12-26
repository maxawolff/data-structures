"""Implementation of double linked list."""

from linked_list import LinkedList, Node
import pdb


class DLL(LinkedList):
    """Double linked list."""

    def __init__(self):
        """On list creation set tail to none."""
        super(DLL, self).__init__()
        self.tail = None

    def push(self, val):
        """Add new item to the head of the double linked list."""
        if self.head is None:
            self.head = Node(val, self.head)
            self.tail = self.head
        else:
            orig_head = self.head
            self.head = Node(val, self.head)
            orig_head.prev_node = self.head
        self.length += 1

    def append(self, val, priority=0):
        """Add new item to the tail of the double linked list."""
        if self.tail is None:
            self.tail = Node(val, priority=priority)
            self.head = self.tail
        else:
            new_node = Node(val, priority=priority)
            orig_tail = self.tail
            self.tail = new_node
            self.tail.prev_node = orig_tail
            orig_tail.next_node = self.tail
        self.length += 1

    def pop(self):
        """Remove and return the head."""
        if self.head is None:
            raise IndexError("List is empty, cannot pop from an empty list")
        val = self.head.val
        if self.head.next_node:
            self.head = self.head.next_node
            self.head.prev_node = None
        else:
            self.head = None
            self.tail = None
        self.length -= 1
        return val

    def shift(self):
        """Remove and return the tail."""
        if self.head is None:
            raise IndexError("List is empty, cannot pop from an empty list")
        val = self.tail.val
        if self.tail.prev_node:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
        else:
            self.head = None
            self.tail = None
        self.length -= 1
        return val

    def remove(self, val):
        """Remove selected node."""
        found = False
        if not self.head and not self.tail:
            raise ValueError("That value is not in the doubly linked list, also the list is empty")
        current = self.head
        while current:
            # pdb.set_trace()
            if current.val == val:
                found = True
                if current.prev_node:
                    current.prev_node.next_node = current.next_node
                    current.next_node.prev_node = current.prev_node
                else:
                    self.head = current.next_node
                    if self.head is None:
                        self.tail = None
                    else:
                        current.next_node.prev_node = None
            current = current.next_node
        if not found:
            raise ValueError("that value is not in the doubly linked list")
        self.length -= 1
