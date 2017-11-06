"""."""

from dll import DLL
from que_ import Queue


class Priorityq(DLL):
    """Class for priority queue."""

    def __init__(self):
        """Make a priority que."""
        self._priority = []
        self.lowest = 0

    def insert(self, val, priority=None):
        """."""
        if not priority:
            priority = self.lowest
        if priority < self.lowest:
            self.lowest = priority
        for queue in self._priority:
            if priority == queue.priority:
                queue.enqueue(val)
                return
        q = Queue(priority)
        q.enqueue(val)
        self._priority.append(q)

    def peek(self):
        """."""
        return self.head.val
