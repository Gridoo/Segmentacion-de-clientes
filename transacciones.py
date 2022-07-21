import json

with open("eventos_classic.json") as archivo:
    datos=json.load(archivo)

class Transacciones:
    def __init__(self,datos):
        self.estado=datos["transacciones"][0]["estado"]
        self.tipo=datos["transacciones"][0]["tipo"]
        self.cuentaNumero=datos["transacciones"][0]["cuentaNumero"]
        self.cupoDiarioRestante=datos["transacciones"][0]["cupoDiarioRestante"]
        self.cantidadExtraccionesHechas=datos["transacciones"][0]["cantidadExtraccionesHechas"]
        self.monto=datos["transacciones"][0]["monto"]
        self.fecha=datos["transacciones"][0]["fecha"]
        self.numero=datos["transacciones"][0]["numero"]
        self.saldoEnCuenta=datos["transacciones"][0]["saldoEnCuenta"]
        self.TarjetasCredito=datos["transacciones"][0]["totalTarjetasDeCreditoActualmente"]
        self.Chequeras=datos["transacciones"][0]["totalChequerasActualmente"]
transacciones=Transacciones(datos)

"""transacciones": [{
			"estado": "ACEPTADA",
			"tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 9000,
			"cantidadExtraccionesHechas": 1,
			"monto": 1000,
			"fecha": "20/06/2022 16:00:55",
			"numero": 1,
			"saldoEnCuenta": 100000,
			"totalTarjetasDeCreditoActualmente" : 0,
			"totalChequerasActualmente" : 0
		},"""