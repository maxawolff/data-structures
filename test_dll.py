"""Test double linked list."""

import pytest
from dll import DLL


@pytest.fixture
def new_dll():
    """Create a new double linked list."""
    new_dll = DLL()
    return new_dll


def test_dll_on_init_has_tail(new_dll):
    """Test_dll_on_init_has_tail."""
    assert hasattr(new_dll, 'tail')


def test_push_to_dll(new_dll):
    """Test to for push method."""
    new_dll.push(2)
    assert new_dll.head.val == 2
