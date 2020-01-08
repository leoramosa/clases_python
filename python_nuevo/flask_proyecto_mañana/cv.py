from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
# rutas
@app.route("/")
def profile():
    return "Este es mi Profile"
@app.route("/educacion")
@app.route("/educacion/<inicial>/<secundaria>/<profesional>")  # diamantes para pasarle un parametro
def educacion(inicial="sin inicial", secundaria="sin secundaria", profesional="no profesional"):
    return "Aca va mi educacion : {}</br>" \
           "mi secundaria fue:{}</br>" \
           "mi grado profesional:{}</br>" \
        .format(inicial, secundaria, profesional)
@app.route("/experiencia")
@app.route("/experiencia/<exp1>/<exp2>/<exp3>")
def experiencia(exp1="sin exp", exp2="sin exp", exp3="sin exp"):
    # listas afuera
    return "Mi Experiencia 1 fue en.-{}</br>" \
           "Mi Experiencia 2 fue en.-{}</br>" \
           "Mi Experiencia 3 fue en.-{}</br>" \
        .format(exp1, exp2, exp3)

@app.route("/referencias")
def referencia():
    contactos = ['daniel de la curz','gustavo gonzales','jonathan tecsup','armando']
    return render_template('referencias.html', lista=contactos)

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route("/plantilla/<nombre>")
def plantilla(nombre="Armando"):
    valor1 = 600 - 400
    if nombre == "Armando":
        msg = "mentor"
    else:
        msg = " no es mentor"
    return render_template("index.html", nom=msg, res=valor1)
app.run(debug=True, port=8000)