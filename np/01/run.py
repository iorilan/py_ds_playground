"""
    iter throu, reverse
"""

import numpy

arr2 = numpy.array([
    [1,2,3],
    [4,5,6]
])
for x in numpy.nditer(arr2):
    print(x)
    if x % 2 == 0:
        print('even number')


arr = [1,2,3,4,5]
res = numpy.flip(numpy.array(arr, float))
print(res)