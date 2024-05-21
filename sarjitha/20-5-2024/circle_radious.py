import math

def calculate_circle_area(radius):
    
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = math.pi * (radius ** 2)
    return area


radius = 5.0
area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is {area:.2f}")
