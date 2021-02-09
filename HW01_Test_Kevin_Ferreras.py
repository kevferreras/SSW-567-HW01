from HW01_Kevin_Ferreras import classify_triangle, check_for_negative_side_lengths, check_the_sum_of_two_sides
import unittest

class ClassifyTriangleTest(unittest.TestCase):

    def test_classify_triangle(self) -> None:
        '''Tests that classify_triangle() correctly classifies a triangle based on 3 given side lengths. 
            classify_triangle() should return one of the following strings: equilateral, isosceles, scalene, right'''

        self.assertEqual(classify_triangle(3, 3, 3), "equilateral")
        self.assertEqual(classify_triangle(4, 4, 6), "isosceles")
        self.assertEqual(classify_triangle(5, 7, 9), "scalene")
        self.assertEqual(classify_triangle(4, 3, 5), "right")

    def test_check_for_negative_side_lengths(self) -> None:
        '''Tests that a ValueError is raised when negative value(s) is/are passed in as side lengths'''

        with self.assertRaises(ValueError):
            check_for_negative_side_lengths(-3, 3, 3)
            check_for_negative_side_lengths(-5, -5, -5)

    def test_check_the_sum_of_two_sides(self) -> None:
        '''Tests that an ArithmeticError is raised if the side lengths do not meet the following triangle property:
             The sum of the length of any two sides of a triangle is greater than the length of the third side'''

        with self.assertRaises(ArithmeticError):
            check_the_sum_of_two_sides(7, 1, 5)
            check_the_sum_of_two_sides(9, 4, 3)


if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)