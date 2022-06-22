# type casting is a way to specify a type on to a variable

x = 1
y = 2.8
z = "3"
w = "4.2"

print(type(x))
print(type(y))
print(type(z))
print(type(w))

x = int(x)
# x was originally an integer so it will remain an integer

y = int(y)

# y was originally a float number but the int() constructor function will turn it into an integer

z = int(z)
# z was originally a string but the int() constructor function will turn it into an integer

print(type(x))
print(type(y))
print(type(z))

