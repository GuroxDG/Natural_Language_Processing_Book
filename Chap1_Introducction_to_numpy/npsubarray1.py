import numpy as np

# -1 all except the last element in ...

arr1 = np.array([1, 2, 3, 4, 5])
print('arr1', arr1)

print('arr1[0:-1]', arr1[0:-1])
print('arr1[1:-1]', arr1[1:-1])
print('arr1[::-1]', arr1[::-1])