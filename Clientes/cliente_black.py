from cliente import cliente


class clientesblack(cliente):

    def puede_crear_chequera(self,cant_chequeras) -> bool:
      if cant_chequeras >= 2:
            return False
      else:
            return True

    def puede_crear_tarjeta_de_credito(self,cant_tarjetas) -> bool:
       if cant_tarjetas >= 5:
            return False
       else:
            return True
            
    def puede_comprar_dolar(self) -> bool:
        return True

    def posee_cuenta_corriente(self) -> bool:
        return True
