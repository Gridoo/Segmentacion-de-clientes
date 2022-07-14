class cliente:
    def __init__(self) -> None:
        self.numero = datos["numero"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.dni = datos["dni"]
        self.direccion = direccion["direccion"]

    def puede_crear_chequera(self) -> bool:
        return False

    def puede_crear_tarjeta_de_credito(self) -> bool:
        return False

    def puede_comprar_dolar(self) -> bool:
        return False
