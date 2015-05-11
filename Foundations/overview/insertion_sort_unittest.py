__author__ = 'pezy'

import unittest
from insertion_sort import *


# case from @Mooophy
class InsertionSortTest(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([5, 2, 4, 6, 1, 3]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(insertion_sort([5]), [5])
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([1, 5, 2, 1, 6]), [1, 1, 2, 5, 6])

    def test_insertion_sort_non_increasing(self):
        self.assertEqual(insertion_sort_non_increasing([1, 5, 2, 1, 6]), [6, 5, 2, 1, 1])
        self.assertEqual(insertion_sort_non_increasing([]), [])

    def test_linear_search(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 6), None)

    def test_add_binary(self):
        self.assertEqual(add_binary([0, 0, 1], [1, 1, 1]), [1, 0, 0, 0])
        self.assertEqual(add_binary([1, 1, 1], [1, 1, 1]), [1, 1, 1, 0])

if __name__ == '__main__':
    unittest.main()
