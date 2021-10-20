import numpy as np

# revel
lst = np.array([[1,2,3], [4,5,6], [7,8,9]])

out = lst.ravel()

print(out)

# flatten -> slower
lst = np.array([[1,2,3], [4,5,6], [7,8,9]])

out = lst.flatten()

print(out)

# reshape
lst = np.array([[1,2,3], [4,5,6], [7,8,9]])

out = lst.reshape(-1)

print(out)