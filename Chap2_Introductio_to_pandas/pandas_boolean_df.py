import pandas  as pd

df1 = pd.DataFrame({'a':[1, 0, 1], 'b':[0,1,1]}, dtype=bool)
df2 = pd.DataFrame({'a':[0, 1, 1], 'b':[1,1,0]}, dtype=bool)

print('df1 & df2 AND')
print(df1 & df2)

print('df1 | df2 OR')
print(df1 | df2)

print("df1 ^ df2: negation")
print(df1 ^ df2)
print()

print('Transposing')

df1 = pd.DataFrame({'a': [1, 0, 1], 'b': [0, 1, 1] },
dtype=int)
print(df1)
print("df1.T:")
print(df1.T)
print()

print('Sum')

df1 = pd.DataFrame({'a' : [1, 0, 1], 'b' : [0, 1, 1] }, dtype=int)
df2 = pd.DataFrame({'a' : [3, 3, 3], 'b' : [5, 5, 5] }, dtype=int)
print("df1 + df2:")
print(df1 + df2)