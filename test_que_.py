"""Test for queue module."""

from que_ import Queue
import pytest


@pytest.fixture
def new_queue():
    """."""
    q = Queue()
    return q


@pytest.fixture
def full_q():
    """Make q with stuff in it."""
    q = Queue([4, 3, 2, 1])
    return q


def test_enqueue(new_queue):
    """."""
    new_queue.enqueue(2)
    print(new_queue)
    assert new_queue.tail.val == 2


def test_multiple_enqueues(new_queue):
    """."""
    new_queue.enqueue(2)
    new_queue.enqueue(4)
    print(new_queue)
    assert new_queue.head.val == 2 and new_queue.tail.val == 4


def test_dequeue_returns_and_deletes_head(new_queue):
    """Test_dequeue_returns_and_deletes_head."""
    new_queue.enqueue(2)
    new_queue.enqueue(4)
    assert new_queue.dequeue() == 2
