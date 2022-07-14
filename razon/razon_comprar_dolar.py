from .razon import Razon
from ..cliente import Cliente
from ..evento import Evento

class RazonComprarDolar(razon):


    def resolver(self, cliente: Cliente, evento: Evento) -> str:
        if not cliente.puede_comprar_dolar():
            return "Esta cuenta no puede adquirir dolares"


            if evento.monto > evento.saldoEnCuenta:
                return "Saldo insuficiente para adquirir dolares"