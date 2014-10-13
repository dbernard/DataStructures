import unittest
from Fib import nth_fib

class FibsTests(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual([], nth_fib([]))

    def test_first_two_fibs(self):
        self.assertEqual([0,1], nth_fib([1, 2]))

    def test_first_three_fibs(self):
        self.assertEqual([0,1,1], nth_fib([1, 2, 3]))

    def test_single_fib(self):
        self.assertEqual([3], nth_fib([5]))

    def test_lots_of_fibs(self):
        self.assertEqual([0, 377, 3, 34, 55, 89], nth_fib([1, 15, 5, 10, 11, 12]))


if __name__ == '__main__':
    unittest.main()
