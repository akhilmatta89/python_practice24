# These are variabke which we create for 1 time use(temporary purpose)
# each time you intilaize new thing gets formed
# we can delete very easily

class Test:
    def __init__(self):
        self.name = "akhil"
        self.age = 28

    def m1(self):
        a = 10 # Local variables
        print(a)
    def m2(self):
        b = 100
        print(b)

t = Test()
t.m1()
t.m2()