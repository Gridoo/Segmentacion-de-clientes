import json

with open("ejemplos_json/eventos_black.json") as file:
    data = json.load(file)
    x = data["transacciones"][0]
    print(x)
