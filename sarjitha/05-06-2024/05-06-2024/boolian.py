import numpy as np

# Create an array with integers
int_array = np.array([0, 1, 2, 0, 5])

# Change data type from integer to boolean
bool_array = int_array.astype(bool)

print(bool_array)
print(f"The data type of the array is: {bool_array.dtype}")
