import datetime

x = datetime.datetime.now()

print(x)

""""
 The output will be year - month - day + 
 hour : minute : second . microsecond
"""

print(x.year)

# will print the current year

print(x.month)

# will print the current month

print(x.day)

# will print the current day

print(x.hour)

# will print the current hour

print(x.minute)

# will print the current minute

print(x.second)

# will print the current second

print(x.strftime("%A"))

# will print the current week day
