name = "akhil"
it = iter(name)
print(it.__next__())
print(it.__next__())
print(it.__next__())
"""---------------------------------------------------------------------------------------------"""
class Test:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration
        self.x = x + 1
        return x
for i in Test(15):
    print(i)

"""---------------------------------------------------------------------------------------------"""
class Test_2:
    def __init__(self, current, end):
        self.current = current
        self.end = end
    def __iter__(self):
        return self

    def __next__(self):
        currentval = self.current
        if self.current > self.end:
            print(f"stoping execution as self.current is {self.current}")
            raise StopIteration
        self.current+=1
        return currentval
print("*"* 40)
for i in Test_2(1,10):
    print(i)




