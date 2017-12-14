"""Test file for quick sort."""
from quick_sort import quick_sort


def test_quicksort_first_part():
    """Test quicksort seperates into larger and smaller."""
    input = [6, 44, 38, 5, 47, 15, 36, 26, 27, 2]
    output = quick_sort(input, 0, 10)
    assert output == [2, 5, 6, 44, 47, 15, 36, 26, 27, 38]


def test_quicksort_part_2():
    """Test quicksort seperates into larger and smaller."""
    input = [2, 5, 6, 44, 47, 15, 36, 26, 27, 38]
    output = quick_sort(input, 0, 2)
    assert output == [2, 5, 6, 44, 47, 15, 36, 26, 27, 38]


def test_quicksort_part_3():
    """Test quicksort seperates into larger and smaller."""
    input = [2, 5, 6, 44, 47, 15, 36, 26, 27, 38]
    output = quick_sort(input, 1, 2)
    assert output == [2, 5, 6, 44, 47, 15, 36, 26, 27, 38]
