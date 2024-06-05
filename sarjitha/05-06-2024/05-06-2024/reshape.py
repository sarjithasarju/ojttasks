#convert id into 2d
import numpy as np
array_1d=np.array([1,2,3,4,5,6])
print("array 1d :",array_1d)
print("shape of array1d :",array_1d.shape)
array_2d=array_1d.reshape((2,3))
print("array 2d :",array_2d)
print("shape of array_2_d : ",array_2d.shape)