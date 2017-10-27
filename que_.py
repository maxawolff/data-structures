"""Implementation of a que."""

from dll import DLL
from linked_list import Node


class Queue(DLL):
    """Makes a queue."""

    def enqueue(self, value):
        """Enqueue method for queue."""
        super(Queue, self).append(value)

    def dequeue(self):
        """Remove head and return val."""
        return super(Queue, self).pop()
