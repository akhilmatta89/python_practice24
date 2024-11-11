mylist = [i for i in range(10) if i%2 == 0]
print(mylist)

squares = [i**2 for i in range(10)]
print(squares)

makeupper = [word.upper() for word in ["akhil", "reddy"]] # using functions in list comprehension
print(makeupper)

# Nested list comprehension
nestedlist = [[1,2,3], [4,5,6], [7,8,9]]
flattened_list = [x for i in nestedlist for x in i]
print(flattened_list)

# Print even or odd
mylist = ["EVEN:{}".format(i) if i%2 == 0 else "ODD:{}".format(i) for i in range(11) ]
print(mylist)

mylist = [i**2 for i in range(10) if i%2 == 0]
print(mylist)


