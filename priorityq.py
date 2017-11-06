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
        if current == self.head:
            return
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
        count = 0
        # pdb.set_trace()
        while current.prev_node:
            # pdb.set_trace()
            if current.prev_node.priority < current.priority:
                # pdb.set_trace()
                count += 1
                print('in while loop, count is ', count)
                old_prev = current.prev_node
                # old_prev, current = current, old_prev
                if current.next_node is None:  # current is tail
                    old_prev.next_node = None
                    if current.prev_node.prev_node:
                        current.next_node = old_prev
                        old_prev.prev_node.next_node = current
                        current.prev_node = current.prev_node.prev_node
                        old_prev.prev_node = current
                        current.next_node = old_prev
                        self.tail = old_prev
                        current = current.prev_node  # current is being reasigned to incorect value
                        print(self, 'in if current.next is none')
                        continue
                    else:
                        return
                elif current.prev_node.prev_node:
                    current.next_node.prev_node = old_prev
                    current.prev_node = old_prev.prev_node
                    old_prev.prev_node.next_node = current
                    old_prev.prev_node = current
                    current.next_node = old_prev
                    old_prev.next_node = old_prev.next_node.next_node
                    current = current.prev_node
                    print(self, "haven't hit head yet")
                    continue
                elif current.prev_node.prev_node is None:
                    current.next_node.prev_node = old_prev
                    current.prev_node = None
                    old_prev.prev_node = current
                    current.next_node = old_prev
                    old_prev.next_node = old_prev.next_node.next_node
                    self.head = current
                    print(self, 'just reasigned head')
                    return
                else:
                    return
            else:
                return

    def peek(self):
        """."""
        return self.head.val
