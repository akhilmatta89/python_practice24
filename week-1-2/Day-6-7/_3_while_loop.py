# With the while loop we can execute a set of statements as long as a condition is true.
# Note: remember to increment i, or else the loop will continue forever.

i = 1
while i <= 6:
    print(i)
    i+=1
print("---------------------------------------------------------------")

# The while loop requires relevant variables to be ready,
# In this example we need to define an indexing variable, i, which we set to 1.

# With the break statement we can stop the loop even if the while condition is true:
i = 1
while i <= 6:
    if i == 3:break
    print(i)
    i+=1
print("---------------------------------------------------------------")
# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i <= 10:
    i += 1
    if i == 5:
        continue
    print(i)
print("---------------------------------------------------------------")
# With the else statement we can run a block of code once when the condition no longer is true:
i = 0
while i <= 10:
    i += 1
    if i == 5:
        continue
    print(i)
else:
    print("Completed successfully")



