import json

with open("eventos_classic.json") as archivo:
    datos = json.load(archivo)
estadoLISTA = []
lista=datos["transacciones"]

for i in range(len(datos)):
    estadoLISTA.append(datos["transacciones"][i]["estado"])

