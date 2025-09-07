import numpy as np
#np.array has fixed size if we need to perform any operations we need to perform any opertaions we can to create a new array

#axis=None : in 1d
# Axis=0->rows
# Axis=1->cols

#insert
#np.insert( array, index, value, axis=None/rows/cols)

#append : insert array value at end
#np.array(array, value, axis=None/rows/cols)

#concat : Adding to array
#np.concatenate((array1, array2))

#delete
#np.delete(array, index, axis=None/rows/cols)

#insert
arr=np.array([1,2,3,4])
new_arr=np.insert(arr, 0, 0)
print(f"New array 1d:{new_arr}")

arr2d=np.array([[1,2],[3,4]])
new_arr2d=np.insert(arr2d,1, [5,6], 1)  #Col insert
print(f"New Array 2d: {new_arr2d}")

#append
arr_append=np.append(arr,[5,6,7,8])
print(f"Array after Append 1d: {arr_append}")
arr_append2d=np.append(arr2d,[[7,8],[9,10]], 1)
print(f'Array after Append 2d : {arr_append2d}')


#Concat
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
concat_array=np.concatenate((arr1, arr2))
print(f"New concat array: {concat_array}")

#delete
del_arr=np.delete(arr1, 1)
print(f'Removed value at index 1: {del_arr}')
del_arr_2d=np.delete(arr2d, 1, axis=0)
print(f'Removed Array Value of index 1 : {del_arr_2d}')