from flask import Flask

app = Flask(__name__)

@app.route("/EstadisticaDESI")
def EstadisticaDESI():
  return """
      <h1 style="font-size: 30px; color:blue;">Hola Estadisticos con H1 </h1>

        """

if __name__ == '__main__':
  app.run(debug=True)
  
# aveces hay errores en las importaciones de flask para soluciona vaya en: ver/paletade comandos ... escribir ipython:select interpreter 
#  y seleccionar el interprete de python correcto .
