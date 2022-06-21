import os

if os.path.exists("myExample0-4.txt"):
    print("file myExample0-3.txt already exists in the current directory.")
    # We will now delete the file so that it will create the file every other time the program is ran.
    os.remove("myExample0-4.txt")
    if os.path.exists("myExample0-4.txt"):
        print("An exception occurred")
    else:
        print("myExample0-4.txt has been removed. Please rerun the program to see the file being created.")
else:
    f = open("myExample0-4.txt", "w")
    f.close()
    # "x" - will create a file if the specified file does not exist.
    print("if you check the current directory \n a text file with name myExample0-4 has been created.")
