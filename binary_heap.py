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
        for idx, item in enumerate(self.container):
            try:
                if item < self.container[count1]:
                    old_val = item
                    self.container[idx] = self.container[count1]
                    self.container[count1] = old_val
                elif item < self.container[count2]:
                    old_val = item
                    self.container[idx] = self.container[count2]
                    self.container[count2] = old_val
            except IndexError:
                pass
