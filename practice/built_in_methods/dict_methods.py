"""------------------------COPY----------------------------"""

mydict = {"name":"akhil"}
newdict = mydict.copy()
print(newdict.items())
print(id(mydict))
print(id(newdict))

"""------------------------POP----------------------------"""
mydict = {"name":"akhil", "age" : 28}
print(mydict.pop("name"))
print(mydict)

"""------------------------CLEAR----------------------------"""
mydict = {"name":"akhil", "age" : 28}
mydict .clear()
print(mydict)

"""------------------------UPDATE----------------------------"""
mydict = {"name":"akhil", "age" : 28}
mydict.update({"company": "UST"})
print(mydict)

"""------------------------GET----------------------------"""
mydict = {"name":"akhil", "age" : 28}
print(mydict.get("name"))

"""------------------------ITEMS----------------------------"""
mydict = {"name":"akhil", "age" : 28}
print(mydict.items())

"""------------------------KEYS----------------------------"""
mydict = {"name":"akhil", "age" : 28, "company": "UST"}
print(mydict.keys())

"""------------------------VALUES----------------------------"""
mydict = {"name":"akhil", "age" : 28}
print(mydict.values())

"""------------------------SETDEFAULT----------------------------"""
mydict = {"name":"akhil", "age" : 28}
mydict.setdefault("name", "reddy")
print(mydict)

mydict.setdefault("company", "UST")
print(mydict)

names = ["Akhil", "Bob", "Anay", "Brain", "Charlie"]
groupnames = {}
for name in names:
    first_letter = name[0]
    groupnames.setdefault(first_letter, []).append(name)
print(groupnames)

"""------------------------POPITEM----------------------------"""
mydict = {"name":"akhil", "age" : 28, "company": "UST"}
mydict.popitem()
print(mydict)

"""------------------------POPITEM----------------------------"""
# The fromkeys method in Python is a class method for dictionaries that creates a new dictionary with
# specified keys, all initialized to a single specified value.

myvalues = ["name", "age", "company"]
mydict = dict.fromkeys(myvalues)
print(mydict)