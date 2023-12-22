# tests/test.py

import unittest
from mycode import mul  # Import at the top of the file


class TestMulFunction(unittest.TestCase):
    def test_mul_positive_numbers(self):
        result = mul(3, 4)
        self.assertEqual(result, 12)

    def test_mul_negative_numbers(self):
        result = mul(-2, 5)
        self.assertEqual(result, -10)

    def test_mul_zero(self):
        result = mul(7, 0)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
