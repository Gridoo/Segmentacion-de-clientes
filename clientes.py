from abc import ABC, abstractmethod
from cuenta import Cuenta9

class Cliente:
    def __init__(self,datos):
        self.nombre=datos["nombre"]
        self.apellido=datos["apellido"]
        self.numero=datos["numero"]
        self.dni=datos["dni"]
        self.direccion=Direccion
        self.tipo=datos["tipo"]
    def get_cuenta(self):
        return self.cuenta

    @abstractmethod
    def puede_crear_chequera(self, cant_chequeras) -> bool:
        pass

    @abstractmethod
    def puede_crear_tarjeta_de_credito(self, cant_tarjetas) -> bool:
        pass

    @abstractmethod
    def puede_comprar_dolar(self) -> bool:
        pass

    @abstractmethod
    def posee_cuenta_corriente(self) -> bool:
        pass

    def costo_transferencia(self, monto: int) -> int:
        pass
data=Cliente(datos)
