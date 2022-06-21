import os

try:
    f = open("myExample0-3.txt", "x")
    f.close()
    # "x" - will create a file, returns an error if the file exists.
except:
    print("file myExample0-3.txt already exists in the current directory.")
    # We will now delete the file so that it will create the file every other time the program is ran.
    if os.path.exists("myExample0-3.txt"):
        os.remove("myExample0-3.txt")
        print("myExample0-3.txt has been removed. Please rerun the program to see the file being created.")
    else:
        print("An exception occurred.")


if os.path.exists("myExample0-3.txt"):
    print("if you check the current directory \n a text file with name myExample0-3 has been created.")



