import numpy as np

#Array indexing is the same as accessing an array element

#Get the first element from the following array

one_d_arr = np.array([34,45,23,32,45,67,32])
print("#accessing one-d array with index")
print(one_d_arr[0])

#Get third and fourth elements from the following array and add them.
print("#Get third and fourth elements from the following array and add them")
print("3rd and 4th value is:",one_d_arr[2],one_d_arr[3])
print(one_d_arr[2]+ one_d_arr[3])

#Access 2-D Arrays
#Think of 2-D arrays like a table with rows and columns, where the row represents the dimension and the index represents the column

two_d_arr = np.array([[34,23,12,45,50,34],[43,10,23,23,45,3]])
print('2nd element on 1st row: ', two_d_arr[0, 1])
#Access the element on the 2nd row, 5th column
print("#Access the element on the 2nd row, 5th column:",two_d_arr[1,4])

#negetive indexing
print("Last element from 2nd dim",two_d_arr[1,-1])

#Access 3-D Arrays
#To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element

three_d_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("accessing 3D array",three_d_arr[0,1,0])
