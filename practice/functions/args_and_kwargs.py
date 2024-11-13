def normal_arguments(a, b, c, d):
    print(a, b, c, d)

def starargumnets(*args):
    for each in args:
        print(each)

def starkwargs(**kwargs):
    for k,v in kwargs.items():
        print(f"key is {k},value is {v}")

# normal_arguments("akhil","mahesh", "sumanth", "jeevan")
# starargumnets(*["akhil","reddy", "matta"])
starkwargs(**{"name":"akhil","rollno":"161392","marks":"95"})