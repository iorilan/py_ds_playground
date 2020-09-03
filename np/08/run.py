"""
    product calculation of 2 array
"""

import numpy as np

a = np.array([1,2])
b = np.array([3,4])

#dot product
print(np.dot(a,b))

#cross product
print(np.cross(a,b))

#inner product
print(np.inner(a,b))

#outer product
print(np.outer(a,b))