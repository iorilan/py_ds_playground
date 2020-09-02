"""
zero ,one ,eye
"""
import numpy as np

# 3 rows 5 columns '1'
print(np.ones((3,5),dtype=np.int))

# 7 rows 3 columns '0'
print(np.zeros((7,3)))

#3 rows 4 columns, diagnal index = 1
print(np.eye(3,4,k=1))

#4 rows 5 columns, diagnal index = 2
print(np.eye(4,5,k=2))

#5 rows 5 columns, diagnal index = 3
print(np.eye(5,5,k=3))

#2 rows 5 columns filled with 7
print(np.full((2,5), 7))

#3 rows 7 columns 0-1 random number
print(np.random.rand(3,7))

