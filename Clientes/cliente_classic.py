from cliente import Cliente


class Classic(Cliente):

    
                                     

    def puede_crear_chequera(self, cant_chequeras) -> bool:
        return False

    def puede_crear_tarjeta_de_credito(self, cant_tarjetas) -> bool:
        return False

    def puede_comprar_dolar(self) -> bool:
        return False

    def posee_cuenta_corriente(self) -> bool:
        return True
