import numpy as np

#from a list
#np.array(list_with_needs_to_be_converted_in_array)
arr=[1,2,3]
print(f'Arr is array: {isinstance(arr, np.ndarray)}')
arr=np.array(arr)
print(f'Arr is array: {isinstance(arr, np.ndarray)}')

#create array with all zeroes
#np.zeros((shape))
array_0=np.zeros((2,2))
print(f"Array having all Zeroes: {array_0}")

#create array with all ones
#np.ones((shape))
array_1=np.ones((3,3))
print(f'Array with all ones : {array_1}')

#create an array with any value
#np.full((shape), value)
array_any_value =np.full((2,2),5)
print(f'Array with value: {array_any_value}')


#crete an array with sequence
#np.arange(start, stop, step)
array_sequence=np.arange(1,10,1)
print(f'Array in sequence: {array_sequence}')


#Identity matrix : all values zeros and diagonal values 1
#np.eye(shape)
idenity_matrix=np.eye(3,3)
print(f'Identity matrix: {idenity_matrix}')