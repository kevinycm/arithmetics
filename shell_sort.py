#!/usr/bin/env python
__author__ = 'kevin'

def shell_sort(array):
    n = len(array)
    gap = int(round(n / 2))

    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i

            while (j >= gap and array[j - gap] > temp):
                array[j] = array[j - gap]
                j = j - gap

            array[j] = temp

            print array
        gap = int(round(gap / 2))

    return array


if __name__ == "__main__":
    array = [20, 12, 4, 18, 7, 10, 19, 1, 6, 8, 11]
    print '#############original: ', array
    print '#############after sort: ', '\n', shell_sort(array)
