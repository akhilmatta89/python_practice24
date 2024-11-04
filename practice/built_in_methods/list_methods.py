"""------------------------APPEND----------------------------"""
# The append() method in Python is used to add a single item to the end of a list.
# It modifies the original list in place, rather than creating a new list.
mylist = ["akhil","reddy", True, 25, 10.2, {"salary":"N/A"}]
mylist.append(["jaya", "reddy"])
print(mylist)

"""------------------------INDEX----------------------------"""
# The index() method in Python is used to find the position of the first occurrence of a specified element in a list.
# if element not present it will raise value error
# we can also add start and end also to search in partcular range
mylist = ["akhil","reddy", True, 25, 10.2, {"salary":"N/A"}, 25]
print(mylist.index(25))

mylist = ["akhil","reddy", True, 25, 10.2, {"salary":"N/A"}, 25]
try:
    mylist.index("UST")
except Exception as ex:
    print("the error is", ex)
finally:
    print("finally block executed")

mylist = ["akhil", "reddy", True, 25, 10.2, {"salary": "N/A"}, 25]
print(mylist.index(25,4,7))

"""------------------------COUNT----------------------------"""
# The count() method in Python is used to count the number of times a specified element appears in a list.

mylist = ["akhil", "reddy", True, 25, 10.2, {"salary": "N/A"}, 25]
print(mylist.count(25))

mylist = ["akhil", "reddy", True, 25, 10.2, {"salary": "N/A"}, 25,  {"salary": "N/A"}]
print(mylist.count(True))

"""------------------------POP----------------------------"""
# The pop() method in Python is used to remove and return an element from a list by index.
# If no index is specified, it removes and returns the last item in the list.
mylist = ["akhil", "reddy", True, 25, 10.2, {"salary": "N/A"}, 25]
mylist.pop()
print(mylist)

mylist = ["akhil", "reddy", True, 25, 10.2, {"salary": "N/A"}, 25]
data = mylist.pop(5)
print(data)
print(mylist)

"""------------------------REMOVE----------------------------"""
# The remove() method in Python is used to remove the first occurrence of a specified value from a list.
# If the value is not found, it raises a ValueError.
mylist = ["akhil", "reddy", True, 25, 10.2, {"salary": "N/A"}, 25]
data = mylist.remove(True)
print(data)
print(mylist)

mylist.remove({"salary":"N/A"})
print(mylist)

mylist.remove(25)
print(mylist)

"""------------------------EXTEND----------------------------"""
# The extend() method in Python is used to add multiple elements to the end of a list. Unlike append(),
# which adds a single element (even if that element is a list), extend() takes an iterable (like a list, tuple, or set)
# and adds each of its elements to the list.
mylist = ["akhil", "reddy", True, 25, 10.2, {"salary": "N/A"}, 25]
mylist.extend([1,2,3,4])
print(mylist)

mylist = ["akhil", "reddy", True, 25, 10.2, {"salary": "N/A"}, 25]
mylist.extend([])
print(mylist)

"""------------------------COPY----------------------------"""
#The copy() method in Python is used to create a shallow copy of a list. A shallow copy means that a new list is created
# , but the elements in the new list are references to the original objects in the original list.
# Therefore, changes to mutable objects within the copied list will affect the original list.
mylist = ["akhil", "reddy", True, 25, 10.2, {"salary": "N/A"}, 25]
mylist2 = mylist.copy()
print(mylist)
print(mylist2)

mylist.append("new one")
print(mylist)
print(mylist2)

mylist2.append("second new one")
print(mylist)
print(mylist2)


new_original_list = [["akhil", "reddy"],["matta", 2672]]
copied_list = new_original_list.copy()
print(new_original_list)
print(copied_list)

copied_list[1][0] = "car"
print(new_original_list)
print(copied_list)

"""------------------------CLEAR----------------------------"""
mylist = ["akhil", "reddy", True, 25, 10.2, {"salary": "N/A"}, 25]
mylist.clear()
print(mylist)

new_original_list = [["akhil", "reddy"],["matta", 2672]]
copied_list = new_original_list.copy()
print(new_original_list)
print(copied_list)

new_original_list.clear()
print(new_original_list)
print(copied_list)

"""------------------------REVERSE----------------------------"""
# The reverse() method in Python is used to reverse the elements of a list in place.
# This means that the original list is modified and no new list is created.
mylist = ["akhil", "reddy", True, 25, 10.2, {"salary": "N/A"}, 25]
mylist.reverse()
print(mylist)

"""------------------------SORT----------------------------"""
my_list = [5, 2, 9, 1, 5, 6]
my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

mylist = ["reddy", "akhil"]
mylist.sort()
print(mylist)

data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

data.sort(key=lambda x:x["age"])
print(data)

"""------------------------INSERT----------------------------"""
mylist = ["akhil", "reddy", True, 25, 10.2, {"salary": "N/A"}, 25]
mylist.insert(1, "matta")
print(mylist)