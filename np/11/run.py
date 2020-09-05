"""
    usage of linalg
    det,eig and inv ,rank
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

print("=============rank===============")
print(np.linalg.matrix_rank([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]]))

print("===========trace=============")
print(np.transpose([[1,2,3],
              [4,5,6],
              [7,8,9]]))


print("===========solve=============")
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([5,6,7])
X=np.linalg.solve(A,B)
print(X)


def lstsq():
    print("=============least square fit===============")
    import matplotlib.pyplot as plt
    
    x = np.arange(0,9)
    #w = np.array([0.5,0.3,1,0.2,0.7,1,1,0.2,1.2])
    #w = np.array([0.9,0.9,1,0.8,0.7,1.1,1.2,0.3,0.9])
    w = np.ones(9)
    A = np.array([x, w])
    print(A)
    # linearly generated sequence
    y = [11,10.5,12.3,14.1,12.9,15.7,16.9,15.8,17.0]
    # obtaining the parameters of regression line
    w = np.linalg.lstsq(A.T, y)[0] 
    
    # plotting the line
    line = w[0]*x + w[1] # regression line
    plt.plot(x, line, 'r-')
    plt.plot(x, y, 'o')
    plt.show()
#lstsq()