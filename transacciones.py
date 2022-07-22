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
    estado = datos["transacciones"][i]["estado"]
    estadoLISTA.append(datos["transacciones"][i]["estado"])
    tipo = datos["transacciones"][i]["tipo"]
    tipoLISTA.append(datos["transacciones"][i]["tipo"])
    cuentaNumero = datos["transacciones"][i]["cuentaNumero"]
    cuentaNumeroLISTA.append(datos["transacciones"][i]["cuentaNumero"])
    cupoDiarioRestante = datos["transacciones"][i]["cupoDiarioRestante"]
    cupoDiarioRestanteLISTA.append(
        datos["transacciones"][i]["cupoDiarioRestante"])
    monto = datos["transacciones"][i]["monto"]
    montoLISTA.append(datos["transacciones"][i]["monto"])
    fecha = datos["transacciones"][i]["fecha"]
    fechaLISTA.append(datos["transacciones"][i]["fecha"])
    numero = datos["transacciones"][i]["numero"]
    numeroLISTA.append(datos["transacciones"][i]["numero"])
    saldoEnCuenta = datos["transacciones"][i]["saldoEnCuenta"]
    saldoEnCuentaLISTA.append(datos["transacciones"][i]["saldoEnCuenta"])
    TarjetasCredito = datos["transacciones"][i]["totalTarjetasDeCreditoActualmente"]
    TarjetasCreditoLISTA.append(
        datos["transacciones"][i]["totalTarjetasDeCreditoActualmente"])
    Chequeras = datos["transacciones"][i]["totalChequerasActualmente"]
    ChequerasLISTA.append(datos["transacciones"][i]
                          ["totalChequerasActualmente"])
    #cantidadExtraccionesHechas = datos["transacciones"][i]["cantidadExtraccionesHechas"]
    # cantidadExtraccionesHechasLISTA.append(
    #   datos["transacciones"][i]["cantidadExtraccionesHechas"])


# cantidadExtraccionesHechas rompe el bucle, lo comento por que no encuentro el motivo
