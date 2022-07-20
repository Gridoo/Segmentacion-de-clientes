import json

with open("eventos_classic.json") as file:
    data = json.load(file)

print(data)