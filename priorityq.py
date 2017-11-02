"""."""

from dll import DLL


class Priorityq(DLL):
    """."""

    def insert(self, val, priority):
        """."""
        super(Priorityq, self).append(val, priority=priority)
        import pdb  # pdb.set_trace()
        if self.length > 1:
            current = self.tail

            while current.prev_node:
                if current.prev_node.priority < current.priority:
                    old_prev = current.prev_node
                    old_prev, current = current, old_prev
                    if old_prev == self.tail:

                        self.tail = current
                    if current.prev_node is None:
                        self.head = old_prev
                    current = old_prev.prev_node
                    pdb.set_trace()
                else:
                    break

    def peek(self):
        """."""
        return self.head.val
