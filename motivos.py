from transacciones import lista
from clientes import data


def motivosEfectivo(i):
    for x in range(i,len(lista)):
        if(data.tipo=="CLASSIC"):
            if(((lista[x]["monto"])<=(lista[x]["cupoDiarioRestante"])) and ((lista[x]["saldoEnCuenta"]) >= (lista[x]["monto"]))):
                    return("Aprobado")
            else:
                    return("Máximo 10k diarios o no tenes los fondos suficientes")
        elif(data.tipo=="GOLD"):
            if((lista[x]["monto"])<=(lista[x]["cupoDiarioRestante"])) and ((lista[x]["saldoEnCuenta"]) >= (lista[x]["monto"])):
                     return("Aprobado")
            else:
                return("Máximo 20k diarios o no tenes fondos suficientes")
        elif(data.tipo=="BLACK"):
            if(((lista[x]["monto"])<=(lista[x]["cupoDiarioRestante"])) and ((lista[x]["saldoEnCuenta"]) >= (lista[x]["monto"]))):
                    return("Aprobado")
            else:
                    return("Máximo 100k diarios o no tenes los fondos suficientes")
        


def motivosTarjeta(i):
    for x in range(i,len(lista)):
        if(data.tipo=="CLASSIC"):
                return("No podes tener tarjeta")
        elif(data.tipo=="GOLD"):
            if(lista[x]["totalTarjetasDeCreditoActualmente"]<1):
                return("Aprobado")
            else:
                return("Solo podes tener una tarjeta")
        elif(data.tipo=="BLACK"):
            if(lista[x]["totalTarjetasDeCreditoActualmente"]<5):
                return("Aprobado")
            else:
                return("Solo podes tener 5 tarjetas")

def motivosChequera(i):
    for x in range(i,len(lista)):
        if(data.tipo=="CLASSIC"):
                return("No podes tener chequera")
        elif(data.tipo=="GOLD"):
            if(lista[x]["totalChequerasActualmente"]<1):
                return("Aprobado")
            else:
                return("No podes tener más de 1 chequera")
        elif(data.tipo=="BLACK"):
            if(lista[x]["totalChequerasActualmente"]<2):
                return("Aprobado")
            else:
                return("No podes tener más de 2 chequeras")

def motivosDolar(i):
    for x in range(i,len(lista)):
        if(data.tipo=="CLASSIC"):
                return("No podes comprar dolares")
        elif(data.tipo=="GOLD" or data.tipo=="BLACK"):
            if(lista[x]["saldoEnCuenta"]>lista[x]["monto"]):
                return("Podes comprar dolares")
            else:
                return("Saldo insuficiente")

def motivosTransfe(i):
    for x in range(i,len(lista)):
        if(data.tipo=="CLASSIC"):
            if(lista[x]["saldoEnCuenta"]>=(lista[x]["monto"]+ (lista[x]["monto"]-(lista[x]["monto"]*0.01)))):
                    return("Aprobado")
            else:
                return("El saldo no cubre la comisión de 1%")
        elif(data.tipo=="GOLD"):
            if(lista[x]["saldoEnCuenta"]>=(lista[x]["monto"]+ (lista[x]["monto"]-(lista[x]["monto"]*0.005)))):
                    return("Aprobado")
            else:
                return("El saldo no cubre la comisión de 0.5%")
        elif(data.tipo=="BLACK"):
            if(lista[x]["saldoEnCuenta"]>=lista[x]["monto"]):
                return("Aprobado")
            else:
                return("Saldo insuficiente")

def motivosTransfeReci(i):
    for x in range(i,len(lista)):
        if(data.tipo=="CLASSIC"):
            if(lista[x]["monto"]<=150000):
                    return("Aprobado")
            else:
                return("No puede recibir transferencias mayores a $150.000 sin previo aviso")
        elif(data.tipo=="GOLD"):
            if(lista[x]["monto"]<=500000):
                    return("Aprobado")
            else:
                return("No puede recibir transferencias mayores a $500.000 sin previo aviso")
        elif(data.tipo=="BLACK"):
                    return("Aprobado")   