"""Test file for quick sort."""
from quick_sort import quick_sort


def test_quicksort_first_part():
    """Test quicksort seperates into larger and smaller."""
    input = [6, 44, 38, 5, 47, 15, 36, 26, 27, 2]
    output = quick_sort(input)
    assert output == [2, 5, 6, 15, 26, 27, 36, 38, 44, 47]


def test_quicksort_part_lenght_1():
    """Test quicksort seperates into larger and smaller."""
    input = [2]
    assert quick_sort(input) == [2]


def test_quicksort_length_2():
    """Test quicksort seperates into larger and smaller."""
    input = [20, 3]
    assert quick_sort(input) == [3, 20]


def test_quicksort_in_order():
    """Test quicksort works on an in order list."""
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert quick_sort(input) == input


def test_quicksort_in_reversed_order():
    """Test quicksort works on an in order list."""
    output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    input = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert quick_sort(input) == output


def test_quicksort_giant_list():
    """Test quicksort on a big ass list."""
    import random
    input = []
    for i in range(1000001):
        input.append(random.randint(0, 1000001))
    sorted_list = sorted(input)
    assert quick_sort(input) == sorted_list
