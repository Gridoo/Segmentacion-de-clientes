import json

with open("eventos_classic.json") as archivo:
    datos=json.load(archivo)

class Direccion:
    def __init__(self) -> None:
        self.calle=datos["calle"]
        self.numero=datos["numero"]
        self.ciudad=datos["ciudad"]
        self.provincia=datos["provincia"]
        self.pais=datos["pais"]

class Cliente:
    def __init__(self) -> None:
        self.nombre=datos["nombre"]
        self.apellido=datos["apellido"]
        self.numero=datos["numero"]
        self.dni=datos["dni"]
        self.direccion=Direccion
        self.tipo=datos["tipo"]
        print(Cliente)
    def info(self):
        nombre="franco"
        print(nombre)
dato=Cliente()
dato.info()
class ClienteClassic(Cliente):
    def __init__(self,data) -> None:
        super().__init__(data)

class ClienteGold(Cliente):
    def __init__(self,data) -> None:
        super().__init__(data)

class ClienteBlack(Cliente):
    def __init__(self,data) -> None:
        super().__init__(data)