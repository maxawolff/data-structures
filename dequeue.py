"""Deque."""
from dll import DLL


class Deque(DLL):
    """Make a dequeue."""

    def appendleft(self, val):
        """Add new node to head of dequeue."""
        super(Deque, self).push(val)

    def pop(self):
        """Remove a value at end of dequeue and return value."""
        return super(Deque, self).shift()
