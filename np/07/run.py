"""
    max min mean var std prod sum where 
"""
import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])

print("=====sum====")
#sum of row/col/all
print(np.sum(arr,axis=1))
print(np.sum(arr,axis=0))
print(np.sum(arr))

print("=====prod====")
#product of row/col/all
print(np.prod(arr,axis=1))
print(np.prod(arr,axis=0))
print(np.prod(arr))

print("=====min====")
#min of row/col/all
print(np.min(arr, axis=1))
print(np.min(arr, axis=0))
print(np.min(arr))

print("=====max====")
#max of row/col/all
print(np.max(arr, axis=1))
print(np.max(arr, axis=0))
print(np.max(arr))


print("=====average====")
#average
print(np.average(arr, axis=1))
print(np.average(arr, axis=0))
print(np.average(arr))

print("=====mean====")
#arithmetic mean of row/col/all
print(np.mean(arr, axis=1))
print(np.mean(arr, axis=0))
print(np.mean(arr))

print("=====var====")
#variance  of row/col/all
print(np.var(arr, axis=1))
print(np.var(arr, axis=0))
print(np.var(arr))

print("=====std====")
# standard deviation of row/col/all
print(np.std(arr, axis=1))
print(np.std(arr, axis=0))
print(np.std(arr))

print("=====where====")
# [[-1  0 -1  0 -1  0 -1  0 -1]
#  [-1 -1 -1 -1 -1 -1 -1  0 -1]
#  [ 0  0  0  0  0  0  0  0  0]]
M=np.array([
    [1,2,3,4,5,6,7,8,9],
    [11,21,31,41,51,61,71,82,91],
    [12,22,32,42,52,62,72,82,92]
    ])
print(np.where(M%2==0, 0, -1))