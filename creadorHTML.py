from clientes import *
from transacciones import *
import transacciones as tr
import motivos as mot


i = mot.transacciones_aprobadas()


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
                <th scope="col">Número</th>
                <th scope="col">DNI</th>
                <th scope="col">Dirección</th> 
              </tr>
            </thead>
            <tbody>
                <tr scope="row">
                  <td>{i}</td>
                  <td>{data.nombre}</td>
                  <td>{data.numero}</td>
                  <td>{data.dni}</td>
                  <td>{direccion.calle} {direccion.numero}</td>
                </tr>
            </table>
      </div>
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
          <tbody>
            <tr scope="row">
              <th scope="row"></th>
              <td></td>
              <td></td>
              <td>{lista[0]["tipo"]}</td>
              <td></td>
              <td></td>
              <td>Excedió el cupo diario.</td>
            </tr>
            <tr class="spacer"><td colspan="100"></td></tr>
            <tr scope="row">
                <th scope="row"></th>
                <td>1</td>
                <td>16/07/2022 21:18:44</td>
                <td>{lista[1]["tipo"]}</td>
                <td>Rechazado</td>
                <td>$10000</td>
                <td>Excedió el cupo diario.</td>
              </tr>
              <tr class="spacer"><td colspan="100"></td></tr>
              <tr scope="row">
                <th scope="row">
                </th>
                <td>1</td>
                <td>16/07/2022 21:18:44</td>
                <td>Retiro_efectivo_cajero_automático</td>
                <td>Rechazado</td>
                <td>$10000</td>
                <td>Excedió el cupo diario.</td>
              </tr>
              <tr class="spacer"><td colspan="100"></td></tr>
              <tr scope="row">
                <th scope="row">
                </th>
                <td>1</td>
                <td>16/07/2022 21:18:44</td>
                <td>Retiro_efectivo_cajero_automático</td>
                <td>Rechazado</td>
                <td>$10000</td>
                <td>Excedió el cupo diario.</td>
              </tr>
              <tr class="spacer"><td colspan="100"></td></tr>
              <tr scope="row">
                <th scope="row">
                </th>
                <td>1</td>
                <td>16/07/2022 21:18:44</td>
                <td>Retiro_efectivo_cajero_automático</td>
                <td>Rechazado</td>
                <td>$10000</td>
                <td>Excedió el cupo diario.</td>
              </tr>
              <tr class="spacer"><td colspan="100"></td></tr>
              <tr scope="row">
                <th scope="row">
                </th>
                <td>1</td>
                <td>16/07/2022 21:18:44</td>
                <td>Retiro_efectivo_cajero_automático</td>
                <td>Rechazado</td>
                <td>$10000</td>
                <td>Excedió el cupo diario.</td>
              </tr>
              <tr class="spacer"><td colspan="100"></td></tr>
              <tr scope="row">
                <th scope="row">
                </th>
                <td>1</td>
                <td>16/07/2022 21:18:44</td>
                <td>Retiro_efectivo_cajero_automático</td>
                <td>Rechazado</td>
                <td>$10000</td>
                <td>Excedió el cupo diario.</td>
              </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  </body>
</html>
    """
    f.write(html)
    f.close()


creacion_html()
