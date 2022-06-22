import os

os.system("notepad.exe example-01.txt")

# os.system opens a new window

f = open("example-01.txt")

print(f.read())


# .read() prints the content of the txt. file
