def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# or if we want it to be dynamic assuming
# the arguments are organized from
# oldest to youngest

def my_sorted_function_1(*olderkids):
    print("Function - assuming the arguments are sorted oldest to youngest, the youngest is : " + olderkids[-1])


my_sorted_function_1("Abby", "Linda", "Anthony", "Suarez", "Chris")


# or if we want it to be dynamic assuming
# the arguments are organized from
# youngest to oldest

def my_sorted_function_2(*youngerkids):
    print("Function -  assuming the arguments are sorted youngest to oldest, the youngest is : " + youngerkids[0])


my_sorted_function_2("Chris", "Suarez", "Anthony", "Linda", "Abby")
