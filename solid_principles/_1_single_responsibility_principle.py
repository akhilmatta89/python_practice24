# This is the first principle among  the solid principles stating the first letter in SOLID word.
# This principle states one class should perform only one reason to change(one class one task).
# This means single class can take single responsibility, if a class takes care of multiple tasks then its should be
# sepearted into seperate tasks.
import csv
import statistics
from pathlib import Path
from zipfile import ZipFile

class WrongWayFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

# Correct Way to implement single responsibility principle
class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

print("------------------------Task-1-----------------------------------")
"""
Create a program that reads data from a CSV file containing information about employees 
(such as name, age, department, and salary), performs some operations on this data 
(e.g., calculating average salary by department), and then outputs the results to the console and/or another file.
"""

class DataLoad:
    def __init__(self, path):
        self.path = path
        self.data = []

    def load_data_from_csv(self):
        # loading the data from CSV
        with open(self.path, 'r') as content:
            reader = csv.DictReader(content)
            for rows in reader:
                self.data.append(rows)
        return self.data

class DataOperations:
    def __init__(self, data):
        self.data = data

    def calculate_average_salary_based_on_department(self):
        departement_salaraies = {}
        for each_row in self.data:
            department = each_row["Department"]
            if not departement_salaraies.get(department):
                departement_salaraies[department] = [int(each_row["Salary"])]
            else:
                departement_salaraies[department].append(int(each_row["Salary"]))
        average_salaries = {}
        for department, salaries in departement_salaraies.items():
            average_salaries[department] = statistics.mean(salaries)
        return average_salaries

class PrintOutPut:
    def __init__(self, data):
        self.data = data
    def print_data_in_console(self):
        for department, average_salary in self.data.items():
            print("The avarage salary for department {} is {} rupees".format(department,average_salary))

d = DataLoad("/Users/akhilmatta/PycharmProjects/python_practice24/solid_principles/employee_info.csv")
data = d.load_data_from_csv()
dop = DataOperations(data)
avg_sal = dop.calculate_average_salary_based_on_department()
prntoutpt = PrintOutPut(avg_sal)
prntoutpt.print_data_in_console()


"""
Task: Create a program that reads text from a file, counts the occurrences of each word, and then generates a report 
displaying the top N most frequent words.
"""

class ReadDataFromFile:

    def read(self):
        with open("test.txt", "r") as file:
            text = file.read()
        return text

class CountOccurencesOfWord:

    def count_occurences(self, data):
        occ_dict = {}
        text_list = data.split()
        for word in text_list:
            word = word.lower()
            occ_dict[word] = occ_dict.get(word,0) + 1
        return occ_dict

class TopNFrequentWords:

    def get_top_n_frequent_words(self, top_n, data):
        sorted_dict_asc = sorted(data.items(), key=lambda x: x[1], reverse=True)
        top_words = sorted_dict_asc[:top_n]
        print(f"Top {top_n} most frequent words:")
        for word, count in top_words:
            print(f"{word}: {count}")

r = ReadDataFromFile()
txt = r.read()
c = CountOccurencesOfWord()
data = c.count_occurences(txt)
t = TopNFrequentWords()
t.get_top_n_frequent_words(5, data)