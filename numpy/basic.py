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

#aggregation function
#np.mean(array)   : calculate the mean of array
#np.std(array)    : Gives the Standard Deveation 
#np.var(array)    : Gives the Varience of array
#np.sum(array)    : Calculate the sum of array
#np.max(array)    : Max of the array
#np.min(array)    : Min of array
#np.argmax(array) : Index of max value
#np.argmin(array) : Index of min Value

#indexing
#array[index_val        : 1d Array
#array[row][col]        : 2d Array
#array[depth][row][col] : 3d Array 
#nd array               : similar as nesting index

#fancy indexing  : Selecting multiple index at once
#array([list of all index values]) : We pass the list here

#Slicing
#array[start: stop: step] : by default step value is 1 and it goes upto stop-1
#array[::-1]              : Reverse an array 
#array[::step]            : get all element and by step value
#2d array                 : array[start_row:stop_row:step_row, start_col:stop_col:step_col]
#3d array                 : array[start_depth:stop_depth:step_depth, start_row:stop_row:step_row, start_col:stop_col:step_col]

#filtering :Boolean Masking
#array[array condition]

#reshaping
#array.reshape( rows, cols) : Only when the dimensions matches
#it doesnot copy the value it return the view

#flatten : to convert the multidimensional array to 1 d
#array.ravel()      : return the view 
#array.faltten()    : return the copy

#operations in array
#axis=None : in 1d /Axis=0->rows /Axis=1->cols
#insert
#np.insert( array, index, value, axis=None/rows/cols)
#append : insert array value at end
#np.array(array, value, axis=None/rows/cols)
#concat : Adding to array
#np.concatenate((array1, array2))
#delete
#np.delete(array, index, axis=None/rows/cols)


#stacking: Arrangement of array
#np.hstack((array1, array2)) : Horizontal stacking
#np.vstack((array1, array2)) : Vertical stacking
#np.dstack((array1, array2)) : Depth stacking

#spliting: Diving the array 
#np.split(array , value)        : divide the array into 'value' equal parts
#np.array_split(array, value)   : Split the array into unqual parts 
#np.vsplit(array, col_value)    : Split via coln Equal split
#np.hsplit(array, col_value)    : Split via Rows Equal Split 
#np.dslpit(array, depth)        : Split via depth (3d) Equal Split


#value operation : default vlaue of replament is 0
#np.isnan(array)                                    : return bolloan value by comparing each values of array
#np.nan_to_num(array, nan=value)                    : Replace the nan by value
#np.isinf(array)                                    : Return bolloan value by comparing each values of array
#np.nan_to_num(array, inf=value, neginf=value)      : Replace the positive and negitive inf by value


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