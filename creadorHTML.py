from re import I
from clientes import *
from transacciones import *
import transacciones as tr
import motivos as mot


id = mot.transacciones_aprobadas()


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
                  <th scope="col">Nro Cliente</th>
                  <th scope="col">Nombre</th>
                  <th scope="col">Número</th>
                  <th scope="col">DNI</th>
                  <th scope="col">Dirección</th> 
                </tr>
              </thead>
              <tbody>
                  <tr scope="row">
                    <td>{id}</td>
                    <td>{data.nombre}</td>
                    <td>{data.numero}</td>
                    <td>{data.dni}</td>
                    <td>{direccion.calle} {direccion.numero}</td>
                  </tr>
              </table>
        </div>
      </div>
    </div>
    <body>
      <div class="table-responsive custom-table-responsive">
        <table class="table custom-table">
          <br><br><br><br>
            <h2 class="mb-5">Historial de Transacciones</h2>
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
        </table>
      </div>
    </body>"""
    f.write(html)
    f.close()

def bloque_html(x):
  f = open('index.html', 'a') 
  html2=f"""
  <body>
      <div class="table-responsive custom-table-responsive">
        <table class="table custom-table">
          <br>
            <tbody>
              <tr scope="row">
                <th scope="row"></th>
                  <td>{lista[x]["numero"]}</td>
                  <td>{lista[x]["fecha"]}</td>
                  <td>{lista[x]["tipo"]}</td>
                  <td>{lista[x]["estado"]}</td>
                  <td>${lista[x]["monto"]}</td>
                  <td>{lista[x]["monto"]}</td>
              </tr>
          </tbody>
        </table>"""
  f.write(html2)
  f.close()


creacion_html()
for x in range(0,len(lista)):
  bloque_html(x)