cars = ["Ford", "Volvo", "BMW"]

j = cars[-1]
print(cars)

cars.pop()
print(cars)

# The pop() method removes an element at the end of a list because the default value is -1
# However, an exact index can be specified

cars.append(j)
print(cars)

k = cars[1]

cars.pop(1)
print(cars)

# This removes the second array item "Volvo"

cars.append(k)
print(cars)

p = cars[0]

cars.pop(0)
print(cars)

# This removes the first array item "Ford"

cars.append(p)
print(cars)

