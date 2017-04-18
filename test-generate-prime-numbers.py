import unittest
from primenumbers import prime_numbers_in_range
class TestGeneratePrimeNumbers(unittest.TestCase):
    def setUp(self):
        self.primenum = prime_numbers_in_range

    def test_prime_numbers_in_range_returns_error_if_arg_is_string(self):
        self.assertRaises(ValueError, self.primenum, "string")

    def test_prime_numbers_in_range_returns_error_if_arg_is_float(self):
        self.assertRaises(ValueError, self.primenum, 2.5)

    def test_prime_numbers_in_range_returns_error_if_arg_is_negative(self):
        self.assertRaises(ValueError, self.primenum, -1)

    def test_prime_numbers_in_range_returns_error_if_arg_is_unity(self):
        self.assertRaises(ValueError, self.primenum, 1)

    def test_prime_numbers_in_range_returns_error_if_arg_is_zero(self):
        self.assertRaises(ValueError, self.primenum, 0)