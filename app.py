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

# Este metodo siempre espera recibir la url con el nombre para eso puedes colocar otro decorador
@app.route("/Saludo/<name>/<int:sueldo>/")
@app.route("/Saludo/<name>/")
@app.route("/Saludo/")
def greeting(name=None,sueldo=None):
  print(name)
  if name is not None:
    if sueldo is not None:
      return f'<h1 style="font-size:32px; color:green;">Hola {name}, Tu sueldo es: {sueldo*2} </h1>'
    return f'<h1 style="font-size:32px; color:green;">Hola {name} </h1>'
  else:
    return f'<h1 style="font-size:32px; color:green;">Hola Desconocido </h1>'
