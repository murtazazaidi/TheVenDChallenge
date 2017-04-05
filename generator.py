import random
import json

data = []
for i in range(1000000):
    person = []
    for j in range(24):
        person.append('Yes' if bool(random.getrandbits(1)) else 'No')
    data.append(person)

with open('quetta.json', 'w') as outfile:
    json.dump(data, outfile)
