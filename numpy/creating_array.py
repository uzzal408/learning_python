import numpy as np
#We can create a NumPy ndarray object by using the array() function.

arr = np.array([34,45,23,32,45,67,32])
print("#array of list")
print(arr)
print(type(arr))

#create array from tuple

tup = np.array((32,31,45,23,12,45,12))
print(tup)

#O-D array
#0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
od_arr = np.array(45)
print("#O-D Array")
print(od_arr)

#1-D Array
#An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
one_d_arr = np.array([32,31,45,23,12,45,12])
print("#ONE-D Array")
print(one_d_arr)
#2-D Array
#An array that has 1-D arrays as its elements is called a 2-D array.
#These are often used to represent matrix or 2nd order tensors

two_d_arr = np.array([[34,23,12,45],[43,10,23,23]])
print("#Two-D Array")
print(two_d_arr)
#3-D Array
#An array that has 2-D arrays (matrices) as its elements is called 3-D array.
#These are often used to represent a 3rd order tensor

#Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6
three_d_arr = np.array([[[1,2,3],[34,23,56]],[[1,2,3],[34,56,34]]])
#three_d_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("#print 3-D array")
print(three_d_arr)

#Check the number of dymension
print("#Check the dymension")
print(od_arr.ndim)
print(one_d_arr.ndim)
print(two_d_arr.ndim)
print(three_d_arr.ndim)

#Higher Dimensional Arrays
#An array can have any number of dimensions.
#When the array is created, you can define the number of dimensions by using the ndmin argument

h_arr = np.array([1, 2, 3, 4], ndmin=5)
print("#Creating Higher Dimention Array")
print(h_arr)
print('number of dimensions :', h_arr.ndim)

