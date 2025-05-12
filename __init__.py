"""Test suite for lcsfinder."""

# Note: You may want to add test cases for your implementation
# even though that is not strictly required for this project

import unittest

from lcsfinder.approach import DataType
from lcsfinder.generate import generate_data
from lcsfinder.lcs import lcs_calculate, lcs_dynamic, lcs_recursive


class TestLCSAlgorithms(unittest.TestCase):
    """Test cases for LCS algorithms."""

    def test_lcs_recursive(self):
        """Test the recursive LCS algorithm."""
        self.assertEqual(lcs_recursive("abcde", "ace"), 3)
        self.assertEqual(lcs_recursive("abc", "def"), 0)
        self.assertEqual(lcs_recursive("", "abc"), 0)

    def test_lcs_dynamic(self):
        """Test the dynamic programming LCS algorithm."""
        self.assertEqual(lcs_dynamic("abcde", "ace"), 3)
        self.assertEqual(lcs_dynamic("abc", "def"), 0)
        self.assertEqual(lcs_dynamic("", "abc"), 0)

    def test_lcs_calculate(self):
        """Test the space-optimized LCS algorithm."""
        self.assertEqual(lcs_calculate("abcde", "ace"), 3)
        self.assertEqual(lcs_calculate("abc", "def"), 0)
        self.assertEqual(lcs_calculate("", "abc"), 0)


class TestGenerateData(unittest.TestCase):
    """Test cases for data generation."""

    def test_generate_data_ints(self):
        """Test data generation for integers."""
        X, Y = generate_data(5, DataType.INTS)
        self.assertEqual(len(X), 5)
        self.assertEqual(len(Y), 5)
        self.assertTrue(all(isinstance(x, int) for x in X))
        self.assertTrue(all(isinstance(y, int) for y in Y))

    def test_generate_data_chars(self):
        """Test data generation for characters."""
        X, Y = generate_data(5, DataType.CHARS)
        self.assertEqual(len(X), 5)
        self.assertEqual(len(Y), 5)
        self.assertTrue(all(isinstance(x, str) for x in X))
        self.assertTrue(all(isinstance(y, str) for y in Y))


if __name__ == "__main__":
    unittest.main()

