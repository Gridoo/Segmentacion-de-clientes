import json
from clientes import datos
class Direccion:
    def __init__(self) -> None:
        self.calle=datos["calle"]
        self.numero=datos["numero"]
        self.ciudad=datos["ciudad"]
        self.provincia=datos["provincia"]
        self.pais=datos["pais"]