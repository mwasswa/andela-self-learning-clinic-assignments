import unittest
from primenumbers import prime_numbers_in_range
class TestGeneratePrimeNumbers(unittest.TestCase):

    def test_prime_numbers_in_range_returns_emptylist_if_arg_is_zero(self):
        self.assertEqual([], prime_numbers_in_range(0),
                         msg='should return empty list for input 0')

    def test_prime_numbers_in_range_returns_emptylist_if_arg_is_unity(self):
        self.assertEqual([], prime_numbers_in_range(0),
                         msg='should return empty list for input 1')

    def test_prime_numbers_in_range_returns_list_if_arg_is_ten(self):
        self.assertEqual([2,3,5,7], prime_numbers_in_range(10),
                         msg='should return [2,3,5,7] list for input 10')

    def test_prime_numbers_in_range_returns_output_of_type_list(self):
        self.assertIsInstance(prime_numbers_in_range(10), list,
                         msg='Invalid output type. Should be a list')

    def test_prime_numbers_in_range_returns_emptylist_for_negative_arg(self):
        self.assertEqual([], prime_numbers_in_range(-10),
                         msg='Should return [] for negative numbers')


