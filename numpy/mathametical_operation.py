import numpy as np
#numpy helps to dynamically update the values of without any loop

arr=np.array([[1,1],[2,2]])
print(f"Original array: {arr}")

#Addition
print(f'Addition : {arr+2}')

#Subtracion
print(f'Subtraction : {arr-1}')

#Multiplication
print(f"Muliplication : {arr*10}")

#Division
print(f'Division : {arr/2}')

#matrix multiplication :Only where there is shape match
#array.dot(array1, array2)
#array.matmul(array1, array2)

a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.array([[1,2],[100,200]])
d=np.array([[400,600],[5,6]])

print(f'Dot product 1d: {np.dot(a ,b)}')
print(f'Matrix Multiplication 1d: {np.matmul(a,b)}')
print(f'Dot product 2d: {np.dot(c ,d)}')
print(f'Matrix Multiplication 2d: {np.matmul(c,d)}')

#Transpose
#array.T
print(f'Transpose : {c.T}')

#Inverse
#np.linalg.inv(array)
print(f'Inverse of Array: {np.linalg.inv(d)}')

#Determinant
#np.linalg.det(array)
print(f'Determinant of 2 d array {np.linalg.det(c)}')

#Eigenvalues and Eigenvectors
#An eigenvector is a direction that doesn't change under a transformation,
#and the eigenvalue tells you how much it stretches or shrinks.
#eigenvalues, eigenvectors = np.linalg.eig(Array)
egienval, eginvec=np.linalg.eig(c)
print(f'Eigenvalues :{egienval}, Eiegenvector :{eginvec}')

#Norm
#norm is a way to measure the size or length of a vector or matrix — like how long or bit it is
#np.linalg.norm(Array)
print(f'Norm of Matrix a is {np.linalg.norm(a)}')
print(f'Norm of Matrix c is {np.linalg.norm(c)}')