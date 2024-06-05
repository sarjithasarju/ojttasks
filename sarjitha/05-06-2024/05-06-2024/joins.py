import numpy as np
array1=np.array([1,2,3])
array2=np.array([4,5,6])
concat_array=np.concatenate((array1,array2))
print("concat_array ",concat_array)

array1d_1=np.array([[1,2,3],[4,5,6]])
array2d_2=np.array([[7,8,9],[10,11,12],[13,14,15]])

vstack_array=np.vstack((array1d_1,array2d_2))
print("vertical stacked array is :",vstack_array)


hstack_array=np. hstack((array1d_1,array2d_2))
print("horizondal stacked array is :",hstack_array)