#!/usr/bin/env python
__author__ = 'kevin'

def merge_sort(array):
    if len(array) <= 1:
        return array

    num = int(len(array) / 2)
    left = merge_sort(array[:num])
    right = merge_sort(array[num:])
    result = merge(left, right)
    return result


def merge(left, right):
    l, r = 0, 0
    result = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]

    return result


if __name__ == "__main__":
    array = [20, 12, 4, 18, 7, 10, 19, 1, 6, 8, 11]

    print '############original: '
    print array
    print '############after sort: ', '\n', merge_sort(array)
