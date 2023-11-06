import numpy as np

# -1 all except the last element in ...

# The method np.zeros() initializes an array with 0 values.
# The method np.ones() initializes an array with 1 values.
# The method np.empty()initializes an array with 0 values.
# The method np.arange() provides a range of numbers:
# The method np.shape() displays the shape of an object:
# The method np.reshape() <= very useful!
# The method np.linspace() <= useful in regression
# The method np.mean() computes the mean of a set of numbers

arr1 = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)])
print('arr1:', arr1)
print('arr1[-1,:]:', arr1[-1,:])
print('arr1[:,-1]:', arr1[:,-1])
print('arr1[-1:,-1]:', arr1[-1:,-1])

