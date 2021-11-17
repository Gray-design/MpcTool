import numpy as np


# def func(array, array_min):
#     array[np.argmin(array)] = array_min
#     return array
#
# ls = [eval(i) for i in input().split(",")]
# n = np.array(ls)
# print(func(n, 3))

r = np.arange(1, 31)
a = np.round(np.pi * r ** 2, 2)
print(a)

a = np.arange(10, 110, 10)
b = np.arange(10, 110, 10)
print(a)