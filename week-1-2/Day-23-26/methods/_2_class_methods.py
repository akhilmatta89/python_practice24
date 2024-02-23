
"""
inside method implementation if we are using only class variables(static variables), the such type of methods we should
declare as class level methods

we can declare class method explicitly by using @classmethod decorator
"""
class Test:
    bank_name = "Kotak Mahindra"

    @classmethod
    def get_bank_name(cls):
        print("my bank name is ", cls.bank_name)
t = Test()
t.get_bank_name()

class Animal:
    legs = 4
    @classmethod
    def dog(cls):
        print("dog has {} legs".format(cls.legs))

a = Animal()
a.dog()