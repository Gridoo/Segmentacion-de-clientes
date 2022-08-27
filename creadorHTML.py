from clientes import *
from transacciones import *
import transacciones as tr
from motivos import *

def creacion_html():
    f = open('index.html', 'w') 
    html = f"""
          <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <link href="https://fonts.googleapis.com/css?family=Roboto:300,400&display=swap" rel="stylesheet">
      <link rel="stylesheet" href="fonts/icomoon/style.css">
      <link rel="stylesheet" href="css/owl.carousel.min.css">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css">
      <link rel="stylesheet" href="style.css">
      <title>Reporte ITBANK</title>
    </head>

    <body>
    <div class="content">
      <div class="container">
        <h1 class="mb-5" >Reporte Transacciones - ITBANK</h1> 
        <div class="container">
          <table class="table custom-table">
              <thead>
                <tr>
                  <th scope="col">Nombre</th>
                  <th scope="col">Apellido</th>
                  <th scope="col">Nro Cliente</th>
                  <th scope="col">DNI</th>
                  <th scope="col">Dirección</th>
                  <th scope="col">Tipo Cuenta</th>
                </tr>
              </thead>
              <tbody>
                  <tr scope="row">
                    <td>{data.nombre}</td>
                    <td>{data.apellido}</td>
                    <td>{data.numero}</td>
                    <td>{data.dni}</td>
                    <td>{direccion.calle} {direccion.numero}</td>
                    <td>{data.tipo}</td>
                  </tr>
              </table>
        </div>
      </div>
    </div>
      <div class="table-responsive custom-table-responsive">
        <table class="table custom-table">
          <br><br><br><br>
            <h2 class="mb-5" style="margin:20px">Historial de Transacciones</h2>
            <thead>
                <tr>  
                  <th scope="col"></th>
                  <th scope="col">Número</th>
                  <th scope="col">Fecha</th>
                  <th scope="col">Tipo</th>
                  <th scope="col">Estado</th>
                  <th scope="col">Monto</th>
                  <th scope="col">Razón Rechazo</th>
                </tr>
            </thead>
            
        """
    f.write(html)
    f.close()

def bloque_html(x):
  f = open('index.html', 'a') 
  html2=f"""
              <tbody>
                  <tr scope="row">
                    <td></td>
                    <td>{lista[x]["numero"]}</td>
                    <td>{lista[x]["fecha"]}</td>
                    <td>{lista[x]["tipo"]}</td>
                    <td>{lista[x]["estado"]}</td>
                    <td>${lista[x]["monto"]}</td>
                    <td>{id}</td>
                  </tr>
              </tbody>
            
"""
  f.write(html2)
  f.close()



creacion_html()
for x in range(0,len(lista),1):
  if(lista[x]["estado"]=="ACEPTADA"):
    print("aceptadas")
    id="-"
  elif(lista[x]["estado"]=="RECHAZADA"):
    print("rechazadas")
    if (lista[x]["tipo"]=="RETIRO_EFECTIVO_CAJERO_AUTOMATICO"):
      id=motivosEfectivo(x)
    elif(lista[x]["tipo"]=="ALTA_TARJETA_CREDITO"):
      id=motivosTarjeta()
  bloque_html(x)