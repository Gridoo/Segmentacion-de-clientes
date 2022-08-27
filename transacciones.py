import json
from clientes import datos

estadoLISTA = []
lista=datos["transacciones"]


for i in range(len(datos)):
    estadoLISTA.append(datos["transacciones"][i]["estado"])
