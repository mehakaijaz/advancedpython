#lambda arguments:expressions

"""add10= lambda x: x + 10
print(add10(5))

def add10_func(x):
    return x+10
#these two does the same work

mul=lambda x,y,z:x*y*z
print(mul(1,2,3))

points2d=[(1,2),(5,-6),(3,4),(-7,8)]

points2d_sorted=sorted(points2d, key=lambda x:x[1])
print(points2d)
print(points2d_sorted)"""

#map(func,seq)

"""a=[1,2,3,4]
b=map(lambda x: x*2,a)
print(list(b))"""

#filter =A function that defines the filtering condition.
#An iterable (like a list, tuple, etc.) to be filtered.

"""a=[1,2,3,4,5,6]
b=filter(lambda x: x*2==6,a)
print(list(b))"""

#reduce= function is part of the functools module and is used for performing a 
# cumulative operation on a sequence of elements. 
# The reduce() function repeatedly applies a binary function to the 
# elements of an iterable, cumulatively, from left to right.

from functools import reduce
a=[1,2,3,4,5,6]
product_a=reduce(lambda x,y:x*y,a)
print(product_a)