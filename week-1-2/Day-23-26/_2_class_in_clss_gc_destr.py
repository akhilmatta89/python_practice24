"""
Declaring the class inside the class are called inner classes

without existing one type of object if there is no chance of existing other type then we will go for inner classes
"""


class Car:
    def __init__(self):
        print("car object creation")

    class Engine:
        def __init__(self):
            print("engine object creation")

        def engine_cc(self):
            print("engine CC method")


# calling these inner class with diff syntax
# 1)
c = Car()
e = c.Engine()
e.engine_cc()

# 2)
c = Car().Engine()
c.engine_cc()

# 3)
c = Car().Engine().engine_cc()


class Person:
    def __init__(self):
        self.name = "akhil"
        self.db = self.Dob()

    def display(self):
        print("my name is ", self.name)
        print("my dob is", self.db)

    class Dob:
        def __init__(self):
            self.dd = 16
            self.mm = 10
            self.yy = 1995

        def display(self):
            print("DOB={}/{}/{}".format(self.dd, self.mm, self.yy))


p = Person()
p.display()
db = p.db
db.display()


# Any number of classes can be created inside a class

class Human:
    print("iam human")

    def __init__(self):
        self.head = self.Head()
        self.eyes = self.Eyes()
        self.nose = self.Nose()

    class Head:
        def think(self):
            print("iam head")

    class Eyes:
        def see(self):
            print("we are eyes we can see")

    class Nose:
        def sense(self):
            print("iam nose i can smell and breathe")


h = Human()
h.head.think()
h.eyes.see()
h.nose.sense()

print("-----------------------------------garbage collection")
"""
In old languages like c++ we like developers are responsible for garbage collection wherein once the use of the variable
is completed dev should garbage if not total memory will be filled up with useless objects.

But in python PVM takes care of the garbage collection that is garbage collector
"""

# Enabling and disabling of garbage collector
# Defaultly it is enabled
import gc
print(gc.isenabled())

# To Disable
print(gc.disable())

# To enable
print(gc.enable())

print("-----------------------------------destructor")
"""
This is the special method and should be called using del
Just before destroying an object, garbage collector always calls destructor to perform cleanup.
Once destructor execution is complete then garbage collector automatically destroys it."""

import time
class Test:
    def __init__(self):
        print("Object initilization")
    def __del__(self):
        print("performing cleanup activities")

t1 = Test()
t1 = None
time.sleep(5)
print("end of the application")


"""
if the object doesnt have any reference variables then only it is eligible for GC
"""
class Test_1:
    def __init__(self):
        print("Object initilization")
    def __del__(self):
        print("performing cleanup activities")
t1 = Test_1()
t2 = t1
t3 = t2
del t1
print("Not destroyed all objects")
time.sleep(5)
del t2
print("Not destroyed all objects")
time.sleep(5)
del t3
