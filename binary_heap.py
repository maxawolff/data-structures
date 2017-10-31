"""Implementation of binary search tree."""


class Binheap(object):
    """Binary search tree."""

    def __init__(self):
        """."""
        self.container = []

    def push(self, val):
        """Add new value."""
        self.container.append(val)
        count1 = 1
        count2 = 2
        idx = 0
        while True:
            while idx < len(self.container):
                item = self.container[idx]
                try:
                    if item < self.container[count1 + idx]:
                        old_val = item
                        self.container[idx] = self.container[count1 + idx]
                        self.container[count1 + idx] = old_val
                        idx = 0
                        count1 = 1
                        count2 = 2
                    elif item < self.container[count2 + idx]:
                        old_val = item
                        self.container[idx] = self.container[count2 + idx]
                        self.container[count2 + idx] = old_val
                        idx = 0
                        count1 = 1
                        count2 = 2
                    count1 += 1
                    count2 += 1
                    idx += 1
                except IndexError:
                    return
