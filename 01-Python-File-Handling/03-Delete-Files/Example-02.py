import os

if os.path.exists("./myExample0-2"):
    print("The folder myExample0-2 in the current directory will now be removed.")
    # We will now delete the folder.
    os.rmdir("myExample0-2")
    if os.path.exists("./myExample0-2"):
        print("An exception occurred")
    else:
        print("myExample0-2 folder has been removed.")
else:
    os.mkdir("myExample0-2")
    # We will create the folder so that it can be deleted every other time the program is ran.
    print("If you check the current directory\na folder named myExample0-2 has been created.\n" +
          "Please rerun the program to see the folder being created.")
