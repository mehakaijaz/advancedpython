#generator =A generator in Python is a concise iterable that produces values 
# on-the-fly using a function with the `yield` keyword, 
# enabling memory-efficient and lazy evaluation of sequences.
import sys

"""def mygen():
    yield 12
    yield 2
    
g=mygen()
print(g)#only print gen objevt
#to get values one at a time use next()
value=next(g)
print(value)
value=next(g)
print(value)

c=sum(g)
print(c)
a=sorted(g)
print(a)"""

"""def count(num):
    print('starting')
    while num > 0:
        yield num
        num -= 1
        
cd=count(4)
value=next(cd)
print(value)
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))#stop iteration"""

"""def firstn(n):
    nums=[]
    num=0
    while num< n:
        nums.append(num)
        num +=1
    return nums

def firstn_gen(n):# genrator
    num=0
    while num< n:
        yield num
        num +=1
    
print(f'function',sys.getsizeof(firstn(10)))
print(sys.getsizeof(firstn_gen(10)))"""

"""def fibonaaci(limit):
    #0,1,1,2,3,5,8
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b

fib=fibonaaci(10)
#print(next(fib))
for i in fib:
    print(i)"""
#generator expression

mygen=(i for i in range(20) if i % 2==0)
for i in mygen :
    print(i)
    
    