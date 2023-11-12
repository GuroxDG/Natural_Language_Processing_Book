import numpy as np
import pandas as pd

myarray = np.array([[10,30,20], [50,40,60], [1000,  2000, 3000]])

rownames = ['apples', 'oranges', 'beer']
colnames = ['January', 'February', 'March']

mydf = pd.DataFrame(myarray, index=rownames, columns=colnames)
print('content data')
print(mydf)

print("contents of January:")
print(mydf['January'])

print("Number of Rows:")
print(mydf.shape[0])

print("Number of Columns:")
print(mydf.shape)

print("Number of Rows and Columns:")
print(mydf.shape)

print("Column Names:")
print(mydf.columns)

print("Column types:")
print(mydf.dtypes)

print("Description:")
print(mydf.describe())
