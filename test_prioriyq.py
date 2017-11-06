"""Test Priorityq."""

from priorityq import Priorityq
import pytest
from que_ import Queue


@pytest.fixture
def pq():
    """."""
    return Priorityq()


# def test_append_different_priorities(pq):
#     """."""
#     pq.insert(1, 2)
#     pq.insert(0, 10)
#     assert pq.tail.val == 1
#
#
# def test_append_different_priorities_2(pq):
#     """."""
#     pq.insert(1, 2)
#     pq.insert(0, 10)
#     assert pq.head.val == 0
#
#
# def test_append_different_priorities_3(pq):
#     """."""
#     pq.insert(1, 2)
#     pq.insert(0, 10)
#     pq.insert(40, 100)
#     assert pq.head.val == 40

# def test_peek_returns_propper_head(pq):
#     """."""
#     pq.insert(1, 0)
#     pq.insert(2, 1)
#     pq.insert(13, 1)
#     pq.insert(12, 2)
#     pq.insert(40, 2)
#     pq.insert(0, 10)
#     print('pq', pq.display())
#     assert pq.head.val == 0


def test_queue_has_priority():
    """Queue should have priority attribute."""
    q = Queue(3)
    assert q.priority == 3
