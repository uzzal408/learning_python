"""
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view
"""

import numpy as np
#Make a copy, change the original array, and display both arrays
#Copy
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0]=6
print(x)
print(arr)

#View
#Make a view, change the original array, and display both arrays

view_arr = np.array([1, 2, 3, 4, 5])
v = view_arr.view()
view_arr[1]=10
print(v)
print(view_arr)

#Check the arr is copy or original

print(v.base)
print(x.base)
