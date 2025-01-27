# # Importando la clase Flask
# from flask import Flask
# # Creando la variable de iniciación
# app = Flask(__name__)
# # Definiendo rutas
# @app.route('/')
# def index():
#     return 'Hola Mundo'

# Importando la clase Flask
from flask import Flask, render_template
# Creando función de control
def create_app():
    # Creando la variable de iniciación
    app = Flask(__name__)
    # Configuración del proyecto
    app.config.from_mapping(
    DEBUG = True,
    SECRET_KEY = 'dev_esit'
    )
    # Importando BP de toto
    from . import todo
    app.register_blueprint(todo.bp)
    # Importando BP de auth
    from . import auth
    app.register_blueprint(auth.bp)

    # Definiendo rutas
    @app.route('/')
    def index():
        return render_template("index.html")
    return app
