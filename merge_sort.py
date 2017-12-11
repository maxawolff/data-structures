"""Merge sort."""

final_list = []


def merge_sort(l):
    """."""
    l_copy = l[::]
    length = len(l_copy)
    while length > 4:
        length /= 2
        length = int(length)
    container = []
    for i in range(0, len(l_copy), length):
        container.append(l_copy[i:i+length])


def _sort(l1, l2):
    """Sort two lists of lenght 1 or 2."""
    return_list = []
    while l1 or l2:
        if l1[0] > l2[0]:
            return_list.append(l2.pop(0))
        else:
            return_list.append(l1.pop(0))
        if not l1:
            return_list += l2
            return return_list
        if not l2:
            return_list += l1
            return return_list