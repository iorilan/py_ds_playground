"""
    slice, broadcasting
"""
import numpy as np
from pprint import pprint
arr = np.reshape(np.array([range(1,26)]),(5,5))
pprint(arr)
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])

arr_slice = arr[1:5,2:5]
pprint(arr_slice)
# array([[ 8,  9, 10],
#        [13, 14, 15],
#        [18, 19, 20],
#        [23, 24, 25]])


pprint(1+(2*arr_slice+3))
# array([[20, 22, 24],
#        [30, 32, 34],
#        [40, 42, 44],
#        [50, 52, 54]])

#last columns
pprint(arr[:-1,-1:])
# array([[ 5],
#        [10],
#        [15],
#        [20]])
pprint(arr[:-1,-1:] %2 == 0)
# array([[False],
#        [ True],
#        [False],
#        [ True]])