"""
    shape and reshape, arange
"""

import numpy as np

arr = np.array([range(0,15)])
print(arr.shape)
print(np.reshape(arr,(3,5)))
# np.reshape(arr,(5,2))  throw error

#[0 1 2 3 4 5 6]
print(np.arange(7))

#[ 0  3  6  9 12 15 18]
print(np.arange(0,20,3))

