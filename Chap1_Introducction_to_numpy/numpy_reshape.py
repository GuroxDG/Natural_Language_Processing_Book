import numpy as np

x = np.array([[2, 3], [4, 5], [6, 7]])
print(x.shape)
print('x',x)

x = x.reshape((2,3))
print(x.shape)
print('x1',x)

x = x.reshape((-1))
print(x.shape)
print('x2',x)

x = x.reshape((6, -1))
print(x.shape)
print('x3',x)

x = x.reshape((-1, 6))
print(x.shape)
print('x4',x)