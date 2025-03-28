import numpy as np
a = [42]
b = [1,2,3,4,5]
c = [[1,2,3],[4,5,6]]
d = [[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]

print(a,"\n")
print(b,"\n")
print(c,"\n")
print(d,"\n")

a1 = np.array([42])
b1 = np.array([1,2,3,4,5])
c1 = np.array([[1,2,3],[4,5,6]])
d1 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a1,a1.ndim,"\n")
print(b1,b1.ndim,"\n")
print(c1,c1.ndim,"\n")
print(d1,d1.ndim,"\n")