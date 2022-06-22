def my_function(**kid):
    print("His last name is + " + kid["lname"])


# Examples

def my_last_name_function(**kid):
    print("His last name is " + kid["lname"])


my_last_name_function(fname="Tobias", lname="Refsnes")
my_last_name_function(fnmae="Paulo", lname="Santos")


def my_first_name_function(**kid):
    print("His last name is " + kid["fname"])


my_first_name_function(fname="Tobias", lname="Refnes")
my_first_name_function(fname="Paulo", lname="Santos")
