import numpy as np
arr=np.array([1,2,3])

#knowing about datatype of an array
#array.dtype: tells about the dataype of an array
print(f'Datype of array : {arr.dtype}')

#Changing the datatype
#arra.astype(new_data_type)
arr=arr.astype(float)
print(f'Array {arr}')
print(f"New Dataype is : {arr.dtype}")