"""Quick sort."""


def quick_sort(input):
    """Sort a list using the quick sort algorith."""
    if not isinstance(input, list):
        raise TypeError("quick sort only works on a list")
    if len(input) == 1:
        return input
    pivot_idx = 0
    left = 0
    right = 0
    for i in range(1, len(input)):
        if right == 0 and input[i] > input[0]:
            right = i
        elif input[i] <= input[0]:
            left = i
        if left > right:
            input[left], input[right] = input[right], input[left]
            left = right
            right += 1
    return input
