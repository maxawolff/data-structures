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
        if current.prev_node is self.head:
            if current.prev_node.priority < current.priority:
                old_prev = current.prev_node
                current.next_node = old_prev
                current.prev_node = None
                old_prev.next_node = None

                old_prev.prev_node = current
                self.tail = old_prev
                self.head = current
                return

        while current.prev_node:
            if current.prev_node.priority < current.priority:
                # pdb.set_trace()
                old_prev = current.prev_node
                # old_prev, current = current, old_prev
                if current.next_node is None:  # current is tail
                    old_prev.next_node = None
                    if old_prev.prev_node:
                        current.next_node = old_prev
                        old_prev.prev_node.next_node = current
                        current.prev_node = current.prev_node.prev_node
                        old_prev.prev_node = current
                        current.next_node = old_prev
                        self.tail = old_prev
                        current = current.prev_node
                        continue
                # elif current.prev_node is None:

                    else:
                        current.prev_node = None
                        self.head = current
                        break
                elif old_prev.prev_node:
                        current.prev_node = old_prev.prev_node
                        old_prev.prev_node = current
                        current.next_node = old_prev
                        continue
                        # self.tail = old_prev
                else:
                    current = current.prev_node
                #     # current.prev_node = None
                #     # self.head = current
                    continue
            else:
                break

    def peek(self):
        """."""
        return self.head.val
