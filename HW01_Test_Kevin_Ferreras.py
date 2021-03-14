from hw01_kevin_ferreras import (classify_triangle, check_if_input_is_string, check_for_negative_side_lengths, 
                                check_the_sum_of_two_sides, check_if_right_triangle)
import unittest
import math
from decimal import Decimal

class ClassifyTriangleTest(unittest.TestCase):

    def test_classify_triangle(self) -> None:
        '''Tests that classify_triangle() correctly classifies a triangle based on 3 given side lengths. 
            classify_triangle() should return one of the following strings: equilateral, isosceles, scalene, right'''

        self.assertEqual(classify_triangle(3, 3, 3), "equilateral")
        self.assertEqual(classify_triangle(4, 4, 6), "isosceles")
        self.assertEqual(classify_triangle(5, 7, 9), "scalene")
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), "right isosceles")
        self.assertEqual(classify_triangle(3, 4, 5), "right scalene")

    def test_check_if_input_is_string(self) -> None:
        '''Tests that a ValueError is raised when string value(s) is/are passed in as side lengths'''

        with self.assertRaises(ValueError):
            check_if_input_is_string('one', 'two', 'three')

        with self.assertRaises(ValueError):
            check_if_input_is_string(' ', ' ', ' ')

        with self.assertRaises(ValueError):
            check_if_input_is_string(' ',2, 3)

        with self.assertRaises(ValueError):
            check_if_input_is_string(1,'two', 3)

        with self.assertRaises(ValueError):
            check_if_input_is_string(1, 2, 'three')

    def test_check_for_negative_side_lengths(self) -> None:
        '''Tests that a ValueError is raised when negative value(s) is/are passed in as side lengths'''

        with self.assertRaises(ValueError):
            check_for_negative_side_lengths(-3, 3, 3)

        with self.assertRaises(ValueError):
            check_for_negative_side_lengths(-5, -5, -5)

    def test_check_the_sum_of_two_sides(self) -> None:
        '''Tests that an ArithmeticError is raised if the side lengths do not meet the following triangle property:
             The sum of the length of any two sides of a triangle is greater than the length of the third side'''

        with self.assertRaises(ArithmeticError):
            check_the_sum_of_two_sides(5, 1, 7)

        with self.assertRaises(ArithmeticError):
            check_the_sum_of_two_sides(1, 7, 5)

        with self.assertRaises(ArithmeticError):
            check_the_sum_of_two_sides(7, 5, 1)

    def test_check_if_right_triangle(self) -> None:
        '''Tests that "True" is returned if the given sides create a right triangle,
            and "False" if they don't'''

        self.assertEqual(check_if_right_triangle(3, 4, 5), True)
        self.assertEqual(check_if_right_triangle(3, 6, 7), False)

if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)