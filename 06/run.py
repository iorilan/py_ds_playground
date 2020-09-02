"""
    array operation
"""

import numpy as np

def show_res(a,b):
    print(np.add(a,b))
    print(np.subtract(a,b))
    print(np.multiply(a,b))
    print(np.divide(a,b))
    print(np.mod(a,b))
    print(np.power(a,b))

show_res(np.array([1,2,3]),np.array([4,5,6]))

#show_res(np.array([1,2,3]),np.array([4,5])) error
#show_res(np.array([1,2]),np.array([4,5,6])) error



# 1,2,3,4,5
print(np.floor(np.array([1.1,2.2,3.3,4.4,5.5])))

# 2,3,4,5,6
print(np.ceil(np.array([1.1,2.2,3.3,4.4,5.5])))

# 1,2,3,4,6
print(np.rint(np.array([1.1,2.2,3.3,4.4,5.5])))