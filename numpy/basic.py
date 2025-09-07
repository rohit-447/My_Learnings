#print of array
import numpy as np
array= np.array([1,3])
print(array)

#properties
#.ndim: find the dimension of array
#.shape : find the shape of array
#.zeroes(shape) : create numpy with all values as 0
#.array : used to convert he array to the list
#.dtype : used to know about the datatype of an array
#.astype : used to change the datatype of an array
#isinstance(a, np.ndarray) : to know whether it is array or not a-> array, np.ndarray is the base class for NumPy arrays

#types of array
#1d array (vector) : only 1 rows 
array1d=np.array([1,2])
print(f'Dimension of array is : {array1d.ndim}')
print(f'Shape of array is : {array1d.shape}')


#2d array (MATRIX): any no. of  rows  and cols
array2d=np.array([[1,2],
                  [3,4]])
print(f'Dimension of array is : {array2d.ndim}')
print(f'Shape of array is : {array2d.shape}')

#3d array (Tensor) : 3 axis
array3d=np.array([[[1,2]],
                  [[2,3]]])

print(f'Dimension of array is : {array3d.ndim}')
print(f'Shape of array is : {array3d.shape}')

#nd array: n dimension
ndarray=np.zeros((3,2,3,2))
print(f'nd Array: {ndarray}')
print(f'Dimension of array is : {ndarray.ndim}')
print(f'Shape of array is : {ndarray.shape}')

#conver the list to array
arr=[1,2,3]
arr=np.array(arr)
print(arr)
print(f'Datatype of array : {arr.dtype}')