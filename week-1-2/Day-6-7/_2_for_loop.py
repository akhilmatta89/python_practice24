"""
Python has two primitive loop commands:
- while loops
- for loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in
    other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# The for loop does not require an indexing variable to set beforehand.
# Even strings are iterable objects, they contain a sequence of characters
for x in "banana":
  print(x)

# With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry", "kiwi", "orange", "pineapple"]
for fruit in fruits:
    if fruit == "orange":
        break
    else:
        print(fruit)

print("---------------------------------------------------------------")
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry", "kiwi", "orange", "pineapple"]
for fruit in fruits:
    if fruit == "orange":
        continue
    else:
        print(fruit)
print("---------------------------------------------------------------")

"""
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
    and ends at a specified number.
"""
for x in range(6):
    print(x)
print("---------------------------------------------------------------")
for x in range(1,6): # we can also specify from where we can start.
    print(x)

print("---------------------------------------------------------------")
for x in range(1,30,3):
    print(x)
print("---------------------------------------------------------------")
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(1,6):
    print(x)
else:print("looop completed")

# Note: The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(1,6):
    if x == 3: break
    print(x)
else:
    print("looop completed")

print("---------------------------------------------------------------")
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# for loops cannot be empty, but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error.

for x in [1,2,3]:
    pass