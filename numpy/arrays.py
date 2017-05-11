import numpy as np

a = np.array([1, 2, 3])
print (type(a))
print (a.shape)
print (a[0], a[1], a[2])
a[0] = 5
print(a)

b = np.array([[1,2,3], [4,5,6]]) # create a rank 2 array
print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0]) #

# Numpy also provides many functions to create arrays:
import numpy as np
a = np.zeros((2,2)) # create an array of all zeros
print(a)

b = np.ones((1,2)) # create an array of all ones
print(b)

c = np.full((2,2), 7) # create a constant array
print(c)

d = np.eye(2) # Create a 2x2 identity matrix
print(d)

e = np.random.random((2,2)) # Create an array filled with random values
print(e)

#### ARRAY INDEXING
# Numpy offers several ways to index into arrays
# Slicing: Similar to Python lists, numpy arrays can be cliced. Since arrays may be multidimentsional, you must specify a slice for each dimentsion of the array:

import  numpy as np

# Create the following rank 2 array with shape(3, 4)
# index from 0
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2,2):
# [[2 3]
# [6 7]]
print(a)
b = a[:2, 1:3] # end_index - 1
print(b)

# A slice of an array is a view into the same data, so modifying it
# will modify the original array

print (a[0, 1])
b[0, 0] = 77 # b refence to a, b[0, 0] = a[0, 1]
print(a[0, 1])

# You can also mix integer indexing with slice indexing. However, doing so will yield an array of lower rank than the original array. Note that this is quite different from the way that MATHLAB handles array slicing:

import numpy as np
# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(a)

# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the
# original array:

row_r1 = a[1, :] # Rank 1 view of the second row of a
print(row_r1) # [5 6 7 8]
row_r2 = a[1:2, :] # Rank 2 view of the second row of a
print(a)
print(row_r2) #[[5 6 7 8]]

print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print (col_r1, col_r1.shape)
print(col_r2, col_r2.shape)

# We can make the same distinction when accesing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]

print (a)

print (col_r1, col_r1.shape)
print (col_r2, col_r2.shape)

print("-" * 100)
# Integer array indexing: When you index into numpy arrays using slicing, the resulting array view will always be a subarray of the original array. In contrast, integer array indexing allows you to construct arbitrary arrays using the data from another array. Here is an example:

import numpy as np

a = np.array([[1,2], [3,4], [5,6]])

# An example of integer array indexing
# The retuned array will have shape (3), and
print(a)

print(a[[0,1,2], [0,1,0]]) # Prints "[1 4 5]"

print(np.array([a[0, 0], a[1, 1], a[2, 0]])) # The above example of integer array indexing is equivalent to this:

print(a[[0, 0],[1, 1]])

print(np.array([a[0, 1], a[0, 1]]))

# One useful trick with integer array indexing is selecting or mutating one element from each row of a matrix:

# Create a new array from which we will select elements
# [[ 1  2  3]
# [ 4  5  6]
# [ 7  8  9]
# [10 11 12]]

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])

print(a)

# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each now of a using the indices in b
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"

# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10 # first

print(a) # prints "array([[11,  2,  3],
         #                [ 4,  5, 16],
         #                [17,  8,  9],
         #                [10, 21, 12]])

#Boolean array indexing: Boolean array indexing lets you pick out arbitrary elements of an array. Frequently this type of indexing is used to select the elements of an array that satisfy some condition. Here is an example:

import numpy as np

a = np.array([[1,2], [3,4], [5,6]])

bool_idx = ( a > 2 ) # Find the elements of a that are bigger than 2
                     # this returns a numpy array of Booleans of the same
                     # shape as a, where each slot of bool_idx tells
                     # whether that element of a is > 2

print(bool_idx)

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx

print(a[bool_idx]) #[3 4 5 6]

# We can do all of the above in a single concise statement

print(a[a>2]) # [3 4 5 6]