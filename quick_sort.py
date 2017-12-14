"""Quick sort."""

sorted = []


def quick_sort(input, start, end):
    """Sort a list using the quick sort algorith."""
    if not isinstance(input, list):
        raise TypeError("quick sort only works on a list")
    if len(input) == 1:
        return input
    left = 0
    right = 0
    for i in range(1, end):
        if right == 0 and input[i] > input[0]:
            right = i
        elif input[i] <= input[0]:
            left = i
        if left > right:
            input[left], input[right] = input[right], input[left]
            left = right
            right += 1
    input[start], input[left] = input[left], input[start]
    return input
