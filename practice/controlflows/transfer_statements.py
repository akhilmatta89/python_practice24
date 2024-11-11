# -------------------------Break-----------------------------
i = 7
for x in range(10):
    if x >= i:
        break
    else:
        print(x)

cartitems = ["rice", "dal", "chicken", "mutton"]
for item in cartitems:
    if item == "chicken":
        print("enough of items")
        break
    print(item)

totalcount = 0
totalitems = {"rice":25, "chicken":120, "dal": 33, "tomatoes":24, "brinjal": 12}
for items in totalitems.items():
    if totalcount >= 150:
        print("I dont have more than 150")
        print("the total count now is {}".format(totalcount))
        break
    totalcount+=items[1]

# -------------------------Continue-----------------------------
cartitems = ["rice", "dal", "chicken", "mutton"]
for item in cartitems:
    if item == "chicken":
        continue
    print(item)

# print odd numbers
for i in range(20):
    if i%2 == 0:
        continue
    print(i)

totalcount = 0
totalitems = {"rice": 25, "chicken": 120, "dal": 33, "tomatoes": 24, "brinjal": 12}
for items in totalitems.items():
    if totalcount >= 150:
        print("I dont have more than 150")
        continue
    totalcount += items[1]
    print(totalcount)

# -------------------------Pass-----------------------------
for i in range(10):
    if i == 2:
        pass
    print(i)

def skipmethod():
    pass