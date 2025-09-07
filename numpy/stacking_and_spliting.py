import numpy as np
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

#Stacking
arr1=np.array([1,2])
arr2=np.array([2,3])
print(f"Horizontal stack :{np.hstack((arr1, arr2))}")
print(f"Vertical stack :{np.vstack((arr1, arr2))}")

arr2d_1=np.array([[1,2],[3,4]])
arr2d_2=np.array([[10,20],[30,40]])
print(f'Horizontal Stacking: {np.hstack((arr2d_1, arr2d_2))}')
print(f'Vertical Stacking: {np.vstack((arr2d_1, arr2d_2))}')

#split

arr1d=np.array([1,2,3,4,5,6,7,8,9,10])
arr2d=np.array([[1,2],[3,4],[4,5]])
print(f"Split 1d Array into 2 equual parts: {np.split(arr1d, 2)}")
print(f"Split 2d Array into 3 equual parts: {np.split(arr2d, 3)}")

#array_split
arr1d_unqual=np.array([1,2,3,4,5])
arr2d_unqual=np.array([[1,2],[3,4],[5,6]])
print(f"Split 1d using array_split: {np.array_split(arr1d_unqual, 2)}")
print(f"Split 2d using array_split: {np.array_split(arr2d_unqual, 2)}")

#vsplit
arr2d_vsplit=np.array([[1,2],
                       [3,4],
                       [4,5],
                       [6,7]])
print(f"Vertical Split of the col: {np.vsplit(arr2d_vsplit, 2)}")
print(f"Horizontal Split of the col: {np.hsplit(arr2d_vsplit, 2)}")

#dsplit
arr3d_dsplit = np.array([[[1, 2, 3],
                 [4, 5, 6]]])
print(f"Split on depth: {np.dsplit(arr3d_dsplit, 3)}")
