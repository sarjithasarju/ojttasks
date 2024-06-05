import numpy as np
# array_id=np.array([1,2,3,4,5,6])
# print("array_id: ",array_id)
# for elements in array_id:
#     print(elements)

array_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2d_array :",array_2d)
# for rows in array_2d:
#     print(rows)
# for elements in rows:
#     print(elements)

for elements in np.nditer(array_2d):
    print(elements)

    for index,element in np.ndenumerate(array_2d):
        print(f"index: {index},element:{element}")