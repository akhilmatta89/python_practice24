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
print_sum_of_numbers_present_in_list([10,20])