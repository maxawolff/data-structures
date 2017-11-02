"""."""

from dll import DLL


class Priorityq(DLL):
    """."""

    def insert(self, val, priority):
        """."""
        super(Priorityq, self).append(val, priority=priority)
        import pdb  # pdb.set_trace()
        # if self.length > 1:
        #     current = self.tail
        current = self.tail
        while current.prev_node:
            pdb.set_trace()
            if current.prev_node.priority < current.priority:
                old_prev = current.prev_node
                # old_prev, current = current, old_prev
                if current.next_node is None:  # current is tail
                    old_prev.next_node = None
                    self.tail = old_prev
                    current.next_node = old_prev
                    if old_prev.prev_node:
                        current.prev_node = old_prev.prev_node
                        current = current.prev_node
                        continue
                    else:
                        current.prev_node = None
                        self.head = current
                        break
                else:
                    current.next_node = old_prev
                    if old_prev.prev_node:
                        current.prev_node = old_prev.prev_node
                        current = current.prev_node
                        continue
                    else:
                        current.prev_node = None
                        self.head = current
                        break

                #     old_prev.prev_node = current
                #     if
                #     self.tail = old_prev
                # if current.prev_node is None: # current is head
                #     old_prev.prev_node = None
                #     self.head = old_prev
                # current.next_node = old_prev
                # old_prev.prev_node = current
                # current = old_prev.prev_node
            else:
                break

    def peek(self):
        """."""
        return self.head.val
