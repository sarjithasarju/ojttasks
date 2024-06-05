import numpy as np
arr=np.array([1,2,3,4,5,6])
arr2=arr.reshape((3,2))
print("reshaped array :",arr)
print("shape of the array:",arr.shape)

#reshape back a s 2d array into 1d
arr2=arr.reshape(1,6)