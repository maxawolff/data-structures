from que_ import Queue
from math import log10


def radix_sort(input):
    """Sort a list using radix sort."""
    if not isinstance(input, list):
        raise TypeError("I only take lists dawg, gimme a list as input")
    container = []
    largest = -1
    for num in input:
        if num > largest:
            largest = num
    length = int(log10(largest))
    for num in input:
        container.append(list(map(int, str(num)))[::-1])
    return container
