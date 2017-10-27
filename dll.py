"""Implementation of double linked list."""

from linked_list import LinkedList, Node


class DLL(LinkedList):
    """Double linked list."""

    def __init__(self, iterable=None):
        """On list creation set tail to none."""
        super(DLL, self).__init__()
        self.tail = None
        if isinstance(iterable, (str, tuple, list)):
            for i in iterable:
                self.push(i)

    def push(self, val):
        """Add new item to the head of the double linked list."""
        # super(DLL, self).push(val)
        if self.head is None:
            self.head = Node(val, self.head)
            self.tail = self.head
        else:
            orig_head = self.head
            self.head = Node(val, self.head)
            orig_head.prev = self.head
        self.length += 1

    def append(self, val):
        """Add new item to the head of the double linked list."""
        # super(DLL, self).push(val)
        if self.tail is None:
            self.tail = Node(val)
            self.head = self.tail
        else:
            new_node = Node(val)
            orig_tail = self.tail
            self.tail = new_node
            self.tail.prev = orig_tail
            orig_tail.next = self.tail
        self.length += 1

    def pop(self):
        """Remove and return the head."""
        if self.head is None:
            raise IndexError("List is empty, cannot pop from an empty list")
        val = self.head.val
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        return val

    def shift(self):
        """Remove and return the tail."""
        if self.head is None:
            raise IndexError("List is empty, cannot pop from an empty list")
        val = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        return val

    def remove(self, val):
        """Remove selected node."""
        if not val:
            raise ValueError("No value was given")

        if not self.head and not self.tail:
            raise IndexError("List is empty")
        current = self.head
        while current:
            if current.val == val:
                if current.prev:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:
                    self.head = current.next
                    current.next.prev = None
            current = current.next
        self.length -= 1
