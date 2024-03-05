# sets : unordered, mutable,no duplicates
"""myset=set()#dictionary type
print(type(myset))
myset2=set("hello")#use it to find out different character in a word
print(myset2)
myset1=set()#set type
print(type(myset1))

myset.add(1)
myset.add(7)
myset.add(6)
myset.add(5)
myset.add(2)
myset.add(3)
print(myset)
#to remove something from set
myset.remove(3)
myset.discard(2)#it removes the element ,if doesnt find the element it does nothing
#clear(),pop()"""
"""odds={1,3,5,7,9}
evens={2,4,6,8}
primes={2,3,5,7}
#in sets actual copy is done by .copy() or set()

u=odds.union(evens)
print(u)
i=odds.intersection(primes)
print(i)"""
seta={1,2,3,4,5,6,7,8,9}
setb={1,2,3,10,11,12}
d=seta.difference(setb)
print(d)
c=seta.symmetric_difference(setb)
print(c)
seta.update(setb)
print(seta)
seta.intersection_update(setb)
print(seta)
seta.difference_update(setb)
print(seta)
print(seta.issubset(setb))# isme true false me ans aiga,isme issuperset() function bhi a
print(seta.isdisjoint(setb))
#frozenset: immutable version of a normal set
a=frozenset([1,2,3,4])
print(a)
#a.add(2)# this will give an error, no updates method(remove,copy ,delete) work here
