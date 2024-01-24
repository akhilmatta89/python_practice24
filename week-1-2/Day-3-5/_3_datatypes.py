#In python we have 3 types of data types
#1. Numeric
#2. Sequence
#3. Boolean

#Numeric data types are :- Numeric data type represent the data which has numeric value.
#1. integer
#2. float
#3. complex

#Text Sequence data types are :- Text Sequence data type representing a string of Unicode characters.
#1. string

#Boolean data types are :- Boolean data type representing True or False.
#1. bool(True or False)

#sequence data types are :- Sequence data type represent the group of individual values as a single entity.
#1. list
#2. tuple
#3. range


#Python has the following built-in data types, in these categories:
#1. Text Type:	str
#2. Numeric Types:	int, float, complex
#3. Sequence Types:	list, tuple, range
#4. Mapping Type:	dict
#5. Set Types:	set, frozenset
#6. Boolean Type:	bool


#Now i ll explain each data type in detail with examples
#1. Numeric data types are :- Numeric data type represent the data which has numeric value.

#1. int :- Int data type represent the integer values. It can be any length such as 10, 2, 29, -20, -150 etc.
# Int data type can be represented in three forms, such as decimal, binary and hexadecimal.
#2. float :- Float data type represent the floating point values.
# It is specified by a decimal point. It can be either used in exponential form or normal form.
#3. complex :- Complex data type represent the complex numbers like 2+3j, 3+4j, -5+6j etc.
# In these numbers, the real part is separated by the imaginary part by using a + sign.
#2. Text Sequence data types are :- Text Sequence data type representing a string of Unicode characters.




print ("------------------------------------Numeric data types ---------------------------------------------")
x = 5 # int
print(x)
print(type(x))
y = 3.14 # float
print(type(y))
print(y)
z = 1j # complex
print(type(z))
print(z)
print("------------------------------------Text data type ---------------------------------------------")
name = "akhil"
print(type(name))
print(name)
print("we can also specify string in multi line")
other_name = """my name is akhil
iam from hyderabad
works for some organization"""
print(other_name)
print("------------------------------------Boolean data type ---------------------------------------------")
is_true = True
is_false = False
if is_true:
    print("iam inside true")

if not is_false:
    print("iam inside false")

# Boolean values often result from comparison operations:
x = 5
y = 10
#Comparison operators
print("Comparison operators with bool")
is_equal = (x == y)
is_not_equal = (x != y)
is_greater_than = (x > y)
is_less_than = (x < y)

print(is_equal)        # Output: False
print(is_not_equal)    # Output: True
print(is_greater_than) # Output: False
print(is_less_than)    # Output: True

a = True
b = False

# Logical operators
print("Logical operators with bool")
logical_and = a and b
logical_or = a or b
logical_not = not a

print(logical_and)  # Output: False
print(logical_or)   # Output: True
print(logical_not)  # Output: False

#In Function
print("In Function with bool")
def is_even(number):
    return number % 2 == 0

# Using the function with boolean values
result1 = is_even(4)
result2 = is_even(7)

print(result1)  # Output: True
print(result2)  # Output: False

print("------------------------------------Sequence data types ---------------------------------------------")
# list is mutable
# ordered collection of elements
# Lists are one of the built-in data types in Python and are commonly used to store and manipulate sequences of items.
# Lists can contain elements of different types

# Creating a empty list
list1 = []

# Creating the list with elements
list2 = [1,2.4,'akhil',2+3j,True,['akhil','reddy'],('akhil','reddy')]
print("This is the basic example of the list")
print(list2)

# Creating a list with a range of numbers
list3 = list(range(1,6))
print(list3)


# Tuple is immutable
# Ordered collection of elements
# Tuples are same like list, but they cannot be modified once they are created

# Creating a tuple
tup1 = ()
print(type(tup1))

# Creating a tuple with elements
tup2 = (1,2,3,4,5,6,7)
print(tup2)

# Creating a tuple with different datatypes
tup3 = (1,2.4,'akhil',2+3j,True,['akhil','reddy'],('akhil','reddy'))
print(tup3)


#Creating a Range
# range type is used to represent an immutable sequence of numbers.
# The range type is commonly used in for loops, list comprehensions, and when you need to generate a
    # series of numbers without explicitly creating a list.

my_range = list(range(6))
print(my_range)

my_range1 = list(range(1,6))
print(my_range1)

my_range2 = range(0, 10, 2)  # Generates even numbers from 0 to 8

print(list(my_range2))

# In range when you just specify number(n) it takes from 0 and till n-1
# if number is given like range(1,6) it goes from 1 till n-1
# there is third input for range method which adds step where we can add and remove that sequence


# Mapping Datatype
print("------------------------------------ Mapping data types ---------------------------------------------")
# In Python, a dictionary (often abbreviated as "dict") is a built-in data type that represents a collection of key-value pairs.
# They provide an efficient way to store and retrieve data based on a unique key.

# Without inbuilt function
dict1 = {"name":"John",
         "age":36,
         "male":True,
         "data":["akhil","reddy"]}
print(dict1)

# With inbuilt function
dict2 = dict(name="akhil", age=28, male=True, data=["akhil","reddy"])
print(dict2)

# Set Datatype
print("------------------------------------ Set data types ---------------------------------------------")
# set
# Creating a empty set datatype
# set is an unordered
# mutable collection of unique elements
# The set data type is defined by enclosing a comma-separated sequence of elements within curly braces {}
# Sets are used for various tasks, such as removing duplicate elements from a list checking membership,
# and performing set operations like union, intersection, and difference.

set1 = {}
print(set1)
set2 = {"apple", "banana", "cherry"}
print(set2)
print(type(set2))

# Creating an empty set
empty_set = set()

# Creating a set with elements
my_set = {1, 2, 3, 4, 5}

# Sets automatically remove duplicates
duplicate_set = {1, 2, 2, 3, 3, 4, 5, 5}

print(empty_set)      # Output: set()
print(my_set)         # Output: {1, 2, 3, 4, 5}
print(duplicate_set)  # Output: {1, 2, 3, 4, 5}

# Frozenset
# frozenset is an immutable version of a set

# Creating a frozenset
fs = frozenset([1, 2, 3, 4, 5])

print(fs)
print(type(fs))

