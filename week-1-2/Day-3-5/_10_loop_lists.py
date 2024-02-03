
# For loop
fruits = ["apple", "banana", "cherry", "apple", "kiwi", "cherry"]
for fruit in fruits:
    print(fruit)

# We can also range it in the range of list.
for i in range(len(fruits)):
    print(fruits[i])

# While loop
"""
You can loop through the list items by using a while loop.
Use the len() function to determine the length of the list, 
    then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration.
"""
print("-----------------------while loop----------------")
fruits = ["apple", "banana", "cherry", "apple", "kiwi", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i+=1

print("---------------------------------------list comprehension ---------------------------------------------")
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

fruits = ["apple", "banana", "cherry", "apple", "kiwi", "cherry"]
[print(x)for x in fruits if x.startswith("a")]

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

print("---------------------------------------one way ---------------------------------------------")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

print("---------------------------------------other way ---------------------------------------------")
newlist_2 = [x for x in fruits if "a" in x]
print(newlist_2)
