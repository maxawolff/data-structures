"""Merge sort."""

final_list = []


def merge_sort(l):
    """Sort a list using merge sort."""
    half = int(len(l) / 2)
    l1 = l[0:half]
    l2 = l[half:]
    if len(l1) > 1:
        l1 = merge_sort(l1)
    if len(l2) > 1:
        l2 = merge_sort(l2)
    return _sort(l1, l2)


def _sort(l1, l2):
    """Take two sorted lists and merge them together."""
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


if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    import random
    sort_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    sort_2 = [8, 7, 6, 5, 4, 3, 2, 1]
    sort_3 = []
    for i in range(0, 9):
        sort_3.append(random.randint(0, 9))

    time_1 = ti.timeit("merge_sort(sort_1[:])",
                       setup="from __main__ import sort_1, merge_sort")
    time_2 = ti.timeit("merge_sort(sort_2[:])",
                       setup="from __main__ import sort_2, merge_sort")
    time_3 = ti.timeit("merge_sort(sort_3[:])",
                       setup="from __main__ import sort_3, merge_sort")
    print("""
        Input: sorted list
        Good case: {}
        Input: revevrsed list
        Bad case: {}
        Input: random list
        average case: {}""".format(time_1, time_2, time_3))
