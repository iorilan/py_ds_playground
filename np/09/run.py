"""
polynomial and root
"""

import numpy as np
print(np.poly([-1,1])) # (x+1)(x-1)=x^2-1  ==> [1,0,-1]
print(np.poly([1,2])) # (x-1)(x-2)=x^2-3^x+2  ==> [1,-3,2]
print (np.poly([1,2,3,4])) # (x-1)(x-2)(x-3)(x-4) ==> [1,-10,35,-50,24]

print (np.roots([1, 0, -1])) #x^2-1 => [-1,1]
print (np.roots([1,-3,2])) #x^2-3*x+2 =>[1,2]
print(np.roots([1,2,3,4,5])) #not real number

#Anti-Derivative of the polynomial.
print (np.polyint([1, 2])) 
print (np.polyint([3, 2,6])) #3x^2+2^x+6

#derivative of poly
print (np.polyder([1,2,3,4])) #(x^3+2*x^2+3*x^1+4)' = [3,4,3]. 0 omited

#value of poly
print (np.polyval([1,2,3],1)) # x^2+2*x+3 (x=1) => 6
print (np.polyval([1,2,3],2)) # x^2+2*x+3 (x=2) =>11
print (np.polyval([1,2,3],3)) # x^2+2*x+3 (x=3) => 18



