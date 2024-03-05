"""result=6*8
print(result)
result=6**7
print(result)
z=[1,2]*14
print(z)"""

"""def foo(a,b,*args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])
foo(1,2,3,4,six=6,seven=7)"""

#unpacking
number=[1,2,3,4,5]
begin,*middle,last=number
print(begin)
print(last)
print(middle)
mytuple=(1,2,3)#this mergring works for sets tuple and list
mylist=[4,5,6]
new_list=[*mytuple,*mylist]
print(new_list)