from flask import Flask, request, redirect, url_for
import requests
from flask_bootstrap import Bootstrap
from flask import render_template
from formularios import *


app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
bootstrap = Bootstrap(app)
URL_app_api = 'http://localhost:5050/'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/proyectos/")
def proyecto_lista():
    formulario = ListaProyectoForm()
    formulario.inicializar()

    url_proyecto = URL_app_api + 'proyectos/'
    respuesta = requests.get(url_proyecto).json()

    for item in respuesta:
        formulario.lista_proyectos.append(item)
        
    return render_template("proyectos.html", form=formulario)


@app.route("/componentes/")
def componente_lista():
    return render_template("componentes.html")


@app.route("/elementos/")
def elementos_lista():
    return render_template("elementos.html")


@app.route("/proyecto/", methods=["POST"])
@app.route("/proyecto/<string:id>", methods=["GET", "POST"])
def proyecto(id):

    return render_template("proyecto.html")


@app.route("/componente/", methods=["POST"])
@app.route("/componente/<string:id>/", methods=["GET", "POST"])
def componente(id):
 return render_template("componente.html")


@app.route("/elemento/", methods=["POST"])
@app.route("/elemento/<string:id>/", methods=["GET", "POST"])
def elemento(id):

    return render_template("elemento.html",)


@app.route("/proyecto/estadisticas")
def estadisticas():
    formulario = EstadisticasForm()

    url_estadisticas = URL_app_api + 'proyecto/productividad/'
    respuesta = requests.get(url_estadisticas).json()
    formulario.productividad = respuesta['productividad']
    formulario.esfuerzo_real = respuesta['esfuerzo real']
    formulario.tamanio_real = respuesta['tamaño real']
    return render_template("estadisticas.html", form=formulario)


if __name__ == '__main__':
    app.run(debug=True)