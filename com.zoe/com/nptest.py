import numpy as np

a = np.arange(10)
b = np.arange(10)
print(">>", a, b)
c = np.ones(10)
d = np.add(a, b, out=c)
print("c:", c)
print(">>>", id(c), id(d))

print("-------------------")
a = np.array([3,2,5,2,7,4,7])
b = np.array([0,9,3,1,6,5,7])
print(">>> ", np.maximum(a,b))

print("----------------------")
a = np.array([3,2,5,2,7,4,7])
b = np.array([0,9,3,1,6,5,7])
c = np.greater(a,b)
print(">>> ", c)
print(">>> ", a[c])

a = np.array([-3.2, 53, -3.6, 68, -4.5, 6.8571, -1.56, 8.4, -7])
print("...",np.rint(a))

A = np.ones(3) * 1
B = np.ones(3) * 2
C = np.ones(3) * 1
D = np.ones(3) * 1

print("A:",A)

np.add(A, B, out=C)
np.subtract(A,B, out=D)
print("C:",C)
print("D:",D)

print(np.divide(C, D))
