# Python has a set of built-in methods that you can use on sets.

#add()
names = {"akhil","mahesh"}
names.add("sumanth") # adds a single element to set
print(names)

# clear
names.clear() # clears the entire set.
print(names)

# copy
names = {"akhil","mahesh"}
dup_names = names.copy() # creates a copy of the set
print(dup_names)
print(id(names))
print(id(dup_names))

# difference
# Return a set that contains the items that only exist in set fruits, and not in set tropical_fruits:
# This will not effect the base set
fruits = {"apple", "banana", "cherry"}
tropical_fruits = {"Pineapple", "mango","apple"}
diff = fruits.difference(tropical_fruits)
other_diff = tropical_fruits.difference(fruits)
print("-----------------")
print(diff)
print(other_diff)
print("-----------------")


# difference_update
# This will effect the base set
"""
The difference_update() method removes the items that exist in both sets.
The difference_update() method is different from the difference() method, because the difference() method 
    returns a new set, without the unwanted items, and the difference_update() method removes the 
    unwanted items from the original set.
"""

fruits = {"apple", "banana", "cherry"}
tropical_fruits = {"Pineapple", "mango","apple"}
fruits.difference_update(tropical_fruits)
print(fruits)
print("-----------------")

# Discard
fruits = {"apple", "banana", "cherry"}
fruits.discard("apple") # Removes the item from the set
print(fruits)
print("-----------------")

# intersection
fruits = {"apple", "banana", "cherry"}
tropical_fruits = {"Pineapple", "mango","apple"}
print(fruits.intersection(tropical_fruits)) # returns the duplicate value, this will not effect the base set
print("-----------------")

# intersection_update()
# Removes the items in this set that are not present in other, specified set(s)
fruits = {"apple", "banana", "cherry"}
tropical_fruits = {"Pineapple", "mango","apple"}
print(fruits.intersection_update(tropical_fruits))
print(fruits)
print("-----------------")

# isdistjoint
fruits = {"apple", "banana", "cherry"}
tropical_fruits = {"Pineapple", "mango","apple"}
print(fruits.isdisjoint(tropical_fruits)) # Returns whether two sets have a intersection or not

fruits = {"apple", "banana", "cherry"}
tropical_fruits = {"Pineapple", "mango"}
print(fruits.isdisjoint(tropical_fruits)) # Returns whether two sets have a intersection or not
print("-----------------")


# issubset
# Return False if not all items in set x are present in set y:
fruits = {"apple", "banana", "cherry", "Pineapple", "mango","apple"}
tropical_fruits = {"Pineapple", "mango","apple"}
print(tropical_fruits.issubset(fruits))
print("-----------------")

fruits = {"apple", "banana", "cherry", "Pineapple", "mango","apple"}
tropical_fruits = {"Pineapple", "mango","orange"}
print(tropical_fruits.issubset(fruits))
print("-----------------")

# issuperset
# Return True if  all items in set x are present in set y:
fruits = {"apple", "banana", "cherry", "Pineapple", "mango","apple"}
tropical_fruits = {"apple", "banana"}
print(fruits.issuperset(tropical_fruits))
print("-----------------")

fruits = {"apple", "banana", "cherry", "Pineapple", "mango","apple"}
tropical_fruits = {"apple", "banana"}
print(fruits.issuperset(tropical_fruits))
print("-----------------")

#pop
#remove
#symmetric difference
#symetric difference update
#union
#update

