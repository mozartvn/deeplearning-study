import numpy as np

def softmax(Z):
  """
  Z is a matrix Z = [z1; z2; ...;zn
  compute softmax values for each sets of scores in V.
  each column of V is a set of score.
  """

  e_Z = np.exp(Z)
  A = e_Z / e_Z.sum(axis = 0) # sum by row
  return A


A = np.array([
  [1, 2, 3],
  [4, 5, 6]
])

print("A")
print(A)
print("A.sum(axis=0)")
print(A.sum(axis=0))
print("A.sum(axis=1)")
print(A.sum(axis=1))
print("A.T")
print(A.T)
print("softmax(A)")
print(softmax(A))


