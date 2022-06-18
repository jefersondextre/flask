from flask import Flask,redirect,url_for

app=Flask(__name__)

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
        
@app.route("/nosotros/")
def about():
  return """
          <h1 style="font-size:32px; color:green;">Nosotros</h1>
        """
# URL_FOR 
@app.route("/ejemplo")
def example():
  # print(url_for("dashboard",name="John",age="27")) # A la url_for() le estamos pasando 
  # como parametro el nombre de una 
  # funcion que esta siendo administrada por 
  # una URL  
  return redirect(url_for("about"))


# Este metodo siempre espera recibir la url con el nombre para eso 
# puedes colocar otro decorador
@app.route("/login/<name>/")
@app.route("/login/")
def login(name=None):
  print(name)
  if name is not None:
    return redirect(f"/dashboard/{name}/")
  else:
    return f'<h1 style="font-size:32px; color:green;">Hola Desconocido </h1> <br> <p>Por favor igresa tu nombre en la URL</p>'


@app.route("/profile/<name>/")
@app.route("/profile/")
def dashboard(name=None):
  if name is not None:
    return f"<h1>Bienvenido {name} al dashboard</h1>"
  return redirect("/login/")
