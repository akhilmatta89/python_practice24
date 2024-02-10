"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:
Dictionary items are ordered, changeable, and do not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
Dictionaries cannot have two items with the same key:
"""
car_dict = {"brand": "maruthi",
            "model": "breeza",
            "year": 2022}
print(car_dict)

# To fetch the values we have 2 types
# 1
print(car_dict["model"])  # if key is not present raises key error
# 2
print(car_dict.get("model"))  # if key is not present returns None

# Duplicate values will overwrite existing values:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

# To find the length of the dictionary
print(len(thisdict))

# To find the type
print(type(thisdict))

# The values in dictionary items can be of any data type:
car_dict = {"brand": "maruthi",
            "model": "breeza",
            "electric": False,
            "colors": ["red", "black", "white"],
            "year": 2022,
            "cc": 1497.82}
print(car_dict)

# we cal also directly create dict with dict inbuilt method
with_dict_method = dict(name="akhil", age=28, org="UST")
print(with_dict_method)
print(type(with_dict_method))

# Access Dictionary Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
print(with_dict_method['name'])
print(with_dict_method.get("name"))

# Keys Method
# The keys() method will return a list of all the keys in the dictionary.
print(with_dict_method.keys())
# The list of the keys is a view of the dictionary, meaning that any changes done
# to the dictionary will be reflected in the keys list.

# values method
# The values() method will return a list of all the values in the dictionary.
print(with_dict_method.values())

# items method
# The items() method will return each item in a dictionary, as tuples in a list.
print(with_dict_method.items())

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
car_dict = {"brand": "maruthi",
            "model": "breeza",
            "electric": False,
            "colors": ["red", "black", "white"],
            "year": 2022,
            "cc": 1497.82}
if "year" in car_dict:
    print("Yes, year is present in this car dictionary")

# Change Values
# You can change the value of a specific item by referring to its key name:
car_dict["cc"] = 1498.00
print(car_dict)

# Update
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
car_dict.update({"year":2023})
print(car_dict)

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
car_dict["seater"] = 5
print(car_dict)

# Removing items from dictionary
# pop
# The pop() method removes the item with the specified key name:
car_dict.pop("seater")
print(car_dict)

# The popitem() method removes the last inserted item
car_dict.popitem()
print(car_dict)

# del
# The del keyword removes the item with the specified key name:
del car_dict["electric"]
print(car_dict)

# del can delete the complete dictionary as well
del car_dict
try:
    print(car_dict) #this will cause an error because "thisdict" no longer exists.
except:
    print("this will cause an error because \"car_dict\" no longer exists.")

# clear
# clear method empties the dictionary
car_dict = {"brand": "maruthi",
            "model": "breeza",
            "year": 2022}
print(car_dict)
car_dict.clear()
print(car_dict)

# To Copy the dictionaries
"""
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, 
    and changes made in dict1 will automatically also be made in dict2.
There are ways to make a copy, one way is to use the built-in Dictionary method copy().
"""
car_dict = {"brand": "maruthi",
            "model": "breeza",
            "electric": False,
            "colors": ["red", "black", "white"],
            "year": 2022,
            "cc": 1497.82}
copied_car_dict = car_dict.copy()
print(copied_car_dict)
print(id(car_dict))
print(id(copied_car_dict))

# Another way to make a copy is to use the built-in function dict().
other_copied_dict = dict(car_dict)
print(other_copied_dict)
print(id(car_dict))
print(id(other_copied_dict))

