# In this file i will do operations on list whereas if you want to know the basics of integer please go and refer
# _3_datatypes.py file for basics

#In Python, you can perform various operations on integers. Here are some common integer operations with examples:

# Airthematic operation
print("------------------------------- Airthematic Operations -----------------------------")
x = 5
y = 2

# Addition
print(x+y)

# Subtraction
print(x-y)

# Multiplication
print(x*y)

# Division
print(x/y)

# Floor Division (returns an integer)
result_floor_div = 15 // 2
print(result_floor_div)  # Output: 7

# Modulus (remainder of the division)
result_mod = 17 % 5
print(result_mod)  # Output: 2

# Exponentiation
result_exp = 2 ** 3
print(result_exp)  # Output: 8

# Comparison operation
print("------------------------------- Comparison Operations -----------------------------")

comp1 = (5==5)
print(comp1)

comp2 = (5!=5)
print(comp2)

comp3 = (5>10)
print(comp3)

comp4 = (5>=5)
print(comp4)

comp5 = (5<10)
print(comp3)

comp6 = (5<=5)
print(comp4)

# Assignment Operators
print("------------------------------- Assignment Operations -----------------------------")
a = 5
print(a)

a+=3
print(a)

a-=3
print(a)

a*=3
print(a)

a/=3
print(a)

import random
import math
print(random.randint(1,6))
print("absolute value of -5.2 is : ", abs(-5.2))

print("The max value among 1,2,3,4,5 is: ", max(1,2,3,4,5))
print("The min value among 1,2,3,4,5 is: ", min(1,2,3,4,5))

print("we can also find power value of numbers", pow(2,3)) #its something like 2 to the power 3
print("we can also find squareroot of given number ", math.sqrt(25)) #this results in boolean value

print("we can also find factorial of given number", math.factorial(5))

print("Divmod returns a tuple containing the quotient and the remainder",divmod(17, 5))

print("we can also round off the number", round(5.25678))

print("we can also the sum the values", sum([2,3,4,5,6,7]))

print("converting string to int", int("123"))
# int - constructs an integer number from an integer literal, a float literal (by removing all decimals),
        # or a string literal (providing the string represents a whole number)
#float - constructs a float number from an integer literal, a float literal or a string literal
        # (providing the string represents a float or an integer)


"""
summary:
- we can perform airthematic, comparision and assignment operations in integer datatype.
- some inbuilt method names which performs some operations are
    -randint
    -abs
    -max
    -min
    -round
    -divmod
    -sum
    -factorial
    -sqrt
    -pow
"""
