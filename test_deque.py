"""Test dequeue."""
from dequeue import Deque
import pytest


@pytest.fixture
def dq():
    """Make an empty dequeue."""
    return Deque()


def test_dequeue(dq):
    """Test append to tail."""
    dq.append(2)
    print(dq)
    assert dq.tail.val == 2


def test_append_left(dq):
    """Test that append left adds value to the head."""
    dq.appendleft(1)
    dq.appendleft(2)
    assert dq.head.val == 2
