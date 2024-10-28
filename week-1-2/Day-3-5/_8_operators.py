"""
Operators are used to perform operations on variables and values.
Python divides the operators in the following groups:

    - Arithmetic operators
    - Assignment operators
    - Comparison operators
    - Logical operators
    - Identity operators
    - Membership operators
    - Bitwise operators
"""

# Arithmetic operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:

# Addition
print(10 + 20)

# Subtraction
print(10 - 5)

# Multiplication
print(10 * 20)

# Division
print(10 / 5) # Division operator returns float value

# Modulus # Gives the reminder
print(10 % 5)

# Exponentiation
print(2 ** 2)  # Perform power operation
print(4 ** 4)

# Floor Division
print(15 // 2)  # The floor division // rounds the result down to the nearest whole number

# Assignment operators
# Assignment operators are used to assign values to variables:

a = "akhil"  # '=' is used to assign the value to a variable
x = 5

x += 3
print(x)

x -= 3
print(x)

x *= 3
print(x)

x /= 3
print(x)

x %= 3
print(x)

x //= 3
print(x)

x **= 3
print(x)

x = 100
x &= 3
print(x)

# Comparision Operators(==, != , >, < , >=,<=)
if "akhil" == "akhil":
    print(True)
if 10 >= 5:
    print(True)
if not 10 <= 5:
    print(False)
if "Akhil" != "Reddy":
    print(True)

# Logical Operators (AND, OR, NOT)
# Logical operators are used to combine conditional statements:
if True and True: # Returns True if both statements are true
    print(True)
if True or False:  # Returns True if any of one are true
    print(True)
if not (5>2 and "akhil"=="Reddy"): # Reverse the result, returns False if the result is true
    print(True)
else:
    print(False)

# Identity Operators (IS, IS NOT)
# Identity operators are used to compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location:

x = 5
y = x

if x is y:
    print("Yes")
    print(id(x))
    print(id(y))

x = 5
y = 7
if x is y:
    print("Yes")
    print(id(x))
    print(id(y))
if x is not y:
    print("No")
    print(id(x))
    print(id(y))

# membership operators (IN,NOT IN)
# Membership operators are used to test.txt if a sequence is presented in an object
x = [1,2,3,4,5,6,7]
y = 5
if y in x:
    print("Yes")

y = 10
if y not in x:
    print("No")

fruits = ["apple", "banana", "cherry"]
fruits[0] = "Kiwi"
print(fruits)







