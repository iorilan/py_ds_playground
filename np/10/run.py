"""
polyfit : pass x and y array and deg. 
get the function line fit in the data.
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3,4,5,6,7,8,9])
y = np.array([1.34,2.56,5.76,4.56,4.12,6.7,7.7,8.1,8.9])
z = np.polyfit(x, y, 4) # use x^4
p = np.poly1d(z)
print(p) 
yvals=p(x)
plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4)
plt.title('polyfitting')
plt.show()