from radix_sort import radix_sort


# def test_first_step():
#     """Test list gets turned into list of list of digits."""
#     input = [1, 12, 123, 1234]
#     new_list = radix_sort(input)
#     assert new_list == [[1, 0, 0, 0], [2, 1, 0, 0], [3, 2, 1, 0], [4, 3, 2, 1]]


def test_num_itterations():
    """Test some stuff."""
    input = [3221, 1, 10, 9680, 577, 9420, 7, 5622, 4793, 2030]
    test = radix_sort(input)
    import pdb; pdb.set_trace()


# def test_num_itterations_different_value():
#     """Test some stuff."""
#     input = [1, 12, 123, 1234, 123456789]
#     assert radix_sort(input) == 9