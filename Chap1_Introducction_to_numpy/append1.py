import numpy as np

arr1 = np.array([1, 2, 3])

arr1 = np.append(arr1,4)
arr1 = np.append(arr1,[5])
print(arr1)

for e in arr1:
    print(e)

arr2 = arr1 + arr1
print(arr2)

for e in arr2:
    print(e)