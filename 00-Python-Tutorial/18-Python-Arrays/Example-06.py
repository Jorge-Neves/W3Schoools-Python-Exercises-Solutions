cars = ["Ford", "Volvo", "BMW"]

print(cars)

cars.append("Honda")

print(cars)
# The append method append() adds an element at the end of a list

cars.pop()

List = ["Toyota", "Suzuki", "Fiat"]

cars.append(List)

print(cars)

# Passing a list to the append() method will add the entire array as the last element
# It is possible to add all elements of List to the cars array as separate elements with a loop

cars.pop()

print(cars)
y = len(List)
count = 0

while count < y:
    cars.append(List[count])
    count += 1

print(cars)

# This while loop adds all elements from List individually to the end of the cars array

for x in range(3):
    cars.pop()

print(cars)

# This for loop returns the 3 items that the previous while loop appended

for x in List:
    cars.append(x)

print(cars)

# This for loop adds all elements from List individually to the end of the cars array
