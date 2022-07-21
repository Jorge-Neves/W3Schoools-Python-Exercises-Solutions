"""

convert and print the following JSON:

[{"name": "Paulo Santos", "city" : "Lisbon", "age" : "25"}]

"""

import json

x = '{"name": "Paulo Santos", "city" : "Lisbon", "age" : "25"}'

y = json.loads(x)

print('json converted into a python dictionary', y)
