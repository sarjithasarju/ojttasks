# 2. Convert the array into a 1D array
import numpy as np

# Example 3D array with dimensions 2x2x2
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Convert to 1D array
array_1d = array_3d.flatten()

print(array_1d)
