'''The purpose of this file is to create a program that
    classifies triangles based on 3 given side lengths'''

from typing import List, Tuple

def classify_triangle(side_a: int, side_b: int, side_c: int) -> None:
    '''Based on given side lengths (side_a, side_b, side_c), this function classifies a triangle as
    equilateral, isosceles, scalene, or right and returns the classification as a string'''

    check_if_input_is_string(side_a, side_b, side_c)
    check_for_negative_side_lengths(side_a, side_b, side_c)
    check_the_sum_of_two_sides(side_a, side_b, side_c)

    right_triangle_flag: bool = check_if_right_triangle(side_a, side_b, side_c)

    if side_a == side_b == side_c:
        return "equilateral"

    if side_a == side_b or side_a == side_c or side_b == side_c:
        if right_triangle_flag is True:
            return "right isosceles"
        if right_triangle_flag is False:
            return "isosceles"

    if side_a != side_b != side_c:
        if right_triangle_flag is True:
            return "right scalene"
        if right_triangle_flag is False:
            return "scalene"

    return None

def check_if_input_is_string(side_a: int, side_b: int, side_c: int) -> None:
    '''Checks if any of the given side lengths for a triangle is a string. If
        a side is a string, raises a ValueError'''

    for triangle_side_length in [side_a, side_b, side_c]:
        if isinstance(triangle_side_length, str):
            raise ValueError(f'''Please enter a numerical value for side
                                length "{triangle_side_length}" ''')

def check_for_negative_side_lengths(side_a: int, side_b: int, side_c: int) -> None:
    '''Checks if any of the given side lengths for a triangle is negative.
        If a side is negative, then raises a ValuError'''

    for triangle_side_length in [side_a, side_b, side_c]:
        if triangle_side_length < 0:
            raise ValueError(f'''The side with length {triangle_side_length} is a negative value.
                                This is not a valid length for the side of a triangle.''')

def check_the_sum_of_two_sides(side_a: int, side_b: int, side_c: int) -> None:
    '''Checks the following triangle property: The sum of the length of any two sides of a triangle
        must be greater than the length of the third side.
        If the property is violated, than an ArithmeticError is raised'''

    triangle_property_definition: str = '''The sum of the length of any two sides of a triangle
                                            must be greater than the length of the third side'''

    if side_a + side_b < side_c:
        raise ArithmeticError (f'''{triangle_property_definition}. {side_a} + {side_b}
                                is not greater than {side_c}.''')

    if side_a + side_c < side_b:
        raise ArithmeticError (f'''{triangle_property_definition}. {side_a} + {side_c}
                                is not greater than {side_b}.''')

    if side_b + side_c < side_a:
        raise ArithmeticError (f'''{triangle_property_definition}. {side_b} + {side_c}
                                is not greater than {side_a}.''')

def check_if_right_triangle(side_a: int, side_b: int, side_c: int) -> bool:
    '''Checks if the given sides of a triangle create a right triangle.
        If the sides create a right triangle, then returns True, if not False'''

    return bool((side_a ** 2 + side_b ** 2) == int(side_c ** 2))

def main() -> None:
    '''Prints out a triangle classification based on the sample inputs.
        Triangle classification includes: equilateral, isosceles, scalene, right'''

    sample_inputs: List[Tuple(int, int, int)] = [(3, 3, 3), (4, 4, 3), (5, 7, 9), (4, 3, 5)]

    for inputs in sample_inputs:
        side_a, side_b, side_c = inputs
        print(classify_triangle(side_a, side_b, side_c))


if __name__ == "__main__":
    main()
