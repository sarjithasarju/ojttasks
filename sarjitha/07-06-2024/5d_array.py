#Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 
# and verify that last dimension has value 4
import numpy as np


array_5d = np.array([1, 2, 3, 4], ndmin=5)

print("Array:")
print(array_5d)


print("Shape of the array:")
print(array_5d.shape)

print("Values in the last dimension:")
print(array_5d[0][0][0][0])
