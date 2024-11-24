def topTen():
    i = 1
    while i <= 10:
        yield i
        i+=1

for i in topTen():
    print(i)