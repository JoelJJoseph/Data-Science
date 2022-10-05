"""
1. Perform the following operations using Numpy


    a. Generate random numbers between 20 and 40
    b. Create a 6X6 array with random values and find the minimum and maximum
    values
    c. Generate a random array of size 9X3 and extract the first five rows of 
    the array and store them into a variable
    d. Write a NumPy program to check two random arrays are equal or not.
"""

import numpy as np
values=np.random.randint(20,40,size=5)
print("values:",values)

import numpy as np
x = np.random.random((6,6))
print("Original Array:")
print(x) 
xmin = x.min() 
xmax= x.max()
print("Minimum Value:")
print(xmin)
print("Maximum Value:")
print(xmax)

x = np.random.rand(9, 3)
print("Original array: ")
print(x)

print("\n")

y= x[:5, :]
print("First 5 rows of the above array:")
print(y)

x = np.random.randint(0,2,6)
print("First array:")
print(x)
print("\n")

y = np.random.randint(0,2,6)
print("Second array:")
print(y)

print("\n")

print("Check two arrays are equal or not!")
array_equal = np.allclose(x, y)
print(array_equal)

"""2.Extract from the array below:
np.array([3,2,4,6,9,12,14,16,18,21,24,27,,40,42,45,48,99,100]) with Boolean masking all the number


1.   which are divisible by 3
2.   Which are not divisible by 2
3.   which are divisible by 5
4.   which are divisible by 3 and 5
5.   which are divisible by 5 and set them to 55




"""

x=np.array([3,2,4,6,9,12,14,16,18,21,24,27,40,42,45,48,99,100])
x

x[x%3==0]

x[x%2!=0]

x[x%5==0]

x[(x%3==0) & (x%5==0)]

y=x[x%5==0]
y

z=x[x%5==0]
y=x[x%5==0]
y[::]=55
print(y)
print(z)

x=np.array([3,2,4,6,9,12,14,16,18,21,24,27,40,42,45,48,99,100])
x[x%5==0]=55
print(x)

"""Calculate the average, variance and standard deviation in Python using NumPy."""

import numpy as np  
data = list(range(1,6))  
output=np.average(data)  
print(data) 
print(output)

import numpy as np  
data = list(range(1,6))  
output=np.var(data)  
print(data) 
print(output)

import numpy as np  
data = list(range(1,6))  
output=np.std(data)  
print(data) 
print(output)

