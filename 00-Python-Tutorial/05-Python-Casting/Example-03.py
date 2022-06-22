# type casting is a way to specify a type on to a variable

x = "s1"
y = 2
z = 3.0

print(type(x))
print(type(y))
print(type(z))

x = str(x)
# x was originally a string, so it will remain a string

y = str(y)

# y was originally an integer but the str() constructor function will turn it into a string

z = str(z)
# z was originally a float number but the str() constructor function will turn it into a string

print(type(x))
print(type(y))
print(type(z))

