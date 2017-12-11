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


if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    import random
    sort_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    sort_2 = [8, 7, 6, 5, 4, 3, 2, 1]
    sort_3 = []
    for i in range(0, 9):
        sort_3.append(random.randint(0, 9))

    time_1 = ti.timeit("bubble_sort(sort_1[:])",
                       setup="from __main__ import sort_1, bubble_sort")
    time_2 = ti.timeit("bubble_sort(sort_2[:])",
                       setup="from __main__ import sort_2, bubble_sort")
    time_3 = ti.timeit("bubble_sort(sort_3[:])",
                       setup="from __main__ import sort_3, bubble_sort")
    print("""
        Input: sorted list
        Good case: {}
        Input: revevrsed list
        Bad case: {}
        Input: random list
        average case: {}""".format(time_1, time_2, time_3))