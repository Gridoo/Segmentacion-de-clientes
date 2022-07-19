import json
from sqlite3 import DateFromTicks

#cambiar archivo 
with open("ejemplos_json/eventos_classic.json") as file:
    data = json.load(file)
    transacciones = data["transacciones"]
    nombre=data["nombre"]
    numero=data["numero"]
    apellido=data["apellido"]
    dni=data["dni"]
    tipo=data["tipo"]
    rechazadas=[]
    aceptadas=[]
    datos=[]
    datos.append(nombre)
    datos.append(numero)
    datos.append(apellido)
    datos.append(dni)
    datos.append(tipo)
    print(datos)

    for i in range(len(transacciones)):
        x=transacciones[i]["estado"]
     #   print(x)
        if x=="RECHAZADA":
            rechazadas.append(transacciones[i]["numero"])
        elif x=="ACEPTADA":
            aceptadas.append(transacciones[i]["numero"])
    
    print(rechazadas)
    print(aceptadas)


#En el reporte se debe incluir el nombre de cliente, número, DNI, dirección y para
#cada transacción la fecha , el tipo de operación, el estado, el monto y razón por la
#cual se rechazó (vacío en caso de ser aceptada).

#rechzada -- razon