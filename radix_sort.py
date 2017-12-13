from que_ import Queue


def radix_sort(input):
    """Sort a list using radix sort."""
    if not isinstance(input, list):
        raise TypeError("I only take lists dawg, gimme a list as input")
    container = []
    for num in input:
        container.append(list(map(int, str(num)))[::-1])
    return container
