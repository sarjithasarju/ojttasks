#Convert the following 1-D array with 12 elements into a 3-D array.
#  The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements
import numpy as np


array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

array_3d = array_1d.reshape(2, 3, 2)


print("3-D array:")
print(array_3d)
