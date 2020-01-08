#1.-utilizando la libreria de flask
from flask import Flask
from flask import request

#2.- crear una aplicacion
app = Flask(__name__)
#3.- Crear Rutas
@app.route('/')
def index():
    return "Bienvenido al 2020-Flask Python"

@app.route('/home')
def home():
    return "Bienvenido al home de mi sitio"

@app.route('/usuario')
def usuario():
    param = request.args.get('usuario','campo vacio')
    return "El usuario es:{}".format(param)

@app.route('/usuarios')
def usuarios():
    user = request.args.get('usuario','usuario no ingresado')
    clave = request.args.get('clave', 'clave no ingresado')
    return "El usuario es : {},{}".format(user, clave)

#4.- ejecutar el servidor de prueba
#app.run()
app.run(debug=True, port=8000)
