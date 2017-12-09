"""Tests for insertion sort."""
from insertion_sort import insertion_sort


def test_insertion_sort_sorted_list():
    """Test that insertion sort doesn't change sorted order."""
    l = [1, 2, 3, 4, 5]
    sorted_l = insertion_sort(l)
    assert l == sorted_l


def test_insertion_sort_works_medium_shuffled():
    """Testing insertion sort on a bigger, slightly out of order list."""
    l = [3, 8, 1, 6, 7, 12, 9]
    sorted_l = insertion_sort(l)
    assert sorted(l) == sorted_l


def test_insertion_sort_reversed_list():
    """Testing insertion sort on a bigger, slightly out of order list."""
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 50, 100, 300, 1000]
    reversed_l = l[::-1]
    sorted_l = insertion_sort(reversed_l)
    assert l == sorted_l


def test_insertion_sort_works_alphabetically():
    """Does this work with strings."""
    l = ["a", "b", "c", "d", "e"]
    sorted_l = insertion_sort(l)
    assert l == sorted_l
