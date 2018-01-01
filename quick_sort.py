"""Quick sort."""

done = []


def quick_sort(input):
    """Sort a list using the quick sort algorith."""
    if not isinstance(input, list):
        raise TypeError("input must be a list")
    if len(input) == 1:
        return input
    left = 0
    right = 0
    for i in range(len(input)):
        if right == 0 and input[i] > input[0]:
            right = i
        elif input[i] <= input[0]:
            left = i
        if left > right:
            input[left], input[right] = input[right], input[left]
            left = right
            right += 1
    input[0], input[left] = input[left], input[0]
    left_list = input[:left]
    if len(left_list) > 1:
        left_list = quick_sort(left_list)
    middle_list = [input[left]]
    right_list = input[left + 1:]
    if len(right_list) > 1:
        right_list = quick_sort(right_list)
    return left_list + middle_list + right_list
