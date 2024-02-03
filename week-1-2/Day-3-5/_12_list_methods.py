
# append
fruits = ["apple", "banana", "cherry", "apple", "kiwi", "cherry"]
fruits.append("pineapple")
print(fruits)

# count
print(fruits.count("apple")) # Returns the occurences

# clear
print(fruits.clear())

# extend
fruits = ["apple", "banana", "cherry", "apple", "kiwi", "cherry"]
other_fruits = ["pineapple", "watermelon"]
fruits.extend(other_fruits)
print(fruits)

# insert
fruits.insert(8, "avocado")
print(fruits)

# index
print(fruits.index("cherry"))

# pop
fruits.pop(8)
print(fruits)

# remove
fruits.remove("apple")
print(fruits)

# reverse
fruits.reverse()
print(fruits)

# sort
fruits.sort()
print(fruits)

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[3:6])


