# write a programs to find the largest of 2 numbers from the input of cmd
def find_largest_of_two_numbers():
    firstnum = int(input("enter the first number"))
    secnum = int(input("enter the second number"))
    if firstnum > secnum:
        print(firstnum, "is the largest number amongst")
    else:
        print(secnum, "is the largest number amongst")

# write a programs to find the largest of 3 numbers from the input of cmd
def find_largest_of_three_numbers():
    firstnum = int(input("enter the first number"))
    secnum = int(input("enter the second number"))
    thirdnum = int(input("enter the third number"))
    if (firstnum > secnum) and (firstnum>thirdnum):
        print(firstnum, "is the largest number amongst")
    elif (secnum > thirdnum):
        print(secnum, "is the largest number amongst")
    else:
        print(thirdnum, "is the largest number amongst")

def find_smallest_of_two_numbers(firstnum, secnum):
    if firstnum < secnum:
        print(firstnum, "is the smallest amongst")
    else:
        print(secnum, "is the smallest amongst")

def find_smallest_of_three_numbers(firstnum, secnum, thirdnum):
    if firstnum < secnum and firstnum < thirdnum:
        print(firstnum, "is the smallest amongst")
    elif secnum < thirdnum:
        print(secnum, "is the smallest amongst")
    else:
        print(thirdnum, "is the smallest amongst")

def check_given_number_btw_1_and_100(num: int):
    if num in range(1, 101):
        print("yes {} is in range of 1 and 100".format(num))
    else:
        print("{} is not in range of 1 and 100".format(num))


find_largest_of_two_numbers()
find_largest_of_three_numbers()
find_smallest_of_two_numbers(10, 30)
find_smallest_of_three_numbers(32, 65, 10)
check_given_number_btw_1_and_100(0)

