#list : ordered,mutalbe,allows duplicate elements
mlist=["banana",'cherry']
#print(mlist)
mylist=list()
mylist1=[7,2,4,6,9,0]
#print(mylist)
#print(mylist1)
item=mylist1[0]
#print(item)

for i in mylist1:
    print(i)
    
if "banana" in mylist1:
    print("yes")
else:
    print("no")
    
#print(len(mylist1))
mylist1.append("lemon")
#print(mylist1)

mylist1.insert(1,"cherry")
#print(mylist1)

mylist1.pop()
#print(mylist1)

mylist1.remove("cherry")
#print(mylist1)

#mylist1.clear()
#print(mylist1)

mylist1.reverse()
#print(mylist1)

mylist1.sort()#this changes original list
#print(mylist1)

#new_list=[0]*5
#print(new_list)

#old_list=[1,2,3,4,5]
#this_list=new_list+old_list
#print(this_list)

new_list=[1,2,3,4,5,6,7,8,9]

a=new_list[1:5]#1 ko include kregi 5 ko exclude
b=new_list[::2]#step index
c=new_list[::-1]#step index for reversing list
print(a)
print(b)
print(c)

d=[1,2,3,4,5]
print(d)
e=d.copy()
e=list(d)
e=d[:]
print(e)
e.append("lemmon")
print(e)
print(d)

#list comprehension
d=[1,2,3,4,5]
g=[i*i for i in d]
print(g)
