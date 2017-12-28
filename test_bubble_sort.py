"""Tests for bubble sort."""
from bubble_sort import bubble_sort


def test_bubble_sort_sorted_list():
    """Test that bubble sort doesn't change sorted order."""
    l = [1, 2, 3, 4, 5]
    sorted_l = bubble_sort(l)
    assert l == sorted_l


def test_bubble_sort_works_medium_shuffled():
    """Testing bubble sort on a bigger, slightly out of order list."""
    l = [3, 8, 1, 6, 7, 12, 9]
    sorted_l = bubble_sort(l)
    assert sorted(l) == sorted_l


def test_bubble_sort_reversed_list():
    """Testing bubble sort on a bigger, slightly out of order list."""
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 50, 100, 300, 1000]
    reversed_l = l[::-1]
    sorted_l = bubble_sort(reversed_l)
    assert l == sorted_l


def test_bubble_sort_works_alphabetically():
    """Does this work with strings."""
    l = ["a", "b", "c", "d", "e"]
    sorted_l = bubble_sort(l)
    assert l == sorted_l
