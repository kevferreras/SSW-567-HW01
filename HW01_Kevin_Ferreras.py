

def classify_triangle(a: int, b: int, c: int) -> str:
    '''Based on given side lengths (a, b, c), this function classifies a triangle as equilateral, isosceles, scalene, or right and  
        returns the classification as a string'''

    check_for_negative_side_lengths(a, b, c)
    check_the_sum_of_two_sides(a, b, c)

    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    elif (a ** 2 + b ** 2) == c ** 2:
        return "right"
    elif a != b != c:
        return "scalene"

def check_for_negative_side_lengths(a: int, b: int, c: int) -> str:
    '''Checks if any of the given side lengths for a triangle are negative. If a side is negative, then returns a "fail", if no 
        negative sides are found, then returns a "pass" '''
    
    for triangle_side_length in [a, b, c]:
        if triangle_side_length < 0:
            raise ValueError(f'The side with length {triangle_side_length} is a negative value. This is not a valid length for the side of a triangle.')

def check_the_sum_of_two_sides(a: int, b: int, c: int) -> None:
    '''Checks the following triangle property: The sum of the length of any two sides of a triangle is greater than the length of the third side.
        if the property is violated, than an error is raised'''

    triangle_property_definition: str = 'The sum of the length of any two sides of a triangle must be greater than the length of the third side'

    if a + b < c:
        raise ArithmeticError (f'{triangle_property_definition}. {a} + {b} is not greater than {c}.')
    elif a + c < b:
        raise ArithmeticError (f'{triangle_property_definition}. {a} + {c} is not greater than {b}.')        
    elif b + c < a:
        raise ArithmeticError (f'{triangle_property_definition}. {b} + {c} is not greater than {a}.')        

def main() -> None:
    '''Prints out a triangle classification'''

    print(classify_triangle(7,1,10))



if __name__ == "__main__":
    main()