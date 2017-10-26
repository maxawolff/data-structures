"""Implementation of double linked list."""

from linked_list import LinkedList, Node


class DLL(LinkedList):
    """Double linked list."""

    def __init__(self):
        """On list creation set tail to none."""
        super(DLL, self).__init__()
        self.tail = None

    def push(self, val):
        """Add new item to the head of the double linked list."""
        # super(DLL, self).push(val)
        if not self.head:
            orig_head = self.head
            self.head = Node(val, self.head)
            orig_head.prev = self.head
        else:
            self.head = Node(val, self.head)

        self.length += 1

    def pop(self):
        """Remove and return the head."""
        return super(DLL, self).pop()

    def remove(self, node):
        """Remove selected node."""
        current = self.head
        node_to_remove = None
        while current:
            if current.next.val == node:
                node_to_remove = current.next
                self.length -= 1
                current.next = current.next.next
                current.prev = current.prev.prev
            current = current.next

        if node_to_remove is None:
            raise IndexError("Node was not found in list")
