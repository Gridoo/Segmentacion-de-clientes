import transacciones as tr


def transacciones_aprobadas():
    for i in range(len(tr.estadoLISTA)):
        if tr.estadoLISTA[i] == "ACEPTADA":
            return i
