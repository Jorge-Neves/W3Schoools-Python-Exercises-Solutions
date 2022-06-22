f = open("demofile03.txt", "r")
print(f.read(3))

# print(f.read(3)) will return the first 3 characters of the file

print(f.read(3))
print(f.read(3))

# the subsequent print(f.read(3)) will continue reading the next 3 characters of the file

f.close()
f = open("demofile03.txt", "r")

print(f.read(3))

# f.close() and reopening the file
# will make it so that print(f.read(3)) returns to printing the first 3 characters of the text file
