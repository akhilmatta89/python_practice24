"""
python is a general purpose language, open source language
Not used for any specific purpose
Can be used to develop any thing
It is high level language(No need of compiling, memory management etc)
Dynamically typed language(No need to externally saying the datatypes PVM takes care of it once we assign the value)
Easily understandable language
Support functional and object orientied approach
Has minimal keywords around 30+
easy to read and write
Platform independent
extensive community and library support
"""

"""
DATATYPES
----------

numeric datatypes
    - int
    - float
    -complex
text datatypes
    - str
sequence datatypes
    - list
    - tuple
    - range
    
mapping types
    - dict
set type
    - set
    - frozenset
boolean type
    - bool  
"""

""" Bytes"""
b = [1, 2, 3]
by = bytes(b)
print(type(b))
print(type(by))
print(by[0])
print(id(b))

# Cannot change once value is created
# by[0] = 100 # uncomment to see the error
print(by)

""" ByteArray"""
ba = [1, 2, 3]
print(id(ba))

bay = bytearray(ba)
print(ba[1])
bay[1] = 100  # Can change the value
print(bay[1])

""" list """
mylist = [1, 2, 3]  # list
print(mylist[1])  # fetches the entity present in 1 index location
# list is mutable that means it can be changed
mylist[1] = 100
print(mylist)

# we can add the values to the list in specific index
mylist.append(200)
mylist.append(400)
print(mylist)

mylist.extend([500, "akhil"])
print(mylist)

# duplicate values can be added as well

mylist.append(500)
print(mylist)

""" ---------------------tuple------------------------ """
tup = (1, 2, 3)
print(type(tup))

# This immutable
# can say this as readonly version of list

print(tup[1])
# tup[1] = 500 # cannot chnage the existing value
print(tup)

tup2 = tup.__add__((100, 200))  # Can add to other tuple but not to the existing tuple
print(tup2)

""" ---------------------range--------------------- """
r = range(1, 20, 3)  # Deafult is 1 and is immutable in nature
print(r)

for i in r:
    print(i)

""" ---------------------set--------------------- """
s = {1, 2, 3, 4, 100, 800}

print(type(s))
print(s)
# insertion order not preserved
# No duplicated allowed
# mutable
#  no indexing concept

s.add(1000)
print(s)
print(id(s))

s.update(s, {1500, 2500})  # 2 sets can be added  using update
print(s)
print(id(s))

s.remove(2500)
print(s)

s.add(1000)
print(s)

""" ---------------------frozenset--------------------- """
fs = frozenset({1,2,3})
print(fs)

# same as set but immutable

""" ---------------------dict--------------------- """

my_dict = {"name": "akhil",
           "age":29,
           "salary": "1389500",
           "tasks":["retry", "log-aggregation"],
           }
print(my_dict)

print(my_dict["tasks"])

my_dict2 = {1:"1st value",
            2:"2nd value"}
print(my_dict2[1])
print(my_dict2[2])

my_dict2 = {1.5:"true value",
            2.5:"2nd value"}
print(my_dict2[1.5])
print(my_dict2[2.5])

my_dict.update({"company":"UST"})
print(my_dict)

print(my_dict.items())
print(my_dict.pop("company"))
print(my_dict)
