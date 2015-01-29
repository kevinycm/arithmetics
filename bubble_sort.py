#!/usr/bin/env python
__author__ = 'kevin'

def bubble_sort(array):
    n = len(array)
    k = 0
    for i in range(n - 1, -1, -1):
        flag = 0
        for j in range(n - 1, k, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
                flag = 1
                k = j

        if not flag:
            break
    return array


if __name__ == "__main__":
    array = [4, 9, 1, 3, 7, 2, 12, 100, 28]
    # array = [4, 9, 1, 3, 7, 2, 22, 102, 5, 6]
    print '########original array: ', array
    print '########after sort: ', bubble_sort(array)


