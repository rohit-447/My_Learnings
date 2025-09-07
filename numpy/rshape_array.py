import numpy as np

#reshaping of array
#array.reshape( rows, cols) : Only when the dimensions matches
#it doesnot copy the value it return the view

#flatten : to convert the multidimensional array to 1 d
#array.ravel()      : return the view 
#array.faltten()    : return the copy

arr=np.array([1,2,3,4,5,6,7,8,9,10])

#reshape
print(f'Shape of orginal Array shape: {arr.shape}')
arr=arr.reshape(5,2)
print(f'Array : {arr}')
print(f'Shape of array: {arr.shape}')

arr2d=np.array([[1,2,3],
               [4,5,6]])
#faltten
print(f'Faltten using ravel: {arr2d.ravel()}')
print(f'Flatten using flatten: {arr2d.flatten()}')
