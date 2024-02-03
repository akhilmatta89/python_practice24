# list:
"""
- Lists are used to store multiple items in a single variable.
- Lists are one of 4 built-in data types in Python used to store collections of data,
    the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
- Lists are created using square brackets:
"""

thislist = ["apple", "banana", "cherry"]
print(thislist)

"""
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
"""

# list supports different types of datatypes in it.

list1 = ["akhil", 100, True, False, 1.0]
print(list1)

list2 = [[1, 2, 3], (4, 5, 6),
         {"name": "akhil", "age": 28, "org": "UST", "sal": 16867}]  # list also supports list, tuple,dict inside it.
print(list2)

"""
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
"""

# It allows duplicates
fruits = ["akhil", "banana", "cherry", "apple", "kiwi", "cherry"]
print(fruits)

# To find the length of the list we use inbuilt function called len
print(len(fruits))

# To find the type we use type function which is inbuilt
print(type(fruits))

# we can also create list with the inbuilt method.

veggies = list(("carrot", "cabbage", "cauliflower", "tomato"))
print(veggies)
print(type(veggies))

# Accessing the list items
"""
    - using slicing
    - using insert method
    
"""
# accessing list elements from front and back is also possible
# the first element is indexed as 0 second as 1 and so on
# from back when you want to access the indexing starts from -1
# we can also provide range and see what all elements are there in that range
print(fruits[0])
print(fruits[-1])
print(fruits[2:6])
print(fruits[-4:-2])
print(fruits[:4])
print(fruits[4:])

# membership operator comes in use here

if "apple" in fruits:
    print("Yes apple is present here")

if "avocado" not in fruits:
    print("Avocado is not present in fruits list")

# we can also chnage elements in list
fruits = ["apple", "banana", "cherry", "apple", "kiwi", "cherry"]
fruits[3] = "grapes"
fruits[-1] = "Cherry"
fruits[0:3] = ("Akhil", "Banana", "Cherry")
# The length of the list will change when the number of items inserted does not match the number of items replaced.
fruits[4:7] = ("Akhil", "Banana", "Cherry", "Mango")
print(fruits)

# we can also add elements using insert method but giving its index
fruits = ["apple", "banana", "cherry", "apple", "kiwi", "cherry"]
fruits.insert(1,"Banana")
print(fruits)


# Adding list items
"""
    - Append
    - Extend
"""
# To add an item to the end of the list, use the append() method
# Append takes only one argument as its input

fruits = ["apple", "banana", "cherry", "apple", "kiwi", "cherry"]
fruits.append("pineapple")
print(fruits)

# We can also add insert to insert elements
fruits = ["apple", "banana", "cherry", "apple", "kiwi", "cherry"]
fruits.insert(1,"Banana")
print(fruits)

# Extend
# To combine to lists we can use extend
# using extend we can add any iterable to the list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist.extend(("Avocado", "blackberry"))
print(thislist)

# Removing list items
"""
    - remove
    - pop
    - del
    - clear
"""

# The remove() method removes the specified item.
# indexing is not present
# if values is not present raises value error
# doesnt return anything after removing element from the list
thislst = thislist.copy()
print(thislst)

thislst.remove("blackberry")
print(thislst)

# pop removes the element from the list based on index.
# Raises IndexError if list is empty or index is out of range.
# If you do not specify the index, the pop() method removes the last item.
thislst.pop(-1)
print(thislst)
thislst.pop()
print(thislst)

# The del keyword also removes the specified index:
# The del keyword can also delete the list completely.
del thislst[-1]
print(thislst)

# The clear() method empties the list.
# The list still remains, but it has no content.
thislst.clear()
print(thislst)




