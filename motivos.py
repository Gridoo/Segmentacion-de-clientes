from transacciones import lista
from clientes import data
#diferenciar entre classic, black y gold
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

def motivosTarjeta(i):
    for x in range(i,len(lista)):
        if(data.tipo=="CLASSIC"):
                return("No podes tener tarjeta")

def motivosChequera(i):
    for x in range(i,len(lista)):
        if(data.tipo=="CLASSIC"):
                return("No podes tener chequera")

def motivosDolar(i):
    for x in range(i,len(lista)):
        if(data.tipo=="CLASSIC"):
                return("No podes comprar dolares")

def motivosTransfe(i):
    for x in range(i,len(lista)):
        if(lista[x]["saldoEnCuenta"]>=(lista[x]["monto"]+ (lista[x]["monto"]-(lista[x]["monto"]*0.01)))):
                return("Aprobado")
        else:
            return("El saldo no cubre la comisión de 1%")

def motivosTransfeReci(i):
    for x in range(i,len(lista)):
        if(lista[x]["monto"]<=150000):
                return("Aprobado")
        else:
            return("No puede recibir transferencias mayores a $150.000 sin previo aviso")
