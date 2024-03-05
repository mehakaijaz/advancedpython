#dictionary=key-value pairs, unordered, mutable
'''mydict={"name":"nick","Age":23,"city":"newyork"}
print(mydict)
mydict2=dict(name="mary",age=12,city='newnoston')
print(mydict2)
value=mydict2["name"]
print(value)
mydict2["email"]="mu@zxy.com"
print(mydict2)
del mydict2["email"]#pop method also
print(mydict2)
mydict2.popitem()
print(mydict2)
for key in mydict.keys():#same for values =values()
 print(key)
 
for key,value in mydict.items():#
 print(key,value)'''

'''mydict={"name":"nick","Age":23,"city":"newyork"}
mydict_copy=mydict # use these functions instead = dict(mydict), copy()
print(mydict_copy)
mydict_copy["email"]="mu@zxy.com"
print(mydict_copy)
print(mydict)'''

#merge= here key value pairs are overwritten 
mydict={"name":"nick","Age":23,"city":"newyork"}
mydict2=dict(name="mary",age=12,city='newnoston')
mydict.update(mydict2)
print(mydict)

my_dict={1:1,2:4,3:9}
print(my_dict)
# in this format use actual keys oe value as stated below
value=my_dict[2]
print(value)