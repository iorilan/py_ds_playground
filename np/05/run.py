"""
zero ,one ,non-zero, eye, diag, random
"""
import numpy as np

print("================ones===============")
# 3 rows 5 columns '1'
print(np.ones((3,5),dtype=np.int))

print("================zeros===============")
# 7 rows 3 columns '0'
print(np.zeros((7,3)))

print("================non-zero===============")
# (array([0, 1, 4], dtype=int32),) . index of non-zero element
print(np.nonzero([1,2,0,0,4,0]))

print("================eye===============")
#3 rows 4 columns, diagnal index = 1
print(np.eye(3,4,k=1))

#4 rows 5 columns, diagnal index = 2
print(np.eye(4,5,k=2))

#5 rows 5 columns, diagnal index = 3
print(np.eye(5,5,k=3))


print("================full===============")
#2 rows 5 columns filled with 7
print(np.full((2,5), 7))

print("================rand===============")
#3 rows 7 columns 0-1 random number
print(np.random.rand(3,7))

Z=np.random.rand(2,4)
#sort each row
Z.sort()
print(Z)

print("================randint===============")
A = np.random.randint(0,3,(2,3))
B = np.random.randint(0,3,(2,3))
print(A)
print(B)
print(np.allclose(A,B))

print("================randomsample===============")
print(np.random.random_sample(size =(2, 3)) )


print("================diag===============")
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]
print(np.diag(1+np.arange(3),k=0))

#all diag element index start from 1, diag column = 2
# [[0 0 1 0 0 0 0]
#  [0 0 0 2 0 0 0]
#  [0 0 0 0 3 0 0]
#  [0 0 0 0 0 4 0]
#  [0 0 0 0 0 0 5]
#  [0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0]]
print(np.diag(1+np.arange(5),k=2))

# [[0 0 0 0 0]
#  [1 0 0 0 0]
#  [0 2 0 0 0]
#  [0 0 3 0 0]
#  [0 0 0 4 0]]
print(np.diag(1+np.arange(4),k=-1))