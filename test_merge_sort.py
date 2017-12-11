from merge_sort import merge_sort, _sort

# def test_length():
#     a = [1, 2, 3, 4, 5]
#     assert 2 == merge_sort(a)


def test_sort_two_lists_of_2():
    """Test helper method sorts two lists length 2."""
    l1 = [1, 2]
    l2 = [3, 4]
    new_list = _sort(l1, l2)
    assert new_list == [1, 2, 3, 4]


def test_sort_two_lists_of_2_different_set():
    """Test helper method sorts two lists length 2."""
    l1 = [1, 4]
    l2 = [2, 3]
    new_list = _sort(l1, l2)
    assert new_list == [1, 2, 3, 4]


def test_sort_different_sizes():
    """Test helper method sorts two lists length 2."""
    l1 = [1, 2]
    l2 = [3]
    new_list = _sort(l1, l2)
    assert new_list == [1, 2, 3]


def test_sort_different_sizes_2():
    """Test helper method sorts two lists length 2."""
    l1 = [1, 9]
    l2 = [3]
    new_list = _sort(l1, l2)
    assert new_list == [1, 3, 9]


def test_sort_length_1():
    """Test helper method sorts two lists length 2."""
    l1 = [9]
    l2 = [3]
    new_list = _sort(l1, l2)
    assert new_list == [3, 9]


def test_sort_length_greater_than_2():
    """Test helper method sorts two lists length 2."""
    l1 = [4, 5, 6]
    l2 = [1, 2, 3]
    new_list = _sort(l1, l2)
    assert new_list == [1, 2, 3, 4, 5, 6]
