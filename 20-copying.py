"""""
org=5
cpy=org
cpy=6
print(cpy)
print(org)

#in list assignment op. works different
org=[1,2,3]
cpy=org
cpy[0]=-10
print(cpy)
print(org)"""

#shallow copy
"""import copy
org=[1,2,3]
cpy=copy.copy(org)
cpy[0]=-10

print(cpy)
print(org)

#deepcopy
import copy
org=[[1,2,3],[6,7,8,9]]
cpy=copy.deepcopy(org)
cpy[0]=-10

print(cpy)
print(org)"""

import copy
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
 
class company:
    def __init__(self,boss,employee):
        self.boss=boss
        self.empolyee=employee
        
        
p1=person('alex',89)
p2=person('joe',84)
#p2=p1 #not an actual copy makes changes in original one
p3=copy.copy(p1)#shallow copy
p3.age=12
print(p2.age)
print(p3.age)
print(p1.age)

comp=company(p1,p2)
comp_clone=copy.deepcopy(comp)#deepcopy
comp_clone.boss.age=45
print(comp_clone.boss.age)
        