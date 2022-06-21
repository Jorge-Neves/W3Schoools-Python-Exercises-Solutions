f = open("demofile.txt", "r")
print(f.read())
f.close()

print("-----")

f = open("demofile.txt", "a")
f.write("Now the file has more content")
f.close()

# "a" stands for append and will append to the end of the file

f = open("demofile.txt", "r")
print(f.read())

print("-----")

# now it prints line 1 -5 and finally "Now the fine has more content"

""""
 However, this behaviour described in the comments of this file
 will only be accurate for the first time this file is ran, because with each run the initial file is being altered
 Therefore we will add a bit of code at the end of this file to return the txt file to its original state
"""
f = open("demofile.txt", "r")
fs = f.read()
f.close()
m = fs.split("\n")
s = "\n".join(m[:-1])
f = open ("demofile.txt", "w+")
for x in range(len(s)):
    f.write(s[x])
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()

print("-----")

# This will remove the last line of the text file, and we will now append a line that matches the original
# "Line 5."

f = open("demofile.txt", "a")
f.write("\n")
f.write("Line 5.")
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()

print("-----")
