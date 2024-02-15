print("-------------------------------Basics of File Handling:----------------------------------------------")
# Opening and Closing Files:
# Use the open() function to open a file.
file = open("example.txt", "r")
print(file)

# Reading from Files:
# Use the read() method to read the entire content of a file.
content = file.read()
print(content)

# Closing Files:
#Always close files after you're done using them to free up system resources.
file.close()
print("file closed successfully")


# Reading the file
file = open("example.txt", "r")
for line in file:
    print(line)
file.close()
print("file closed successfully")

# using with statement
print("-------------Using with----------")
with open("example.txt", "r") as file:
    print("File opened and started reading content")
    for line in file:
        print(line)
    file.close()
    print("file closed successfully")


####### writing into files

# Use mode "w" to open a file for writing. This will overwrite the existing content.
with open("example_1.txt", "w") as file:
    file.write("iam akhil")
    file.close()

# Appending to Files:
# Use mode "a" to append to a file without overwriting existing content.
with open("example_1.txt", "a") as file:
    file.write("\niam from hyd")
    file.close()

##### In Python, there are six methods or access modes, which are:
"""
Read Only ('r’)
    This mode opens the text files for reading only. The start of the file is where the handle is located. 
    It raises the I/O error if the file does not exist. This is the default mode for opening files as well.
Read and Write ('r+’)
    This method opens the file for both reading and writing. 
    The start of the file is where the handle is located. 
    If the file does not exist, an I/O error gets raised.
Write Only ('w’)
    This mode opens the file for writing only. 
    The data in existing files are modified and overwritten. 
    The start of the file is where the handle is located. 
    If the file does not already exist in the folder, a new one gets created.
Write and Read ('w+’)
    This mode opens the file for both reading and writing. 
    The text is overwritten and deleted from an existing file. 
    The start of the file is where the handle is located.
Append Only ('a’)
    This mode allows the file to be opened for writing. 
    If the file doesn't yet exist, a new one gets created. 
    The handle is set at the end of the file. 
    The newly written data will be added at the end, following the previously written data.
Append and Read (‘a+’)
    Using this method, you can read and write in the file. 
    If the file doesn't already exist, one gets created. 
    The handle is set at the end of the file. 
    The newly written text will be added at the end, following the previously written data.
"""

# "x" is used to create a new file if and if there is no file already present, if present it throws error
# with open ("myfile_with_x", "x") as file:
#     file.write("created this file using x")

"""
"w" – Write: this command will create a new text file whether or not there is a file in the memory with the new 
    specified name. 
It does not return an error if it finds an existing file with the same name – instead it will overwrite the existing file.
"""
"""
write() method
    This function inserts the string into the text file on a single line.

writelines() method:
    This function inserts multiple strings at the same time. 
    A list of string elements is created, and each string is then added to the text file.
"""
with open("example_1.txt", "a") as file:
    file.writelines(["\nHello World ", "\nYou are welcome to Fcc\n"])
    file.close()

"""
read() method:
    This function returns the bytes read as a string. If no n is specified, it then reads the entire file
readline() method:
    This function reads a line from a file and returns it as a string. It reads at most n bytes for the specified n. 
    But even if n is greater than the length of the line, it does not read more than one line.
"""
print("------------------readlines method")
f = open("example_1.txt", "r")
print(f.readline())
f.close()