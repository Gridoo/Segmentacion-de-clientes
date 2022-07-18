from turtle import title


def creacion_html():
    f = open('index.html', 'w')
    html = """
        <html>
        <title>Listado de transacciones</title>
        <body>
        <h1></h1>    
        </body>
        </html>
    """
    f.write(html)
    f.close()


creacion_html()
