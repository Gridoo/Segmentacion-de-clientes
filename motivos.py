import transacciones as tr


def transacciones_aprobadas():
    for i in tr.estado:
        print(i)
        # if tr.estado[i] == "ACEPTADA":
        # print("-")


transacciones_aprobadas()
