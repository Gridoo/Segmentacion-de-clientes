class Direccion:
    def __init__(self,datos):
        self.calle=datos["direccion"]["calle"]
        self.numero=datos["direccion"]["numero"]
        self.ciudad=datos["direccion"]["ciudad"]
        self.provincia=datos["direccion"]["provincia"]
        self.pais=datos["direccion"]["pais"]
    def output_as_label(self):
        return f"{self.calle} N° {self.numero}, {self.ciudad}, {self.provincia}, {self.pais}"
