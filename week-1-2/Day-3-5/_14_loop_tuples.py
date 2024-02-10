# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.

thistuple = ("apple", "banana", "cherry")
for x in thistuple: # Iterating through the tuple
  print(x)

# Loop Through the Index Numbers
for x in range(len(thistuple)):
    print(thistuple[x])


# While loop
"""
You can loop through the tuple items by using a while loop.

Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the 
    tuple items by referring to their indexes.

Remember to increase the index by 1 after each iteration.
"""
print("----------------------------- while loop -----------------------")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
i = 0
while i < len(fruits):
    print(fruits[i])
    i+=1