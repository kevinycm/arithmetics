#!/usr/bin/env python

import unittest

def binary_search(array, key, low, high):
    if low < -1 or high < -1 or (low > high):
        return -1

    if not isinstance(array, list):
        return -1

    if not array:
        return -1

    middle = (low + high) / 2
    if array[middle] == key:
        return middle

    elif key < array[middle]:
        return binary_search(array, key, low, middle - 1)
    else:
        return binary_search(array, key, middle + 1, high)


class TestBinarySearchWithEmptyList(unittest.TestCase):
    def setUp(self):
        self.array = []
        self.result_position = -1

    def test_binary_search(self):
        position = binary_search(self.array, 0, 0, len(self.array))
        self.assertEqual(position, self.result_position)


class TestBinarySearchWithOneElementList(unittest.TestCase):
    def setUp(self):
        self.array = [4]
        self.result_position = 0

    def test_binary_search_with_exist_element(self):
        position = binary_search(self.array, 4, 0, len(self.array))
        self.assertEqual(position, self.result_position)

    def test_binary_search_with_none_exist_element(self):
        position = binary_search(self.array, 0, 0, len(self.array))
        self.assertEqual(position, -1)


class TestBinarySearchWithNormalElementsList(unittest.TestCase):
    def setUp(self):
        self.array = [1, 5, 9, 10, 14, 17, 20, 26]
        self.result_position = 2

    def test_binary_search(self):
        position = binary_search(self.array, 9, 0, len(self.array))
        self.assertEqual(position, self.result_position)

if __name__ == "__main__":
    unittest.main()