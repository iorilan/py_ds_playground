"""
    usage of linalg
    det,eig and inv
"""

import numpy as np

print("=======det=======")
#determinant of an array
print (np.linalg.det([
    [1,2], 
    [3,4]
    ]))
#array must be square. this will throw error

# print (np.linalg.det([
#     [1,2,3], 
#     [4,5,6]
#     ]))

print(np.linalg.det([
    [1,2,3], 
    [4,5,6],
    [7,8,9],
    ]))



print("======eigenvalues======")
#eigenvalues and right eigenvectors of a square array
print (np.linalg.eig([
    [1,2], 
    [3,4]
    ]))
print(np.linalg.eig([
    [1,2,3], 
    [4,5,6],
    [7,8,9],
    ]))

print("====== inverse ======")
#inverse of matrix
print (np.linalg.inv([
    [1,2], 
    [3,4]
    ]))
print(np.linalg.inv([
    [1,2,3], 
    [4,5,6],
    [7,8,9],
    ]))