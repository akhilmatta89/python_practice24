"""
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List,
    Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.
Sets are unordered, so you cannot be sure in which order the items will appear.
Set items are unordered, unchangeable, and do not allow duplicate values.
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
"""

fruits = {"apple", "banana", "cherry", "strawberry", "raspberry"}
print(fruits)
print(len(fruits))  # Get the Length of a Set
print(type(fruits))  # Get the Type of a Set

# Duplicates Not allowed
names = {"akhil", "mahesh", "sumnath", "akhil"}
print(names)

# The values True and 1 are considered the same value in sets, and are treated as duplicates:
my_set = {"akhil", True, 25, False, 1, 0}
print(my_set)

# We have a inbuilt method called set to create a set
my_inbuilt_set = set(("akhil", "Reddy", True, False))
print(my_inbuilt_set)

# Access Set Items
# You cannot access items in a set by referring to an index or a key.
#
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
#   by using the in keyword.

thisset = {"apple", "banana", "cherry"}
# Using a for loop
for x in thisset:
    print(x)

# using a membership operator we can see whether value is present in set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#  Once a set is created, you cannot change its items, but you can add new items.
fruits = {"apple", "banana", "cherry"}
other_fruit = "orange"
fruits.add(other_fruit)
print(fruits)

# Add one set to other set
fruits = {"apple", "banana", "cherry"}
tropical_fruits = {"Pineapple", "mango"}
fruits.update(tropical_fruits)
print(fruits)

# Add any iterable
# The object in the update() method does not have to be a set,
# it can be any iterable object (tuples, lists, dictionaries etc.).
fruits = {"apple", "banana", "cherry"}
tropical_fruits = ["Pineapple", "mango"]
fruits.update(tropical_fruits)
print(fruits)

# Removing items from a set
# If the item to remove does not exist, remove() will raise an error.
fruits = {"apple", "banana", "cherry"}
fruits.remove("apple")
print(fruits)
try:
    fruits.remove("mango")
except Exception as ex:
    print("Mango is not present in set so set remove is throwing error")

# Remove item by using the discard() method:
# If the item to remove does not exist, discard() will NOT raise an error.
fruits = {"apple", "banana", "cherry", "strawberry", "raspberry"}
fruits.discard("raspberry")
print(fruits)
try:
    fruits.discard("mango")
    print("Discard will not throw any error if the item is not present")
except Exception as ex:
    print("Mango is not present in set so set remove is throwing error")

"""
You can also use the pop() method to remove an item, but this method will remove a random item, 
    so you cannot be sure what item that gets removed.

The return value of the pop() method is the removed item.
Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
"""
names = {"akhil", "mahesh", "sumanth", "akhil"}
print(names)
poped_item = names.pop()
print(poped_item)

# The clear() method empties the set:
names = {"akhil", "mahesh", "sumanth", "akhil"}
print(names.clear())

# The del keyword deleted the entire set
names = {"akhil", "mahesh", "sumanth", "akhil"}
print(names)
del names
try:
    print(names)
except:
    print("Obviously throws error as we deleted names")

# Looping through sets
names = {"akhil", "mahesh", "sumanth", "akhil"}
for i in names:
    print(i)

# Joining 2 sets
#  Both union() and update() will exclude any duplicate items.
fruits = {"apple", "banana", "cherry"}
tropical_fruits = {"Pineapple", "mango","apple"}
using_union = fruits.union(tropical_fruits) # This will not update base tuple
print(using_union)

using_update = fruits.update(tropical_fruits) # This updatees the base tuple
print(using_update)
print(fruits)

# To keep only the duplicates in both the sets we can use intersection_update(), intersection() methods
fruits = {"apple", "banana", "cherry"}
tropical_fruits = {"Pineapple", "mango","apple"}
yes = fruits.intersection_update(tropical_fruits) # this effects the base set
print("---------")
print(fruits)


fruits = {"apple", "banana", "cherry"}
tropical_fruits = {"Pineapple", "mango","apple"}
yes = fruits.intersection(tropical_fruits) # this will not effect the base set
print("---------")
print(fruits)
print(yes)

#  Keep All, But NOT the Duplicates
#  The symmetric_difference_update(), symmetric_difference() methods will keep only the elements that are NOT present in both sets.
fruits = {"apple", "banana", "cherry"}
tropical_fruits = {"Pineapple", "mango","apple"}
yes = fruits.symmetric_difference_update(tropical_fruits) # this will effect the base set
print("---------")
print(fruits)
print(yes)

fruits = {"apple", "banana", "cherry"}
tropical_fruits = {"Pineapple", "mango","apple"}
yes = fruits.symmetric_difference(tropical_fruits) # this will not effect the base set
print("---------")
print(fruits)
print(yes)
