from flask import Flask,redirect

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
        
@app.route("/Nosotros")
def about():
  return """
          <h1 style="font-size:32px; color:green;">Nosotros</h1>
        """

# Este metodo siempre espera recibir la url con el nombre para eso puedes colocar otro decorador
@app.route("/login/<name>/")
@app.route("/login/")
def login(name=None):
  print(name)
  if name is not None:
    return redirect(f"/dashboard/{name}")
  else:
    return f'<h1 style="font-size:32px; color:green;">Hola Desconocido </h1> <br> <p>Por favor igresa tu nombre en la URL</p>'


@app.route("/dashboard/<name>/")
@app.route("/dashboard/")
def dashboard(name=None):
  # print("In dashboard")
  if name is not None:
    return f"<h1>Bienvenido {name} al dashboard</h1>"
  # return redirect("/login/")
  return redirect("https://google.com")
