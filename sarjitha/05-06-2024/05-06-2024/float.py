import numpy as np

# Create an array with floating-point numbers
float_array = np.array([1.5, 2.8, 3.3, 4.7, 5.9])

# Change data type from float to integer
int_array = float_array.astype(int)

print(int_array)
print(f"The data type of the array is: {int_array.dtype}")
