import unittest
from MagicIndex import MagicIndex

class MagicIndexTest(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(None, MagicIndex([], 0, 0))

    def test_successful_single_element(self):
        self.assertEqual(0, MagicIndex([0], 0, 0))

    def test_fail_single_element(self):
        self.assertEqual(None, MagicIndex([5], 0, 0))

    def test_successful_even_array(self):
        self.assertEqual(4, MagicIndex([-2, 0, 1, 2, 4, 8], 0, 5))

    def test_successful_odd_array(self):
        self.assertEqual(10, MagicIndex([-5, -3, -1, 0, 1, 2, 4, 5, 7, 8, 10], 0, 10))

if __name__ == '__main__':
    unittest.main()

