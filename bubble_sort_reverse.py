#!/usr/bin/env python
__author__ = 'kevin'

def bubble_sort(array):
    n = len(array)
    k = n

    for i in range(n):
        flag = 0
        for j in range(1, k):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                flag = 1
                k = j

        if not flag:
            break

    return array


if __name__ == "__main__":
    array = [4, 9, 1, 3, 7, 2]
    print '###########original: '
    print array
    print '###########after sort: '
    print bubble_sort(array)
