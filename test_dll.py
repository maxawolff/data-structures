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
