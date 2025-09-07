import numpy as np

arr1d=np.array([1,2,np.nan, 3,4, np.inf, -np.inf])
arr2d=np.array([[1,2],
                [3,np.nan],
                [np.nan, 7],
                [np.inf, -np.inf]])
#properties
#default via of replace is 0
#np.isnan(array)                                    : return bolloan value by comparing each values of array
#np.nan_to_num(array, nan=value)                    : Replace the nan by value
#np.isinf(array)                                    : Return bolloan value by comparing each values of array
#np.nan_to_num(array, inf=value, neginf=value)      : Replace the positive and negitive inf by value

#isnan
print(f'Missing Values in 1d array: {np.isnan(arr1d)}')
print(f'Missing Values in 2d array: {np.isnan(arr2d)}')

#Replacing nan via values
print(f'Replacing missing values in 1d via 100: {np.nan_to_num(arr1d, nan=11)}')
print(f'Replacing missing values in 2d via 100: {np.nan_to_num(arr2d, nan=100)}')

#isinf
print(f'Infinity Value in 1d: {np.isinf(arr1d)}')
print(f'Infinity Value in 2d: {np.isinf(arr2d)}')

#Replacing the value of inf
print(f"Replacing value of 1d: {np.nan_to_num(arr1d, posinf=0, neginf=1)}")
print(f"Replacing value of 2d: {np.nan_to_num(arr2d, posinf=0, neginf=1)}")