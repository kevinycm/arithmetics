#!/usr/bin/env python
__author__ = 'kevin'

def quick_sort(array):
    return qsort(array, 0, len(array) - 1)

def qsort(array, left, right):
    if left >= right:
        return array

    key = array[left]
    lp = left
    rp = right

    while lp < rp:
        while array[rp] >= key and lp < rp:
            rp -= 1

        while array[lp] <= key and lp < rp:
            lp += 1

        array[lp], array[rp] = array[rp], array[lp]

    array[left], array[lp] = array[lp], array[left]
    qsort(array, left, lp - 1)
    qsort(array, rp + 1, right)
    return array


if __name__ == "__main__":
    array = [6, 5, 3, 1, 8, 7, 2, 4]

    print '############original: '
    print array

    print '############after sort: '
    print quick_sort(array)

