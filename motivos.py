import transacciones as tr
from transacciones import Transacciones

def transacciones_aprobadas():
    for i in range(len(tr.estadoLISTA)):
        if tr.estadoLISTA[i] == "ACEPTADA":
            return i
   
i=transacciones_aprobadas()