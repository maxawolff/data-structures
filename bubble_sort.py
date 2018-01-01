"""Bubble sort."""


def bubble_sort(l):
    """."""
    l_copy = l[::]
    end_point = len(l) - 1
    while end_point:
        for i in range(0, end_point):
            if l_copy[i] > l_copy[i + 1]:
                l_copy[i], l_copy[i + 1] = l_copy[i + 1], l_copy[i]
        end_point -= 1
    return l_copy
