import numpy as np


original_array = np.array(["apple", "banana", "cherry"])

view_array = original_array.view()


print("Original Array base attribute:", original_array.base)
print("View Array base attribute:", view_array.base)

print("Original Array:", original_array)
print("View Array:", view_array)
