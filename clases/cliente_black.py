import json
from clases.cliente import Cliente

class Black(Cliente):
    def __init__(self) -> None:
        with open("data/eventos_black.json") as jsonFile:
            archivo = json.load(jsonFile)
            jsonFile.close()
        super().__init__(archivo, {'limite_extraccion_diario': 100000, 'limite_transferencia_recibida': None,'costo_transferencia': None})

    def puede_crear_chequera(self, cant_chequeras):
        if cant_chequeras >= 2:
            return False
        else:
            return True

    def puede_crear_tarjeta_de_credito(self, cant_tarjetas):
        if cant_tarjetas >= 5:
            return False
        else:
            return True

    def puede_comprar_dolar(self):
        return True

    def posee_cuenta_corriente(self):
        return True