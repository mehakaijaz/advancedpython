# string : ordered , immutable ,text rep
"""mystring="     hello world"
char=mystring[1:5]
print(char)
name= "tome"
sense=mystring + "" + name
print(sense)
if 'e'in mystring:#substring k lie bhi yehi use kr ste hai
    print("yes")
else:
    print("no")
    
mystring="     hello world   "
mystring2=mystring.strip()
print(mystring2)
print(mystring2.replace("world","company"))
print(mystring2.count('o'))#ye no of char dega
print(mystring2.find("o"))#ye index dega
print(mystring2.startswith("h"))
print(mystring2.endswith('o'))
print(mystring2.upper())
print(mystring2.lower())""" 
"""mystring="     hello world is vet   "
mystring2=mystring.split()
newstring=" ".join(mystring2)
print(mystring2)
print(newstring)"""
from timeit import default_timer as timer
mtlist=["a"]*6
print(mtlist)
mystring=""
#bad coding
start=timer()
for i in mtlist:
    mystring +=i

stop=timer()
print(stop-start)

#good coding
start=timer()
mystring="".join(mtlist)#much clear and much faster
print(mystring)
stop=timer()
print(stop-start)