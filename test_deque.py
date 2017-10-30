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


def test_pop_removes_tail(dq):
    """Test_pop_removes_tail."""
    dq.append(2)
    dq.append(1)
    dq.append(3)
    assert dq.pop() == 3


def test_pop_raises_error_with_empty_deque(dq):
    """Raise an index error when pop from empty deque."""
    with pytest.raises(IndexError):
        dq.pop()


def test_popleft_returns_head(dq):
    """Pop should remove and return head."""
    dq.append(2)
    dq.append(1)
    dq.append(3)
    assert dq.popleft() == 2
