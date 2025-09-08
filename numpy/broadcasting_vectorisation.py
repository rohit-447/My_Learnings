#broadcasting : perform mathematical operations in numpy wihtout any loops
import numpy as np

#broadcasting
arr=np.array([100,200,300])
discount=10
arr=arr-(arr*discount/100)
print(f'Final proce after broadcasting : {arr}')


#without broadcasting
arr=[100,200,300]
discount=10
final_prices=[]
for prices in arr:
    final_price=prices-(prices*discount/100)
    final_prices.append(final_price)

print(f'Final Price after discount {final_prices}')

#Vectorisation : Perfrom operations element wise
arr2d=np.array([[1,2,3],[4,5,6]])
print(f'Sum of both Array : {arr+arr2d}')