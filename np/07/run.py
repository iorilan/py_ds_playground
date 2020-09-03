import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])

#sum of row/col/all
print(np.sum(arr,axis=1))
print(np.sum(arr,axis=0))
print(np.sum(arr))

#product of row/col/all
print(np.prod(arr,axis=1))
print(np.prod(arr,axis=0))
print(np.prod(arr))

#min of row/col/all
print(np.min(arr, axis=1))
print(np.min(arr, axis=0))
print(np.min(arr))

#max of row/col/all
print(np.max(arr, axis=1))
print(np.max(arr, axis=0))
print(np.max(arr))

#arithmetic mean of row/col/all
print(np.mean(arr, axis=1))
print(np.mean(arr, axis=0))
print(np.mean(arr))

#variance  of row/col/all
print(np.var(arr, axis=1))
print(np.var(arr, axis=0))
print(np.var(arr))

# standard deviation of row/col/all
print(np.std(arr, axis=1))
print(np.std(arr, axis=0))
print(np.std(arr))