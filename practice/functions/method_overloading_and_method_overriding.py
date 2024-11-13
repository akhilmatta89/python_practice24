# Method Overloading
# Method overloading is not supported in python
class Student:
    # def m1(self,a,b):
    #     print("a",a)
    #     print("b", b)
    #     print("m1 1st method")

    def m1(self):
        print("m1 second method")

s = Student()
s.m1()

# Method Overrirding
class Manager:
    def goodWork(self):
        print("This manager has good amount of work")

class Manger_two(Manager):
    def goodWork(self):
        print("This manager doesnot has good amount of work")
    def work(self):
        print("Manger 2 works with python")

m = Manger_two()
m.goodWork()