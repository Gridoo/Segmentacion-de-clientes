from .razon import Razon
from ..cliente import Cliente
from ..evento import Evento

class RazonALtaChequera(Razon):

    def resolver(self, cliente: Cliente, evento: Evento)  -> str:
        if not cliente.puede_crear_chequera():
            return "No se puede tener chequeras"

            if cliente.cuenta.total_chequeras < (evento.totalChequerasActualmente + 1):
                return "Ya se tiene el cupo de chequeras disponibles"