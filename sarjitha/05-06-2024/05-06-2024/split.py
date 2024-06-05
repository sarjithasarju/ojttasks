import numpy as np
array=np.array([1,2,3,4,5,6,7,8,9])
split_array=np.split(array,3)
print("orginal array :",split_array)

array_2d=np.array([[1,2,3,],[4,5,6],[7,8,9],[11,12,13]])
vsplit_array=np.vsplit(array_2d,2)
print("vsplited array:",vsplit_array)
