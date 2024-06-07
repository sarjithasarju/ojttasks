
#Check if the returned array is a copy or a view
import numpy as np


array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

array_3d = array_1d.reshape(2, 3, 2)


print("3-D array:")
print(array_3d)

is_view = array_3d.base is array_1d
print("Is the 3-D array a view of the original array?", is_view)
