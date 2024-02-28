# Inheritance allows us to get all teh properties of the base class to the child class and make use of them

class Person: # base class
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print("fullname: ", self.fname +" " +self.lname)

p = Person("akhil", "reddy")
p.print_name()

class Student(Person):
    pass

s = Student("Jaya","Reddy")
s.print_name()

class Public(Person):
    def __init__(self, fname, lname, area):
        super().__init__(fname,lname)
        self.area = area

    def welcome(self):
        print("welcome {} {} from the area {}".format(self.fname, self.lname, self.area))

p = Public("sunitha","reddy","uppal")
p.print_name()
p.welcome()
