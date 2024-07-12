import unittest
from unittest.mock import patch
from calculator_app import Calculations

class TestCalculations(unittest.TestCase):
    """TestCalculation Class

    Args:
        unittest (Unit testing library): This allows the developer to perform unit testing on a created application.
    """
    @classmethod
    def setUpClass(self):
        """setUpClass method

        Returns: Initiates the instance of the calculator class once to avoid 
        repitition in the different tests methods
        """
        self.calculation = Calculations(22, 10)

    def test_sum(self):
        """test_sum method

        Returns: the sum test result of a and b
        """
        self.assertEqual(self.calculation.get_sum(), 32, 'The sum is wrong.')

    def test_diff(self):
        """test_diff method

        Returns: the difference test result between a and b
        """
        self.assertEqual(self.calculation.get_difference(), 12, 'The difference is wrong.')

    def test_product(self):
        """test_product method

        Returns: the product test result of a and b
        """
        self.assertEqual(self.calculation.get_product(), 220, 'The product is wrong.')

    def test_division(self):
        """test_quotient method

        Returns: the quotient test result between a and b
        """

        self.assertEqual(self.calculation.get_division(), 2.2, 'The quotient is wrong.')
        
    def test_modulus(self):
        """test_modulus method

        Returns: the modulus test result of a and b
        """          
        self.assertEqual(self.calculation.get_modulus(), 2, 'The modulus is wrong.')
    
    def test_exponent(self):
        """test_exponent method

        Returns: the exponent test result of a and b
        """
        self.assertEqual(self.calculation.get_exponent(), 26559922791424, 'The exponent is wrong.')
    
    def test_floordiv(self):
        """test_floordiv method

        Returns: the floor division test result between a and b
        """
        self.assertEqual(self.calculation.get_floordiv(), 2, 'The floor division is wrong.')


def test_get_valid_inputs(self):
        """
        Tests the get_valid_operand function with valid and invalid input.
        """
        # Valid input
        with patch('builtins.input', return_value='23'):
            self.assertEqual(self.calculation.get_valid_inputs('Enter a number: '), 23)

        # Invalid input followed by valid input
        with patch('builtins.input', side_effect=['invalid', '23']):
            self.assertEqual(self.calculation.get_valid_inputs('Enter a number: '), 23)

if __name__ == '__main__':
    unittest.main()