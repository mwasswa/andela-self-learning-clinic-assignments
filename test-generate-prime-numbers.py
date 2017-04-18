import unittest
from primenumbers import prime_numbers_in_range
class TestGeneratePrimeNumbers(unittest.TestCase):

    def test_prime_numbers_in_range_returns_emptylist_if_arg_is_zero(self):
        self.assertEqual("argument must be an integer greater than 2", prime_numbers_in_range(0),
                         msg='should return error message if input is zero')

    def test_prime_numbers_in_range_returns_emptylist_if_arg_is_unity(self):
        self.assertEqual("argument must be an integer greater than 2", prime_numbers_in_range(1),
                         msg='should return error message if input value is 1')

    def test_prime_numbers_in_range_returns_list_if_arg_is_ten(self):
        self.assertEqual([2,3,5,7], prime_numbers_in_range(10),
                         msg='Output must be list of prime numbers')

    def test_prime_numbers_in_range_returns_output_of_type_list_if_arg_isvalid(self):
        self.assertIsInstance(prime_numbers_in_range(10), list,
                         msg='Invalid output type. Should be a list')

    def test_prime_numbers_in_range_returns_emptylist_for_negative_arg(self):
        self.assertEqual("argument must be an integer greater than 2", prime_numbers_in_range(-10),
                         msg='Should return error message if argument is negative')


