import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 5, size=(5, 2)),columns=['a','b'])
dd = df.agg(['sum', 'mean'])
print(dd)

df = pd.concat([df,dd])
print("Contents of data frame:")
print(df)