from que_ import Queue
from math import log10
import pdb


def radix_sort(input):
    """Sort a list using radix sort."""
    if not isinstance(input, list):
        raise TypeError("Input must be a list")
    container = []
    largest = -1
    for num in input:
        if num > largest:
            largest = num
    length = int(log10(largest)) + 1
    for num in input:
        str_num = str(num)
        str_num_list = []
        for digit in str_num:
            str_num_list.append(int(digit))
        str_num_list = str_num_list[::-1]
        for i in range(0, length):
            try:
                str_num_list[i]
            except IndexError:
                str_num_list.append(0)
        container.append(str_num_list)
    for i in range(0, length):
        bucket_list = []
        for j in range(0, 10):
            q = Queue()
            q.enqueue(j)
            bucket_list.append(q)
        for num in container:
            digit = num[i]
            bucket_list[digit].enqueue(num)
        container = []
        for bucket in bucket_list:
            bucket.dequeue()
            while bucket:
                container.append(bucket.dequeue())
    return_list = []
    for num_list in container:
        multiplier = 1
        number = 0
        for num in num_list:
            number += (num * multiplier)
            multiplier *= 10
        return_list.append(number)
    return return_list
