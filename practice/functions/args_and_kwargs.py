def normal_arguments(a, b, c, d):
    print(a, b, c, d)

def starargumnets(*args): # whatever input you give it takes as a tuple
    for each in args:
        print(each)

def starkwargs(**kwargs): # this one will be of type dict
    for k,v in kwargs.items():
        print(f"key is {k},value is {v}")

# normal_arguments("akhil","mahesh", "sumanth", "jeevan")
# starargumnets(*["akhil","reddy", "matta"])
#starargumnets("akhil", "reddy", "matta")
# starkwargs(**{"name":"akhil","rollno":"161392","marks":"95"})
