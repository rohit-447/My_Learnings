import numpy as np

#properies
#np.mean(array)   : calculate the mean of array
#np.std(array)    : Gives the Standard Deveation 
#np.var(array)    : Gives the Varience of array
#np.sum(array)    : Calculate the sum of array
#np.max(array)    : Max of the array
#np.min(array)    : Min of array
#np.argmax(array) : Index of max value
#np.argmin(array) : Index of min Value
arr=np.array([1,2,3])

#mean
print(f'Mean of Array: {np.mean(arr)}')

#std
print(f'Standard Devation of Array : {np.std(arr)}')

#var
print(f'Variance of Array : {np.var(arr)}')

#sum
print(f'Sum of Array : {np.sum(arr)}')

#max and min
print(f'Min : {arr.min()} and Max: {arr.max()}')

#argmax and argmin
print(f"Index of Max: {arr.argmax()} and Min : {arr.argmin()}")