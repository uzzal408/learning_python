#Slicing arrays
#Slicing in python means taking elements from one given index to another given index

"""
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1
"""

import numpy as np

one_d_arr = np.array([1, 2, 3, 4, 5, 6, 7])

#slice array 2 to 4

print("#Slicing array 2 to 4")
print(one_d_arr[2:4])
#Slice elements from index 4 to the end of the array
print("#Slicing array index 4 to end of array")
print(one_d_arr[4:])
#Slice elements from the beginning to index 4
print("#Slice elements from the beginning to index 4")
print(one_d_arr[:4])
#Negetive Slicing
#Slice from the index 3 from the end to index 1 from the end
print("#negetive slicing")
print(one_d_arr[-3:-1])

#Use the step value to determine the step of the slicing

print(one_d_arr[1:5:2])
print(one_d_arr[::2])

#Slicing 2-D Arrays


two_d_arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("#Slicing two array")
print(two_d_arr[1,1:4])

print("#From both elements, return index 2")
print(two_d_arr[0:2,2])
print("#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array")
print(two_d_arr[0:2,1:3])



