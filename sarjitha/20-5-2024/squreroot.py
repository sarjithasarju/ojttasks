import math

def calculate_square_root(number):

    if number < 0:
        raise ValueError("Square root is not defined for negative numbers")
    return math.sqrt(number)

number = 25
square_root = calculate_square_root(number)
print(f"The square root of {number} is {square_root}")
