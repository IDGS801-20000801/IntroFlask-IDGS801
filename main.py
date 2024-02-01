from flask import Flask, render_template, request
import forms

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos", methods = ["GET", "POST"])
def alumnos():
    # titulo = "UTL"
    # nombres = ["Shava", "Alexa", "Ceci", "Armando", "Cordova"]
    # return render_template(
    #     "alumnos.html", 
    #     titulo = titulo, nombres = nombres
    # )
    alumno_clase = forms.UserForm(request.form)
    if request.form == 'POST' :
        nom = alumno_clase.nombre.data
        p_ap = alumno_clase.a_paterno.data
        s_ap = alumno_clase.a_materno.data
        edad = alumno_clase.edad.data
    
        print('Nombre {} - Primer Apellido {} - Segundo Apellido {} - Edad {} - Edad {}'
              .format(nom, p_ap, s_ap, edad))
    return render_template("alumnos.html", 
                form = alumno_clase, nom = nom, p_ap = p_ap, s_ap = s_ap)

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

@app.route("/hola")
def hola():
    return "<h1>Saludos desde Hola</h1>"

@app.route("/Saludo")
def saludo():
    return "<h1>Saludos desde Saludo</h1>"
    
@app.route("/nombre/<string:nombre>")
def nombre(nombre):
    return "Hola " + nombre

@app.route("/numero/<int:n1>")
def numero(n1):
    return "Número: {}".format(n1)

@app.route("/user/<int:id>/<string:nombre>")
def user(id, nombre):
    return "ID: {} Nombre: {}".format(id, nombre)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma de {} + {} = {}".format(n1, n2, n1 + n2)

@app.route("/default")
@app.route("/default/<string:d>")
def func2(d="Dario"):
    return "El nombre de User es: " + d

@app.route("/calcular", methods=["GET", "POST"])
def calcular():
    if request.method == "POST" :
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicación de {} * {} = {}".format(num1, num2, str(int(num1) * int(num2)))
    return '''
        <form action="/calcular" method="POST">
            <label> N1: </label>
            <input type = "text" name = "n1"><br>
            <label> N2: </label>
            <input type = "text" name = "n2"><br>
            <input type = "submit"/>
        </form>
    '''
    
@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST" :
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicación de {} x {} = {}".format(num1, num2, str(int(num1) * int(num2)))
    
if __name__ ==  "__main__":
    app.run(debug=True)