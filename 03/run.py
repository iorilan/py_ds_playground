"""
transpose and flatten
"""

import numpy as np

# transpose
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(np.transpose(arr))

# flatten
print(arr.flatten())