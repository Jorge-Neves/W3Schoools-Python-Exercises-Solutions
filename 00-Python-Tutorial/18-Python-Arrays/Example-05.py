cars = ["Ford", "Volvo", "BMW"]

for x in cars:
    print(x)

# will print each item in the cars array

print("-----")

count = 0


for y in cars:
    if count % 2 == 0:
        print(y)
    count += 1

count = 0

# will print all items at even indexes in the cars array

print("-----")

for z in cars:
    if count % 2 == 1:
        print(z)
    count += 1

# will print all items at odd indexes in the cars array
