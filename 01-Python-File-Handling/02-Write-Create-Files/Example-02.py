f = open("demofile.txt", "r")
print(f.read())
f.close()

print("-----")

f = open("demofile.txt", "w")
f.write("Woops! This Line has overwritten all content in the text file!")
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()

print("-----")

f = open("demofile.txt", "w")
L = ["Line 1.\n", "Line 2.\n", "Line 3.\n", "Line 4.\n", "Line 5.\n"]
f.writelines(L)
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()

# with this last step we return the text file to its initial content
