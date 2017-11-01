"""Test Priorityq."""

from priorityq import Priorityq
import pytest


@pytest.fixture
def pq():
    return Priorityq()


def test_append_different_priorities(pq):
    """."""
    pq.insert(1, 2)
    pq.insert(0, 10)
    assert pq.tail.val == 1


def test_append_different_priorities_2(pq):
    """."""
    pq.insert(1, 2)
    pq.insert(0, 10)
    assert pq.head.val == 0


def test_append_different_priorities_3(pq):
    """."""
    pq.insert(1, 2)
    pq.insert(0, 10)
    pq.insert(40, 100)
    assert pq.head.val == 40

def test_append_different_priorities_4(pq):
    """."""
    pq.insert(1, 2)
    pq.insert(0, 10)
    pq.insert(40, 100)
    assert pq.tail.val == 1
