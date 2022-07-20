import os
import sys
import json
from clientes import Cliente
from string import Template
print("Programa sprint 5")

file= open("plantilla.html")
src= Template(file.read())

nombre=Cliente()
resultado=src.substitute(nombre)

try:
    os.mkdir("index")
    file2=open('index.html','a')
    file2.writelines(resultado)
    print("La carpeta se creó")
except OSError:
    if os.path.exists("index"):
        file2=open('index.html','a')
        file2.writelines(resultado)
        print("guardado")