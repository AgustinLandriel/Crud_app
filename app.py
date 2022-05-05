from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from config import conexionDatabase

# En este modulo configuramos la variable de entorno

app = Flask(__name__)
app.config["SECRET_KEY"] = "clave312125315123"
app.config["SQLALCHEMY_DATABASE_URI"] = conexionDatabase
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


SQLAlchemy(app)  # inicializamos sqlalchemy en la app
app.register_blueprint(contacts)  # registramos el blueprint en la app
