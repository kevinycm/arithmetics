#!/usr/bin/env python
__author__ = 'kevin'

import unittest

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


class TestBubbleSortWithEmptyList(unittest.TestCase):
    def setUp(self):
        self.array = []
        self.result_array = []

    def test_bubble_sort(self):
        array = bubble_sort(self.array)
        self.assertEqual(array, self.result_array)


class TestBubbleSortWithOneElementList(unittest.TestCase):
    def setUp(self):
        self.array = [1]
        self.result_array = [1]

    def test_bubble_sort(self):
        array = bubble_sort(self.array)
        self.assertEqual(array, self.result_array)


class TestBubbleSortWithNormalElementsList(unittest.TestCase):
    def setUp(self):
        self.array = [4, 9, 3, 6, 12, 10, 100, 1]
        self.result_array = [1, 3, 4, 6, 9, 10, 12, 100]

    def test_bubble_sort(self):
        array = bubble_sort(self.array)
        self.assertEqual(array, self.result_array)


if __name__ == "__main__":
    unittest.main()

