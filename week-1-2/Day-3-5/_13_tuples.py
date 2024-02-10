"""
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

Tuple items are ordered, unchangeable, and allow duplicate values.(When we say that tuples are ordered, it means that
    the items have a defined order, and that order will not change.)

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.(Tuples are unchangeable,
    meaning that we cannot change, add or remove items after the tuple has been created.)

Since tuples are indexed, they can have items with the same value:
"""

# tuple basic example
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")  # Allows duplicate values
print(thistuple)

print(len(thistuple))  # Returns the length of the tuple.
print(type(thistuple))  # Returns the type.

# When you have a single item in a tuple you need to add comma or else python doesn't treat that as tuple
print(type(("akhil")))  # This returns as a string
print(type(("akhil",)))  # This returns tuple

#  A tuple can contain different data types:
tup = (
"akhil", 10, 25.6, True, ["Reddy", "Akhil"], ("mahesh", "netha"), {"sumanth", "reddy"}, {"name": "akhil", "age": 28})
print(tup)
print(type(tup[4]))  # We can access the variables and its types

# We have a inbuilt function called tuple where we can create a tuple
list_to_tup = tuple(["akhil", "reddy"])
print(list_to_tup)
print(type(list_to_tup))

set_to_tup = tuple({"akhil", "reddy"})
print(set_to_tup)
print(type(set_to_tup)) # same like this we can create tuples with any datatype.


# Accessing the tuples
# You can access tuple items by referring to the index number, inside square brackets:
tup = (
"akhil", 10, 25.6, True, ["Reddy", "Akhil"], ("mahesh", "netha"), {"sumanth", "reddy"}, {"name": "akhil", "age": 28})

print(tup[1])  # Positive indexing
print(tup[-1])  # Negative indexing
print(tup[-1].get("name"))
print(tup[1:4])  # Accessing using index ranges
print(tup[:4])  # first item till 4-1 item
print(tup[4:])  # 4th item till last
print(tup[-4:-1])  # Range of Negative Indexes


# Check if item exists
if True in tup:
    print("Yes boolean value is present")

if False in tup:
    print("Yes boolean value is present")


# Updating tuples
# As the tuples are immutable(un changeable) we cannot modify it but there is a workaround for it.
# The workaround is like convert list to tuple make changes and convert back to tuple.

fruits = ("Apple", "Banana", "Cherry")
fruits_list = list(fruits)
print(fruits_list)
fruits_list.append("Grapes")
fruits = tuple(fruits_list)
print(fruits)

# Updating the value inside the tuple
fruits_list  = list(fruits)
fruits_list[1] = "Orange"
fruits = tuple(fruits_list)
print(fruits)

# Adding tuple inside a tuple
names = ("akhil", "mahesh", "sumanth")
name = ("Jeevan",)
all_names = names + name
print(all_names)

# Remove Items from tuple
fruits = ("Apple", "Banana", "Cherry")
fruits_lst = list(fruits)
fruits_lst.remove("Cherry")
fruits = tuple(fruits_lst)
print(fruits)

# Removing the total tuple
del fruits
# print(fruits) # This will raise error as in above line we performed del operation


# Unpacking the tuples
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# If the number of variables is less than the number of values, you can add an * to the variable name and the
#   values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until
#   the number of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)








