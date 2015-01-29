#!/usr/bin/env python
__author__ = 'kevin'

def heap_sort(array):
    n = len(array)
    first = int(n / 2 - 1)
    for start in range(first, -1, -1):
        max_heapify(array, start, n - 1)

    for end in range(n - 1, 0, -1):
        array[end], array[0] = array[0], array[end]
        max_heapify(array, 0, end - 1)

    return array

def max_heapify(array, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break

        if child + 1 <= end and array[child] < array[child + 1]:
            child = child + 1

        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break

    print root
    print array


if __name__ == "__main__":
    array = [6, 5, 3, 1, 8, 7, 2, 4]
    print '##########original: '
    print array

    print '##########after sort: '
    print heap_sort(array)