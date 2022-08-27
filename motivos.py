from transacciones import lista
from clientes import data

def motivosEfectivo(i):
    for x in range(i,len(lista)):
        if(((lista[x]["monto"])<=(lista[x]["cupoDiarioRestante"])) and ((lista[x]["saldoEnCuenta"]) >= (lista[x]["monto"]))):
            #    print(lista[x]["monto"])
             #   print(lista[x]["cupoDiarioRestante"])
              #  print(lista[x]["saldoEnCuenta"])
               # print(lista[x]["monto"])
                return("Aprobado")
        else:
                return("Máximo 10k diarios o no tienes los fondos suficientes")

def motivosTarjeta():
    for x in range(0,len(lista)):
        if(data.tipo=="CLASSIC"):
                return("No puedes tener")



