import numpy as np

arr_1d=np.array([1,2,3,4,5,6,7,8,9,10])
arr_2d=np.array([[1,1],[2,2]])
arr_3d=np.array([[[1,1],[2,2], [3,3]]])

#indexing
#array[index_val        : 1d Array
#array[row][col]        : 2d Array
#array[depth][row][col] : 3d Array 
#nd array               : similar as nesting index

#fancy indexing  : Selecting multiple index at once
#array([list of all index values])

#Slicing
#array[start: stop: step] : by default step value is 1 and it goes upto stop-1
#array[::-1]              : Reverse an array 
#array[::step]            : get all element and by step value
#2d array
#array[start_row:stop_row:step_row, start_col:stop_col:step_col]
#3d array
#array[start_depth:stop_depth:step_depth, start_row:stop_row:step_row, start_col:stop_col:step_col]



#filtering :Boolean Masking
#array[array condition]

#indexing of 1d array
print(f'Value at 0 index: {arr_1d[0]}')
#indexing of 2d array
print(f'Value at 3 index: {arr_2d[1][0]}')
#indexing of 3d array
print(f'Value at 9 index: {arr_3d[0][2][1]}')

#fancy indexing
print(f'Getting value of index 1,3 and 7 : {arr_1d[[1,3,7]]}')

#slicling 
print(f'Slicing 1 to 5: {arr_1d[0: 6:1]}')
print(f'Reverse of array: {arr_1d[::-1]}')

#slicing of 2d array 
arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(f'Slicied row :{arr2[2,0::3]}')                                #Slicing the rows
print(f'Slicing the Cols: {arr2[:2:2]}')                             #Slicing the Cols
print(f'Slicing the rows and Cols: {arr2[0:2:1, 0:2:1]}')            #Slicing the rows and Cols

#Slicing of 3d Array
arr3 = np.array([
    [[1, 2, 3], [4, 5, 6]],       # Layer 0
    [[7, 8, 9], [10, 11, 12]]     # Layer 1
])
print(f'Slicing of the Row: {arr3[:,0,:]}')                      #Slicing the rows
print(f'Slicing of the Col: {arr3[::,1]}')                       #Slicing the Cols
print(f'Slicing of the Row and Col: {arr3[:,:1:,:1:]}')          #Slicing the rows and cols


#Flitering in 1d, 2d and 3d array
print(f'All values greater than 5 :{arr_1d[arr_1d>5]}')
print(f'All values greater than 1 :{arr_2d[arr_2d>1]}')
print(f'All values greater than 3 :{arr3[arr3>5]}')