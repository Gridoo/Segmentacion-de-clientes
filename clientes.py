
import json
from direccion import Direccion

with open("eventos_classic.json") as archivo:
    datos=json.load(archivo)


class Cliente:
    def __init__(self) -> None:
        self.nombre=datos["nombre"]
        self.apellido=datos["apellido"]
        self.numero=datos["numero"]
        self.dni=datos["dni"]
        self.direccion=Direccion(datos["direccion"])
        self.tipo=datos["tipo"]

class ClienteClassic(Cliente):
    def __init__(self,data) -> None:
        super().__init__(data)

class ClienteGold(Cliente):
    def __init__(self,data) -> None:
        super().__init__(data)

class ClienteBlack(Cliente):
    def __init__(self,data) -> None:
        super().__init__(data)