import random


"""a= random.random()
print(a)
a= random.uniform(1,10)
print(a)
a= random.randint(1,5)#this includes upper bound in this case 5
print(a)
a= random.randrange(1,8)# this will not include upper bound
print(a)"""

#psudo random

"""mylist=list("abcdefgh")
a=random.choice(mylist)
b=random.sample(mylist,3)
c=random.choices(mylist,k=3)#it can let same element multiple time
random.shuffle(mylist)
print(mylist)
print(a)
print(b)
print(c)"""

"""random.seed(1)#this takes less time
print(random.random())
print(random.randint(1,6))
print(random.randrange(1,6))"""

import secrets #it takes more time

"""a=secrets.randbelow(10)#exclusive upper bound=an exclusive upper bound means that the highest possible value is not included in the set or range.
# if you have a range from 1 to 10 with an exclusive upper bound, 
# it includes all numbers from 1 up to (but not including) 10. So, the range would be 1, 2, 3, 4, 5, 6, 7, 8, 9.

print(a)
b=secrets.randbits(4)#it will return int will "k" random bits
print(b)
mylist=list("abcdefgh")
c=secrets.choice(mylist)#not reproduceable choice
print(c)"""

import numpy as np #for array

a=np.random.randint(0,3,(3,4))
#print(a)
arr=np.array([[1,2],[3,4],[5,6]])
print(arr)
ab=np.random.shuffle(arr)#this will never switch elements it btw therefore output will be none
print(ab)
