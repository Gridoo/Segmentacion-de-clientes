import json

with open("ejemplos_json/eventos_classic.json") as file:
    data = json.load(file)
    transacciones = data["transacciones"]
    rechazadas=[]
    aceptadas=[]
    for i in range(len(transacciones)):
        x=transacciones[i]["estado"]
     #   print(x)
        if x=="RECHAZADA":
            rechazadas.append(transacciones[i]["numero"])
        elif x=="ACEPTADA":
            aceptadas.append(transacciones[i]["numero"])
    print(rechazadas)
    print(aceptadas)

class Cliente:
    def Datos(self) -> None:
        self.numero = data["numero"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.dni = data["dni"]
        self.direccion = data["direccion"]

    def puede_crear_chequera(self) -> bool:
        return False

    def puede_crear_tarjeta_de_credito(self) -> bool:
        return False

    def puede_comprar_dolar(self) -> bool:
        return False

    def posee_cuenta_corriente(self) -> bool:
        return False

#mostrar la razón de porque estas transacciones fueron *rechazadas*
#Si son *aceptadas* agregar al reporte la transacción que se hizo sin detalle particular,


with open("ejemplos_json/eventos_classic.json") as file:
    data = json.load(file)
    transacciones = data["transacciones"]
    nombre=data["nombre"]

    print(nombre)
    rechazadas=[]
    aceptadas=[]
    datos=[]

    for i in range(len(transacciones)):
        x=transacciones[i]["estado"]
     #   print(x)
        if x=="RECHAZADA":
            rechazadas.append(transacciones[i]["numero"])
        elif x=="ACEPTADA":
            aceptadas.append(transacciones[i]["numero"])
    
    
    print(rechazadas)
    print(aceptadas)