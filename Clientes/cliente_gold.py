from cliente import cliente


class clientesgold(cliente):

    def puede_crear_chequera(self, cant_chequeras) -> bool:
         if cant_chequeras >= 1:
            return False
         else:
            return True

    def puede_crear_tarjeta_de_credito(self, cant_tarjetas) -> bool:
        if cant_tarjetas >= 1:
            return False
        else:
            return True
            
    def puede_comprar_dolar(self) -> bool:
        return True

    def posee_cuenta_corriente(self) -> bool:
        return True
