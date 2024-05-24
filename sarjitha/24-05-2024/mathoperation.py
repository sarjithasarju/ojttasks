class MathOperations:
    @classmethod
    def add(cls, a, b):
        """Returns the sum of a and b."""
        return a + b

    @classmethod
    def subtract(cls, a, b):
        """Returns the difference of a and b."""
        return a - b

    @classmethod
    def multiply(cls, a, b):
        """Returns the product of a and b."""
        return a * b

    @staticmethod
    def factorial(n):
        """Returns the factorial of n."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        elif n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result


print(MathOperations.add(10, 5))         # Output: 15
print(MathOperations.subtract(10, 5))    # Output: 5
print(MathOperations.multiply(10, 5))    # Output: 50
print(MathOperations.factorial(5))       # Output: 120
