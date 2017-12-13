from radix_sort import radix_sort


def test_first_step():
    """Test list gets turned into list of list of digits."""
    input = [1, 12, 123, 1234]
    new_list = radix_sort(input)
    assert new_list == [[1, 0, 0, 0], [2, 1, 0, 0], [3, 2, 1, 0], [4, 3, 2, 1]]
