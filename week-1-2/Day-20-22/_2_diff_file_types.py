"""
Handling different file types in Python involves understanding the structure and format of each file type and
then using appropriate libraries or modules to read, write, or manipulate data within those files.
Here's a brief overview of handling some common file types:
"""

## text files
with open("example.txt", "r") as f:
    for line in f:
        print(line)

## CSV Files
"""
CSV (Comma-Separated Values) files store tabular data with each line representing a row and fields separated by commas.
Python's csv module provides functionalities to read from and write to CSV files.
Example: Reading data from a CSV file:
"""
import csv

with open('data.csv', "w+", newline='') as csvfile:
    data = [
        ['Name', 'Age', 'City'],
        ['John', 30, 'New York'],
        ['Alice', 25, 'Los Angeles'],
        ['Bob', 35, 'Chicago']
    ]

    writer = csv.writer(csvfile)
    writer.writerows(data)
    csvfile.seek(0)
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))

## json files
"""
JSON (JavaScript Object Notation) files store data in a human-readable format as key-value pairs.
Python's json module provides functions to work with JSON data.
Example: Reading data from a JSON file:
"""
import json
with open("data.json","r") as f:
    data = json.load(f)
    print(data)

## Excel Files (.xlsx, .xls):
"""
Excel files are spreadsheet files commonly used for storing tabular data.
Libraries like openpyxl or pandas can be used to read from and write to Excel files.
Example (using openpyxl):
"""

## Binary Files:
"""Binary files contain data in a format that is not human-readable.
You can read from and write to binary files using Python's file handling functions with appropriate modes and methods.
Example: Reading binary data from a file:"""
