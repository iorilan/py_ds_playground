"""
    array operation
"""

import numpy as np

def show_res(a,b):
    #[5 7 9]
    print(np.add(a,b))
    print(a+b)
    #[-3 -3 -3]
    print(np.subtract(a,b))
    print(a-b)
    #[ 4 10 18]
    print(np.multiply(a,b))
    print(a*b)
    #[0.25 0.4  0.5 ]
    print(np.divide(a,b))
    print(a/b)
    #[1 2 3]
    print(np.mod(a,b))
    print(a%b)
    ##[  1  32 729]
    print(np.power(a,b))
    print(a**b)

    #[0 0 2]
    print(np.bitwise_and(a,b))

    #[5 7 7]
    print(np.bitwise_or(a,b))

    #[5 7 5]
    print(np.bitwise_xor(a,b))

show_res(np.array([1,2,3]),np.array([4,5,6]))

#show_res(np.array([1,2,3]),np.array([4,5])) error
#show_res(np.array([1,2]),np.array([4,5,6])) error


print("====")
# 1,2,3,4,5
print(np.floor(np.array([1.1,2.2,3.3,4.4,5.5])))

# 2,3,4,5,6
print(np.ceil(np.array([1.1,2.2,3.3,4.4,5.5])))

# 1,2,3,4,6
print(np.rint(np.array([1.1,2.2,3.3,4.4,5.5])))

print("====")
#[ 2.71828183  7.3890561  20.08553692 54.59815003]
print(np.exp(np.array([1,2,3,4])))
#[0.         0.69314718 1.09861229 1.38629436]
print(np.log(np.array([1,2,3,4])))
#[1.         1.41421356 1.73205081 2.        ]
print(np.sqrt(np.array([1,2,3,4])))
#[1. 2. 3. 4.]
print(np.fabs(np.array([1,-2,3,-4])))

print("====")
#[ 0.84147098  0.90929743  0.14112001 -0.7568025 ]
print(np.sin(np.array([1,2,3,4])))
#[ 0.54030231 -0.41614684 -0.9899925  -0.65364362]
print(np.cos(np.array([1,2,3,4])))
#[ 1.55740772 -2.18503986 -0.14254654  1.15782128]
print(np.tan(np.array([1,2,3,4])))
#[ 3.14159265  6.28318531  9.42477796 12.56637061]
print(np.pi*np.array([1,2,3,4]))
