"""Test file for radix sort."""

from radix_sort import radix_sort
import pytest


def test_radix_sort1():
    """Test some stuff."""
    input = [3221, 1, 10, 9680, 577, 9420, 7, 5622, 4793, 2030]
    output = sorted(input)
    assert radix_sort(input) == output


def test_radix_sort_bad_input():
    """Assert type error on bad input type."""
    with pytest.raises(TypeError):
        radix_sort(3)


def test_radix_sort_one_item():
    """Test radix sort with one item in list."""
    assert radix_sort([2]) == [2]


def test_radix_sort_same_num_digits():
    """Test radix sort with all numbers having the same amoutn of digits."""
    input = [100, 398, 530, 111, 948, 632, 243, 545, 101]
    assert radix_sort(input) == sorted(input)


def test_radix_sort_in_order():
    """An in order list should stay in order."""
    input = [1, 2, 3, 4, 100]
    assert radix_sort(input) == input


def test_radix_sort_reversed_order():
    """A backwards list should sort properly."""
    input = [10000, 1000, 100, 10, 1]
    assert radix_sort(input) == sorted(input)


def test_radix_sort_random_list():
    """A random list should sort properly."""
    import random
    input = []
    for i in range(100000):
        input.append(random.randint(0, 1000001))
    sorted_list = sorted(input)
    assert radix_sort(input) == sorted_list
