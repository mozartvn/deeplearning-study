# MATLAB files
#
# The functions scipy.io.loadmat and scipy.io.savemat allow you to read and write MATLAB files. You can read about them in the documentation.

# Distance between points

# Scipy defines some useful functions for computing distances between sets of points
#
# The function scipy.spatial.distance.pdist computes the distance between all pairs of points in a given set:

import numpy as np
from scipy.spatial.distance import pdist, squareform

# Create the following array where each row is a point in 2D space:
#[[0 1]
# [1 0]
# [2 0]]

x = np.array([[0, 1],
              [1, 0],
              [2, 0]])
print(x)

# d[i, j] is the Euclidean distance between x[i, :] and x[j, :],
# and d is the following array:
# [[ 0.          1.41421356  2.23606798]
#  [ 1.41421356  0.          1.        ]
#  [ 2.23606798  1.          0.        ]]

d = squareform(pdist(x, 'euclidean'))

print(d)

# More
#http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html