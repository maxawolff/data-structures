"""Test Priorityq."""

from priorityq import Priorityq
import pytest
from que_ import Queue
import pdb


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


def test_q_insert_1(pq):
    """."""
    pq.insert(1, 1)
    assert pq._priority[0].priority == 1


def test_q_insert_2(pq):
    """."""
    pq.insert(1, 1)
    pq.insert(2, 1)
    assert len(pq._priority[0]) == 2


def test_q_insert_2_priorities(pq):
    """."""
    pq.insert(1, 1)
    pq.insert(2, 0)
    assert len(pq._priority) == 2


def test_q_insert_2nodes_1_priority_default(pq):
    """."""
    pq.insert(1, 1)
    pq.insert(2)
    assert len(pq._priority) == 2


def test_q_insert_lower_priority(pq):
    """."""
    pq.insert(1, 1)
    pq.insert(1, -1)
    assert pq.lowest == -1


def test_queue_inserted_correct_order(pq):
    """."""
    pq.insert(1, 1)
    pq.insert(1, 10)
    assert pq._priority[0].priority == 10


def test_queue_inserted_correct_order_2(pq):
    """."""
    pq.insert(1, 10)
    pq.insert(1, 1)
    assert pq._priority[0].priority == 10


def test_peek_empty_priorityq(pq):
    """."""
    assert pq.peek() is None


def test_peek_several_vals(pq):
    """."""
    pq.insert(1, 1)
    pq.insert(2, 5)
    assert pq.peek() == 2


def test_empty_priorityq_pop(pq):
    """."""
    with pytest.raises(IndexError):
        pq.pop()


def test_list_pop(pq):
    """."""
    pq.insert(1, 1)
    pq.insert(2, 5)
    assert pq.pop() == 2


def test_list_pop(pq):
    """."""
    pq.insert(1, 1)
    pq.insert(2, 5)
    pq.pop()
    # pdb.set_trace()
    assert len(pq._priority) == 1
