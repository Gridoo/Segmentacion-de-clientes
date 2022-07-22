import json

with open("eventos_classic.json") as archivo:
    datos = json.load(archivo)
estadoLISTA = []
tipoLISTA = []
cuentaNumeroLISTA = []
cupoDiarioRestanteLISTA = []
cantidadExtraccionesHechasLISTA = []
montoLISTA = []
fechaLISTA = []
numeroLISTA = []
saldoEnCuentaLISTA = []
TarjetasCreditoLISTA = []
ChequerasLISTA = []

for i in range(len(datos)):
    estadoLISTA.append(datos["transacciones"][i]["estado"])
    tipoLISTA.append(datos["transacciones"][i]["tipo"])
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
