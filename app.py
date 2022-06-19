from flask import Flask,redirect,url_for,request

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
# @app.route("/login/<name>/")
@app.route("/login/",methods=["GET","POST"])
def login():
  # ------  USAREMOS UN FORMULARIO DE HTML PARA MANEJAR METODO POST ------------
  # print(request.method)
  if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    if username and password:
      print(username,password)
      return redirect(url_for("dashboard",name=username))     
  return """
<h3>Ingresa tus datos</h3>
      <form method="POST" style="background-color:#e6e6e6; padding:2em;">
        <input type="text" name="username" placeholder="Nombres y apellidos"/> <br/><br/> 
        <input type="password" name="password" placeholder="contraseña"/>
        <br/><br/>
        <button type="submit"> Enviar </button>  
      </form>
        """
  

@app.route("/profile/<name>/")
@app.route("/profile/")
def dashboard(name=None):
  if name is not None:
    return f"<h1>Bienvenido {name} al dashboard</h1>"
    # return f"<h1>Bienvenido al dashboard</h1>"
  # return redirect("/login/")
  return redirect(url_for("login"))
