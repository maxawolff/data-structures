"""Merge sort."""

final_list = []


def merge_sort(l):
    """."""
    half = int(len(l) / 2)
    l1 = l[0:half]
    l2 = l[half:]
    if len(l1) > 1:
        l1 = merge_sort(l1)
    if len(l2) > 1:
        l2 = merge_sort(l2)
    return _sort(l1, l2)


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
