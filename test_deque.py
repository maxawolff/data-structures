"""Test dequeue."""
from dequeue import Deque
import pytest


@pytest.fixture
def new_dequeue():
    """Make an empty dequeue."""
    return Deque()


def test_dequeue(new_dequeue):
    """Test append to tail."""
    new_dequeue.append(2)
    print(new_dequeue)
    assert new_dequeue.tail.val == 2
