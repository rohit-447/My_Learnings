import numpy as np
#np.random.seed()                       : used to fix the random no for each runtime
#np.linesapce(start, stop , num )       :used to create a list of evenly spaced numbers over a specific range.
#start: where the numbers begin, stop: where the numbers end ,num: how many numbers you want
#np.random.randint(start, stop, num)    :used to create  random numbers over a specific range.
#np.random.rand(shape)                  :used to create  of  numbers of specific shape.
#np.random.choice(array, size)          :used to choose the random no.
#np.randm.shuffle(array)                :used to suffle the raay values randomly

arr=np.array([1,2,3,4,5,6,7,8,9])
print(f'Evenly spaced Values : {np.linspace(1,5,3)}')
print(f'Two random no. btwn 1 to 10{np.random.randint(1,10,2)}')
print(f'Random no. of shape 1X2 :{np.random.rand(1,2)}')
print(f'Random no. of shape 1X2 :{np.random.randn(1,2)}')
print(f'Two Random no. from array :{np.random.choice(arr,2)}')
np.random.shuffle(arr)
print(f'Randomly shuffled Array: {arr}')