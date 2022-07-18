import json

with open("ejemplos_json/eventos_classic.json") as file:
    data = json.load(file)
    transacciones = data["transacciones"]
    rechazadas=[]
    for i in range(len(transacciones)):
        x=transacciones[i]["estado"]
        print(x)
        if x=="RECHAZADA":
            rechazadas.append(transacciones[i]["numero"])
    print(rechazadas)    
class cliente:
    def __init__(self, datos, direccion) -> None:
        self.numero = datos["numero"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.dni = datos["dni"]
        self.direccion = direccion["direccion"]

    def puede_crear_chequera(self) -> bool:
        return False

    def puede_crear_tarjeta_de_credito(self) -> bool:
        return False

    def puede_comprar_dolar(self) -> bool:
        return False

    def posee_cuenta_corriente(self) -> bool:
        return False
