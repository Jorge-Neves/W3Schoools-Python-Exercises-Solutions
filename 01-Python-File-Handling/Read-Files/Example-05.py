f = open("demofile03.txt", "r")

print(f.readline())
print(f.readline())

# Will print the first two lines of the file


f.close()
f = open("demofile03.txt", "r")

print(f.readline())

# f.close() and reopening the file
# will make it so that print(f.readline()) returns to printing the first line of the text file

