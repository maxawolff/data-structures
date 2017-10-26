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
            orig_tail = self.tail
            self.tail = Node(val)
            self.tail.prev = orig_tail
            # self.tail = orig_tail.next
        self.length += 1

    def pop(self):
        """Remove and return the head."""
        return super(DLL, self).pop()

    def remove(self, val):
        """Remove selected node."""
        # if node == self.head.val:
        #     self.head = node.next
        # else:
        #     current = self.head
        #     node_to_remove = None
        #     while current:
        #         if current.next.next is None:
        #             self.tail = current.next
        #             current.next is None
        #         elif current.next.val == node:
        #             node_to_remove = current.next
        #             self.length -= 1
        #             current.next = current.next.next
        #             if current.prev is None:
        #                 pass
        #             else:
        #                 current.prev = current.prev.prev
        #         current = current.next
        if not val:
            raise ValueError("No value was given")

        if not self.head and not self.tail:
            raise IndexError("List is empty")
        current = self.head
        if val == current.val:
            self.head = current.next
            self.length -= 1
        elif current.val == self.tail.val:
            self.tail.prev = None
            self.length -= 1
        else:
            while current.next:
                if current.val == val:
                    print('current.val in while: ', current.val)
                    current.prev.next = current.next
                    self.length -= 1
                    break
                current = current.next
