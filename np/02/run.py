"""
    shape and reshape
"""

import numpy as np

arr = np.array([range(0,15)])
print(arr.shape)
print(np.reshape(arr,(3,5)))

# np.reshape(arr,(5,2))  throw error