from clientes import cliente


class clientesblack(cliente):

    def puede_crear_chequera(self) -> bool:
        return True

    def puede_crear_tarjeta_de_credito(self) -> bool:
        return True

    def puede_comprar_dolar(self) -> bool:
        return True

    def posee_cuenta_corriente(self) -> bool:
        return True
