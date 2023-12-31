import numpy as np

a = np.array([1, 2])
b = np.array([2, 3])

dot2 = 0
for e,f in zip(a,b):
    print('e:',e,', f',f)
    dot2 += e*f

print('a: ',a)
print('b: ',b)
print('a*b: ',a*b)
print('dot1:',a.dot(b))
print('dot2:',dot2)