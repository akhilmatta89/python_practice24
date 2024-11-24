class Student:
    Company = "UST"

    def __init__(self):  # Constructor
        print("constructor intialized")
        self.name = "akhil"  # declaring and intializing the instance variable
        self.rollno = "161392"
        self.marks = 95

    def m1(self):  # Instance Method
        print(f"my name is {self.name}")
        print(f"my roll no is {self.rollno}")
        print(f"my marks are {self.marks}")

    @classmethod
    def m2(cls):  # class method
        print("This is class method")
        print("now ill try to use static variables")
        print(cls.Company)  # getting static variable with cls
        print(Student.Company)  # getting static variable with cls name

    @staticmethod
    def m3():  # static method
        x = 30
        print("iam a static method used as utility method")
        print("iam using local variable: ", x)

# s = Student()
# s.m1()
# s.m2()
# s.m3()

class Student1:
    a = 10
    def __init__(self):
        self.b = 100
        Student1.c = 120

    def m1(self):
        print(self.a) #if instance variable is not present and class variable is present
        #                 we can access that using self
        print(self.b)
        print(self.c)
        Student1.d = 140
        print(self.d)
# s = Student1()
# s.m1()

class Student2:
    a = 10

    def m1(self):
        self.a = 100

Student2().m1()
print(Student2.__dict__)