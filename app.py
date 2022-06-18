from flask import Flask

app=Flask(__name__)

# if __name__=='__main__':
  # ya no necesitamos esta condicion ya que ahora usamos a el propio flask para levantar nuestro servidor.
  
@app.route("/")
def index():
  return """
        <h1 style="font-size:32px; color:steelblue;">Inicio</h1>
        """
@app.route("/contacto")
def contact():
  return """
        <h1 style="font-size:32px; color:green;">Contact</h1>
        """
        
@app.route("/Nosotros")
def about():
  return """
          <h1 style="font-size:32px; color:green;">Nosotros</h1>
        """
