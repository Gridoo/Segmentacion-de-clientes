import json

with open("eventos_classic.json") as archivo:
    datos = json.load(archivo)
estadoLISTA = []
#tipoLISTA = []
#cuentaNumeroLISTA = []
#cupoDiarioRestanteLISTA = []
#cantidadExtraccionesHechasLISTA = []
#montoLISTA = []
#fechaLISTA = []
#numeroLISTA = []
#saldoEnCuentaLISTA = []
#TarjetasCreditoLISTA = []
#ChequerasLISTA = []
lista=datos["transacciones"]
class Transacciones:
    def __init__(self,datos):
        self.tipo=lista[0]["tipo"]
        self.cuentaNumero=datos["transacciones"][0]["cuentaNumero"] #se puede borrar todo, hay que usar {lista[posicion]["tipo"]}
        self.cupoDiarioRestante=datos["transacciones"][0]["cupoDiarioRestante"]
        self.cantidadExtraccionesHechas=datos["transacciones"][0]["cantidadExtraccionesHechas"]
        self.monto=datos["transacciones"][0]["monto"]
        self.fecha=datos["transacciones"][0]["fecha"]
        self.numero=datos["transacciones"][0]["numero"]
        self.saldoEnCuenta=datos["transacciones"][0]["saldoEnCuenta"]
        self.TarjetasCredito=datos["transacciones"][0]["totalTarjetasDeCreditoActualmente"]
        self.Chequeras=datos["transacciones"][0]["totalChequerasActualmente"]

transaccionesData=Transacciones(datos)
print(transaccionesData.tipo)


for i in range(len(datos)):
    estadoLISTA.append(datos["transacciones"][i]["estado"])



"""  tipoLISTA.append(datos["transacciones"][i]["tipo"])
    cuentaNumeroLISTA.append(datos["transacciones"][i]["cuentaNumero"])
    cupoDiarioRestanteLISTA.append(
        datos["transacciones"][i]["cupoDiarioRestante"])
    montoLISTA.append(datos["transacciones"][i]["monto"])
    fechaLISTA.append(datos["transacciones"][i]["fecha"])
    numeroLISTA.append(datos["transacciones"][i]["numero"])
    saldoEnCuentaLISTA.append(datos["transacciones"][i]["saldoEnCuenta"])
    TarjetasCreditoLISTA.append(
        datos["transacciones"][i]["totalTarjetasDeCreditoActualmente"])
    ChequerasLISTA.append(datos["transacciones"][i]
                          ["totalChequerasActualmente"])
    # cantidadExtraccionesHechasLISTA.append(datos["transacciones"][i]["cantidadExtraccionesHechas"])
# cantidadExtraccionesHechas rompe el bucle, lo comento por que no encuentro el motivo
"""