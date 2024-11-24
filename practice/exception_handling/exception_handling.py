# Exception Handling
# we use exception handling in python to make sure the errors are captured without any appplication or service interuptts

def divide_by_zero(val):
    try:
        return val/0
    except ZeroDivisionError as z:
        print("value cannot be divided with zero")


def take_input_and_sum_it():
    try:
        a = int(input("enter first value"))
        b = int(input("enter b value"))
        sumval = a+b
        return sumval
    except ValueError:
        print("enter correct datatype value")
    except Exception:
        print("Unknown error found")

# Finally block is used to execute some functionality as per the requirement even though if there is some error
def get_indexes(indexval):
    mylist = [10, 20,30]
    try:
        print(mylist[indexval])
    except IndexError:
        print("please give correct index")
    except Exception:
        print("some error occured")
    finally:
        print("Ill execute always")

# divide_by_zero(10)
# print(take_input_and_sum_it())
get_indexes(2)
get_indexes(10)
