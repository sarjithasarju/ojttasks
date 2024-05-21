from functools import reduce

multiply = lambda x, y: x * y


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return reduce(multiply, range(1, n + 1))


number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
