#!/usr/bin/env python

def binary_search(array, key, low, high):
    if low > high:
        return -1

    middle = (low + high) / 2
    if array[middle] == key:
        return middle

    elif key < array[middle]:
        return binary_search(array, key, low, middle - 1)
    else:
        return binary_search(array, key, middle + 1, high)


if __name__ == "__main__":
    array = [12, 14, 15, 18, 20, 25, 30, 31]
    print binary_search(array, 15, 0, len(array) - 1)
