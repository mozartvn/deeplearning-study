# Datatypes
#
# Every numpy array is a grid of elements of the same type. Numpy provides a large set of numeric datatypes that you can use to construct arrays. Numpy tries to guess a datatype when you create an array, but functions that construct arrays usually also include an optional argument to explicitly specify the datatype. Here is an example:

import numpy as np

x = np.array([1, 2]) # Let numpy choose the data type
print(x.dtype)

x = np.array([1.0, 2.0])
print(x.dtype)

x = np.array([1,2], dtype=np.int64)
print(x.dtype)

# Array math
# Basic mathematical functions operate elementwise on arrays, and are available both as operator overloads and as functions in the numpy module:

import numpy as np

x = np.array([[1,2], [3,4]], dtype=np.float64)
y = np.array([[5,6], [7,8]], dtype=np.float64)

# Elementtwise sum; both produce the array
# [[ 6.0 8.0]
# [10.0 12.0]

print(x+y)
print(np.add(x,y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]

print(x - y)
print(np.subtract(x,y))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]

print(x*y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x/y)
print(np.divide(x,y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))

# Note that unlike MATLAB, * is elementwise multiplication, not matrix multiplication. We instead use the dot function to compute inner products of vectors, to multiply a vector by a matrix, and to multiply matrices. dot is available both as a function in the numpy module and as an instance method of array objects:

import numpy as np

x = np.array([[1,2], [3,4]])
y = np.array([[5,6], [7,8]])

v = np.array([9,10])
w = np.array([11,12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v,w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(v.dot(x))

print("-"*100)
# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x,y))

# Numpy provides many useful functions for performing computations on arrays; one of the most useful is sum:

import numpy as np

x = np.array([[1,2],[3,4]])

print(np.sum(x)) # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0)) # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1)) # Compute sum of each row; prints "[3 7]"

#You can find the full list of mathematical functions provided by numpy in the documentation.
# Apart from computing mathematical functions using arrays, we frequently need to reshape or otherwise manipulate data in arrays. The simplest example of this type of operation is transposing a matrix; to transpose a matrix, simply use the T attribute of an array object:

import numpy as np

x = np.array([[1,2], [3,4]])

print(x) # Prints "[[1 2]
         #          [3 4]]"
print(x.T) # Prints "[[1 3]
           #          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print(v)  # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"

# https://docs.scipy.org/doc/numpy/reference/routines.array-manipulation.html

