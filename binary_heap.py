"""Implementation of binary search tree."""


class Binheap(object):
    """Binary search tree."""

    def __init__(self):
        """."""
        self.container = []
        self._tailidx = -1

    def push(self, val):
        """Add new value."""
        self._tailidx += 1
        if self._tailidx < len(self.container):
            self.container[self._tailidx] = val
        else:
            self.container.append(val)
        self._shiftup(self._tailidx)
        # self.container.append(val)
        # count1 = 1
        # count2 = 2
        # idx = 0
        # while True:
        #     while idx < len(self.container):
        #         item = self.container[idx]
        #         try:
        #             if item < self.container[count1 + idx]:
        #                 old_val = item
        #                 self.container[idx] = self.container[count1 + idx]
        #                 self.container[count1 + idx] = old_val
        #                 idx = 0
        #                 count1 = 1
        #                 count2 = 2
        #                 continue
        #             elif item < self.container[count2 + idx]:
        #                 old_val = item
        #                 self.container[idx] = self.container[count2 + idx]
        #                 self.container[count2 + idx] = old_val
        #                 idx = 0
        #                 count1 = 1
        #                 count2 = 2
        #                 continue
        #             count1 += 1
        #             count2 += 1
        #             idx += 1
        #         except IndexError:
        #             return

    def pop(self):
        """Remove head by bubbling down and removing and returning the val."""
        if self.container == []:
            raise IndexError('Cannot pop from an empty list')

        while self.container:
            pass

    def _shiftup(self, idx):
        while idx > 0:
            parent_idx, parent_val = self._parent(idx)
            if parent_val <= self.container[idx]:
                break
            self.container[parent_idx], self.container[idx] = self.container[idx], self.container[parent_idx]
            idx = parent_idx

    def _parent(self, idx):
        if idx == 0:
            return None, None

        parent_idx = (idx - 1) // 2
        return parent_idx, self.container[parent_idx]

    def _leftchild(self, idx):
        child_idx = 2 * idx + 1
        if child_idx > len(self.container) - 1:
            return None, None
        return child_idx, self.container[child_idx]

    def _rightchild(self, idx):
        child_idx = 2 * idx + 2
        if child_idx > len(self.container) - 1:
            return None, None
        return child_idx, self.container[child_idx]
