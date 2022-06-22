# type casting is a way to specify a type on to a variable

x = 1
y = 2.8
z = "3"
w = "4.2"

print(type(x))
print(type(y))
print(type(z))
print(type(w))

x = float(x)
# x was originally an integer but with the float() constructor function will turn into a float number

y = float(y)

# y was originally a float number , so it will remain a float number

z = float(z)
# z was originally a string but with the float() constructor function will turn it into a float number

w = float(w)
# w was originally a string but with the float() constructor function will turn into a float number

print(type(x))
print(type(y))
print(type(z))
print(type(w))

print(x)
print(z)

# x and z will be 1.0 and 3.0 respectively instead of 1 and 3

