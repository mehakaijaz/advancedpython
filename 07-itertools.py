#itertools=product,permutations,combinations,accumulate,groupby,and infinte iterators.
#itertools= is a module that provides a set of fast, memory-efficient tools for working with iterators.
"""from itertools import product
a=[1,2]
b=[3,4]
prod=product(a,b,repeat=2)
print(prod)#yha object milega
print(list(prod))#yha product of list milega"""

"""from itertools import permutations
a=[1,2,3]
b=[3,4]
perm=permutations(a,2)
print(perm)#yha object milega
print(list(perm))#yha permutations of list milega

from itertools import combinations, combinations_with_replacement
a=[1,2,3,4]
comb=combinations(a,2)
print(comb)#yha object milega
print(list(comb))
combwr=combinations_with_replacement(a,2)
print(list(combwr))"""

"""from itertools import accumulate
import operator
a=[1,2,4,3,5]
acc=accumulate(a,func=operator.mul)
print(acc)#yha object milega
print(list(acc))"""

"""from itertools import groupby

def smaller_than_3(x):
    return x<3

a=[1,2,4,3,5]
group_obj=groupby(a,key=smaller_than_3)
for key,value in group_obj:
    #print(key,value)#yha object milega
    print(key,list(value))"""
    
    
from itertools import count,cycle,repeat
for i in count(10):
    print(i)   
    if i==15:
        break
    
#a=[1,2,3,4]
#for i in cycle(a):
    #print(i)

a=[1,2,3,4]
for i in repeat(1,4):
    print(i)