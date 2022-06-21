import os

if os.path.exists("myExample0-1.txt"):
    print("The file myExample0-1.txt in the current directory will now be removed.")
    # We will now delete the file so that it will create the file every other time the program is ran.
    os.remove("myExample0-1.txt")
    if os.path.exists("myExample0-4.txt"):
        print("An exception occurred")
    else:
        print("myExample0-1.txt has been removed.")
else:
    f = open("myExample0-1.txt", "w")
    f.close()
    # "x" - will create a file if the specified file does not exist.
    print("if you check the current directory \n" + "a text file with name myExample0-1 has been created.\n" +
          "Please rerun the program to see the file being created.")
