#tuple=ordered,immutalbe,allows duplicate elements
'''mytuple=tuple(['max',28,89])
print(mytuple)
item=mytuple[0]
print(item)

for i in mytuple:
    print(i)
    
if "max" in mytuple:
    print("yes")   
else:
    print("no")
    
my_tuple=(1,2,3,5,7,8,9,9,9,9)
print(len(my_tuple))
print(my_tuple.count(9))
print(my_tuple.index(9))
mylist=list(my_tuple)
print(mylist)
my_tuple2=tuple(mylist)
print(my_tuple2)
'''
#slicing with tuple
'''my_tuple=(1,2,3,5,7,8,9,4,6,0)
b=my_tuple[2:5]
c=my_tuple[::3]
print(b)
print(c)
#unpacking
tuple2="mehak",67,"lives"
name,age,city=tuple2
print(name,age,city)
a=(1,2,3,4,5)
i1,*i2,i3=a
print(i1)
print(i2)
print(i3)'''
# working with tuples amd list togther ,tuple is better than list for large data
import sys
my_list=[0,1,2,"hekko",True]
my_tuple=(0,1,2,"hekko",True)
print(sys.getsizeof(my_list),"bytes")
print(sys.getsizeof(my_tuple),"bytes")

import timeit
print(timeit.timeit(stmt="[1,2,3,4,5]",number=100))
print(timeit.timeit(stmt="(1,2,3,4,5)",number=100))