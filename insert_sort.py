#!/usr/bin/env python
__author__ = 'kevin'

def insert_sort(array):
    n = len(array)

    for i in range(1, n):
        if array[i] < array[i - 1]:
            temp = array[i]
            index = i

            for j in range(i - 1, -1, -1):
                if array[j] > temp:
                    array[j + 1] = array[j]
                    index = j
                else:
                    break
            array[index] = temp

    return array


if __name__ == "__main__":
    array = [4, 9, 1, 3, 7, 2]

    print '########original: ', array
    print '########after sort: ', insert_sort(array)
