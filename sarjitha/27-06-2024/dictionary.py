# Dictionary comprehension to create squares of even numbers from 1 to 20
squares_of_evens = {x: x**2 for x in range(2, 21, 2)}

print(squares_of_evens)
