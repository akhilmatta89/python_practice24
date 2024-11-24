class FileOps:
    def open_file_and_read_content(self):
        try:
            raise CustomFileOpenError("some error occured", 400)
        except CustomFileOpenError as c:
            print(c)

class CheckAge:
    def checkAdultOrMinor(self):
        try:
            age = int(input("enter teh age"))
            if age < 18:
                raise MinorAgeException("the age of the customer is less than 18")
        except MinorAgeException as e:
            print(e)

class OpenFile:

    def open_the_file(self):
        filename = ""
        try:
            filename = "example.txt"
            with open(filename, "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            raise CustomFileNotFoundError("file not found", filename, 400)

def trigger_open_file():
    try:
        OpenFile().open_the_file()
    except CustomFileNotFoundError as c:
        print(c)
    finally:
        print("iam always there")

def check_salary_in_range():
    salary = int(input("enter salary"))
    if not 5000 < salary < 15000:
        raise SalaryNotInRangeError(salary)


"""--------------------------------------- CustomErrors----------------------------"""
class MinorAgeException(Exception):
    pass


class CustomFileOpenError(Exception):

    def __init__(self, value, errCode):
        self.value = value
        self.errcode = errCode

    def __str__(self):
        return (f"{self.value} with errocode as {self.errcode}")

class CustomFileNotFoundError(Exception):
    def __init__(self, message, filename, errorcode):
        self.message = message
        self.filename = filename
        self.errorcode = errorcode

    def __str__(self):
        return (f"{self.message}, while opening file: {self.filename}, resulting error code{self.errorcode}")

class SalaryNotInRangeError(Exception):

    def __init__(self,salary, message="salary is not in 5000 to 15000 range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

# f = FileOps()
# f.open_file_and_read_content()

# c = CheckAge().checkAdultOrMinor()
#trigger_open_file()
check_salary_in_range()

