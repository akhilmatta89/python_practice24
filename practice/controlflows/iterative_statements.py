"""
for loop
while loop
"""

# -------------------- For Loop -----------------------------
def iterate_string(name:str):
    for each in name:
        print(each)

def iterate_str_wth_indx(name):
    i = 0
    for each in name:
        print("This letter: {}, has index {}".format(each, i))
        i+=1

def print_hello_10_times():
    for i in range(10):
        print("Hello: ", i)

def display_num_from_0_to_10():
    for i in range(0,11):
        print(i)

def display_odd_numbers_from_0_to_20():
    for i in range(21):
        if (i%2 !=0):
            print(i)

def print_10_to_1_in_descending_order():
    for i in range(10,0,-1):
        print(i)

def print_10_to_1_in_descending_order_using_list():
    mylist = []
    for i in range(11):
        mylist.append(i)
    mylist.sort(reverse=True)
    print(mylist)

def print_sum_of_numbers_present_in_list(mylist):
    total_count = 0
    indexcount = 0
    for i in mylist:
        total_count+=(mylist[indexcount])
        indexcount+=1
    print(total_count)


#iterate_string("akhil")
#iterate_str_wth_indx("akhil")
#print_hello_10_times()
#display_num_from_0_to_10()
#display_odd_numbers_from_0_to_20()
#print_10_to_1_in_descending_order()
#print_10_to_1_in_descending_order_using_list()
#print_sum_of_numbers_present_in_list([10,20])

# -------------------- While Loop -----------------------------

def print_number_from_1_to_10_using_while():
    x = 1
    while x <= 10:
        print(x)
        x+=1

def display_sum_of_first_n_number(number):
    sumcount = 0
    indx = 1
    while indx<= number:
        sumcount = sumcount + indx
        indx = indx+1
    print(sumcount)

def function_to_display_akhil():
    ip = ""
    while ip != "Akhil":
        ip = str(input("enter name"))
    print("Thanks for entering name as akhil")

def function_to_print_right_angled_triangle():
    lines = int(input("enter number of rows"))
    line = 1
    for i in range(lines):
        if line <= lines:
            print('* ' * line)
            line+=1

def function_to_print_equaliant_triangle():
    n = int(input("enter number of rows:"))
    for i in range(1, n+1):
        print(" "*(n-i),end="")
        print("* "*i)


# print_number_from_1_to_10_using_while()
# display_sum_of_first_n_number(2)
# function_to_display_akhil()
#function_to_print_right_angled_triangle()
#function_to_print_equaliant_triangle()