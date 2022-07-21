import json

with open("eventos_classic.json") as archivo:
    datos=json.load(archivo)

class Direccion:
    calle=datos["direccion"]["calle"]
    numero=datos["direccion"]["numero"]
    ciudad=datos["direccion"]["ciudad"]
    provincia=datos["direccion"]["provincia"]
    pais=datos["direccion"]["pais"]

class Cliente:
    nombre=datos["nombre"]
    apellido=datos["apellido"]
    numero=datos["numero"]
    dni=datos["dni"]
    direccion=Direccion
    tipo=datos["tipo"]

class ClienteClassic(Cliente):
    def __init__(self,data) -> None:
        super().__init__(data)

class ClienteGold(Cliente):
    def __init__(self,data) -> None:
        super().__init__(data)

class ClienteBlack(Cliente):
    def __init__(self,data) -> None:
        super().__init__(data)