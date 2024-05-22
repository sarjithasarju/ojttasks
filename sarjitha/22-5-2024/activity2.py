import math

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.side_length = side_length

    def calculate_diagonal(self):
        # The diagonal of a square can be calculated using the Pythagorean theorem
        return math.sqrt(2) * self.side_length

# Example usage
square = Square(5)
print(f"Side length: {square.side_length}")
print(f"Area: {square.area()}")               # Output: 25
print(f"Perimeter: {square.perimeter()}")     # Output: 20
print(f"Diagonal: {square.calculate_diagonal()}")  # Output: 7.0710678118654755
