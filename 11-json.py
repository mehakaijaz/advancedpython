import json
"""person={
    
    "name": "John",
    "age": 30,
    "city": "New York",
    "haschildren":False
}

personjson=json.dumps(person , indent=4)
print(personjson)

#with open('person.json','w') as file:
 #   json.dump(person,file,indent=4)
 
with open('person.json','r') as file:
   #json.dump(person,file,indent=4)
    person=json.loads(personjson)
    print(person)"""

class Users:
    def __init__(self,name,age):
        self.name=name
        self.age=age
user=Users('max',20)

def encode_user(o):
    if isinstance(o,Users):
        return {'name':o.name,"age":o.age,o.__class__.__name__:True}
    else:
        raise TypeError('Object of type Users is not Json serializable')
    
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o,Users):
            return {'name':o.name,"age":o.age,o.__class__.__name__:True}
        return JSONEncoder.default(self,o)
    
    
#userjson=json.dumps(user, default=encode_user)
userJson=UserEncoder().encode(user)
print(userJson)

user=json.loads(userJson)
print(user)