import json
#cambiar eventos.json para ver Classic, Gold y BLack

with open("eventos_classic.json") as archivo:
    datos=json.load(archivo)

class Direccion:
    def __init__(self,datos):
        self.calle=datos["direccion"]["calle"]
        self.numero=datos["direccion"]["numero"]
        self.ciudad=datos["direccion"]["ciudad"]
        self.provincia=datos["direccion"]["provincia"]
        self.pais=datos["direccion"]["pais"]
direccion=Direccion(datos)
class Cliente:
    def __init__(self,datos):
        self.nombre=datos["nombre"]
        self.apellido=datos["apellido"]
        self.numero=datos["numero"]
        self.dni=datos["dni"]
        self.direccion=Direccion
        self.tipo=datos["tipo"]
data=Cliente(datos)
