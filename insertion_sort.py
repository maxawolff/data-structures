"""Insertion sort."""
import pdb


def insertion_sort(l):
    """."""
    l_copy = l[::]
    end_point = 0
    while end_point < len(l) - 1:
        end_point += 1
        for i in range(end_point, 0, -1):
            if l_copy[i] < l_copy[i - 1]:
                l_copy[i], l_copy[i - 1] = l_copy[i - 1], l_copy[i]
            else:
                break
    return l_copy
